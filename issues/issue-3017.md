---
title: Additional testnet for integration
source_url: https://github.com/monero-project/monero/issues/3017
author: amiuhle
assignees: []
labels:
- proposal
created_at: '2017-12-27T16:43:25+00:00'
updated_at: '2018-03-05T23:00:41+00:00'
type: issue
status: closed
closed_at: '2018-03-05T23:00:41+00:00'
---

# Original Description
We currently have a v6 and a v7 version of testnet. v6 is still required because applications like Monerujo support testnet, but ship release binaries.

I suggest we create an additional testnet that will run release binaries (eg current v6 testnet fork), making it easier to set up demos which people can quickly test using a wallet like Monerujo.

We already have this situation at the moment, it's just about making it "official", give it a name and it's own ports and set up some rules how frequently it will be reset.

Hardforks could be deployed a couple of weeks before they go live on mainnet to potentially catch some additional bugs.

I initially called it `staging`, but maybe `integration` would be a better name.  
https://www.reddit.com/r/Monero/comments/7mcte3/can_we_have_a_staging_testnet/

Thoughts?

# Discussion History
## moneromooo-monero | 2017-12-27T18:07:15+00:00
"applications like Monerujo support testnet, but ship release binaries"

Isn't there a contradiction between "testing" and "release" ?


## fluffypony | 2017-12-27T18:10:43+00:00
@moneromooo-monero the discussion I had with @binaryFate was around three nets:

- Devnet, which is the current testnet renamed. It lets us test future forks and features live.
- Testnet, which is a new net, new ports, and matches the live environment by forking at roughly the same time.
- Mainnet, stays as-is.

The big change is that testnet becomes a "staging" testnet, which lets integrators play and test without burning live funds.

## moneromooo-monero | 2017-12-27T18:34:44+00:00
Then whoever does this, please also add the "fake chain" overrides used by core tests.

## hyc | 2018-01-03T17:09:42+00:00
I'm kinda inclined to keep testnet with its current network and ports, and come up with a new name for the newly created staging network. But I guess it's not crucial and we could go with this existing proposal as-is.

## dEBRUYNE-1 | 2018-01-08T12:40:01+00:00
+proposal

## moneromooo-monero | 2018-03-04T10:17:31+00:00
stoffu has done this (see link above). For this network to be useful, it'll need people who asked for it to mine on it semi-reguarly, as well as some seeding data (ie, transactions). This patch will most likely go in for the coming release, and will be set to fork till v6 over some yet to be determined timeframe. This will allow pre-rct txes to be recorded on the blockchain so this new network gets a representative set of data. So be prepared to mine when this goes live.

## moneromooo-monero | 2018-03-05T22:36:01+00:00
+resolved

It's not using rct though, people who want to use this will need to decide when they want to switch.

# Action History
- Created by: amiuhle | 2017-12-27T16:43:25+00:00
- Closed at: 2018-03-05T23:00:41+00:00
