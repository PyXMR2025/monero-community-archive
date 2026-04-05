---
title: XMRig 5.1.1 system hangs
source_url: https://github.com/xmrig/xmrig/issues/1392
author: heavyarms2112
assignees: []
labels: []
created_at: '2019-12-06T15:27:45+00:00'
updated_at: '2021-04-12T15:11:08+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:11:08+00:00'
---

# Original Description
**Describe the bug**
system hangs, locksup after sometime while running xmrig 5.1.1 with yield option (default on)

**To Reproduce**
Re-ran miner thrice.

Miner v5.0.0  runs fine multiple nights since fork with same settings.




# Discussion History
## heavyarms2112 | 2019-12-06T15:29:17+00:00
let me know if I can enable some debug logging and provide those.

## champmine | 2019-12-07T13:54:19+00:00
same here, Ryzen 1600 platform miner dies sporadically after a few hours

## list1999 | 2019-12-08T10:03:01+00:00
also on ryzen 1600 the program closes after a random number of hours, if you do an automatic start again - the computer freezes

## heavyarms2112 | 2019-12-08T18:38:35+00:00
I updated the BIOS on the board on x399 (which states better RAM stability support).  cpu is threadripper 1920x.  Also, I loosened some memory timings.  Is 5.1.1 more taxing on the memory vs 5.0.0?  If so perhaps my previous memory settings might not be stable.

Anyways, I am able to run overnight without hangups so far.

## BradT7 | 2019-12-10T18:22:18+00:00
I'm also having the same issue with Ryzen 2600X, I've been running XMRig for over 6 months on this CPU setup with no freezing issues until I upgraded from 5.0.1 to 5.1.1
System will randomly hard lock and become unresponsive until a reboot. Has been happening about twice a day so far. Yield option also turned on.
Also a side note, I get much better hash rates running only 6 threads rather than 8, on 0,2,4,6,8,10 (~3950 h/s)

## heavyarms2112 | 2019-12-10T18:33:27+00:00
@BradT7 I get 4K+ on Ryzen 2600 with 8 threads and clocks at 3.4-3.5 Ghz.

## BradT7 | 2019-12-10T19:48:40+00:00
System just froze again, I've dropped back to 5.0.1 for now and expect it to run with no issues (as it has with the same settings for months) until next update. 
Getting around 4K now with 6 threads (only get around 3.6K with 8 threads, 7 threads is no better either for me). 
Running at 3.8 GHz with all the default built in Asus auto overclocking settings (again this has been the norm. for months now with no hard locks) and 16GB of 2933MHz memory.
The only other thing that changed is I recently updated Windows 10 to 1909 around the same time as the update to 5.1.1 and did a BIOS update to the latest a few days before updating to 5.1.1. 
If I run 5.0.1 for the next few days with no issues then I will have to assume it's something with the code change from 5.0.1 to 5.1.1. I'll post back in a few days with stability results on 5.0.1 again.
If you'd like any further system details or configurations please let me know.

## BradT7 | 2019-12-12T20:32:56+00:00
Just providing an update to system locks, same issue happened with 5.0.1 after about a day, then I remembered I recently enabled CPU virtualization for use with Docker. I've since disabled virtualization and uninstalled Docker (and just ran Pi-hole on a dedicated Linux box now).
No more freezing so far.
I'm going to be running the recent 5.2 update going forward, but I really believe the lock up was due to CPU virtualization being enabled (I'm running multiple other identical boxes without CPU virtualization and they never had any of the recent hard lock issues).
Hopefully that helps some others that might be having lock up issues with these newer 5.x versions.
Perhaps future versions could look into this possible issue with CPU virtualization being enabled, and hard locking this system. Board is ASUS PRIME B450M-A/CSM running latest BIOS 2006
If anyone would like me to continue to test mining with CPU virtualization enabled again with newer xmrig versions let me know, otherwise I expect this work around solution to be valid for me (but perhaps not valid for others) and it will remain off by default going forward.

## bluedalmatian | 2020-12-07T18:13:24+00:00
Can confirm this still causes a problem on XMRig 6.5.3 (Ryzen 3950X)

## BradT7 | 2020-12-07T21:11:09+00:00
Hey, I think my issue ended up being memory related using Corsair stock settings.
I ended up using DRAM Calculator for Ryzen along with Thaiphoon Burner to find out my memory die type.
After setting my memory configuration manually in the BIOS to match that of DRAM Calculator I was fine after that!
Haven't had any issue since, and also had a huge increase in my hash rate as well!

# Action History
- Created by: heavyarms2112 | 2019-12-06T15:27:45+00:00
- Closed at: 2021-04-12T15:11:08+00:00
