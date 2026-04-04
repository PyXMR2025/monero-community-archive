---
title: rpc transfer failed:real_out_found
source_url: https://github.com/monero-project/monero/issues/6212
author: DreamHackchosenone
assignees: []
labels: []
created_at: '2019-12-03T09:42:11+00:00'
updated_at: '2022-07-20T20:00:00+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:00:00+00:00'
---

# Original Description
I have two accounts, One account can send transactions, but using the other account will fail
The account that cannot send transactions. Today I registered some sub-account addresses.
here is the error log:
Monero 'Boron Butterfly' (v0.14.1.2-release)
*********
W Requested ring size 1 too low, using 11
W WARNING: no two valid DNS TXT records were received
E !real_out_found. THROW EXCEPTION: error::wallet_internal_error

# Discussion History
## moneromooo-monero | 2019-12-03T12:08:05+00:00
0.14.1.2 is too old to work on the current network. You need at least 0.15.0.0, though 0.15.0.1 is prefered. Though for wallet_internal_error should not happen either way. Start the wallet with --log-level 2 and it'll display more info about this.

## DreamHackchosenone | 2019-12-03T14:14:54+00:00
still dont understand what happened
2019-12-03 14:12:47.377	T READ ENDS: Success. bytes_tr: 170
2019-12-03 14:12:47.377	T http_stream_filter::parse_cached_header(*)
2019-12-03 14:12:47.377	T READ ENDS: Success. bytes_tr: 9689
2019-12-03 14:12:47.378	E !real_out_found. THROW EXCEPTION: error::wallet_internal_error
2019-12-03 14:12:47.378	W /home/ubuntu/build/monero/src/wallet/wallet2.cpp:7981:N5tools5error21wallet_internal_errorE: Daemon response did not include the requested real output
2019-12-03 14:12:47.378	T HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 161
Content-Type: text/plain
Last-Modified: Tue, 03 Dec 2019 14:12:47 GMT
Accept-Ranges: bytes

## moneromooo-monero | 2019-12-03T16:23:34+00:00
Are you running the same daemon version as the wallet ?

## DreamHackchosenone | 2019-12-03T16:30:11+00:00
yes,  monerod and monero-wallet-rpc both are v0.15.0.0
I have two accounts, One account can send transactions, but using the other account will fail
The account that cannot send transactions. Today I registered some sub-account addresses.
2019-12-03 16:26:10.254	I Monero 'Carbon Chamaeleon' (v0.15.0.0-release)
2019-12-03 16:26:10.254	I Initializing cryptonote protocol...

Monero 'Carbon Chamaeleon' (v0.15.0.0-release)
Logging to monero-wallet-rpc.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
2019-12-03 16:28:42.360	W Loading wallet...
2019-12-03 16:28:42.361	I Generating SSL certificate

## moneromooo-monero | 2019-12-03T17:31:13+00:00
So far it looks like the daemon reorg'd and the wallet got confused.
"rescan_bc" in the wallet ought to fix this, but this should not have happened in the first place.
The failing wallet has refreshed at least once since then, right ? I'm assuming you did not disable auto refresh.

## DreamHackchosenone | 2019-12-04T01:13:59+00:00
I dont know hot to  disable auto refresh.
I started  monerod and monero-wallet-rpc with these two commands, besides I restarted monerod and monero-wallet-rpc many times
`monerod --confirm-external-bind --log-level=4 --db-sync-mode=fastest:async:10000 --config-file=/data/.bitmonero/monerod.conf`
`monero-wallet-rpc --log-level=4 --config-file=/data/.bitmonero/monero-wallet.conf --confirm-external-bind`
config-file doesn't contain keywords "refresh"

Wallet get_balance is weird
```
MoneroClient()._wallet_request('get_balance', {'account_index':0})['balance']
Out[97]: 7646742961000

a = MoneroClient()._wallet_request('get_transfers',{ 'in':True, 'account_index':0})['in']
total = 0
for i in a:
    total += i['amount']
total
Out[103]: 13016601502000
```
Why the account_index 0 balance is so much more than the total amount transferred, I did not mine
And yesterday, the balance of account_0 was still about 1XMR, and then I transferred a few XMRs from account_1 to account_0 to the current value.

## moneromooo-monero | 2020-05-17T14:38:17+00:00
Disalbing auto refresh: set auto-refresh 0

About the balance, are you saying you sent X to that wallet, and it's got more than X ? Did you send from that wallet to itself ?

## selsta | 2022-07-20T20:00:00+00:00
No reply from issue creator.

# Action History
- Created by: DreamHackchosenone | 2019-12-03T09:42:11+00:00
- Closed at: 2022-07-20T20:00:00+00:00
