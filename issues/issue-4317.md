---
title: Monero GUI from Manjaro Officiial Repro does NOT recognize TREZOR Safe 3
source_url: https://github.com/monero-project/monero-gui/issues/4317
author: OnAirDroid
assignees: []
labels: []
created_at: '2024-05-23T18:53:15+00:00'
updated_at: '2024-11-10T11:04:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The Monero GUI Wallet (Version 0.18.3.3) from the Manjaro's official repro does NOT recognize the Trezor Safe 3 (device not found) even when the Trezor Suite is open and the 'trezord' bridge is active (confirmed by http://127.0.0.1:21325/status/)!

Then I installed the stand-alone-bridge 'trezord-git' (Version 2.0.33) from AUR (and activated it by /usr/bin/trezord -e 21324), without any success for the Monero GUI Wallet - device NOT found, but the stand-alone-bridge 'trezord-git' works fine as the Exodus Wallet and recognize the Trezor Safe 3!
Unfortunately i couldn't try the other variant 'trezord-go' from AUR due to an build error and my knowledge is not sufficient to correct the build process and find the error. @prusnak
I tried the old stand-alone-bridge 'trezor-bridge-bin' (Version 2.0.30) from AUR as well, without success for the Monero GUI Wallet and of course, always a reboot in between)!

**So it all boils down to a 'device NOT found' by the Monero GUI Wallet (everything else works fine)!**

The integrated bridge in the Trezor AppImage works ok as well as the 'trezord-git' bridge by itself works fine with Exodus Wallet.

Manjaro Linux (KDE 6, latest update)
Kernel 5.15

I've repeated that on another computer (also Manjaro) without success (same results) !!

# Discussion History
## selsta | 2024-05-23T18:58:58+00:00
Does using the binaries from getmonero.org work? If yes, then the issue is with the package itself, it is likely compiled without Trezor support. You have to reach out to the package maintainer.

See https://gitlab.archlinux.org/archlinux/packaging/packages/monero/-/issues/1

## OnAirDroid | 2024-05-23T19:17:16+00:00
with Manjaro Linux I depend on Manjaro's Official Repro and Manjaro can't handle .deb files from getmonero.org!

 

The link you mentioned is for an older version of Monero GUI and as I filled two issues, cause the Flatpak version has a huge glitch as well.

My bug report is for version 0.18.3.3


 

Regards

 

