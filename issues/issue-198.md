---
title: reported problem upgrading non-deterministic wallet
source_url: https://github.com/monero-project/monero/issues/198
author: iamsmooth
assignees: []
labels: []
created_at: '2014-12-07T22:28:50+00:00'
updated_at: '2014-12-08T05:09:14+00:00'
type: issue
status: closed
closed_at: '2014-12-08T05:09:14+00:00'
---

# Original Description
https://bitcointalk.org/index.php?topic=583449.msg9770689#msg9770689

Minor bug in simplewallet v0.8.8.5-unknown:

After updated to 0.8.8.5, when I initially opened an old non-deterministic wallet, simplewallet detected that it was a deprecated version of the wallet and then produced a 25-word seed. I assumed that being given a new seed implied that my non-deterministic wallet had been upgraded to a deterministic wallet. But when I entered the "seed" command, I received the message: "Error: The wallet is non-deterministic. Cannot display seed." So my wallet remains in its original non-deterministic format. 

Also when I ran simplewallet with the --restore-deterministic-wallet flag, and entered those 25 words at the "Specify electrum seed:" prompt, I received the message "Error: electrum-style wordlist failed verification." I exited and re-opened my non-deterministic wallet, this time without any flag, using my password. The funds are still there and I was not presented with the erroneous 25 word seed this time.

Summary: The new version of simplewallet erroneously presented me with a 25 seed the first time I used it to open a non-deterministic wallet.


# Discussion History
## warptangent | 2014-12-08T02:38:51+00:00
The display of a seed for ND wallets during the wallet JSON upgrade is a known issue and fixed in PR #196.


## warptangent | 2014-12-08T04:59:14+00:00
The second issue, the error while restoring a deterministic wallet from the 25 words, is probably unrelated. The current restore behavior doesn't accept the words that contain newlines. So copying and pasting the displayed 25 words to restore a wallet won't work. The newlines need to be removed so that the restore function interprets them correctly.

I patched this last month during testing and will include it in a future PR.

Note that in the case described above, if a wallet were to restore successfully from the 25 words the user was given, it would be a new wallet and NOT the original non-deterministic wallet.


## fluffypony | 2014-12-08T05:04:39+00:00
The line breaks are there because we had the seed being cut off in some environments. I don't know if supporting cut and paste is a good idea or counter-productive from a security perspective?


## warptangent | 2014-12-08T05:07:47+00:00
In the patch, line breaks included are fine. It includes them in splitting the recovery text into individual words.


## fluffypony | 2014-12-08T05:09:14+00:00
Ah got it. ok then I'm closing this as resolved in #196 and a future PR


# Action History
- Created by: iamsmooth | 2014-12-07T22:28:50+00:00
- Closed at: 2014-12-08T05:09:14+00:00
