---
title: '#Huge page problem in android'
source_url: https://github.com/xmrig/xmrig/issues/1892
author: Saikatsaha1996
assignees: []
labels: []
created_at: '2020-10-13T12:12:03+00:00'
updated_at: '2024-03-25T16:37:21+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:45:55+00:00'
---

# Original Description
![Screenshot_20201013-173252](https://user-images.githubusercontent.com/72664192/95858508-d6738c00-0d7a-11eb-88ac-0780db8ca685.png)
Anyone can help me?
Its xmrig 6.3.5 in android
I got 340 h/s in my mobile
And showing huge page supported but showing huge page 0% how can I solve it please help..

# Discussion History
## Lonnegan | 2020-10-13T16:18:21+00:00
To lock huge pages, the RAM mustn't be fragmented. When an Android device has been on already for a few days, there isn't a free contiguous RAM section anymore. Reboot your smartphone and it should work :)

## Saikatsaha1996 | 2020-10-13T16:21:27+00:00
If i reboot my mobile so my all termux data gone.. how can i saved my termux data?

## Lonnegan | 2020-10-13T16:37:09+00:00
Google for "Backing up Termux" ;)

## xerox87 | 2020-10-19T04:59:06+00:00
where to get xmrig-notls on linux?

## paypur | 2020-12-18T00:25:40+00:00
> To lock huge pages, the RAM mustn't be fragmented. When an Android device has been on already for a few days, there isn't a free contiguous RAM section anymore. Reboot your smartphone and it should work :)

This is not working for me, my phone has 8gbs of ram so It should work

## FrankHB | 2020-12-21T10:10:00+00:00
> This is not working for me, my phone has 8gbs of ram so It should work

8 GB won't work after a few days, esp. the miner can be killed frequently. In my experience, even a 16 GB device would probably fail. 40 GB can work without worry.



## Spudz76 | 2020-12-22T05:33:23+00:00
You can reserve hugepages at boot time (or early after boot) with sysfs or kernel args, google about it (not sure exact methods for Android) ...  But then nothing else but the miner can use that region ever, which might make OOM for other things, or even boot failure.

Some CPUs don't get any gains from it anyway, it might not be a real problem.

## abyssbad | 2024-01-23T22:12:05+00:00
Hola cuál es el procedimiento por favor quisiera saber

## abyssbad | 2024-01-23T22:30:57+00:00
Necesito el procedimiento exacto para habilitar hugepages en mi Android estoy usando app userland Ubuntu... Con xmrig... Actualmente minando con 194h/s pero si ha levantado un poco más en un solo dispositivo... Coloco varios pero quiero usar más memoria y levantar más los h/s

## ChaoLine892 | 2024-03-25T16:37:20+00:00
for enable hugepages use kernel with support hugepages and su with magisk or supersu

# Action History
- Created by: Saikatsaha1996 | 2020-10-13T12:12:03+00:00
- Closed at: 2021-04-12T14:45:55+00:00
