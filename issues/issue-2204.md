---
title: Hashrate is far lower than expected according to the official Benchmark
source_url: https://github.com/xmrig/xmrig/issues/2204
author: panyi1981
assignees: []
labels:
- question
created_at: '2021-03-24T13:59:59+00:00'
updated_at: '2021-04-12T13:50:20+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:50:20+00:00'
---

# Original Description
hi,everybody
My xmrig hashrate is only 8200 with Ryzen 3700X/Single DDR4 16G 2666/B450 mainBoard, whether in Ubuntu20.04 or in Windows10, using parameters **--randomx-1gb-pages --randomx-cache-qos --cpu-no-yield.**
The expected hashrate is over 11000 from the official Benchmark. Is there any thing I can do to raise the hashrate?
I'd appreciate it very much if everyone could point out something whether in my miner configuration or hardware problem. Thanks a lot
![sn1](https://user-images.githubusercontent.com/37579196/112321677-363b6f00-8ceb-11eb-94a8-e5347f805797.JPG)


# Discussion History
## SChernykh | 2021-03-24T14:04:41+00:00
- You need dual channel (2 sticks of RAM) to achieve maximum performance
- 11000 h/s is a highly overclocked CPU with super-fast RAM (DDR4-3600 CL14 or faster)
- from my experience 9500-10000 h/s is already a good result for 3700X

## panyi1981 | 2021-03-24T14:20:22+00:00
Thank you very much for your advice. I overlooked the RAM frequency before. Could it be possibe to reach 9500 or more in normal mode(without overclock) if I buy another 16G RAM 2666 to make dual channel from your experience?

## SChernykh | 2021-03-24T14:29:56+00:00
I know that you need DDR4-3200 CL14 and a small CPU overclock to 4.1 GHz to reach 10000 h/s. Try to tune your RAM timings, use Ryzen DRAM calculator.

## snipeTR | 2021-03-24T17:58:56+00:00
I was touched to see that the benchmark system created by my suggestion works. you do a very good job @xmrig 

## panyi1981 | 2021-03-25T14:53:14+00:00
@SChernykh Thanks again for your advice. I'll follow your sugguest and have a try.

# Action History
- Created by: panyi1981 | 2021-03-24T13:59:59+00:00
- Closed at: 2021-04-12T13:50:20+00:00
