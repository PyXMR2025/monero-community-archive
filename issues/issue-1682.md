---
title: GUI 0.13.0.3 crashes on launch on macOS due to missing library
source_url: https://github.com/monero-project/monero-gui/issues/1682
author: rex4539
assignees: []
labels:
- resolved
created_at: '2018-10-18T18:59:19+00:00'
updated_at: '2018-10-19T11:18:23+00:00'
type: issue
status: closed
closed_at: '2018-10-19T11:18:23+00:00'
---

# Original Description
macOS 10.13.6 (17G3020)

```
Termination Reason:    DYLD, [0x1] Library missing

Application Specific Information:
dyld: launch, loading dependent libraries

Dyld Error Message:
  Library not loaded: /usr/local/Cellar/openssl/1.0.2p/lib/libcrypto.1.0.0.dylib
  Referenced from: /Applications/monero-wallet-gui.app/Contents/Frameworks/libssl.1.0.0.dylib
  Reason: image not found
```

[monero-wallet-gui_2018-10-18-214832_MacBook-Pro-2011.log](https://github.com/monero-project/monero-gui/files/2493231/monero-wallet-gui_2018-10-18-214832_MacBook-Pro-2011.log)


# Discussion History
## rex4539 | 2018-10-18T19:02:42+00:00
Looks like the path is hardcoded.

## sanderfoobar | 2018-10-18T22:03:48+00:00
The problem was already identified. The fix will be in `.4` that is due soon. The build template for OSX was misconfigured. `brew install openssl` for those that can't wait.

Thanks for reporting!

## dEBRUYNE-1 | 2018-10-19T11:10:59+00:00
Duplicate of #1658. This particular issue will be fixed in GUI v0.13.0.4. In addition, a temporary workaround can be found here:

https://monero.stackexchange.com/questions/10364/gui-v0-13-0-3-does-not-start-on-mac-os-x-monero-wallet-gui-cannot-be-opened-bec

## dEBRUYNE-1 | 2018-10-19T11:11:04+00:00
+resolved

# Action History
- Created by: rex4539 | 2018-10-18T18:59:19+00:00
- Closed at: 2018-10-19T11:18:23+00:00
