---
title: '"QtMultimedia not found" while it is installed'
source_url: https://github.com/monero-project/monero-gui/issues/474
author: voidzero
assignees: []
labels: []
created_at: '2017-02-15T20:59:13+00:00'
updated_at: '2017-03-29T22:37:45+00:00'
type: issue
status: closed
closed_at: '2017-03-29T22:37:45+00:00'
---

# Original Description
I had to revert commit 93d2eb5e1a0 because, even though I got monero-core to compile (after jumping through some hoops related to my other issue re libepee), when I start it I get the message that QtMultimedia can't be found, while it is installed. Version 5.6.2 on Linux x64 (Funtoo, a Gentoo derivative).

I don't exactly know why I'm being told that QtMultimedia can't be found - somewhere I read that it might have to do with an optional dependency on gstreamer 0.10. I don't have that installed, because it's too old and pulls in a number of other dependencies I'd rather not use.

After reverting this commit, I can run monero-core succesfully again.

# Discussion History
## moneromooo-monero | 2017-02-19T18:34:48+00:00
Did you run qmake again ? Do you have an older version of qtmultimedia ?

## voidzero | 2017-02-19T20:24:38+00:00
qmake is being executed from build.sh - QtMultimedia as stated is version 5.6.2..

## glv2 | 2017-02-27T16:50:12+00:00
Have you checked that *qtmultimedia* is compiled with the *qml* USE flag activated?

Also on my Gentoo system, I must compile using the command ```QT_SELECT=5 ./build.sh```. If I don't indicate the Qt version to use explicitly, it tries to use the Qt4 version of binaries and libraries.


## voidzero | 2017-03-03T00:11:41+00:00
@glv2 it seems that I didn't enable the qml USE flag. Thanks for the tip. Regarding the QT_SELECT env var, I didn't know about that. I always just changed the qmake line to point to `/usr/lib/qt5/bin/qmake`. I'll try that suggestion too and update this issue again in a bit. Much thanks. :+1: 

## voidzero | 2017-03-03T01:11:27+00:00
Ok. Cool. This fixed it. Thumbs up, @glv2.

@moneromooo-monero could you add a comment into the README about these two things... Gentoo users need to enable the "qml" USE flag, and need to run `QT_SELECT=5 ./build.sh` or something similar?

Which reminds me.. since my shell is zsh and the script doesn't play nice with zsh, what I run is actually `env QT_SELECT=5 SHELL=/bin/bash ./build.sh` -- because even though build.sh contains a hashbang pointing to /bin/bash, it also uses $SHELL which is the problematic part because this var is not changed upon invocation. Ideally the hashbang would contain `#!/usr/bin/env bash` and instead of `$SHELL`, simply `bash` should be used.

## moneromooo-monero | 2017-03-18T08:57:25+00:00
It'd be best if you  (or someone with Gentoo) did it, since I might write something slightly wrong since I don't use it.

## ghost | 2017-03-29T03:43:06+00:00
@voidzero Can this issue be closed?

## voidzero | 2017-03-29T22:37:45+00:00
Busy as a bee and forgot all about adding those comments to the README. Sorry about that - @glv2 much thanks for adding #632. Means this one can be closed :+1: 

# Action History
- Created by: voidzero | 2017-02-15T20:59:13+00:00
- Closed at: 2017-03-29T22:37:45+00:00
