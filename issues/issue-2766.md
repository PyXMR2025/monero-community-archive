---
title: strange font bug
source_url: https://github.com/monero-project/monero-gui/issues/2766
author: susp3c1
assignees: []
labels: []
created_at: '2020-02-05T08:17:48+00:00'
updated_at: '2021-12-02T06:04:29+00:00'
type: issue
status: closed
closed_at: '2021-12-02T06:04:29+00:00'
---

# Original Description
package from arch community repo

this is how it locks:
https://imgur.com/FUgtrBu.png

## ~/.bitmonero/monero-wallet-gui.log

`2020-02-05 08:12:07.988	    7f2f1c859ac0	WARNING	wallet.wallet2	src/mnemonics/language_base.h:198	Español word 'red' is shorter than its prefix length, 4
2020-02-05 08:12:07.988	    7f2f1c859ac0	WARNING	wallet.wallet2	src/mnemonics/language_base.h:198	Español word 'res' is shorter than its prefix length, 4
2020-02-05 08:12:07.988	    7f2f1c859ac0	WARNING	wallet.wallet2	src/mnemonics/language_base.h:198	Español word 'rey' is shorter than its prefix length, 4
2020-02-05 08:13:52.667	    7f2f1c859ac0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:/wizard/WizardOpenWallet1.qml:48: TypeError: Cannot call method 'rowCount' of null
2020-02-05 08:13:52.667	    7f2f1c859ac0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:/wizard/WizardOpenWallet1.qml:72: TypeError: Cannot call method 'rowCount' of null
2020-02-05 08:13:58.902	    7f0d73862ac0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-02-05 08:13:58.902	    7f0d73862ac0	WARNING	frontend	src/wallet/api/wallet.cpp:410	app startd (log: /home/suspect/.bitmonero/monero-wallet-gui.log)
2020-02-05 08:13:58.903	    7f0d73862ac0	WARNING	frontend	src/wallet/api/wallet.cpp:410	Qt:5.14.1 GUI:- | screen: 1366x768 - dpi: 96 - ratio:0.885438
2020-02-05 08:14:00.122	    7f0d2e544700	WARNING	frontend	src/wallet/api/wallet.cpp:410	Warning: distance-field glyph is not available with index 1831
2020-02-05 08:14:56.876	    7f0d2e544700	WARNING	frontend	src/wallet/api/wallet.cpp:410	Warning: distance-field glyph is not available with index 1831
`

##Console log
`2020-02-05 08:13:58.902	W app startd (log: /home/suspect/.bitmonero/monero-wallet-gui.log)
2020-02-05 08:13:58.903	W Qt:5.14.1 GUI:- | screen: 1366x768 - dpi: 96 - ratio:0.885438
2020-02-05 08:14:00.122	W Warning: distance-field glyph is not available with index 1831
2020-02-05 08:14:56.877	W Warning: distance-field glyph is not available with index 1831
`

# Discussion History
## selsta | 2020-02-05T08:35:57+00:00
Can/Did you report it to the arch repo/package? Does the same happen with the getmonero.org version?

## selsta | 2020-04-22T20:47:30+00:00
ping

## xblackbytesx | 2020-04-23T14:19:18+00:00
I have the exact same issue. Both with the binary release in the official Arch repository as with my self-built binaries. Everything else seems to run perfectly fine but the 'excerpt' fonts are completely unreadable and renders the wallet unusable at the moment.

Some of this error log is probably not related at all and I think it's mostly due to the distance-field-glyph issue. But for completeness I've included the entire stdout output.
```
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
2020-04-23 14:13:59.266	W app startd (log: /home/$USER/.bitmonero/monero-wallet-gui.log)
2020-04-23 14:13:59.266	W Qt:5.14.2 GUI:- | screen: 1440x900 - dpi: 96 - ratio:0.858178
2020-04-23 14:13:59.882	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2020-04-23 14:14:00.399	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2020-04-23 14:14:00.436	W Warning: distance-field glyph is not available with index 1831
2020-04-23 14:14:01.324	I Version 0.15.0.1 of monero-gui for linux-x64 is available: https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.15.0.1.tar.bz2, SHA256 hash 85a6885849d578691a09834c66ed55af4783ea8347b7784de9ea46e90995a57c
2020-04-23 14:14:04.509	E Failed to fetch and verify signed hash: failed to fetch https://web.getmonero.org/downloads/hashes.txt.sig: response code 404
2020-04-23 14:14:14.636	W Warning: distance-field glyph is not available with index 1831
```

Really hope this can be fixed. At first I figured I might be missing a requirement or something but I can't seem to find a proper fix other than maybe the codebase has an issue perhaps.

Thanks!

## xblackbytesx | 2020-04-23T14:26:14+00:00
Btw. To answer your previous question to OP: For me the version from getmonero.org is working fine. It does however have scaling issues where it is tiny on high-density screen. Other than that there seems to be no issues with glyphs. What would be the difference there? I built my build from the instructions in the README. When it comes to wallets I always prefer to build from source.

## selsta | 2020-04-23T14:59:18+00:00
> For me the version from getmonero.org is working fine. It does however have scaling issues where it is tiny on high-density screen.

