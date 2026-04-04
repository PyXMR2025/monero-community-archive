---
title: monerod upgrade v0-9-4-0 -> v0-10-0-0 fails
source_url: https://github.com/monero-project/monero/issues/1143
author: ElLamparto
assignees: []
labels: []
created_at: '2016-09-27T09:06:47+00:00'
updated_at: '2016-12-15T17:10:39+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:10:39+00:00'
---

# Original Description
After about 20 minutes of torturing disk, v0-10-0-0 fails fails with:

2016-Sep-24 12:00:06.700432 Failed to delete tx_outputs: MDB_TXN_FULL: Transaction has too many dirty pages - transaction too big

2016-Sep-24 12:00:06.723907 Error opening database: Failed to delete tx_outputs: MDB_TXN_FULL: Transaction has too many dirty pages - transaction too big

Then monerod starts but does nothing.

OS: Debian Jessie 32bit


# Discussion History
## moneromooo-monero | 2016-09-27T17:42:19+00:00
Sync from scratch, it's usually faster than conversion anyway.


## ElLamparto | 2016-09-28T07:23:58+00:00
Maybe then syncing from scratch should be the default option?


## fluffypony | 2016-09-28T07:30:20+00:00
@ElLamparto the problem is unattended nodes - we're trying not to break them, and the auto-conversion seemed the least harmful way. We do mention in the release notes that sync-from-scratch is preferred.


## ElLamparto | 2016-09-29T12:16:33+00:00
@fluffypony, It seems that in my case the auto-conversion killed the database (quite harmful!). It is then up to you to close this ticket.

Where can I find the release notes? Thanks.


## iamsmooth | 2016-10-06T05:05:50+00:00
Release notes are here: https://github.com/monero-project/monero/releases/tag/v0.10.0

The other disadvantage of sync-from-scratch is much higher bandwidth use, which can be expensive for people with bandwidth metering or limits. Conversion-in-place should ideally work, but is just broken in some cases.


## ghost | 2016-10-17T21:28:26+00:00
Hi @ElLamparto is this still an issue for you or can it be closed?


## ElLamparto | 2016-10-18T12:29:54+00:00
I have synced from the scratch, so it is no longer an issue for me. But the bug exists - so it is up to you to close this ticket (with or without fixing the bug).


## luigi1111 | 2016-12-15T17:10:39+00:00
Will likely be without "fixing". :)

# Action History
- Created by: ElLamparto | 2016-09-27T09:06:47+00:00
- Closed at: 2016-12-15T17:10:39+00:00
