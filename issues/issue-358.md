---
title: build.sh fails on openSUSE - qmake not found
source_url: https://github.com/monero-project/monero-gui/issues/358
author: peronero
assignees: []
labels: []
created_at: '2016-12-24T17:43:27+00:00'
updated_at: '2017-06-30T17:28:14+00:00'
type: issue
status: closed
closed_at: '2017-06-30T17:28:14+00:00'
---

# Original Description
```
./build.sh: line 68: qmake: command not found
make: *** No targets specified and no makefile found.  Stop.
cp: cannot create regular file 'release/bin': No such file or directory

```

'qmake' is 'qmake-qt5' on openSUSE.

# Discussion History
## ghost | 2016-12-24T17:56:43+00:00
It looks as if you didn't add the Qt bin dir to your path:

`export PATH=$PATH:$HOME/Qt/5.7/clang_64/bin`

where Qt is the folder you selected to install Qt.

I had this same problem on OSX, so hopefully it works on openSUSE.

## Jaqueeee | 2016-12-27T12:40:25+00:00
if qmake-qt5 is in your path you can create an alias or a symlink from qmake->qmake-qt5.
You can add `alias qmake='qmake-qt5'`to your `.bashrc` in home folder 

## voidzero | 2016-12-27T23:03:42+00:00
I don't think that aliases are used by scripts. In the case of Gentoo, qmake for qt5 is at /usr/lib64/qt5/bin/qmake. That could either be added to the path by the user, but it'd be more convenient to have something like this on a separate line: `: ${QMAKE:-/usr/bin/qmake}` (the line does need to start with a colon there), and consequently use `$QMAKE` rather than `qmake`.

That way a user could also run build.sh as `QMAKE=/usr/lib64/qt5/bin/qmake ./build.sh`

## medusadigital | 2017-04-18T09:39:23+00:00
can this be closed ? 
or needs something being done ? 

## voidzero | 2017-04-21T01:32:29+00:00
@peronero can you try to do the following:

`QT_SELECT=5 ./build.sh`

See if that works. If so, we can ask @glv2 to add OpenSUSE next to Gentoo, in #637.

If you already have it working, or lost interest, please close this bug.

# Action History
- Created by: peronero | 2016-12-24T17:43:27+00:00
- Closed at: 2017-06-30T17:28:14+00:00
