---
title: CORS headers in monero-wallet-rpc
source_url: https://github.com/monero-project/monero/issues/1677
author: amiuhle
assignees: []
labels: []
created_at: '2017-02-04T23:26:34+00:00'
updated_at: '2017-11-14T20:56:33+00:00'
type: issue
status: closed
closed_at: '2017-11-14T20:56:33+00:00'
---

# Original Description
Currently, `monero-wallet-rpc` doesn't send CORS headers and thus can't be used in web apps.

I don't know whether this is by design or just hasn't been implemented, although I can't think of any reason why this would be by design.

If a PR will be merged, I'll create one.

# Discussion History
## vtnerd | 2017-02-05T00:43:17+00:00
This doesn't seem like a good idea. If someone combines CORS with `--disable-rpc-login`, then the CSRF exploits are even more dire because you can `POST` without user interaction.

What is the use case? A JS only local webapp that calls into `monero-wallet-rpc` ?

## amiuhle | 2017-02-07T11:16:12+00:00
Well it should be behind a reverse proxy for production anyways to enable SSL, so the CORS headers can be set there, too.

On the other hand, if both options are in `moner-wallet-rpc` behind flags, we could check that they should not be used together or at least give out a warning. Especially for development, this would make stuff a little easier...

That said, I don't have any strong feelings about this. If it's a bad idea then I'll post a snippet for a CORS proxy below so others can find this and close the issue.

> What is the use case? A JS only local webapp that calls into `monero-wallet-rpc` ?

Yes, I'm playing around with a local setup to receive monero using a progressive web app...



## moneromooo-monero | 2017-11-14T19:49:27+00:00
+resolved

# Action History
- Created by: amiuhle | 2017-02-04T23:26:34+00:00
- Closed at: 2017-11-14T20:56:33+00:00
