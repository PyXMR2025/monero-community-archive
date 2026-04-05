---
title: how to optimize Config for AMD 7702
source_url: https://github.com/xmrig/xmrig/issues/2364
author: decstgc
assignees: []
labels: []
created_at: '2021-05-10T06:57:44+00:00'
updated_at: '2021-06-14T03:22:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
hi everybody 

I'm using a PC with Dual AMD 7702 , 16X2G memory  for Monero mining ,  pool is : supportxmr . HUGE PAGES is permission granted. 

Now my miner speed is 21K in total , but based on XMRig benchmark , dual AMD 7702 should has a speed around 80K . 

Anything I can do to optimize my speed ? how to config JSON CONFIG file ? 

I need your help !

# Discussion History
## Spudz76 | 2021-05-10T07:21:59+00:00
Show initial output of xmrig for memory type and speeds and etc.

Memory should be clocked to 3800+ or as near as possible.  Check benchmark top result, click Memory header, it shows what speeds they had (and model number, even).  Usually +600 on 3200 MHz RAM needs overvolting also and either XMP mode or customized timings CAS/RAS/etc (benchmark result doesn't show that).  Usually searching for model number of your RAM and overclock gives some results to try.

## Spudz76 | 2021-05-10T07:28:10+00:00
Looks like most all of the 7702 results are at 3200, maybe overclock not possible... Ryzens like 3800

So mostly need to see some output.  Also, windows or linux?

## decstgc | 2021-05-10T07:43:14+00:00
> Looks like most all of the 7702 results are at 3200, maybe overclock not possible... Ryzens like 3800
> 
> So mostly need to see some output.

 Thank  you man ! I will update my output later, here are some screen shoots for your ,this may helps.....

http://tiebapic.baidu.com/forum/pic/item/6654951090ef76c6181d0f9b8a16fdfaae51673a.jpg
http://tiebapic.baidu.com/forum/pic/item/b90e9b51352ac65c84ca92c3ecf2b21192138a3a.jpg
http://tiebapic.baidu.com/forum/pic/item/240fbb167f3e670938cfb14f2cc79f3df9dc553a.jpg




## SChernykh | 2021-05-10T07:47:01+00:00
AMD EPYC has 8 memory channels, and you have 2 CPUs. You need 8 memory modules per CPU, 16 sticks in total. And you have only 2 sticks, this is why it's so slow.

## decstgc | 2021-05-10T07:51:54+00:00
> AMD EPYC has 8 memory channels, and you have 2 CPUs. You need 8 memory modules per CPU, 16 sticks in total. And you have only 2 sticks, this is why it's so slow.

Thank you! I will upgrade it to 256G soon !

## Spudz76 | 2021-05-10T17:32:31+00:00
Oops I read 16 x 2GB as sixteen sticks of 2GB

But now I realize you can't get 2GB sized DDR4 so that must be "backward" meaning it's actually 2 x 16GB

You only need 16 x 4GB I'd get rid of the 16GB's unless you need memory for something else.

## decstgc | 2021-05-11T05:46:55+00:00
> > AMD EPYC has 8 memory channels, and you have 2 CPUs. You need 8 memory modules per CPU, 16 sticks in total. And you have only 2 sticks, this is why it's so slow.
> 
> Thank you! I will upgrade it to 256G soon !

problem solved ,,,,,,Great thanks ,man !

## decstgc | 2021-05-11T05:48:27+00:00
> Oops I read 16 x 2GB as sixteen sticks of 2GB
> 
> But now I realize you can't get 2GB sized DDR4 so that must be "backward" meaning it's actually 2 x 16GB
> 
> You only need 16 x 4GB I'd get rid of the 16GB's unless you need memory for something else.

it's typo...my mistake ,,, now the problem has been solved, thank you man !

## dasdqww | 2021-06-14T03:22:01+00:00
> > > AMD EPYC 有 8 個內存通道，你有 2 個 CPU。每個 CPU 需要 8 個內存模塊，總共 16 個內存條。而且你只有 2 根棍子，這就是為什麼它這麼慢。
> > 
> > 
> > 謝謝！我會盡快升級到256G！
> 
> 問題解決了，，，，，，非常感謝，伙計！

It's hard to tell, how did you do it? thx man

# Action History
- Created by: decstgc | 2021-05-10T06:57:44+00:00
