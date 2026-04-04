---
title: Monero GUI FLATPAK can NOT transfer the Seedphrase to TREZOR Safe 3
source_url: https://github.com/monero-project/monero-gui/issues/4318
author: OnAirDroid
assignees: []
labels: []
created_at: '2024-05-23T19:03:58+00:00'
updated_at: '2024-05-25T23:25:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The Trezor Support suggested to try the Flatpak version and even so the device is found, another heavy glitch comes up!

Steps for a Hidden Wallet ...
1. Create a new wallet from hardware
2. Name it and Trezor Safe 3 is chosen
3. Password for Monero GUI
4. Seedphrase to Hardware
5. Passphrase for Hidden Wallet
6. Create Wallet
7. Than a confirmation screen for the password comes up and here it ends!
**Even with the correct password, the ok bottom brings this screen up again and again (endless times)!**

Than I deleted the Monero folder for a fresh try as a Standard Wallet ...
1. Create a new wallet from hardware
2. Name it and Trezor Safe 3 is chosen
3. Password for Monero GUI
4. Seedphrase to Hardware
5. Create Wallet > **FAILED TO STORE THE WALLET** !!

I've tried and repeated this procedure to create a hardware wallet a dozen of times! No success, neither as Standard Wallet nor as Hidden Wallet!

No Log-File was created by Monero GUI, but something goes wrong with the communication between the Trazor Safe 3 and the Monero GUI Wallet!
When I got stuck at the password screen, this step messes up the 'trezord-git' bridge, meaning I had to exit the bridge and restart it before another try, otherwise I would get the 'device not found' message.

Manjaro Linux (KDE 6, latest update)
Kernel 5.15

# Discussion History
## selsta | 2024-05-23T19:23:53+00:00
First step, did you make sure no other program is open that communicates with the Trezor? Like for example Trezor Suite or a different wallet.

> Seedphrase to Hardware

Can you please explain what you mean with this step?

> I've tried and repeated this procedure to create a hardware wallet a dozen of times! No success, neither as Standard Wallet nor as Hidden Wallet!

Did you try to create a regular wallet first, not a hardware wallet? Just to make sure that that works.

## OnAirDroid | 2024-05-23T19:32:48+00:00
> First step, did you make sure no other program is open that communicates with the Trezor? Like for example Trezor Suite or a different wallet.

Yes, I closed all others and started the stand-alone bridge 'trezord-git' from AUR and tested the bridge.

> Did you try to create a regular wallet first, not a hardware wallet? Just to make sure that that works.

Yes, Monero GUI wallet by itself works ok.

**Everything boils down to the faulty communication between Trezor and Monero GUI _not only_ on Manjaro** !!
and I'm not alone, someone also on NixOS (with many more logs !!)
https://github.com/NixOS/nixpkgs/issues/313470

# Action History
- Created by: OnAirDroid | 2024-05-23T19:03:58+00:00
