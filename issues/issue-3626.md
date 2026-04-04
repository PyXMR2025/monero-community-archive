---
title: Monerod crashes with sigbus if I try to sync from my phone
source_url: https://github.com/monero-project/monero-gui/issues/3626
author: seamasteruwu
assignees: []
labels: []
created_at: '2021-07-16T01:31:53+00:00'
updated_at: '2023-02-27T23:25:58+00:00'
type: issue
status: closed
closed_at: '2023-02-27T23:25:58+00:00'
---

# Original Description
So when i try to sync (using an sd card) monerod quickly crashes with an sigbus. It only happens if i am syncing since if i have no internet monerod works however is useless since i can't use monerod without an blockchain. It also isn't because my blockchain is corrupted since i'm trying to sync from scratch. I am using the latest version of the monero wallet and the lastest version of termux. 
[monero.error.log](https://github.com/monero-project/monero-gui/files/6827158/monero.error.log)
That is what i get by running
./monerod --data-dir ~/my/sdcard/bitmonero --log-level 4 > monero.error.log
before i get SIGBUS. I am running the precompiled monero binaries from getmonero.org. I'm in android 8.1 32 bits.

# Discussion History
## seamasteruwu | 2021-07-16T01:33:54+00:00
Also im writing the issue here because i cant do it in the main monero repo since i must have contribuited there.

## djemilbakhti | 2021-07-21T11:27:35+00:00
> So when i try to sync (using an sd card) monerod quickly crashes with an sigbus. It only happens if i am syncing since if i have no internet monerod works however is useless since i can't use monerod without an blockchain. It also isn't because my blockchain is corrupted since i'm trying to sync from scratch. I am using the latest version of the monero wallet and the lastest version of termux.
> [monero.error.log](https://github.com/monero-project/monero-gui/files/6827158/monero.error.log)
> That is what i get by running
> ./monerod --data-dir ~/my/sdcard/bitmonero --log-level 4 > monero.error.log
> before i get SIGBUS. I am running the precompiled monero binaries from getmonero.org. I'm in android 8.1 32 bits.

you can use monerod without blockchain 
just run 
./monerod --no-sync --bootstrap-daemon-address auto


## selsta | 2023-02-27T23:25:58+00:00
Please open an issue here if you continue to have issues: https://github.com/monero-project/monero

# Action History
- Created by: seamasteruwu | 2021-07-16T01:31:53+00:00
- Closed at: 2023-02-27T23:25:58+00:00
