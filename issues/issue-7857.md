---
title: Restoring GUI Wallet From Recent Height Yields No Outbound Tx's In Tx History.
source_url: https://github.com/monero-project/monero/issues/7857
author: downystreet
assignees: []
labels: []
created_at: '2021-08-13T01:21:00+00:00'
updated_at: '2021-08-13T03:56:12+00:00'
type: issue
status: closed
closed_at: '2021-08-13T03:56:12+00:00'
---

# Original Description
GUI Version: 0.17.2.2-937cb98 (Qt 5.15.2)

When restoring GUI wallet in Simple Mode from a recent height of approximately 2 months ago there are no outbound tx's listed in the tx history. Comparing the CLI show_transfers command to the GUI tx history, the GUI has omitted all outbound tx's.

# Discussion History
## selsta | 2021-08-13T01:22:03+00:00
Can you go to Settings -> Info and post the restore height you have set?

## downystreet | 2021-08-13T01:24:10+00:00
The height was set at 2021-07-01. I have already started refreshing from another height that I usually refresh from which is before there were any tx's.

## selsta | 2021-08-13T01:25:01+00:00
What is the date of your first transactions?

## downystreet | 2021-08-13T01:27:26+00:00
Actually what I said is not correct the first transactions are from around the first few months of 2019 but I usually restore from January of 2020.

## selsta | 2021-08-13T01:28:11+00:00
You have to set a restore height that is earlier than the first received transaction.

## downystreet | 2021-08-13T01:28:41+00:00
Ok that's what it is then. I will restore from 2019 and see if that fixes it.


## downystreet | 2021-08-13T03:40:33+00:00
All is good now. I can see all outbound and inbound tx's. Thank you!

# Action History
- Created by: downystreet | 2021-08-13T01:21:00+00:00
- Closed at: 2021-08-13T03:56:12+00:00
