---
title: RandomX crash on ARM
source_url: https://github.com/xmrig/xmrig/issues/1318
author: willwill85
assignees: []
labels:
- enhancement
created_at: '2019-11-27T06:07:51+00:00'
updated_at: '2026-01-18T15:11:36+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:28:03+00:00'
---

# Original Description
I build 5.0.0 version 
and test the application
After the line “ rx allocated 2336MB（2080+256） huge pages 0%/1168 +JIT（3ms）”
the application is killed

CPU is  ARM （4 core A53） 512MB RAM

# Discussion History
## SChernykh | 2019-11-27T13:39:53+00:00
Maybe because 512 MB RAM is not enough for mining? XMRig will try to mine only with 256 MB in light mode, but even this can fail if you only have 512 MB.

## willwill85 | 2019-11-28T01:27:47+00:00
> Maybe because 512 MB RAM is not enough for mining? XMRig will try to mine only with 256 MB in light mode, but even this can fail if you only have 512 MB.

how can i switch to light mode?  with what parameters? Thanks

## SChernykh | 2019-11-28T06:54:14+00:00
XMRig tries to switch to light mode automatically but fails in your case. You probably need to add 512 MB swap file to make it work.

## xmrig | 2019-11-29T06:34:41+00:00
In next version v5.1 (code available in dev branch) added new option `mode` for RandomX, with 3 possible values:

- `auto` new behavior, miner will not try allocate dataset if system has not enough total memory.
- `fast` old behavior, miner will try allocate dataset and only if it fails and system did't kill miner, switch to light mode.
- `light` force light (slow) mode.

However, `auto` mode required additional testing.

In addition miner will print information about memory on startup and this information also added to API.
Thank you.

## willwill85 | 2019-12-05T08:06:47+00:00
> In next version v5.1 (code available in dev branch) added new option `mode` for RandomX, with 3 possible values:
> 
> * `auto` new behavior, miner will not try allocate dataset if system has not enough total memory.
> * `fast` old behavior, miner will try allocate dataset and only if it fails and system did't kill miner, switch to light mode.
> * `light` force light (slow) mode.
> 
> However, `auto` mode required additional testing.
> 
> In addition miner will print information about memory on startup and this information also added to API.
> Thank you.

I built 5.1.1 version, and test light mode and auto mode.
But the application killed..




## SChernykh | 2019-12-05T10:04:34+00:00
With only 512 MB RAM you have to add swap file (512 MB or bigger) to fix the crash. You just don't have enough memory for XMRig even in light mode.

## 1265578519 | 2022-03-08T18:38:51+00:00
windows版本randomx经常导致突然切换 rx/0 算法后爆掉内存引起死机

关键日志
[2022-03-09 00:58:48.923] randomx init dataset algo rx/0 (2 threads) seed 32edb000247493a7...
[2022-03-09 00:58:48.923] randomx allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2022-03-09 00:59:12.524] randomx dataset ready (23601 ms)
[2022-03-09 00:59:48.667] net new job from mine.c3pool.com:80 diff 8532 algo rx/0 height 2575216 (12 tx)
[2022-03-09 00:59:48.889] net dev donate finished
[2022-03-09 00:59:48.898] net new job from mine.c3pool.com:17777 diff 2897 algo astrobwt height 6665492
[2022-03-09 00:59:48.912] cpu stopped (5 ms)

配置文件randomx字段
```
    "randomx": {
        "init": -1,
        "init-avx2": 0,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
```
https://github.com/xmrig/xmrig/issues/1318#issuecomment-559676080
https://xmrig.com/docs/miner/randomx-optimization-guide
https://xmrig.com/docs/miner/command-line-options
找到了些资料，表明出在 Windows 上 4GB 内存可能没有足够的内存运行系统进程，auto（fast）模式下单路CPU需要2080+256MB开销。

默认值auto，可选值auto, fast, light
所以解决办法就是改成 light ，或者禁掉rx/0算法，，，此时运行过程就不会占用任何内存了。
性能对比，差了快十倍
auto（fast）模式下570H/s
light模式下74H/s

所以我决定锁定astrobwt算法。。然后猜猜我看到了什么，astrobwt-avx2
--astrobwt-avx2 | enable AVX2 optimizations for AstroBWT algorithm
性能对比，接近两倍提升
false模式下95H/s
true模式下162H/s



补充下
![1](https://user-images.githubusercontent.com/6442439/158659213-6da7c669-d389-4e57-b76f-a694f94f8adb.png)

我算是知道，，为什么内存炸了
原来就是被抽1分钟导致算法切换引起的
"mode": "light",
终极爆内存解决办法auto改成light
这样就没事了。。
关键字dev donate started 代表开始抽水，dev donate finished抽水完成，然后会产生输出信息randomx切换算法，导致配置文件使用~锁定ast，和rx0值写0无效，还是被切上去就炸内存了。

## UnixCro | 2026-01-18T15:11:36+00:00
> XMRig will try to mine only with 256 MB in light mode

What exactly is light mode? How does XMRIG work in it compared to fast mode? Why does XMRIG use 2MB of RAM when it already has 2MB of L3 cache? And why doesn't XMRIG access the 2MB of L2 cache directly as L3? This is especially helpful with M1. Why don't Apple Silicon users get a message that MSR hasn't been set?

Sorry for all the questions.

Thank you for everything!


# Action History
- Created by: willwill85 | 2019-11-27T06:07:51+00:00
- Closed at: 2021-04-12T15:28:03+00:00
