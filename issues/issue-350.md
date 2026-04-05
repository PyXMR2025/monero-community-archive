---
title: Raspberry Pi-3B-Centos7 xmrig config.json
source_url: https://github.com/xmrig/xmrig/issues/350
author: rainmo
assignees: []
labels:
- arm
created_at: '2018-01-19T03:10:15+00:00'
updated_at: '2018-01-22T02:54:35+00:00'
type: issue
status: closed
closed_at: '2018-01-19T06:21:40+00:00'
---

# Original Description
I get a new problem. It can't display hash num. How do I modify this settings?
**speed 2.5s/60s/15m n/a 13.3 13.1 H/s max: n/a H/s**

And, What settings is more better for Raspberry Pi-3B?  when I run xmrig, it used too much cpu.Thank you. 

%Cpu(s): 99.9 us, 





# Discussion History
## xmrig | 2018-01-19T06:31:48+00:00
2.5s hashrate report is buggy on low hashrate it know issue. `cryptonight-lite` only usable for AEON coin.
If you closed this issue looks like you found `threads` option :)

Please check this issue https://github.com/xmrig/xmrig/issues/325 may help increase performance.
Thank you.

## rainmo | 2018-01-20T01:30:39+00:00
@xmrig So kind of you. yes, I found "threads" option.
Seriously,  I can not understand #325  now. Maybe need more time to... 
Thank you.

## kyle-go | 2018-01-21T04:55:02+00:00
@rainmo  Is he reason of "n/a H/s" is the program run too slow?  how do you fixed it?  I tried add 
CFLAGS="-mcpu=cortex-a53 -mfloat-abi=hard -mfpu=neon-fp-armv8 -mneon-for-64bits -mtune=cortex-a53" to compile.  
But it not work!  
thx.

I got the flags from here : https://gist.github.com/fm4dd/c663217935dc17f0fc73c9c81b0aa845

## rainmo | 2018-01-22T02:25:36+00:00
@kylescript Hi, buddy. Show me your config.json settins and your linux distribution.
And can you tell me how to use the flags when you complied xmrig. Thanks.

## rainmo | 2018-01-22T02:54:35+00:00
@kylescript Did you modified these code？RP-3B has a ArmV8 CPU, But  when I show cpu edtion, it displays Armv7l. So I do not know what really is. We can discuss it. 
  if (XMRIG_ARMv8)
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -march=armv8-a+crypto")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=armv8-a+crypto -flax-vector-conversions")
    elseif (XMRIG_ARMv7)
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -mfpu=neon")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mfpu=neon -flax-vector-conversions")

# Action History
- Created by: rainmo | 2018-01-19T03:10:15+00:00
- Closed at: 2018-01-19T06:21:40+00:00
