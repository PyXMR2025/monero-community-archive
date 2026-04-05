---
title: I tried switching USDT versions in Zergpool now can't mine gprx for some reason
source_url: https://github.com/xmrig/xmrig/issues/3334
author: Jinxsyns
assignees: []
labels: []
created_at: '2023-09-18T20:36:39+00:00'
updated_at: '2023-09-18T21:44:30+00:00'
type: issue
status: closed
closed_at: '2023-09-18T21:44:30+00:00'
---

# Original Description
**Describe the bug**
I've been mining gprx on my AMD 7950x for roughly a week then yesterday in an effort to not have to mine 200 dollars off of 1 cpu to be able to be paid to my wallet (was mining gprx being paid out in USDT TRC20) I tried switching to USDT BEP20 and now all of a sudden the miner won't open at all. Where before I would click on it it would bring up a text window then it would auto show up run as admin (set it in the xmrig executable for the msr mod specifically) click yes and xmrig would start and begin mining. Now when I try to run the batch file all of a sudden the first text window doesn't show up and no run as admit will show up. It will just flash a window up and instantly close.

**To Reproduce**
Everything else works RTM ghostrider example works. Clicking the XMrig executable works just fine. solo mine example works fine. same with benchmarks. I have no clue what I did

**Expected behavior**
It to run? i apolgize if that seems the wrong way.

**Required data**
 - Miner log as text or screenshot: I don't have one because it won't start i'm sorry
 - Config file or command line (without wallets) this is what is written in the batch file directly copied from Zergpool which worked fine a week ago. 

-a ghostrider -o stratum+tcp://ghostrider.na.mine.zergpool.com:5354 -u  --timeout 120 -p  c=USDT-BEP20,mc=GPRX
 
- OS: Windows 11
 - For GPU related issues: information about GPUs and driver version.: only cpu mining with xmrig

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2023-09-18T20:47:31+00:00
> It will just flash a window up and instantly close.

Add `pause` at the end of the batch file, and it will not close until you press a button. Then you will see what error you get.

## Jinxsyns | 2023-09-18T21:27:08+00:00
Here's what it said. I did notice it say -a is not a valid command so I tried -algo like I thought I would see in other xmrig files but that didn't work either. threw the same error just said -algo is not recognized

![Screenshot 2023-09-18 162621](https://github.com/xmrig/xmrig/assets/130711085/ec2c5202-707d-4ea2-a827-2dc20d6fcbe5)

## geekwilliams | 2023-09-18T21:38:56+00:00
Based on your error, you're not calling the xmrig executable. Add ".\xmrig.exe" before the -a

## Jinxsyns | 2023-09-18T21:44:30+00:00
I got it to work with that thank you so much!

# Action History
- Created by: Jinxsyns | 2023-09-18T20:36:39+00:00
- Closed at: 2023-09-18T21:44:30+00:00
