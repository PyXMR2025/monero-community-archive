---
title: OSX Dev setup
source_url: https://github.com/monero-project/monero-gui/issues/101
author: rstormsf
assignees: []
labels: []
created_at: '2016-11-02T23:52:32+00:00'
updated_at: '2016-11-13T17:58:48+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:58:48+00:00'
---

# Original Description
Does anyone have tried to build the GUI on OSX? 
If so, please advice what you have done and what am I missing.

It seems to me that all PRs are failing for OSX10.11 and 10.12 due to some issue in OSX environment. 

I'm trying to build it myself and also facing the issues.

The first issue was in Qt that needed to change a string from `xcrun` to `xcodebuild`(source: [link](https://stackoverflow.com/questions/33728905/qt-creator-project-error-xcode-not-set-up-properly-you-may-need-to-confirm-t) )

The second issue was that in `libwalletqt` folder it was expecting to have [wallet](https://github.com/monero-project/monero/tree/master/src/wallet) folder from actual monero project that has a file  `wallet2_api.h` I symlinked the folder and build started running, but

The third issue that I see now is 
```
d: warning: directory not found for option '-L/YOUR_PATH/monero-core/monero/lib'
ld: library not found for -lwallet_merged
```
Let me know if someone is using OSX to build monero-core

**UPDATE:**
I was pointed out that I'd need run `./get_libwallet_api.sh` first and then run `build.sh`
which solves some problems.
Before that, you also need to have openssl headers installed

**Update**: 
All is working, so I'll update readme.md for osx setup to
1)`brew install openssl`
2)add `-L/usr/local/opt/openssl/lib \` in here
https://github.com/monero-project/monero-core/blob/master/monero-core.pro#L133-L134
3)run `./get_libwallet_api.sh`
4)run `./build.sh`

# Discussion History
## ghost | 2016-11-03T06:51:55+00:00
I'm running OSX 10.11.6 and I have similar issues. I'm not sure for what version of MacOS the build scripts has been initial written for.

On my local installation, i have added the following path in the monero-core.pro file:

```
-L/usr/local/opt/openssl/lib \
-L/usr/local/opt/boost159/lib \
```

`brew` installs the libraries under `/usr/local/opt/[library]` (which is symlinked to `/usr/local/Cellar/[library]`, so I had to add these paths to the file.

The other problem I had was the `boost` library. The build doesn't work with `boost` version 1.62. I got the following errors:

```
Undefined symbols for architecture x86_64:
  "boost::re_detail::get_mem_block()", referenced from:
...
```

So I have installed `boost` 1.59 with `brew install homebrew/versions/boost159 --c++11` , and now the build works without problems.


## fluffypony | 2016-11-13T17:58:48+00:00
Closing as fixed


# Action History
- Created by: rstormsf | 2016-11-02T23:52:32+00:00
- Closed at: 2016-11-13T17:58:48+00:00
