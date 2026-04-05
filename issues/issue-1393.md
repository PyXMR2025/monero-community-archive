---
title: Speed dowm problem
source_url: https://github.com/xmrig/xmrig/issues/1393
author: alexblock2019
assignees: []
labels:
- stability
created_at: '2019-12-07T01:24:59+00:00'
updated_at: '2020-08-31T05:48:16+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:48:16+00:00'
---

# Original Description
Hello，I found another problem。
I don't know is win10 or Ryzen bug？
System version win10 1903
Both Ryzen 2600 and 3700x encountered this problem
 
log info：（Removed mining pool information）

[2019-12-07 03:46:07.280] speed 10s/60s/15m 7235.8 7465.3 7609.8 H/s max 9244.0 H/s
[2019-12-07 03:47:07.310] speed 10s/60s/15m 6854.6 7103.2 7535.9 H/s max 9244.0 H/s
[2019-12-07 03:47:36.168]  cpu  accepted (3914/0) diff 120001 (12 ms)
[2019-12-07 03:48:07.340] speed 10s/60s/15m 64.9 1018.8 7121.2 H/s max 9244.0 H/s
[2019-12-07 03:49:07.373] speed 10s/60s/15m 26.7 118.6 6628.2 H/s max 9244.0 H/s
[2019-12-07 03:50:07.404] speed 10s/60s/15m 17.2 107.7 6121.9 H/s max 9244.0 H/s
[2019-12-07 03:51:07.439] speed 10s/60s/15m 66.8 116.7 5608.3 H/s max 9244.0 H/s
[2019-12-07 03:52:07.475] speed 10s/60s/15m 94.5 144.4 5100.8 H/s max 9244.0 H/s
[2019-12-07 03:53:07.510] speed 10s/60s/15m 23.5 144.6 4604.7 H/s max 9244.0 H/s
[2019-12-07 03:54:07.546] speed 10s/60s/15m 102.1 144.6 4090.5 H/s max 9244.0 H/s
[2019-12-07 03:55:07.584] speed 10s/60s/15m 92.7 144.3 3590.3 H/s max 9244.0 H/s
[2019-12-07 03:56:07.626] speed 10s/60s/15m 86.0 144.4 3088.2 H/s max 9244.0 H/s
[2019-12-07 03:57:07.670] speed 10s/60s/15m 82.3 144.9 2581.3 H/s max 9244.0 H/s

# Discussion History
## SChernykh | 2019-12-11T08:25:05+00:00
@jindyzhao When this happens next time, can you check CPU and memory usage in task manager?

## saltednutz825 | 2019-12-19T02:03:46+00:00
I got the exactly same problem a lot, namely a lot.
on both my 1700 and 2600x rigs.

## SChernykh | 2019-12-19T06:12:22+00:00
@seamushroom54 Can you check in task manager, what uses CPU and memory - what % goes to XMRig and what % goes to something else (if anything).

## SChernykh | 2019-12-19T06:13:06+00:00
Can you also press `h` to print full hashrate report when this happens?

## saltednutz825 | 2019-12-19T06:13:40+00:00
I will check when it happends again.

## alexblock2019 | 2019-12-19T07:41:21+00:00
> Can you also press `h` to print full hashrate report when this happens?

yes，print speed very low or Na.
task manager show 100% CPU usage and Normal memory useage.
But the processor temperature is much lower than normal,I suspect it is a problem with high temperature operation

## alexblock2019 | 2019-12-19T07:44:27+00:00
> @seamushroom54 Can you check in task manager, what uses CPU and memory - what % goes to XMRig and what % goes to something else (if anything).

But as long as I restart the miner, everything returns to normal.
And I found an interesting phenomenon. If you do not connect to the monitor and use TeamViewer for remote operation, this problem will occur very likely.

## SChernykh | 2019-12-19T07:48:10+00:00
Can you make the screenshot of miner window with full hashrate report visible and task manager with processes sorted by CPU usage?

## alexblock2019 | 2019-12-19T07:50:16+00:00
> Can you make the screenshot of miner window with full hashrate report visible and task manager with processes sorted by CPU usage?

Sorry,It hasn't appeared in a long time, no screenshots saved

