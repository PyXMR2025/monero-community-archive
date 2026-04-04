---
title: GUI wallet suddenly not opening through Trezor Model T
source_url: https://github.com/monero-project/monero-gui/issues/4105
author: Benjvoo
assignees: []
labels: []
created_at: '2023-01-18T05:10:11+00:00'
updated_at: '2024-04-22T00:32:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello and best wishes to you all. A quick question from a beginner to Monero gui wallet. I was able to set up GUI wallet and use it through the Trezor Model T. The set up was working great. Had not opened the wallet for a month and when I recently tried to open it I could not get past the second password requirement (which asks for the Trezor device password, the primary XMR GUI password is accepted). Getting an error message "Couldn't open wallet cannot get a device address." I've turned off all anti virus programs, even tried outside VPN. No luck. Has anyone encountered this problem or have any suggestions? Thanks so much

# Discussion History
## selsta | 2023-01-21T09:20:40+00:00
Can you add a screenshot of the exact error?

Also did you try entering an empty passphrase?

## plowsof | 2023-01-21T20:32:16+00:00
@selsta https://github.com/monero-project/monero/pull/8713 related?



## Benjvoo | 2023-01-22T08:17:50+00:00
I should mention I'm on Windows 10. The passwords must be correct because the Trezor password opens Trezor Suite software and the initial log in window for Moneru GUI wallet works. It is the 2nd password step that is failing (into which I am to enter the Trezor password). I have tired the 2nd password screen with no password and it is the same error. I will paste screenshot below. Any ideas would be greatly appreciated. The screenshot the error screen I am receiving directly after inputting the 2nd step (Trezor) password. 
![Fullscreen capture 1222023 25555 PM](https://user-images.githubusercontent.com/105096057/213906640-1cb269ba-0a39-403b-8969-de3253934b1b.jpg)


## Benjvoo | 2023-01-22T08:19:44+00:00
> @selsta [monero-project/monero#8713](https://github.com/monero-project/monero/pull/8713) related?

yes same , sorry if I added confusion

## selsta | 2023-01-26T22:50:19+00:00
@ph4r05 any idea here?

## ph4r05 | 2023-01-26T23:10:41+00:00
It would be great if we can get the Monero GUI logs. Message "Cannot get a device address" is from the first message call to the Trezor, there are various checks performed, so having logs could help identifying the culprit.

@Benjvoo, pls check if TrezorSuite enabled Passphrase for Trezor. The thing is that any passphrase works in principle with Trezor. No error will be shown if you type totally different passphrase, as it generates new wallet secrets for that particular passphrase (to  any passphrase exists some wallet secret, plausible deniability). So if you created a Monero wallet with another passphrase that you are using now, you will be getting errors like this. Try various possible passphrases.

Then there is a wallet password - totally unrelated to Trezor. Any Monero wallet has it, it is used to encrypt wallet file on the PC.

Few suggestions:
- Try reconnecting Trezor
- TrezorSuite cannot be running simultaneously with Monero wallet
- Make sure Trezor bridge is installed
- Try empty passphrase

## HumanG33k | 2023-01-30T18:24:44+00:00
Not sure it's related but on my macOs when i first updated to last version the app crash after password asking form. After i read the stacktrace i see it's try to open the previous version. So instead of replace current .app in software i delete existing one and install the new version (drag & drop). And it works. If dev need the stacktrace i made a backup. 

## thestinger | 2023-02-17T04:07:07+00:00
I can reproduce this issue on Arch Linux where monero-gui-wallet is dynamically linked against libusb (1.0.26) and hidapi (0.13.1) so I don't think the issue is caused by out-of-date dependencies. Trezor Suite works fine. Issue occurs with or without running trezord (Trezor Bridge), which I've never needed to run separately before. Downgrading to an old release of the Monero software doesn't resolve the issue so I suspect it was caused by a recent Trezor Model T firmware update, but that doesn't mean the problem is in the Trezor Model T firmware rather than the Monero wallet.

## thestinger | 2023-02-17T04:09:28+00:00
@ph4r05 The hardware wallet passphrase entry dialog never appears after entering the wallet passphrase. monerod crashes. I haven't yet gotten a useful traceback since Arch packages have debug symbols stripped. There are split debug packages and I can translate the traceback later when I have time.

```

2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::system::system_error>
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /usr/bin/monerod(+0x5eaad) [0x5c334378daad]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/bin/monerod(+0x192b96) [0x5c33438c1b96]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /usr/bin/monerod(+0x276503) [0x5c33439a5503]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /usr/bin/monerod(+0x27c3e6) [0x5c33439ab3e6]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /usr/bin/monerod(+0x2aa1a0) [0x5c33439d91a0]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /usr/bin/monerod(+0x2ad572) [0x5c33439dc572]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /usr/bin/monerod(+0x1749e2) [0x5c33438a39e2]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /usr/lib/libc.so.6(+0x23790) [0x71667943c790]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x8a) [0x71667943c84a]:__libc_start_main+0x8a) [0x71667943c84a]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/bin/monerod(+0x1885c5) [0x5c33438b75c5]
2023-02-17 04:05:30.873	    716679ceda00	INFO	stacktrace	src/common/stack_trace.cpp:172	

## prusnak | 2023-02-17T19:46:25+00:00
> a recent Trezor Model T firmware update

What version of Trezor firmware are you using right now?
Do you remember what version you were using before the update?

Here's the list of Trezor Model T updates which might help figuring the versions out:
* 2.5.3 (16th November 2022)
* 2.5.2 (17th August 2022)
* 2.5.1 (18th May 2022)
* 2.4.3 (8th December 2021)

## prusnak | 2023-02-17T19:52:22+00:00
Worth checking out - can these be related? https://github.com/trezor/trezor-firmware/issues/2811

## thestinger | 2023-02-17T20:43:15+00:00
Currently on 2.5.3 and likely have been since early December at at the latest. Would have previously been on 2.5.2 since early September at the latest. It could be that it stopped working after updating to 2.5.3.

I send a Bitcoin transaction every month to fund multiple other developers but I don't regularly use the other cryptocurrencies. Been checking on the Monero every few months to see how much is available and noticed a few days ago that it was no longer working. This issue was fairly issue to find.

After entering the Monero GUI wallet decryption password, the Trezor Model T prompts for the passphrase but the Monero GUI wallet shows an error caused by the issue above instead of showing the usual prompt for choosing between entry on the computer or the hardware wallet.

I tried several older Arch Linux releases of the Monero GUI wallet which required running it in a container where I had to install OpenSSL 1.1.x and downgrade Boost since it was linked against older library versions. I tried ones from mid-2022 back when it was definitely working.

I don't know what has changed in the Trezor firmware recently but my suspicion was that it's either a firmware bug or a Monero GUI wallet bug that was previously not triggered until after a firmware update. Not necessarily a firmware bug but I think it was caused by a firmware change even if the bug is on the Monero wallet side of things.

## selsta | 2023-02-17T20:45:36+00:00
@thestinger can you reproduce with the getmonero.org binaries?

## thestinger | 2023-02-17T20:49:58+00:00
I'll try that next.

I just tried moving away my current wallet state and restoring which didn't work and triggered a similar error.

## prusnak | 2023-02-17T20:51:30+00:00
@thestinger you can also try downgrading to 2.5.2 via `trezorctl firmware update --version 2.5.2` (the seed will not be erased because the minor version stays the same, but anyway, don't do this unless you are 100% sure you can recover if something goes bad).

## thestinger | 2023-02-17T20:55:07+00:00
@prusnak I have proper seed phrase backups and could do a dry run test and then test that.

## thestinger | 2023-02-17T20:57:31+00:00
@selsta Doesn't help. This is the error I get running it without trezord:

```
2023-02-17 20:53:44.558	E Get public address exception: Trezor returned unexpected message: 17
2023-02-17 20:53:44.559	E !dev_cold->get_public_address_with_no_passphrase(device_account_public_address). THROW EXCEPTION: error::wallet_internal_error
2023-02-17 20:53:44.559	E Error opening wallet: Cannot get a device address
2023-02-17 20:53:44.559	E Error opening wallet with password:  Cannot get a device address
```

This is the error with trezord running separately:

```
2023-02-17 20:56:24.200	    76b2c4c566c0	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:4482	Account on device. Initing device...
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] monero-wallet-gui(+0x1566c6) [0x5eb829f786c6]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] monero-wallet-gui(+0x4ca45d) [0x5eb82a2ec45d]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] monero-wallet-gui(+0x30a7ba) [0x5eb82a12c7ba]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] monero-wallet-gui(+0x284cb7) [0x5eb82a0a6cb7]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] monero-wallet-gui(+0x2aba1f) [0x5eb82a0cda1f]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] monero-wallet-gui(+0x23381d) [0x5eb82a05581d]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] monero-wallet-gui(+0x233bb5) [0x5eb82a055bb5]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] monero-wallet-gui(+0x23d6a6) [0x5eb82a05f6a6]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /usr/lib/libQt5Core.so.5(+0xe8251) [0x76b2cb6e8251]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/lib/libQt5Core.so.5(+0xe432a) [0x76b2cb6e432a]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /usr/lib/libc.so.6(+0x85bb5) [0x76b2caa9ebb5]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /usr/lib/libc.so.6(+0x107d90) [0x76b2cab20d90]
2023-02-17 20:56:24.200	    76b2c4c566c0	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

## thestinger | 2023-02-17T20:58:23+00:00
Note: that traceback is from the getmonero.org release rather than the Arch Linux build like the previous one above.

## thestinger | 2023-02-17T20:59:37+00:00
That `get_public_address_with_no_passphrase` method call is suspicious because I do have a BIP39 passphrase for it so it looks like it's doing the wrong thing.

