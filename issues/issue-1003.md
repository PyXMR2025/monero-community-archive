---
title: '[MINOR] Debug info highlighting flaw'
source_url: https://github.com/monero-project/monero-gui/issues/1003
author: 1337tester
assignees: []
labels:
- resolved
created_at: '2017-12-08T11:31:13+00:00'
updated_at: '2018-01-11T13:45:13+00:00'
type: issue
status: closed
closed_at: '2018-01-11T13:45:13+00:00'
---

# Original Description
**Problem:**
'Debug info' text highlighted text stays after highlighting another part of the info (should disappear and allow only the last part to be highlighted)

![debug_info](https://user-images.githubusercontent.com/6553766/33764038-174467fa-dc13-11e7-844d-f6e33beff05d.jpg)

Distro: Ubuntu 17.10


# Discussion History
## Timo614 | 2017-12-08T17:07:20+00:00
Taking a look into this but I think this bug may be biting us: https://bugreports.qt.io/browse/QTBUG-50587

http://doc.qt.io/qt-5/qml-qtquick-textedit.html#persistentSelection-prop with QT 5 it's set to false by default so it should prevent multiple selections across these components. It looks like when readonly is set to true, however, this isn't the case. I set readonly to false locally and was able to see the correct select behavior in action. I'd wager when it's readonly it never has focus so it never loses it when the mouse is clicked off of the component so it doesn't trigger this logic.

https://github.com/monero-project/monero-gui/blob/master/pages/Settings.qml#L483
https://github.com/monero-project/monero-gui/blob/master/components/TextBlock.qml#L3

I'll look into the ramifications of switching this to some other component outside TextEdit given our use case of using this like a label. I'm not sure if we intended to use TextEdit here for some reason though but I'll call that out in a PR once I figure out the right component (new to QT).

## Timo614 | 2017-12-08T18:42:48+00:00
I assume we're using the TextEdit for the rich formatting features. I was able to find a workaround until QT fixes that bug. I listen on the `onFocusChanged` event and if the focus has been lost I call the `deselect()` method which removes the selection. I've been playing with it locally for a little bit and seems to mimic the same behavior as `persistentSelection: false` for a non `readonly: true` TextEdit component.

I'll file up a PR for this change shortly but should fix the selection issue without losing any functionality we're relying on for this component until QT is able to get a bugfix out.

## medusadigital | 2017-12-13T12:06:05+00:00
link: https://github.com/monero-project/monero-gui/issues/960

however keeping both open for now, since the windows specific issue in https://github.com/monero-project/monero-gui/issues/960 is still open afaik.


thx for the work guys <3

## medusadigital | 2018-01-11T13:40:16+00:00
closing in favour of https://github.com/monero-project/monero-gui/issues/960

fiy is here: https://github.com/monero-project/monero-gui/pull/952

## medusadigital | 2018-01-11T13:40:24+00:00
+resolved

# Action History
- Created by: 1337tester | 2017-12-08T11:31:13+00:00
- Closed at: 2018-01-11T13:45:13+00:00