## SChernykh | 2019-12-19T08:01:38+00:00
Ok, can you also check that pressing `p` and then `r` (pause, resume) fixes the hashrate when this happens?

## alexblock2019 | 2019-12-19T08:09:14+00:00
> Ok, can you also check that pressing `p` and then `r` (pause, resume) fixes the hashrate when this happens?

I'm not sure
I remember trying it, but it was still slow, must restart the miner
If this problem occurs again, I try again.
Memory may be wrong

## saltednutz825 | 2019-12-20T05:19:05+00:00
![Screenshot_20191220-131322_TeamViewer](https://user-images.githubusercontent.com/49343437/71231973-0acd1600-232b-11ea-910a-a71e36d9ef7a.jpg)
The screenshot of task manager was taken when the slowdown happened.
I run xmrig hidden on this machine, so can't test about the pause and resume function now.

## SChernykh | 2019-12-20T06:13:57+00:00
It's using only 2 MB of memory on the screenshot, so it's swapping really heavily. How much memory does this PC have and how much was free at that moment?

## saltednutz825 | 2019-12-20T06:22:31+00:00
It's on idle, and the ram amount is 32gigs, which means the total usage should less than a quarter.

## SChernykh | 2019-12-20T06:31:52+00:00
I see. It doesn't show 2GB if large pages are used. It might have something to do with something programs running there to, especially Kaspersky Antivirus.

## saltednutz825 | 2019-12-20T06:37:58+00:00
But this issue happends on instances that doesn't have antivirus too, I've even tried to uninstall all the programs including those MB utilities, but still doesn't help.

## SChernykh | 2019-12-20T06:43:17+00:00
Can you install Process Explorer https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer and when this happens next time, right click on xmrig.exe, choose "Create Dump -> Create Minidump" and upload the resulting .DMP file here. I'll be able to see where it's stuck at.

## saltednutz825 | 2019-12-20T07:32:15+00:00
Okay I'll report when this happends again


## SChernykh | 2019-12-20T08:28:46+00:00
@jindyzhao @seamushroom54 One more thing to try is to set `"yield": false,` in config.json, maybe it will help.

## alexblock2019 | 2019-12-21T01:16:27+00:00
> @jindyzhao @seamushroom54 One more thing to try is to set `"yield": false,` in config.json, maybe it will help.

It happened again for a short time today, but it was restored automatically when I came to the computer，in ryzen 2600

## alexblock2019 | 2019-12-21T13:06:41+00:00


> @jindyzhao @seamushroom54 One more thing to try is to set `"yield": false,` in config.json, maybe it will help.

I think that this problem is caused by several factors, one of which may be the problem of windows itself. After the lock screen and automatic shutdown, this problem is very easy to occur. Once the computer is operated, it returns to normal. But I have disabled all the energy-saving options and used the high-performance mode. It may be related to some hidden energy-saving factors in the system. It is worth mentioning that GPU mining has never been affected.
I also had this problem on Intel (R) Xeon (R) CPU E3-1230 v3, so it may not be just a Ryzen problem.
All systems that have problems are win10 1903.linux This problem has never occurred.

## alexblock2019 | 2019-12-21T14:07:56+00:00




> @jindyzhao When this happens next time, can you check CPU and memory usage in task manager?

![p r](https://user-images.githubusercontent.com/43772741/71309044-51f7fb80-243e-11ea-8525-72d0ee3103e0.jpg)
![task](https://user-images.githubusercontent.com/43772741/71309045-53c1bf00-243e-11ea-9069-cd70124567fd.jpg)


## SChernykh | 2019-12-21T14:11:42+00:00
I can see that xmrig doesn't use any cpu, it's some OS glitch there.

## alexblock2019 | 2019-12-21T14:15:57+00:00
> I can see that xmrig doesn't use any cpu, it's some OS glitch there.

I renamed the program,"System" is xmrig.

## alexblock2019 | 2019-12-21T14:23:07+00:00
> I can see that xmrig doesn't use any cpu, it's some OS glitch there.

[GPU-Z Sensor Log.zip](https://github.com/xmrig/xmrig/files/3991462/GPU-Z.Sensor.Log.zip)
I used gpu-z to record some logs. I can see that the CPU temperature dropped from 80 + ° c at full load to 60 + ° c, but it did not drop to standby temperature

## SChernykh | 2019-12-21T14:27:14+00:00
There's also system process with pid 0 using 31% cpu, this is strange. It's definitely not a normal state for Windows.

## alexblock2019 | 2019-12-21T14:49:12+00:00
> There's also system process with pid 0 using 31% cpu, this is strange. It's definitely not a normal state for Windows.

pid 0 is System idle process,higher means the system is more idle.
From the task manager, there is no difference between the load and normal time. The difference I can find is the processor temperature.


## alexblock2019 | 2019-12-21T14:50:49+00:00
> There's also system process with pid 0 using 31% cpu, this is strange. It's definitely not a normal state for Windows.

I turned on smt,use 7 thread,so 31% idle is normal

## alexblock2019 | 2019-12-21T15:07:26+00:00
> There's also system process with pid 0 using 31% cpu, this is strange. It's definitely not a normal state for Windows.

If it is possible, is it possible to add an automatic detection of the speed drop and automatically restart the miner function? Like some GPU miners

## saltednutz825 | 2019-12-23T01:02:20+00:00
@SChernykh 
that happend again on 1700 this morning, windows 10 build 1809, cpu no yeild has been set.
The situation is the same, hashrate goes to 0 and normal cpu usage, but only 4mb ram used in the task manager.
Attachment is the dump
[xmrig.zip](https://github.com/xmrig/xmrig/files/3993239/xmrig.zip)



## SChernykh | 2019-12-23T08:53:38+00:00
@seamushroom54 Interesting. I can see in the dump that 8 threads are still running mining code, so they're not stuck somewhere. What's the ram usage for xmrig when hashrate is normal?

## saltednutz825 | 2019-12-24T05:55:38+00:00
@SChernykh it happens again on the same machine today
I've checked, it appears to be 2 to 3 mb of ram used reported in the task manager.
![Screenshot_20191224-135446_TeamViewer](https://user-images.githubusercontent.com/49343437/71396429-0cf9e200-2655-11ea-99cd-45a8836097c9.jpg)

[xmrig.zip](https://github.com/xmrig/xmrig/files/3997335/xmrig.zip)


## implodnik | 2019-12-24T15:54:30+00:00
I also suffer from this annoying bug. My observations:

1) I have 16 different PCs at different locations, both Intel and AMD based, all running xmrig on the Nicehash pools. Only 4 of them experience this problem – those that run Windows 10 1903 or 1809, all are based on Intel CPUs. Earlier Windows 10 builds and non-10 Windows work fine (well, almost fine, see below).

2) The slowdown begins and ends spontaneously (at least on the Nicehash pools), usually exactly at an hour boundary, sometimes at 30-minute boundary, and almost never at random time:
![Even hour](https://user-images.githubusercontent.com/59203846/71418925-c8cb0980-2675-11ea-8b4b-e906c28b6c97.png)
*(horizontal and almost horizontal parts on the graph correspond to slowdown periods).

3) It may happen without any visible clue in the log, but often it happens after series of "end of file" errors:
![i7-8700 1](https://user-images.githubusercontent.com/59203846/71418693-5dcd0300-2674-11ea-91f0-0d739b29da80.png)

4) The other 12 PCs also experience a slowdown after this, but it's not that dramatic and usually recovers within minutes:
![tr1950x 1](https://user-images.githubusercontent.com/59203846/71418738-c2885d80-2674-11ea-9e0e-78b201c2a1b0.png)

5) I tried to do "pause-resume", it didn't help:
![i7-8700 2](https://user-images.githubusercontent.com/59203846/71419047-37a86280-2676-11ea-90d8-d2628286c69a.png)


## implodnik | 2019-12-24T17:01:58+00:00
Also please note that when the "end of file" happens, xmrig immediately says "no active pools, stop mining", despite the fact that there is also an alternative pool defined (randomxmonero.usa.nicehash.com).

## alexblock2019 | 2019-12-26T05:37:03+00:00
> I also suffer from this annoying bug. My observations:
> 
> 1. I have 16 different PCs at different locations, both Intel and AMD based, all running xmrig on the Nicehash pools. Only 4 of them experience this problem – those that run Windows 10 1903 or 1809, all are based on Intel CPUs. Earlier Windows 10 builds and non-10 Windows work fine (well, almost fine, see below).
> 2. The slowdown begins and ends spontaneously (at least on the Nicehash pools), usually exactly at an hour boundary, sometimes at 30-minute boundary, and almost never at random time:
>    ![Even hour](https://user-images.githubusercontent.com/59203846/71418925-c8cb0980-2675-11ea-8b4b-e906c28b6c97.png)
>    *(horizontal and almost horizontal parts on the graph correspond to slowdown periods).
> 3. It may happen without any visible clue in the log, but often it happens after series of "end of file" errors:
>    ![i7-8700 1](https://user-images.githubusercontent.com/59203846/71418693-5dcd0300-2674-11ea-91f0-0d739b29da80.png)
> 4. The other 12 PCs also experience a slowdown after this, but it's not that dramatic and usually recovers within minutes:
>    ![tr1950x 1](https://user-images.githubusercontent.com/59203846/71418738-c2885d80-2674-11ea-9e0e-78b201c2a1b0.png)
> 5. I tried to do "pause-resume", it didn't help:
>    ![i7-8700 2](https://user-images.githubusercontent.com/59203846/71419047-37a86280-2676-11ea-90d8-d2628286c69a.png)
I think it may be related to the priority option.
Whether the priority option is used？

## alexblock2019 | 2019-12-26T05:37:18+00:00
> Okay I'll report when this happends again

I think it may be related to the priority option.
Whether the priority option is used？

## alexblock2019 | 2019-12-26T05:38:44+00:00
I discovered the problem again today, so I tried to change the priority in taskmanger, and the speed returned to normal.

## implodnik | 2019-12-26T11:54:31+00:00
> >    I think it may be related to the priority option.
> >    Whether the priority option is used？

No, I never used the priority option for xmrig yet.

## implodnik | 2020-01-08T11:33:52+00:00
Even with the new 5.5.0 version (which started to overprioritize working threads) and priority set to 3 it still happens after a series of "end of file"->"internal server error" messages.

## SChernykh | 2020-01-08T11:39:47+00:00
If there's no connection to pool, XMRig stops hashing of course.

## implodnik | 2020-01-08T11:40:14+00:00
Did you see the screenshots above?

## SChernykh | 2020-01-08T11:52:31+00:00
Try to disable Memory Compression in Windows 10, it's known to trigger periodically and mess with hashrate.

## implodnik | 2020-01-08T12:16:43+00:00
I will, but it seems unlikely that memory compression process is the cause of this since low hashrate periods start exactly after error events in xmrig and may last for many hours.

## implodnik | 2020-01-16T18:05:20+00:00
Yep, it happens even with disabled memory compression:

![xmrig-mc-disabled-slowdown](https://user-images.githubusercontent.com/59203846/72550381-4b24a300-389b-11ea-80c2-ec80b8661f9f.png)


## implodnik | 2020-01-17T00:30:27+00:00
And the moment where it fixes itself – by switching to a devfee session, doing nothing there, returning to the main session, not printing hashrate for 7 minutes, and then suddenly starting to work at full speed:

![xmrig-mc-disabled-slowdown-recovery](https://user-images.githubusercontent.com/59203846/72574314-3fec6a00-38d1-11ea-90e9-26d0a6026434.png)


## SChernykh | 2020-01-17T06:29:46+00:00
> And the moment where it fixes itself – by switching to a devfee session, doing nothing there, returning to the main session, not printing hashrate for 7 minutes, and then suddenly starting to work at full speed:

This is very strange. Hashrate printing is very basic functionality that works always. It seems that some other process took 100% CPU for a while. You should watch what happens in task manager during these outages. I also recommend using "Process Explorer" instead of regular task manager because it shows more data.

## implodnik | 2020-01-17T06:56:26+00:00
I'll try to investigate this deeper, but usually I see such events post factum, after recovery. Was hoping you can determine the cause empirically; the theory about a mysterious external process looks quite doubtful (when I catch a slowdown in progress, the affected PC works subjectively normally; restarting xmrig resolves the problem immediately, but pausing/resuming doesn't help; strong correlation with events inside xmrig also suggests an idea about an internal problem).

## implodnik | 2020-01-17T16:29:29+00:00
A question. I see strong discrepancy between the three averages during the slowdown periods, which definitely is not normal and indicates logical errors in the code. Could it be that it doesn't print hashrate when it becomes "n/a n/a n/a" (due to, say, some exception)? Why it is "n/a" instead of "0"? Why average of "n/a"s is some number? Could some exception handling code (or even masked exceptions) eat the hashrate?

## SChernykh | 2020-01-17T16:31:58+00:00
"n/a" is shown when there was not enough hashes during time period to calculate the average hashrate.

## implodnik | 2020-01-17T16:36:19+00:00
It's not normal that it is able to print something like "n/a 2.0 7.0" for an hour or two, there are serious flaws in the current logic,

## saltednutz825 | 2020-01-19T00:38:39+00:00
It still happends a lot, namely a lot, on different instances.
Normal cpu and memory usage when the miner hang.
![擷取](https://user-images.githubusercontent.com/49343437/72672538-63acdd00-3a96-11ea-935e-2e773461f81a.PNG)

Tested, after pause and resume the hashes goes back, and the unauthenticated message shown whenever this happends (when the miner hangs or after the pause-and-resume), had asked the pool owner, but they said it's not their problem.
![1擷取](https://user-images.githubusercontent.com/49343437/72672545-7f17e800-3a96-11ea-868b-2c07355b0113.PNG)


## saltednutz825 | 2020-01-19T04:09:28+00:00
Again, same day, same issue, different machine.
![Screenshot_20200119-120730_TeamViewer](https://user-images.githubusercontent.com/49343437/72674686-76cea580-3ab4-11ea-8ef8-a7c5dca6d0f3.jpg)


## SChernykh | 2020-01-19T07:16:30+00:00
Can you use `Process Explorer` instead of regular Task Manager next time? https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer
When this happens, right click on xmrig in Process Explorer, select `Properties` and then `Performance Graph` tab - I need to see it.

## saltednutz825 | 2020-01-20T12:09:57+00:00
@SChernykh 
happend again right now
![image](https://user-images.githubusercontent.com/49343437/72725156-0614af80-3bc0-11ea-8d41-b8ec96c69dea.png)


## SChernykh | 2020-01-20T12:15:55+00:00
If it's still happening, right-click on xmrig, select `Create Dump` -> `Create Minidump` and attach the dump file here.

## saltednutz825 | 2020-01-20T12:17:18+00:00
@SChernykh 
have done a full dump before restart
uploading it to cloud drive, hold on.

## saltednutz825 | 2020-01-20T12:19:08+00:00
https://drive.google.com/file/d/1FZex0JcOKofGw09HACCJKT2VXfwGG5sZ/view?usp=sharing

## SChernykh | 2020-01-20T12:37:31+00:00
Hmm, at the first glance I don't see anything strange - 8 mining threads are running RandomX mining code, so hashrate should have been normal when the dump was taken.

## saltednutz825 | 2020-01-20T12:42:15+00:00
@SChernykh I don't know, but I was informed by pool disconnected notification (which means it's not just a hastate display issue, but not sending any hash to the pool), and then go check that rig, see the abnormalities on xmrig.
![Screenshot_20200120-203845_LINE](https://user-images.githubusercontent.com/49343437/72727215-53dfe680-3bc5-11ea-9599-d04876d5fb4d.jpg)


## SChernykh | 2020-01-20T12:53:59+00:00
Do you run any rigs on Linux or Windows 7? Did you see this problem there? Maybe it's Windows 10 specific issue, or maybe it's Kaspersky Antivirus interfering somehow. I'm out of ideas right now.

## saltednutz825 | 2020-01-20T12:58:02+00:00
@SChernykh All of my rigs are using win10, sadly this problem hapends on the instances without kaspersky too, and the problem exist across 1700, 2600x, 3600 and 3600x.
Hoping this could be solved in future update, thanks for your effort.

## implodnik | 2020-01-20T14:00:48+00:00
@SChernykh
> I'm out of ideas right now.

Please note that on the seamushroom54's screenshots there is the same anomaly – during slowdowns displayed short term hashrate averages are consistently lower than mid term and long term ones, which is totally wrong. There is a chance that investigating and fixing this will lead you to understanding what happens here.

## SChernykh | 2020-01-20T14:12:31+00:00
This is normal - hashrates shown are moving averages, so 15-minute hashrate adjusts only after 15 minutes. 1-minute hashrate is bigger than 10-second hashrate because more hashes are averaged, so it's more precise. Maybe there is a bias to lower hashrates in the accounting code, I need to check it.

## implodnik | 2020-01-20T14:19:47+00:00
> 1-minute hashrate is bigger than 10-second hashrate because more hashes are averaged, so it's more precise

Not for 10-20-30-60 minutes in a row.

> Maybe there is a bias to lower hashrates in the accounting code

Maybe. But it could be something else related to the topic problem, so it worth checking.


## implodnik | 2020-02-07T17:28:32+00:00
5.5.2 and 5.5.3 didn't resolve the problem. Disabling memory compression still does not help, setting priority 2 or 3 does not help, Windows 8 compatibility mode does not help, using the gcc-compiled version instead of the msvc one also does not help.

The slowdown start and stop clearly gets triggered by error events, I can't see a way how the OS could be blamed for this:
![xmrig-bug-again](https://user-images.githubusercontent.com/59203846/74050018-f1b51d00-49dd-11ea-8e64-f3d88bbfb381.png)

Amazingly, this issue is still not even tagged as a "bug".
And, is it normal that xmrig keeps saying "no active pools, stop mining" after an error on the main pool despite having a secondary pool defined?

Also, dunno if this could help, but a strange anomaly – xmrig managed to set speed record while doing virtually nothing:
![xmrig-bug-again overspeed](https://user-images.githubusercontent.com/59203846/74051424-989ab880-49e0-11ea-9ece-96e6bee41dbd.png)

That 8700 can reach 4.5 KH/s with 6 threads, but xmrig is configured for using only 5, so 3.9..4K is its normal hashrate on that machine.

## SChernykh | 2020-02-07T17:42:22+00:00
@implodnik Can you do memory dump with Process Explorer when this happens again (see instructions above)? Also check how much CPU does xmrig use when it slows down.

## implodnik | 2020-02-07T18:05:35+00:00
It generates exactly the same CPU load as it does during normal operation – 41..42% (5 logical cores of 12), just slightly less (~1.5 times) context switches per second on calculating threads, according to Process Explorer.
Also, while operating normally, xmrig briefly wakes up two usually sleeping threads on every new line of text in console; in slowdowns, it seems to not do this, bit I have to check again.

I can share a memory dump if it's absolutely necessary, but I'd prefer to avoid this for security reasons.

## saltednutz825 | 2020-04-29T11:36:42+00:00
@xmrig 
It has been so long, and the problem still exist
Are there any potential cause?

## SChernykh | 2020-04-29T11:42:04+00:00
Try to remove CPU core binding (use `"rx":[-1,-1,...,-1],` in config.json), you can read more here: https://github.com/xmrig/xmrig/issues/1506#issuecomment-597624636

## saltednutz825 | 2020-04-30T01:09:00+00:00
@SChernykh
Thanks for your advice, I'm using win10 build 1909 now
After cross-testing, I found the ultimate problem might be priority drop.
Which means windows will change the priority set by xmrig to "below normal" under some circumstances, then the anomaly would emerge.
So I ended up using an .bat file to launch xmrig, which makes the priority fixed, and till now, the problem didn't happen again, and I'll keep an eye on it.

## saltednutz825 | 2020-05-16T00:56:30+00:00
Issue solved.
Confirmed, new version of Windows+priority drop would result in this.
Never happens again after I manually get priority fixed by .bat

## mrdogITC | 2020-06-25T11:24:14+00:00
Can you write the example of the .bat script with which you set the priority?

## xmrig | 2020-08-31T05:48:16+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: alexblock2019 | 2019-12-07T01:24:59+00:00
- Closed at: 2020-08-31T05:48:16+00:00
