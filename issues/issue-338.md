---
title: Overwrites previous wallet files without warning (macOs)
source_url: https://github.com/monero-project/monero-gui/issues/338
author: dternyak
assignees: []
labels: []
created_at: '2016-12-22T18:48:36+00:00'
updated_at: '2016-12-22T20:55:00+00:00'
type: issue
status: closed
closed_at: '2016-12-22T20:55:00+00:00'
---

# Original Description
After creating a wallet, closing monero-wallet-gui, and re-opening it, creating a new account with the default values overwrites the previous wallet without warning. 

# Discussion History
## dternyak | 2016-12-22T18:53:01+00:00
The gui was also unable to recognize that I had previously created a wallet - I am noticing that re-opening it now does not prompt me to "recover" or choose a wallet file to open as it had previously.

I am worried that the wallet file I had generated was somehow deleted when closing the GUI, as it had hung for an unusual amount of time upon close.

## dternyak | 2016-12-22T19:09:13+00:00
One additional "edge" to this case would be that my mac underwent a hard shutdown by running out of battery, and this behavior was noticed after I restarted it. Perhaps the wallet was being held onto and then corrupted when the GUI was forced to close. 

## moneromooo-monero | 2016-12-22T20:07:09+00:00
Anything special about that previous wallet ? Like non ASCII chars, on a non local mounted partition, etc ? If I try to create a wallet which already exists, the GUI tells me I can't do that.

## dternyak | 2016-12-22T20:10:30+00:00
@moneromooo-monero Nothing special. The more I think about it, the more I believe the wallet was somehow already deleted when I opened monero-wallet-gui again. 

This was the order of usage:

1. start monero-wallet-gui
2. create new wallet with default settings.
3. sync.
4. close <--- I believe the wallet was somehow deleted here (the GUI appeared to freeze and perhaps even crash upon close). 
5. machine shuts off (battery dead)
6. machine back up
7. start monero-wallet-gui
8. prompted to create new wallet again (which I now realize the wallet was somehow already deleted / the gui believed it did not have a wallet).
9. created new wallet with same defaults.
10. wallet is overwritten. 



## Jaqueeee | 2016-12-22T20:12:00+00:00
this is related to #337 right? The wallets gets created in "wrong" folder even this time?

## dternyak | 2016-12-22T20:16:08+00:00
Yes @Jaqueeee - it gets created in the "wrong" folder and overwrites the previous wallet that was also in the "wrong" folder.

I'm on macOS 10.11 and not 10.12 like a lot of people, but I don't think thats the reason. 

## moneromooo-monero | 2016-12-22T20:19:30+00:00
I think the GUI saves the wallet regularly (Jaquee, is that right ? I think there were some changes there a month ago or so). A system crash might well cause a file currently being written to be lost, depending on the filesystem.

## Jaqueeee | 2016-12-22T20:24:31+00:00
@moneromooo-monero IIRC the .keys file is saved on creation and the cache after first refresh + on exit.

I'm also on 10.11. That log would be valuble @dternyak (https://github.com/monero-project/monero-core/issues/337#issuecomment-268880566). I'm really curious about what happens on creation. 

## dternyak | 2016-12-22T20:26:41+00:00
@Jaqueeee Reposting here: 

> I  deleted all wallet files and tried to simulate the same conditions as the original entry - Now it creates at the correct location - /Users/first-last/Monero/wallets/wallet-name.



## Jaqueeee | 2016-12-22T20:50:30+00:00
Thanks. Maybe wallet wasn't even created after all. Because of the hardware crash. I suggest we close this if it isn't reproducible?

## dternyak | 2016-12-22T20:55:00+00:00
It was created because I was able to get an address and send 1 xmr as a test to it. But since we can't reproduce, I'll close anyway.

# Action History
- Created by: dternyak | 2016-12-22T18:48:36+00:00
- Closed at: 2016-12-22T20:55:00+00:00
