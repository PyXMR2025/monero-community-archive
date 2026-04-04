---
title: 'Pop-Up File Dialog for picking a wallet opens behind GUI '
source_url: https://github.com/monero-project/monero-gui/issues/1096
author: medusadigital
assignees: []
labels:
- bug
- wontfix
created_at: '2018-01-27T12:48:17+00:00'
updated_at: '2018-03-30T00:36:19+00:00'
type: issue
status: closed
closed_at: '2018-03-30T00:36:19+00:00'
---

# Original Description
File Dialog for picking s wallet opens behind GUI. Depending on location of the main window, it can be hidden completely.

--> All popups of this kind are affected (also when signing a trx for example)

![seed_restore_behind](https://user-images.githubusercontent.com/17108301/35472070-b8290fd2-0368-11e8-9dee-35500066a721.png)


# Discussion History
## medusadigital | 2018-01-27T12:48:30+00:00
+Bug

## preston-wagner | 2018-02-18T04:41:02+00:00
I think this is part of a bigger issue where the monero gui renders in front of _everything_ and can't be minimized.

## sanderfoobar | 2018-03-30T00:14:32+00:00
Related to the window manager in use.

## sanderfoobar | 2018-03-30T00:14:43+00:00
+wontfix

# Action History
- Created by: medusadigital | 2018-01-27T12:48:17+00:00
- Closed at: 2018-03-30T00:36:19+00:00
