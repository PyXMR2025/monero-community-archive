---
title: Hashrate variance on Intel Arrow Lake, improved by background migrating thread
source_url: https://github.com/xmrig/xmrig/issues/3612
author: yump
assignees: []
labels: []
created_at: '2025-01-05T20:43:15+00:00'
updated_at: '2025-06-28T10:28:39+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:28:39+00:00'
---

# Original Description
On my new Intel 265K (8 P cores, 12 E cores, no SMT), I'm seeing results like this with repeated --bench=1M runs:

    117.992 seconds (8475.2 h/s)
    115.892 seconds (8628.7 h/s)
    114.032 seconds (8769.5 h/s)
    113.521 seconds (8808.9 h/s)
    112.626 seconds (8878.9 h/s)
    112.520 seconds (8887.3 h/s)
    111.918 seconds (8935.1 h/s)
    111.753 seconds (8948.3 h/s)
    111.161 seconds (8996.0 h/s)
    110.625 seconds (9039.5 h/s)

(Sorted, so it's easy to eyeball the distribution. There was no decrease-with-time evidence of heat soak before the sort.)

The machine is *extremely* quiescent. According to top -d60, `xmrig` is getting 1995% CPU out of a possible 2000%, and the balance is made up by time spent servicing interrupts.

The topology is that the P-cores have 3MiB L2, and the E-cores are in clusters of 4 with 4 MiB of shared L2, and then the whole thing has 30 MiB of L3. The best performance, so far, has been with all cores loaded up. Idling 2 threads in each E-core cluster does not seem to help.

I would like to understand this so that I can 1) know if I have a hardware problem, and 2) hopefully fix it so that I can get the high end of the distribution all the time, or at least not have to repeat the benchmark so many times to detect small perf differences between BIOS versions/settings.

----

More investigation, after the above was written:

