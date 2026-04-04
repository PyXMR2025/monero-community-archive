---
title: Unable to Access my Ledger Nano S Monero Wallet After the Most Recent Update
source_url: https://github.com/monero-project/monero/issues/4706
author: deathd0tcom
assignees: []
labels: []
created_at: '2018-10-23T14:47:20+00:00'
updated_at: '2018-11-04T01:17:00+00:00'
type: issue
status: closed
closed_at: '2018-10-25T16:14:06+00:00'
---

# Original Description
So I downloaded the newest release for Windows, and I copied over my wallet to the new folder I extracted the .zip folder to. I opened cmd in that folder by typing 'cmd' & hitting enter in file explorer. I'm using a Ledger Nano S (if that changes anything). After I successfully enter my wallet name & password, I get the following error:

Error: failed to load wallet: Wrong sequence_idx

When I first got this error, I did some precursory Google searching and couldn't find any helpful information for what was causing this specific error or how to fix it. I did find I could use the now-updated daemon with the monero-wallet-cli from the Lithium Luna release. In the end, I used the Lithium Luna monero-wallet-cli to load my wallet by using the following flag:

--allow-mismatched-daemon-version

That worked fine, but I'm hoping to get this figured out. Any help is greatly appreciated, so please feel free to ask for more information if you have any theories/experience with this issue! Thanks in advance!!

