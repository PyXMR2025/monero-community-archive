---
title: '[Feature Request] - ability to select text in history tab'
source_url: https://github.com/monero-project/monero-gui/issues/198
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-11-24T03:07:07+00:00'
updated_at: '2016-11-24T15:17:29+00:00'
type: issue
status: closed
closed_at: '2016-11-24T15:17:29+00:00'
---

# Original Description
built commit c83336cc4714215725cba957d8ea164a57c33987

Is it possible to select any of the text on the history tab, so that I can copy and paste the text that is found there? 

Seems silly that it displays it but I can't select it and (for example) paste it into a block explorer. 

# Discussion History
## Gingeropolous | 2016-11-24T13:14:41+00:00
This was built and run on Ubuntu 16. 

## Jaqueeee | 2016-11-24T14:19:51+00:00
All fields except amount and fee should be selectable by mouse AFAICT. Haven't tested on Ubuntu though. Can you confirm that block height isn't selectable for example?
https://github.com/monero-project/monero-core/blob/c83336cc4714215725cba957d8ea164a57c33987/components/HistoryTable.qml#L234

## Gingeropolous | 2016-11-24T15:17:29+00:00
im an idiot. it works as it should. 

# Action History
- Created by: Gingeropolous | 2016-11-24T03:07:07+00:00
- Closed at: 2016-11-24T15:17:29+00:00
