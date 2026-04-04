---
title: Cannot Ctrl-C close the wallet when it's "Locked due to inactivity."
source_url: https://github.com/monero-project/monero/issues/6192
author: binaryFate
assignees: []
labels: []
created_at: '2019-11-27T17:50:45+00:00'
updated_at: '2023-10-10T18:55:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As the title says, it does not react to signal without first entering the password.
Is that on purpose? If so what is the reasoning?

I find it mildly frustrating when I have several tabs open with several wallets, don't remember which one it is and hence the password, and just want to close it and be done with it. So I'm curious if there is a good reason to be blocking not just wallet but also access back to the shell?

# Discussion History
## moneromooo-monero | 2019-11-27T18:23:10+00:00
I don't think so. The keyboard is in raw mode for password entry I think, so the ^C does not get concerted to a signal. Though IIRC ^Z and kill -9 works :)
Detecting ^C should be possible to stop password entry, though if anyone added a ^C to their password that'd be SOL.

## binaryFate | 2019-11-27T18:38:21+00:00
Other password prompts do not seem to have same behavior, I tried the prompt when opening wallet and it gently closes when ctrl-ced.

> though if anyone added a ^C to their password that'd be SOL

Terrific idea for added security!

## vtnerd | 2019-11-27T23:48:03+00:00
[Ctrl-c is disabled during password prompt](https://github.com/monero-project/monero/blob/master/src/simplewallet/simplewallet.cpp#L10213). The actual issue was a thread joining itself and other weird shutdown issues. There was something funky about readline too. You can  scroll through the commits / PRs for the discussion about it.

## selsta | 2022-07-20T19:58:37+00:00
#7722 should solve this but moneromooo didn't like it.

## max-ishere | 2023-10-10T18:34:14+00:00
I find this "to exit put in your password first" to be frustrating. I mean it's fine, I can go open my kdbx, find the password, copy it, go to the terminal, paste in (probably the wrong password) type exit. But man I wish there was just a <kbd>Ctrl</kbd><kbd>C</kbd> or <kbd>Ctrl</kbd><kbd>D</kbd> and it would just exit.

I think a reasonable thing to do is when you lock it, save the wallet, then lock, so if some (reasonably lazy person) just closes the terminal tab they don't cause (whatever the `exit` command prevents from).

Also after say 3 or 5 or 10 or some config value attempts it can just exit the wallet and if you wanna open it again then you just type the wallet command.

## max-ishere | 2023-10-10T18:37:31+00:00
Another improvement that I think is worth implementing is showing the filename of the wallet currently locked. I'd appreciate the feature.

## max-ishere | 2023-10-10T18:40:13+00:00
And also something I noticed is that there seem to be several different implementations of wallet password input. There's the one you see when you open the wallet, there's an autolock one same as the one from `lock` command. idk how it came to be this way, but from a development standpoint it makes sense to have 1 implentation of it.

**When opening the wallet**

![wallet-unlock](https://github.com/monero-project/monero/assets/47008271/893493c9-5277-4caf-9b80-854bf6bb256e)

**When unlocking after `lock` command**

![wallet-lock-cmd](https://github.com/monero-project/monero/assets/47008271/9be33b45-cbfa-43a6-9919-16474e7992b5)

**Autolock prompt**

![screenshot](https://github.com/monero-project/monero/assets/47008271/ba602d68-a79e-45ea-adce-5f89f807567e)



# Action History
- Created by: binaryFate | 2019-11-27T17:50:45+00:00
