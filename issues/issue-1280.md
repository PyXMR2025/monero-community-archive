---
title: error  with 6* gtx 1080 TI rig
source_url: https://github.com/xmrig/xmrig/issues/1280
author: ari2asem
assignees: []
labels:
- question
created_at: '2019-11-13T18:50:29+00:00'
updated_at: '2019-11-15T07:20:55+00:00'
type: issue
status: closed
closed_at: '2019-11-15T07:20:55+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/57032135/68793479-29404300-0602-11ea-9a85-ec5385382aa3.png)
![image](https://user-images.githubusercontent.com/57032135/68793506-3826f580-0602-11ea-8dd3-2cd89710e68b.png)

I get error while trying to mine with a rig of 6 cards gtx 1080 ti (4* zotact, 2* gigabyte)….
gpu0 - gpu3 = zotact (all exact the same model)
gpu4 - gpu5 = gigabyte (2 different model)

cpu i7-5820k (6 cores / 12 HT)
memory 16GB (4*  4GB, ddr4-2133Mhz)
mainboard asus x99-e ws
bios without any tweak or overclock, all default

cpu mining is disabled in config.json….only gpu (nvidia) mining is enabled

when I stop xmrig-5.0.0 and restart again, second time are another gpu's in troubles. thus according to these screenshots are gpu1, gpu2 and gpu5 with problems. but at next start of xmrig it can be changed to any other number, e.g. gpu3, gpu0 or gpu4....it is always changing these numbers

# Discussion History
## xmrig | 2019-11-13T18:56:36+00:00
Try reducing `"threads": 54,` until errors disappear, location in config file `"cuda"` -> `"cn/2"`.
Thank you.

## ari2asem | 2019-11-14T06:40:40+00:00
![image](https://user-images.githubusercontent.com/57032135/68831306-c4690500-0662-11ea-805b-8688f8b502fd.png)

![image](https://user-images.githubusercontent.com/57032135/68831424-2b86b980-0663-11ea-8fff-718dc2bc77b7.png)


I set now threads to 28, seems to work.
but a question....when I set threads to 40, i see hashrate drops very litte. is this normal?

threads 40 ==>> 722 H/s
threads 28 ==>> 767 H/s
threads 10 ==>> 727 H/s


can you explain me what the function of  THREADS is if the hashrate is almost the same with so much difference between high and low values (threads 28 and threads 10)?? 

## xmrig | 2019-11-14T07:39:02+00:00
threads * blocks * 2 = this is memory in MB used on GPU, but dependency memory/hashrate very nonlinear, you can also change blocks count, right now it `28 * 3 = 84` where 28 is smx count.

For example 28x84 and 42x56 use same memory amount but results may be different too. With different blocks count optimal threads count also changed.
Thank you.

## ari2asem | 2019-11-14T11:15:35+00:00
thanks for your answer.

please, take a very good look at this screenshot

![image](https://user-images.githubusercontent.com/57032135/68852133-24c06c80-068c-11ea-8e31-2ccc728fb2f4.png)

when i start with 58x56, gpu0 gives error. changing only the values of gpu0 (52x56) gives gpu5 error while nothing gpu5 has been changed. these all is done (addjusting config.json) while xmrig-5.0.0 is running.

thus, there is so much inconsistency with this whole story

also, all the cards have the same gpu (1080 ti) and 11GB gpu memory.

why should one card work with 52x56 yet another card will give error with 52x56....they are all the same chipset and amount of memory

could this be because of my RAM size? I have RAM memory of 16GB, windows 10 v1903

## xmrig | 2019-11-14T13:34:48+00:00
Try increase swap file size and you are right threads initialization order is undefined.
Thank you.

## ari2asem | 2019-11-14T16:13:44+00:00
yes, swap file (pagefile) size trick helpen....now having threads 54 and blocks at 84, working good.

problem solved. thank you

# Action History
- Created by: ari2asem | 2019-11-13T18:50:29+00:00
- Closed at: 2019-11-15T07:20:55+00:00
