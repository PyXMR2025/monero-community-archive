---
title: Monero GUI suddenly restarts syncing blockchain from block 0
source_url: https://github.com/monero-project/monero-gui/issues/3929
author: stefan-reich
assignees: []
labels: []
created_at: '2022-05-24T12:49:07+00:00'
updated_at: '2024-10-25T07:54:00+00:00'
type: issue
status: closed
closed_at: '2022-05-26T15:43:42+00:00'
---

# Original Description
Hi, I have Monero GUI wallet running with a pruned blockchain. After 2 days it was finally done downloading the (pruned) blockchain and ready to use. I did successfully send a transaction too IIRC.

However, another few days later, the wallet suddenly started syncing the blockchain from the very first block again.

I literally didn't do anything to it, it just exhibited this behavior spontaneously.

Obviously, I can't use the wallet in this state, waiting 2 days for it to sync again...

Any idea what may be going on?

Wallet GUI version is 0.17.3.2 on Ubuntu 20 in a LUKS partition.

# Discussion History
## selsta | 2022-05-24T18:53:11+00:00
Can you go to Settings -> Info and post the output of "status" ?

Did you have a custom blockchain location in Settings -> Node?

## stefan-reich | 2022-05-24T19:31:33+00:00
Hi,

the field "blockchain location" is empty. 

Hm, I don't see "status" in Settings / Info... I see "GUI version", "Embedded Monero version" and some more items...

Is the node log something you could work with?

## selsta | 2022-05-24T19:32:52+00:00
Sorry, I meant Settings -> Log and post the output of "status".

Also did you previously set a custom blockchain location?


## stefan-reich | 2022-05-24T19:46:53+00:00
No, I never changed the blockchain location.

Here is a [screenshot.](https://botcompany.de/images/1103134)

## selsta | 2022-05-25T21:07:16+00:00
The blockchain gets saved into ~/.bitmonero/lmdb/data.mdb

Any idea if that file got somehow deleted? monero and monero-gui don't have any function to delete it.

## stefan-reich | 2022-05-26T11:37:35+00:00
The file is there but small (1 GB). Incidentally, I just noticed the .bitmonero folder was on the wrong drive (not in the LUKS partition), which is also almost full. So I just moved it there and will let it re-sync. Maybe this was actually the problem (lack of space on the drive). Thank you

## stefan-reich | 2022-05-26T15:43:42+00:00
OK I figured it out. There was a copy of the blockchain inside the GUI wallet folder (is it supposed to be there?), and additionally that incomplete one in ~/.bitmonero.

Maybe the problem was triggered by me upgrading from 0.17.3.1 to 0.17.3.2? Does it matter which folder I run the GUI wallet from?

Anyway I moved the complete blockchain to ~/.bitmonero and now it's all there again. monerod is happily syncing the last 14k blocks.

## adrelanos | 2024-10-25T07:53:58+00:00
In my case, I was using:

    flatpak override org.getmonero.Monero --filesystem=host

Because I wanted to use `--wallet-file` to point to a wallet file on the host operating system (not inside flatpak). That resulted in "resync from block 0". To fix, I used:

    mv ./.var/app/org.getmonero.Monero/.bitmonero .bitmonero

Not something Monero can fix.

I just didn't expect `flatpak override ... --filesystem=host` to change all folders to the host filesystem. Instead assumed it only allows host file system access without changing all folders.

# Action History
- Created by: stefan-reich | 2022-05-24T12:49:07+00:00
- Closed at: 2022-05-26T15:43:42+00:00
