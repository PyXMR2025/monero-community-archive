---
title: Update keyring for Windows Building Instructions
source_url: https://github.com/monero-project/monero-gui/issues/4070
author: elibroftw
assignees: []
labels: []
created_at: '2022-11-17T23:58:16+00:00'
updated_at: '2022-11-18T00:53:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Following the build instructions if you already have an existing Msys install can result in `error: failed to commit transaction (invalid or corrupted package)`

I suggest informing the user to update the keyring (supply the command) before supplying the install commands. This way, Windows users like me who aren't familiar with Msys or pacman don't have troubles. Maybe we need to run `pacman -Syu` first?

It would also speed up setup if a --noconfirm was used or something.

# Discussion History
## selsta | 2022-11-18T00:11:45+00:00
Not sure if we need to explain to the user how to use their package manager. We don't do it for other OS too.

## elibroftw | 2022-11-18T00:53:50+00:00
These are build instructions and so is most useful to developers on windows. It is not a how to install monero guide. (next you'll say it's not our job to instruct users how to verify binaries 😂). 

Msys and pacman aren't windows native. It's not the user's package manager, it's archs'.
A windows user should not be expected to know or learn how to use another OS' package manager. The instructions should be stupid proof and be as resilient as possible. I hope you can see where I'm coming from. Time spent troubleshooting should be as low as possible. 

Troubleshooting code setup is such a turn off to contribute or even use software. It requires such a high resolve that I don't have everyday on hand.

I want to get back into monero-gui development without installing Linux on my primary devices. The laptop I have Linux installed on took a long time to compile the GUI and can't run anything more than vscode at a time 😂. There's no developer guide either. Just this build guide. 

# Action History
- Created by: elibroftw | 2022-11-17T23:58:16+00:00
