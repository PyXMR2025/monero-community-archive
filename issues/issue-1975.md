---
title: 'Wallet CLI: show_transfers pool does not work'
source_url: https://github.com/monero-project/monero/issues/1975
author: iDunk5400
assignees: []
labels: []
created_at: '2017-04-14T17:20:02+00:00'
updated_at: '2017-04-17T19:43:15+00:00'
type: issue
status: closed
closed_at: '2017-04-17T19:43:15+00:00'
---

# Original Description
`show_transfers pool` does not return anything when an incoming TX is in the daemon's mempool.
There was another report of the issue on IRC by another user.

Tested with version 0.10.3.1-release of daemon and wallet.

# Discussion History
## moneromooo-monero | 2017-04-14T19:15:33+00:00
Hmm. Works for me...


## moneromooo-monero | 2017-04-16T11:01:39+00:00
If anyone has this happening, it'd be useful to have a level 2 log of the *wallet*, from the start (ie, setting log level 2 after you see a tx missing is not enough, I'd need to see the log on the first refresh where the incoming tx would have been seen). Since there are probably going to be private data (which outputs you own), feel free to add a password to the paste on fpaste.org, and PM me the password on IRC (moneromooo).

## iDunk5400 | 2017-04-17T15:11:25+00:00
I made three transfers in two sessions from my Linux testnet wallet to my Windows testnet wallet. These are separate Monero accounts. The receiving wallet's daemon was open and synced the whole time.

In the first session, the receiving wallet was open when the first two transactions were made. For the first transfer, `show_transfers pool` did not show anything in the receiving wallet's shell. The transaction came through relatively quickly as `print_tx` in the daemon showed it was already included in a block.
I made a second transfer which was then picked up by `show_transfers pool` only once (the first time it was issued) by the receiving wallet. `print_tx` showed the transaction was in the receiving daemon's pool. The transaction was included in a block after a couple of minutes and showed up in the receiving wallet.

In the second session, the receiving wallet was closed when the transfer was made, which is equivalent to the situation when I noticed this behaviour after a pool payout on mainnet. The transfer, consisting of two transactions, was made and the receiving wallet was then opened. `show_transfers pool` never showed anything in the receiving wallet until the transactions were included in a block. `print_tx` in the daemon printed out the transactions, but I was unable to determine if they were in the pool at the time or already mined due to the amount of outputs used and limited scrollback. I assume they were in the pool because it took some time for them to be mined.

[Wallet's terminal log](https://paste.fedoraproject.org/paste/~-y9MTY27G7u5CTz6zJ3Nl5M1UNdIGYhyRLivL9gydE=)
[monero-wallet-cli.log](https://paste.fedoraproject.org/paste/CgcOHhis04HkjA4JYNxqtF5M1UNdIGYhyRLivL9gydE=)

## moneromooo-monero | 2017-04-17T19:11:50+00:00
Thanks. https://github.com/monero-project/monero/pull/1989

## iDunk5400 | 2017-04-17T19:13:51+00:00
You are most welcome :)

# Action History
- Created by: iDunk5400 | 2017-04-14T17:20:02+00:00
- Closed at: 2017-04-17T19:43:15+00:00
