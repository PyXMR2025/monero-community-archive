---
title: Static build is broken cause of libsodium
source_url: https://github.com/monero-project/monero/issues/6245
author: KeyFiDennis
assignees: []
labels: []
created_at: '2019-12-17T12:14:59+00:00'
updated_at: '2020-05-16T16:05:05+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:05:04+00:00'
---

# Original Description
The build is broken as main as well as fallback site are not available.

`make -j8 depends target=x86_64-linux-gnu`

Error:
```
Fetching libsodium-1.0.16.tar.gz from https://download.libsodium.org/libsodium/releases/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
curl: (22) The requested URL returned error: 404 
Fetching libsodium-1.0.16.tar.gz from https://bitcoincore.org/depends-sources
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
curl: (22) The requested URL returned error: 404 Not Found
funcs.mk:259: recipe for target '/monero/contrib/depends/sources/download-stamps/.stamp_fetched-sodium-libsodium-1.0.16.tar.gz.hash' failed
make[1]: *** [/monero/contrib/depends/sources/download-stamps/.stamp_fetched-sodium-libsodium-1.0.16.tar.gz.hash] Error 22
make[1]: Leaving directory '/monero/contrib/depends'
Makefile:50: recipe for target 'depends' failed
make: *** [depends] Error 2
``` 
Cause:
libsodium-1.0.16 is outdated and was moved on the release site. The backup https://bitcoincore.org/depends-sources does not exist.

Fix:
Either upgade https://github.com/monero-project/monero/blob/master/contrib/depends/packages/sodium.mk to a newer release or change
`$(package)_download_path=https://download.libsodium.org/libsodium/releases/`
to
`$(package)_download_path=https://download.libsodium.org/libsodium/releases/old`

# Discussion History
## selsta | 2019-12-17T12:15:58+00:00
#6231 

## KeyFiDennis | 2019-12-17T13:07:52+00:00
Added comment to your pull request for the specific fix.

The fallback to `https://bitcoincore.org/depends-sources` should be removed/changed its a broken link.

## moneromooo-monero | 2020-05-16T16:05:04+00:00
Fixed

# Action History
- Created by: KeyFiDennis | 2019-12-17T12:14:59+00:00
- Closed at: 2020-05-16T16:05:04+00:00
