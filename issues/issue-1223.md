---
title: Memory leaks
source_url: https://github.com/monero-project/monero-gui/issues/1223
author: rex4539
assignees: []
labels:
- invalid
created_at: '2018-03-31T04:16:31+00:00'
updated_at: '2019-04-27T00:36:33+00:00'
type: issue
status: closed
closed_at: '2019-04-27T00:36:33+00:00'
---

# Original Description
As requested, consolidating all memory leaks into one issue (which is wrong from a QA/release process perspective as each bug should be fixed separately and are not connected).

This issue covers:

https://github.com/monero-project/monero-gui/issues/1032
https://github.com/monero-project/monero-gui/issues/1033
https://github.com/monero-project/monero-gui/issues/1034
https://github.com/monero-project/monero-gui/issues/1035
https://github.com/monero-project/monero-gui/issues/1036
https://github.com/monero-project/monero-gui/issues/1037
https://github.com/monero-project/monero-gui/issues/1038
https://github.com/monero-project/monero-gui/issues/1039
https://github.com/monero-project/monero-gui/issues/1040
https://github.com/monero-project/monero-gui/issues/1041
https://github.com/monero-project/monero-gui/issues/1042
https://github.com/monero-project/monero-gui/issues/1043
https://github.com/monero-project/monero-gui/issues/1044
https://github.com/monero-project/monero-gui/issues/1045
https://github.com/monero-project/monero-gui/issues/1046
https://github.com/monero-project/monero-gui/issues/1111
https://github.com/monero-project/monero-gui/issues/1112

In case this overwhelms devs and folks start accusing QT, I have already suggested to drop QT altogether and implement https://github.com/monero-project/monero-gui/issues/1049

# Discussion History
## pazos | 2018-03-31T13:40:33+00:00
Did you run a local node? Was monerod started by the gui? Is the blockchain synced? Could you reproduce those issues running the gui against a local node started elsewhere?

I think that start the wallet without an almost up-to-date chain is a bad idea. The gui feels unresponsive for some time and everything the user can do within the gui could break the program.

## rex4539 | 2018-03-31T18:12:18+00:00
@pazos Watch the video below, it's very entertaining :)

https://www.dropbox.com/s/niqw0uk7gg96uig/Monero%20leaks.mp4?dl=0

## pazos | 2018-04-01T20:33:24+00:00

@rex4539: the leaks shown in the video seem related to upstream qt bugs. In that case most of the leaks are related to the bundled qt libraries (in static builds) or your system libraries. If you wish you could try to build from master and link against a recent version of qt (5.10+) and see how many leaks are resolved.

## selsta | 2019-04-27T00:27:35+00:00
If this is still happening on the latest master (and with a newer Qt version) please open a new issue.

+invalid

# Action History
- Created by: rex4539 | 2018-03-31T04:16:31+00:00
- Closed at: 2019-04-27T00:36:33+00:00
