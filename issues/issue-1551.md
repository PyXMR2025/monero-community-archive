---
title: Unable to see any transactions with wallets generated from keys on macOS
source_url: https://github.com/monero-project/monero/issues/1551
author: vickio
assignees: []
labels: []
created_at: '2017-01-09T22:05:30+00:00'
updated_at: '2017-01-13T19:36:49+00:00'
type: issue
status: closed
closed_at: '2017-01-13T19:36:49+00:00'
---

# Original Description
On macOS Sierra 10.12, I am unable to see any transactions in the CLI or GUI for wallets that were created using `--generate-from-keys`. This causes the balance to always be 0.

With `set_log 2`, I am able to see that during the blockchain scan, every block is skipped due to the account timestamp being incorrect:

>Skipped block by timestamp, height: 1220200, block time 1483989027, account time 18446744073709551615

# Discussion History
## moneromooo-monero | 2017-01-09T22:19:15+00:00
That account time is -1. Very good lead, thanks.

## moneromooo-monero | 2017-01-09T22:22:18+00:00
Can you please paste the exact command line you used to get this result (you can replace any private data with placeholders though) ?

## vickio | 2017-01-09T22:35:41+00:00
    ./monero-wallet-cli --generate-from-keys test --log-level 2

It happens for me very reliably with any starting block height and any wallet. I'm running v0.10.1.0-release, but I also compiled from head today (incorporating two unmerged PRs to fix compile errors) and it was the same.

## vickio | 2017-01-09T22:39:42+00:00
If I generate a new wallet, or restore one with `--restore-deterministic-wallet`, it works fine. It seems to only be a problem with `--generate-from-keys`.

## vickio | 2017-01-10T13:29:58+00:00
I don't have a debugging environment set up for monero, so I just added a logging line to the end of `account_base::create_from_keys` to see what the timestamp was there:

    LOG_PRINT_L2("Account creation timestamp is " << m_creation_timestamp);

When I run it with that, it logs the correct timestamp and everything works (transactions appear during scan, balance is correct). If I comment out that logging line and recompile, it goes back to the old behavior of creation timestamp -1 and skipping all blocks during scan. I thought maybe it was a compiler optimization problem, so I set `-O0` but that didn't change anything.

# Action History
- Created by: vickio | 2017-01-09T22:05:30+00:00
- Closed at: 2017-01-13T19:36:49+00:00
