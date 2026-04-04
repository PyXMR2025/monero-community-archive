---
title: cant open wallet with monero-wallet-cli.
source_url: https://github.com/monero-project/monero/issues/8833
author: hubgitbb
assignees: []
labels: []
created_at: '2023-04-28T13:58:46+00:00'
updated_at: '2023-04-28T21:37:38+00:00'
type: issue
status: closed
closed_at: '2023-04-28T21:37:38+00:00'
---

# Original Description
Hi
i have build the p2pool with Docker Compose and a new wallet was generated. i have the wallet name and password but cannot login to it.  there is no error message. it looks like the wallet does not exist.

monero-wallet-cli.log
**INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO**




# Discussion History
## selsta | 2023-04-28T14:01:10+00:00
Your log doesn't show anything. What is the command line output when opening the wallet?

## hubgitbb | 2023-04-28T14:02:26+00:00
monero@dffd5696461f:~$ monero-wallet-cli
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Fluorine Fermi' (v0.18.2.2-release)
Logging to monero-wallet-cli.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit):

## selsta | 2023-04-28T14:03:26+00:00
You have to enter the wallet name that you want to open.

## hubgitbb | 2023-04-28T14:08:33+00:00
if i enter my wallet name i get
"No wallet found with that name. Confirm creation of new wallet named"

## selsta | 2023-04-28T14:10:04+00:00
It searches for the wallet in the same directory as the monero-wallet-cli binary. Is the wallet in the same directory? If not, try to manually set the path to the wallet using the `--wallet-file` flag.

## hubgitbb | 2023-04-28T14:21:47+00:00
i cant find any wallet file that eq my walletname

## selsta | 2023-04-28T14:23:13+00:00
You have to create a wallet first before opening it. If you have one created you also have a wallet and wallet.keys file.

## hubgitbb | 2023-04-28T14:36:14+00:00
ok i have the wallet name, wallet password, the 25 words for recreating the wallet but i cant find the wallet file and wallet keys file
is it possible that docker did not create the files?

## selsta | 2023-04-28T14:39:25+00:00
I am not familiar with your docker setup. The wallet file gets created in the same folder as the monero-wallet-cli binary by default.

Why even use docker to run monero-wallet-cli? Just run it locally and avoid all this extra complexity.

## plowsof | 2023-04-28T14:42:58+00:00
"where does docker store files" / "where are my docker volumes located" is out of scope. once you find them point the monero wallet cli to it with `--wallet-file` as instructed above. 

## hubgitbb | 2023-04-28T15:05:59+00:00
My volumes are the defaults from the docker compose file
monero:/home/monero/.bitmonero:rw
/dev/null:/home/monero/.bitmonero/bitmonero.log:rw
/dev/hugepages:/dev/hugepages:rw

But the wallet files are not in there

## selsta | 2023-04-28T15:09:09+00:00
This is not the right place to get support on how to use docker.

I can only say again that I would suggest you to run monero-wallet-cli natively.

## hubgitbb | 2023-04-28T16:26:02+00:00
OK thanks for the help

## selsta | 2023-04-28T21:37:38+00:00
The docker compose is for running **monerod + p2pool**. It's not for running monero-wallet-cli. See https://github.com/SChernykh/p2pool/tree/master/docker-compose

> Run your own Monero Node + P2Pool + XMRig in Docker

It does not expose any wallet files. Run monero-wallet-cli locally on your computer and you won't have any issues.

# Action History
- Created by: hubgitbb | 2023-04-28T13:58:46+00:00
- Closed at: 2023-04-28T21:37:38+00:00
