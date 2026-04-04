---
title: Retrieving of viewkey
source_url: https://github.com/monero-project/monero/issues/76
author: othevtc
assignees: []
labels: []
created_at: '2014-08-02T14:43:29+00:00'
updated_at: '2014-08-05T07:43:58+00:00'
type: issue
status: closed
closed_at: '2014-08-05T07:43:58+00:00'
---

# Original Description
The viewkey is only displayed once the wallet is started, so we need an option to print it out via commandline.

It can be accesses the following way from simplewallet: m_account.get_keys().m_view_secret_key


# Discussion History
## fluffypony | 2014-08-02T14:49:39+00:00
@jakoblind are you able to pick this up? Since you're going to be adding the ability to show the mnemonic via RPC, this should follow similar functionality. I think these "show X key" RPC calls should be separate so that retrieving a view key, for instance, does not accidentally leak a spend key to a client application that is bad at managing it.


## jakoblind | 2014-08-05T06:58:46+00:00
I added the code to the seed PR 


## fluffypony | 2014-08-05T07:43:58+00:00
PR merged, issue closed. Thanks @jakoblind!


# Action History
- Created by: othevtc | 2014-08-02T14:43:29+00:00
- Closed at: 2014-08-05T07:43:58+00:00
