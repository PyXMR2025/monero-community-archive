---
title: gui wallet crashes with hardware wallet (Trazor T)
source_url: https://github.com/monero-project/monero-gui/issues/3367
author: DWShuo
assignees: []
labels: []
created_at: '2021-03-24T02:32:08+00:00'
updated_at: '2021-04-07T13:52:24+00:00'
type: issue
status: closed
closed_at: '2021-04-07T13:52:24+00:00'
---

# Original Description
Gui wallet asks for hardware wallet passphrase.

If enter from computer option is chosen, immediately after entering the passphrase gui wallet crashes with the following output.

```
2021-03-24 02:20:40.087	W Qt:5.15.2 GUI:0.17.1.9-3ca5f10f | screen: 1920x1080 - dpi: 96.1263 - ratio:1.12427
2021-03-24 02:20:40.974	W Logging to "/home/nullptr/.bitmonero/monero-wallet-gui.log"
2021-03-24 02:20:40.976	W file:///usr/lib/qt/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[1616552441] libunbound[5437:0] error: read (in tcp s) failed and this could be because TCP Fast Open is enabled [--disable-tfo-client --disable-tfo-server] but does not work: Transport endpoint is not connected for 194.150.168.168 port 53
[1616552441] libunbound[5437:0] error: read (in tcp s) failed and this could be because TCP Fast Open is enabled [--disable-tfo-client --disable-tfo-server] but does not work: Transport endpoint is not connected for 193.58.251.251 port 53
2021-03-24 02:20:47.940	W Account on device. Initing device...
munmap_chunk(): invalid pointer
[1]    5437 abort (core dumped)  ./monero-wallet-gui
```

If the enter passphrase from hardware option is chosen. The wallet is loaded but once syncing begins the gui wallet crashes with the following log

```
2021-03-24 02:23:04.425	W Qt:5.15.2 GUI:0.17.1.9-3ca5f10f | screen: 1920x1080 - dpi: 96.1263 - ratio:1.12427
2021-03-24 02:23:05.309	W Logging to "/home/nullptr/.bitmonero/monero-wallet-gui.log"
2021-03-24 02:23:05.311	W file:///usr/lib/qt/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[1616552585] libunbound[5696:0] error: read (in tcp s) failed and this could be because TCP Fast Open is enabled [--disable-tfo-client --disable-tfo-server] but does not work: Transport endpoint is not connected for 193.58.251.251 port 53
2021-03-24 02:23:09.947	W Account on device. Initing device...
2021-03-24 02:23:27.855	W Device inited...
2021-03-24 02:23:27.948	W Loaded wallet keys file, with public address: 
2021-03-24 02:23:41.571	I Monero 'Oxygen Orion' (v0.17.1.9-release)
Forking to background...
free(): invalid size
[1]    5696 abort (core dumped)  ./monero-wallet-gui
```

#### OS and hardware if relevant:
  OS: Arch Linux x86_64 
  CPU: Intel i7-8750H (12) @ 4.100GHz
  GPU: NVIDIA GeForce GTX 1050 Ti Mobile
  GPU: Intel UHD Graphics 630

 Trezor model T : firmware version 2.3.6

# Discussion History
## dEBRUYNE-1 | 2021-03-29T13:26:16+00:00
Are you running any other wallet software concurrently? 

## DWShuo | 2021-03-31T01:56:33+00:00
I only have monero wallet installed, and im pretty sure nothing else is accessing the trezor 

## dEBRUYNE-1 | 2021-03-31T07:39:52+00:00
Ping @ph4r05.

## ph4r05 | 2021-03-31T08:45:51+00:00
Hello @DWShuo, (@dEBRUYNE-1),

## Quick solution
Typically, when monero-gui crashes, there is some communication problem with the Trezor. A new monero-gui build should not crash, PR is merged (more info below in "New build")

Trezor bridge can sometimes be left in an inconsistent state when previous program tried to use the Trezor and did not close the session properly or Trezor was disconnected or similar problem happened. It is thus recommended to restart the Trezor bridge with each error. 

