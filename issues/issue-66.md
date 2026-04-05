---
title: cpu not fully utilized
source_url: https://github.com/xmrig/xmrig/issues/66
author: anandanand84
assignees: []
labels:
- NUMA
created_at: '2017-08-20T20:39:23+00:00'
updated_at: '2017-11-27T00:27:27+00:00'
type: issue
status: closed
closed_at: '2017-09-03T03:05:43+00:00'
---

# Original Description
I am running xmrig on xeon Dual E5620 with below config (with 100% max usage) and huge pages enabled but it doesn't utilize full cpu. I get hashes around 240 h/s where I expect it to be around 370+ h/s.

<img width="233" alt="screen shot 2017-08-20 at 3 29 04 pm" src="https://user-images.githubusercontent.com/5538452/29498209-cb2a564c-85bc-11e7-898e-bea12e8b76ea.png">


<img width="603" alt="screen shot 2017-08-20 at 3 30 30 pm" src="https://user-images.githubusercontent.com/5538452/29498207-c1612ffa-85bc-11e7-8131-8386513e31ab.png">

When I get the top the cpu utillization is at 600% which means 2 cores are not utilized.

<img width="615" alt="screen shot 2017-08-20 at 3 11 45 pm" src="https://user-images.githubusercontent.com/5538452/29498222-ff1f57d6-85bc-11e7-9ab0-af73db60370a.png">

How to get all cpu cores utilized.


# Discussion History
## xmrig | 2017-08-21T08:45:28+00:00
Please try manually set `"threads": 12,`
Your system is dual socket or has 2 NUMA nodes with single CPU in each node?
Thank you.

## xmrig | 2017-08-21T08:49:29+00:00
Something wrong with CPU count detection, Mac Pro, is normal dual socket. Windows running on it, detect CPU count correctly.

## tigermine | 2017-10-10T18:08:42+00:00
it is looking like you were successful to able to run the CPU mining ... I am new to programming and not so efficient so could you please advice which command line did you use after building the file I have followed all the steps from here 

https://github.com/xmrig/xmrig/wiki/OS-X-Build

![image](https://user-images.githubusercontent.com/32683382/31402607-c86e4a14-adf6-11e7-9ba3-3c67b3b4e25c.png)

but after it is build I am not sure which command line to run to start the mining as you have shown in the above screenshot 

I would be glad if you can help me on this.... 



Thanks,
T

## atarate | 2017-10-10T18:17:38+00:00
are you using clang? I have seen this error with clang
try using GCC and G++ instead

## tigermine | 2017-10-10T18:49:04+00:00
I am on mac and no I am not using clang so what command i should write normally in windows if you write "xmrig.exe ..... -o... -u ..." mining start from respective pool .. so in this case if i want to start mining on mac what command line i should be using.. "xmrig.?"

Thanks,
T

## xmrig | 2017-10-10T19:03:51+00:00
It not a error it just a warning can simple ignore it. Also this warning was fixed in recent commits.

Use:
`./xmrig ...`

@atarate clang it default compiler for OS X.

## tigermine | 2017-10-10T19:17:06+00:00
@atarate  thanks a lot bud.. I will try it and let you know the result I am on other place and dont have my mining mac with me.. 

Regards,
T

# Action History
- Created by: anandanand84 | 2017-08-20T20:39:23+00:00
- Closed at: 2017-09-03T03:05:43+00:00
