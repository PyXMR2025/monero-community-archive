---
title: Drop-down menus not opening on Manjaro (KDE)
source_url: https://github.com/monero-project/monero-gui/issues/3938
author: SandaruKasa
assignees: []
labels: []
created_at: '2022-06-04T11:22:55+00:00'
updated_at: '2023-01-25T07:30:59+00:00'
type: issue
status: closed
closed_at: '2023-01-11T17:17:43+00:00'
---

# Original Description
I'm running Manjaro Linux x86_64 with Plasma 5.24.5 and kwin-bismuth tiling extension 3.1.1 (though, I don't think Bismuth is relevant here, because the issue persists even when I turn the tiling off).

I've installed monero-gui 0.17.3.2-1 via pacman and the dropdown menus in it don't seem to be working. When I click on one, nothing happens. Such menus include, for example, the network selection (mainnet/stagenet/testnet) during wallet setup or transaction priority in the "Send" tab of the app.

# Discussion History
## SandaruKasa | 2022-06-04T11:44:18+00:00
Tried building from source instead, same issue.

## selsta | 2022-06-04T13:09:31+00:00
Can you try the getmonero.org binary for testing purposes?

## SandaruKasa | 2022-06-04T14:06:12+00:00
Okay, tried it, it works properly

## selsta | 2022-06-04T14:12:34+00:00
Similar report: https://github.com/monero-project/monero-gui/issues/3152

## devhyper | 2022-06-08T01:05:10+00:00
I get this issue when compiling from source, but when compiling statically with docker it works fine.

## selsta | 2022-06-08T07:28:22+00:00
I always assumed it's related to how arch package manager compiles Qt.

## devhyper | 2022-06-08T21:14:21+00:00
I'm on Fedora, so it might be related to their packaging too.

## selsta | 2022-06-10T18:15:35+00:00
@devhyper do you use KDE on fedora?

## devhyper | 2022-06-10T21:10:57+00:00
> @devhyper do you use KDE on fedora?

Yes.

## dginovker | 2022-06-13T06:12:13+00:00
Another data point - 

```
Kubuntu 22.04 LTS x86_64 
DE: Plasma 5.24.4 
WM: KWin 
Theme: Breeze Light [Plasma], Breeze [GTK2/3]
Install Method: Flatpak
```

Dropdowns don't work and a lot of text fields are just white - including my address and my mnemonic when I created the wallet.

