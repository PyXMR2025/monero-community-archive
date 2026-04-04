---
title: Failed to restore from seed (Japanese characters in username)
source_url: https://github.com/monero-project/monero-gui/issues/758
author: Jaqueeee
assignees: []
labels:
- resolved
created_at: '2017-06-04T07:22:31+00:00'
updated_at: '2018-07-17T15:45:30+00:00'
type: issue
status: closed
closed_at: '2018-07-17T15:45:30+00:00'
---

# Original Description
<ar4s> When using Monero core (gui) to restore from a moneroaddress seed I'm getting the error "failed to save file 'C:/Users/聖奈/AppData/Local/Temp/monero-core.fl9692.keys'"  I am able to make a wallet from scratch though.
<ar4s> @jaquee windows 10, downloaded yesterday. 0.10.3.1   I didn't get it from github, rather I downloaded it from getmonero.org.  My machine is dead atm, using the girlfriends laptop (note the Japanese characters in the username, which I though was perhaps the problem... But I can create a new wallet from a new seed)

# Discussion History
## Jaqueeee | 2017-06-04T08:24:32+00:00
related to https://github.com/monero-project/monero-core/issues/199

## rbrunner7 | 2018-03-04T07:44:47+00:00
Just a little note because this issue is still formally open: My [PR #1141](https://github.com/monero-project/monero-gui/pull/1141) will probably fix this.

## sanderfoobar | 2018-07-17T15:17:38+00:00
Should be fixed via #1141. Re-open if problem remains.

+resolved

# Action History
- Created by: Jaqueeee | 2017-06-04T07:22:31+00:00
- Closed at: 2018-07-17T15:45:30+00:00