Gesendet: Donnerstag, 23. Mai 2024 um 20:59 Uhr
Von: "selsta" ***@***.***>
An: "monero-project/monero-gui" ***@***.***>
Cc: "OnAirDroid" ***@***.***>, "Author" ***@***.***>
Betreff: Re: [monero-project/monero-gui] Monero GUI from Manjaro Officiial Repro does NOT recognize TREZOR Safe 3 (Issue #4317)


 

Does using the binaries from getmonero.org work? If yes, then the issue is with the package itself, it is likely compiled without Trezor support. You have to reach out to the package maintainer.

See https://gitlab.archlinux.org/archlinux/packaging/packages/monero/-/issues/1

—
Reply to this email directly, view it on GitHub, or unsubscribe.
You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2024-05-23T19:19:29+00:00
I don't know what you mean, we don't have .deb files on getmonero.org, it's a binary that can be opened on any Linux system.

> The link you mentioned is for an older version of Monero GUI

The link is still relevant, it doesn't appear to be fixed yet.


## OnAirDroid | 2024-05-23T19:35:18+00:00
> I don't know what you mean, we don't have .deb files on getmonero.org, it's a binary that can be opened on any Linux system.

OK, I will try the binary and report back.

## OnAirDroid | 2024-05-23T20:24:24+00:00
> I don't know what you mean, we don't have .deb files on getmonero.org, it's a binary that can be opened on any Linux system.

I see it's an AppImage.
I got one step further, but NO solution.
**Now Monero GUI is stuck since 15 minutes on the screen 'OPENING WALLET'!**

I've tried  it with a Standard- and a Hidden Wallet on the Trezor Safe 3 - **same result !!**
(Had to use a kill command for Monero GUI in between, also I restarted the bridge)


Here is what the 'trezord-git' bridge puts out in the terminal
$ /usr/bin/trezord -e 21324
2024/05/23 22:00:00 trezord v2.0.34 (rev db03d99) is starting on port 21325
POST /enumerate
127.0.0.1 - - [23/May/2024:22:01:48 +0200] "POST /enumerate HTTP/1.1" 200 94
POST /acquire/1/null
127.0.0.1 - - [23/May/2024:22:01:49 +0200] "POST /acquire/1/null HTTP/1.1" 200 16
POST /call/1
127.0.0.1 - - [23/May/2024:22:01:50 +0200] "POST /call/1 HTTP/1.1" 200 566
POST /call/1
127.0.0.1 - - [23/May/2024:22:01:50 +0200] "POST /call/1 HTTP/1.1" 200 12
POST /call/1
127.0.0.1 - - [23/May/2024:22:01:52 +0200] "POST /call/1 HTTP/1.1" 200 16
POST /call/1
127.0.0.1 - - [23/May/2024:22:01:52 +0200] "POST /call/1 HTTP/1.1" 200 206
POST /call/1
127.0.0.1 - - [23/May/2024:22:02:57 +0200] "POST /call/1 HTTP/1.1" 200 566
POST /call/1
127.0.0.1 - - [23/May/2024:22:02:57 +0200] "POST /call/1 HTTP/1.1" 200 16
POST /call/1
127.0.0.1 - - [23/May/2024:22:02:57 +0200] "POST /call/1 HTTP/1.1" 200 274

Monero GUI Log attached
[monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/15422254/monero-wallet-gui.log)


## selsta | 2024-05-23T21:49:56+00:00
Please test first to create a regular wallet without Trezor so that we can point out that the issue is elsewhere.

## OnAirDroid | 2024-05-23T22:52:06+00:00
> Please test first to create a regular wallet without Trezor so that we can point out that the issue is elsewhere.

This is mentioned nowhere!
Anyway, I created a usual wallet first, but the creation of a new Hardware Wallet is stuck again on the same screen 'OPENING WALLET' forever!
I had to send a kill command, than I restarted the bridge and opened Monero GUI and the Hardware Test Wallet (which got stuck in the process) is there. In the settings is 'Mnemonic seed protected by hardware device' as it should be, but that was never displayed as the process got stuck on 'OPENING WALLET'!
**Is the private key really in the Trezor?**

I made this test with the Standard Wallet and I wonder now, whether I can use Monero GUI with the Standard Wallet when those bugs are fixed?
For example, if I create a Monero Hardware Wallet in the future will it override the seedphrase (from the tests I've done) or will it block Monero GUI to do so? Does that depend on the Name of that Monero hardware wallet or on the Monero address? How is that handling?

Trezor blames Monero GUI, Monero GUI blames Manjaro and I spent already two days in between!
My summery, Trezor and Monero is a nightmare !!

Good luck for mass adoption ...

## selsta | 2024-05-23T23:16:49+00:00
I'm having a hard time following. Did creating a regular wallet (without Trezor) work?

If yes, did you create a Trezor wallet with or without passphrase? Try creating a wallet without passphrase first to see if you can open it.

> For example, if I create a Monero Hardware Wallet in the future will it override the seedphrase (from the tests I've done) or will it block Monero GUI to do so? Does that depend on the Name of that Monero hardware wallet or on the Monero address? How is that handling?

I don't understand what you are asking here.

## OnAirDroid | 2024-05-23T23:34:29+00:00
> I'm having a hard time following. Did creating a regular wallet (without Trezor) work?

Yes, a regular wallet can be created without any problem.

> If yes, did you create a Trezor wallet with or without passphrase? Try creating a wallet without passphrase first to see if you can open it.

Yes, I've created one without passphrase and I can open it.

> > For example, if I create a Monero Hardware Wallet in the future will it override the seedphrase (from the tests I've done) or will it block Monero GUI to do so? Does that depend on the Name of that Monero hardware wallet or on the Monero address? How is that handling?
> 
> I don't understand what you are asking here.

Listen, I've created now some Hardware Test Wallets without passphrase (some failed and a few seemed to be created, even so the procedure was stuck on 'OPENING WALLET' and a seedphrase was never displayed), that means those are all related to the Trezor Standard Wallet.
What is stored in the Trezor beside the seedphrase?
Can I use the Name of that Monero hardware test wallet again if I delete the Monero folder? How is that handling?

So far I don't have any assets in this Monero GUI wallet and I won't use this Trezor-Monero combination in this BUGGY CONDITION !!

## selsta | 2024-05-23T23:38:16+00:00
Keep in mind for each wallet file, you have to use the same passphrase. Meaning if you want one wallet without passphrase and one with passphrase, you have to create two separate wallet files with different names. You can't use one wallet file with different passphrases.

> Can I use the Name of that Monero hardware test wallet again if I delete the Monero folder? How is that handling?

Yes, you can reuse the wallet name. Only the seedphrase is stored on the Trezor.

> Listen, I've created now some Hardware Test Wallets without passphrase (some failed and a few seemed to be created, even so the procedure was stuck on 'OPENING WALLET' and a seedphrase was never displayed), that means those are all related to the Trezor Standard Wallet.

The seedphrase should never be displayed, the seed is securely stored on the Trezor.

Regarding the stuck on "opening wallet" issue, did you make sure that the Trezor doesn't ask you to do anything on the device? As far as I remember you have to click if you want to enter the passphrase on device or on your computer, and then enter the passphrase.

## OnAirDroid | 2024-05-23T23:50:16+00:00
> Keep in mind for each wallet file, you have to use the same passphrase. Meaning if you want one wallet without passphrase and one with passphrase, you have to create two separate wallet files with different names. You can't use one wallet file with different passphrases.

Yes, I'm aware of that.

> The seedphrase should never be displayed, the seed is securely stored on the Trezor.

**Shouldn't it be displayed in the creation process, like a regular Monero GUI wallet?**
If not, does that mean a Monero Hardware Wallet can only be restored via the Trezor seedphrase?

> Regarding the stuck on "opening wallet" issue, did you make sure that the Trezor doesn't ask you to do anything on the device? As far as I remember you have to click if you want to enter the passphrase on device or on your computer, and then enter the passphrase.

Yes, sure, there wasn't any message on the device to confirm. I watched everything carefully and on top I went through this procedure x-times now!

## selsta | 2024-05-23T23:53:25+00:00
> Shouldn't it be displayed in the creation process, like a regular Monero GUI wallet? If not, does that mean a Monero Hardware Wallet can only be restored via the Trezor seedphrase?

No, the seedphrase will NEVER be displayed. And yes, you need a Trezor to restore the wallet, or you need some a software that can convert your Trezor seed to a monero seed.


## selsta | 2024-05-24T00:03:13+00:00
Unfortunately I don't have a Trezor Safe 3, so I don't know if it's an issue with this model. So far we have not received other reports about your issue.

You said you have access to a different computer, can you try it on that?

## OnAirDroid | 2024-05-24T00:13:05+00:00
> > Shouldn't it be displayed in the creation process, like a regular Monero GUI wallet? If not, does that mean a Monero Hardware Wallet can only be restored via the Trezor seedphrase?
> 
> No, the seedphrase will NEVER be displayed. And yes, you need a Trezor to restore the wallet, or you need some a software that can convert your Trezor seed to a monero seed.

**So to understand correctly, the seedphrase is only displayed for regular wallets, but not for hardware wallets, correct?**

Which software can convert a Trezor seed into a Monero seed?
I'm a bit nervous now due to all those bugs I discovered (Manjaro official repro version does not recognize Trezor, Flatpack version doesn't work and the AppImage gets stuck on 'Opening Wallet')!

My last question!
Even so a hardware wallet creation got stuck in the 'Opening wallet' procedure, but I can open it (after restarting eveything),  **does that means the seedphrase is correctly stored in the Trezor?**

_Anyway,I appreciate your help, thank you very much._


## selsta | 2024-05-24T00:15:34+00:00
> Which software can convert a Trezor seed into a Monero seed?

It's a python tool so not really user friendly: https://github.com/ph4r05/monero-agent/blob/master/PoC.md#trezor-seeds

> Even so a hardware wallet creation got stuck in the 'Opening wallet' procedure, but I can open it (after restarting eveything), does that means the seedphrase is correctly stored in the Trezor?

Yes, the seedphrase is stored completely separately from monero-gui. You can confirm that by creating a wallet, writing down the address. Deleting the wallet, re-creating it again and confirming that the old address matched the new address.

## OnAirDroid | 2024-05-24T01:10:06+00:00
> Yes, the seedphrase is stored completely separately from monero-gui. You can confirm that by creating a wallet, writing down the address. Deleting the wallet, re-creating it again and confirming that the old address matched the new address.

At least one Hardware Wallet was created as I can see by the symbol (Open a wallet from file) and also because in this wallet the seedphrase is not displayed in the setting (Mnemonic seed protected by hardware device).
So I deleted the Monero folder to restore that hardware wallet, but there are many more bugs concerning the restore process !!

![Passphrase](https://github.com/monero-project/monero-gui/assets/30511754/2a048fb5-982e-47cd-a3de-0efdffeae334)

I chose 'Computer', cause this Hardware Wallet was created without a passphrase, so I left it empty and hit OK
The message on the Trezor display 'Please enter your passphrase' stays there forever until I disconnect the device!
The device doesn't accept any input (like frozen) and when I chose from computer I get stuck on the next screen! 

![Restore Wallet](https://github.com/monero-project/monero-gui/assets/30511754/b9b75d25-a4f3-4034-b52d-df82c4d25fe9)

and if i hit restore wallet again it get stuck **forever** on the screen 'Creating Wallet from Device'!

![Creating Wallet from Device](https://github.com/monero-project/monero-gui/assets/30511754/4b52b0e5-f4cd-4d91-b55f-7db7d21bf8ef)

So I wasn't able to restore the Hardware Wallet and I've tried it on a second computer (also Manjaro) without success!

When those bugs bugs hit an average computer user, than there won't be more adoption for Monero!

**I really would appreciate if the Monero GUI and the 'trezord-git' bridge gets tested with all features on Manjaro !!**
It's a nightmare !!

Monero GUI Log File
2024-05-24 00:49:57.171	    7f08d3ee6280	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-05-24 00:49:57.172	    7f08d3ee6280	WARNING	frontend	src/wallet/api/wallet.cpp:411	Logging to "/home/space/.bitmonero/monero-wallet-gui.log"
2024-05-24 00:50:21.350	    7f08d3ee6280	WARNING	frontend	src/wallet/api/wallet.cpp:411	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2024-05-24 00:51:19.080	    7f08d2ad06c0	ERROR	device.trezor	src/device_trezor/device_trezor.cpp:176	Get public address exception: Call method failed
2024-05-24 00:51:19.082	    7f08d2ad06c0	ERROR	account	src/cryptonote_basic/account.cpp:220	Cannot get a device address
2024-05-24 00:52:44.589	    7f08d3ee6280	WARNING	frontend	src/wallet/api/wallet.cpp:411	qrc:/wizard/WizardWalletInput.qml:111: TypeError: Cannot read property 'btnPrev' of undefined
2024-05-24 00:52:44.590	    7f08d3ee6280	WARNING	frontend	src/wallet/api/wallet.cpp:411	qrc:/wizard/WizardWalletInput.qml:112: TypeError: Cannot read property 'btnPrev' of undefined

## selsta | 2024-05-24T16:12:10+00:00
I would recommend to either use a regular wallet (without Trezor), or try on a different computer.

It seems clear there is some issue here than affects all Trezor related communication and it's not possible for me to remotely figure out what is going on.

@ph4r05 any idea what could cause issue with almost all communcation?

## ph4r05 | 2024-05-24T16:24:36+00:00
Hello! We would need more verbose logs. I cannot tell much from this.

There was a way to increase log level but I wasnt involved for quite some time so I don't remember right now.

The usual suspects: invalid passphrase (if any), broken cable, some other trezor app running. Trezor Suite at some point enabled passphrase, maybe try enabling it and use an empty one. (Seed is stored on the device, passphrase is never stored anywhere).

It should use libusb/webusb not bridge. If bridge is involved, update to the latest, reboot and try again with higher log level.

## OnAirDroid | 2024-05-24T19:59:01+00:00
Thank you for looking into the problem.

> Hello! We would need more verbose logs. I cannot tell much from this.
> 
Verbose log? What I have to do to get those?

> There was a way to increase log level but I wasn't involved for quite some time so I don't remember right now.
> 
Nor do I !!

> The usual suspects: invalid passphrase (if any), broken cable, some other trezor app running. Trezor Suite at some point enabled passphrase, maybe try enabling it and use an empty one. (Seed is stored on the device, passphrase is never stored anywhere).

None of this applies!
I've tried different cables, a second computer (also Manjaro), with new passphrases (of course passphrases are enabled), and also without a passphrase, no other Trezor app was running,

> It should use libusb/webusb not bridge. If bridge is involved, update to the latest, reboot and try again with higher log level.

Do I understand that correctly, a bridge is NOT needed at all ??
**_EDIT:_** Without the 'trezord-git' bridge (latest version from AUR), Monoero GUI is stuck on 'Creating wallet from device' forever!

Would log level 4 be good enough or is that just for the deamon?

With the bridge I come until the second screenshot of my previous post.
[monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/15439714/monero-wallet-gui.log)

Who is in charge to solve that problem? Whom to ping?

## selsta | 2024-05-24T23:40:15+00:00
@OnAirDroid can you open a regular wallet (without Trezor), go to Settings -> Log, set it to level 4 and then try to open the Trezor wallet and share the log file?

Or did you already do that in the last .log file you shared?

Currently it only shows that it fails, but not why

```
2024-05-24 20:16:43.236	    7fd1fbfff6c0	ERROR	device.trezor	src/device_trezor/device_trezor.cpp:176	Get public address exception: Call method failed
2024-05-24 20:16:43.237	    7fd1fbfff6c0	ERROR	account	src/cryptonote_basic/account.cpp:220	Cannot get a device address
```

## OnAirDroid | 2024-05-25T01:50:35+00:00
> @OnAirDroid can you open a regular wallet (without Trezor), go to Settings -> Log, set it to level 4 and then try to open the Trezor wallet and share the log file?
> Or did you already do that in the last .log file you shared?

Yes, it's the previous log file was done with level 4.
Here one more (Opening Wallet stays forever)
[monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/15441075/monero-wallet-gui.log)

I made another Test and installed the Monero GUI AppImage on Tails and **wow everything works without a bridge!** out of the box  (no bridge needed as @ph4r05 mentioned)!
I imported the same Hardware Wallet from the Trezor Standard Wallet (which failed as mentioned in my previous post on Manjaro with the same Monero GUI AppImage used on Tails).
EDIT: Even so it works, but there is a glitch, sometimes the wallet 'Opening Screen' and the wallet 'Closing Screen' stay forever!

In summery the Trezor device is ok, the cable is ok, the recover of the Hardware Wallet is ok (same computer) !!

**Everything boils down to the faulty communication between Trezor and Monero GUI _not only_ on Manjaro** (in opposite to Tails/Debian) the 'trezord' bridge **is needed** (if I don't start the bridge, Trezor is not recognized at all on Manjaro).

I really hope that one of the devs looks into that problem as Manjaro belongs to the top 5 distros and many users will be unhappy and frustrated with Trezor and the Monero GUI @kpcyrd
Will be just a matter of time when the complains flood the net.

**I appreciate your help and I'm looking forward to a solution for that faulty communication on Manjaro ...**
and I'm not alone, someone also on NixOS (with many more logs !!)
https://github.com/NixOS/nixpkgs/issues/313470


## kpcyrd | 2024-05-26T15:34:13+00:00
> We have added USE_DEVICE_TREZOR_MANDATORY CMake variable to the master branch, but since this was a larger change we didn't port it to the release banch yet.

https://github.com/monero-project/monero-gui/issues/4105#issuecomment-2068288488

This flag is still not released, but hopefully stops the monero build from silently disabling hardware wallet support in the future.

## OnAirDroid | 2024-05-26T20:56:33+00:00
> This flag is still not released, but hopefully stops the monero build from silently disabling hardware wallet support in the future.

The faulty build process is one thing, but the AppImage (from getmonero.org) which includes the Trezor support doesn't work on Manjaro (and most likely on other distros) as described on my posts above! @kpcyrd

**There is at least one more major issue concerning the communication (via the trezord-git bridge) as @selsta stated correctly!**

Trezor Safe 3 is out since 8 month and it's very disappointing! @matejcik @prusnak

Even the Trezor Support wasted my time and recommended the Flatpak version, not aware about the first thing to test is the original AppImage!

## matejcik | 2024-05-27T11:34:11+00:00
weirdly enough @OnAirDroid is onto something here.
I was able to reproduce the problem _without bridge_ on a fresh install of the official Monero GUI appimage: after entering valid wallet password, monero got stuck at "Opening wallet..." forever, with only this in the log:
```
2024-05-27 11:27:54.483	W Account on device. Initing device...
```
When started **with** bridge, the right wallet came up ~instantly, and afterwards it would work even without bridge, so I was not able to reproduce the same thing again.

A possibly related problem I detected can be reproduced as follows:
1. set up a Trezor wallet with a passphrase
2. close and reopen monero gui
3. open the wallet
4. when prompted, enter **wrong** passphrase
5. monero will complain and want you to re-enter your wallet password
6. reenter
7. now monero will get stuck forever on "Opening wallet"

log also only says "Initing device..."

full log attached
[monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/15455316/monero-wallet-gui.log)

## Nygosaki | 2024-11-10T11:04:19+00:00
I am facing the same issue, though on Debian (12).   
I am trying to create a new wallet from hardware with my Trezor Safe 3.   
First, it says it can not connect to the device, and when I click continue again, it just gets stuck on "creating hardware wallet".    
I can create normal wallets just fine.

[Log here](https://pastebin.com/qL162hYs)    
The first time is just leaving the Trezor in and clicking the continue button two times.   
The second time is disconnecting and reconnecting my Trezor after it says it can not find the device.    

# Action History
- Created by: OnAirDroid | 2024-05-23T18:53:15+00:00
