---
title: cn-heavy/xhv and Ryzen 5 5600X actually only works with parameter "--asm=none"
source_url: https://github.com/xmrig/xmrig/issues/2156
author: termi-1
assignees: []
labels:
- bug
created_at: '2021-03-04T01:09:29+00:00'
updated_at: '2021-04-12T14:06:09+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:06:09+00:00'
---

# Original Description
This happens with Version 6.90,
xmrig terminates itself, System Windows 10

An older Version, e.g. 6.32 is working

# Discussion History
## SChernykh | 2021-03-04T07:18:28+00:00
Can you paste your full xmrig command line here (you can remove wallet address)?

## termi-1 | 2021-03-04T08:09:51+00:00
normal, i am working only with config-file.

the alternative batch-file (with intel it is working):

.\xmrig.exe -a cn-heavy/xhv -t 5 -o haven.herominers.com:10451 -u hvx...

The last four lines of xmrig with amd ryzen 5 5600X:

[2021-03-04 08:55:11.121]  net      use pool haven.herominers.com:10451  168.119.11.231
[2021-03-04 08:55:11.121]  net      new job from haven.herominers.com:10451 diff 30000 algo cn-heavy/xhv height 0
[2021-03-04 08:55:11.331]  msr      register values for "ryzen_19h" preset have been set successfully (209 ms)
[2021-03-04 08:55:11.331]  cpu      use profile  *  (5 threads) scratchpad 4096 KB

After this, xmrig stop working and it is the normal cmd-line.


## SChernykh | 2021-03-04T08:12:57+00:00
Yes, I confirm it crashes with this command line. Remove `-t 5` until the fix is ready.

## Lonnegan | 2021-03-04T23:33:07+00:00
Hm, can you explane this fix, please? I don't understand what's going on here. "Round up number of threads to the multiple of 8". Why? And why only on Zen 3? And when I look at the code, it looks different, again. 

const size_t N = ((m_threads + 7) / 8) * 8;

The user who reported the bug used 5 as m_threads. So 5+7 makes 12, divided by 8 is 1.5 * 8 = 12. But 12 is not a multiple of 8. And are now 12 threads running, although the user wanted to use just 5? Please help me to understand what's going on here. :)

## termi-1 | 2021-03-05T02:01:47+00:00
hi,
perhaps you thinking wrong. I don´t really understand, what you mean.
With the parameter (-t) you can control, how much threads (cores of the cpu) should be used. You can mine with, 1 thread, 2, 3, 4 or more. The limitation is the cpu and the algo.

Error occurs with zen 3 together with thread-count and algo cn-heavy and asm=ryzen (auto)
Without thread-count cn-heavy is working  (8 threads on ryzen 5 5600X)
With cryptonight-turtle there is no problem with thread-count!
Other algos i have not tested with xmrig V 6.90

SChernykh understood this problem ;-)


## SChernykh | 2021-03-05T07:17:16+00:00
@Lonnegan Memory allocation needs number rounded up to 8 because this is how this Zen3 cn-heavy optimization works.

## Lonnegan | 2021-03-05T07:46:06+00:00
@termi-1
I know what the parameter threads does. I've asked for the formula. When the user sets 5 as -t in the command line as you did I get 12 as N with that formula and not 8. That's what I asked.

## SChernykh | 2021-03-05T07:48:04+00:00
@Lonnegan this is now how C/C++ works here. You'll get 8.

## Lonnegan | 2021-03-05T08:06:49+00:00
@SChernykh ahhh, thank you for the explanation. I have (once again) overlooked the fact that C/C++ uses the same operators for integer division without decimal places as for floating point calculations. In other languages e.g. Delphi you would use div here instead of /. Thanks, I've got it now. 

# Action History
- Created by: termi-1 | 2021-03-04T01:09:29+00:00
- Closed at: 2021-04-12T14:06:09+00:00
