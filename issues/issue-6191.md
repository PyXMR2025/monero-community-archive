---
title: 'Wallet: Export transfers to CSV'
source_url: https://github.com/monero-project/monero/issues/6191
author: tmoravec
assignees: []
labels: []
created_at: '2019-11-27T10:14:27+00:00'
updated_at: '2019-11-27T13:35:15+00:00'
type: issue
status: closed
closed_at: '2019-11-27T13:31:51+00:00'
---

# Original Description
Having the option to export the transfers history into CSV is something that would be tremendously useful for people and companies building services on top of Monero. I offer to implement it.

# Discussion History
## arnuschky | 2019-11-27T11:49:19+00:00
Not much more to say. 
 - export the content of `show_transfers` to a `.csv` file (simple write the same table separated with `,`) to a file
 - write a heading first
 - command could be `export_csv <filename>`
 - should also be accessible via command line for scripting

I think that's about it. I wouldn't bother doing more (ie messing with configurable separators or similar)

Is that sufficient detail?

## ghost | 2019-11-27T12:36:13+00:00
Not in wallet with C++ please. There's already `wallet-rpc` that can export structured JSON array, which is also very business friendly like CSV.

## fluffypony | 2019-11-27T13:19:01+00:00
@fuwa0529 what does C++ have to do with it? Producing CSV is pretty trivial, and I've never heard of an accounting system like Xero allowing you to import random JSON. I don't see a problem with this feature request, imho.

## moneromooo-monero | 2019-11-27T13:23:10+00:00
export_transfers

## fluffypony | 2019-11-27T13:31:51+00:00
Closed because it already exists :)

## ghost | 2019-11-27T13:35:15+00:00
@fluffypony there are many problems with too much C++, but I'll save it since it's closed..



# Action History
- Created by: tmoravec | 2019-11-27T10:14:27+00:00
- Closed at: 2019-11-27T13:31:51+00:00
