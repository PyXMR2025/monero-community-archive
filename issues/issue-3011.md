---
title: 'Docker static builds: undefined reference to symbol ''xcb_glx_id'''
source_url: https://github.com/monero-project/monero-gui/issues/3011
author: tobtoht
assignees: []
labels: []
created_at: '2020-07-14T19:09:23+00:00'
updated_at: '2020-07-29T14:51:25+00:00'
type: issue
status: closed
closed_at: '2020-07-29T14:51:25+00:00'
---

# Original Description
`docker run --rm -it -v $(pwd):/monero-gui -w /monero-gui monero:build-env-gui sh -c 'USE_SINGLE_BUILDDIR=ON DEV_MODE=ON make release-static -j4'` fails with:

```
[ 78%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qrc_translations.cpp.o
[ 78%] Linking CXX executable ../bin/monero-wallet-gui
/usr/bin/ld: /usr/plugins/xcbglintegrations/libqxcb-glx-integration.a(qxcbglxintegration.o): undefined reference to symbol 'xcb_glx_id'
//usr/lib/x86_64-linux-gnu/libxcb-glx.so.0: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
src/CMakeFiles/monero-wallet-gui.dir/build.make:1554: recipe for target 'bin/monero-wallet-gui' failed
```

Tested on current master (b7b1221) and Docker version 19.03.12

# Discussion History
## xiphon | 2020-07-14T19:40:41+00:00
It can't be `docker build ...` output, the step doesn't build Monero GUI. Please double check this.

## tobtoht | 2020-07-14T19:55:07+00:00
My bad, I copied the wrong command. I have updated the issue.

## xiphon | 2020-07-14T20:06:11+00:00
Could you try to `rm -rf build` directory and run the build again?

## tobtoht | 2020-07-14T20:35:22+00:00
I tried that just now, the issue is still there.

## tobtoht | 2020-07-14T20:40:35+00:00
Full build logs: https://paste.debian.net/plainh/6343a879

## xiphon | 2020-07-15T23:27:35+00:00
Could you please test the fix? https://github.com/monero-project/monero-gui/pull/3015

## tobtoht | 2020-07-15T23:47:44+00:00
Thanks for taking the time to look into this. 

The build succeeds now.

# Action History
- Created by: tobtoht | 2020-07-14T19:09:23+00:00
- Closed at: 2020-07-29T14:51:25+00:00
