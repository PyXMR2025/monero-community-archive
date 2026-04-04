---
title: monerod.exe causing high hard pagefaults
source_url: https://github.com/monero-project/monero-gui/issues/614
author: exemar
assignees: []
labels: []
created_at: '2017-03-27T14:30:16+00:00'
updated_at: '2017-03-27T19:00:38+00:00'
type: issue
status: closed
closed_at: '2017-03-27T19:00:38+00:00'
---

# Original Description
Ran LatencyMon with the monero daemon running form the beta gui client and noticed very high numbers of hard pagefaults from the monerod.exe process. I've attached a screenshot of the results from latencymon. If there's any other information I can provide to help identifying this issue please just let me know and I will do so. First time posting here (was redirected from reddit) so not really sure what information I should be providing. 
![monerohp](https://cloud.githubusercontent.com/assets/26716564/24361566/2207d60c-1302-11e7-9389-b09e82b6cfee.png)


# Discussion History
## Jaqueeee | 2017-03-27T17:32:16+00:00
@exemar Thanks. monerod.exe isn't related to this repo (GUI). Could you please add this to https://github.com/monero-project/monero/issues instead?

## Jaqueeee | 2017-03-27T17:35:02+00:00
@exemar and please also provide some more info about your system. 
From #monero-dev:
<+hyc> how much memory involved?
19:32 total system RAM, total free, process size.
<+hyc> also, all LMDB reads are page faults.
19:33 that's how memory mapped files work...

## exemar | 2017-03-27T18:00:12+00:00
@Jaqueeee ok adding it there instead. will add additional system info. Sorry not too knowledgeable about all this stuff just thought I might have spotted a bug and wanted to report it! are you saying the pagefaults are normal therefore and not a concern?

## medusadigital | 2017-03-27T18:45:29+00:00
Pagefaults in latencyMon means the application expected something in Ram, but needs to go to look on disk insstead. If your music apllication does this, its bad (thats why latencymon tracks it). With monerod.exe i would say this is expected behaviour 

## exemar | 2017-03-27T19:00:38+00:00
Thanks for the clarification. 

# Action History
- Created by: exemar | 2017-03-27T14:30:16+00:00
- Closed at: 2017-03-27T19:00:38+00:00
