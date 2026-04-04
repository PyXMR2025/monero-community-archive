---
title: Wallets created in monero-wallet-gui don't open in monero-wallet-cli and vice
  versa
source_url: https://github.com/monero-project/monero-gui/issues/4141
author: ghost
assignees: []
labels: []
created_at: '2023-03-29T03:04:16+00:00'
updated_at: '2023-03-29T19:44:14+00:00'
type: issue
status: closed
closed_at: '2023-03-29T19:44:14+00:00'
---

# Original Description
I'm using archlinux and have tried the bleeding edge packages(always using `monero-wallet-cli` and `monero-wallet-gui` from the same repo to confirm same version plus higher likelihood of compatibility) from arch community repo, building monero-gui from source, and using binaries from getmonero.org. 
When I create a wallet using `monero-wallet-cli`, I'm unable to open that wallet in `monero-wallet-gui` on archlinux(but can open it on other operating systems after sending the wallet over).
When I create a wallet using `monero-wallet-gui`, I'm unable to open that wallet in both `monero-wallet-cli` on archlinux or with 'monero-wallet-cli' on any other operating system.
I always leave the password blank or copy-paste it in (after various attempts of typing the correct password).

The error that appears in cli when I try to enter password is: "Error: failed to load wallet: invalid password" The error that appears in gui when I try to enter password is: "Couldn't open wallet: invalid password"
the gui also gives the following in terminal when I run `monero-wallet-gui` via a terminal:

```
W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
W Logging to "/home/user/.bitmonero/monero-wallet-gui.log"
W file:///usr/lib/qt/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
W qrc:/wizard/WizardWalletInput.qml:112: TypeError: Cannot read property 'btnPrev' of undefined
W qrc:/wizard/WizardWalletInput.qml:111: TypeError: Cannot read property 'btnPrev' of undefined
W qrc:/wizard/WizardWalletInput.qml:112: TypeError: Cannot read property 'btnPrev' of undefined
W qrc:/wizard/WizardWalletInput.qml:111: TypeError: Cannot read property 'btnPrev' of undefined
W WARNING: no majority of DNS TXT records matched (only 2/7)
E portable_storage: wrong binary format - signature mismatch
E !r. THROW EXCEPTION: error::invalid_password
E Error opening wallet: invalid password
E Error opening wallet with password:  invalid password```

# Discussion History
## plowsof | 2023-03-29T11:50:06+00:00
can't reproduce in manjaro kde password abc123 getmonero dot org binaries

[arch-screen0.webm](https://user-images.githubusercontent.com/77655812/228526494-0c89b5e0-3d03-44d6-9eaa-6bed602b2d1a.webm)



## selsta | 2023-03-29T12:27:22+00:00
Can you confirm that your KDF value field looks like this?

<img width="401" src="https://user-images.githubusercontent.com/7697454/228534806-bb04f4b4-a66c-4ffb-8a7f-b8d9a493ef2e.png">

Did you try pressing "Ok" with your mouse instead of Return / Enter while password entry?

Are you creating a hardware wallet?


## ghost | 2023-03-29T17:23:27+00:00
> Can you confirm that your KDF value field looks like this?
> <img alt="" width="401" src="https://user-images.githubusercontent.com/7697454/228534806-bb04f4b4-a66c-4ffb-8a7f-b8d9a493ef2e.png">
***I describe below how I'm using either 1 or 1024 KDF rounds in every test and use Mainnet every time.***
> Did you try pressing "Ok" with your mouse instead of Return / Enter while password entry?
***yes***
> Are you creating a hardware wallet?
***no***

In all of my attempts to create a wallet, I used either 1024 KDF rounds or used simple mode (and was promptly unable to open the wallet in `monero-wallet-cli`). I believe the set number of KDF rounds may have still been in effect in simple mode from when it was set in advanced mode. I'm using Mainnet in every attempt - I've not used stagenet or testnet in any examples or tests mentioned in or related to this thread.
I just tried advanced mode with 1 KDF round and was able to open open the wallet in `monero-wallet-cli` after its creation in `monero-wallet-gui`. Is this intended behavior? Why can I not open wallets created with 1024 KDF rounds in `monero-wallet-cli after this? Must I set the `--kdf-rounds` argument(after some testing it appears this *does* allow me to open the wallet)? If this is what I must do, would it be best for an update to monero-wallet-cli to automatically detect kdf-rounds to be implemented(or is this not currently possible to implement in a way that doesn't drag down the rest of the application)? 
[Warn When Adjusting KDF Rounds #4076](https://github.com/monero-project/monero-gui/issues/4076) - If there *was* a warning implemented, I certainly didn't see it.

## plowsof | 2023-03-29T19:35:38+00:00
@PeculiarProductions are you kidding me. youve had 2 days of tech support on matrix from 2 people , both of whom have tried to replicate your results and can't. now suddenly you reveal youve changed the number of kdf rounds to 1024. im not going to read the rest of your comment 

## selsta | 2023-03-29T19:42:36+00:00
> Is this intended behavior? 

Yes, you need to set the same KDF rounds everywhere you open the wallet.

> would it be best for an update to monero-wallet-cli to automatically detect kdf-rounds to be implemented

How would this work? Try to decrypt with 1, if it fails 2, ...? This wouldn't work. There might be some ways by saving the KDF round value separately but this would reduce security and is not something we are going to implement.

> If there was a warning implemented, I certainly didn't see it.

Usually it's best to not randomly change settings under advanced options unless you know what they are doing. The issue for adding a warning is still open so it's not implemented yet.

# Action History
- Created by: ghost | 2023-03-29T03:04:16+00:00
- Closed at: 2023-03-29T19:44:14+00:00
