---
title: UI is inaccessible to accessibility clients
source_url: https://github.com/monero-project/monero-gui/issues/4020
author: ethindp
assignees: []
labels: []
created_at: '2022-09-02T19:17:40+00:00'
updated_at: '2022-10-02T20:40:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As it currently stands, the Monero UI for `monero-wallet-gui` is completely inaccessible to accessibility clients. An "accessibility client" is a program that interacts with accessibility frameworks to act as assistive technology, such as screen readers. There are a number of things that can cause this:

* The user interface may be drawn using technologies such as OpenGL, Vulkan, Metal, etc.
* The user interface might use custom components and not components provided by the UI framework (in this case, QT).

QT provides accessibility through classes such as [QAccessible](https://doc.qt.io/qt-5/qaccessible.html). An application need only implement the [QAccessibleInterface](https://doc.qt.io/qt-5/qaccessibleinterface.html) class (or its derivatives, [QAccessibleObject](https://doc.qt.io/qt-5/qaccessibleobject.html) and [QAccessibleWidget](https://doc.qt.io/qt-5/qaccessiblewidget.html)). I am curious if the Monero community would be interested in implementing any of these interfaces. More information about accessibility in QT can be found [here](https://doc.qt.io/qt-5/accessible-qwidget.html). I would do it myself, but it appears that all of the components are implemented through QML, something I am not particularly knowledgable about (I generally prefer building UIs through code because UI editors for QT aren't accessible to the screen readers I use). Though I certainly don't mind using a wallet like [Feather](https://featherwallet.org), having the Monero wallet as an option would be quite nice. I really hope that we can make the Monero GUI wallet accessible together! :)

# Discussion History
## selsta | 2022-10-02T20:34:43+00:00
QML does support accessibility and we have added it for example on the "Open wallet from file" screen. There are a couple PRs open that improve accessibility in other places but it is a lot of work, not only to program but also to review. @rating89us did great work there but I'm simply behind with reviewing.

## ethindp | 2022-10-02T20:40:05+00:00
@selsta I'm not familiar enough with QML to add accessibility myself, otherwise I would. It shouldn't be overly difficult, so long as you stick to native QT widgets. Its making custom widgets that presents a significant difficulty, particularly since you need to implement QAccessible/QAccessibleWidget/etc.

# Action History
- Created by: ethindp | 2022-09-02T19:17:40+00:00
