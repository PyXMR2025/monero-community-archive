---
title: monero-wallet-rpc does not reliably sync if started without --daemon-address
source_url: https://github.com/monero-project/monero/issues/8776
author: woodser
assignees: []
labels:
- reproduction needed
created_at: '2023-03-14T19:19:20+00:00'
updated_at: '2025-07-23T06:17:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I observe a difference in behavior when monero-wallet-rpc is started with a `--daemon-address` connection versus without any connection, creating a wallet, and then setting the connection with `set_daemon`.

If the connection is set when monero-wallet-rpc is started, the wallet reliably syncs, whereas if no connection is provided on startup, the sync (or `refresh`) often hangs or takes much longer.

This is observed using remote daemons.

# Discussion History
## j-berman | 2023-03-14T22:52:22+00:00
Haven't been able to repro this behavior, but a few questions to help debug:

Are the daemons you're using compiled from source or release binaries? edit: also do you know what OS the daemons are running on?

Would you be ok with calling `set_daemon` with `"ssl_support": "disabled"` and seeing if the issue persists, just to see if ssl is the issue here?

Could you share log level 2 output on an unreliable sync?

## woodser | 2023-03-15T14:09:52+00:00
These are from self compiled binaries connected to hosted stagenet daemons (I don't know their OS).

It will be a while before I can retest, but the issue was mostly regular in my environment.

## plowsof | 2023-03-15T14:38:17+00:00
watching the output with --log-level 2 i notice these lines with `set_daemon` (they seem to not appear when starting rpc with --daemon-address`) so i notice a difference in logs with/without --daemon-address 
```
2023-03-15 14:34:15.600	D Pulled blocks: blocks_start_height 2757000, count 703, height 2757703, node height 2842578
2023-03-15 14:34:15.654	I Refresh done, blocks received: 795, balance (all accounts): 175.784949954333, unlocked: 175.784949954333
2023-03-15 14:34:16.710	D Already seen <d96139a9b32dc0c7797242964d304df2e7a1a23dbed1f27cc7e4354289542613>, and not for us, skipped
2023-03-15 14:34:16.710	I Found new pool tx: <210fc31e3332e6be03eaf4a0823f2e6e63257a3830d2c4dfab372148e7dd3a43>
2023-03-15 14:34:16.711	D Already seen <67464e94b479146f92da64cd25ab6f81eaa465af718f8d37ecad13c3ca2f8948>, and not for us, skipped
2023-03-15 14:34:16.711	D Already seen <ed12abeaaa578c63f020e8bf3472992ea000becc63220ed36df66cfb4828d668>, and not for us, skipped
2023-03-15 14:34:16.711	D Already seen <53e2f36f782e7d06e3a3e4a62fee37589a857e15007074e7e9094efbd6a44fa1>, and not for us, skipped
2023-03-15 14:34:16.711	I Found new pool tx: <9b7c24623431c49446757e8b98057d31403644cf94c6e9e4b0da04f65a140dc6>
2023-03-15 14:34:16.711	I Found new pool tx: <40706d6bad500ae874a5164c8f433a891994abce45800cf74e1598cd9ecb1fec>
2023-03-15 14:34:16.711	D asking for 3 transactions
2023-03-15 14:34:16.750	D Got 1 and OK
2023-03-15 14:34:16.750	D Pulling blocks: start_height 0
2023-03-15 14:34:21.433	D Pulled blocks: blocks_start_height 2757000, count 703, height 2757703, node height 2842578
2023-03-15 14:34:21.479	D Pulling blocks: start_height 0
```

```
./monero-wallet-rpc --rpc-bind-port 18082 --disable-rpc-login --wallet-file ccs --password "" --log-level 2
```
```
curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"set_daemon","params": {"address":"http://node2.monerodevs.org:18089"}},' -H 'Content-Type: application/json'
```
observe the above print outs^ (pulling blocks...) which i dont see when starting with --daemon-address

## gprethesh | 2025-07-23T06:17:39+00:00
This occurs when you keep the wallet-rpc on a server more than 10+ hrs and it will fail to fetch transactions. 

# Action History
- Created by: woodser | 2023-03-14T19:19:20+00:00