![snip_xmr-error-bb](https://user-images.githubusercontent.com/41760082/47369130-0074a500-d6b1-11e8-9cb7-6b2b753831a1.PNG)


# Discussion History
## deathd0tcom | 2018-10-23T14:55:49+00:00
I'd like to add that this Issue (https://github.com/monero-project/monero/issues/4534), which was previously marked as Resolved & is now marked as Closed, was never resolved in a way that allows all users to access Ledger Nano S. 

That thread has a comment suggesting a fix will be forthcoming in the v0.13.0.4 release, but how are we supposed to gain access to our Ledger Nano S wallets in the meantime? The Ledger Nano S is currently the only hardware solution for Monero. Every Monero user that stored their XMR on a hardware wallet are now unable to access their funds, aside from the few lucky ones who managed to get into the wallet on a subsequent attempt. Some of us, myself included, have been entirely unable to access our XMR ever since the update was released, and would really appreciate if someone could explain what we can do to correct these problems. Thanks so much in advance!!!!

## selsta | 2018-10-23T14:59:42+00:00
Use the pre-release binaries from here:

https://www.reddit.com/r/Monero/comments/9qo76v/gui_v01304_prerelease_test_binaries_buildbot/

Or you can convert your Ledger seed to a Monero seed:

https://github.com/LedgerHQ/ledger-app-monero/tree/master/tools/python

As written in the issue, this is a dev issue tracker and if something is fixed in the code, it is closed here.

## deathd0tcom | 2018-10-23T15:17:04+00:00
After dowloading the v0.13.0.4 binaries I'm still unable to access the Ledger Nano S monero wallet. 

![snip_xmr-v0 13 0 4-gui-error](https://user-images.githubusercontent.com/41760082/47370921-bdb4cc00-d6b4-11e8-95ea-c325865dce7e.PNG)

Now the only option would be to use my Ledger's seed to create a Monero/Electrum seed & then use that seed with the GUI to "Restore wallet from keys or mnemonic seed," correct?

## xiphon | 2018-10-23T16:10:44+00:00
Please use [Win master nightly build](https://build.getmonero.org/downloads/monero-2287fb9f-win64.tar.gz) and provide `monero-wallet-cli` logs with `--log-level 4`

## dEBRUYNE-1 | 2018-10-23T16:14:16+00:00
@xiphon & @deathd0tcom - Please see my comment here:

https://www.reddit.com/r/Monero/comments/9qo76v/gui_v01304_prerelease_test_binaries_buildbot/e8axwx2/

In addition, @deathd0tcom, could you try this binary? 

https://build.getmonero.org/builders/monero-static-win64/builds/5765

## blockchainbuzz | 2018-10-23T21:57:33+00:00
I have tried binary builds 5765. Open wallet  ( `LedgerMonero.keys` and no `LedgerMonero` wallet file ) with `monero-wallet-cli`, Enter wallet password. Then the cli seems requesting view key access from the NanoS, trying to access view key from the device Yes or No. Press right button (Yes). Then cli generating the  `LedgerMonero` wallet file. Up till know, It seems working. 
![capture3](https://user-images.githubusercontent.com/36054391/47391563-66494700-d71a-11e8-839c-1f9240b3eba2.jpg)

However after closing the wallet. And then try to open `LedgerMonero` wallet file w/ `monero-wallet-cli`. the cli crashed. I don't know if below picture is the cli log of the crashed. 

![image](https://user-images.githubusercontent.com/36054391/47393113-e5407e80-d71e-11e8-8ff4-85f0f6ec5ac8.png)

I try to open `LedgerMonero.keys`  w/ GUI instead of `Error: failed to load wallet: Wrong sequence_idx`. Receive new error message bellow.
![capture4-1](https://user-images.githubusercontent.com/36054391/47392931-41ef6980-d71e-11e8-91ad-0230c80bb792.jpg)





## dEBRUYNE-1 | 2018-10-24T07:19:18+00:00
The GUI you used probably does not include the fix yet. 

>However after closing the wallet. And then try to open LedgerMonero wallet file w/ monero-wallet-cli. the cli crashed. I don't know if below picture is the cli log of the crashed.

Could you elaborate? Why did you try to open the wallet cache in particular? Or did you simply try to reopen the wallet? 

## blockchainbuzz | 2018-10-24T15:37:53+00:00
> The GUI you used probably does not include the fix yet.
> 
> > However after closing the wallet. And then try to open LedgerMonero wallet file w/ monero-wallet-cli. the cli crashed. I don't know if below picture is the cli log of the crashed.
> 
> Could you elaborate? Why did you try to open the wallet cache in particular? Or did you simply try to reopen the wallet?

I simply  try to reopen the wallet. 

## dEBRUYNE-1 | 2018-10-24T20:45:42+00:00
Ok, interesting. @blockchainbuzz, could you perhaps try the GUI build that is listed here?

https://www.reddit.com/r/Monero/comments/9qywzf/gui_v01304_prerelease_test_binaries_buildbot/

## mferrari43 | 2018-10-25T00:02:54+00:00
> I had the same error. "Error: failed to load wallet: Wrong sequence_idx"
> My solution was to go to "USB Configuration" then "Bluetooth and other devices" In "Other devices" "Ledger S" Remove device.
> Then it worked.
> 
> Sorry for my English,
> I do not know if the problem had already been solved.
> Greetings.

from other thread, just wanted to say this worked for me

## blockchainbuzz | 2018-10-25T14:33:42+00:00
I can confirm that there are two things that crash the `monero-wallet-cli ` on my machine.
1. Missing `microsoft usdid smartcard reader (wudf) `drivers.
2. `Monero ` app is NOT open on Ledger Nano S upon opening the wallet. 
Or view key from the device Yes or No acknowledgment not arrive in-time (time expires) .  
I think this can be prevented by running some check with `Monero ` app on Ledger Nano S. 

When above items are done correctly, `menero-v0.13.0.4 ` solves the error. 

> Error: failed to load wallet: Wrong sequence_idx


## deathd0tcom | 2018-10-25T16:14:06+00:00
> Ok, interesting. @blockchainbuzz, could you perhaps try the GUI build that is listed here?
> 
> https://www.reddit.com/r/Monero/comments/9qywzf/gui_v01304_prerelease_test_binaries_buildbot/

@dEBRUYNE-1 After downloading this release ^^ I was able to access the Ledger wallet. Anyone unable to access their Ledger still should use this link to download the updated release! Thanks again!

# Action History
- Created by: deathd0tcom | 2018-10-23T14:47:20+00:00
- Closed at: 2018-10-25T16:14:06+00:00
