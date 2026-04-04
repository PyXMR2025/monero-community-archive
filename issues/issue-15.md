---
title: 'Kovri: Configure buildbot to post coverage info to coveralls.io'
source_url: https://github.com/monero-project/meta/issues/15
author: danrmiller
assignees: []
labels: []
created_at: '2016-11-14T20:18:27+00:00'
updated_at: '2017-01-03T23:18:38+00:00'
type: issue
status: closed
closed_at: '2017-01-03T21:38:25+00:00'
---

# Original Description
Post json coverage data with the kovri repo token to coveralls as a buildstep in the kovri build factories on buildbot.

# Discussion History
## anonimal | 2016-11-20T00:22:46+00:00
This was resolved for kovri (afaict, yes?). Should this issue be extended to monero too?


## anonimal | 2017-01-03T14:19:54+00:00
Is this issue still applicable?

## danrmiller | 2017-01-03T21:38:22+00:00
Resolved. https://coveralls.io/github/monero-project/kovri

Monero testing has several steps to be completed, like the libwallet environment, before adding coveralls.

## anonimal | 2017-01-03T23:18:38+00:00
Oops, I wasn't clear: I meant applicable for Monero.

# Action History
- Created by: danrmiller | 2016-11-14T20:18:27+00:00
- Closed at: 2017-01-03T21:38:25+00:00