getmonero.org uses Qt 5.9 which does not have automatic high dpi scaling. Self compiled uses Qt 5.14 which has this feature.

You can play around with the `QT_SCALE_FACTOR` env var, e.g. set it to `QT_SCALE_FACTOR=2` to get high dpi support with the getmonero.org version.

Regarding the font issue, no idea at the moment.

## xblackbytesx | 2020-04-23T19:56:57+00:00
> getmonero.org uses Qt 5.9 which does not have automatic high dpi scaling. Self compiled uses Qt 5.14 which has this feature.

Shouldn't the Qt version requirement be pinned in the requirements/provisioning files in the codebase? 

Sorry if I'm sounding completely stupid since I have never worked with Qt before, but I do wonder why the Qt build version would be different for self-built versus the pre-built binary, especially since it claims to be built from the same tag. Is this a build parameter or flag that I can pass to my build as well? This seems a bit strange otherwise.

Thanks for the tips on `QT_SCALE_FACTOR` will play around with that one. However I do feel a bit hesitant to fully trust a pre-built binary for wallets and especially when the output of the same tag seems to differ. Absolutely not doubting anyone's intentions here btw. it's just that as a rule of thumb I tend to be more careful with binaries when it comes to holding currency.


## selsta | 2020-04-23T20:36:08+00:00
> Shouldn't the Qt version requirement be pinned in the requirements/provisioning files in the codebase?

We set 5.9 as minimum version. Newer Qt version are also fine as Qt is backwards compatible for minor releases: https://wiki.qt.io/Qt-Version-Compatibility

> but I do wonder why the Qt build version would be different for self-built versus the pre-built binary, especially since it claims to be built from the same tag. Is this a build parameter or flag that I can pass to my build as well? This seems a bit strange otherwise.

The high dpi thing is an env var we set so that newer Qt versions have high DPI scaling: https://github.com/monero-project/monero-gui/blob/master/src/main/main.cpp#L175

The release binaries use Qt 5.9 which does not support this env var yet, that’s why the behaviour is different.

Note that the font issue does not seem to be a monero-gui bug. I don’t know what the arch repo package does. Most of the issues we had in the past with arch were custom Qt themes. Did you self compile using the arch package or from scratch? Did you install your Qt from arch repo or did you download it from qt.io?

> However I do feel a bit hesitant to fully trust a pre-built binary for wallets and especially when the output of the same tag seems to differ.

Different Qt versions can have different bugs which might result in small visual changes. We can’t control what version someone uses to self compile. We could pin it but that would be an inconvenience with no gain.

## xblackbytesx | 2020-04-23T21:06:18+00:00
> Did you self compile using the arch package or from scratch

I built from scratch using just a git clone on my local machine.

> Did you install your Qt from arch repo or did you download it from qt.io

I'm using the Arch repo version. I might just build another build from scratch using the Qt install from qt.io as I see that this is actually the recommended way of installing Qt.

Other than that I have no custom Qt theme active as far as I can tell. 

Thanks for your fast replies btw. I'll see if I can help out debugging this further by trying some different Qt versions. I'm now also doubting this is an issue with Monero-gui per-se but we might be able to help others out in building successfully from a standard Arch install. Always nice to have the option to produce a reproducible build yourself.

## selsta | 2020-04-23T21:17:17+00:00
> I might just build another build from scratch using the Qt install from qt.io as I see that this is actually the recommended way of installing Qt.

Yep that’s probably the best start to figure this issue out.

## FabioNevesRezende | 2021-02-15T18:18:56+00:00
I'm also having this exact same issue, neither worked: archlinux repo's version and version downloaded from getmonero.org...

## FabioNevesRezende | 2021-02-17T14:32:52+00:00
I've tried building it from source directly and the error stills the same

## selsta | 2021-02-17T14:36:22+00:00
@FabioNevesRezende please see https://github.com/monero-project/monero-gui/issues/3338#issuecomment-779976053

Try (re)installing / updating your graphics drivers and make sure they properly support opengl. 

## lindevel | 2021-11-07T11:22:57+00:00
I have the same on Intel integral graphics
```
$ pacman -Q | grep -iE "monero-gui|^qt5|mesa|vulkan"
lib32-mesa 21.2.4-1
lib32-vulkan-icd-loader 1.2.194-1
lib32-vulkan-intel 21.2.4-1
mesa 21.2.4-1
mesa-demos 8.4.0-4
monero-gui 0.17.2.3-1
qt5-base 5.15.2+kde+r254-1
qt5-declarative 5.15.2+kde+r36-1
qt5-graphicaleffects 5.15.2-1
qt5-imageformats 5.15.2-1
qt5-location 5.15.2-3
qt5-multimedia 5.15.2-1
qt5-networkauth 5.15.2-1
qt5-quickcontrols 5.15.2-1
qt5-quickcontrols2 5.15.2+kde+r8-1
qt5-sensors 5.15.2-1
qt5-speech 5.15.2-1
qt5-svg 5.15.2+kde+r13-1
qt5-wayland 5.15.2+kde+r36-1
qt5-webchannel 5.15.2-1
qt5-webengine 5.15.7-1
qt5-webkit 5.212.0alpha4-10
qt5-x11extras 5.15.2-1
qt5-xmlpatterns 5.15.2-1
vulkan-headers 1:1.2.194-1
vulkan-icd-loader 1.2.194-1
vulkan-intel 21.2.4-1
```
It works for me `env QMLSCENE_DEVICE=softwarecontext monero-wallet-gui`

