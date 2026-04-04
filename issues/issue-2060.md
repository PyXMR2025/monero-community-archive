---
title: Confusing interaction between simplewallet's --restore-deterministic-wallet
  and --wallet-file
source_url: https://github.com/monero-project/monero/issues/2060
author: zagaberoo
assignees: []
labels: []
created_at: '2017-05-31T17:12:13+00:00'
updated_at: '2017-06-18T15:28:02+00:00'
type: issue
status: closed
closed_at: '2017-06-18T15:28:02+00:00'
---

# Original Description
Reproduction:

    $ monero-wallet-cli --wallet-file wal --restore-deterministic-wallet --password="asdf" --electrum-seed="gypsy annoyed renting delayed object ostrich vinegar suffice enigma excess paradise five ruling ulcers upon gotten eskimos unquoted plotting cinema jamming bimonthly skulls sleepless delayed"
    Monero 'Wolfram Warptangent' (v0.10.3.1-release)
    Logging to monero-wallet-cli.log
    Error: failed to generate new wallet: failed to save file "": No such file or directory

The presence of --wallet-file seems to skip the file prompt, but then the value is pulled from --generate-new-wallet instead, which is the empty string.

Additionally, unix hidden file droppings are left behind as a quirk of the empty string being used as the base filename:

    $ find .
    .
    ./.keys
    ./.new
    ./monero-wallet-cli.log
    ./.address.txt

Simply failing fast by checking for the empty string [here](https://github.com/monero-project/monero/blob/v0.10.3.1/src/simplewallet/simplewallet.cpp#L1222) would do the trick.

Should I put together a pull request that implements this?

# Discussion History
## moneromooo-monero | 2017-06-04T09:47:06+00:00
Yes, thanks.

# Action History
- Created by: zagaberoo | 2017-05-31T17:12:13+00:00
- Closed at: 2017-06-18T15:28:02+00:00
