---
title: Immediate Crash on Launch with Qt Quick Errors and OpenGL Context Failure in
  monero-wallet-gui
source_url: https://github.com/monero-project/monero/issues/9300
author: Kudzu-glitch
assignees: []
labels: []
created_at: '2024-04-22T00:42:11+00:00'
updated_at: '2024-04-22T01:37:46+00:00'
type: issue
status: closed
closed_at: '2024-04-22T01:37:46+00:00'
---

# Original Description
I would like to report an issue I am having with `monero-wallet-gui` in case it is a bug of some kind. I am not really a programmer, so please let me know if there is additional helpful information I can provide. Meantime, `monero-wallet-cli` is still working for me.

## Environment
- **OS**: Arch Linux x86_64
- **Kernel**: 6.8.7-hardened1-2-hardened
- **Monero GUI Version**: 0.18.3.3-1
- **Qt Version**: 5.15.13+kde+r145-1
- **GPU**: NVIDIA GeForce GTX 1660 SUPER
- **NVIDIA Driver Version**: 550.76-1
- **Resolution**: 3840x1080 (dual 1920x1080)

## Description
When attempting to start `monero-wallet-gui`, the icon appears in the taskbar briefly (approximately 1-2 seconds) before a second icon appears (< 1 second), then the both disappear before the window initializes.

When I run `monero-wallet-gui` from the command line, I get the following:

```bash
$ monero-wallet-gui
2024-04-22 00:12:15.776 W Qt:5.15.13 GUI:- | screen: 1920x1080 - available: QSize(1920, 1080) - dpi: 96 - ratio:0.717139
2024-04-22 00:12:16.073 W QGLXContext: Failed to create dummy context
2024-04-22 00:12:16.741 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.742 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.742 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.742 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.742 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.742 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.742 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.742 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.778 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.778 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.796 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.796 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.796 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.796 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.796 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.796 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.796 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.796 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.827 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:16.827 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.174 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.191 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.191 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.191 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.191 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.191 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.191 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.191 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.191 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.420 W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-04-22 00:12:17.463 W Logging to "/home/nathan/.bitmonero/monero-wallet-gui.log"
2024-04-22 00:12:17.465 W file:///usr/lib/qt/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2024-04-22 00:12:17.483 E Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags<QSurfaceFormat::FormatOption>(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior QSurfaceFormat::DoubleBuffer, swapInterval 1, colorSpace QSurfaceFormat::DefaultColorSpace, profile  QSurfaceFormat::NoProfile) 
```

Checking `monero-wallet-gui.log`, I see:

```bash
2024-04-22 00:08:39.887	    6a36823c1000	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-04-22 00:08:39.887	    6a36823c1000	WARNING	frontend	src/wallet/api/wallet.cpp:411	Logging to "/home/nathan/.bitmonero/monero-wallet-gui.log"
2024-04-22 00:08:39.896	    6a36823c1000	WARNING	frontend	src/wallet/api/wallet.cpp:411	file:///usr/lib/qt/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2024-04-22 00:08:39.940	    6a36823c1000	ERROR	frontend	src/wallet/api/wallet.cpp:415	Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags<QSurfaceFormat::FormatOption>(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior QSurfaceFormat::DoubleBuffer, swapInterval 1, colorSpace QSurfaceFormat::DefaultColorSpace, profile  QSurfaceFormat::NoProfile)
```
## Additional Information
- No core dumps were generated (`COREFILE: none` reported by `coredumpctl`).
- Attempts to run under gdb did not yield useful debugging information due to lack of debugging symbols.
- Monero GUI was working fine until recent system update, but I don't know exactly when it broke


# Discussion History
## Kudzu-glitch | 2024-04-22T01:37:46+00:00
After rebooting the computer, the issue is gone. Feel a bit silly, really.

# Action History
- Created by: Kudzu-glitch | 2024-04-22T00:42:11+00:00
- Closed at: 2024-04-22T01:37:46+00:00
