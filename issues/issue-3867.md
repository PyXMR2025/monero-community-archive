---
title: No way to exit out of Confirm Send Modal
source_url: https://github.com/monero-project/monero-gui/issues/3867
author: elibroftw
assignees: []
labels: []
created_at: '2022-03-18T04:24:39+00:00'
updated_at: '2023-11-24T14:16:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I was trying to send Monero today and it seems that if the wallet has been locked for quite some time, the gui is unable to calculate the fee, so when I click send while the fee is calculating, I get stuck on the creating transaction modal.

This is two bugs. One is infinite fee calculation and the second is no way to cancel the confirm send modal while the fee is calculating. Solving the former solves the latter but if the former takes too long to fix, the latter should be fixed first.

These two issues combined with the fact it's hard to close the wallet make for a very horrible UX. I'm unable to start working on a my own Monero wallet atm but these are serious issues that need to be addressed! 

# Discussion History
## selsta | 2022-03-18T07:35:14+00:00
Which node are you using? The fee shouldn't take long to calculate in the first place.

## elibroftw | 2022-03-18T13:40:37+00:00
I was using a trusted remote node. The issue has nothing to do with a node since after I restarted the wallet the fee took only a couple seconds. The issue definitely has to do with running the gui for long period of time. 

## selsta | 2022-03-18T13:41:42+00:00
Can you reproduce this issue consistently?

## elibroftw | 2022-03-18T13:45:43+00:00
It would take hours to reproduce the error. The gui was running for over 12 hours when I tried to send a transaction. 

## elibroftw | 2023-04-29T19:37:26+00:00
By the way, this issue still exists. Keep the GUI open for a couple hours and then click send.
![image](https://user-images.githubusercontent.com/21298211/235321123-d60545d4-f67d-45d4-9fa0-90960b5fbf31.png)


## elibroftw | 2023-04-29T19:37:51+00:00
Okay so it took a whole minute 

## elibroftw | 2023-11-23T17:49:38+00:00
Wanted to send someone their money yesterday and it took 3 minutes for the transaction to be created into the gui. Mymonero is faster at this so I don't know what's going on.

## selsta | 2023-11-24T14:09:44+00:00
MyMonero set to the same daemon as the GUI?

## elibroftw | 2023-11-24T14:11:08+00:00
No it is their own daemon. the GUI is connected to mine. I'll try using a different remote node but wondering what hardware could limit the daemon?

## selsta | 2023-11-24T14:16:20+00:00
I don't know but to isolate the issue it would be good to set both to the same daemon. Really slow storage can slow down transaction generation but multiple minutes is too long even for a slow daemon.

# Action History
- Created by: elibroftw | 2022-03-18T04:24:39+00:00