(For scripts and detailed results, see [yump/xmrig-turbostat-anomaly](https://github.com/yump/xmrig-turbostat-anomaly). If you have an Arrow Lake, Lunar Lake, or any other Intel hyrbid CPU, please check and see if `ecore-tickler.py` improves performance on your machine.)

Found a clue on the high variance of xmrig results: turbostat running in the background at 5 Hz adds ~800 kH/s, even when all it's doing is `--show usec`.

10 hz seems to work _slightly_ better than 5 hz, but it's a negligible difference.

Doesn't work if it's not running on E-cores. Doesn't work if's running on only 1 E-core. Minimum reproducer seems to be:

    turbostat --quiet --show usec --interval 0.1 --cpu 8-19

Recorded a pair of scheduler traces of xmrig running with (good.trace.dat) and without (bad.trace.dat) the background turbostat at 20 Hz. The command to do that is:

    sudo trace-cmd record -e sched -- sleep 0.5

Analyzed as follows:

1. Open in kernelshark.
2. Filter to one cluster of E-cores with Plots -> CPU.
3. Filter out `sched_stat_runtime` events by unchecking them in Filter -> Events.
4. Zoom in on one group of pips.
5. Double click the first, to attach marker A to that one and scroll the table to the proper timestamp.
6. Swtich to marker B, and arrow-key through the table to see what's going on.

Turbostat's behavior is that it wakes on the last E-core at the beginning of the sampling interval, then migrates rapidly from e-core to e-core in sequence, starting with the first (8), presumably by setting its affinity, then goes back to sleep.

To eliminate variables, I implemented `ecore-tickler.py`, found in this same directory, which rotates its own affinity in a similar fashion, but does absolutely nothing else.

Initally, it was crashing out due to negative sleep lengths caused by wakeup latency (really, linux?). Wrapping with `sudo chrt 1` worked as a bandaid fix, but I fixed it to run without that.

Although, the tickling seems to be _very_ slightly more effective with chrt, just based on eyeballing the hashrate while mining monero.

Effect of tickling at 5 hz, perfgov:

`xmrig --bench=1M` on e-cores only, `MSR_PREFETCH_CONTROL = 0xa5`, which is 0x25 + the bit the disables the Array of Pointers prefetcher, which is locked as of BIOS 2.22.AS05. Single run, avg/peak:

* Untickled: 4992 / 6444
* Tickled : 6444 / 6457

Conducted further tests of various tickling parameters, with `xmrig --bench=1M` on all cores, `MSR_PREFETCH_CONTROL = 0x80`, which is default as of BIOS 2.22.AS05. Detailed results in `test_tickler_params_result.txt`. Summary of 5 runs:

| prio        | timing  | interval | median kH/s | peak kH/s |
| ----------- | ------- | -------- | ----------- | --------- |
| no tickling | n/a     | n/a      | 8813.7      | 8841.6    |
| realtime    | sync    | 0.2      | 9720.3      | 9854.6    |
| realtime    | sync    | 0.1      | 9882.0      | 9954.7    |
| realtime    | sync    | 0.05     | 9810.8      | 9970.5    |
| realtime    | stagger | 0.2      | 9829.4      | 9861.1    |
| realtime    | stagger | 0.1      | 9921.2      | 9999.9    |
| realtime    | stagger | 0.05     | 9894.1      | 9876.2    |
| sched_other | stagger | 0.1      | 9670.1      | 9876.2    |

"Best" appears to be realtime priority stagger at 10 Hz.


# Discussion History
## SChernykh | 2025-01-05T21:55:14+00:00
Can you run the benchmark with `--cpu-no-yield` in XMRig command line? With and without this "tickling".

## yump | 2025-01-06T13:32:54+00:00
Alas, I've been running with a `--config=` that has `"yield": false` in it this whole time, because it sounded like it might help.  I don't remember it making a noticeable difference when I put it there, but... I switched it off an on and did 5 runs of each combination of tickling x yield:

| yield | tickling      | median kH/s | peak kH/s |
| ----- | ------------- | ----------: | --------: |
| true  | no            |      8632.7 |    8943.3 |
| true  | 10 Hz stagger |      9862.4 |   10013.7 |
| false | no            |      8549.5 |    8704.4 |
| false | 10 Hz stagger |      9910.5 |    9966.4 |

If anything, yield seems *help*? It seems to be a marginal bonus to everything but the ticked median.  That gestures at something beneficial happening when threads are de-scheduled. 

New theory: The clustered L2 cache (4 MiB) is too small to hold 4 threads worth of scratchpad. If two cores get a "head start", could they force the other two threads hotter part of working set out to L3, wasting L2 space on less profitable scratchpad? In that case, the slow threads might be punished even more for having less memory traffic, in a positive feedback effect. The equillibrium could then be disrupted by the fast threads getting de-scheduled. If it snowballs slowly, that might explain the Uncomputerly Long timescale?

Experiments to try:

1. `perf stat` cache hit rate response to tickling.
2. Does tickling still help with only 1 or 2 threads per cluster?
3. Pick out some phoronix tests that are CPU-intensive, parallel, and have  long-lived threads with little blocking. See if anything else benefits from E-core tickling. Maybe y-cruncher?



## SChernykh | 2025-01-06T14:05:00+00:00
I think this is related to power management mechanism of this CPU/OS combination. It probably drops CPU speed on some cores after a while, and "tickling" prevents it. You should monitor CPU speeds on each core to check it.

## yump | 2025-01-06T19:58:32+00:00
That is, in fact, exactly what I was doing when I discovered that running `turbostat` along side xmrig made xmrig run faster. Turbostat reports the ecores holding 4600 MHz solid (like they're supposed to), and the P-cores [throttling for some reason I cannot explain](https://community.intel.com/t5/Processors/265K-mystery-throttling-resolved-by-AVX-offset-doesn-t-appear-in/m-p/1653161) to 5130. But whatever is going on *here* seems to affect the e-cores alone.  

E-cores only with background tickling ("max" number is from all cores because I edited config.json without restarting):

    [2025-01-06 13:28:55.930]  miner    speed 10s/60s/15m 6242.3 6250.2 n/a H/s max 10741.1 H/s

E-cores only, no tickling:

    [2025-01-06 13:57:16.499]  miner    speed 10s/60s/15m 5795.6 5863.2 5844.3 H/s max 5988.6 H/s

Just in case, [the test script disables voluntary freqency scaling](https://github.com/yump/xmrig-turbostat-anomaly/blob/d829f9197e48e5816540930a5c15bf4eb2ace948/test_tickler_params.bash#L27).

## yump | 2025-01-06T23:06:38+00:00
Well that's weird. Without the tickler, some of the E-cores get "stuck" in a low-IPC mode:

```
> turbostat --quiet --show CPU,Bzy_MHz,Bzy%,IPC --cpu 8-19 sleep 10
CPU     Bzy_MHz IPC
-       4601    0.97
8       4602    1.04
9       4602    0.96
10      4602    0.74 <=
11      4602    1.08
12      4601    0.99
13      4601    1.04
14      4601    0.87 <=
15      4601    1.06
16      4601    0.76 <=
17      4601    1.03
18      4601    1.03
19      4601    1.03
```

But when the tickler is running:

```
CPU     Bzy_MHz IPC
-       4601    1.03
8       4602    1.01
9       4602    1.06
10      4602    1.01
11      4602    1.07
12      4601    1.02
13      4601    1.01
14      4601    1.05
15      4601    1.05
16      4601    1.01
17      4601    1.00
18      4601    1.01
19      4601    1.01
```

Running the test repeatedly, I did catch one sample where 3 cores in the same cluster were afflicted:

```
CPU     Bzy_MHz IPC
-       4601    0.94
8       4602    1.05
9       4602    1.08
10      4602    1.04
11      4602    1.08
12      4601    1.02
13      4601    0.66 <=
14      4601    0.77 <=
15      4601    0.72 <=
16      4601    1.04
17      4601    1.03
18      4601    1.04
19      4601    0.71 <=
```

Only running 1 core per cluster was not protective:

```
CPU     Busy%   Bzy_MHz IPC
-       25.10   4601    0.94
8       99.76   4601    0.71 <-
9       0.31    4599    0.24
10      0.04    4599    0.30
11      0.14    4601    0.79
12      99.76   4601    1.06 *
13      0.55    4602    0.11
14      0.07    4602    0.16
15      0.17    4601    1.14
16      99.76   4602    1.06 *
17      0.11    4602    0.44
18      0.30    4602    0.16
19      0.19    4601    0.26
```

So, my L2 cache pressure theory is scuppered.  I guess I need to figure out how to profile the floundering cores without taking them out of the bad state ... Only thing that comes to mind is *extremely* slow sample rate.

## ValeZAA | 2025-01-09T21:10:38+00:00
> I think this is related to power management mechanism of this CPU/OS combination. It probably drops CPU speed on some cores after a while, and "tickling" prevents it. You should monitor CPU speeds on each core to check it.

Downgrade Intel ME and downgrade BIOS to 0x110 ucode. So far all updates Intel did were degrading the speed, future Intel ME 2.4 will be better:

![image](https://github.com/user-attachments/assets/c89dc7e5-7cbf-40d5-bd27-a28e8407249d)


## ValeZAA | 2025-05-16T14:10:11+00:00
Hey, any updates for kernel 6.14 in particular?

# Action History
- Created by: yump | 2025-01-05T20:43:15+00:00
- Closed at: 2025-06-28T10:28:39+00:00
