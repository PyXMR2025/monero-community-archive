---
title: Issues when starting monero-wallet-rcp
source_url: https://github.com/monero-project/monero/issues/7988
author: S1700
assignees: []
labels: []
created_at: '2021-10-03T21:56:08+00:00'
updated_at: '2021-10-06T02:37:11+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:20:45+00:00'
---

# Original Description
im in the bin dir and i have set the path but when I run It with this command `./monero-wallet-rpc --wallet-file monero_pool --password BHFy=passwrrd --rpc-bind-port 18083 --rpc-bind-ip 127.0.0.1 --disable-rpc-login` i get the error:
```
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.0.0-6b824c9ed)
Logging to ./monero-wallet-rpc.log
2021-10-03 21:55:40.280 W Loading wallet...
2021-10-03 21:55:41.437 E e || !exists. THROW EXCEPTION: error::file_not_found
2021-10-03 21:55:41.437 E Wallet initialization failed: file not found "moneropool.keys"
```

Thanks!

# Discussion History
## selsta | 2021-10-03T22:03:32+00:00
Something doesn't add up.

Your command says `--wallet-file monero_pool` and your log says `failed: file not found "moneropool.keys"`.

## S1700 | 2021-10-04T07:28:56+00:00
ikr that's what i was thinking

## S1700 | 2021-10-04T07:46:59+00:00
should i make a .keys file if so what should i put in the file

## selsta | 2021-10-04T16:31:20+00:00
Can you type `ls -l` inside the `bin` dir and post the output here.

## S1700 | 2021-10-05T13:00:41+00:00
```
root@MoneroPool:~/monero/build/Linux/master/release/bin#  ls -l
total 120564
-rwxr-xr-x 1 root root  7826440 Oct  3 21:02 monero-blockchain-ancestry
-rwxr-xr-x 1 root root  6730200 Oct  3 21:02 monero-blockchain-depth
-rwxr-xr-x 1 root root  6834024 Oct  3 21:01 monero-blockchain-export
-rwxr-xr-x 1 root root  7169056 Oct  3 21:02 monero-blockchain-import
-rwxr-xr-x 1 root root  3317120 Oct  3 21:02 monero-blockchain-mark-spent-outputs
-rwxr-xr-x 1 root root  6769040 Oct  3 21:01 monero-blockchain-prune
-rwxr-xr-x 1 root root  6739768 Oct  3 21:02 monero-blockchain-prune-known-spent-data
-rwxr-xr-x 1 root root  6722504 Oct  3 21:01 monero-blockchain-stats
-rwxr-xr-x 1 root root  6733616 Oct  3 21:03 monero-blockchain-usage
-rwxr-xr-x 1 root root 15023312 Oct  3 21:00 monerod
-rwxr-xr-x 1 root root  1767984 Oct  3 20:58 monero-gen-ssl-cert
-rwxr-xr-x 1 root root 14927000 Oct  3 20:58 monero-gen-trusted-multisig
-rwxr-xr-x 1 root root 16300216 Oct  3 20:58 monero-wallet-cli
-rwxr-xr-x 1 root root 16557024 Oct  3 20:57 monero-wallet-rpc
-rw------- 1 root root     8455 Oct  3 21:55 monero-wallet-rpc.log
root@MoneroPool:~/monero/build/Linux/master/release/bin#

```

## selsta | 2021-10-05T13:03:54+00:00
I don't see any wallet file in your folder.

According to your command it should be in the same folder aa `monero-wallet-rpc`.

You have to specify the correct path to your wallet file.


## S1700 | 2021-10-05T13:04:45+00:00
that is the same folder as monero-wallet-rpc

## selsta | 2021-10-05T13:06:38+00:00
Yes, but there is no wallet file. You have to generate one first.

## S1700 | 2021-10-05T13:07:36+00:00
how do i generate one


## selsta | 2021-10-06T02:20:45+00:00
Just create a wallet file with monero-wallet-cli for example. Closing as there doesn't seem to be a bug here.

## selsta | 2021-10-06T02:37:11+00:00
See also the example in this comment: https://github.com/monero-project/monero/issues/7431#issue-823171923

# Action History
- Created by: S1700 | 2021-10-03T21:56:08+00:00
- Closed at: 2021-10-06T02:20:45+00:00
