---
title: XMRig v2.16.0-beta cannot mine randomwow on Xeon v2
source_url: https://github.com/xmrig/xmrig/issues/1048
author: nutsnox
assignees: []
labels: []
created_at: '2019-07-01T05:36:22+00:00'
updated_at: '2019-07-12T15:39:31+00:00'
type: issue
status: closed
closed_at: '2019-07-09T14:02:10+00:00'
---

# Original Description
Just started trying to mine Wownero (randomwow) with an ivy bridge xeon and it will only report n/a H/s:

I ran 2.15 beta from SChernykh's github and it does the same thing - it looks like it's spooling the threads but never finishes. This identical config (with different thread config of course) works perfectly on all of my AMD boxes.

# Discussion History
## Spudz76 | 2019-07-06T18:53:31+00:00
I have been running it on Linux on Sandy and Ivys and all work great.

I have been unable to get the Windows one to compile, much less work.

## x151973 | 2019-07-08T02:30:03+00:00
"low_power_mode": 1

## Spudz76 | 2019-07-09T05:16:29+00:00
Yeah, that's one thing, anything but single thread doesn't work, if that's what you were doing.
Use double-single-threads like affined to same core but lpm:1 still if you need to use more cache.

Example my config from [E5-2620](https://ark.intel.com/content/www/us/en/ark/products/64594/intel-xeon-processor-e5-2620-15m-cache-2-00-ghz-7-20-gt-s-intel-qpi.html) which is 'Sandy Bridge EP' with 15M cache:
```
    "threads": [
        {
            "low_power_mode": 1,
            "affine_to_cpu": 6,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 6,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 7,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 7,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 8,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 8,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 9,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 9,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 10,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 10,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 11,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 11,
            "asm": true
        }
    ],
```

## nutsnox | 2019-07-09T06:29:57+00:00
If i use CPU affinity I can get one CPU to hash but the other will not. If I simply assign all threads to their physical/HT cores then it won't hash; however, if I look at the NUMA structure and assign threads accordingly to CPU 0 then it hashes as I'd expect a single CPU to hash.

Weird?

## nutsnox | 2019-07-09T14:02:10+00:00
I had to disable NUMA to get this to work. Now it hashes about like it should. Thanks!

## Spudz76 | 2019-07-09T15:47:05+00:00
Strange, pretty sure I'm using NUMA (but again, Linux)

## nutsnox | 2019-07-09T18:01:14+00:00
I'm also on Linux (ubuntu 16.04 server)

## Spudz76 | 2019-07-09T19:52:06+00:00
Very strange, could be BIOS related then (bad ACPI tables, leading to failed NUMA mapping) which is somewhat common.

Mine are Supermicro X9SRL or X9DRL with latest bios.

Sometimes the OEM goofs up the ACPI information for what's wired to what, or it is not quite in the absolute correct format (Windows may workaround what Linux takes literally).

Apologies for assuming this was Windows somehow (most windows users don't mention any OS while usually Linux users definitely mention using Linux cuz it's cool like cigarettes).

## Spudz76 | 2019-07-09T19:53:42+00:00
Oh and also the no-hashrate bug is what I have on Windows no matter what with randomx

So that played a part in assuming it was Windows

I have not seen the same no-hashrate thing on any Linux (even crappy non-AES cpus...)

## Spudz76 | 2019-07-09T19:55:18+00:00
But, this could expose the same vector for that bug probably.  Some hw mapping thing.

RandomX does have an alternate hugepages / allocation method, different completely from the regular one for the rest of the supported algos.  (note there is no more hugepages message at startup, when in rx/wow mode)

## Spudz76 | 2019-07-09T19:56:09+00:00
Are you dual-cpu? or just single with HT...?

## Spudz76 | 2019-07-09T20:03:21+00:00
NUMA mode may require more hugepages in the sysctl, I did have it fail on some that were still set to only 4.  Some miners suggest 128 and I think that works, but some RandomX related one suggested like 1280 which seems extreme, but also works.

I may have had one do a zero hashrate until I got the `vm.nr_hugepages` large enough and working.  It doesn't seem to error out like the other algos when failing to setup memory in some cases (uncaught fail vectors?)

## Spudz76 | 2019-07-09T20:10:43+00:00
There is also a `ulimit -l` for max memory allocation, that may need expansion compared to CN algos.

RandomX needs 2080MB before it even begins with the scratchpads, so a 4GB total RAM box might be tight.  I run some thin spec miners since CN really doesn't care, and still can do RandomX (wow) on 4GB but it's pretty stripped out and headless (memory usage for other-than-mining minimized).

The other RandomX based coins may use 2MB scratchpads and overflow 4GB ram though.  RX-Wow is using 1MB scratchpads like CN-Lite does, saving some memory.  But the 2080MB thing is constant regardless of scratchpad sizing or coin options/tweaks/mods.

## nutsnox | 2019-07-09T23:30:19+00:00
This is a pair of Quanta Windmills each with dual e5-2650L v2 CPU's - it wasn't even hashing before and I don't know if I'm leaving performance on the table by disabling NUMA (would be interested to know of course). Currently they are doing about 6.3KH for the pair which is ABOUT what I'd expect... not bad for two 70w TDP CPU's.

This isn't the first time I've run into issues with XMRIG and NUMA. In working on some quad-CPU opteron servers I'd run into similar problems (though those would ultimately hash on SOME level, whereas in this scenario it all simply fell flat on its face).

Additional specs:
dual 2650L v2
16GB (4x4GB) per node
USB stick flash drive.

## Spudz76 | 2019-07-12T15:39:31+00:00
It's not so much limited to xmrig, I know of similar issues in xmr-stak with libhwloc (which eventually also probes NUMA when enabled).  But it is always from some bad ACPI tables in the BIOS of whatever board the OEM didn't bother to make perfect.  ACPI tables are touchy and can "work" sort of like a badly coded HTML page, Windows will guess or assume, Linux will usually detect this isn't spec and drop it.  Like IE vs Chrome parsing a not-quite-perfectly-formatted HTML file.

I do run a whole bunch of Quanta (Dell) C1100 cloudservers and I think they have been OK, but don't mine on them so I'm not sure if it has the same sort of problems.  But they are also single proc and so there should be everything on one NUMA-node anyway (NUMA pointless on single processor / simple memory map).

Definitely never had a Quad to try out, but would imagine the more devices to properly describe in the ACPI tables the more room for the OEM to goof up on building the map, so that NUMA could use it correctly.  I think since Windows is what may of them design toward and test with, once it "works" there they think Linux will love it too (but it probably won't).  Same as webdevs checking their junk code with IE and then calling it done (while nothing works over on Chrome, etc) - which is 90% of US/Local Gov websites for example.  So bad to the point I don't even try those type of sites with anything else and just assume they are IE only.  And the same thing happens with ACPI tables.

Linux does let you overlay a custom ACPI table, if you dump the one from the BIOS and edit it to make it correct and Linux compatible, that could allow NUMA to map properly.  There should be some ACPI debug that can be turned on with kernel args which will then actually mention the parts of the tables it doesn't understand correctly (and what workaround was chosen, if any).

I have had to hack ACPI on some old laptops, they seem to have the worst sloppy tables sometimes (extra cheap HP windows laptop, that came with windows on it, but I flattened and installed Linux on day1, but it definitely wasn't designed for that, etc).

# Action History
- Created by: nutsnox | 2019-07-01T05:36:22+00:00
- Closed at: 2019-07-09T14:02:10+00:00
