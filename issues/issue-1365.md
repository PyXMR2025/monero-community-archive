---
title: Is the new 5.1.0 version sacrifying the stability for the performance increment?
source_url: https://github.com/xmrig/xmrig/issues/1365
author: JeffreyChu2009
assignees: []
labels:
- bug
created_at: '2019-12-02T06:04:36+00:00'
updated_at: '2019-12-04T10:37:14+00:00'
type: issue
status: closed
closed_at: '2019-12-04T10:37:13+00:00'
---

# Original Description
My TR2920X was working @4GHz_DDR4-3200 very stable in the previous 5.0.1 gcc_win64 version all day long.

I updated to the latest 5.1.0 msvc_win64 version, copying the current config.json file from the previous 5.0.1 version folder to the new 5.1.0 version folder. Run the "start.cmd"... Voila! The hashrate does increase a little bit for Ryzen in the new version. Yet, after 5~10 minutes, the computer frozes and I have to restart the machine.

My mining environment has nothing changed except for shifting from 5.0.1 to 5.1.0, so I have to suspect that the newly released version maybe sacrifying the stability for the performance.

# Discussion History
## shehi | 2019-12-02T14:12:57+00:00
In past I was using xmrig (when it was CPU only) and xmrig-nvidia, both working simultaneously, with mild system slowness. Now with the latest xmrig which bundles CUDA as well, I get more freezing when CUDA is enabled. Guess the new version is pushing harder.

## JeffreyChu2009 | 2019-12-02T14:39:48+00:00
> In past I was using xmrig (when it was CPU only) and xmrig-nvidia, both working simultaneously, with mild system slowness. Now with the latest xmrig which bundles CUDA as well, I get more freezing when CUDA is enabled. Guess the new version is pushing harder.

Yep, I feel the same way. In fact, the 5.0.1 version is not as stable as the previous 4.6.x beta though it's definitely more stable than the latest 5.1.0 one.

## SChernykh | 2019-12-02T14:56:21+00:00
Normally, computer shouldn't just freeze under any load. It seems that your TR2920X is overclocked a bit over the limit.

## JeffreyChu2009 | 2019-12-02T15:42:38+00:00
> Normally, computer shouldn't just freeze under any load. It seems that your TR2920X is overclocked a bit over the limit.

Well, it's totally OK in the previous versions. Plus, I've clocked it down to 3.9GHz already.

## SChernykh | 2019-12-02T15:52:08+00:00
New version has a bit higher hashrate, so it puts more load on CPU. If it was already on the edge, it will fail. There's nothing unusual in the new code, it can't just freeze entire system.

## JeffreyChu2009 | 2019-12-02T16:10:57+00:00
> New version has a bit higher hashrate, so it puts more load on CPU. If it was already on the edge, it will fail. There's nothing unusual in the new code, it can't just freeze entire system.

I don't know why you just stick to the theoretical "can't, can't can't", and ignore the fact.
Actually, TR2920X's upper limit for overclocking is around 4.2~4.3GHz @1.4V yet I only use it 4.0GHz @1.3V which is far away from the edge, not to mention with a 360mm AIO keep it working under 60°C.

## SChernykh | 2019-12-02T16:28:46+00:00
If the whole system freezes it means your system is unstable. It can be not only CPU but your RAM. Try to run Prime95 on all cores, then MemTest86 and some other heavy tests to be sure.

## JeffreyChu2009 | 2019-12-03T01:08:58+00:00
> If the whole system freezes it means your system is unstable. It can be not only CPU but your RAM. Try to run Prime95 on all cores, then MemTest86 and some other heavy tests to be sure.

It is so BOLD of you to judge the others by your own wretched anticipation. My whole system is quite stable using the previous versions, and can pass Prime95 on all cores at least 60 minutes... on and on.

Plus, I am using the 4 DIMMs of Klevv DDR4-3200 16GB modules on the Asus X399-E mainboard, which are the most compatible RAM and chipset for the Zen+ architecture's Threadripper CPUs. To avoid your so called unstable factors, I set the RAM in the BIOS to run slower at 2933MHz, which is the TR2000 CPU's official support RAM speed, even though the whole system was running heavenly stable at 3200MHz RAM speed using 5.0.1 and 4.6.x versions.

This is it. I don't need your useless comments any more. I've shifted back to 5.0.1 instead of the radical 5.1.0 already. Thanks a lot for letting me learn how a coder could be judgemental and ignorance.

## xmrig | 2019-12-03T02:13:47+00:00
@JeffreyChu2009 can you check current dev branch? with new option `yield` set to `true` https://github.com/xmrig/xmrig/blob/dev/src/config.json#L28 this option revert back `std::this_thread::yield();` call removed in v5.1.0, it should increase system responsive on full load and may positive affect stability.
Thank you.

## SChernykh | 2019-12-03T06:21:30+00:00
If it's not hardware freeze then it can be something else. What do you have for "priority" in your config.json? If it is what I think it is, then setting higher priority may introduce severe lags/freezes with 5.1.0

## monero101 | 2019-12-03T09:43:17+00:00
@JeffreyChu2009  Chill out dude, you didn't provide any system or miner logs so it was a good guess by the devs. 

## JeffreyChu2009 | 2019-12-03T12:49:00+00:00
> @JeffreyChu2009 can you check current dev branch? with new option `yield` set to `true` https://github.com/xmrig/xmrig/blob/dev/src/config.json#L28 this option revert back `std::this_thread::yield();` call removed in v5.1.0, it should increase system responsive on full load and may positive affect stability.
> Thank you.

Thanks. Problems solved by your solution, really helpful.

## xmrig | 2019-12-04T10:37:13+00:00
v5.1.1 released, `yield` option enabled by default.
Thank you.

# Action History
- Created by: JeffreyChu2009 | 2019-12-02T06:04:36+00:00
- Closed at: 2019-12-04T10:37:13+00:00
