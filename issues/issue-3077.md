---
title: Missing dependency on howto
source_url: https://github.com/monero-project/monero/issues/3077
author: paulohm2
assignees: []
labels: []
created_at: '2018-01-07T16:08:18+00:00'
updated_at: '2018-01-30T10:00:37+00:00'
type: issue
status: closed
closed_at: '2018-01-30T10:00:37+00:00'
---

# Original Description
https://github.com/monero-project/monero should list qt4-dev-tools as a dependency. make fails with the following error if it is no installed.

lrelease: could not exec '/usr/lib/x86_64-linux-gnu/qt4/bin/lrelease': No such file or directory

# Discussion History
## moneromooo-monero | 2018-01-07T17:11:48+00:00
No, monero should be fixed to not use lrelease instead, if it's not found.

## glv2 | 2018-01-07T17:44:18+00:00
In fact there is already a test in *translations/CMakeLists.txt* checking if *lrelease* is present or not.

@paulohm2 it looks as if on your system *lrelease* exists but is some kind of wrapper trying to execute the real *lrelease* binary, which is not installed...
What result do you get when entering the command ```which lrelease```?


## paulohm2 | 2018-01-07T19:10:03+00:00
Sorry too late :-)

already did a sudo apt-get install qt4-dev-tools

it now reads /usr/bin/lrelease


## moneromooo-monero | 2018-01-07T20:25:34+00:00
Uninstall it, then. Unless you have a sudden non-monero use for it now :)

## paulohm2 | 2018-01-07T21:13:14+00:00
ok did a apt-get remove but now the make does not issue an error :-|


## moneromooo-monero | 2018-01-08T08:40:52+00:00
rm build/type/CMakeCache.txt

The presence might be cached. 

## paulohm2 | 2018-01-08T21:11:57+00:00
it wasn't there already, did a make clean before retrying the make



## paulohm2 | 2018-01-08T21:13:05+00:00
which lrelease continues to report  /usr/bin/lrelease even after I removed the qt4 package

## moneromooo-monero | 2018-01-08T21:25:52+00:00
Is this flie a link to /usr/lib/x86_64-linux-gnu/qt4/bin/lrelease, and does /usr/lib/x86_64-linux-gnu/qt4/bin/lrelease exist, and is it an executable file for your arch, and does it have the exec permission for you or your group, and are the directories leading to it readable/executable for you or your group (I forget exactly which bits must be set here) ?

## moneromooo-monero | 2018-01-08T21:26:27+00:00
Oh, and "hash -r" is needed to get bash to flush the what's in path cache.
  

## paulohm2 | 2018-01-08T21:30:13+00:00
$which lrelease
/usr/bin/lrelease

$ls -Al /usr/bin/lrelease
lrwxrwxrwx 1 root root 9 Jan  6 00:41 /usr/bin/lrelease -> qtchooser

$ls -Al /usr/lib/x86_64-linux-gnu/qt4/bin/lrelease
-rwxr-xr-x 1 root root 1699400 Abr  5  2016 /usr/lib/x86_64-linux-gnu/qt4/bin/lrelease

$hash -r
$ which lrelease
/usr/bin/lrelease



## moneromooo-monero | 2018-01-08T23:22:08+00:00
file /usr/lib/x86_64-linux-gnu/qt4/bin/lrelease
uname -a

## paulohm2 | 2018-01-08T23:28:59+00:00
$ file /usr/lib/x86_64-linux-gnu/qt4/bin/lrelease
/usr/lib/x86_64-linux-gnu/qt4/bin/lrelease: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=5770b5b62cf1a9ca177b4ee4eaff893f60bc8263, stripped

$uname -a
Linux xxx 4.10.0-42-generic #46~16.04.1-Ubuntu SMP Mon Dec 4 15:57:59 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

  

## moneromooo-monero | 2018-01-08T23:32:25+00:00
Can you run /usr/lib/x86_64-linux-gnu/qt4/bin/lrelease manually ?

## paulohm2 | 2018-01-08T23:35:51+00:00
$ /usr/lib/x86_64-linux-gnu/qt4/bin/lrelease
Usage:
    lrelease [options] project-file
    lrelease [options] ts-files [-qm qm-file]

lrelease is part of Qt's Linguist tool chain. It can be used as a
stand-alone tool to convert XML-based translations files in the TS
format into the 'compiled' QM format used by QTranslator objects.

Options:
    -help  Display this information and exit
    -idbased
           Use IDs instead of source strings for message keying
    -compress
           Compress the QM files
    -nounfinished
           Do not include unfinished translations
    -removeidentical
           If the translated text is the same as
           the source text, do not include the message
    -markuntranslated <prefix>
           If a message has no real translation, use the source text
           prefixed with the given string instead
    -silent
           Do not explain what is being done
    -version
           Display the version of lrelease and exit


$ /usr/lib/x86_64-linux-gnu/qt4/bin/lrelease -version
lrelease version 4.8.7


## moneromooo-monero | 2018-01-08T23:37:17+00:00
And make still can't run it at the moment ?

## paulohm2 | 2018-01-08T23:40:28+00:00
I think you misunderstood me.

make was not working, so i installed qt4-dev-tools and it worked.

After your first comments, I uninstalled qt4-dev-tools and did a make clean

Since then make works flawlessly


## moneromooo-monero | 2018-01-08T23:46:59+00:00
So uninstall does not actually uninstall it. Or does not uninstall implicit deps it installed with it. Fair enough.

## danrmiller | 2018-01-08T23:58:01+00:00
I had systems where lrelease was installed and found by cmake, but didn't produce the expected output when run because other qt tools (qmake i think) were not in the path, so the build failed. This may have been something similar.

## glv2 | 2018-01-09T09:52:10+00:00
PR #3091 adds a check that should help on systems where a *lrelease* wrapper is installed even if the *lrelease* program is not installed or not working.


## moneromooo-monero | 2018-01-30T09:50:57+00:00
+resolved

# Action History
- Created by: paulohm2 | 2018-01-07T16:08:18+00:00
- Closed at: 2018-01-30T10:00:37+00:00
