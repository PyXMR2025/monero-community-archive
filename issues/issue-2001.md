---
title: Local daemon with Android
source_url: https://github.com/monero-project/monero-gui/issues/2001
author: takel1
assignees: []
labels: []
created_at: '2019-03-10T09:21:04+00:00'
updated_at: '2019-04-12T08:14:10+00:00'
type: issue
status: closed
closed_at: '2019-04-12T08:14:10+00:00'
---

# Original Description
After some research, I found that monerod compiling for Android was disabled on get_libwallet_api.

I enabled and everything is ok.

Apk package installs on Android without monerod and work well!

Any help on inserting monerod (as external binary) on an apk package?

Daemon can not be inserted on apk even when i enable this line on build.sh that for some unknown reasons was disabled.

 cp ../$MONERO_DIR/bin/$MONEROD_EXEC $BIN_PATH 

# Discussion History
# Action History
- Created by: takel1 | 2019-03-10T09:21:04+00:00
- Closed at: 2019-04-12T08:14:10+00:00