Fast things to try:
- Try updating [Trezor bridge](https://wiki.trezor.io/Trezor_Bridge)
- Try checking the Trezor USB-C cable (maybe try a different cable)
- Try checking the Trezor operates normally with your official Trezor web wallet https://wallet.trezor.io/

If everything of above works, you can then:
- Unplug the Trezor
- Before running monero-gui, end all other Trezor using processes / web wallets. 
- Also restart trezor bridge, e.g. by `pkill -9 trezord`
- Plug Trezor back to the PC
- Try running monero-gui again
 
If the previous procedure fails, try restarting the whole PC and run only the monero-gui (eliminate possibility something other is trying to access the Trezor or leave it in inconsistent state)

## Cannot replicate the issue - more logs are needed
I've just tried to replicate this issue with:
- monero-gui, current master, b3dace6b450db582d8b683b9dcff4fca96357586
- trezor-firmware, current master, f97af2af1bf49862d79fcdcaf875f2dde10d1949
- trezor-firmware, tag core/v2.3.6 (your Trezor firmware version)

I initialized the Trezor device to use a passphrase.

I tried then to use both emulator and a real device to restore (and open) the wallet entering the passphrase both on computer and the device. It started syncing my testnet and finished fine in both cases. Unfortunately, I am not able to replicate this problem. 

We thus would need more information about this. Could you please run monero-gui with a higher logging level?
We would need also debugging messages from the log (log will be longer)

Start the moner-gui from the console:

```
MONERO_LOG_LEVEL=4 ./monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
```

Also, create a new software wallet with monero-gui (make sure you do not overwrite your previous wallets). After you create a new wallet, you can change a logging level in the monero-gui app: Settings -> Log -> LogLevel -> 4. 

Then try opening/restoring a Trezor-based wallet (log should contain more entries now).

## New build
You obviously use the most up-to-date monero-gui binary, I've checked the tag and commit ID from your log. 

There was [a PR](https://github.com/monero-project/monero/pull/7336) recently merged to a monero codebase that handles similar crashes when working with the Trezor. Thus a new monero-gui release should not cause the crash.
Alternatively, you can build the fresh monero-gui on your own. 
 
The monero-gui v0.17.1.9 usually crashes when there is a communication problem with the Trezor device. E.g., some bridge exception. So if there is still problem with connectivity / trezor-bridge, the new monero-gui won't crash, but it won't work either so it has to be addressed.

https://github.com/monero-project/monero-gui/issues/3296

## DWShuo | 2021-04-01T02:02:56+00:00
This is the level 4 log output when i tried to restore a Trezor-based wallet, im going to uninstall and build monero-gui from master see if that fixes the issue

### Console output:
```
nullptr@nullptr ~ % MONERO_LOG_LEVEL=4 /usr/bin/monero-wallet-gui
2021-04-01 00:41:47.525	W Qt:5.15.2 GUI:0.17.1.9-3ca5f10f | screen: 1920x1080 - dpi: 96.1263 - ratio:1.12427
2021-04-01 00:41:48.057	D fiatPriceError: Invalid ticker value: 0
2021-04-01 00:41:48.090	D Invalid address format
2021-04-01 00:41:48.094	D >>> wallet updated
2021-04-01 00:41:48.104	D fiatPriceError: Invalid ticker value: 0
2021-04-01 00:41:48.104	D fiatPriceError: Invalid ticker value: 0
2021-04-01 00:41:48.409	D transfer page loaded
2021-04-01 00:41:48.507	D SettingsWallet loaded
2021-04-01 00:41:48.508	D SettingsLayout loaded
2021-04-01 00:41:48.508	D setLanguage   "en"
2021-04-01 00:41:48.512	D fiatPriceError: Invalid ticker value: 0
2021-04-01 00:41:48.513	D walletMode: simple
2021-04-01 00:41:48.513	D qrScannerEnabled disabled
2021-04-01 00:41:48.513	D "/tmp/xmr-gui_nullptr.sock"
2021-04-01 00:41:48.514	D Checking for a new monero-gui version for linux-x64
2021-04-01 00:41:48.514	D Checking updates for linux-x64 monero-gui
2021-04-01 00:41:48.516	I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5
2021-04-01 00:41:48.516	I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D
2021-04-01 00:41:48.659	I Found "monero:linux-x64:0.17.1.9:0fb6f53b7b9b3b205151c652b6c9ca7e735f80bfe78427d1061f042723ee6381" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.659	I Found "monero:linux-x86:0.17.1.9:1f51206c1996a577f976c0526b93cc495fe577db21f68b55636dce926f201206" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.659	I Found "monero:mac-x64:0.17.1.9:d4850ae45eee67868140183cd8c00f9e1f9e1cc5e415b00bc78c14c7bab85834" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.659	I Found "monero:win-x64:0.17.1.9:a3e6e2f55deb487f6b4a33cf430d82d62e986d37d7d589dcb33a4ff0a13a062b" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.659	I Found "monero:win-x86:0.17.1.9:bb3c633a3d8ac160bc9c75ef514a9cbc77f1f45bdbd220d1963d78d66435c23a" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.659	I Found "monero:android-armv7:0.17.1.9:c7192caf85f82ecdd1e7299c9ae6314fe2fb02ed9b7035a426a8644b676cc75f" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.660	I Found "monero:android-armv8:0.17.1.9:2c45e0fb364ff2e60aa9cdf0d3faef145b22a8632b3336cc248eeba24352d39b" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.660	I Found "monero:freebsd-x64:0.17.1.9:3052f691a1a7631ba50c3f4d6f1b1355bdcc9a8c0c617cf56ced400afa1ea402" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.660	I Found "monero-gui:install-win-x64:0.17.1.9:edc47b1540510640a40e8d52ad4ab3a6220f935e881fd65b02ccce94a28c3fa2" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.660	I Found "monero-gui:linux-x64:0.17.1.9:6334acbe9877e2e86b1902b111abc59e170aedc701ea71cbae49830191bbd745" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.660	I Found "monero-gui:mac-x64:0.17.1.9:c8a8ea012e8731bfacd17434fdd3a0f03302fc61d7187d218da5ff6a6e869f0b" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.660	I Found "monero-gui:win-x64:0.17.1.9:862aa9a6564a60be3e70ee30eb061d5186a141ce62842b3d741558470c255988" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.660	I Found "monero:linux-armv7:0.17.1.9:c8b226af900b018fade24742e5936b0ef6cec3fcdbc8a57a4b3f3d6d2507a2ec" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.660	I Found "monero:linux-armv8:0.17.1.9:ef16c3aefc8a17f0a547ffec9e2f087923c6bf293b9538294d14cbd318f1ab98" in TXT record for updates.moneropulse.org
2021-04-01 00:41:48.660	I Failed to verify DNSSEC record from updates.moneropulse.org, falling back to TCP with well known DNSSEC resolvers
2021-04-01 00:41:48.660	I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5
2021-04-01 00:41:48.660	I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D
[1617237708] libunbound[1927:0] error: read (in tcp s) failed and this could be because TCP Fast Open is enabled [--disable-tfo-client --disable-tfo-server] but does not work: Transport endpoint is not connected for 80.67.169.40 port 53
[1617237708] libunbound[1927:0] error: read (in tcp s) failed and this could be because TCP Fast Open is enabled [--disable-tfo-client --disable-tfo-server] but does not work: Transport endpoint is not connected for 80.67.169.40 port 53
[1617237709] libunbound[1927:0] error: read (in tcp s) failed and this could be because TCP Fast Open is enabled [--disable-tfo-client --disable-tfo-server] but does not work: Transport endpoint is not connected for 80.67.169.40 port 53
[1617237709] libunbound[1927:0] error: read (in tcp s) failed and this could be because TCP Fast Open is enabled [--disable-tfo-client --disable-tfo-server] but does not work: Transport endpoint is not connected for 194.150.168.168 port 53
[1617237709] libunbound[1927:0] error: read (in tcp s) failed and this could be because TCP Fast Open is enabled [--disable-tfo-client --disable-tfo-server] but does not work: Transport endpoint is not connected for 89.233.43.71 port 53
2021-04-01 00:41:51.373	I Found "monero-gui:mac-x64:0.17.1.9:c8a8ea012e8731bfacd17434fdd3a0f03302fc61d7187d218da5ff6a6e869f0b" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero-gui:install-win-x64:0.17.1.9:edc47b1540510640a40e8d52ad4ab3a6220f935e881fd65b02ccce94a28c3fa2" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:linux-armv7:0.17.1.9:c8b226af900b018fade24742e5936b0ef6cec3fcdbc8a57a4b3f3d6d2507a2ec" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:win-x86:0.17.1.9:bb3c633a3d8ac160bc9c75ef514a9cbc77f1f45bdbd220d1963d78d66435c23a" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:android-armv7:0.17.1.9:c7192caf85f82ecdd1e7299c9ae6314fe2fb02ed9b7035a426a8644b676cc75f" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero-gui:linux-x64:0.17.1.9:6334acbe9877e2e86b1902b111abc59e170aedc701ea71cbae49830191bbd745" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:android-armv8:0.17.1.9:2c45e0fb364ff2e60aa9cdf0d3faef145b22a8632b3336cc248eeba24352d39b" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:freebsd-x64:0.17.1.9:3052f691a1a7631ba50c3f4d6f1b1355bdcc9a8c0c617cf56ced400afa1ea402" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:linux-x64:0.17.1.9:0fb6f53b7b9b3b205151c652b6c9ca7e735f80bfe78427d1061f042723ee6381" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:win-x64:0.17.1.9:a3e6e2f55deb487f6b4a33cf430d82d62e986d37d7d589dcb33a4ff0a13a062b" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero-gui:win-x64:0.17.1.9:862aa9a6564a60be3e70ee30eb061d5186a141ce62842b3d741558470c255988" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:linux-x86:0.17.1.9:1f51206c1996a577f976c0526b93cc495fe577db21f68b55636dce926f201206" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:mac-x64:0.17.1.9:d4850ae45eee67868140183cd8c00f9e1f9e1cc5e415b00bc78c14c7bab85834" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.373	I Found "monero:linux-armv8:0.17.1.9:ef16c3aefc8a17f0a547ffec9e2f087923c6bf293b9538294d14cbd318f1ab98" in TXT record for updates.moneropulse.se
2021-04-01 00:41:51.619	I Found "monero:linux-armv8:0.17.1.9:ef16c3aefc8a17f0a547ffec9e2f087923c6bf293b9538294d14cbd318f1ab98" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.619	I Found "monero-gui:linux-x64:0.17.1.9:6334acbe9877e2e86b1902b111abc59e170aedc701ea71cbae49830191bbd745" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero:linux-x64:0.17.1.9:0fb6f53b7b9b3b205151c652b6c9ca7e735f80bfe78427d1061f042723ee6381" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero-gui:mac-x64:0.17.1.9:c8a8ea012e8731bfacd17434fdd3a0f03302fc61d7187d218da5ff6a6e869f0b" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero:freebsd-x64:0.17.1.9:3052f691a1a7631ba50c3f4d6f1b1355bdcc9a8c0c617cf56ced400afa1ea402" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero-gui:win-x64:0.17.1.9:862aa9a6564a60be3e70ee30eb061d5186a141ce62842b3d741558470c255988" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero-gui:install-win-x64:0.17.1.9:edc47b1540510640a40e8d52ad4ab3a6220f935e881fd65b02ccce94a28c3fa2" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero:linux-armv7:0.17.1.9:c8b226af900b018fade24742e5936b0ef6cec3fcdbc8a57a4b3f3d6d2507a2ec" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero:android-armv8:0.17.1.9:2c45e0fb364ff2e60aa9cdf0d3faef145b22a8632b3336cc248eeba24352d39b" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero:mac-x64:0.17.1.9:d4850ae45eee67868140183cd8c00f9e1f9e1cc5e415b00bc78c14c7bab85834" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero:win-x64:0.17.1.9:a3e6e2f55deb487f6b4a33cf430d82d62e986d37d7d589dcb33a4ff0a13a062b" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero:android-armv7:0.17.1.9:c7192caf85f82ecdd1e7299c9ae6314fe2fb02ed9b7035a426a8644b676cc75f" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero:win-x86:0.17.1.9:bb3c633a3d8ac160bc9c75ef514a9cbc77f1f45bdbd220d1963d78d66435c23a" in TXT record for updates.moneropulse.org
2021-04-01 00:41:51.620	I Found "monero:linux-x86:0.17.1.9:1f51206c1996a577f976c0526b93cc495fe577db21f68b55636dce926f201206" in TXT record for updates.moneropulse.org
2021-04-01 00:41:54.272	I Found "monero-gui:install-win-x64:0.17.1.0:be3b1f07ba86a0d46c27f670b27d936baa5c4e7b68f3dc37349b8f91b073dc6a" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:win-x86:0.17.1.0:d438ce08ebce2705b1de8469833ccda47c76401887751972086246cb3c59f041" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:linux-armv8:0.17.1.0:487011bc1bdaa9bcc276cdbee0930c2289b317c752a99a38d98c0ad13324a612" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero-gui:linux-x64:0.17.1.0:9076b731634e073430817cd590ea015a19a9cf3336c3c7a7bb16f1fd25b429f4" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:linux-armv7:0.17.1.0:2ad46e3834a25f78f1c070220dd1b907200abe57246a7b0cc410b998174e5ed2" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:mac-x64:0.17.1.0:3e9cefcb02e0fd5f4c720165bf1621ccda48f18eda1f63f207f29a2549658620" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero-gui:win-x64:0.17.1.0:85ecd625721435e99fff0f4849ff40bb3f2de26573b50432a5fe9632dfba3026" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero-gui:mac-x64:0.17.1.0:b9c0cbdc8f9c74d6205858ccb4fb0f1eec792e301aa819bf8aa445a3d17869d3" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:win-x64:0.17.1.0:b942b584601faa504ed2eb5c6d7bdf62740826cbef63d33d35b48e414dd48f5d" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:linux-x64:0.17.1.0:b7b573ff3d2013527fce47643a6738eaf55f10894fa5b2cb364ba5cd937af92e" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:android-armv8:0.17.1.0:a758c81dfe177c74567e9793e1332adc3e2ce9ae71addb81f1e7f5fcce4303f7" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:linux-x86:0.17.1.0:e58e1f60120cc9a3be1f6bad95d4605843608630437794c56d705547db2bfd69" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:freebsd-x64:0.17.1.0:11577db88edf29d5a09c45599cb43c1da568f63a1303322bf0aecabfaffd48a7" in TXT record for updates.moneropulse.co
2021-04-01 00:41:54.272	I Found "monero:android-armv7:0.17.1.0:e0234000ee183656092621066658bece27a49442101755b565f190d4e0d29314" in TXT record for updates.moneropulse.co
2021-04-01 00:41:56.921	I Found "monero:mac-x64:0.17.1.9:d4850ae45eee67868140183cd8c00f9e1f9e1cc5e415b00bc78c14c7bab85834" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero:win-x86:0.17.1.9:bb3c633a3d8ac160bc9c75ef514a9cbc77f1f45bdbd220d1963d78d66435c23a" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero:android-armv7:0.17.1.9:c7192caf85f82ecdd1e7299c9ae6314fe2fb02ed9b7035a426a8644b676cc75f" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero:freebsd-x64:0.17.1.9:3052f691a1a7631ba50c3f4d6f1b1355bdcc9a8c0c617cf56ced400afa1ea402" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero:android-armv8:0.17.1.9:2c45e0fb364ff2e60aa9cdf0d3faef145b22a8632b3336cc248eeba24352d39b" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero-gui:mac-x64:0.17.1.9:c8a8ea012e8731bfacd17434fdd3a0f03302fc61d7187d218da5ff6a6e869f0b" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero:linux-x64:0.17.1.9:0fb6f53b7b9b3b205151c652b6c9ca7e735f80bfe78427d1061f042723ee6381" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero-gui:linux-x64:0.17.1.9:6334acbe9877e2e86b1902b111abc59e170aedc701ea71cbae49830191bbd745" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero-gui:win-x64:0.17.1.9:862aa9a6564a60be3e70ee30eb061d5186a141ce62842b3d741558470c255988" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero:win-x64:0.17.1.9:a3e6e2f55deb487f6b4a33cf430d82d62e986d37d7d589dcb33a4ff0a13a062b" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero:linux-x86:0.17.1.9:1f51206c1996a577f976c0526b93cc495fe577db21f68b55636dce926f201206" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero:linux-armv8:0.17.1.9:ef16c3aefc8a17f0a547ffec9e2f087923c6bf293b9538294d14cbd318f1ab98" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero-gui:install-win-x64:0.17.1.9:edc47b1540510640a40e8d52ad4ab3a6220f935e881fd65b02ccce94a28c3fa2" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	I Found "monero:linux-armv7:0.17.1.9:c8b226af900b018fade24742e5936b0ef6cec3fcdbc8a57a4b3f3d6d2507a2ec" in TXT record for updates.moneropulse.net
2021-04-01 00:41:56.921	D DNSSEC not available for hostname: updates.moneropulse.co, skipping.
2021-04-01 00:41:56.921	D DNSSEC validation failed for hostname: updates.moneropulse.co, skipping.
2021-04-01 00:41:56.921	I Found new version 0.17.1.9 with hash 6334acbe9877e2e86b1902b111abc59e170aedc701ea71cbae49830191bbd745
2021-04-01 00:41:57.194	W Logging to "/home/nullptr/.bitmonero/monero-wallet-gui.log"
2021-04-01 00:42:35.045	W file:///usr/lib/qt/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
free(): invalid size
[1]    1927 abort (core dumped)  MONERO_LOG_LEVEL=4 /usr/bin/monero-wallet-gui
```

### monero-wallet-gui.log

```
2021-04-01 00:41:57.194	    7fc8e58c3b40	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-04-01 00:41:57.194	    7fc8e58c3b40	WARNING	frontend	src/wallet/api/wallet.cpp:412	Logging to "/home/nullptr/.bitmonero/monero-wallet-gui.log"
2021-04-01 00:42:35.045	    7fc8e58c3b40	WARNING	frontend	src/wallet/api/wallet.cpp:412	file:///usr/lib/qt/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
```

## ph4r05 | 2021-04-01T08:09:19+00:00
@DWShuo unfortunately, there is no debug message in the `monero-wallet-gui.log`. There is also no new useful information in the logs.

Did you also try to change log level in the Monero gui settings? Both are needed.

Also - did you try all the steps with webwallet and trezor bridge update and restart? Thanks

When building your own binary pls make sure you have all dependencies installed according to the [Monero readme](https://github.com/monero-project/monero) and Monero GUI readme.

You need to have installed: `libhidapi`, `libusb`, `libprotobuf`, `protoc`, `libudev`, otherwise Trezor support won't compile in.

## DWShuo | 2021-04-01T10:09:37+00:00
okay here is the log, is `Enumeration yielded 2 Trezor devices` the problem here?
### monero-wallet-gui.log
```
2021-04-01 09:42:29.813	    7fe5a0cc6640	INFO	WalletAPI	src/wallet/api/wallet.cpp:770	closing wallet...
2021-04-01 09:42:29.813	    7fe5a0cc6640	INFO	WalletAPI	src/wallet/api/wallet.cpp:781	Calling wallet::stop...
2021-04-01 09:42:29.813	    7fe5a0cc6640	INFO	WalletAPI	src/wallet/api/wallet.cpp:783	wallet::stop done
2021-04-01 09:42:29.813	    7fe54c823640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2150	refreshThreadFunc: refresh lock acquired...
2021-04-01 09:42:29.813	    7fe54c823640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2151	refreshThreadFunc: m_refreshEnabled: 0
2021-04-01 09:42:29.813	    7fe54c823640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2152	refreshThreadFunc: m_status: 0
2021-04-01 09:42:29.813	    7fe54c823640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2153	refreshThreadFunc: m_refreshShouldRescan: 0
2021-04-01 09:42:29.813	    7fe54c823640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2159	refreshThreadFunc: refresh thread stopped
2021-04-01 09:42:29.813	    7fe5a0cc6640	INFO	WalletAPI	src/wallet/api/wallet.cpp:466	~WalletImpl finished
2021-04-01 09:42:29.813	    7fe5a0cc6640	DEBUG	net	contrib/epee/include/net/net_helper.h:647	Problems at ssl shutdown: uninitialized
2021-04-01 09:42:29.813	    7fe5a0cc6640	DEBUG	net	contrib/epee/include/net/net_helper.h:571	Problems at cancel: Bad file descriptor
2021-04-01 09:42:29.813	    7fe5a0cc6640	DEBUG	net	contrib/epee/include/net/net_helper.h:574	Problems at shutdown: Bad file descriptor
2021-04-01 09:42:29.815	    7fe5a0cc6640	DEBUG	frontend	src/wallet/api/wallet.cpp:404	m_walletImpl deleted
2021-04-01 09:42:29.818	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Hiding processing splash
2021-04-01 09:45:11.548	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Calculated blockchain height: 2205988
2021-04-01 09:45:11.563	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Creating temporary wallet /tmp/monero-core.vKQxGu
2021-04-01 09:45:11.563	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Displaying processing splash
2021-04-01 09:45:11.565	    7fe5a0cc6640	DEBUG	device	src/cryptonote_basic/account.cpp:62	account_keys::set_device device type: N2hw6trezor13device_trezorE
2021-04-01 09:45:11.565	    7fe5a0cc6640	DEBUG	device	src/cryptonote_basic/account.cpp:216	device type: N2hw6trezor13device_trezorE
2021-04-01 09:45:11.565	    7fe5a0cc6640	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:117	Enumerating Trezor devices...
2021-04-01 09:45:11.565	    7fe5a0cc6640	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2021-04-01 09:45:11.566	    7fe5a0cc6640	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-04-01 09:45:11.569	    7fe5a0cc6640	TRACE	net	contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 267
2021-04-01 09:45:11.569	    7fe5a0cc6640	TRACE	net.http	contrib/epee/include/net/http_client.h:654	http_stream_filter::parse_cached_header(*)
2021-04-01 09:45:11.569	    7fe5a0cc6640	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2021-04-01 09:45:11.599	    7fe5a0cc6640	TRACE	device.trezor.transport	src/device_trezor/trezor/transport.cpp:914	Libusb devices: 14
2021-04-01 09:45:11.599	    7fe5a0cc6640	TRACE	device.trezor.transport	src/device_trezor/trezor/transport.cpp:929	Found Trezor device: 4617:21441 dev_idx 1
2021-04-01 09:45:11.600	    7fe5a0cc6640	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:121	Enumeration yielded 2 Trezor devices
2021-04-01 09:45:11.600	    7fe5a0cc6640	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:123	  device: BridgeTransport<path=bridge:10, info={"path":"10","vendor":4617,"product":21441,"debug":false,"session":null,"debugSession":null}, session=None>
2021-04-01 09:45:11.600	    7fe5a0cc6640	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:123	  device: WebUsbTransport<path=webusb:001:2, vendorId=4617, productId=21441, deviceType=TrezorT>
2021-04-01 09:45:11.600	    7fe5a0cc6640	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:129	Device Match: bridge:10
2021-04-01 09:45:11.600	    7fe5a0cc6640	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-04-01 09:45:11.869	    7fe5a0cc6640	TRACE	net	contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 189
2021-04-01 09:45:11.870	    7fe5a0cc6640	TRACE	net.http	contrib/epee/include/net/http_client.h:654	http_stream_filter::parse_cached_header(*)
2021-04-01 09:45:11.933	    7fe5a0cc6640	TRACE	net	contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 607
2021-04-01 09:45:11.934	    7fe5a0cc6640	TRACE	net.http	contrib/epee/include/net/http_client.h:654	http_stream_filter::parse_cached_header(*)
2021-04-01 09:45:12.385	    7fe5a0cc6640	TRACE	net	contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 184
2021-04-01 09:45:12.386	    7fe5a0cc6640	TRACE	net.http	contrib/epee/include/net/http_client.h:654	http_stream_filter::parse_cached_header(*)
2021-04-01 09:45:12.386	    7fe5a0cc6640	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:476	on_passhprase_request
2021-04-01 09:45:12.386	    7fe5a0cc6640	DEBUG	frontend	src/wallet/api/wallet.cpp:404	onDevicePassphraseRequest
2021-04-01 09:45:12.386	    7fe5a0cc6640	DEBUG	frontend	src/wallet/api/wallet.cpp:404	onDevicePassphraseRequest
2021-04-01 09:45:12.389	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Hiding processing splash
2021-04-01 09:45:12.391	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet passphrase needed: 
2021-04-01 09:45:12.394	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet passphrase needed: 
2021-04-01 09:45:13.130	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	onPassphraseEntered
2021-04-01 09:45:13.130	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	onPassphraseEntered
2021-04-01 09:45:13.130	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Displaying processing splash
2021-04-01 09:45:13.136	    7fe5a0cc6640	TRACE	net	contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 188
2021-04-01 09:45:13.136	    7fe5a0cc6640	TRACE	net.http	contrib/epee/include/net/http_client.h:654	http_stream_filter::parse_cached_header(*)
2021-04-01 09:45:13.136	    7fe5a0cc6640	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:429	on_button_request, code: 19
2021-04-01 09:45:13.136	    7fe5a0cc6640	DEBUG	frontend	src/wallet/api/wallet.cpp:404	onDeviceButtonRequest
2021-04-01 09:45:13.143	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Displaying processing splash
2021-04-01 09:45:13.144	    7fe5a2480b40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Displaying processing splash
2021-04-01 09:45:21.565	    7fe59b7fe640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2150	refreshThreadFunc: refresh lock acquired...
2021-04-01 09:45:21.565	    7fe59b7fe640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2151	refreshThreadFunc: m_refreshEnabled: 0
2021-04-01 09:45:21.565	    7fe59b7fe640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2152	refreshThreadFunc: m_status: 0
2021-04-01 09:45:21.565	    7fe59b7fe640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2153	refreshThreadFunc: m_refreshShouldRescan: 0
2021-04-01 09:45:21.565	    7fe59b7fe640	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2140	refreshThreadFunc: waiting for refresh...
2021-04-01 09:45:30.032	    7fe5a0cc6640	TRACE	net	contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 379
2021-04-01 09:45:30.032	    7fe5a0cc6640	TRACE	net.http	contrib/epee/include/net/http_client.h:654	http_stream_filter::parse_cached_header(*)
2021-04-01 09:45:30.033	    7fe5a0cc6640	DEBUG	frontend	src/wallet/api/wallet.cpp:404	onDeviceButtonPressed
2021-04-01 09:45:30.033	    7fe5a0cc6640	TRACE	device.trezor	src/device_trezor/device_trezor.cpp:239	Get address response received
2021-04-01 09:45:30.033	    7fe5a0cc6640	DEBUG	device.trezor	src/device_trezor/device_trezor.cpp:181	Loading view-only key from the Trezor. Please check the Trezor for a confirmation.
```

## ph4r05 | 2021-04-01T10:39:58+00:00
No it is a normal behaviour, Trezor is reachable via both bridge and webusb.  But still, logs do not show any problem. 

The log `Device Match: bridge:10` indiates the bridge is being used. 
You could try forcing using webusb (native libusb) by exporting the environment variable `TREZOR_PATH=webusb`. Webusb driver bypasses bridge so it can avoid some consistency problem the bridge might have.

The most probable cause is problem with the bridge. Pls let us know how fixes proposed in "Quick solution" went.

> Also - did you try all the steps with webwallet and trezor bridge update and restart? Thanks

When it is still crashing, try attaching `gdb` or starting it with `gdb /usr/bin/monero-wallet-gui`. If program crashes, try command `bt` to dump the stack trace. It would be quite helpful. 

Btw is this your own build or still the official binary?

## ph4r05 | 2021-04-06T08:55:02+00:00
ping @DWShuo :)
can we close the issue?

## DWShuo | 2021-04-06T12:26:08+00:00
Yeah i guess, i pretty much tried everything, webwallet works fine, gdb doesn't  give much more info than the logs. I installed ubuntu on another computer that worked fine.  

Im currently using archlabs (pretty much just a install script for arch). Did a barebones reinstall its still crashing. So am thinking maybe this can be reproduced in a VM. In the meantime i have resorted to using monero wallet running in whonix

## ph4r05 | 2021-04-06T13:15:50+00:00
@DWShuo thanks for info! So `gdb` and then `bt` when it crashed did not reveal helpful stacktrace? Or the place of the crash? That would be helpful.

So Ubuntu did not crash with Trezor? And Whonix works with Trezor as well or you are using software only there?

Did you also try your own build that should not crash? (from master). Thanks!

## DWShuo | 2021-04-07T02:49:29+00:00
I can confirm this problem is reproducible in a vm.
Both ubuntu and whonix worked fine using trezor, [trezord-go](https://github.com/trezor/trezord-go), and monero-gui

Here is the output from `gdb` and `bt`, this is the version from the arch repo. I ran into some problems with building from master, im trying to fix it now.

```
user@archlabs ~ % gdb /usr/bin/monero-wallet-gui 
GNU gdb (GDB) 10.1
Reading symbols from /usr/bin/monero-wallet-gui...
(No debugging symbols found in /usr/bin/monero-wallet-gui)
(gdb) r
Starting program: /usr/bin/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
[New Thread 0x7ffff1d1b640 (LWP 13539)]
[New Thread 0x7ffff1474640 (LWP 13540)]
2021-04-07 02:30:07.333	W Qt:5.15.2 GUI:0.17.1.9-3ca5f10f | screen: 800x600 - dpi: 96.3795 - ratio:0.752965
[New Thread 0x7ffff0c73640 (LWP 13541)]
[New Thread 0x7fffdb890640 (LWP 13542)]
[New Thread 0x7fffdb08f640 (LWP 13543)]
[New Thread 0x7fffda88e640 (LWP 13544)]
[New Thread 0x7fffda08d640 (LWP 13545)]
[New Thread 0x7fffd9689640 (LWP 13546)]
[New Thread 0x7fffd8e32640 (LWP 13547)]
[New Thread 0x7fffc2989640 (LWP 13548)]
[New Thread 0x7fffc0b12640 (LWP 13549)]
[New Thread 0x7fffc0311640 (LWP 13550)]
[New Thread 0x7fffbfb10640 (LWP 13551)]
[New Thread 0x7fffc3ff8640 (LWP 13552)]
[1617762608] libunbound[13535:0] error: read (in tcp s) failed and this could be because TCP Fast Open is enabled [--disable-tfo-client --disable-tfo-server] but does not work: Transport endpoint is not connected for 89.233.43.71 port 53
2021-04-07 02:30:35.634	W Logging to "/home/user/.bitmonero/monero-wallet-gui.log"
[Thread 0x7fffc0b12640 (LWP 13549) exited]
[Thread 0x7fffc0311640 (LWP 13550) exited]
[Thread 0x7ffff1474640 (LWP 13540) exited]
2021-04-07 02:31:07.479	W file:///usr/lib/qt/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[New Thread 0x7fffc0311640 (LWP 13562)]
[New Thread 0x7ffff1474640 (LWP 13563)]
[New Thread 0x7fffc0b12640 (LWP 13564)]
[Thread 0x7fffc0b12640 (LWP 13564) exited]
free(): invalid size
 
Thread 14 "Thread (pooled)" received signal SIGABRT, Aborted.
[Switching to Thread 0x7fffbfb10640 (LWP 13551)]
0x00007ffff501eef5 in raise () from /usr/lib/libc.so.6
(gdb) bt
#0  0x00007ffff501eef5 in raise () from /usr/lib/libc.so.6
#1  0x00007ffff5008862 in abort () from /usr/lib/libc.so.6
#2  0x00007ffff5060f38 in __libc_message ()
   from /usr/lib/libc.so.6
#3  0x00007ffff5068bea in malloc_printerr ()
   from /usr/lib/libc.so.6
#4  0x00007ffff5069fcc in _int_free () from /usr/lib/libc.so.6
#5  0x00007ffff506dca8 in free () from /usr/lib/libc.so.6
#6  0x00007ffff5888277 in google::protobuf::internal::ArenaStringPtr::SetAllocated(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, google::protobuf::Arena*) () from /usr/lib/libprotobuf.so.26
#7  0x0000555555d074a5 in ?? ()
#8  0x0000555555bfc1dc in ?? ()
#9  0x0000555555bfc956 in ?? ()
#10 0x0000555555b1fbe5 in ?? ()
#11 0x0000555555973267 in ?? ()
#12 0x00005555558006e7 in ?? ()
#13 0x000055555583c60c in ?? ()
#14 0x00005555557c1e71 in ?? ()
#15 0x00005555557c23de in ?? ()
#16 0x00005555557df9a6 in ?? ()
#17 0x00007ffff5ba42f2 in ?? () from /usr/lib/libQt5Core.so.5
#18 0x00007ffff5ba0eff in ?? () from /usr/lib/libQt5Core.so.5
#19 0x00007ffff51b8299 in start_thread ()
   from /usr/lib/libpthread.so.0
#20 0x00007ffff50e1053 in clone () from /usr/lib/libc.so.6
```

## ph4r05 | 2021-04-07T07:41:33+00:00
Thanks for more info @DWShuo! It is interesting it is crashing only in Arch. 

Did you pls try to bypass trezor-bridge with `TREZOR_PATH=webusb` and observe if the webusb link gets selected in the logs? This could be helpful. 

Also it would be great if you can build the newest master. Compiling `make devmode` should be more helpful for obtaining stacktraces from the crash.

Also, if you could replace line https://github.com/monero-project/monero-gui/blob/183585653f70e6ca66a043c42fdd825f1899c1c4/Makefile#L41 with
```
	mkdir -p build && cd build && cmake -DTREZOR_DEBUG=ON -D ARCH="x86-64" -D DEV_MODE=$(or ${DEV_MODE},ON) -DMANUAL_SUBMODULES=${MANUAL_SUBMODULES} -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release .. && $(MAKE)
```

(`-DTREZOR_DEBUG=ON` added, indent is important).
Thanks!!

## DWShuo | 2021-04-07T08:06:06+00:00
@ph4r05 good news, I built the master branch of [monero](https://github.com/monero-project/monero) and current release of monero-gui everything is working correctly now. 

## ph4r05 | 2021-04-07T09:02:41+00:00
@DWShuo good to hear! Thanks for testing. So the new release should have everything fixed. 

# Action History
- Created by: DWShuo | 2021-03-24T02:32:08+00:00
- Closed at: 2021-04-07T13:52:24+00:00
