---
title: No auto start mining option
source_url: https://github.com/monero-project/monero-gui/issues/3919
author: Tembelweed
assignees: []
labels: []
created_at: '2022-05-11T13:19:34+00:00'
updated_at: '2022-07-21T12:02:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero GUI has to finish syncing before being able to mine. It would be great if there was an option to auto start mining when the sync process is finished

# Discussion History
## plowsof | 2022-07-12T14:41:07+00:00
A full node is required to mine. However, if you want mine using p2pool - you can do what you wish and use a remote one. please read https://github.com/plowsof/listen_for_zmq and see list here for public nodes https://github.com/plowsof/listen_for_zmq/blob/main/zmq_list.md

## Emojibotbot | 2022-07-21T12:02:22+00:00
From what I see, the instructions listed above still requires the user to press the "start mining" button right?  If so, that does not address the initial intent of the request.  If windows reboots for some reason, the user still needs to interact with the GUI to start mining.  I think the intent would be to have a "auto start mining" checkbox of some sort in the advanced settings section of the GUI that initiates mining without user interaction upon starting the GUI.

# Action History
- Created by: Tembelweed | 2022-05-11T13:19:34+00:00
