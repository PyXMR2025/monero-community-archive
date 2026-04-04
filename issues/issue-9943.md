---
title: Monero Wallet Cli password command changes password incorrectly
source_url: https://github.com/monero-project/monero/issues/9943
author: rudolfschmidt
assignees: []
labels: []
created_at: '2025-06-05T12:15:08+00:00'
updated_at: '2025-06-14T18:56:54+00:00'
type: issue
status: closed
closed_at: '2025-06-14T18:56:54+00:00'
---

# Original Description
Using monero version 0.18.4.0-2 I changed my wallet password from one password to another, noticing that the password was set incorrectly. I created a new test wallet file and noticed the same. If you change the password to another password, sometimes it works and sometimes it doesn't. The mistakes occur more often if you enter the same password as the previous one. Next time you try to log in you it tells you incorrect password. Not sure how to debug it.


# Discussion History
## nahuhh | 2025-06-05T12:27:28+00:00
What is 18.4.0-2? And how did you obtain this revision?

## rudolfschmidt | 2025-06-05T12:46:12+00:00
arch package

Monero 'Fluorine Fermi' (v0.18.4.0-release) is the name then


## nahuhh | 2025-06-05T15:21:03+00:00
Do you have the same issue with the release binaries from getmonero.org (or github)?

## rudolfschmidt | 2025-06-05T19:50:36+00:00
tested now with the recent version from the website
Monero 'Fluorine Fermi' (v0.18.4.0-release)
and found the same problem.

For me, it looks like the implementation of changing the password is broken. If you put a password and even its confirmed twice (otherwise it would be rejected), the chance that you have the same typo twice is very slim. I encourage you to test it and report here. I use Arch Linux.

## nahuhh | 2025-06-05T20:32:56+00:00
1. setup wallet:
wallet name: 9943
password: 123
seed lang: english

2. Change password: 321
3. Stop wallet
4. Reopen wallet
5. success

Arch linux

## rudolfschmidt | 2025-06-05T20:45:39+00:00
Can you test it a little bit more? What do you want me to do? Record a video for you?
Yes, if you change the password in the same session, it seems to work. But try to create a wallet, then log out, log in, change the password, log out, and try to log in again with the new password, it does not work. I have not developed the code, so I dont know why.

## nahuhh | 2025-06-05T21:07:47+00:00
1. Changed oaaaword 123 -> 321, logout in = success
2. Changed password 321 -> 321 = success
3. Changes password 321 -> 456 = success
4. "But try to create a wallet, then log out, log in, change the password, log out, and try to log in again with the new password" = it worked

(closed wallet in between attempts)

i don't know what to tell you. I cant reproduce.
sure, send a screen recording, or steps to reproduce 

## rudolfschmidt | 2025-06-06T02:32:49+00:00
![Image](https://github.com/user-attachments/assets/9c83592c-ae38-4ff3-a8e3-7a0000e7af6a)

## rudolfschmidt | 2025-06-06T14:48:48+00:00
any idea?

## nahuhh | 2025-06-06T20:42:13+00:00
i can reproduce.

1. Create wallet
2. Close wallet
3. **open wallet using .keys extension** like `./monero-wallet-cli --wallet-file 9943.keys`
4. Change password & close wallet
5. Password doesnt work


this only seems to happen when specifying the .keys extension

## rudolfschmidt | 2025-06-06T21:45:01+00:00
Finally, you can reproduce it.

Yes, if you skip the extension, he saves the password correctly.

Is there a way to restore the wallet with the incorrect password setting?

## rudolfschmidt | 2025-06-07T04:30:38+00:00
I have found the bug and will prepare a PR

## plowsof | 2025-06-07T10:26:35+00:00
out of curiosity - i reproduced in v18.3.2 - and no .keys.keys file is created 

# Action History
- Created by: rudolfschmidt | 2025-06-05T12:15:08+00:00
- Closed at: 2025-06-14T18:56:54+00:00
