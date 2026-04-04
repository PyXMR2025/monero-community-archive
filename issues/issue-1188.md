---
title: '[RFC] Option to view live logs in daemon mode'
source_url: https://github.com/monero-project/monero/issues/1188
author: ghost
assignees: []
labels: []
created_at: '2016-10-06T15:02:37+00:00'
updated_at: '2016-10-12T15:18:30+00:00'
type: issue
status: closed
closed_at: '2016-10-12T15:18:30+00:00'
---

# Original Description
`monerod --live` could give scrolling logs at the current log level for those geeks (such as myself) who like to watch things happily tick by on the terminal...


# Discussion History
## moneroexamples | 2016-10-06T23:51:11+00:00
set_log (or similar, dont remember) command in the deamon allows to specify how much log info is displayed in the terminal window. 


## ghost | 2016-10-07T00:39:32+00:00
Yes but if I log out and then want to log back in again and check up on my little node...

I currently use a terminal alias to call `tail -f ./.bitmonero/monero.log` but for people who don't know or care to do this, it might be a nice little feature to add.

Not sure how you'd terminate it again from the command line without terminating the daemon though :(


# Action History
- Created by: ghost | 2016-10-06T15:02:37+00:00
- Closed at: 2016-10-12T15:18:30+00:00
