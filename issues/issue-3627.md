---
title: Support (or at least improve error message) for monero daemons that use rpc-login
source_url: https://github.com/xmrig/xmrig/issues/3627
author: karldray
assignees: []
labels:
- bug
- review later
created_at: '2025-01-31T23:13:48+00:00'
updated_at: '2025-06-16T15:11:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
My monero daemon uses the `--rpc-login=my_user:my_password` option, which adds HTTP digest authentication to the RPC API. (This way I can sync my wallet from anywhere without letting others poke around on my node via the RPC API.)

It works with the official monero client and Cake wallet, and the following command works as expected on the machine running xmrig:

`curl -k -u my_user:my_password --digest https://my_node:18089/get_height`

But when try to mine to this node:

`xmrig -o my_node:18089 -a rx/0 --cuda -u my_wallet_address --daemon --tls --userpass=my_user:my_password`

XMRig reports  `connect error: "Invalid wallet address."`.

This is misleading, since the wallet address is valid (it works in other pool configurations), and I get the same error if I use `--userpass=my_user:wrong_password`, so it seems like xmrig is incorrectly interpreting the authentication failure as wallet address problem.

[This StackExchange answer](https://monero.stackexchange.com/questions/13893/how-connect-to-monerod-via-xmrig) says xmrig doesn't support daemons that use `rpc-login`. Seems like it would be easy to add.

Thanks for your attention!



# Discussion History
## SChernykh | 2025-02-01T00:20:22+00:00
@karldray XMRig doesn't support HTTP authorization which is required when rpc-login is enabled on Monero side.

# Action History
- Created by: karldray | 2025-01-31T23:13:48+00:00
