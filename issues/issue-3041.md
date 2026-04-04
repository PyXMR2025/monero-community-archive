---
title: Compilation GUI for Windows
source_url: https://github.com/monero-project/monero-gui/issues/3041
author: gvozdi1234
assignees: []
labels: []
created_at: '2020-08-15T11:21:42+00:00'
updated_at: '2020-08-26T23:19:45+00:00'
type: issue
status: closed
closed_at: '2020-08-26T23:09:19+00:00'
---

# Original Description

 I'm trying to compile GUI for Windows as described here https://github.com/monero-project/monero-gui. After execution "make deploy" I'm getting the error (see screenshot). How to fix it? Is there another way to compile it?
![Untitled](https://user-images.githubusercontent.com/69717319/90311569-9b281e80-deeb-11ea-9632-626d0db4f09d.png)

Also tried executing "windeployqt C:/msys64/home/Administrator/monero-gui/build/release/bin/monero-wallet-gui.exe -no-translations -qmldir=C:/msys64/home/Administrator/monero-gui", got error when launching compiled exe (screenshot 2)
![Untitled-2](https://user-images.githubusercontent.com/69717319/90311555-88154e80-deeb-11ea-9bb1-b3fcad5e9f88.png)


# Discussion History
## selsta | 2020-08-15T11:33:48+00:00
Can you drag and drop the screenshot here into Github?

## gvozdi1234 | 2020-08-15T11:37:23+00:00
> Can you drag and drop the screenshot here into Github?

Attached

## selsta | 2020-08-15T11:54:09+00:00
Seems to be similar to https://github.com/monero-project/monero-gui/issues/3021

As an (unsatisfying) workaround you can start the GUI directly from the mingw64 console and skip the deploy step.

## italocoin-project | 2020-08-22T13:29:40+00:00
Hello, i face the same issue, any updates on this?

## italocoin-project | 2020-08-22T13:42:21+00:00
I found the issue comes from QT https://forum.qt.io/topic/109779/windeployqt-exe-comes-with-qt-5-14-not-copy-the-dlls-to-the-app-directory/6

## selsta | 2020-08-26T23:09:19+00:00
Will be fixed with #3047

Edit: Sorry for closing early, should be merged in the next days.

# Action History
- Created by: gvozdi1234 | 2020-08-15T11:21:42+00:00
- Closed at: 2020-08-26T23:09:19+00:00
