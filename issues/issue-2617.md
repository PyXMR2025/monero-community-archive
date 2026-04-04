---
title: WIndows compile error
source_url: https://github.com/monero-project/monero-gui/issues/2617
author: FinOdyaks8
assignees: []
labels: []
created_at: '2019-12-16T10:44:46+00:00'
updated_at: '2021-04-13T23:52:31+00:00'
type: issue
status: closed
closed_at: '2021-04-13T23:52:31+00:00'
---

# Original Description
Hello,

compile stops almost in the end

"C:\msys64\mingw64\bin\windres.exe: monero-wallet-gui_resource.rc:6: syntax error
make[1]: *** [Makefile.Release:469: release/monero-wallet-gui_resource_res.o] Error 1
make[1]: Leaving directory '/e/monero-gui/build'
make: *** [Makefile:38: release] Error 2

on linux compile is successful

there is no change anywhere just git clone and ./build.sh release-static

# Discussion History
## ScottGold | 2020-01-05T06:06:34+00:00
I have the almost same problem.

C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_zu.ts -qm C:/dev/bitcoin-0.18/monero-gui/build/translations/monero-core_zu.qm
Updating 'C:/dev/bitcoin-0.18/monero-gui/build/translations/monero-core_zu.qm'...
Removing translations equal to source text in 'C:/dev/bitcoin-0.18/monero-gui/build/translations/monero-core_zu.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 648 untranslated source text(s)
windres -i monero-wallet-gui_resource.rc -o release/monero-wallet-gui_resource_res.o --include-dir=. -DUNICODE -D_UNICODE -DWIN32 -DMINGW_HAS_SECURE_API=1 -DQT_NO_DEBUG -DQT_SVG_LIB -DQT_WIDGETS_LIB -DQT_QUICK_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -DQT_NEEDS_QMAIN
make[1]: Leaving directory“/c/dev/bitcoin-0.18/monero-gui/build”



## selsta | 2020-01-23T16:25:09+00:00
Can reproduce the issue here: https://github.com/monero-project/monero-gui/runs/405327392

## selsta | 2020-01-24T11:47:10+00:00
@FinOdyaks8 @ScottGold Did you git clone the repository? Or did you use the .zip from Github?

## selsta | 2021-04-13T23:52:31+00:00
We use a new build system. Reopen if this issue still exists.

# Action History
- Created by: FinOdyaks8 | 2019-12-16T10:44:46+00:00
- Closed at: 2021-04-13T23:52:31+00:00
