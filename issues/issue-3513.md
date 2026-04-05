---
title: rx/arq gpu?
source_url: https://github.com/xmrig/xmrig/issues/3513
author: MTCHANNELL
assignees: []
labels: []
created_at: '2024-07-21T09:59:39+00:00'
updated_at: '2025-06-18T22:09:30+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:09:30+00:00'
---

# Original Description
Hello. I have 10 "rx580". I want to mine in the "rx/arq" algorithm with these. But I always get a rejected error. I don't have any problems when doing it with the CPU. I'm only having trouble doing it with the gpu. I am using the latest driver.
1-) Which driver version should I use?
2-) Which xmrig version should I use?
I have friends who say they are doing rx/arq mining using gpu, but they do not give details. I didn't see it with my own eyes. That's why I want to consult with you. Thank you in advance for your interest.

# Discussion History
## SChernykh | 2024-07-21T10:09:41+00:00
RandomX (and its variants) is very slow on GPU, but if you want to try it on RX-580, you should try old AMD drivers from around 2020, and use Windows 10.

## MTCHANNELL | 2024-07-21T11:19:46+00:00
right now;
1-) I am using windows 11
2-) "https://drivers.amd.com/drivers/radeon-software-adrenalin-2020-21.10.1-win10-win11-64bit-oct5.exe" .. I tested this driver version but it continues to be rejected .
Upgrading to Windows 10 is very difficult at the moment:( I have a lot of applications I use and it would take me 2 days to install them all one by one. I guess there is nothing to do.

extra question;
So, when you make a new update for xmrig, is there any chance you can make it work with the new driver versions of "rx570 polaris"? I know it may seem unnecessary. But I like mining "rx/arq". earnings are not important. Go with CPU. I would be very happy if I could do it with GPU as well.

## SChernykh | 2024-07-21T11:23:57+00:00
It doesn't make sense to continue supporting RandomX on GPU because performance is too low to be practical. You can get 10x profit per kWh of electricity basically on any GPU coin, compared to RandomX. So RandomX GPU support is limited to OS and driver combinations that were popular in 2019-2020 when RandomX just came out.

## MTCHANNELL | 2024-07-22T08:16:26+00:00
1-) win11-22621.2715
2-) rx570 gpu driver : radeon-software-adrenalin-2020-21.3.1-win10-64bit-mar24
3-) xmrig 6.21.3
I managed to mine the "rx" algorithm with GPU. I achieved my goal :) I get 1.8khs hashrate with xfx Rx570 8gb 256bit. room temperature 35.5 degrees. The GPU can mine at 54 degrees at stock settings. Mine was an adventure :)

# Action History
- Created by: MTCHANNELL | 2024-07-21T09:59:39+00:00
- Closed at: 2025-06-18T22:09:30+00:00
