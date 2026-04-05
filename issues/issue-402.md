---
title: cpu-priority and hasrate on my notebook
source_url: https://github.com/xmrig/xmrig/issues/402
author: BearTi
assignees: []
labels: []
created_at: '2018-02-13T11:46:56+00:00'
updated_at: '2018-11-05T12:53:04+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:53:04+00:00'
---

# Original Description
Hi,

I´ve two short questioons / problem:

1) I set "cpu-priority" to "0", but even when I am working with my notebook mining is still done. (How) is it possible to stop mining when I am  working? 

2) I have a notebook with Intel i7-5600U and only get about 50 H/s, is that okay? How can I increase it? Here is my config:
`
    "algo": "cryptonight", 
    "av": 2,                
    "background": false,   
    "colors": true,        
    "cpu-affinity": null,   
    "cpu-priority": 0,  	
    "donate-level": 1,     
    "log-file": null,     
    "max-cpu-usage": 80,   
    "print-time": 120,     
    "retries": 5,          
    "retry-pause": 5,      
    "safe": false,       
    "threads": 1,       
`


# Discussion History
## Zelecktor | 2018-02-13T14:57:38+00:00
> "threads": 1

Your are using only one thread thats the reason. See how many cores have your CPU and you can highly increase your hashrate.
My suggestion is to set it "null", the software will automatically detect your threads, usually 4

## BearTi | 2018-02-13T16:10:07+00:00
Hi, thanks for the answer.

Even when I set it to "null" the script just uses 1 Thread:
`
 THREADS:      1, cryptonight, av=2, donate=5%
`

And even when I set 4 threads manually, my Hash-Rate gets lower (about 20H/s).

Any idea?

What Hashrate would be normale for an i7-5600U  or i7-7500U?


## Zelecktor | 2018-02-13T17:39:33+00:00
change `"av": 2`  to `"av": 0`

Which OS are you using? Are you trying mining on a VPS openVZ?

## BearTi | 2018-02-13T18:07:44+00:00
Ah, seems better... Now I have about 80H/s.
It´s a "normal" Notebook. 

What Hashrate would be okay for this one? I have two:  i7-5600U and i7-7500U

## Meyer01 | 2018-02-13T18:08:30+00:00
Normal hashrate for i7-5600U must be around 100-110H/s. Try 2 threads manually. Or let the miner calculate better amount itself.

## BearTi | 2018-02-13T18:13:36+00:00
Hmm... Here is a Screenshot:

![image](https://user-images.githubusercontent.com/3652708/36166094-d4bc9bd2-10f1-11e8-95b3-c88f3c68f367.png)


## Meyer01 | 2018-02-13T19:20:59+00:00
x86 or x64 miner?

## BearTi | 2018-02-13T19:39:14+00:00
Ah, I think that was the problem. Now I have about 100H/s :-D

Thanks.

## BearTi | 2018-02-13T19:42:57+00:00
Ah... do you have a configuration advice for Mining on a vServer?
And an idea why my config "cpu-priority" -> "0" doesn´t seems to work?

## Meyer01 | 2018-02-13T19:59:09+00:00
CPU priority doesn't stop the mining process. It just means that if you have two processes that both want CPU time, the one with a higher priority will get it. If you lower mining priority it woud be more comfortable to do other things on PC.

## Zelecktor | 2018-02-13T21:39:22+00:00
if you try xmrig-2.4.4-msvc-win64.zip (when you download on release) you have better performance.

## kimats | 2018-02-25T00:15:08+00:00
@BearTi 
The Doc says the treads depends on the L3 cache,  cryptonight need 4MB L3 cache per thread, can you please set the thread to 1,  guess you will have the same hashrate? but have better feeling when you use the notebook work at the same time?

## g5-freemen | 2018-02-27T22:29:26+00:00
set "max-cpu-usage": from 80 to 100 and feel the difference.
and "cpu-priority": 0 is not good idea i think, better set 1, because miner will not work most of time

**also try to use x64 OS**
and if you will use 64-bit OS try to compare speed of XMRIG GCC and MSVC builds

## g5-freemen | 2018-02-27T22:31:47+00:00
"algo": "cryptonight", "av": 0, "background": false, "colors": true, "cpu-affinity": null, "cpu-priority": 1, "donate-level": 1, "log-file": null, "max-cpu-usage": 100, "print-time": 60, "retries": 5, "retry-pause": 5, "safe": false, "threads": 2

# Action History
- Created by: BearTi | 2018-02-13T11:46:56+00:00
- Closed at: 2018-11-05T12:53:04+00:00
