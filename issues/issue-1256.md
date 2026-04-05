---
title: There is no accept when using Xmrig-Proxy
source_url: https://github.com/xmrig/xmrig/issues/1256
author: ghost
assignees: []
labels:
- question
created_at: '2019-11-01T08:12:42+00:00'
updated_at: '2019-12-22T19:42:50+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:42:50+00:00'
---

# Original Description
I want to ask if the Xmrig-Proxy server configuration affects the hashrate?
I use Xmrig-CPU and Xmrig-Proxy to mine, for a very long time there is no accept.
Can you give me advice.

<img src="https://upanh.vn/images/2019/11/01/2019-10-31_17-44-3914c48d70d5c4fc20.png" alt="2019-10-31_17-44-3914c48d70d5c4fc20.png" border="0" />


# Discussion History
## xmrig | 2019-11-01T12:45:39+00:00
You removed most important part from log, the diff, but if you have a lot of miners and on proxy side is normal share rate (1-2 share per minute) it's fine and expected.
Thank you.

## xmrig | 2019-11-01T18:02:50+00:00
Diff is 626911 miner hashrate is about ~1180, so `626911 / 1180 = 531` seconds or about 9 minutes with 100% effort, so miner screenshot above is OK, in miner lucky there will be 2 or more shares in 9 minutes if not lucky - zero for longer periods it exactly same mechanism how pools (or solo miners) find blocks, but with smaller numbers.

Pool autodiff is also works correctly `626911 / 30` is about 20 kH/s.
Zero hashrate for 1 minute interval is expected too (bad luck), press `h` for other intervals.



## xmrig | 2019-11-01T18:06:12+00:00
Rejected share not look good is other rejected shares with same (null) ip and invalid time?
Thank you.

## ghost | 2019-11-01T18:52:28+00:00
> Rejected share not look good is other rejected shares with same (null) ip and invalid time?
> Thank you.

Do I need to adjust anything in the config? I use noip as the intermediate dns have influence?
I feel Total HashRate is not very stable compared to not using proxy.
Thank you so much!
<img src="https://i.imgur.com/wBD5tF2.jpg" />

## xmrig | 2019-11-01T19:06:36+00:00
Config good, only one thing you can remove wallet address from miner config, less shares count - higher hashrate fluctuation on pool side, more small shares (direct connections or small fixed diff) - more smooth graph, but any pool will be unhappy (shares need be validated on pool side) and can cause ban.
Thank you.

## ghost | 2019-11-01T19:23:58+00:00
@xmrig Thank you so much for your enthusiasm.
I want to ask more. With Proxy I should exploit server 1 cpu or more cpu more effectively.
Another question, with you mining XMR or SUMO brings better returns.

## xmrig | 2019-11-01T19:40:12+00:00
Proxy use single threaded event based architecture with asynchronous network I/O, so it can utilize only one core, but it enough for handle hundreds of thousands connections.

About XMR/SUMO/whatever, it is rhetorical question, I'm not answer, use profit calculators/feelings/etc.

## ghost | 2019-11-02T03:38:49+00:00
> Proxy use single threaded event based architecture with asynchronous network I/O, so it can utilize only one core, but it enough for handle hundreds of thousands connections.
> 
So with high configuration servers should not use Proxy?
I have servers 16-72 CPU.
I mean the mining server, not the proxy server.


## ghost | 2019-11-02T04:50:12+00:00
With XMR, I should choose the PPLNS or PPS. Can you give me a specific pool.
I am new to mining. Sorry for asking you so much.



## 0xman | 2019-11-02T18:00:44+00:00
Sounds like botnet activity lol

## Spudz76 | 2019-11-03T20:49:09+00:00
If you are concerned with profit then use MoneroOcean which will hop algos to whatever is worth the most at the moment.  They do the conversions from the altcoins to XMR for payout so you still only have to handle one wallet for XMR, but earn with any algo they support.  They have their own proxy which handles the coin switching and reporting your mining device hashrates to the pool so it can tell you which algo is most effective for your hardware, and replaces xmrig-proxy completely, works well for me.  Pool has been highly reliable compared to many others, occasionally some maintenance on the frontend/graphs/stats but the backend mining has always worked great, never unreachable.

They also make a fork of xmrig with integrated (direct connection no proxy) upstream hashrate reporting which then allows elimination of the proxy that adds that feature.

Otherwise the answer to what is most useful to mine changes often and would be out of date by the time anyone gave their opinion.  And is different per various CPUs or GPUs capabilities.  Autoswitching solves all that as it tests each algo on each device and bases its decisions on the entire map of what your specific hardware can do best.

The general rule was to use proxy for slow devices, but if you have a device that rips more than 1200H/s by itself then run those direct the proxy is mostly in the way at that point.

I run every device "direct solo proxied" via the multi-miner proxy from ocean, because the grouping proxy switches every device on the proxy to the same algo at the same time which is not optimal unless all the devices are literally identical.  As I run a large mix of CPUs and GPUs it would be worse that way, for me, and so far the pool hasn't complained (~25 devices anywhere from 40H/s up to 2000H/s).

## Spudz76 | 2019-11-03T20:54:26+00:00
There are also two types of proxy, the simpler one is more of a passthrough (pool shows and services each miner separately, via one connection though), the good ones are "merging" the miners into a single virtual miner.  I have not found a CryptoNight proxy that does the merging style, such as ckproxy does for BTC, much less one that can algo-switch.

## ghost | 2019-11-04T13:21:35+00:00
@Spudz76 Do you know dxpool.com with PPS and fee 0.5%. It is reliable ?


# Action History
- Created by: ghost | 2019-11-01T08:12:42+00:00
- Closed at: 2019-12-22T19:42:50+00:00
