---
title: 'ubuntu 16.04 : master fails to compile, v0.9.4 works'
source_url: https://github.com/monero-project/monero/issues/905
author: schnerchi
assignees: []
labels: []
created_at: '2016-07-11T10:31:01+00:00'
updated_at: '2016-07-12T06:53:31+00:00'
type: issue
status: closed
closed_at: '2016-07-12T06:53:31+00:00'
---

# Original Description
maybe someone with more knowledge can have a look : 

http://pastebin.com/DKYCgsDt


# Discussion History
## schnerchi | 2016-07-11T10:33:17+00:00
more info : http://pastebin.com/Wh0eP1Hm


## moneromooo-monero | 2016-07-11T17:04:08+00:00
This doesn't seem to include the error.
In the future, can you also please put logs either in the bug itself if not too loing, or on fpaste.org ? I usually can't get to pastebin.com as they'll block tor exit nodes 95% of the time, though I got lucky today :)


## iDunk5400 | 2016-07-11T20:24:14+00:00
@schnerchi Maybe you should try cloning master into a folder that does not contain a space in its name.


## moneroexamples | 2016-07-11T23:57:33+00:00
Did you check instructions here:
- https://github.com/moneroexamples/compile-monero-09-on-ubuntu-16-04


## radfish | 2016-07-12T04:18:44+00:00
(Just a minor sidenote: please do not use fpaste.org either because they expire. There are issues here without any information except the dead link to fpaste.org. Github has perfectly usable file attachment feature: via drag-drop or the link right below. Use that please; in addition to pasting the most relevant chunk inline. Thanks.)


## schnerchi | 2016-07-12T06:53:31+00:00
Ok, issue solved. Problem was/is the space in the folder name. So something must have changed between 0.9.4 and MASTER that causes this.

Thanks everybody!


# Action History
- Created by: schnerchi | 2016-07-11T10:31:01+00:00
- Closed at: 2016-07-12T06:53:31+00:00
