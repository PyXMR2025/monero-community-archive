---
title: 'Monero RPC: Moving Counter Buffer?'
source_url: https://github.com/monero-project/monero/issues/5095
author: MikeScanlan5
assignees: []
labels: []
created_at: '2019-01-25T16:38:55+00:00'
updated_at: '2019-01-26T00:18:39+00:00'
type: issue
status: closed
closed_at: '2019-01-25T21:47:17+00:00'
---

# Original Description
I have a Bitcoin ATM business that also allows buys and sells of Monero. 

I'm running my own Monero full node daemon and the RPC on a Windows 2012 Server which is the sole purpose of that machine -- just a Monero node. The RPC is open only to the IP of my ATM client/server software from General Bytes to buy/sell via an ATM. 

I've run into a problem recently where each time the RPC is called, the Monero RPC plays "catch up" by way of a "Moving counter buffer by 1 second" trace line in the log. Hundreds and even thousands of them.  Depending on the amount of time the RPC was last called, this can last anywhere from a half second all the way to a full minute if the RPC hasn't been called for a day or two.  This is causing a time out on my machines (read: failed transactions) because the RPC is scrolling through this "moving counter buffer" stuff and taking too long to answer the actual RPC request. When it does get to that point, the answer is good and the RPC works successfully. If I keep calling the RPC from the ATM every few seconds, no issues because it only needs to run through a dozen or two of these moving counter buffer lines. But if any more than a half hour goes by without the RPC being called, it can't catch up fast enough to answer the ATM machine's RPC call. 

I've tried using Google to debug the error message but coming up empty handed. Can anyone help? I have no idea what this message means. I've re-imaged my server. I've re-downloaded the Monero daemon and software, and even deleted the entire blockchain and re-synced all ~50 GB.  No dice. It keeps happening. 

Here's the screen shot of what continues to scroll by each time the RPC is called.  I'm also attaching the full RPC log (IP addresses and wallet balances changed for privacy) showing a test call at 2019-01-25 16:27:58 to help.  Any ideas would be really appreciated. 

[Monero-RPC-Log.txt](https://github.com/monero-project/monero/files/2796960/Monero-RPC-Log.txt)

![wqt0j9eb5lc21](https://user-images.githubusercontent.com/44779151/51758523-e7a2d380-2093-11e9-8894-336674cab5c5.jpg)



# Discussion History
## moneromooo-monero | 2019-01-25T18:29:50+00:00
I believe this is the code that calculates wait times to meet download/upload rates (which doesn't even apply to RPC anyway). I'll see what can be done to speed it up. If it's taking a minute, there's clearly some silly complexity here.

## moneromooo-monero | 2019-01-25T19:06:04+00:00
Trying here, I get a delay of less than one second if I simulate an idle time of 100 hours (and that's in debug mode with ASAN on). To make sure, that pause you're reporting also happens when you are not specifically asking for all trace logs, right ?

## moneromooo-monero | 2019-01-25T21:19:36+00:00
https://github.com/monero-project/monero/pull/5096 removes a lot of copying, though I think your problem is just that lots of logs take logs of time.

## MikeScanlan5 | 2019-01-25T21:47:13+00:00
You know what, I am a complete idiot.  

I turned log-level up to 4 for another reason a couple days ago to troubleshoot something then mistakenly either a) thought I turned it back, or b) realized I didn't but thought those messages were out of the ordinary.  

Yes, it's the logging that is causing the actual problem it appears. log-level back to 1 and all appears good. I'll let it run overnight and make another test RPC call in the morning, and if the theory is correct it'll respond right away like it had been before.  

This is what happens when you stare at screens and code and logs for months on end. :)  Thanks!

## MikeScanlan5 | 2019-01-26T00:18:39+00:00
PS. @moneromooo-monero  thanks for the comments. 

# Action History
- Created by: MikeScanlan5 | 2019-01-25T16:38:55+00:00
- Closed at: 2019-01-25T21:47:17+00:00
