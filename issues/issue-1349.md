---
title: Extremely High Usage
source_url: https://github.com/monero-project/monero-gui/issues/1349
author: cinjon
assignees: []
labels:
- resolved
created_at: '2018-04-23T01:02:45+00:00'
updated_at: '2019-03-29T16:27:37+00:00'
type: issue
status: closed
closed_at: '2019-03-29T16:27:37+00:00'
---

# Original Description
I just downloaded the Monero GUI client for Mac and the usage is at 700% CPU, even after the wallet and daemon are synchronized. I'm right now using a remote node (node.moneroworld.com:18089). How can I reduce this?

# Discussion History
## dEBRUYNE-1 | 2018-04-23T11:26:10+00:00
It's, most likely, caused by the daemon (your local node) performing the initial sync. Could you perhaps post the output of `Show status`  (on the `Settings` page of the GUI)? 

## cinjon | 2018-04-28T20:56:09+00:00
I don't see that option in the GUI.

## dEBRUYNE-1 | 2018-04-29T10:16:47+00:00
It's button 10 -> https://github.com/monero-ecosystem/monero-GUI-guide/blob/master/media/black_settings.png. Or is your wallet mode set to `Remote node` (indicated by the button being grey)?

## ChurchOfNotNothing | 2018-05-24T03:46:39+00:00
I'm using the Monero GUI client for Mac as well and my CPU usage is also insane. Force programs to quit and I've never had that issue before. 
@dEBRUYNE-1 
I tried to click the 'Status' button you were referring to and there was no response. In fact, nothing responds except for the left hand [Send, Receive, Settings] but then when the screen changes nothing responds.

## dEBRUYNE-1 | 2018-05-24T08:52:02+00:00
@ChurchOfNotNothing - Try applying this guide:

https://monero.stackexchange.com/questions/6651/my-gui-feels-buggy-freezes-all-the-time

## dEBRUYNE-1 | 2018-07-04T08:44:29+00:00
This particular issue (the lag issue) is supposedly resolved in GUI v0.12.2.0: 

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

@cinjon and @ChurchOfNotNothing - Could you give it a try? 

## sanderfoobar | 2019-03-29T16:18:30+00:00
In addition, another improvement related to performance is #1920 - closing this.

+resolved

# Action History
- Created by: cinjon | 2018-04-23T01:02:45+00:00
- Closed at: 2019-03-29T16:27:37+00:00
