---
title: Stuck on "Opening wallet..." when using hardware wallet with Trezor Safe 3
  in Ubuntu 24
source_url: https://github.com/monero-project/monero-gui/issues/4430
author: mrbeast87
assignees: []
labels: []
created_at: '2025-04-03T17:16:04+00:00'
updated_at: '2025-04-27T20:15:43+00:00'
type: issue
status: closed
closed_at: '2025-04-27T20:15:41+00:00'
---

# Original Description
I found issues similar to this one I'm opening, but since mine involves a live Ubuntu 24 image, it might be easier to reproduce.  

I booted from a live Ubuntu 24 installation and downloaded the latest Monero GUI (Linux 64-bit) from the official source. Running the AppImage without sudo didn't detect my hardware wallet, so I ran it as sudo.  

I then selected Simple Mode → Create Hardware Wallet → Trezor Safe 3 (empty passphrase) → Confirmed export of watch-only keys → Empty password for the wallet → Create Wallet.

Then, it got stuck on this screen and although I left it for ~30 minutes nothing happens:

![Image](https://github.com/user-attachments/assets/97509624-62e9-4c8f-88c7-bd73f7e7f1e8)

(You can see some of the logs by zooming in on the terminal).

Can anyone help me fix this?

# Discussion History
## selsta | 2025-04-03T18:17:45+00:00
Can you try installing Trezor bridge?

## mrbeast87 | 2025-04-03T21:33:57+00:00
@selsta isn't Trezor bridge deprecated?

The only official resource I found about this is this page which says it's deprecated and you should uninstall it: https://trezor.io/learn/a/deprecation-and-removal-of-standalone-trezor-bridge

Can you provide the link for downloading?

## selsta | 2025-04-04T16:54:28+00:00
Can you try to install Trezor Suite? It might come with the bridge.

## mrbeast87 | 2025-04-05T16:12:41+00:00
Trezor Suite only ships as an `AppImage` file, so I guess it does not install anything?

In any case, I ran it on my Ubuntu live image. It didn't work, the app only showed a black screen. I opened an issue on Trezor official forum to try to solve this.

But I'm not sure that this will solve anything regarding the connection between Monero GUI and my Trezor Safe 3.

## mrbeast87 | 2025-04-27T20:15:41+00:00
Ok, closing this ticket because I finally got Trezor Suite running on Ubuntu 24.

Here’s what I did:
- Installed the OS instead of using the live boot.
- Ran Trezor Suite (had to install some udev rules so that my device could be detected properly).
- Spun up Monero GUI — everything worked perfectly now.

Thanks for the help @selsta!

# Action History
- Created by: mrbeast87 | 2025-04-03T17:16:04+00:00
- Closed at: 2025-04-27T20:15:41+00:00
