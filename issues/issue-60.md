---
title: .config directory name on Linux
source_url: https://github.com/monero-project/monero-gui/issues/60
author: peronero
assignees: []
labels: []
created_at: '2016-10-13T21:13:29+00:00'
updated_at: '2016-12-15T15:56:11+00:00'
type: issue
status: closed
closed_at: '2016-12-15T15:56:11+00:00'
---

# Original Description
Currently monero-core creates a 'The Monero Project' directory in .config to store .conf files - ideally this directory should not have spaces, perhaps something as simple as 'monero' is the best solution.


# Discussion History
## mbg033 | 2016-11-01T17:42:42+00:00
Reason of this is the  [`Settings`](http://doc.qt.io/qt-5/qml-qt-labs-settings-settings.html) QML type that uses [`QSettings`](http://doc.qt.io/qt-5/qsettings.html) internally and does't offer any public API to change location where the data actually stored. Even more, on different platforms it stored in different places.
What is the problem with spaces actually?


## mbg033 | 2016-11-01T17:43:57+00:00
But yes, if we really have a reasons to move settings file to the different location - it can be custom implementation


## medusadigital | 2016-11-06T09:18:13+00:00
decision here: https://github.com/monero-project/monero-core/pull/96

can be closed. 


## peronero | 2016-11-07T23:24:15+00:00
I don't think that is an accurate assessment of the situation. 

There are no other  apps on my system using either spaces or capitals in their .config names, nor are there any on most systems - certainly not using spaces. 

It must be against some standards and specs, and we would be just be creating more work down the road for any packagers wanting to include Monero in a distro's repositories, even more additional work devising a clunky contingency plan to deal with legacy directories if this is not addressed before it goes into the wild, not to mention generally looking like amateurs using a 'The Monero Project' directory to store configs _on Linux._

The Atom project has a somewhat related discussion about this on their github: https://github.com/atom/atom/issues/8281

Further, the Qt5 spec does not seem to limit the .config directory name to the organization.

`AppConfigLocation "~/.config/<APPNAME>", "/etc/xdg/<APPNAME>"`

> In the table above, APPNAME is usually the organization name, the application name, or both, or a unique name generated at packaging

http://doc.qt.io/qt-5/qstandardpaths.html


## hyc | 2016-11-09T20:47:06+00:00
Fwiw, spaces in directory names are a horrible idea and generally NOT done on POSIX systems. I vote to change it to just "monero" too.


## peronero | 2016-12-15T15:56:11+00:00
Fixed by #267.

# Action History
- Created by: peronero | 2016-10-13T21:13:29+00:00
- Closed at: 2016-12-15T15:56:11+00:00
