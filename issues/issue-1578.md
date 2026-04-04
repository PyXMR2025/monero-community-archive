---
title: version numbers missing on macOS
source_url: https://github.com/monero-project/monero-gui/issues/1578
author: core-code
assignees: []
labels:
- Hacktoberfest
created_at: '2018-10-01T18:35:47+00:00'
updated_at: '2020-02-20T03:10:00+00:00'
type: issue
status: closed
closed_at: '2020-02-20T03:10:00+00:00'
---

# Original Description

i've downloaded Version '0.12.3.0' but when selecting it in the Finder and using 'Get Info' it doesn't show any Version-number at all. i guess the **CFBundleVersion** and **CFBundleShortVersionString** entries in your **Info.plist** file are missing.
all apps on macOS are supposed to contain valid version information.


# Discussion History
## pazos | 2018-10-04T17:57:48+00:00
@core-code: yes, both keys are missing on [our Info.plist](https://github.com/monero-project/monero-gui/blob/master/share/Info.plist). A few months ago, before using our own template instead of qmake generated one I proposed [adding versioning support](https://github.com/monero-project/monero-gui/pull/1313) based on github commits. You can give it a try or propose another way of pulling the version automatically.

Anyways, you can check the version from the running gui, so it shouldn't matter.

## core-code | 2018-10-04T19:00:17+00:00
well i think there are several reasons it matters:
• users don't need to launch the app to check the installed version
• users don't need to update manually but can use third party updater apps like MacUpdater
• only the version information from the CFBundleVersion key can be used by the operating system which is helpful e.g. if you have multiple versions installed. hiding something in the app has no use to any outside consumers

## pazos | 2018-10-04T19:27:32+00:00
> well i think there are several reasons it matters:
• users don't need to launch the app to check the installed version
• users don't need to update manually but can use third party updater apps like MacUpdater
• only the version information from the CFBundleVersion key can be used by the operating system which is helpful e.g. if you have multiple versions installed. hiding something in the app has no use to any outside consumers.

I agree with you.

 A manual version should be trivial to implement, but an automatic version tagger would be preferred.

BTW, nice software @core-code. I'm a fan of your UninstallPKG app. 

## core-code | 2018-10-04T19:29:37+00:00
> A manual version should be trivial to implement, but an automatic version tagger would be preferred.

you are right its quite easy to forget updating prior to a release unless you follow strict procedure

> I'm a fan of your UninstallPKG app.

thanks! dark-mode update coming soon ;)

## erciccione | 2018-10-06T15:50:46+00:00
+hacktoberfest

## selsta | 2020-02-13T02:50:46+00:00
#2773 should solve this.

# Action History
- Created by: core-code | 2018-10-01T18:35:47+00:00
- Closed at: 2020-02-20T03:10:00+00:00
