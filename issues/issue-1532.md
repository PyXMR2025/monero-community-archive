---
title: Xmrig doesn't start mining monero
source_url: https://github.com/xmrig/xmrig/issues/1532
author: MAHDI00032
assignees: []
labels: []
created_at: '2020-02-03T08:27:10+00:00'
updated_at: '2022-03-21T13:42:34+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:58:54+00:00'
---

# Original Description
when i started to mine monero on my vps it didnt repond me anything!!!!!
vps info:
Linux ide 4.14.104-95.84.amzn2.x86_64 #1 SMP Sat Mar 2 00:40:20 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

![Capture](https://user-images.githubusercontent.com/30466994/73636842-1591ff00-467c-11ea-942c-da05bfc18835.jpg)


# Discussion History
## xmrig | 2020-02-03T08:38:18+00:00
Connection might be blocked somehow, try use `14433` port with `--tls` option or another pool.
Thank you.

## MAHDI00032 | 2020-02-03T12:19:21+00:00
Again it dosnt work : 

![Capture1](https://user-images.githubusercontent.com/30466994/73652549-6ca7cc00-469c-11ea-80b4-4cc295320bd1.PNG)

I tried another pool too :
![Capture2](https://user-images.githubusercontent.com/30466994/73652704-bc869300-469c-11ea-9054-1a10ea874d57.jpg)


## SChernykh | 2020-02-03T13:42:16+00:00
Your VPS provider most likely blocks all connections to known pools. But even if you manage to connect, you have less than 2 GB free RAM, so you won't be able to get good hashrate.

## MAHDI00032 | 2020-02-03T14:02:09+00:00
it dosent matter . How did you get i have 2GB free ram ? i thinks the free space is more. 
please help me :(

## SChernykh | 2020-02-03T14:03:56+00:00
It shows `Memory 28.4/30.4 GB (93%)` on your screenshot. There's not enough memory to allocate full RandomX dataset for efficient mining.

## MAHDI00032 | 2020-02-03T14:10:20+00:00
i want to free it . can you help me ?

## mmbuilder01 | 2020-02-03T16:39:55+00:00
it seems it is a bug !

## mmbuilder01 | 2020-02-03T16:50:30+00:00
look here i am using 8 GB of my memory , But the miner shoews 98% !!!!!!!

![55555555555552-53](https://user-images.githubusercontent.com/60614506/73672316-e56d4f00-46c1-11ea-8e1a-2c7587fcddd7.jpg)
![33333333333333335](https://user-images.githubusercontent.com/60614506/73672628-7d6b3880-46c2-11ea-8d29-85d3b96a5824.jpg)

After starting to mine : 
![2222222222222-03_20-19-50](https://user-images.githubusercontent.com/60614506/73672671-91169f00-46c2-11ea-94a4-6acb85ba5123.jpg)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


## 2010phenix | 2020-02-03T21:03:18+00:00
try disable huge pages and look if your problem is memory

## GjBrutello | 2020-02-05T08:30:12+00:00
reboot the comp to free memory and launch again a miner.

## MAHDI00032 | 2020-02-10T04:43:17+00:00
I cant restart my linux server , i do a command for disabling huge pages but it didn't work : 
![Captdddure](https://user-images.githubusercontent.com/30466994/74121546-2e9b3280-4bdd-11ea-9cd7-060647199ae2.jpg)




## BlankerL | 2020-02-23T08:39:57+00:00
It is highly possible that the VPS provider blocks all the traffic to the existing pool. You can build a xmrig-proxy on a not-blocked machine, connect the current VPS to the proxy.

## BlankerL | 2020-02-23T08:41:46+00:00
> I cant restart my linux server , i do a command for disabling huge pages but it didn't work :
> ![Captdddure](https://user-images.githubusercontent.com/30466994/74121546-2e9b3280-4bdd-11ea-9cd7-060647199ae2.jpg)

Kill some processes that take a large amount of memory. 

## BlankerL | 2020-02-23T08:46:38+00:00
> look here i am using 8 GB of my memory , But the miner shoews 98% !!!!!!!

Use the `free` command to check the memory usage, 

```bash
# free
              total        used        free      shared  buff/cache   available
Mem:       14288688      452720    11827976      634204     2007992    12951636
Swap:             0           0           0
```

I think you need to focus on the `free`/`available` part.

## RIKIPB | 2020-10-16T07:28:42+00:00
I don't understand why when I send the command nothing happens ..
![Cattura](https://user-images.githubusercontent.com/28224000/96225545-86badd80-0f91-11eb-9122-b290c2c23c2c.PNG)

This is the directory where i try to send the command
![Cattwa](https://user-images.githubusercontent.com/28224000/96225736-cf729680-0f91-11eb-83ef-9ca2f5a6366e.PNG)
OS: Ubuntu Server 18.04
CPU: Intel core i3
Ram: 8GB
what am I doing wrong?


## BlankerL | 2020-10-16T19:40:32+00:00
@RIKIPB Because you copied & pasted the command from somewhere else, and did not realize that your command contains a `-B`, which means that running the process in the background. You can `ps aux | grep xmrig`, and I suppose you will find that `xmrig` is still running in the background (if you have executed the command multiple times, there will be many processes running in the same time)

## RIKIPB | 2020-10-16T22:12:54+00:00
> @RIKIPB Because you copied & pasted the command from somewhere else, and did not realize that your command contains a `-B`, which means that running the process in the background. You can `ps aux | grep xmrig`, and I suppose you will find that `xmrig` is still running in the background (if you have executed the command multiple times, there will be many processes running in the same time)

Thanks!

## Saikatsaha1996 | 2020-10-24T22:14:48+00:00
![IMG_20201025_034415](https://user-images.githubusercontent.com/72664192/97094659-5e5b6f00-1674-11eb-9277-422d39faeebe.jpg)
Please help not start....

## GregoryUnderscore | 2022-03-21T13:41:58+00:00
I'm seeing the same problem with plenty of memory available. I do expect it is the pool. I know it is not a block on the computer or network, as I can sometimes connect without any issue. My primary question here is whether XMR Rig is just stuck sitting there? It appears to never try to reconnect. However, there is no way to tell if it is attempting a 2nd connection attempt or just sitting idle (which would seem a problem).

# Action History
- Created by: MAHDI00032 | 2020-02-03T08:27:10+00:00
- Closed at: 2020-08-29T04:58:54+00:00
