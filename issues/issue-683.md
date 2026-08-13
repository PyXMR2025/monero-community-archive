---
title: 'Wallet cannot sync with 0.1.0-preview: `/get_blocks.bin` and `/get_hashes.bin`
  return HTTP 500, `get_transactions`/`is_key_image_spent` missing'
source_url: https://github.com/Cuprate/cuprate/issues/683
author: R-Caser
assignees: []
labels:
- C-bug
- C-slop
created_at: '2026-08-12T02:11:58+00:00'
updated_at: '2026-08-12T09:28:55+00:00'
type: issue
status: closed
closed_at: '2026-08-12T09:26:30+00:00'
---

# Original Description
## Environment

- `cuprated` 0.1.0-preview "Kesterite" (release 2026-08-01), Linux x86_64
- `--version`: `{ major_version: 0, minor_version: 1, patch_version: 0, rpc_major_version: 3, rpc_minor_version: 15, rpc_version: 196623, hardfork: 16 }`
- Network: Mainnet, fully synced (height ~3,738,000)
- RPC config: restricted `0.0.0.0:18088`, unrestricted `127.0.0.1:18089`

## What we tried — both with and without credentials

We connected standard Monero wallets (`monero-wallet-cli`/GUI and Cake Wallet) to the unrestricted RPC in three configurations, to rule out auth/proxy issues:

1. **With credentials** — via a reverse proxy on port `18189` requiring HTTP Basic Auth (`cuprate` / `********`), forwarding to `127.0.0.1:18089`. Result: **handshake OK, sync fails**.
2. **Without credentials** — the same proxy with Basic Auth temporarily disabled (plain pass-through on `18189` → `127.0.0.1:18089`). Result: wallet **connects immediately** (proves auth was only a connection barrier), but **sync still fails** with the same HTTP 500.
3. **Direct, no proxy, no auth** — requests straight to `127.0.0.1:18089`. Result: the same failures reproduce with `curl` (see below).

**Conclusion of the matrix**: the `500`/missing-method errors are **independent of authentication and transport** — they come from inside cuprated's RPC implementation.

## Reproduction (direct, no auth involved)

```bash
# Works
curl -X POST http://127.0.0.1:18089/json_rpc -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"0","method":"get_version"}'
curl -X POST http://127.0.0.1:18089/json_rpc -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}'
curl http://127.0.0.1:18089/get_height

# Fails
curl -X POST http://127.0.0.1:18089/get_blocks.bin -H 'Content-Type: application/json' \
  -d '{"block_ids":["0000000000000000000000000000000000000000000000000000000000000000"],"start_height":3737230,"prune":false}'
# HTTP 500, empty body

curl -X POST http://127.0.0.1:18089/get_hashes.bin -H 'Content-Type: application/json' \
  -d '{"block_ids":["0000000000000000000000000000000000000000000000000000000000000000"],"start_height":3737230,"prune":false}'
# HTTP 500, empty body

curl -X POST http://127.0.0.1:18089/json_rpc -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"0","method":"sync_info"}'
# HTTP 500

curl -X POST http://127.0.0.1:18089/json_rpc -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"0","method":"get_transactions"}'
# 422: Failed to deserialize the JSON body ... unknown variant `get_transactions`

curl -X POST http://127.0.0.1:18089/json_rpc -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"0","method":"is_key_image_spent"}'
# 422: unknown variant `is_key_image_spent`
```

## Log excerpts (`/var/log/cuprate/cuprated.log`, level debug)

```
2026-08-10T16:01:41.331174Z  INFO Starting RPC server restricted=true  address=0.0.0.0:18088
2026-08-10T16:01:41.331458Z  INFO Starting RPC server restricted=false address=127.0.0.1:18089

2026-08-10T16:12:31.295233Z ERROR response failed classification=Status code: 500 Internal Server Error latency=0 ms
2026-08-10T16:12:31.333485Z ERROR response failed classification=Status code: 500 Internal Server Error latency=0 ms
2026-08-10T16:12:53.134012Z ERROR response failed classification=Status code: 500 Internal Server Error latency=0 ms
2026-08-10T16:12:53.162107Z ERROR response failed classification=Status code: 500 Internal Server Error latency=0 ms
2026-08-10T16:15:05.438585Z ERROR response failed classification=Status code: 500 Internal Server Error latency=0 ms
2026-08-12T02:03:29.022523Z ERROR response failed classification=Status code: 500 Internal Server Error latency=0 ms
```

