---
title: Xmrig killed on start (Android 10)
source_url: https://github.com/xmrig/xmrig/issues/2593
author: webcmrj
assignees: []
labels: []
created_at: '2021-09-20T15:04:06+00:00'
updated_at: '2021-11-14T03:11:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi! Im trying to run the xmrig mining on my S9 but whenever it starts the process it gets killed.

I've tried lots of editions on config.json but none worked so far:

- Changing mode auto to light 
- enable/disable numa 
- enable/disable huge pages 

My phone has 4gb and 8 threads as you can see on screenshot below.

Thanks in advance for any help.

![Screenshot_20210920-115511_Termux](https://user-images.githubusercontent.com/91077253/134025362-432fd553-c8c4-4223-8d9b-19eb161d27a5.jpg)


# Discussion History
## Spudz76 | 2021-09-20T16:34:48+00:00
I would imagine `dmesg` (or whatever android uses, maybe `logread`?) would show OOMkiller took it out.

4GB is very very very tight for 2336MB+16MB (8 threads * 2MB) allocation while other things are already using most of it.  Kernel OOM (out of memory) killer will kill the most recent memory-hogging thing automatically to avoid system lockup (among some other rules).

You might make it work by killing off most of the system services to reclaim more memory but I'd just mine anything other than RandomX through MoneroOcean or such to be paid XMR for something that doesn't need to blow all your RAM.

## webcmrj | 2021-09-20T17:48:37+00:00
Isn't there a way to reduce the threads or memory usage on config.json or similar on xmrig?
I was expecting it to use only around 2MB.

## webcmrj | 2021-09-20T18:03:52+00:00
Also is there any way i can disable the OOM killer? Even when using around 70 / 80% it keeps getting killed.

## Spudz76 | 2021-09-20T20:50:34+00:00
No, and No.

RandomX has the large 2336MB dataset whether you have one thread or 50.  Although, light mode should work and just needs 256MB, not sure why it isn't.

OOMKiller is hard to control and the best way to keep it behaving is to not OOM.

cn and others don't have a dataset and do follow your expectation of 2MB per thread (though some are 4MB per thread, and astrobwt uses 20MB per thread).  Thus the suggestion to sidestep the RandomX hugeness problem by autoexchange mining at MoneroOcean for XMR payout -- the output is essentially the same or better because your CPU will be better at easier algos anyway thus earning more than it would trying to haul RandomX uphill in the snow against the wind.

Monero used to be cn based (cn/0 then cn/r) so if you're reading ancient posts they will have the wrong memory requirements (back when it was per-thread and no dataset, because it wasn't rx/0 yet).

## webcmrj | 2021-09-20T21:09:33+00:00
I just ran it on my S9 plus and XMRIG uses 2.6gb (as expected)...but on my lower S9 it keeps getting 3.2gb!!!
Something is going on here... @Spudz76 

## asumas | 2021-11-14T03:11:20+00:00
@webcmrj how can you run the .exe file on your phone can you show me

# Action History
- Created by: webcmrj | 2021-09-20T15:04:06+00:00
