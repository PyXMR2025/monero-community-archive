---
title: Xmrig Miners Receive 50 New Jobs In 1 Minute Multiple Times Per day
source_url: https://github.com/xmrig/xmrig/issues/2127
author: downystreet
assignees: []
labels:
- bug
created_at: '2021-02-23T07:00:12+00:00'
updated_at: '2022-03-22T18:55:50+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:10:31+00:00'
---

# Original Description
xmrig version: 6.8.2 & 6.9.0

I'm mining to the monero daemon in my own network through the xmrig proxy. I created a log file on 2 different machines and noticed that several times per day they are receiving mass amounts of jobs in the span of a minute. For example I counted over 50 new jobs in the span of a minute for one instance. Every instance occurs at the same time on both machines. I'm not sure if this issue was addressed with the recent update but I wanted to point it out. Here is a picture of the log file.

Update: also occurs on version 6.9.0

![proxy5](https://user-images.githubusercontent.com/63488055/108811143-b484e400-757a-11eb-8377-30bd5799e82d.png)



# Discussion History
## alanhasgari | 2021-02-23T20:43:58+00:00
I'm getting the same mining to minexmr pool... It's been present in the last couple releases, for sure... Have to close xmrig and start again to correct the behavior...

## venze | 2021-02-23T21:20:12+00:00
Hey, what pool is this and how is your config file set up? Thanks!

## alanhasgari | 2021-02-24T03:01:24+00:00
> Hey, what pool is this and how is your config file set up? Thanks!

OP said they're mining to monerod, I'm mining to minexmr pool.
I've experienced this on 3 of my 5 rigs... It's most noticable on my i5 and Ryzen5 rigs...

You'll see in my screenshots the sharp peaks followed by steep drops; the issue corrects itself when I close and restart xmrig. The steep drops are when the rigs aren't submitting any shares as the jobs are rapidly changing. As I mentioned, it's been happening the last 2 or 3 releases. I did not have this issue previously...

I haven't had this issue with my Xeon rig, but that one is running xmrig via idleminer. I'm not entirely convinced the issue OP is having is with xmrig, but if we can get some help troubleshooting, that would be great...

![Screenshot_20210223-215815](https://user-images.githubusercontent.com/5217983/108940985-45fb6100-7622-11eb-9ed9-1d5421a0f457.png)
![Screenshot_20210223-215824](https://user-images.githubusercontent.com/5217983/108940996-498ee800-7622-11eb-9bab-8e7b58b40e68.png)



## Lonnegan | 2021-02-24T08:08:41+00:00
@alanhasgari Are you sure you have the same problem as @downystreet ? Can you see the jobs coming quickly in the xmrig window? Otherwise the frequently droping hashrates could be the Windows 10 v1903+ scheduler problem, as well:
https://github.com/xmrig/xmrig/issues/1506

## alanhasgari | 2021-02-24T08:35:02+00:00
> @alanhasgari Are you sure you have the same problem as @downystreet ? Can you see the jobs coming quickly in the xmrig window? Otherwise the frequently droping hashrates could be the Windows 10 v1903+ scheduler problem, as well:
> #1506

The cause may be different, but the description is very much the same. It'll mine fine for awhile, then the jobs switch so rapidly that it doesn't submit a share, then it'll submit several share when the height changes, then repeats until I close xmrig and relaunch it.

## snipeTR | 2021-02-24T09:20:37+00:00
it looked like the wrong "difficulty calculation" to me.

## 2010phenix | 2021-02-25T14:33:55+00:00
it can be wrong auto detect option, old(CN R) one before RandomX... same problem I see in proxy (drop hashrate x4 - x5)

## downystreet | 2021-02-26T00:20:00+00:00
I just checked the logs again. The mass of new jobs corresponds to the proxy giving the connection error: connect error: "connection timed out", #000 no active pools, stop ,connect error: "connection timed out". So when the proxy is giving the connect error the miners are getting lots of new jobs for the same block. I submitted the connection issue in #2118. 

Update: The same thing happens when not using the xmrig proxy. I set 2 miners to connect directly to the daemon and not go through xmrig proxy and the same thing happens. They get the connection timeout at certain times followed by a mass of new jobs for the same block.

## alanhasgari | 2021-02-26T21:34:43+00:00
My ryzen system freaked out again. I switched it to idleminer, which calls xmrig to mine when idle... The method works great on my Xeon which is only a part time miner, but we will see if this solves my problem... The issue now seems to be idleminer is no longer calling xmrig for kawpow mining when idle, but that's unrelated to xmrig 😅

## snipeTR | 2022-03-22T15:58:48+00:00
![Adsız](https://user-images.githubusercontent.com/31975916/159523610-58cfd243-b8ff-4def-90e5-2f9ab54fd8cb.png)

same problem.


## SChernykh | 2022-03-22T17:04:08+00:00
This is how Dero mining works, these are real new jobs.

## snipeTR | 2022-03-22T18:55:50+00:00
is there a way to turn off this new jobs message?  such as the -silent command.  or like pressing the g key on the keyboard :)

# Action History
- Created by: downystreet | 2021-02-23T07:00:12+00:00
- Closed at: 2021-04-12T14:10:31+00:00
