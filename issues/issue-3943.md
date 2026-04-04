---
title: run as admin when installing P2Pool in GUI wallet
source_url: https://github.com/monero-project/monero-gui/issues/3943
author: TheColetrain
assignees: []
labels: []
created_at: '2022-06-09T19:56:49+00:00'
updated_at: '2023-07-15T19:40:12+00:00'
type: issue
status: closed
closed_at: '2022-06-10T18:06:47+00:00'
---

# Original Description
you need to run the GUI wallet as Admin when installing P2Pool and starting to mine.   Requesting that added to the error message, or in the wallet as text.  It seems so simple now, but for a while until I did a lot of digging, It didn't work.  I was new to it.. and so I was not sure what to expect.

# Discussion History
## selsta | 2022-06-10T16:15:31+00:00
Did you use the .exe installer or the .zip?

## TheColetrain | 2022-06-10T16:32:35+00:00
I already had the GUI wallet running on Windows 10.  So i just selected P2P pool.  and when you hit "mine" it should install.  However, since I didnt know to run the GUI wallet as admin, it failed.   And this is my point.  there was no clear explanation in the error message or in the GUI wallet that mentioned something so simple as "run as admin"

## selsta | 2022-06-10T16:33:41+00:00
Yes, what I'm asking is how did you install the GUI wallet? Did you use the installer or the .zip?

## TheColetrain | 2022-06-10T17:06:40+00:00
I have had the GUI wallet for some time.  I don't recall exactly how I installed it...perhaps a year ago..  I obviously updated it, by following the prompts, recently.   I probably would have just picked the installer on getmonero.org back in the day.  

I wanted to answer you as best i could, but now you have me wondering why this is pertinent.  perhaps it has something to do with the admin privilege's used upon installation, were different then compared to what was needed now, for the p2pool?



## selsta | 2022-06-10T17:08:47+00:00
I'm asking because https://github.com/monero-project/monero-gui/pull/3933 did some changes to the installer so that admin privileges shouldn't be required anymore.

## TheColetrain | 2022-06-10T17:20:19+00:00
Makes sense!  I auto updated when prompted to get where I am now. 
and now that you have responded, with that, maybe it should have been installed directly to the C drive.  I'm not sure if my install location was default once-upon-a-time, or not... or maybe I just goofed.

```
GUI version: 0.17.3.2-unknown (Qt 5.15.3)
Embedded Monero version: 0.17.3.2-unknown
Wallet path: C:\Users\XXX\Desktop\Monero\wallet\X wallet.keys
Wallet restore height: 2337045
Wallet log path: C:\Users\XXX\AppData\Roaming\monero-wallet-gui\monero-wallet-gui.log
Wallet mode: Advanced mode (Local node)
Graphics mode: OpenGL
```

## TheColetrain | 2022-06-10T17:25:58+00:00
Anyway.  I feel like one line of text somewhere would make this an easy fix.  either in wallet or on the error screen

## selsta | 2022-06-10T18:02:04+00:00
#3946

## TheColetrain | 2022-06-10T18:06:47+00:00
Awesome. I'm all fixed up, but this will help many future people.  Have a great day.  Seems so silly now, but at the time, you don't know what to think.

## diginomad23 | 2023-07-14T18:20:12+00:00
> you need to run the GUI wallet as Admin when installing P2Pool and starting to mine. Requesting that added to the error message, or in the wallet as text. It seems so simple now, but for a while until I did a lot of digging, It didn't work. I was new to it.. and so I was not sure what to expect.

how do I run as admin on Mac?

## selsta | 2023-07-15T19:40:12+00:00
@diginomad23 you don't have to run as admin on Mac, what issue are you having?

# Action History
- Created by: TheColetrain | 2022-06-09T19:56:49+00:00
- Closed at: 2022-06-10T18:06:47+00:00
