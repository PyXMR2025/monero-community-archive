---
title: I build fail on windows and OSx
source_url: https://github.com/monero-project/monero-gui/issues/2698
author: ScottGold
assignees: []
labels:
- duplicate
created_at: '2020-01-06T10:05:13+00:00'
updated_at: '2020-02-13T02:45:45+00:00'
type: issue
status: closed
closed_at: '2020-02-13T02:45:45+00:00'
---

# Original Description
**message on windows :**
Project MESSAGE: Host is 64bit
Project MESSAGE: Target is 32bit
Project MESSAGE: This project is using private headers and will therefore be tied to this specific Qt module build version.
Project MESSAGE: Running this project against other versions of the Qt modules may crash at any arbitrary point.
Project MESSAGE: This is not a bug, but a result of using Qt internals. You have been warned!
Project MESSAGE: Host is 64bit
Project MESSAGE: Target is 32bit
Project MESSAGE: Host is 64bit
Project MESSAGE: Target is 32bit
WARNING: Failure to find: debug/monero-wallet-gui_resource_res.o
make[1]: *** 没有规则可制作目标“../../../../../msys64/mingw64/include/QtWidgets/QApplication”，由“release/main.o” 需求。 停止。
make: *** [Makefile:38：release] 错误 2

**message on OSx**
Sorry, macx is ok now, it's my fault, It need build monero first, which install the dependencies.


# Discussion History
## selsta | 2020-02-13T02:43:16+00:00
#2617

+duplicate

# Action History
- Created by: ScottGold | 2020-01-06T10:05:13+00:00
- Closed at: 2020-02-13T02:45:45+00:00