## Expected

`get_blocks.bin` / `get_hashes.bin` should return the requested blocks/hashes so wallets can sync (as promised by the release notes: "Wallets can now sync the blockchain and send transactions with Cuprate"). `get_transactions`, `is_key_image_spent` and `sync_info` are also needed by wallets and are currently missing/erroring.

Thanks for the great work — happy to provide more logs or test a fix.

---

## Update — additional testing (2026-08-12)

Since opening this, we tested further and found something important:

1. **Without credentials the wallet connects immediately** — after temporarily disabling HTTP Basic Auth on the reverse proxy (port `18189` → `127.0.0.1:18089`), Cake Wallet connects to the node right away. So auth was only a connection barrier, not the sync problem.

2. **But the sync endpoints still fail** — we re-tested `get_blocks.bin` / `get_hashes.bin` with multiple standard request formats (genesis block hash, real tip hash, empty `block_ids`, various `start_height` values): **all return HTTP 500 with an empty body**, and a fresh `ERROR response failed ... 500` appears in the log for each attempt.

3. **No 500 errors are logged from the wallet itself** — aside from our curl tests, there are no `get_blocks.bin` errors in the log tied to the wallet. This suggests Cake Wallet may be **silently falling back to a public node** when the sync request fails, which makes it look like the wallet is "syncing fine" even though it is not actually using this node.

**Current picture**: connection works without auth, but a real wallet sync from this node still can't happen because `get_blocks.bin` / `get_hashes.bin` return HTTP 500 (and `get_transactions`, `is_key_image_spent`, `sync_info` are missing/erroring).

Happy to run a debug build or provide more logs.


# Discussion History
## SyntheticBird45 | 2026-08-12T07:32:47+00:00
Your analysis contradicts your recent tweet that suggests that the issue authentication related, which Cuprate do not yet support. Your additional testing has also made nothing but restate your original trials.

I can reproduce your curl errors HOWEVER:

- `curl -X POST http://127.0.0.1:18089/get_blocks.bin -H 'Content-Type: application/json' \
  -d '{"block_ids":["0000000000000000000000000000000000000000000000000000000000000000"],"start_height":3737230,"prune":false}'`
is `400 Bad request` through monerod.

- `curl -X POST http://127.0.0.1:18089/get_hashes.bin -H 'Content-Type: application/json' \
  -d '{"block_ids":["0000000000000000000000000000000000000000000000000000000000000000"],"start_height":3737230,"prune":false}'`
is `400 Bad request` through monerod.

- `curl -X POST http://127.0.0.1:18089/json_rpc -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"0","method":"sync_info"}'`
`sync_info` method is unavailable over restricted RPC.

- `curl -X POST http://127.0.0.1:18089/json_rpc -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"0","method":"get_transactions"}'`
`/get_transactions` is an HTTP endpoint, not a json-rpc method. So 422 might be confusing but is expected.

- `curl -X POST http://127.0.0.1:18089/json_rpc -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"0","method":"is_key_image_spent"}'`
`/is_key_image_spent` is also an HTTP endpoint, not a json-rpc method.

Cake Wallet desktop application is broken at the moment. But fortunately Stack Wallet is working on my machine and I was able to reproduce that the wallet is NOT syncing over Cuprate. It can reliably ping the node and the request is logged, but whenever it is time to sync, the wallet fails indicating a connection failure, without anything logged on Cuprate side. This is surprising considering we confirmed this worked with core monero wallet

So I will investigate.

## SyntheticBird45 | 2026-08-12T09:15:40+00:00
@R-Caser I investigated the issue over Stack Wallet and was able to fix it by explicitly specifying the http:// protocol. Can you confirm this works over Cake Wallet ?

## SyntheticBird45 | 2026-08-12T09:26:30+00:00
@R-Caser I installed Cake wallet on desktop and its working perfectly fine. Mistakes' on you. My advice is stopping vibeslopping everything.

# Action History
- Created by: R-Caser | 2026-08-12T02:11:58+00:00
- Closed at: 2026-08-12T09:26:30+00:00
