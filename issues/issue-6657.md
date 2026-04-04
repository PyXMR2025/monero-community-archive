---
title: 'CLI Wallet v0.16.0.0- Error: Error mining to daemon: Found nonce, but daemon
  did not credit us with the expected amount'
source_url: https://github.com/monero-project/monero/issues/6657
author: downystreet
assignees: []
labels: []
created_at: '2020-06-14T16:38:02+00:00'
updated_at: '2022-07-20T20:51:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
OS: CentOS 8, wallet: v0.16.0.0
On a fresh compile when using the refresh command in the wallet, the wallet fails to automatically start mining for RPC payment. For example, I start the wallet and use the refresh command and I get Error: refresh failed: payment required... Blocks received: 0. Error: Error mining to daemon: found nonce, but daemon did not credit us with the expected amount. Error: Failed to start mining for RPC payment. Usually I would just wait and the wallet would mine some RPC  to start loading the blocks however it is not. When I manually use the command 'start_mining_for_rpc' the wallet then starts mining and I am able to use the refresh command and it starts loading the blocks. This happened when I was restoring a wallet using the --restore-deterministic-wallet command. I'm not seeing this problem when creating new wallet keys.

Update: I restored a second wallet using the --restore-deterministic-wallet command and it initially started to refresh but then it throws the same error: Error: Error mining to daemon: found nonce, but daemon did not credit us with the expected amount. Error: Failed to start mining for RPC payment. After it throws this error it ceases to mine for RPC, so as I keep using the refresh command it does not load the blocks and keeps throwing that three line error.

Update 2: After using the command 'start_mining_for_rpc' it gives the usual output and then throws an error. Error: Error mining to daemon: found nonce, but daemon did not credit us with the expected amount. Error: Failed to start mining for RPC payment. This was from the restored wallet.

Update3: Tried using a new wallet and after 2 refreshes from RPC it then throws the 3 line error listed above. When using the refresh command again it acts like it is loading some blocks but then throws error Error: refresh failed: payment required.. Blocks recieved: 0. When I see it loading some blocks I would expect there to be a number greater than 0 in the blocks received section. Each time a refresh command is done it acts like its loading the blocks and then throws the error of Blocks received: 0 and also throws the other errors randomly. However, after multiple refresh attempts it actually gets to a synced state. The restore from height was set at 2000000.

Update 4: When running the daemon regularly without any rpc payment commands there is no refresh problem in any wallet. 

I've also noticed that when I use the rpc_payments command in the daemon, none of the clients connected are producing any RPC payments except my wallet.

Update5: After restarting daemon with rpc commands and restarting restored wallet, refresh is only throwing error Error: refresh failed: payment required.. Blocks received: 0. After using refresh again it is now synced saying: Refresh done, blocks recieved: 25. The restored wallet is now synced.

Update 6: After restarting the restored wallet once again about a minute after being synced, the first refresh gives error: starting refresh failed: payment required.. Blocks received: 0. On the second refresh command it is now synced, Refresh done, blocks received: 3. I'm not seeing the 3 line error now for whatever reason.

On the getmonero.org version I created a new wallet and it acted as expected throwing error and telling me a number of blocks received, however when I do a --restore-deterministic-wallet it is giving me multiple errors Error: Error mining to daemon: found nonce, but daemon did not credit us with the expected amount. Error: Failed to start mining for RPC payment.  and saying 0 blocks received on every error output when doing a refresh command. After restarting the wallet I am not seeing the daemon did not credit us error but still showing blocks received 0 after every refresh command. It is however syncing because its asking me for a password to confirm outputs.

# Discussion History
## Cactii1 | 2022-07-20T20:51:06+00:00
Very old support request.

Propose to close.

# Action History
- Created by: downystreet | 2020-06-14T16:38:02+00:00