## thestinger | 2023-02-17T21:03:29+00:00
> Worth checking out - can these be related? [trezor/trezor-firmware#2811](https://github.com/trezor/trezor-firmware/issues/2811)

This does seem related.

## matejcik | 2023-02-17T23:11:19+00:00
message 17 is `Features`.

This looks more like some sort of crosstalk: Monero is expecting a response for GetPublicKey (or the Monero equivalent) but is getting back Features. This is not something a Trezor device will just randomly do in a firmware upgrade. Either there is another program talking to the device at the same time (?) or Monero introduced a bug where they call `Initialize` or `GetFeatures` and then don't read the response. The subsequent call would send a new message, but read the previous response.

## thestinger | 2023-02-17T23:55:03+00:00
There's nothing else running and Trezor Suite runs fine, so it must be a Monero GUI Wallet bug. I'm not sure why older releases didn't work for me. I could try older releases from the official site next instead of older Arch packages which may simply be having issues due to not downgrading enough packages in the container where I tried to get that to work.

## thestinger | 2023-02-17T23:55:33+00:00
It could be from a dependency that got updated both in the Monero GUI Wallet and in Arch Linux.

## ph4r05 | 2023-02-18T02:47:15+00:00
I can check @matejcik 's suggestion on reading Features / Initialize response correctly

## ph4r05 | 2023-02-18T20:33:46+00:00
@thestinger 
> There's nothing else running and Trezor Suite runs fine

Just to clarify, when using Monero GUI, Trezor Suite is not running, correct? 
Ideally:
- stop all applications that may be using Trezor device (Trezor suite, maybe https://suite.trezor.io/web/ is running in some web browser tab)
- kill even monero-gui
- reconnect Trezor to make sure it is reset to a default state
- start Monero GUI

Another option is to recompile Monero from sources on your machine with debugging (@selsta it is `make debug`, right?), if possible. We could get more useful info, including debugging logging messages.

Function `get_public_address_with_no_passphrase` being called is OK, in the linked flow we firstly try opening Trezor without passphrase and match it to the address stored in your wallet. If this fails, Passphrase will be prompted. https://github.com/monero-project/monero/blob/75d80d431a9586996c559cb39f3eabebad3da60a/src/wallet/wallet2.cpp#L4501

You get an error during the first logical message message to the Trezor. It seems that it may be left in invalid state or something else was talking to it.

@matejcik I presume there was no change of the init / passphrase flow since the last upgrade which we integrated to monero codebase, right?

I will go through passphrase logic in monero codebase in the following days and do some cleanup, remove old code and backward compatibility with old devices, this should make code simpler. 

---------
@matejcik 
> message 17 is `Features`.
> 
> This looks more like some sort of crosstalk: Monero is expecting a response for GetPublicKey (or the Monero equivalent) but is getting back Features. This is not something a Trezor device will just randomly do in a firmware upgrade. Either there is another program talking to the device at the same time (?) or Monero introduced a bug where they call `Initialize` or `GetFeatures` and then don't read the response. The subsequent call would send a new message, but read the previous response.

This is a good hypothesis. I've just checked it out, I initialize Trezor with 
https://github.com/monero-project/monero/blob/da9aa1f7f802552b9de459f331a2f39c84898009/src/device_trezor/device_trezor_base.cpp#L385

But `client_exchange` https://github.com/monero-project/monero/blob/da9aa1f7f802552b9de459f331a2f39c84898009/src/device_trezor/device_trezor_base.hpp#L143 

always calls `call_raw` https://github.com/monero-project/monero/blob/da9aa1f7f802552b9de459f331a2f39c84898009/src/device_trezor/device_trezor_base.cpp#L281 which is basically write and read. We should always read the response. 



## thestinger | 2023-02-18T22:09:50+00:00
Trezor Suite and other applications that may use it aren't running and it happens with it freshly connected and unlocked. I can try on Windows and macOS instead of Arch Linux since there are other computers around, although they don't have the Monero state on them.

## ph4r05 | 2023-02-18T23:15:37+00:00
Another idea - increase log level to capture also debugging logs and pls check which transfer protocol is used for Trezor comm

## RootInit | 2023-02-23T09:49:09+00:00
I also have this issue.
The Appimage version works.

## ph4r05 | 2023-02-23T15:47:49+00:00
Another tip - do you have just one Trezor connected?

## thestinger | 2023-02-23T15:53:38+00:00
It's one Trezor and no other software. I think a good question would be whether anyone has a Trezor Model T working with updated firmware + updated Monero GUI wallet, and if they do have it working what OS, etc. they are using.

## selsta | 2023-02-24T00:28:29+00:00
I can confirm that I can open my Trezor wallet with

- Firmware: 2.5.3
- Version: GUI v0.18.1.2 and soon to be released v0.18.2.0
- OS: macOS 13.3

## dmitryd | 2023-03-07T12:35:14+00:00
I have this error if I try to enter the passphrase from the computer. It works if I enter the passphrase on my Trezor. So it must be a GUI issue.

## selsta | 2023-03-07T13:03:12+00:00
@dmitryd Please post more information, which Trezor firmware? Which GUI version? Can you reproduce the issue with the CLI wallet?

## dmitryd | 2023-03-07T13:20:48+00:00
OS: macOS Monterey
Model: T
GUI: 0.18.2.0-release (Qt 5.12.8)
Trezor firmware: 2.5.3 universal
CLI: sorry, no CLI here :( 

Initially Monero GUI cannot connect to the device at all. I have to start `trezord` manually. Then I enter wallet password and GUI asks me about passphrase. Now I can choose either computer or wallet to enter the passphrase.

If I choose computer, I can type the passphrase (and it is correct) but I am getting the error from the first post about the device address. At this time Trezor shows that it is waiting for the passphrase. Nothing can be done after on the Trezor itself that because Trezor still waits for the passphrase until it is disconnected. Even if I close Monero GUI, Trezor still waits for the passphrase.

If I select to enter passphrase on the device, GUI opens fine and I see my wallet.

## ph4r05 | 2023-03-08T22:22:53+00:00
Thanks for the further clarification @dmitryd! 

Unfortunately, I was not able to replicate the problem. I used the newest Trezor firmware, built newest monero-gui 710e3f694817b6db48092702ca061228e44a67cb (tagged v0.18.2.0).

Using "computer" mode is discouraged as pc-running malware can intercept the passhrapse, but this mode should work nevertheless. Glad to hear that on-device entry works fine. 

> If I choose computer, I can type the passphrase (and it is correct) but I am getting the error from the first post about the device address. At this time Trezor shows that it is waiting for the passphrase. Nothing can be done after on the Trezor itself that because Trezor still waits for the passphrase until it is disconnected. Even if I close Monero GUI, Trezor still waits for the passphrase.

It is preferable to reconnect Trezor before starting Monero wallet to reset Trezor state.

> Initially Monero GUI cannot connect to the device at all. I have to start trezord manually. 

This is interesting as Monero-gui should have libusb linked, trezor bridge should not be required.

Experiment, install python trezor lib

```
pip3 install trezor
```

and print connected trezor paths:
```
$> trezorctl list

webusb:000:1 - (unnamed) [Trezor T, serialnum]
bridge:3 - (unnamed) [Trezor T, serialnum]
```
 
I have 1 Trezor connected, accessible via libusb (webusb) and bridge.

Then you can start monero-gui app with both paths and test it (log level is increased): 
```
MONERO_LOG_LEVEL=4 TREZOR_PATH=webusb:000:1 /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
```

If started from terminal, you will see the logs in the terminal directly. 

I tested both libusb and bridge methods, Trezor initialized with passphrase and pin enabled, it worked smoothly. (Just for completeness I suggest trying another USB cable, it tends to be a culprit quite often).

## prusnak | 2023-03-09T08:59:57+00:00
It almost sounds like the GUI is mangling some passphrase characters?

@ph4r05 Is it possible that when you were trying to reproduce the issue you used a simple passphrase with no special characters?

@dmitryd Can you confirm that your passphrase has special characters in it? (I assume you are not using UTF-8, since you can't enter them on the device, so by special characters I mean chars like `!@#$%^&*()_` etc.)

## dmitryd | 2023-03-09T09:01:59+00:00
@prusnak Only letters and numbers in this particular wallet.

## prusnak | 2023-03-09T09:08:06+00:00
> Only letters and numbers in this particular wallet.

Are you sure that it is numbers being entered in GUI? For example the Czech keyboard has this in place of the number row: `+ěščřžýáíé`, so if you enter 234 while this layout is selected you'll get `ěšč`.

(Sorry if this is obvious, but I am trying to eliminate all possibilities to reduce the search space for errors).

## dmitryd | 2023-03-09T09:19:48+00:00
@ph4r05 

If I connect trezor:

```
$ trezorctl list
webusb:002:1 - C1 [Trezor T, D***]
```

When I connect trezor, I have no daemon running automatically:

```
$ ps aux | grep trezord
dmitry           46072   0.0  0.0 408637584   1792 s002  S+   12:10PM   0:00.00 grep trezord
```

Now if I open GUI, it asks me to enter wallet password, recognizes it but then says "Couldn't open wallet: Could not connect to the device Trezor". So I start the daemon manually in verbose mode to see what GUI does:

```
$ trezord -v
2023/03/09 12:11:39 trezord v2.0.32 (rev 9aa6576) is starting
[0.000167 : 12:11:39] [trezord.go 78 main.initUsb] Initing libusb
[0.000201 : 12:11:39] [usb/libusb.go 63 usb.InitLibUSB] init
[0.002810 : 12:11:39] [usb/libusb.go 74 usb.InitLibUSB] init done
[0.002840 : 12:11:39] [trezord.go 89 main.initUsb] Initing hidapi
[0.002854 : 12:11:39] [trezord.go 191 main.main] UDP port count - 0
[0.002866 : 12:11:39] [trezord.go 213 main.main] Creating core
[0.002881 : 12:11:39] [trezord.go 215 main.main] Creating HTTP server
[0.002897 : 12:11:39] [server/http.go 36 server.New] starting
[0.003271 : 12:11:39] [server/http.go 71 server.New] server created
[0.003285 : 12:11:39] [trezord.go 222 main.main] Running HTTP server
```

Next I try again to enter my wallet password. There are some POST calls and then is a lot of background activity, never ending:
```
POST /enumerate
[47.887919 : 12:12:27] POST /enumerate
[47.891757 : 12:12:27] [server/api/api.go 102 server/api.(*api).Enumerate] start
[47.891786 : 12:12:27] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 0
[47.891807 : 12:12:27] [core/core.go 256 core.(*Core).Enumerate] bus
[47.891831 : 12:12:27] [usb/libusb.go 122 usb.(*LibUSB).Enumerate] low level enumerating
[47.891916 : 12:12:27] [usb/libusb.go 128 usb.(*LibUSB).Enumerate] low level enumerating done
[47.891939 : 12:12:27] [usb/libusb.go 347 usb.(*LibUSB).match] start
[47.892006 : 12:12:27] [usb/libusb.go 361 usb.(*LibUSB).match] matched, get active config
[47.892052 : 12:12:27] [usb/libusb.go 369 usb.(*LibUSB).match] let's test
[47.892073 : 12:12:27] [usb/libusb.go 391 usb.(*LibUSB).match] matched
[47.892094 : 12:12:27] [usb/libusb.go 148 usb.(*LibUSB).Enumerate] getting device descriptor
[47.892120 : 12:12:27] [usb/libusb.go 347 usb.(*LibUSB).match] start
[47.892141 : 12:12:27] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[47.892160 : 12:12:27] [usb/libusb.go 347 usb.(*LibUSB).match] start
[47.895101 : 12:12:27] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[47.895423 : 12:12:27] [usb/libusb.go 347 usb.(*LibUSB).match] start
[47.895466 : 12:12:27] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[47.895496 : 12:12:27] [usb/libusb.go 131 usb.(*LibUSB).Enumerate.func1] freeing device list
[47.895528 : 12:12:27] [usb/libusb.go 133 usb.(*LibUSB).Enumerate.func1] freeing device list done
[47.895559 : 12:12:27] [usb/hidapi.go 42 usb.(*HIDAPI).Enumerate] low level
[47.903019 : 12:12:27] [usb/hidapi.go 45 usb.(*HIDAPI).Enumerate] low level done
[47.903129 : 12:12:27] [core/core.go 266 core.(*Core).Enumerate] release disconnected
[47.903152 : 12:12:27] [server/api/api.go 108 server/api.(*api).Enumerate] encoding and exiting
127.0.0.1 - - [09/Mar/2023:12:12:27 +0300] "POST /enumerate HTTP/1.1" 200 94
[47.903360 : 12:12:27] 127.0.0.1 - - [09/Mar/2023:12:12:27 +0300] "POST /enumerate HTTP/1.1" 200 94
POST /acquire/1/null
[47.904243 : 12:12:27] POST /acquire/1/null
[47.904372 : 12:12:27] [core/core.go 434 core.(*Core).Acquire] input path 1 prev
[47.904396 : 12:12:27] [core/core.go 438 core.(*Core).Acquire] actually previous
[47.904417 : 12:12:27] [core/core.go 471 core.(*Core).Acquire] trying to connect
[47.904438 : 12:12:27] [core/core.go 500 core.(*Core).tryConnect] try number 0
[47.904459 : 12:12:27] [usb/libusb.go 181 usb.(*LibUSB).Connect] low level enumerating
[47.904512 : 12:12:27] [usb/libusb.go 187 usb.(*LibUSB).Connect] low level enumerating done
[47.904534 : 12:12:27] [usb/libusb.go 347 usb.(*LibUSB).match] start
[47.904554 : 12:12:27] [usb/libusb.go 361 usb.(*LibUSB).match] matched, get active config
[47.904582 : 12:12:27] [usb/libusb.go 369 usb.(*LibUSB).match] let's test
[47.904602 : 12:12:27] [usb/libusb.go 391 usb.(*LibUSB).match] matched
[47.904623 : 12:12:27] [usb/libusb.go 347 usb.(*LibUSB).match] start
[47.904642 : 12:12:27] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[47.904660 : 12:12:27] [usb/libusb.go 347 usb.(*LibUSB).match] start
[47.904707 : 12:12:27] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[47.904733 : 12:12:27] [usb/libusb.go 347 usb.(*LibUSB).match] start
[47.904754 : 12:12:27] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[47.904797 : 12:12:27] [usb/libusb.go 287 usb.(*LibUSB).connect] detect old BL
[47.904825 : 12:12:27] [usb/libusb.go 293 usb.(*LibUSB).connect] low level
[47.904977 : 12:12:27] [usb/libusb.go 298 usb.(*LibUSB).connect] reset
[48.049708 : 12:12:27] [usb/libusb.go 224 usb.(*LibUSB).setConfiguration] current configuration 1
[48.049768 : 12:12:27] [usb/libusb.go 227 usb.(*LibUSB).setConfiguration] not setting config, same
[48.049777 : 12:12:27] [usb/libusb.go 272 usb.(*LibUSB).claimInterface] claiming interface
[48.051943 : 12:12:27] [usb/libusb.go 280 usb.(*LibUSB).claimInterface] claiming interface done
[48.051965 : 12:12:27] [usb/libusb.go 190 usb.(*LibUSB).Connect.func1] freeing device list
[48.051975 : 12:12:27] [usb/libusb.go 192 usb.(*LibUSB).Connect.func1] freeing device list done
[48.051985 : 12:12:27] [core/core.go 486 core.(*Core).Acquire] new session is 1
127.0.0.1 - - [09/Mar/2023:12:12:27 +0300] "POST /acquire/1/null HTTP/1.1" 200 16
[48.052231 : 12:12:27] 127.0.0.1 - - [09/Mar/2023:12:12:27 +0300] "POST /acquire/1/null HTTP/1.1" 200 16
POST /call/1
[48.057303 : 12:12:27] POST /call/1
[48.057351 : 12:12:27] [server/api/api.go 196 server/api.(*api).call] start
[48.057380 : 12:12:27] [core/core.go 568 core.(*Core).Call] checking other call on same session
[48.057393 : 12:12:27] [core/core.go 574 core.(*Core).Call] checking other call on same session done
[48.057403 : 12:12:27] [core/core.go 599 core.(*Core).Call] before actual logic
[48.057412 : 12:12:27] [core/core.go 607 core.(*Core).writeDev] decodeRaw
[48.057419 : 12:12:27] [core/core.go 659 core.(*Core).decodeRaw] readAll
[48.057426 : 12:12:27] [core/core.go 661 core.(*Core).decodeRaw] decodeString
[48.057433 : 12:12:27] [core/core.go 681 core.(*Core).decodeRaw] returning
[48.057440 : 12:12:27] [core/core.go 613 core.(*Core).writeDev] writeTo
[48.057447 : 12:12:27] [wire/v1.go 25 wire.(*Message).WriteTo] start
[48.057453 : 12:12:27] [wire/v1.go 39 wire.(*Message).WriteTo] actually writing
[48.057473 : 12:12:27] [usb/libusb.go 557 usb.(*LibUSBDevice).Write] write start
[48.057480 : 12:12:27] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[48.057485 : 12:12:27] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[48.057496 : 12:12:27] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[48.058052 : 12:12:27] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[48.058076 : 12:12:27] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[48.058086 : 12:12:27] [core/core.go 619 core.(*Core).readDev] readFrom
[48.058094 : 12:12:27] [wire/v1.go 76 wire.ReadFrom] start
[48.058101 : 12:12:27] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[48.060382 : 12:12:27] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[48.060413 : 12:12:27] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[48.060423 : 12:12:27] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[48.087153 : 12:12:27] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[48.087200 : 12:12:27] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[48.087211 : 12:12:27] [wire/v1.go 96 wire.ReadFrom] actual reading started
[48.087222 : 12:12:27] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[48.087229 : 12:12:27] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[48.087235 : 12:12:27] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[48.087245 : 12:12:27] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[48.088045 : 12:12:27] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[48.088060 : 12:12:27] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[48.088068 : 12:12:27] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[48.088078 : 12:12:27] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[48.088096 : 12:12:27] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[48.088102 : 12:12:27] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[48.089048 : 12:12:27] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[48.089060 : 12:12:27] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[48.089067 : 12:12:27] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[48.089075 : 12:12:27] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[48.089082 : 12:12:27] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[48.089088 : 12:12:27] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[48.090052 : 12:12:27] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[48.090066 : 12:12:27] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[48.090081 : 12:12:27] [wire/v1.go 119 wire.ReadFrom] actual reading finished
[48.090088 : 12:12:27] [core/core.go 625 core.(*Core).readDev] encoding back
[48.090097 : 12:12:27] [core/core.go 691 core.(*Core).encodeRaw] start
[48.090105 : 12:12:27] [core/core.go 601 core.(*Core).Call] after actual logic
127.0.0.1 - - [09/Mar/2023:12:12:27 +0300] "POST /call/1 HTTP/1.1" 200 482
[48.090130 : 12:12:27] 127.0.0.1 - - [09/Mar/2023:12:12:27 +0300] "POST /call/1 HTTP/1.1" 200 482
POST /call/1
[48.091062 : 12:12:27] POST /call/1
[48.091088 : 12:12:27] [server/api/api.go 196 server/api.(*api).call] start
[48.091108 : 12:12:27] [core/core.go 568 core.(*Core).Call] checking other call on same session
[48.091117 : 12:12:27] [core/core.go 574 core.(*Core).Call] checking other call on same session done
[48.091124 : 12:12:27] [core/core.go 599 core.(*Core).Call] before actual logic
[48.091132 : 12:12:27] [core/core.go 607 core.(*Core).writeDev] decodeRaw
[48.091139 : 12:12:27] [core/core.go 659 core.(*Core).decodeRaw] readAll
[48.091145 : 12:12:27] [core/core.go 661 core.(*Core).decodeRaw] decodeString
[48.091155 : 12:12:27] [core/core.go 681 core.(*Core).decodeRaw] returning
[48.091163 : 12:12:27] [core/core.go 613 core.(*Core).writeDev] writeTo
[48.091172 : 12:12:27] [wire/v1.go 25 wire.(*Message).WriteTo] start
[48.091180 : 12:12:27] [wire/v1.go 39 wire.(*Message).WriteTo] actually writing
[48.091189 : 12:12:27] [usb/libusb.go 557 usb.(*LibUSBDevice).Write] write start
[48.091197 : 12:12:27] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[48.091206 : 12:12:27] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[48.091212 : 12:12:27] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[48.092062 : 12:12:27] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[48.092083 : 12:12:27] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[48.092090 : 12:12:27] [core/core.go 619 core.(*Core).readDev] readFrom
[48.092100 : 12:12:27] [wire/v1.go 76 wire.ReadFrom] start
[48.092106 : 12:12:27] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[48.092112 : 12:12:27] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[48.092119 : 12:12:27] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[48.092125 : 12:12:27] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[48.106648 : 12:12:27] [core/core.go 184 core.(*Core).backgroundListen] background enum runs
[48.106688 : 12:12:27] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 1
[48.106701 : 12:12:27] [core/core.go 266 core.(*Core).Enumerate] release disconnected
[48.607824 : 12:12:28] [core/core.go 184 core.(*Core).backgroundListen] background enum runs
[48.609055 : 12:12:28] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 1
[48.609401 : 12:12:28] [core/core.go 266 core.(*Core).Enumerate] release disconnected
[48.725644 : 12:12:28] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[48.725826 : 12:12:28] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[48.725877 : 12:12:28] [wire/v1.go 96 wire.ReadFrom] actual reading started
[48.725918 : 12:12:28] [wire/v1.go 119 wire.ReadFrom] actual reading finished
[48.726050 : 12:12:28] [core/core.go 625 core.(*Core).readDev] encoding back
[48.726111 : 12:12:28] [core/core.go 691 core.(*Core).encodeRaw] start
[48.726195 : 12:12:28] [core/core.go 601 core.(*Core).Call] after actual logic
127.0.0.1 - - [09/Mar/2023:12:12:27 +0300] "POST /call/1 HTTP/1.1" 200 12
[48.726299 : 12:12:28] 127.0.0.1 - - [09/Mar/2023:12:12:27 +0300] "POST /call/1 HTTP/1.1" 200 12
POST /call/1
[48.743038 : 12:12:28] POST /call/1
[48.743122 : 12:12:28] [server/api/api.go 196 server/api.(*api).call] start
[48.743177 : 12:12:28] [core/core.go 568 core.(*Core).Call] checking other call on same session
[48.743198 : 12:12:28] [core/core.go 574 core.(*Core).Call] checking other call on same session done
[48.743212 : 12:12:28] [core/core.go 599 core.(*Core).Call] before actual logic
[48.743225 : 12:12:28] [core/core.go 607 core.(*Core).writeDev] decodeRaw
[48.743236 : 12:12:28] [core/core.go 659 core.(*Core).decodeRaw] readAll
[48.743248 : 12:12:28] [core/core.go 661 core.(*Core).decodeRaw] decodeString
[48.743261 : 12:12:28] [core/core.go 681 core.(*Core).decodeRaw] returning
[48.743270 : 12:12:28] [core/core.go 613 core.(*Core).writeDev] writeTo
[48.743281 : 12:12:28] [wire/v1.go 25 wire.(*Message).WriteTo] start
[48.743291 : 12:12:28] [wire/v1.go 39 wire.(*Message).WriteTo] actually writing
[48.743306 : 12:12:28] [usb/libusb.go 557 usb.(*LibUSBDevice).Write] write start
[48.743322 : 12:12:28] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[48.743332 : 12:12:28] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[48.743346 : 12:12:28] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[48.744115 : 12:12:28] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[48.744144 : 12:12:28] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[48.746974 : 12:12:28] [core/core.go 619 core.(*Core).readDev] readFrom
[48.746994 : 12:12:28] [wire/v1.go 76 wire.ReadFrom] start
[48.747003 : 12:12:28] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[48.747012 : 12:12:28] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[48.747019 : 12:12:28] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[48.747027 : 12:12:28] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[49.110510 : 12:12:28] [core/core.go 184 core.(*Core).backgroundListen] background enum runs
[49.110665 : 12:12:28] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 1
[49.110703 : 12:12:28] [core/core.go 266 core.(*Core).Enumerate] release disconnected
[49.611886 : 12:12:29] [core/core.go 184 core.(*Core).backgroundListen] background enum runs
[49.612300 : 12:12:29] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 1
[49.612415 : 12:12:29] [core/core.go 266 core.(*Core).Enumerate] release disconnected
[49.693906 : 12:12:29] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[49.694158 : 12:12:29] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[49.694272 : 12:12:29] [wire/v1.go 96 wire.ReadFrom] actual reading started
[49.694302 : 12:12:29] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[49.694324 : 12:12:29] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[49.694348 : 12:12:29] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[49.694372 : 12:12:29] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[49.696669 : 12:12:29] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[49.696796 : 12:12:29] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[49.696828 : 12:12:29] [wire/v1.go 119 wire.ReadFrom] actual reading finished
[49.696855 : 12:12:29] [core/core.go 625 core.(*Core).readDev] encoding back
[49.696879 : 12:12:29] [core/core.go 691 core.(*Core).encodeRaw] start
[49.696905 : 12:12:29] [core/core.go 601 core.(*Core).Call] after actual logic
127.0.0.1 - - [09/Mar/2023:12:12:28 +0300] "POST /call/1 HTTP/1.1" 200 206
[49.697083 : 12:12:29] 127.0.0.1 - - [09/Mar/2023:12:12:28 +0300] "POST /call/1 HTTP/1.1" 200 206
POST /call/1
[49.700336 : 12:12:29] POST /call/1
[49.700512 : 12:12:29] [server/api/api.go 196 server/api.(*api).call] start
[49.700574 : 12:12:29] [core/core.go 568 core.(*Core).Call] checking other call on same session
[49.700618 : 12:12:29] [core/core.go 574 core.(*Core).Call] checking other call on same session done
[49.700643 : 12:12:29] [core/core.go 599 core.(*Core).Call] before actual logic
[49.700667 : 12:12:29] [core/core.go 607 core.(*Core).writeDev] decodeRaw
[49.700691 : 12:12:29] [core/core.go 659 core.(*Core).decodeRaw] readAll
[49.700714 : 12:12:29] [core/core.go 661 core.(*Core).decodeRaw] decodeString
[49.700744 : 12:12:29] [core/core.go 681 core.(*Core).decodeRaw] returning
[49.700769 : 12:12:29] [core/core.go 613 core.(*Core).writeDev] writeTo
[49.700793 : 12:12:29] [wire/v1.go 25 wire.(*Message).WriteTo] start
[49.700816 : 12:12:29] [wire/v1.go 39 wire.(*Message).WriteTo] actually writing
[49.700839 : 12:12:29] [usb/libusb.go 557 usb.(*LibUSBDevice).Write] write start
[49.700859 : 12:12:29] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[49.700879 : 12:12:29] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[49.700902 : 12:12:29] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[49.702124 : 12:12:29] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[49.702173 : 12:12:29] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[49.702284 : 12:12:29] [core/core.go 619 core.(*Core).readDev] readFrom
[49.702331 : 12:12:29] [wire/v1.go 76 wire.ReadFrom] start
[49.702356 : 12:12:29] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[49.702444 : 12:12:29] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[49.702465 : 12:12:29] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[49.702740 : 12:12:29] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[50.113602 : 12:12:29] [core/core.go 184 core.(*Core).backgroundListen] background enum runs
[50.113958 : 12:12:29] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 1
[50.114009 : 12:12:29] [core/core.go 266 core.(*Core).Enumerate] release disconnected
[50.324469 : 12:12:29] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[50.324737 : 12:12:29] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[50.324776 : 12:12:29] [wire/v1.go 96 wire.ReadFrom] actual reading started
[50.324806 : 12:12:29] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[50.324833 : 12:12:29] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[50.324969 : 12:12:29] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[50.325013 : 12:12:29] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[50.326027 : 12:12:29] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[50.326060 : 12:12:29] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[50.326085 : 12:12:29] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[50.326108 : 12:12:29] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[50.326132 : 12:12:29] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[50.326170 : 12:12:29] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[50.327056 : 12:12:29] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[50.327095 : 12:12:29] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[50.327120 : 12:12:29] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[50.327144 : 12:12:29] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[50.327165 : 12:12:29] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[50.327190 : 12:12:29] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[50.328041 : 12:12:29] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[50.328089 : 12:12:29] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[50.328116 : 12:12:29] [wire/v1.go 119 wire.ReadFrom] actual reading finished
[50.328143 : 12:12:29] [core/core.go 625 core.(*Core).readDev] encoding back
[50.328272 : 12:12:29] [core/core.go 691 core.(*Core).encodeRaw] start
[50.328305 : 12:12:29] [core/core.go 601 core.(*Core).Call] after actual logic
127.0.0.1 - - [09/Mar/2023:12:12:29 +0300] "POST /call/1 HTTP/1.1" 200 482
[50.328410 : 12:12:29] 127.0.0.1 - - [09/Mar/2023:12:12:29 +0300] "POST /call/1 HTTP/1.1" 200 482
POST /call/1
[50.329260 : 12:12:29] POST /call/1
[50.329396 : 12:12:29] [server/api/api.go 196 server/api.(*api).call] start
[50.329511 : 12:12:29] [core/core.go 568 core.(*Core).Call] checking other call on same session
[50.329545 : 12:12:29] [core/core.go 574 core.(*Core).Call] checking other call on same session done
[50.329582 : 12:12:29] [core/core.go 599 core.(*Core).Call] before actual logic
[50.329606 : 12:12:29] [core/core.go 607 core.(*Core).writeDev] decodeRaw
[50.329629 : 12:12:29] [core/core.go 659 core.(*Core).decodeRaw] readAll
[50.329666 : 12:12:29] [core/core.go 661 core.(*Core).decodeRaw] decodeString
[50.329691 : 12:12:29] [core/core.go 681 core.(*Core).decodeRaw] returning
[50.329714 : 12:12:29] [core/core.go 613 core.(*Core).writeDev] writeTo
[50.329737 : 12:12:29] [wire/v1.go 25 wire.(*Message).WriteTo] start
[50.329759 : 12:12:29] [wire/v1.go 39 wire.(*Message).WriteTo] actually writing
[50.329783 : 12:12:29] [usb/libusb.go 557 usb.(*LibUSBDevice).Write] write start
[50.329804 : 12:12:29] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[50.329826 : 12:12:29] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[50.329847 : 12:12:29] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[50.331069 : 12:12:29] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[50.331143 : 12:12:29] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[50.331167 : 12:12:29] [core/core.go 619 core.(*Core).readDev] readFrom
[50.331188 : 12:12:29] [wire/v1.go 76 wire.ReadFrom] start
[50.331210 : 12:12:29] [usb/libusb.go 571 usb.(*LibUSBDevice).Read] read start
[50.331229 : 12:12:29] [usb/libusb.go 507 usb.(*LibUSBDevice).readWrite] start
[50.331460 : 12:12:29] [usb/libusb.go 509 usb.(*LibUSBDevice).readWrite] checking closed
[50.331533 : 12:12:29] [usb/libusb.go 517 usb.(*LibUSBDevice).readWrite] actual interrupt transport
[50.615116 : 12:12:30] [core/core.go 184 core.(*Core).backgroundListen] background enum runs
[50.615406 : 12:12:30] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 1
[50.615445 : 12:12:30] [core/core.go 266 core.(*Core).Enumerate] release disconnected
[50.953596 : 12:12:30] [usb/libusb.go 521 usb.(*LibUSBDevice).readWrite] single transfer done
[50.953862 : 12:12:30] [usb/libusb.go 537 usb.(*LibUSBDevice).readWrite] single transfer successful
[50.953900 : 12:12:30] [wire/v1.go 96 wire.ReadFrom] actual reading started
[50.953930 : 12:12:30] [wire/v1.go 119 wire.ReadFrom] actual reading finished
[50.954041 : 12:12:30] [core/core.go 625 core.(*Core).readDev] encoding back
[50.954070 : 12:12:30] [core/core.go 691 core.(*Core).encodeRaw] start
[50.954096 : 12:12:30] [core/core.go 601 core.(*Core).Call] after actual logic
127.0.0.1 - - [09/Mar/2023:12:12:29 +0300] "POST /call/1 HTTP/1.1" 200 12
[50.954304 : 12:12:30] 127.0.0.1 - - [09/Mar/2023:12:12:29 +0300] "POST /call/1 HTTP/1.1" 200 12
[51.116992 : 12:12:30] [core/core.go 184 core.(*Core).backgroundListen] background enum runs
[51.117126 : 12:12:30] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 0
[51.117171 : 12:12:30] [core/core.go 256 core.(*Core).Enumerate] bus
[51.117212 : 12:12:30] [usb/libusb.go 122 usb.(*LibUSB).Enumerate] low level enumerating
[51.117323 : 12:12:30] [usb/libusb.go 128 usb.(*LibUSB).Enumerate] low level enumerating done
[51.117366 : 12:12:30] [usb/libusb.go 347 usb.(*LibUSB).match] start
[51.117406 : 12:12:30] [usb/libusb.go 361 usb.(*LibUSB).match] matched, get active config
[51.117462 : 12:12:30] [usb/libusb.go 369 usb.(*LibUSB).match] let's test
[51.118840 : 12:12:30] [usb/libusb.go 391 usb.(*LibUSB).match] matched
[51.118909 : 12:12:30] [usb/libusb.go 148 usb.(*LibUSB).Enumerate] getting device descriptor
[51.118972 : 12:12:30] [usb/libusb.go 347 usb.(*LibUSB).match] start
[51.119014 : 12:12:30] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[51.119050 : 12:12:30] [usb/libusb.go 347 usb.(*LibUSB).match] start
[51.119102 : 12:12:30] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[51.119141 : 12:12:30] [usb/libusb.go 347 usb.(*LibUSB).match] start
[51.119233 : 12:12:30] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[51.119279 : 12:12:30] [usb/libusb.go 131 usb.(*LibUSB).Enumerate.func1] freeing device list
[51.119318 : 12:12:30] [usb/libusb.go 133 usb.(*LibUSB).Enumerate.func1] freeing device list done
[51.119368 : 12:12:30] [usb/hidapi.go 42 usb.(*HIDAPI).Enumerate] low level
[51.129549 : 12:12:30] [usb/hidapi.go 45 usb.(*HIDAPI).Enumerate] low level done
[51.129625 : 12:12:30] [core/core.go 266 core.(*Core).Enumerate] release disconnected
[51.630540 : 12:12:31] [core/core.go 184 core.(*Core).backgroundListen] background enum runs
[51.630973 : 12:12:31] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 0
[51.631039 : 12:12:31] [core/core.go 256 core.(*Core).Enumerate] bus
[51.631227 : 12:12:31] [usb/libusb.go 122 usb.(*LibUSB).Enumerate] low level enumerating
[51.631411 : 12:12:31] [usb/libusb.go 128 usb.(*LibUSB).Enumerate] low level enumerating done
[51.631444 : 12:12:31] [usb/libusb.go 347 usb.(*LibUSB).match] start
[51.631472 : 12:12:31] [usb/libusb.go 361 usb.(*LibUSB).match] matched, get active config
[51.631533 : 12:12:31] [usb/libusb.go 369 usb.(*LibUSB).match] let's test
[51.631555 : 12:12:31] [usb/libusb.go 391 usb.(*LibUSB).match] matched
[51.631584 : 12:12:31] [usb/libusb.go 148 usb.(*LibUSB).Enumerate] getting device descriptor
[51.631659 : 12:12:31] [usb/libusb.go 347 usb.(*LibUSB).match] start
[51.631684 : 12:12:31] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[51.631707 : 12:12:31] [usb/libusb.go 347 usb.(*LibUSB).match] start
[51.631818 : 12:12:31] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[51.631839 : 12:12:31] [usb/libusb.go 347 usb.(*LibUSB).match] start
[51.631859 : 12:12:31] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[51.632603 : 12:12:31] [usb/libusb.go 131 usb.(*LibUSB).Enumerate.func1] freeing device list
[51.632663 : 12:12:31] [usb/libusb.go 133 usb.(*LibUSB).Enumerate.func1] freeing device list done
[51.632694 : 12:12:31] [usb/hidapi.go 42 usb.(*HIDAPI).Enumerate] low level
[51.641361 : 12:12:31] [usb/hidapi.go 45 usb.(*HIDAPI).Enumerate] low level done
[51.641639 : 12:12:31] [core/core.go 266 core.(*Core).Enumerate] release disconnected
[52.142834 : 12:12:31] [core/core.go 184 core.(*Core).backgroundListen] background enum runs
[52.143208 : 12:12:31] [core/core.go 254 core.(*Core).Enumerate] callsInProgress 0
[52.143265 : 12:12:31] [core/core.go 256 core.(*Core).Enumerate] bus
[52.143324 : 12:12:31] [usb/libusb.go 122 usb.(*LibUSB).Enumerate] low level enumerating
[52.144221 : 12:12:31] [usb/libusb.go 128 usb.(*LibUSB).Enumerate] low level enumerating done
[52.144355 : 12:12:31] [usb/libusb.go 347 usb.(*LibUSB).match] start
[52.144414 : 12:12:31] [usb/libusb.go 361 usb.(*LibUSB).match] matched, get active config
[52.144487 : 12:12:31] [usb/libusb.go 369 usb.(*LibUSB).match] let's test
[52.144530 : 12:12:31] [usb/libusb.go 391 usb.(*LibUSB).match] matched
[52.144574 : 12:12:31] [usb/libusb.go 148 usb.(*LibUSB).Enumerate] getting device descriptor
[52.144638 : 12:12:31] [usb/libusb.go 347 usb.(*LibUSB).match] start
[52.144683 : 12:12:31] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[52.144720 : 12:12:31] [usb/libusb.go 347 usb.(*LibUSB).match] start
[52.144760 : 12:12:31] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[52.144799 : 12:12:31] [usb/libusb.go 347 usb.(*LibUSB).match] start
[52.144838 : 12:12:31] [usb/libusb.go 357 usb.(*LibUSB).match] unmatched
[52.145645 : 12:12:31] [usb/libusb.go 131 usb.(*LibUSB).Enumerate.func1] freeing device list
[52.145774 : 12:12:31] [usb/libusb.go 133 usb.(*LibUSB).Enumerate.func1] freeing device list done
[52.146404 : 12:12:31] [usb/hidapi.go 42 usb.(*HIDAPI).Enumerate] low level
[52.160761 : 12:12:31] [usb/hidapi.go 45 usb.(*HIDAPI).Enumerate] low level done
[52.160962 : 12:12:31] [core/core.go 266 core.(*Core).Enumerate] release disconnected
```

and so on.

Next I type passphrase on the computer. I immediately get "Couldn't open wallet: Cannot get a device address". Daemon does not show anything new, only those "background enum runs" and further message run all the time in a cycle. It is like GUI never sent anything to Trezor.

> Are you sure that it is numbers being entered in GUI?For example the Czech keyboard

I use US English keyboard. I am prety sure that when I press 1234, it sends 1234 :) 

## dmitryd | 2023-03-09T09:29:01+00:00
@ph4r05 

Running GUI from terminal, part after I entered wallet password:

> 2023-03-09 09:22:43.240	W Account on device. Initing device...
> 2023-03-09 09:22:45.010	W Wallet opening with an empty passphrase failed. Retry again: 1

After I enter passphrase on the computer:

>2023-03-09 09:24:02.209	E Get public address exception: Call method failed
> 2023-03-09 09:24:02.210	E !hwdev.get_public_address(device_account_public_address). THROW EXCEPTION: error::wallet_internal_error
> 2023-03-09 09:24:02.212	E Error opening wallet: Cannot get a device address
> 2023-03-09 09:24:02.214	E Error opening wallet with password:  Cannot get a device address

When trying on the device:

> 2023-03-09 09:26:12.059	W Account on device. Initing device...
> 2023-03-09 09:26:13.907	W Wallet opening with an empty passphrase failed. Retry again: 1
> 2023-03-09 09:27:00.424	W Device inited...
> 2023-03-09 09:27:00.484	W Loaded wallet keys file, with public address: 44****
> 2023-03-09 09:27:02.098	W Display non non-main thread! Deferring to main thread
> 2023-03-09 09:27:14.144	I Monero 'Fluorine Fermi' (v0.18.2.0-release)
> Forking to background...

## dmitryd | 2023-03-09T09:33:04+00:00
Using `TREZOR_PATH=bridge:1` does not change anything.

## ph4r05 | 2023-03-09T10:31:42+00:00
Thanks for more info @dmitryd! There seems to be a communication problem with the Trezor.

Things to try:
- delete old trezord, download the latest trezor bridge, reinstall. (Delete before install to ensure the new one is used)
- another USB cable
- `TREZOR_PATH=webusb:002:1 monego-wallet-gui` to ensure that webusb/libusb is used, do not use bridge in this attempt (kill it ideally). Pls send us logs from this attempt to avoid using bridge. 

---------- 
Regarding the logs, the following line is important

```
2023-03-09 09:24:02.209 E Get public address exception: Call method failed
```

It is emitted from here https://github.com/monero-project/monero/blob/da9aa1f7f802552b9de459f331a2f39c84898009/src/device_trezor/trezor/transport.cpp#L466 , i.e., communication with the bridge returned error. 

Btw isn't there another error above this line? Something like the following, it would help.
```
Failed to invoke http request to ...
Failed to invoke http request to ... internal error (null response ptr)
Failed to invoke http request to ... , wrong response code: ...
```

This should not happen under normal circumstances. Errors are communicated normally, e.g., if device was not initialized

```
2023-03-09 10:20:41.047	E Get public address exception: Device is not initialized
```

or if passphrase differs

```
2023-03-09 10:23:16.612	E device_account_public_address != m_account.get_keys().m_account_address. THROW EXCEPTION: error::wallet_internal_error
2023-03-09 10:23:16.612	W monero-gui/monero/src/wallet/wallet2.cpp:4520:N5tools5error21wallet_internal_errorE: Device wallet does not match wallet address. If the device uses the passphrase feature, please check whether the passphrase was entered correctly (it may have been misspelled - different passphrases generate different wallets, passphrase is case-sensitive)
```


## dmitryd | 2023-03-09T11:02:00+00:00
@ph4r05 I do not have a separate trezor bridge, I use the one from the Trezor suite. Is this a problem?

Binary is in `/Applications/Trezor Suite.app/Contents/Resources/bin/bridge/trezord` 

```
 $ trezord --version
trezord version 2.0.32 (rev 9aa6576)
```

---

> another USB cable

This is Apple USB-C cable. It works with everything. It works also with Trezor suite. I do not have another one.

> TREZOR_PATH=webusb:002:1 monego-wallet-gui to ensure that webusb/libusb is used, do not use bridge in this attempt (kill it ideally). Pls send us logs from this attempt to avoid using bridge.

Connections:

```
$ trezorctl list
webusb:002:1 - C1 [Trezor T, D*]
```

So no bridge right now.

GUI cannot connect at all:

```
$ MONERO_LOG_LEVEL=4 TREZOR_PATH=webusb:002:1 /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
2023-03-09 10:43:33.242	W Qt:5.12.8 GUI:- | screen: 1728x1117 - available: QSize(1679, 1079) - dpi: 72 - ratio:0.996094
2023-03-09 10:43:34.031	D fiatPriceError: Invalid ticker value: 0
2023-03-09 10:43:34.087	D Invalid address format
2023-03-09 10:43:34.092	D >>> wallet updated
2023-03-09 10:43:34.117	D fiatPriceError: Invalid ticker value: 0
2023-03-09 10:43:34.117	D fiatPriceError: Invalid ticker value: 0
2023-03-09 10:43:34.444	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.444	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.444	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.467	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.467	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.467	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.467	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.468	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.468	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.468	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.468	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.468	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.468	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.479	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.479	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.479	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.501	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.830	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.830	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.830	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.841	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.841	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.841	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.886	D transfer page loaded
2023-03-09 10:43:34.968	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.968	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.968	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"
2023-03-09 10:43:34.985	D fiatPriceError: Invalid ticker value: 0
2023-03-09 10:43:34.985	D fiatPriceError: Invalid ticker value: 0
2023-03-09 10:43:35.028	D SettingsWallet loaded
2023-03-09 10:43:35.030	D SettingsLayout loaded
2023-03-09 10:43:35.084	D setLanguage   "en"
2023-03-09 10:43:35.089	D fiatPriceError: Invalid ticker value: 0
2023-03-09 10:43:35.090	D walletMode: Advanced
2023-03-09 10:43:35.090	D qrScannerEnabled disabled
2023-03-09 10:43:35.093	W Logging to "/Users/dmitry/Library/Logs/monero-wallet-gui.log"
2023-03-09 10:43:35.094	W file:///Applications/monero-wallet-gui.app/Contents/Resources/qml/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2023-03-09 10:43:35.137	W Display non non-main thread! Deferring to main thread
2023-03-09 10:43:49.361	W Account on device. Initing device...
2023-03-09 10:43:49.366	E BridgeTransport enumeration failed:Bridge enumeration failed
2023-03-09 10:43:49.366	E No matching Trezor device found. Device specifier: ""
2023-03-09 10:43:49.367	E !hwdev.connect(). THROW EXCEPTION: error::wallet_internal_error
2023-03-09 10:43:49.368	E Error opening wallet: Could not connect to the device Trezor
2023-03-09 10:43:49.392	E Error opening wallet with password:  Could not connect to the device Trezor
```


## selsta | 2023-03-09T11:04:20+00:00
> I do not have a separate trezor bridge, I use the one from the Trezor suite. Is this a problem?

Can you try manually installing the bridge from https://suite.trezor.io/web/bridge ? Or maybe wait for @ph4r05 to give instructions but as far as I know on macOS it is necessary to manually install the bridge.

## dmitryd | 2023-03-09T11:10:00+00:00
Yeah, I just did and it worked! Current downloadable standalone bridge version for macOS is 2.0.27 and it works with Monero GUI. The version that ships with Trezor suit is 2.0.32 (newer) and it does not work with GUI.

So the problem could be with a newer bridge version.

## ph4r05 | 2023-03-09T11:21:11+00:00
EDIT: ah I noticed this too late.

btw aren't you using something like LittleSnitch or other restrictive firewall that could interfere with Trezord communication? 

Trezor bridge acts as everything is fine (200) code

```
127.0.0.1 - - [09/Mar/2023:12:12:29 +0300] "POST /call/1 HTTP/1.1" 200 12
```

This is called by monero wallet https://github.com/monero-project/monero/blob/da9aa1f7f802552b9de459f331a2f39c84898009/src/device_trezor/trezor/transport.cpp#L460-L464

but as you indicated, it fails later after passphrase entry.


## ph4r05 | 2023-03-09T11:22:58+00:00
> Yeah, I just did and it worked! Current downloadable standalone bridge version for macOS is 2.0.27 and it works with Monero GUI. The version that ships with Trezor suit is 2.0.32 (newer) and it does not work with GUI.
> 
> So the problem could be with a newer bridge version.

@prusnak this is interesting, was trezor bridge comm protocol changed somehow recently?

## dmitryd | 2023-03-09T11:23:10+00:00
> btw aren't you using something like LittleSnitch or other restrictive firewall that could interfere with Trezord communication?

Firsts, it is deactivated for testing, secondly it does not restrict connections to 127.0.0.1 :) 

## ph4r05 | 2023-03-09T11:25:15+00:00
also, pls @selsta can we pls check if monero-gui binaries have libusb linked correctly, as @dmitryd indicated? monero-gui cannot connect to the Trezor directly and bridge is needed. This is suboptimal, libusb should be used in the first place.

## selsta | 2023-03-09T11:33:27+00:00
@ph4r05 can you show me where we link against libusb in CMake? monero-wallet-gui.app has a protobuf and hidapi dylib, but I don't see anything about libusb.

## prusnak | 2023-03-09T11:36:56+00:00
> @prusnak this is interesting, was trezor bridge comm protocol changed somehow recently?

@ph4r05 I am not aware of any changes. The bridge should not interfere with the protocol anyway, it's just passes the messages, it does not understand them. 

## prusnak | 2023-03-09T11:37:59+00:00
> Yeah, I just did and it worked! Current downloadable standalone bridge version for macOS is 2.0.27 and it works with Monero GUI. The version that ships with Trezor suit is 2.0.32 (newer) and it does not work with GUI.

@dmitryd do you run bridge 2.0.32 manually (suite does not run) or do you let suite start it for you (suite runs)?

## dmitryd | 2023-03-09T11:56:50+00:00
@prusnak 

> do you run bridge 2.0.32 manually (suite does not run) or do you let suite start it for you (suite runs)?

I ran the bridge manually as ` '/Applications/Trezor Suite.app/Contents/Resources/bin/bridge/trezord'`. It seems that device can be used only by one app at a time:
- If I ran Trezor Suit, Monero GUI cannot connect to the bridge anymore. It is like Suit locks the device to itself.
- If I run Monero GUI, then Trezor Suite cannot connect to Trezor, the message is that it is used by another application.

![iScreen Shoter - Trezor Suite - 230309145447](https://user-images.githubusercontent.com/306133/224015890-0cbbf7cf-fecd-4b74-9e11-82594e939152.jpg)

Same behavior with a standalone bridge version.


## prusnak | 2023-03-09T12:25:48+00:00
@dmitryd Thanks for confirmation. That's the correct behaviour.

But anyway, when you run the 2.0.32 bridge manually, it should work.

So it seems we have two issues:
- it seems that recent monero-cli/monero-gui versions do not link against libusb (trezor does not use hidapi)
- bridge 2.0.32 does not work with monero-cli/monero-gui

## dmitryd | 2023-03-09T12:27:55+00:00
@prusnak If you want me to test anything else (more logging, etc), just post it here. I will.

## ph4r05 | 2023-03-09T12:46:49+00:00
This was quite a helpful session, thanks! I will take a look on both cases and let you know. 

## ph4r05 | 2023-03-10T11:24:22+00:00
Unfortunately, I cannot replicate this, bridge `trezord v2.0.32 (rev 9aa6576) is starting` works for me, all selected tests passed. @prusnak any ideas why it makes a difference for @dmitryd?

Things worth trying:
- reinstalling both bridges
- checking if OSX USB permission was rejected for the bridge that is not working properly: In the System Preferences Security & Privacy -> Privacy -> USB. This could block not working bridge access to the Trezor.
- diffing logs from both bridge versions
 
@selsta LibUSB fix is in https://github.com/monero-project/monero/pull/8752

## dmitryd | 2023-03-10T11:31:05+00:00
@ph4r05 No "USB" in Security>Privacy here.

## ph4r05 | 2023-03-10T11:50:44+00:00
thaks for feedback! I was just phishing possible causes, this came to mind, I think there is a [change since Ventura](https://9to5mac.com/2022/06/06/macos-ventura-usb-security/).

It may help downloading Trezor Suite again, opening in a different location than Applications (not sure how OSX permissions tie permission to the executable, hash / path), starting from command line (kill -9 all running bridges before). 

## dmitryd | 2023-03-10T11:52:39+00:00
I am still on Monterey because some of my other software does not play well with Ventura. Could it be important?

## ph4r05 | 2023-03-10T11:55:36+00:00
> I am still on Monterey because some of my other software does not play well with Ventura. Could it be important?

I am not sure, but I think not.

## arbolis | 2023-03-12T11:30:04+00:00
I also face the same problem (I'm on Arch Linux). After starting the Trezor T and its suite, running Monero GUI and entering the passphrase in there shows the message that it isn't able to find the Trezor T. I have the latest versions of all firmwares + softwares, as far as I know. Will there be a fix in the next versions?

## dmitryd | 2023-03-12T11:32:13+00:00
@arbolis This is different: only one application can use Trezor at a time it seems. If you start first Monero GUI and then the Suit, it will tell you that the wallet is in use by another application.

## arbolis | 2023-03-12T14:03:28+00:00
@dmitryd Hmm not really. As I said, I didn't get the message that the wallet is used by another application.

What happened is that (after I unlocked my Trezor T by entering the PIN) I ran Monero GUI, entered the passphrase in Monero GUI and got the error that it wasn't finding the Trezor T. I thought "Uh, ok, maybe I should have started Trezor Suite". And so I redid everything except that I started the Trezor T suite before Monero GUI. Same error in any case. Unable to find the Trezor T, that's the message from Monero GUI.

## ph4r05 | 2023-03-13T12:00:15+00:00
@arbolis Trezor Suite cannot be running when you want to use Monero wallet. 

If Monero GUI is not able to find your Trezor, install [Trezor Bridge](https://suite.trezor.io/web/bridge/) 



## thestinger | 2023-03-15T04:35:07+00:00
Using the official Trezor Bridge release doesn't resolve the issue for me, and neither does using a self-built trezord. I also tried building a couple older versions of trezord and nothing helped.

## ph4r05 | 2023-03-15T08:59:59+00:00
@thestinger can you pls provide logs? https://github.com/monero-project/monero-gui/issues/4105#issuecomment-1460959116 

```
MONERO_LOG_LEVEL=4 /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
```

and also 
```
trezorctl list
```

As a last resort you can try building this PR which has libusb compilation fixed https://github.com/monero-project/monero/pull/8752

## thestinger | 2023-03-15T09:11:47+00:00
With or without running Trezor Bridge (trezord) separately?

## ph4r05 | 2023-03-15T09:40:22+00:00
@thestinger pls keep running trezord and try `trezorctl list`

## thestinger | 2023-03-15T09:55:32+00:00
`trezorctl list` shows `webusb:004:2` and `bridge:1` with `trezord` 2.0.32. Trying to use `TREZOR_PATH=bridge:1 monero-wallet-gui` or `TREZOR_PATH=webusb:004:2 monero-wallet-gui` doesn't change anything. Can confirm `trezord` / `trezorctl` does work fine separately from the Monero wallet software.

## prusnak | 2023-03-15T09:58:31+00:00
@thestinger
1. Can you also try `TREZOR_PATH=bridge:1 monero-wallet-gui` with trezord 2.0.27 (from http://suite.trezor.io/web/bridge/)?
2. Can you also try `TREZOR_PATH=webusb:xxx monero-wallet-gui` with the patch from https://github.com/monero-project/monero/pull/8752?

## thestinger | 2023-03-15T10:00:56+00:00
Same thing with trezord 2.0.27 and `TREZOR_PATH=bridge:1`. Also, not getting any useful logs from monero-wallet-gui just the same:

```
2023-03-15 09:59:57.227	W Account on device. Initing device...
2023-03-15 09:59:57.228	E Error opening wallet: device not found: Trezor
2023-03-15 09:59:57.263	E Error opening wallet with password:  device not found: Trezor
```

I can try building it later with the patch.

## selsta | 2023-03-15T10:13:29+00:00
@thestinger how did you install monero-wallet-gui ? The logs look like you compiled without Trezor support.

## arbolis | 2023-03-16T18:18:24+00:00
> @arbolis Trezor Suite cannot be running when you want to use Monero wallet.
> 
> If Monero GUI is not able to find your Trezor, install [Trezor Bridge](https://suite.trezor.io/web/bridge/)

I never had to install Trezor Bridge before, and I never faced any problem before. Anyway, for the sake of it, I installed the latest version of Trezor Bridge (2.0.30). I can confirm it works from my browser (checking its status). I then ran Monero GUI, entered my passphrase, and.... exactly the same message as above. Cannot find the Trezor (while it is unlocked).

## thestinger | 2023-03-16T19:57:19+00:00
@selsta Tried both the official release and the Arch Linux package. Both have Trezor support.

## selsta | 2023-03-16T20:01:03+00:00
@thestinger "device not found: Trezor" means it's compiled without Trezor support. Can you post the exact error message you are getting with the getmonero.org binary?

## ph4r05 | 2023-03-16T21:57:38+00:00
> Same thing with trezord 2.0.27 and `TREZOR_PATH=bridge:1`. Also, not getting any useful logs from monero-wallet-gui just the same:
> 
> ```
> 2023-03-15 09:59:57.227	W Account on device. Initing device...
> 2023-03-15 09:59:57.228	E Error opening wallet: device not found: Trezor
> 2023-03-15 09:59:57.263	E Error opening wallet with password:  device not found: Trezor
> ```

It is better to enable full debugging (either `MONERO_LOG_LEVEL=4` or `--log-level
4`), correct build is able to detect both Webusb and Bridge interfaces (consistent with `pip install trezor; trezorctl list`):


```
2023-03-16 21:52:14.516	     0x1e2558140	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:125	Enumeration yielded 2 Trezor devices
2023-03-16 21:52:14.517	     0x1e2558140	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:127	  device: WebUsbTransport<path=webusb:001:1, vendorId=4617, productId=21441, deviceType=TrezorT>
2023-03-16 21:52:14.517	     0x1e2558140	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:127	  device: BridgeTransport<path=bridge:4, info={"path":"4","vendor":4617,"product":21441,"debug":true,"session":null,"debugSession":null}, session=None>
```

Also, Webusb is preferred approach as Trezor bridge may be left in inconsistent state and may require reset (pkill -9 trezord) + device reconnect.

> I can try building it later with the patch.

Did you pls try this? Thanks!

## arbolis | 2023-03-31T16:48:51+00:00
I just tested to download Monero GUI from the website itself rather than using the Arch Linux repository. That was it. Now everything works fine. It means whoever compiled Monero GUI for Arch Linux stopped to do it with Trezor support.

## kpcyrd | 2023-04-03T13:56:26+00:00
hi, I'm the maintainer of the `monero` and `monero-gui` Arch Linux packages. There's nothing explicitly disabling hardware wallets so it seems the binary sometimes just doesn't have support, there's an earlier [bug report from 2021](https://bugs.archlinux.org/task/69738) and I've [tried to acquire a hardware wallet to test with](https://twitter.com/sn0int/status/1437753834772774919) but failed.

The package is currently built like this:
```sh
mkdir -p build && cd build
cmake -D CMAKE_BUILD_TYPE=Release -D ARCH=default -D WITH_DESKTOP_ENTRY=OFF -D WITH_UPDATER=OFF ../
make
```

In the [Arch Linux bug report](https://bugs.archlinux.org/task/78085) somebody noticed [the buildlog](https://web.archive.org/web/20230403124642/https://reproducible.archlinux.org/api/v0/builds/410869/log) contains this line:

```
-- Trezor support disabled
```

I've searched the code base for this string and there's no matches in the monero-gui repo, but the monero repo mentions it (disclaimer that I'm not good at reading cmake):

**src/device_trezor/CMakeLists.txt**
```cmake
# Protobuf and LibUSB processed by CheckTrezor
if(DEVICE_TREZOR_READY)
    message(STATUS "Trezor support enabled")

    [...]

else()
    message(STATUS "Trezor support disabled")
    monero_private_headers(device_trezor)
    monero_add_library(device_trezor device_trezor.cpp)
    target_link_libraries(device_trezor PUBLIC cncrypto)
endif()
```

I've then searched for `DEVICE_TREZOR_READY` and found this:

**cmake/CheckTrezor.cmake**
```cmake
# Try to build protobuf messages
if(Protobuf_FOUND AND USE_DEVICE_TREZOR AND TREZOR_PYTHON AND Protobuf_COMPILE_TEST_PASSED)
    [...]

    execute_process(COMMAND ${TREZOR_PYTHON} tools/build_protob.py ${TREZOR_PROTOBUF_PARAMS} WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/../src/device_trezor/trezor RESULT_VARIABLE RET OUTPUT_VARIABLE OUT ERROR_VARIABLE ERR)
    if(RET)
        message(WARNING "Trezor protobuf messages could not be regenerated (err=${RET}, python ${PYTHON})."
                "OUT: ${OUT}, ERR: ${ERR}."
                "Please read src/device_trezor/trezor/tools/README.md")
    else()
        message(STATUS "Trezor protobuf messages regenerated out: \"${OUT}.\"")
        set(DEVICE_TREZOR_READY 1)
        add_definitions(-DDEVICE_TREZOR_READY=1)
        add_definitions(-DPROTOBUF_INLINE_NOT_IN_HEADERS=0)

        [...]

        if(CMAKE_BUILD_TYPE STREQUAL "Debug")
            add_definitions(-DTREZOR_DEBUG=1)
        endif()
```

It seems either any of `Protobuf_FOUND`, `USE_DEVICE_TREZOR`, `TREZOR_PYTHON`, `Protobuf_COMPILE_TEST_PASSED` are false-y or `python tools/build_protob.py [...]` has failed, which would also build a binary without hardware wallet support instead of error-ing the build as I would want it to (to let me know I need to fix something).

I also recalled this other line in the build log:

```
-- Could NOT find PythonInterp (missing: PYTHON_EXECUTABLE) 
```

I assume `TREZOR_PYTHON` is either an empty string or null, I recall python was at some point removed from the default Arch Linux build environment, so I added `python` as an explicit `makedepends=`, which now prints these lines during build:

```
-- Found PythonInterp: /usr/bin/python (found version "3.10.10") 
[...]
-- Trezor support enabled
```

I've uploaded this as `monero-gui-0.18.2.0-2-x86_64.pkg.tar.zst`, I have no hardware to test this with but I hope this helps. If there's a more reliable way to build the binary with enabled hardware wallet support please let me know.

## ph4r05 | 2023-04-04T06:25:32+00:00
@kpcyrd thanks for your investigation, I may change cmake so if fails if trezor compilation is not disabled and it fails for some reason.

## thestinger | 2023-04-04T07:02:26+00:00
@kpcyrd The new Arch package works for me. Thanks! Still get the error from earlier with the official release:

https://github.com/monero-project/monero-gui/issues/4105#issuecomment-1435259250

Not able to invest more time in this. Very happy to have it working though.

## kpcyrd | 2023-04-04T13:50:10+00:00
@ph4r05 that would be great!

## ph4r05 | 2023-04-05T19:55:50+00:00
So if `USE_DEVICE_TREZOR` is enabled and Trezor support cannot be built for some reason, build fails with descriptive error message. PR: https://github.com/monero-project/monero/pull/8752

## ghost | 2023-05-29T16:55:54+00:00
I had this issue today, when I typed in my phrase on the device itself it actually worked.

## ghost | 2023-05-29T21:06:09+00:00
I was able to solve this issue by closing trezor suite, which was running at the same time as gui.

## dement6d | 2024-04-17T06:53:14+00:00
having this same issue on Archcraft x86_64 (6.8.2-arch2-1), tried a full system upgrade, tried using `monero-wallet-cli` and `monero-wallet-gui`, both unable to connect to my trezor. i dont have trezor suite open but trezor suite works fine. i tried with the built in trezord and i also built trezord-go, neither get any calls from the monero wallet but they do get calls from the trezor web app or when i just make a post call to it myself, so trezord is working. my trezor firmware is up to date and so are both `monero` and `monero-gui`
here is my `.bitmonero/monero-wallet-gui.log`:
```
2024-04-17 06:19:43.645	   7a05db237000	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-04-17 06:19:43.645	   7a05db237000	WARNING	frontend	src/wallet/api/wallet.cpp:411	Logging to "/home/demented/.bitmonero/monero-wallet-gui.log"
2024-04-17 06:19:43.647	   7a05db237000	WARNING	frontend	src/wallet/api/wallet.cpp:411	file:///usr/lib/qt/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2024-04-17 06:23:23.824	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2024-04-17 06:23:23.824	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	   [1] monero-wallet-gui(+0x9287c) [0x59dfb87eb87c] 
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	   [2] monero-wallet-gui(+0x1eca84) [0x59dfb8945a84] 
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	   [3] monero-wallet-gui(+0x16fa97) [0x59dfb88c8a97] 
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	   [4] monero-wallet-gui(+0x16fdc0) [0x59dfb88c8dc0] 
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	   [5] monero-wallet-gui(+0x180766) [0x59dfb88d9766] 
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	   [6] /usr/lib/libQt5Core.so.5(+0xf0631) [0x7a05df4f0631] 
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	   [7] /usr/lib/libQt5Core.so.5(+0xeb88a) [0x7a05df4eb88a] 
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	   [8] /usr/lib/libc.so.6(+0x8b55a) [0x7a05de6a955a] 
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	   [9] /usr/lib/libc.so.6(+0x108a3c) [0x7a05de726a3c] 
2024-04-17 06:23:23.825	   7a05d8c006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	
```
i ended up having to use a feather wallet appimage, as exodus is currently having issues syncing XMR. ill note, i also had to type in my jumbled password from the trezor device itself for it to work. unfortunately though after synchronizing and loading my balance properly, im unable to make a transaction from feather wallet due to "Failed to construct transaction Device state not initialized"

## kpcyrd | 2024-04-17T15:36:41+00:00
I've never heard of Archcraft and I'm not interested in troubleshooting downstreams, if there are still issues with the package patches can be sent here:

https://gitlab.archlinux.org/archlinux/packaging/packages/monero-gui

## dement6d | 2024-04-20T06:44:57+00:00
> i ended up having to use a feather wallet appimage, as exodus is currently having issues syncing XMR. ill note, i also had to type in my jumbled password from the trezor device itself for it to work. unfortunately though after synchronizing and loading my balance properly, im unable to make a transaction from feather wallet due to "Failed to construct transaction Device state not initialized"

an update on this, i managed to get into my feather wallet by typing the password normally through the feather prompt and make transactions successfully just by not having trezord or trezor suite run in the background
unfortunately still not able to get monero-gui-wallet working

> I've never heard of Archcraft

its pretty much vanilla arch with some themes for bspwm and openbox, the kernel is not modified afaik

## selsta | 2024-04-20T11:23:55+00:00
@dement6d did you try the monero-wallet-gui from getmonero.org instead of package manager?

## dement6d | 2024-04-20T19:18:59+00:00
> @dement6d did you try the monero-wallet-gui from getmonero.org instead of package manager?

i just tried, `monero-wallet-gui` from getmonero.org **does** work

## selsta | 2024-04-21T01:32:12+00:00
@dement6d the arch package appears to have been compiled without protobuf and libusb which disables Trezor support.

## kpcyrd | 2024-04-21T20:53:30+00:00
Patches welcome.

I already invested a significant amount of time into this github issue and it's apparently still an issue on/off for >1 year. The concept of silently stripping features from release binaries is evidently wasting people's time.

## selsta | 2024-04-22T00:32:06+00:00
We have added `USE_DEVICE_TREZOR_MANDATORY` CMake variable to the master branch, but since this was a larger change we didn't port it to the release banch yet.

@kpcyrd I might be wrong regarding what I wrote in my previous comment. I checked `PKGBUILD` and there is no `protobuf` under the depends section, but at the same time there is for example https://gitlab.archlinux.org/archlinux/packaging/packages/monero-gui/-/commit/ca9f48f6846b59ec4297784e40e579a805e61669 so it does seem like it depends on protobuf somehow.

# Action History
- Created by: Benjvoo | 2023-01-18T05:10:11+00:00
