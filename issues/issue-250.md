---
title: Cannot add GPG key to forum
source_url: https://github.com/monero-project/monero-site/issues/250
author: jonathancross
assignees: []
labels: []
created_at: '2017-04-12T15:45:07+00:00'
updated_at: '2017-10-20T22:13:31+00:00'
type: issue
status: closed
closed_at: '2017-09-18T01:25:55+00:00'
---

# Original Description
When trying to register for forum.getmonero.org - I repeatedly got errors, eg: **_"Whoops, looks like something went wrong."_**.  Turns out that it was because I was trying to add my gpg key which completely blocks the registration process.

After registering (without GPG key), I tried to add my gpg key to my profile, but again the backend seems to be broken and returns a 500 error when I POST to https://forum.getmonero.org/user/settings/add-gpg

Note: It is unclear what format is expected, so I tried the following:
* `9386 A2FB 2DA9 D0D3 1FAF  0818 C0C0 7613 2FFA 7695`
* `0xC0C076132FFA7695`
* `C0C076132FFA7695`
* `2FFA7695`


# Discussion History
## mattcode55 | 2017-09-14T16:51:12+00:00
I think the [monero-forum](https://github.com/monero-project/monero-forum) repository might be a more appropriate place for this issue.

## jonathancross | 2017-09-18T01:25:55+00:00
Moved to https://github.com/monero-project/monero-forum/issues/44

# Action History
- Created by: jonathancross | 2017-04-12T15:45:07+00:00
- Closed at: 2017-09-18T01:25:55+00:00
