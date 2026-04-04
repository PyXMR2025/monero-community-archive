---
title: monerod regtest mode has issues in the v0.18.1.1 release
source_url: https://github.com/monero-project/monero/issues/8600
author: dimalinux
assignees: []
labels: []
created_at: '2022-09-29T10:40:45+00:00'
updated_at: '2022-11-04T12:33:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Test code that I have written for interacting with `monerod` is breaking with the v0.18.1.1 release. When I try to refresh wallets, I get this error:
> Unexpected hard fork version v16 at height 1. Make sure the node you are connected to is running the latest version

In hopes that it will help replicate the problem quickly, here is a bash script:
```
#!/bin/bash
set -e
set -x

# This script shows a problem with the v0.18.1.1 release of Monero when running
# tests in the regtest mode. Calling refresh on a wallet will generate the error
# message:
#  Unexpected hard fork version v16 at height 1.
#  Make sure the node you are connected to is running the latest version

MONEROD_PORT=18081
WALLET_PORT=18084

MONERO_BIN_DIR="${PWD}/monero-bin"
DATA_DIR="${PWD}/test-data"
WALLET_DIR="${DATA_DIR}/wallet"
# Test only address (from Mastering Monero)
MINE_ADDRESS="4BKjy1uVRTPiz4pHyaXXawb82XpzLiowSDd8rEQJGqvN6AD6kWosLQ6VJXW9sghopxXgQSh1RTd54JdvvCRsXiF41xvfeW5"

monero-rpc-request() {
	local port="${1:?}"   # can be a monerod or monero-wallet-rpc port
	local method="${2:?}" # RPC method name
	local params="${3:?}" # JSON parameters to method
	curl --http0.9 "http://localhost:${port}/json_rpc" \
		--silent \
		--show-error \
		-d "{\"jsonrpc\":\"2.0\",\"id\":\"0\",\"method\":\"${method}\",\"params\":${params}" \
		-H 'Content-Type: application/json' \
		-w "\n"
}

create-wallet() {
	local port="${1:?Please provide a monero wallet port}"
	local wallet_name="${2:?Please specify wallet name}"
	local params='{"filename":"'"${wallet_name}"'","password":"","language":"English"}'
	monero-rpc-request "${port}" "create_wallet" "${params}"
}

refresh-wallet() {
	local port="${1:?Please provide a monero wallet port}"
	monero-rpc-request "${port}" "refresh" "{}"
}

generate-block() {
	local port="${1:?Please provide monerod port}"
	local params="{\"amount_of_blocks\":1,\"wallet_address\":\"${MINE_ADDRESS}\"}"
	monero-rpc-request "${port}" "generateblocks" "${params}"
}

# Kill any previous running instances
pkill --echo --uid "${UID}" --full '/monerod .* --regtest ' || true
pkill --echo --uid "${UID}" --full '/monero-wallet-rpc ' || true
sleep 2

# Start with fresh data/wallet directories
rm -rf "${DATA_DIR}"
mkdir -p "${DATA_DIR}" "${WALLET_DIR}"

# Start monerod in regtest mode
"${MONERO_BIN_DIR}/monerod" \
	--detach \
	--regtest \
	--offline \
	"--data-dir=${DATA_DIR}/monerod" \
	"--pidfile=${DATA_DIR}/monerod.pid" \
	--fixed-difficulty=1 \
	--rpc-bind-ip=127.0.0.1 \
	"--rpc-bind-port=${MONEROD_PORT}"
sleep 5

# Start a wallet client
"${MONERO_BIN_DIR}/monero-wallet-rpc" \
	--detach \
	--rpc-bind-ip 127.0.0.1 \
	--rpc-bind-port "${WALLET_PORT}" \
	--pidfile="${DATA_DIR}/monero-wallet-rpc.pid" \
	--log-file="${DATA_DIR}/monero-wallet-rpc.log" \
	--disable-rpc-login \
	--wallet-dir "${WALLET_DIR}"
sleep 2

create-wallet "${WALLET_PORT}" test-wallet
generate-block "${MONEROD_PORT}"
# Refresh below will generate an error on v0.18.1.1, but worked fine with v0.18.1.0 and earlier.
refresh-wallet "${WALLET_PORT}"
```

# Discussion History
## j-berman | 2022-09-29T11:31:13+00:00
You can start your wallet RPC client with the flag `--allow-mismatched-daemon-version`

## selsta | 2022-09-29T13:19:55+00:00
Also try to compile `v0.18.1.2` in addition to `--allow-mismatched-daemon-version`.

## dimalinux | 2022-09-29T18:33:20+00:00
@j-berman's solution worked! I didn't try compiling the unreleased version mentioned by @selsta.

My `monerod` and `monero-wallet-rpc` binaries are from the same release, so this workaround is not obvious. I'll let a Monero developer decided if this ticket should be closed or not.  Maybe whatever settings are made by `--allow-mismatched-daemon-version` should be automatic when `--regtest` is passed?  My immediate problem is resolved. Thanks!

## delta1 | 2022-11-04T12:33:24+00:00
Thanks @dimalinux @j-berman - confirmed the same issue for me in regtest and the same flag works around the issue. 

# Action History
- Created by: dimalinux | 2022-09-29T10:40:45+00:00