![image](https://user-images.githubusercontent.com/32943174/173290533-af6286b1-1ec8-4bbf-83db-92ab0d304621.png)

*****

The Flatpak install works perfectly fine on the below system:

```
Xubuntu 21.10 x86_64 
DE: Xfce 
WM: Xfwm4 
Chicago95 [GTK2], Greybird [GTK3]
Install Method: Flatpak
```

I can also provide a Monero contributor remote access to this machine via [AnyDesk](https://flathub.org/apps/details/com.anydesk.Anydesk) - PM me on Reddit (/u/OsrsNeedsF2P) or via Email (danielginovker@gmail.com) with confirmation here

## q7nm | 2022-06-13T14:35:04+00:00
I can confirm. The problem occurs in the flatpak version and from the repository in archlinux. (but the official binary works fine)

## RootInit | 2022-09-10T06:22:39+00:00
Can confirm this is still an issue.

## damianchoc | 2022-09-10T14:03:45+00:00
tested now on Manjaro with KDE and it still doesn't work 
Edit:
it works when i run monero-gui with sudo

## Jaspix | 2022-09-27T00:15:42+00:00
I get the same issue with Arch with KDE.

## SamuelAleks | 2022-10-01T15:59:00+00:00
Can confirm this issue with EndeavourOS KDE. Only works with sudo

## selsta | 2022-10-01T16:58:10+00:00
Can someone compile monero-gui with Qt installed using https://github.com/engnr/qt-downloader instead of from package manager?

## SandaruKasa | 2022-10-04T10:53:03+00:00
> Can someone compile monero-gui with Qt installed using https://github.com/engnr/qt-downloader instead of from package manager?

I'd love to try, but as an effort to help Ukrainian civilians (I guess), qt.io doesn't allow downloading anything from a Russian IP address.

I've tried using VPN, but that qt-downloader thing gave me an error anyways. Although this time it looks like a qt-downloader bug and not a byproduct of war:
```
$ ./qt-downloader/qt-downloader linux desktop 5.15.6
OS type: linux
Target: desktop
Qt version: 5.15.6
Discovering available toolchains...b'<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>404 Not Found</title>\n</head><body>\n<h1>Not Found</h1>\n<p>The requested URL was not found on this server.</p>\n</body></html>\n'
 Done
  Choose from: 
```

## selsta | 2022-10-04T10:55:15+00:00
@SandaruKasa try 5.15.2, Qt does not offer prebuilt binaries for newer 5.15 versions.

## SandaruKasa | 2022-10-04T11:27:25+00:00
> @SandaruKasa try 5.15.2, Qt does not offer prebuilt binaries for newer 5.15 versions.

It works. I have to `LD_LIBRARY_PATH=~/qt/5.15.2/gcc_64/lib/ ./monero-wallet-gui`, but drop-down menus work just fine.

## selsta | 2022-10-04T17:45:59+00:00
As I suspected here: https://github.com/monero-project/monero-gui/issues/3938#issuecomment-1149561913

Don't really know how to continue here, since it seems to be an issue with how Qt gets compiled when installing from package manger. Not sure if they add custom patches on top.

## SandaruKasa | 2022-10-08T10:32:26+00:00
Well, since the static binary seems to work without any problems, I've added it to AUR: https://aur.archlinux.org/packages/monero-gui-static-bin

Hope it'll help Arch/Manjaro/etc. users out there.

## RootInit | 2022-11-08T03:26:50+00:00
Bumping this issue. I would rather not use the AUR workaround

## jkhsjdhjs | 2022-11-25T15:02:27+00:00
The following line is logged for me 71 times if I run `monero-wallet-gui` from the command line:

    2022-11-25 14:39:49.174 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.

This doesn't happen with the downloaded qt version (I used the same method described in https://github.com/monero-project/monero-gui/issues/3938#issuecomment-1266765352).
I'm using Arch Linux, but maybe this also happens on other distros where the dropdowns don't work.

## devhyper | 2022-11-25T22:24:05+00:00
I found a workaround, to disable KDE's theming of monero-gui:

1. Install `qt5ct`
2. run monero-gui-wallet with `QT_QPA_PLATFORMTHEME=qt5ct`

## jkhsjdhjs | 2022-11-25T23:40:57+00:00
Works perfectly, thank you so much for this! The `recursive rearrange` warnings are still shown on startup, so it's possible they aren't related to this issue.

## RootInit | 2022-11-26T00:52:49+00:00
But... what if we don't want to change system theme. Running it with that as an argument did nothing.

## selsta | 2022-11-26T00:54:16+00:00
It's a QML application. We don't support any themes and I have no idea what exactly these KDE themes are supposed to change.

## selsta | 2022-11-26T00:55:25+00:00
@RootInit did you do

```
QT_QPA_PLATFORMTHEME=qt5ct monero-wallet-gui
```

It seems to have worked for the other user.

## RootInit | 2022-11-26T00:58:56+00:00
@selsta No I did `monero-wallet-gui QT_QPA_PLATFORMTHEME=qt5ct`

Did work the proper way. I guess I will use that workaround.

## Mart-Bogdan | 2022-11-26T20:37:58+00:00
> Dropdowns don't work and a lot of text fields are just white - including my address and my mnemonic when I created the wallet.

I've solved issue with white textboxes, by swithcing wallet to white theme.

But no luck with dropdowns.

## Mart-Bogdan | 2022-11-26T20:47:40+00:00
Indeed `QT_QPA_PLATFORMTHEME=qt5ct` helps.

so I've basically changed my `monero-gui.desktop` to following, and it works.

```ini
[Desktop Entry]
...
Exec=env QMLSCENE_DEVICE=softwarecontext QT_QPA_PLATFORMTHEME=qt5ct monero-wallet-gui %u
```
I'm using QMLSCENE_DEVICE to disable fancy effects like blur, becouse:
1. Reduce VRAM usage
2. increase startup time
3. Blured window still leaks some personal information. 

But first 2 are more important for me.

This aren't related to this issue.


Now comes the question, how we should proceed? can we make some workaround insied monero GUI to detect/reject nonstandard QT themes?
Or we should just ping distros maintainers to fix the desktop file with workaround? ( as I understand problem is not only on Manjaro)

## jkhsjdhjs | 2022-11-26T23:34:55+00:00
[Antonio Rojas recommended](https://bugs.archlinux.org/task/72489#comment213161) to report this issue to KDE, which is what I did: https://bugs.kde.org/show_bug.cgi?id=462293

## jkhsjdhjs | 2022-12-01T22:36:50+00:00
Can a dev put together a simple testcase that can be run with `qmlscene` and illustrates the issue? That would really help the KDE devs locate the issue! Thanks in advance!
https://bugs.kde.org/show_bug.cgi?id=462293#c3

## devhyper | 2022-12-26T10:32:13+00:00
#4091 will fix this, an alternative workaround that does not require qt5ct is to use the env var `QT_QUICK_CONTROLS_STYLE=desktop`

## Mart-Bogdan | 2023-01-04T20:40:10+00:00
> #4091 will fix this, an alternative workaround that does not require qt5ct is to use the env var `QT_QUICK_CONTROLS_STYLE=desktop`

Wuld this be actual fix? If it sets "desktop", but correct fix them is `qt5ct` 

## Mart-Bogdan | 2023-01-04T20:41:40+00:00
yeah. it works. thanks)))))) would wait for PR


## Rikj000 | 2023-01-25T06:57:10+00:00
~~Please re-open this issue as it still occurs on Manjaro Linux to this day.~~
See comment by @selsta https://github.com/monero-project/monero-gui/issues/3938#issuecomment-1403199224

### Work Around
1. Install `qt5ct` through `pamac`
2. Alter the `Exec` entry in `/usr/share/applications/monero-gui.desktop` as following:
    ```properties
    Exec=QT_QPA_PLATFORMTHEME=qt5ct monero-wallet-gui %u
    ```

## selsta | 2023-01-25T07:26:58+00:00
@Rikj000 The issue has been fixed in code so we closed the issue. You have to wait for the next release.

## Rikj000 | 2023-01-25T07:30:59+00:00
> @Rikj000 The issue has been fixed in code so we closed the issue. You have to wait for the next release.

Thank you @selsta, happy too hear that!   
I've altered my comment accordingly :slightly_smiling_face:  

# Action History
- Created by: SandaruKasa | 2022-06-04T11:22:55+00:00
- Closed at: 2023-01-11T17:17:43+00:00
