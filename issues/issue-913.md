---
title: '[BUILD][OSX]: install_name_tool can''t open file libssl.1.0.0.dylib'
source_url: https://github.com/monero-project/monero-gui/issues/913
author: danrmiller
assignees: []
labels:
- bug
- resolved
created_at: '2017-10-23T03:19:36+00:00'
updated_at: '2018-11-18T14:00:35+00:00'
type: issue
status: closed
closed_at: '2018-11-18T14:00:35+00:00'
---

# Original Description
@Jaqueeee Where in the build process is libssl.1.0.0.dylib supposed to be copied to build/release/bin/monero-wallet-gui.app/Contents/Frameworks? 

I'm getting [this](https://build.getmonero.org/builders/monero-core-osx-10.12/builds/915/steps/link/logs/stdio) error:
```
error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/install_name_tool: can't open file: build/release/bin/monero-wallet-gui.app/Contents/Frameworks/libssl.1.0.0.dylib (No such file or directory)
```
on the step that runs this:
```
install_name_tool -change /usr/local/Cellar/openssl/1.0.2j/lib/libcrypto.1.0.0.dylib @executable_path/../Frameworks/libcrypto.1.0.0.dylib build/release/bin/monero-wallet-gui.app/Contents/Frameworks/libssl.1.0.0.dylib
```
I was looking into an unrelated error building the daemon on this machine with the newly added ssl support and did update the brew package, so I think that's what broke this.
 
I also tried /usr/local/Cellar/openssl/1.0.2l/lib/libcrypto.1.0.0.dylib (1.02.l instead of j) which also exists but get the same error. 




# Discussion History
## dEBRUYNE-1 | 2017-10-27T13:42:07+00:00
+bug

## Jaqueeee | 2017-10-28T06:38:48+00:00
@danrmiller I think the libs are copied by macdeployqt when running `make deploy`.
https://github.com/monero-project/monero-core/blob/master/monero-wallet-gui.pro#L377

## danrmiller | 2017-10-31T04:14:16+00:00
@Jaqueeee Thanks. Here is more verbose output of the "make deploy"/macdeployqt step, and I don't see libssl

https://build.getmonero.org/builders/monero-core-osx-10.12/builds/959/steps/deploy/logs/stdio


## erciccione | 2018-11-18T13:59:56+00:00
Related to old version. Please reopen if bug still exists

+resolved

# Action History
- Created by: danrmiller | 2017-10-23T03:19:36+00:00
- Closed at: 2018-11-18T14:00:35+00:00
