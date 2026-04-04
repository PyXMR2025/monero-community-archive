---
title: 'Bug report: offline signing'
source_url: https://github.com/monero-project/monero/issues/5741
author: dnaleor
assignees: []
labels: []
created_at: '2019-07-07T22:14:19+00:00'
updated_at: '2019-08-28T15:23:44+00:00'
type: issue
status: closed
closed_at: '2019-08-28T15:23:44+00:00'
---

# Original Description
When trying to do offline signing, I get this error: 

> imported outputs omit more outputs than we know of

To be clear: I had a fully synced view wallet with all imported keyimages and created an unsigned transaction. Then I went to the offline PC, imported my seed and tried to sign this transaction.

This always worked in the past. Now it didn't.

Workaround: export outputs and import them to the cold wallet before trying to sign the transaction.

edit: viewwallet was on Linux 64bit system; cold wallet was on Rpi3 (Armv7)

# Discussion History
## moneromooo-monero | 2019-07-08T01:09:26+00:00
Does it work between armv7 and armv7, or between what I asume is x86_64 and x86_64 ?

## dnaleor | 2019-08-28T15:23:44+00:00
issue wasn't really an issue. Combination of misunderstanding export_outputs, which data "piggybacked" with an unsigned_transaction and maybe a change in my cold signing routine. 

solved my issue, i'll close it. 

# Action History
- Created by: dnaleor | 2019-07-07T22:14:19+00:00
- Closed at: 2019-08-28T15:23:44+00:00
