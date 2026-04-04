---
title: unable to obtain and/or process more than 40 new blocks per day
source_url: https://github.com/monero-project/monero/issues/8144
author: nkinnan
assignees: []
labels: []
created_at: '2022-01-16T20:26:52+00:00'
updated_at: '2022-01-26T06:56:01+00:00'
type: issue
status: closed
closed_at: '2022-01-25T23:38:27+00:00'
---

# Original Description
This is on a pi 4 with 4 gb ram running https://github.com/monero-ecosystem/PiNode-XMR with usb ssd.  The monerod build is obtained via "git clone --recursive -b $RELEASE https://github.com/monero-project/monero.git" according to the scripts.  Stats dump after 20 hours from the web portal:

```
  Monero Version: 0.17.3.0-release
  Node Status: OK
  Busy Syncing: false
  Current Sync Height: 2537680
  P2P Outgoing Connections: 2
  P2P Incoming Connections: 7
  RPC Connections Count: 1
  Network Type: mainnet
  TX Pool Size: 0
  White Peerlist Size: 1000
  Grey Peerlist Size: 4999
  Update Available: false
```

Three log dumps from this 20 hour long run, the first showing startup behavior, the second after 12 hours, and the last after 20 hours.  At the 12 and 20 hours marks, I had obtained 20 blocks each for a total of 40 blocks over 20 hours.
[bitmonero_startup.log](https://github.com/monero-project/monero/files/7877817/bitmonero_startup.log)
[bitmonero_12hrs_tail.log](https://github.com/monero-project/monero/files/7877819/bitmonero_12hrs_tail.log)
[bitmonero_20hrs_tail.log](https://github.com/monero-project/monero/files/7877820/bitmonero_20hrs_tail.log)

* The network appears healthy (AFAICT) with multiple connected nodes in state "syncronizing"
* The usb ssd tests out with 200/230 write/read MB/s and I don't see issues in dmesg 
* It does see new top block candidates in the logs, it just either doesn't seem to get them, or fails to process them
* The SSD is constantly being accessed, here's a top listing, I'm not sure how to get ssd stats?
```
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
16975 pinodex+  20   0  761044 310000    556 S  58.6   7.9 737:05.73 monerod
```
* I don't have anything special on my network, just a dd-wrt flashed router that does dhcp and upnp
* The blockchain was obtained using the windows monero core wallet "monero-gui-v0.17.3.0" and transferred to the pi via sftp.  I have transferred the blockchain three times after syncing it to top with the desktop software.  The desktop and the pi monerod are always shut down before and during transfer.  The desktop software has no issues with the blockchain and the pi does at least occasionally add new blocks, just at far slower than realtime speed.
* It syncs ***significantly*** faster if I let it go from scratch, but would take weeks to get the full chain due to the pi's lack of grunt
* The usb ssd is formatted as EXT4 and attached to a mount point that holds the blockchain data only
* I have tried this across two completely fresh sets of hardware (pi, ssd enclosure, ssd) and across multiple installs to the SD card and blockchain copies
* I've started this node without p2pstate.bin using defaults, deleted p2pstate.bin and pointing to a known good node with --seed-node option, and with a copy of my desktop p2pstate.bin (desktop has no issues syncing).  

Any idea where I can look to debug further?  If I need a new build it'd be a lot easier for me to grab one via GIT if available than to rebuild on the pi.  I'm a windows dev without a lot of linux experience but will give it my best if needed.

# Discussion History
## selsta | 2022-01-16T20:37:20+00:00
The problem is that the Raspberry doesn't support hardware AES, so everything will be extremely slow. Now 40 blocks per day sounds wrong, as far as I know people can run nodes on Raspberry fine and we get 720 blocks per day.

Can you run "status" and "sync_info" on your raspberry and post the output here?

## nkinnan | 2022-01-16T20:44:18+00:00
> Can you run "status" and "sync_info" on your raspberry and post the output here?

How would I do this?  Telnet to the RPC port?  Is there a binary to use?  I tried monerod --status but it spit an error.

## nkinnan | 2022-01-16T22:35:07+00:00
After days of banging my head against the wall trying to solve this, out of desperation I tried the steps here https://forums.raspberrypi.com/viewtopic.php?f=28&t=245931 to downgrade from UAS to mass-storage protocol for the external SSD enclosure.

Although I had no dmesg lines indicating problems with UAS, I am now syncing > 10 blocks per minute, the SSD enclosure light is no longer constantly lit up, I have 3x the number of peers (this must have been seriously hurting my perf in general, not just disk speed), and the monero log file is filling up perhaps 50x faster than before, and checkpointing takes < 1 second instead of 20.

Hopefully this helps someone else.

## tcoza | 2022-01-23T22:42:21+00:00
Can we reopen this issue please? I'm having the exact same problem, except for me @nkinnan's solution did not work. I need help debugging this.

## selsta | 2022-01-23T22:46:33+00:00
@tcoza do you also use a Raspberry?

seeing that @nkinnan issue wasn't related to monero software there isn't much we can do

## tcoza | 2022-01-23T23:08:43+00:00
@selsta Yes, it's almost the exact same thing. Raspberry Pi 4, 4GB memory, external SSD. And the syncing is VERY slow, i.e. slower than the monero block rate, which makes running a node impossible. I actually asked first on Stackexchange before I found this issue, you can take a look here for details: https://monero.stackexchange.com/questions/13472/monerod-synchronization-so-slow-it-cant-catch-up-to-blockchain-on-raspberry-pi

Edit: Also, I just ran a test and I can attest that the SSD's read speed is about 30 MB/s and the write speed is well over 100 MB/s. The network's speed (Ethernet) is at least 10 MB/s. It has to be something else.
Edit 2: On second thought, I might have measured the SSD read speed using a fallacious method. I remeasured using a better method and it seems to be about 1.5 GB/s. See my comment below for more details.

## nkinnan | 2022-01-24T04:08:18+00:00
@tcoza Given your read/write speeds seem out of whack (and low for a SSD) is it possible you didn't apply the fix correctly?  What is the output of the command "dmesg | grep usb-storage"?

## tcoza | 2022-01-24T04:15:58+00:00
I did apply it correctly here's the relevant output:

```
[    6.263707] usb 2-2: UAS is blacklisted for this device, using usb-storage instead
[    6.263715] usb-storage 2-2:1.0: USB Mass Storage device detected
[    6.269678] usb-storage 2-2:1.0: Quirks match for vid 0bc2 pid 203c: 800000
[    6.270931] scsi host0: usb-storage 2-2:1.0
[    6.271273] usbcore: registered new interface driver usb-storage
```

Also I know something changed because now `monerod` says that the blockchain is on a rotating drive "consider using an SSD". Why do you think it's out of wack? Perhaps I didn't measure it correctly. I remeasured the read speed with a method that makes more sense, it seems that the read speed is actually in the GB/s. Just so you know, I measured both the read and write speeds using the `time` utility and outputting `/dev/zero` into a file on the drive (for write), and then outputting that file into `/dev/null` (for read).

## nkinnan | 2022-01-24T04:50:53+00:00
@tcoza Yes that looks correct.  Unfortunately I "got nothin" then.  Anecdotally I was getting excellent read/write speeds before I disabled UAS (and still decent but lower speeds after applying the fix) so raw sequential r/w doesn't seem connected to the issue I experienced.  Probably something to do with access patterns causing UAS failures and retries, thus hogging the CPU, at least in my case.  Not sure I can help any further but UAS doesn't appear to be your issue.  I'd look at heat and power but that's just a guess for lack of any deeper insight.  Good luck!

## tcoza | 2022-01-24T04:56:26+00:00
@nkinnan I replaced the pre-installed Raspberry Pi OS with an Ubuntu Server for Pi image, by the way. It's probably not relevant, but I think I should mention it, given that in your case, you probably kept Raspberry Pi OS (from lack of you saying otherwise). Also, my SSD's filesystem isn't ext4, but exfat.

## nkinnan | 2022-01-24T05:02:39+00:00
@tcoza In that case, two more suggestions.  I'm using PiNodeXMR on top of a raspbian image (with EXT4 for the SSD).  You might try your luck with that, it's here on github and provides a web interface and configuration help.  https://github.com/monero-ecosystem/PiNode-XMR

Also, the Pi can't do more than about an amp on the 5v USB-3 ports (the blue ones) so if your SSD is rated at more than 5 watts, that could theoretically cause issues due to power droop, or cause SSD device resets or something.  Worth checking.

If none of that works, try a different power supply.  You need at least 3 amps.

## tcoza | 2022-01-24T20:29:11+00:00
@selsta Should I send you the "status" and "sync_info" outputs?

## selsta | 2022-01-24T20:30:48+00:00
I can take a look if you post them here

## tcoza | 2022-01-24T20:48:37+00:00
@selsta 
`status`: `Height: 2543358/2544464 (99.9%) on mainnet, not mining, net hash 3.30 GH/s, v14, 11(out)+0(in) connections, uptime 0d 0h 6m 51s`
`sync_info`:
```
Height: 2543358, target: 2544464 (99.9565%)
Downloading at 63 kB/s
11 peers
212.12.30.145:18080       0000000000000000  before_handshake  0         0  0 kB/s, 0 blocks / 0 MB queued
90.64.198.32:18080        86c67315fb82dc8f  synchronizing     0         2544464  7 kB/s, 0 blocks / 0 MB queued
90.241.174.216:18080      61931a67e870d39c  synchronizing     0         2544464  7 kB/s, 0 blocks / 0 MB queued
95.111.227.54:18080       226c4769f4b61f74  synchronizing     0         2544464  7 kB/s, 0 blocks / 0 MB queued
85.215.92.77:18080        627c53625a88c962  synchronizing     0         2544464  7 kB/s, 0 blocks / 0 MB queued
110.172.104.62:18080      10de9b52a30e00d8  normal            0         1  0 kB/s, 0 blocks / 0 MB queued
83.97.20.234:18080        e08bf1b224ac510a  synchronizing     0         2544464  7 kB/s, 0 blocks / 0 MB queued
185.64.106.226:18080      57d82fe2a781c8be  synchronizing     0         2544464  7 kB/s, 0 blocks / 0 MB queued
59.66.168.34:18080        a6b46a2866d86cd3  synchronizing     0         2544464  7 kB/s, 0 blocks / 0 MB queued
98.255.252.239:18080      b82d1e2adc8cba79  synchronizing     0         2544464  7 kB/s, 0 blocks / 0 MB queued
45.15.16.99:18080         c4ced3b078fef58c  synchronizing     0         2544464  7 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]
```

## selsta | 2022-01-24T21:24:25+00:00
Can you delete your log file, start monerod with

--log-level 1,*queue*:DEBUG,*p2p*:DEBUG

and then wait a couple minutes and upload the logs here?

## moneromooo-monero | 2022-01-24T21:34:17+00:00
github mangled the stars, so:

--log-level 1,\*queue\*:DEBUG,\*p2p\*:DEBUG

## tcoza | 2022-01-24T21:56:50+00:00
@selsta @moneromooo-monero I uploaded it to Google Drive because it is quite a large amount of text: https://drive.google.com/file/d/1ix_KDRQafdDxjKNHF59H3vUlNih2y20p/view?usp=sharing

## moneromooo-monero | 2022-01-24T22:15:04+00:00
Try adding --disable-dns-checkpoints and use these log settings:

--log-level 1,*queue*:DEBUG,*p2p*:DEBUG,net.cn:DEBUG

## selsta | 2022-01-24T22:16:36+00:00
`--log-level 1,*queue*:DEBUG,*p2p*:DEBUG,net.cn:DEBUG`

## tcoza | 2022-01-24T22:22:37+00:00
@selsta  @moneromooo-monero Here's the log file for that: https://drive.google.com/file/d/1A6QlpfKxnlj9g7NdF3OxWB-2lVZdgKQB/view?usp=sharing

## moneromooo-monero | 2022-01-24T22:39:52+00:00
Now run with --log-level 1, wait for the first time "BLOCK SUCCESSFULLY ADDED" gets printed, then every 5 seconds or so, run this:

```
pstack `pidof monerod` > /tmp/monerod-stack-$(date +%s)
```

Once it prints "BLOCK SUCCESSFULLY ADDED" a second time:

tar cfvz /tmp/monerod-stacks.tar.gz /tmp/monerod-stack-*

and upload  /tmp/monerod-stacks.tar.gz

## moneromooo-monero | 2022-01-24T22:41:20+00:00
During that time, you can also leave "sudo perf top -a" running and after letting it settle for a couple dozen seconds after the first "BLOCK SUCCESSFULLY ADDED", post the contents of the screen.

## moneromooo-monero | 2022-01-24T22:42:22+00:00
Also the output of top between the two "BLOCK SUCCESSFULLY ADDED" lines, esp the third line.

## tcoza | 2022-01-24T22:43:12+00:00
> Now run with --log-level 1

Do I keep `--disable-dns-checkpoints`?

## moneromooo-monero | 2022-01-24T22:47:46+00:00
Doesn't matter here.

## tcoza | 2022-01-24T22:50:05+00:00
@moneromooo-monero I don't seem to have `pstack` installed. `apt install pstack` says it can't find the package. I'm going to try to install it somehow and get back to you.

Edit: Could it be that pstack isn't available on `aarch64` architecture?

## moneromooo-monero | 2022-01-24T22:56:38+00:00
It ships with gdb AFAICT. Do you have that installed ?


## tcoza | 2022-01-24T22:59:46+00:00
Well, I just installed `gdb` and I still don't have `pstack`. No, on my laptop, it says that I have to install the `pstack` package, but on the Raspberry Pi it says:
```

Command 'pstack' not found, did you mean:

  command 'jstack' from deb openjdk-11-jdk-headless (11.0.13+8-0ubuntu1~20.04)
  command 'jstack' from deb openjdk-16-jdk-headless (16.0.1+9-1~20.04)
  command 'jstack' from deb openjdk-17-jdk-headless (17.0.1+12-1~20.04)
  command 'jstack' from deb openjdk-8-jdk-headless (8u312-b07-0ubuntu1~20.04)
  command 'jstack' from deb openjdk-13-jdk-headless (13.0.7+5-0ubuntu1~20.04)
  command 'stack' from deb haskell-stack (1.9.3.1-1)

Try: sudo apt install <deb name>
```

Is there an alternative? I can still try to search for a way to make that command available.

## moneromooo-monero | 2022-01-24T23:06:27+00:00
gdb \`pidof monerod\`
cont

then every 5 seconds:

^C

thread apply all bt

cont



It's just more annoying to do manually.


## moneromooo-monero | 2022-01-24T23:08:02+00:00
(start gdb that way after you started monerod)

## tcoza | 2022-01-25T00:08:33+00:00
@moneromooo-monero All right, it's been quite a while but I finally did it. I replaced the `pstack` command with
`gdb -batch -ex 'thread apply all bt' -p `pidof monerod` > /tmp/monerod-stack-$(date +%s)`
I hope you approve. I uploaded the tar.gz on Google Drive: https://drive.google.com/file/d/11aNRQjE7V5XYNOwaF6CiQrHnizu8tGkq/view?usp=sharing
And here's the `perf` screenshot:
![image](https://user-images.githubusercontent.com/4213839/150885748-58a713e3-a685-4dad-bce8-106d48df1aad.png)


## moneromooo-monero | 2022-01-25T08:46:19+00:00
This is all pointing to your disk I/O being horrendous. Also possibly your CPU being slow. You'll likely have a high %wa field in top.
monerod also blocks in its P2P code since it needs blockchain data to know what to request next, but blockchain data is locked by the very slow (due to disk I/O) block verification. So: slow disk, and code that is not optimized for slow accesses. Someone mentioned (again) they might look at a rw lock for chain access, which would likely fix a lot of the wait for chain data in the P2P code. Meanwhile, all your traces show the logger stuck writing logs, --log-file /tmp/monerod.log might help speed things up (and possibly --max-log-files and --max-log-file-size so you don't fill /tmp up).

## tcoza | 2022-01-25T18:09:30+00:00
But how can it be the disk I/O? It is an SSD, and I recorded write speeds at >100 MB/s, and read speeds at 1.5 GB/s. Plus, it absolutely CANNOT be the physical disk itself, because I used the same disk to synchronize on my laptop and `monerod` was synchronizing just fine. So might it be a problem with the driver? Also, it is possible that a lot of the traces show log writing because the log level was pretty high. Perhaps it wouldn't show that at log level zero.

## moneromooo-monero | 2022-01-25T20:23:21+00:00
Well, maybe not the disk but the I/O circuitry in your Pi. Or maybe you got bad luck with those traces and they're not representative. You still haven't posted the top output, which will show the %wa.

## tcoza | 2022-01-25T20:31:24+00:00
@moneromooo-monero I don't know what that means, can you tell me the command? Also, tell me how to measure disk I/O speed. Tell me a way that doesn't involve `monerod`, and that would indicate that disk I/O on my Pi is subpar.

The way I measured it until now was to measure the time it took to write `/dev/zero` to the disk, and read back that file into `/dev/null`. Is that an accurate method? What other method would reveal that the disk is slow?

## moneromooo-monero | 2022-01-25T20:39:59+00:00
top

For benchmarking I/O, I can't help. Search the web. But for monero you want random access, not raw sequential throughput.

## tcoza | 2022-01-25T20:43:30+00:00
@moneromooo-monero Ok, so you're saying it's the random access that might be slow, not the sequential access. Do you think the type of filesystem on my drive might affect that somehow? My filesystem type is `exfat`.

Also, for the `top` command, the `wa` field is showing about `74.3` while `monerod` is running. Is this what you're referring to?

## tcoza | 2022-01-25T21:42:33+00:00
@moneromooo-monero I benchmarked random I/O on the SSD using the `sysbench` utility and I got the following results (partial output):
```
Throughput:
    read, MiB/s:                  3.80
    written, MiB/s:               2.53
```
Do you think this is too slow?

Edit: @nkinnan Can you run the benchmark test on your Pi and send me your results for comparison, please? The commands I ran are the following (install `sysbench` first):
```
mkdir Benchmark                     # Somewhere on the SSD
cd Benchmark
sysbench fileio prepare
sysbench fileio --file-test-mode=rndrw run
``` 

Edit 2: I ran the `sysbench` test on the same SSD on my laptop (where `monerod` works perfectly fine), and it gave even worse results (2.63 read and 1.76 write). @moneromooo-monero Still think slow disk I/O is the problem?

## moneromooo-monero | 2022-01-25T22:22:46+00:00
With the logs you posted, yes.

## moneromooo-monero | 2022-01-25T22:23:12+00:00
Or some filesystem or I/O code in the middle.

## tcoza | 2022-01-25T22:23:55+00:00
But then how do you explain the benchmark results?

## moneromooo-monero | 2022-01-25T22:25:42+00:00
I do not. But AFAICT they're both shit. A SSD should be able to read way more than 3 MB per second.

## moneromooo-monero | 2022-01-25T22:26:39+00:00
I had missed your previous comment. 74 in %wa is massive. You're spending your time in I/O.

## selsta | 2022-01-25T22:26:46+00:00
@tcoza did you try using ext4 with the same config as @nkinnan?

## tcoza | 2022-01-25T22:27:49+00:00
@selsta I guess that's the next thing I'm going to try. I will also try that XMR node OS.

## tcoza | 2022-01-25T23:13:03+00:00
> I had missed your previous comment. 74 in %wa is massive. You're spending your time in I/O.

By the way, `top` also consistently shows `monerod` as using 99%-100% of the CPU. @moneromooo-monero 

## tcoza | 2022-01-25T23:23:11+00:00
UPDATE: I have created another partition on the SSD and formatted it as `ext4`. `monerod` now synchronizes at a decent speed! The node is up to date.
Personally, I don't mind reformatting my SSD as `ext4` to run the node. But this is still very strange. Were there any contraindications to using `exfat`? And why is `exfat` only a problem on the Raspberry Pi? I think this has to be looked into.

## selsta | 2022-01-25T23:25:22+00:00
some driver bug? no idea, but this isn't anything we can fix on monero's side

## tcoza | 2022-01-25T23:29:20+00:00
@selsta All right. Then it's probably not a Monero issue. Nevertheless, I can't make heads or tails of this, but at least I got my node running. Should we close the issue?

## hyc | 2022-01-25T23:38:27+00:00
On most Linux distros exFAT is supported by a FUSE driver, not an actual in-kernel filesystem driver. So at best it will always be 2-3x slower than a native filesystem. ext4 is of course a native filesystem.

## tcoza | 2022-01-26T06:03:48+00:00
> On most Linux distros exFAT is supported by a FUSE driver, not an actual in-kernel filesystem driver. So at best it will always be 2-3x slower than a native filesystem. ext4 is of course a native filesystem.

Yeah, that explanation would be more satisfying if `monerod` didn't run perfectly fine on my Linux laptop on that same `exfat` SSD but whatever.

Thank you all for helping me out, really appreciate it.

## nkinnan | 2022-01-26T06:56:01+00:00
Your laptop has a lot more CPU grunt :)

# Action History
- Created by: nkinnan | 2022-01-16T20:26:52+00:00
- Closed at: 2022-01-25T23:38:27+00:00