## selsta | 2021-11-07T17:08:46+00:00
@lindevel can you post a screenshot?

## lindevel | 2021-11-07T19:01:06+00:00
@selsta
![Знімок екрану_2021-11-07_20-45-35](https://user-images.githubusercontent.com/79170599/140658054-c10a037f-e391-4830-a9c1-0ce0507bd52a.png)
![Знімок екрану_2021-11-07_20-48-33](https://user-images.githubusercontent.com/79170599/140658056-dcc65df3-c938-4eb6-9996-138fc6c75fcc.png)
![Знімок екрану_2021-11-07_20-49-11](https://user-images.githubusercontent.com/79170599/140658057-7ed5818d-f3db-419a-b070-5e0a9e9ff3f7.png)
![Знімок екрану_2021-11-07_20-49-21](https://user-images.githubusercontent.com/79170599/140658058-d1fe8278-116b-4303-bba5-221f63f704df.png)

## maltejur | 2021-11-09T19:51:34+00:00
I also have the same behavior, but only when I use some custom fonts via KDE, like [Roboto](https://archlinux.org/packages/community/any/ttf-roboto/). When I use other custom fonts, the interface looks normal but the font also isn't changed. (I tried the version from the arch linux repositories and building from source)

Steps to reproduce:
- Download the latest [Manjaro Minimal KDE ISO](https://manjaro.org/downloads/official/kde/) and boot into live environment in a VM
- Install `monero-gui`: `sudo pacman -Sy monero-gui`
- Start Monero GUI and notice how everything is normal, close it again
- Install `ttf-roboto`: `sudo pacman -S ttf-roboto`
- Go into `System Settings`>`Appearance`>`Fonts`, set `General` to `Roboto` and apply
- Start Monero GUI again and notice how some parts of the UI have weird letters

![image](https://user-images.githubusercontent.com/48161361/140999738-29ac72ed-11b4-4610-8f80-3e5bf8bb64c9.png)


## lindevel | 2021-11-10T08:58:08+00:00
I've tried all "* Regular" fonts on my system with Xfce, works fine with all except "Roboto Regular"

## sylvesterroos | 2021-11-10T09:33:32+00:00
Same here on Arch based KDE Plasma. Got the weird bug with the Roboto font, but it was fixed when I switched to a different one

## selsta | 2021-11-11T00:36:55+00:00
FWIW we use Roboto in Monero GUI as the font, though that doesn't explain why that interferes if someone sets Roboto as their custom font.

## btn21 | 2021-11-12T15:38:32+00:00
I can confirm the weird font issue with Roboto as well. I'm on Arch Linux using the Cinnamon DE.
None of the other fonts I tried presented this bug.

## maltejur | 2021-11-26T22:13:34+00:00
This seems to also have something to do with the font size. Updating the `font.pixelSize` of some of the broken text elements seems to "fix" them. For example in the [`WizardMenuItem.qml`](https://github.com/monero-project/monero-gui/blob/ecf5c501d61bf5f85fb69fd9136cd0235f97f7b8/wizard/WizardMenuItem.qml#L128):
```diff
        MoneroComponents.TextPlain {
            id: body
            Layout.fillWidth: true
            color: MoneroComponents.Style.dimmedFontColor
            font.family: MoneroComponents.Style.fontRegular.name
            font.pixelSize: {
                if(wizardController.layoutScale === 2 ){
-                   return 16;
+                   return 17;
                } else {
                    return 14;
                }
            }
            topPadding: 4
``` 
This will result in:
![image](https://user-images.githubusercontent.com/48161361/143658169-b59c3c95-d36c-40ec-9ba8-8ff0bf946a70.png)

Instead of:
![image](https://user-images.githubusercontent.com/48161361/143658192-238774ae-6a4c-4a9c-a192-2a24166be4ea.png)

Changing `font.family` directly to `Roboto-Regular` also seems to fix the issue.
```diff
        MoneroComponents.TextPlain {
            id: body
            Layout.fillWidth: true
            color: MoneroComponents.Style.dimmedFontColor
-           font.family: MoneroComponents.Style.fontRegular.name
+           font.family: "Roboto-Regular"
            font.pixelSize: {
                if(wizardController.layoutScale === 2 ){
                    return 16;
                } else {
                    return 14;
                }
            }
```

This bug also looks similar to \
https://bugreports.qt.io/browse/QTBUG-63127 \
https://bugreports.qt.io/browse/QTBUG-47399 \
https://bugreports.qt.io/browse/QTBUG-63476 

# Action History
- Created by: susp3c1 | 2020-02-05T08:17:48+00:00
- Closed at: 2021-12-02T06:04:29+00:00
