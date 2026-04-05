---
title: CPU usage mysteriously changed to 70%
source_url: https://github.com/xmrig/xmrig/issues/2634
author: johnyblazin
assignees: []
labels: []
created_at: '2021-10-17T07:13:58+00:00'
updated_at: '2021-10-17T20:25:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
i have been usuing xmrig for almost a year and i have never seen this. today when i was just sitting by my pc with task manager and hardware monitor open and i saw the usage jump in task manger to 70% but it stays at 50% on hardware monitor..

whenever i run xmrig it usualy would sit at 50% now its mysteriously at 70%
when i close xmrig it shows a idle usage of 0% so i know there is something showing up mysteriously when xmrig app is running 


![Untitled](https://user-images.githubusercontent.com/92664775/137616015-acd94ca5-99aa-4715-9a0c-715b9c04bbf8.png)



# Discussion History
## Lonnegan | 2021-10-17T15:38:22+00:00
Strange, indeed, especially since the RessourceManager and HWMonitor are completely correct in showing 50% utilization for xmrig.

Of course your CPU don'r really have 8 cores, but 4 cores with SMT. So, when running xmrig with 4 threads, the CPU indeed is loaded with more than 50%. But normally the taskmgr don't care about that. My Ryzen 7 uses SMT, too, when I run xmrig with 8 threads on that 16 thread CPU, the taskmanager shows 52%, which is ok. Your 71% instead are strange. Perhaps the taskmgr get's confused thru certain turbo or P-states functions. Or the system itself get's load from something, because when you look at the unloaded "cores" in the taskmgr's graph, you can see that there is indeed some load. But where does it come from?

## johnyblazin | 2021-10-17T18:50:23+00:00
yeah i actually came to that conclusion because im overclocked to 4.8ghz thats almost 123% faster of its suposed speed of turbo boost for this 3770k this article explains it , but then if i disable overclocking this should technicaly fix it ?

https://support.microsoft.com/en-us/topic/5e3ca7cf-b99b-24ba-1ddf-c961979d3111#:~:text=Starting%20with%20Windows%208%2C%20a%20change%20was%20made,when%20capacity%20is%20boosted%20by%20Intel%20Turbo%20Boost.

## johnyblazin | 2021-10-17T18:55:41+00:00
with overclocking disabled it settles closest to 55% but this is at stock config so it has someting to do with https://support.microsoft.com/en-us/topic/5e3ca7cf-b99b-24ba-1ddf-c961979d3111#:~:text=Starting%20with%20Windows%208%2C%20a%20change%20was%20made,when%20capacity%20is%20boosted%20by%20Intel%20Turbo%20Boost.[
![Untitled](https://user-images.githubusercontent.com/92664775/137641043-51eb3029-5775-4afc-97c4-9f8889f6ed6a.png)


## johnyblazin | 2021-10-17T19:08:48+00:00
also i had a question about overclocking , i heard you want to change your CPU switching frequencey to a lower value to obtain higher lifespan on your vrms can you confirm this as factual ? 

## Spudz76 | 2021-10-17T20:25:54+00:00
If you algo-switch then some of them are using more/less threads.

# Action History
- Created by: johnyblazin | 2021-10-17T07:13:58+00:00
