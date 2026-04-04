---
title: version.js not found (git rev-list issue in monero/src/version.cmake?)
source_url: https://github.com/monero-project/monero-gui/issues/360
author: voidzero
assignees: []
labels: []
created_at: '2016-12-26T00:38:21+00:00'
updated_at: '2017-03-03T13:33:49+00:00'
type: issue
status: closed
closed_at: '2017-03-03T13:33:49+00:00'
---

# Original Description
Trying to build this on Gentoo x64, but getting an error that version.js isn't found. Probably related to the following, that is shown when `./get_libwallet_api.sh` is executed. It suggests that `git rev-list` isn't executed correctly by monero/src/version.cmake:

```
make[3]: Entering directory '/foobar/monero-core/monero/build/release'
[100%] Generating version/version.h
-- You are currently on commit dd580d7
usage: git rev-list [OPTION] <commit-id>... [ -- paths... ]
  limiting output:
    --max-count=<n>
    --max-age=<epoch>
    --min-age=<epoch>
    --sparse
    --no-merges
    --min-parents=<n>
    --no-min-parents
    --max-parents=<n>
    --no-max-parents
    --remove-empty
    --all
    --branches
    --tags
    --remotes
    --stdin
    --quiet
  ordering output:
    --topo-order
    --date-order
    --reverse
  formatting output:
    --parents
    --children
    --objects | --objects-edge
    --unpacked
    --header | --pretty
    --abbrev=<n> | --no-abbrev
    --abbrev-commit
    --left-right
    --count
  special purpose:
    --bisect
    --bisect-vars
    --bisect-all
CMake Warning at src/version.cmake:47 (message):
  Cannot determine most recent tag.  Make sure that you are building either
  from a Git working tree or from a source archive.

```

When running `qmake` from qt5:

```
% /usr/lib/qt5/bin/qmake
Project MESSAGE: Building with libunwind
RCC: Error in 'qml.qrc': Cannot find file 'version.js'
```

# Discussion History
## Jaqueeee | 2016-12-26T00:40:08+00:00
Run build.sh instead of qmake

## moneromooo-monero | 2016-12-26T11:10:01+00:00
What is the output of this command, when you're in the monero tree ?

git rev-list --tags --max-count=1 --abbrev-commit

Then this one:

git show --oneline


## voidzero | 2016-12-26T14:01:50+00:00
The first command gives me the same usage output. The second shows me a loong output, too long to post, 471507 lines! Full of diffs.

I think we need to pass a commit-id to git rev-list:

```
% git rev-list --tags --max-count=1 --abbrev-commit HEAD
dd580d7
```

The `git rev-parse` command might be a usable alternative:

```
% git rev-parse --short HEAD
dd580d7

% git rev-parse --abbrev-ref HEAD
master

% git rev-parse --short master     
dd580d7


## voidzero | 2016-12-26T14:22:00+00:00
@Jaqueeee build.sh doesn't help me much either, even after I corrected the path to qmake, I get the same usage output from `git rev-list` and after a few other lines (generating translations), I get:

```
g++ -c -pipe -O2 -std=gnu++0x -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-core -I. -I/mnt/coindb/src/monero-core/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -I/usr/lib64/qt5/mkspecs/linux-g++ -o main.o ../main.cpp
In file included from ../main.cpp:39:0:
../src/libwalletqt/WalletManager.h:6:32: fatal error: wallet/wallet2_api.h: No such file or directory
```

## moneromooo-monero | 2016-12-26T14:27:08+00:00
What is the output of:

git --version

## moneromooo-monero | 2016-12-26T14:28:36+00:00
Did you clone a shallow repo (ie, --depth 1) ?


## moneromooo-monero | 2016-12-26T14:29:22+00:00
What is the output of:

git tag


## voidzero | 2016-12-26T14:33:06+00:00
```
% git --version
git version 2.7.3

% git tag
v0.0-beta-1
```

Not a shallow clone.

## voidzero | 2016-12-26T14:33:49+00:00
That tag is from monero-core, btw.

## moneromooo-monero | 2016-12-26T20:35:53+00:00
Works here (with a test repo) with git 2.7.3.
I'll have to ignore this then, unless/until new information.

## Jaqueeee | 2016-12-27T12:33:36+00:00
@voidzero Can you post your full output from get_libwallet_api.sh and build.sh? Preferably on https://paste.fedoraproject.org or similar. 

## voidzero | 2016-12-27T20:27:29+00:00
sure. Here's build.sh:
https://paste.fedoraproject.org/513848/48287037/

Here's get_libwallet_api.sh:
https://paste.fedoraproject.org/513850/48287041/

Both links will expire in one month.

## Jaqueeee | 2016-12-27T21:49:22+00:00
@voidzero 
Sorry, I meant the output you get when running those scripts. 


## voidzero | 2016-12-27T22:59:07+00:00
@moneromooo-monero or @Jaqueeee, what are the contents of a correctly generated version.js? I will add it manually so that I can at least try to continue building the gui.

## voidzero | 2016-12-27T23:09:57+00:00
@Jaqueeee Oh, the output :smile: Alright, will post tomorrow. 

## moneromooo-monero | 2016-12-28T23:33:49+00:00
var GUI_VERSION = "7555502"
var GUI_MONERO_VERSION = "049b7e9"


## Jaqueeee | 2017-03-03T11:43:14+00:00
@voidzero can this be closed or are you still having issues?

## voidzero | 2017-03-03T13:33:49+00:00
No issues anymore, I'll close it. Thanks.

# Action History
- Created by: voidzero | 2016-12-26T00:38:21+00:00
- Closed at: 2017-03-03T13:33:49+00:00
