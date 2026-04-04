---
title: 'import_outputs: Error: Failed to import outputs: unsupported version'
source_url: https://github.com/monero-project/monero/issues/1456
author: moneroexamples
assignees: []
labels: []
created_at: '2016-12-15T00:00:47+00:00'
updated_at: '2016-12-25T00:13:15+00:00'
type: issue
status: closed
closed_at: '2016-12-25T00:13:15+00:00'
---

# Original Description
This error is boost serialisation error. If normal wallet is made on a pc that uses different boost version than a pc with viewonly wallet, exporting and importing outputs may result in this error.

I used ubuntu 16.10 to export outputs, and my second wallet is on 16.04. The import fails because boost versions are different on those systems. 

Its worth mantioning, that it only happens when importing and exporting output files, as only this functionality uses boost serialization to produce and read the files. Importing key images, unsigned and singed txs files works because they dont use boost for this. 

# Discussion History
## ghost | 2016-12-15T01:29:28+00:00
I think this is a known issue with binary compatibility between wallets. @hyc is trying to solve by converting the wallet to use LMDB, @kenshi84 is proposing a change to the serialisation library.

## moneroexamples | 2016-12-15T04:46:21+00:00
Thanks, for info.

## kenshi84 | 2016-12-15T08:55:21+00:00
I think PR #1435 fixes this issue.

## moneroexamples | 2016-12-25T00:13:05+00:00
PR https://github.com/monero-project/monero/pull/1483c solved the issue with output files.

Thank you. Closing this issue.

# Action History
- Created by: moneroexamples | 2016-12-15T00:00:47+00:00
- Closed at: 2016-12-25T00:13:15+00:00
