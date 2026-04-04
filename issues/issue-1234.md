---
title: monero.win.x64.v0-10-0-0 monero-wallet-cli clouses after password input
source_url: https://github.com/monero-project/monero/issues/1234
author: Pilotvt
assignees: []
labels: []
created_at: '2016-10-18T07:32:21+00:00'
updated_at: '2017-08-07T18:42:16+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:42:16+00:00'
---

# Original Description
Hi I'm new here so sory for my dullness in advance.
monero.win.x64.v0-10-0-0 monero-wallet-cli clouses after password input
I enter wallet name, then pass, and it show some error, but it clouses before i can read it.


# Discussion History
## dEBRUYNE-1 | 2016-10-18T10:43:56+00:00
It might be that you are entering the wrong password. Could you check the `monero-wallet-cli` log file for errors? It's called `monero-wallet-cli.txt` if I recall correctly. 


## Pilotvt | 2016-10-18T12:52:16+00:00
2016-Oct-18 15:51:36.930709 Monero 'Wolfram Warptangent' (v0.10.0.0-release)
2016-Oct-18 15:51:36.930709 Setting log level = 0
2016-Oct-18 15:51:36.930709 default_log: C:\Users\Vitaly\Downloads\monero.win.x64.v0-10-0-0\monero-wallet-cli.log
2016-Oct-18 15:51:36.930709 Logging at log level 0 to C:\Users\Vitaly\Downloads\monero.win.x64.v0-10-0-0\monero-wallet-cli.log
2016-Oct-18 15:51:46.725226 Loaded wallet keys file, with public address: 44VsJWdhEzUNZc5jtG8yds8aZjVFHT61heQGV57iLq1R1u6HdRyWsb8gprgRWrW4h2YvWk9hisfAvAv1LSau9DXQR52iQSo
2016-Oct-18 15:51:47.257411 Error: failed to load wallet: std::bad_alloc
2016-Oct-18 15:51:47.319912 Error: You may want to remove the file "monerovt2" and try again
2016-Oct-18 15:51:47.319912 ERROR C:/msys64/DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:1432 failed to open account
2016-Oct-18 15:51:47.319912 ERROR C:/msys64/DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:3928 Failed to initialize wallet


## moneromooo-monero | 2016-10-18T15:07:14+00:00
Known bug with the prebuilt binaries. See https://github.com/monero-project/monero/issues/1106


## Pilotvt | 2016-10-18T19:24:45+00:00
It does help, but I encountered another problem: the wallet started to synchronise and windows freezed (probably because I flash GPUs) I restarted the system, and tryed to start monerod - it shuts down by itself.


## moneromooo-monero | 2016-10-22T10:24:14+00:00
Paste the error message(s) monerod outputs.


## Pilotvt | 2016-10-29T07:55:11+00:00
it just clousing, no log file for it.


## moneromooo-monero | 2017-08-07T17:26:19+00:00
Now fixed thanks to the switch to portable boost format.

+resolved

# Action History
- Created by: Pilotvt | 2016-10-18T07:32:21+00:00
- Closed at: 2017-08-07T18:42:16+00:00
