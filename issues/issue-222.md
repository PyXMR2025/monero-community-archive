---
title: Hook into URI scheme on, eg, Android, iOS
source_url: https://github.com/monero-project/monero-gui/issues/222
author: moneromooo-monero
assignees: []
labels:
- resolved
created_at: '2016-11-28T18:13:24+00:00'
updated_at: '2019-05-04T19:00:39+00:00'
type: issue
status: closed
closed_at: '2019-05-04T19:00:39+00:00'
---

# Original Description
I've no idea how that'd technically work, but:

- the GUI now shows a QR code for simple payment
- there are now RPC and wallet2 API for parsing a monero: URI

So there needs to be a way for the wallet to register itself as a handler for monero: URIs. When invoked, this should call the wallet2 API (tools::wallet2::parse_uri) to get back the constituents, then call the transfer function with those, and ensure a user prompt will be made.


# Discussion History
## johnalanwoods | 2017-09-17T21:11:25+00:00
This is trivial on iOS and macOS. Will investigate on Android.

## erciccione | 2018-11-18T13:02:06+00:00
@moneromooo-monero is still also present in new GUI or can be closed?

## erciccione | 2019-05-04T18:59:19+00:00
@moneromooo-monero This looks fixed in #2029. Please reopen if necessary.

+resolved

# Action History
- Created by: moneromooo-monero | 2016-11-28T18:13:24+00:00
- Closed at: 2019-05-04T19:00:39+00:00
