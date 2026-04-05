---
title: Color output issue on macOS if config file is used
source_url: https://github.com/xmrig/xmrig/issues/281
author: fonix232
assignees: []
labels: []
created_at: '2017-12-21T13:00:30+00:00'
updated_at: '2018-11-05T07:03:46+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:03:46+00:00'
---

# Original Description
If I start xmrig with just a config file (no matter if it's the default config path or with `-c`, I get the basic, colorless output. The config file specifies that it is indeed intended to be a color output (the property `colors` is set to `true`), however I'm getting colorless output. If I apply the same settings via command line parameters, colors work just fine.

Versions: XMRig/2.4.3 libuv/1.18.0 clang/9.0.0

# Discussion History
## namsur1234 | 2017-12-30T06:24:35+00:00
I also have a similar problem with no color. Color is present if there is no log file specified in json config file.
VERSIONS:     XMRig/2.4.3-beta2 libuv/1.14.1 OpenCL/2.0 MSVC/2017
Just noticed this is for CPU, not sure if that's an issue for me but it certainly is on AMD cards so I opened an issue there. I'm guessing the same code runs color for everything so i bet they all have an issue. I also noticed that pressing "h" would print the hashrate, pause the output and then it would stop/crash.

Edit: I've confirmed enabling logging via .cmd or .json file causes color output to be disabled for CPU mining.

# Action History
- Created by: fonix232 | 2017-12-21T13:00:30+00:00
- Closed at: 2018-11-05T07:03:46+00:00
