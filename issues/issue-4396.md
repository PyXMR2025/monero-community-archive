---
title: v0.18.3.4 total fail, nothing works, what gives
source_url: https://github.com/monero-project/monero-gui/issues/4396
author: nomisma-qt
assignees: []
labels: []
created_at: '2025-01-08T17:43:03+00:00'
updated_at: '2025-01-08T18:29:27+00:00'
type: issue
status: closed
closed_at: '2025-01-08T18:28:52+00:00'
---

# Original Description
.appimage is bad, the binary is all over the place, what is up? linux.
Why release at all?

# Discussion History
## selsta | 2025-01-08T17:45:15+00:00
Please explain in more detail what exactly is fails.

The mock .appimage is used so that it can be started from a file explorer, some distros don't allow starting binariers directly.

## nomisma-qt | 2025-01-08T17:57:00+00:00
executing the appimage results in a error message saying 'not an appimage'

executing the binary results in a screenfull of:

`$ ./monero-wallet-gui
2025-01-08 17:56:03.431 W Qt:5.15.14 GUI:- | screen: 3840x2160 - available: QSize(3840, 2106) - dpi: 120 - ratio:1.09334
2025-01-08 17:56:05.108 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.108 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.108 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.108 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.108 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.108 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.108 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.108 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.137 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.137 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.144 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.144 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.144 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.144 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.144 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.144 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.144 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.144 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.163 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.163 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.602 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.611 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.611 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.611 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.611 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.611 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.611 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.611 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.611 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.799 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.800 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.800 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.800 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.800 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.800 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.800 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.800 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.800 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.800 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2025-01-08 17:56:05.907 W Logging to "/home/user/.bitmonero/monero-wallet-gui.log"
2025-01-08 17:56:05.909 W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
`

## nomisma-qt | 2025-01-08T18:19:55+00:00
> Please explain in more detail what exactly is fails.
> 
> The mock .appimage is used so that it can be started from a file explorer, some distros don't allow starting binariers directly.

now why the hell would you create a mock .appimage? what is wrong with a real appimage?

## selsta | 2025-01-08T18:23:34+00:00
> executing the binary results in a screenfull of:

None of these are errors, what is the exact issue you are having here?

> now why the hell would you create a mock .appimage?

I already explained it. Some people don't know how to start programs from the terminal and prefer to double click something from the file explorer. Ubuntu for example doesn't allow starting binariers directly from the file explorer so this workaround is used.

> what is wrong with a real appimage?

Nothing is wrong with it, it's just not something we use.


## nomisma-qt | 2025-01-08T18:27:08+00:00
some people? You either release a working appimage, or you don't.

Don't provide a webpage with a link to a linux appimage, if you don't intend to provide a god damn appimage.

## selsta | 2025-01-08T18:28:52+00:00
Try to use featherwallet if you want a real appimage.

## nomisma-qt | 2025-01-08T18:29:26+00:00
here we go with the attitude again. Thanks and bye.

# Action History
- Created by: nomisma-qt | 2025-01-08T17:43:03+00:00
- Closed at: 2025-01-08T18:28:52+00:00
