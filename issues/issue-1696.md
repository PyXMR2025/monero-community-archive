---
title: Android Gui frozen
source_url: https://github.com/monero-project/monero-gui/issues/1696
author: twiuglufosfa
assignees: []
labels: []
created_at: '2018-10-23T12:54:07+00:00'
updated_at: '2019-02-01T18:29:29+00:00'
type: issue
status: closed
closed_at: '2019-02-01T18:29:29+00:00'
---

# Original Description
i achieved to compile for android armv8 but apk created and installed
correctly is useless.

frozen menus,not all menu visible etc.

qt5.11 version.

any proposal??

# Discussion History
## sanderfoobar | 2018-10-24T13:36:37+00:00
The UI is not 100% suited for mobile yet. The alternatives at this point in time are Cake wallet and Monerujo.

## twiuglufosfa | 2018-10-25T05:40:06+00:00
why gui is working very well on windows,linux etc.

is strange that is so useless on android.

i test it on different android phones.

same behaviour.

maybe is time to use smth else and not qt?

## pazos | 2018-12-18T18:35:05+00:00
@twiuglufosfa: It is not useless, but needs a bit of love.

Did you type `cd build && make deploy` ???

## pazos | 2018-12-18T18:39:09+00:00
most of our app are a bunch of scripts (everything qml). We need to copy them on the application (this is the deploy stage) before distribution. Since there is no official build for android you may think that doesn't work because you can't compare, like you can do on desktop systems.

Once you deploy the application it will work (with a bunch of "UI" problems, but everything "core" should work as is)


## twiuglufosfa | 2018-12-19T01:03:31+00:00
of course i did cd build&&make deploy and apk is created.

there are no tabs (u want screenshot?)
only one fixed menu

maybe androiddeployqt is not working well.
after make deploy i have

"Skipping /opt/android/Qt-5.11/plugins/platforms/libqwebgl.so. It has unmet dependencies: lib/libQt5WebSockets.so.
  -- Skipping /opt/android/Qt-5.11/plugins/iconengines/libqsvgicon.so. It has unmet dependencies: lib/libQt5Svg.so.
  -- Skipping /opt/android/Qt-5.11/plugins/imageformats/libqsvg.so. It has unmet dependencies: lib/libQt5Svg.so."

# Action History
- Created by: twiuglufosfa | 2018-10-23T12:54:07+00:00
- Closed at: 2019-02-01T18:29:29+00:00
