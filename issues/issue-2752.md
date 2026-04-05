---
title: XVH Heaven thread# self-test failed
source_url: https://github.com/xmrig/xmrig/issues/2752
author: Maythecoffee
assignees: []
labels: []
created_at: '2021-11-29T17:54:46+00:00'
updated_at: '2021-11-29T19:26:45+00:00'
type: issue
status: closed
closed_at: '2021-11-29T19:26:45+00:00'
---

# Original Description
**Describe the bug**
running 6.16. version  appeared error 
thread #1 self-test failed
and the same for al lthreads. 

i tried to run 6.7.0 - everything works fine.
another case threads q-ty are 16 not 32 even i run 6.7.0 version 
**To Reproduce**
xmrig.exe -a cn-heavy/xhv -o haven.herominers.com:10451 -u hvs1YiVcVZQ2n8UQx1a4xA1EkRDCGmZdGPmUsSS2HqWu8noPsH6Lfb3cad6aBjdiEzd5i6ox1f7xcgAWiePNPa9c4tnhZC3ASe -k --tls -p 5950PC


![IMG_7273](https://user-images.githubusercontent.com/92730184/143918597-62914b56-7a3a-4324-b987-3fdc8dcc9866.jpg)
![IMG_7274](https://user-images.githubusercontent.com/92730184/143918605-0a0c91df-06e8-4d0c-9279-70e0430806d3.jpg)




# Discussion History
## SChernykh | 2021-11-29T17:59:19+00:00
Try version v6.16.1, it should work fine with cn-heavy again.

## Lonnegan | 2021-11-29T18:02:15+00:00
> another case threads q-ty are 16 not 32 even i run 6.7.0 version

That's fine. Haven algo is a cn/heavy-variant, which has a scratchpad size of 4 MB per thread. Your CPU has 64 MB last level cache. 64 MB / 4 MB per thread = 16 threads. That's why xmrig starts 16 threads on your CPU. Would it start more than 16 threads, the data won't fit into the last level cache anymore and the CPU would have to access the slow DRAM. That would decrease your hashrate massively!

## Maythecoffee | 2021-11-29T18:03:31+00:00
> Try version v6.16.1, it should work fine with cn-heavy again.

no

## Maythecoffee | 2021-11-29T18:04:18+00:00
> > another case threads q-ty are 16 not 32 even i run 6.7.0 version
> 
> That's fine. Haven algo is a cn/heavy-variant, which has a scratchpad size of 4 MB per thread. Your CPU has 64 MB last level cache. 64 MB / 4 MB per thread = 16 threads. That's why xmrig starts 16 threads on your CPU. Would it start more than 16 threads, the data won't fit into the last level cache anymore and the CPU would have to access the slow DRAM. That would decrease your hashrate massively!

right, thank you, so 16T is normal mode for that!  but anyway new version is not working right now

## Lonnegan | 2021-11-29T18:07:29+00:00
Is 6.15.3 working for you? It's the last one without

a. massive code addition for Ghostrider and
b. making a difference between Zen 3 Vermeer and Cezanne

Unfortunately, I can't countertest because I only have Zen 2 based CPUs.

## Maythecoffee | 2021-11-29T18:14:28+00:00
i ve just checked 15.3 also  - works fine!
1350 h/s vs 1270 in 6.7.0!

## Lonnegan | 2021-11-29T18:20:13+00:00
Ok, 6.16.1 works with Haven on Zen 2, as well. So it must have something to do with the Zen 3 optimizations, either VAES or the Cezanne vs. Vermeer thing.

## SChernykh | 2021-11-29T18:29:10+00:00
@Maythecoffee Version v6.16.1 MSVC works on Zen3 too, I just tested.

## Maythecoffee | 2021-11-29T19:26:31+00:00
> @Maythecoffee Version v6.16.1 MSVC works on Zen3 too, I just tested.

sorry. that can be my mistake, i tried on 16.1 and yes it is working. so option one i tried only 16.0 both times (wrong shortcut? or option 2  my stupid head)) 

# Action History
- Created by: Maythecoffee | 2021-11-29T17:54:46+00:00
- Closed at: 2021-11-29T19:26:45+00:00
