---
title: 'Wallet initialization failed: reorg exceeds maximum allowed depth, use ''set
  max-reorg-depth N'' to allow it'
source_url: https://github.com/monero-project/monero/issues/7227
author: ghost
assignees: []
labels: []
created_at: '2020-12-29T20:50:00+00:00'
updated_at: '2021-02-16T02:50:47+00:00'
type: issue
status: closed
closed_at: '2021-02-16T02:50:47+00:00'
---

# Original Description
When starting the monero-wallet-rpc daemon: 

- Wallet should not be getting "initialized" if it's already a thing, I don't like that
- Where shall I "set" max-reorg-depth `N` I don't see a `--max-reorg-depth` in the 
`--help`

```
docker run --rm --net host -e DAEMON_HOST=0.0.0.0 -e WALLET_PASSWD=xxxxxx -v /home/toor/monero:/monero xmrto/monero monero-wallet-rpc --wallet-file wallet
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.0.0-e5decd0cd)
Logging to monero-wallet-rpc.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
2020-12-29 20:38:30.374 W Loading wallet...
2020-12-29 20:38:32.403 W Loaded wallet keys file, with public address: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
2020-12-29 20:38:32.805 E reorg_depth > m_max_reorg_depth. THROW EXCEPTION: error::reorg_depth_error
2020-12-29 20:38:32.817 E Wallet initialization failed: reorg exceeds maximum allowed depth, use 'set max-reorg-depth N' to allow it, reorg depth: 2041137
```
version
```

❯ docker run --rm --net host -e DAEMON_HOST=0.0.0.0 -e WALLET_PASSWD=xxxxxxxxx -v /home/toor/monero:/monero xmrto/monero monero-wallet-rpc --version
Monero 'Oxygen Orion' (v0.17.0.0-e5decd0cd)

```


- daemon is running (same version)
```
❯ docker run --rm --net host --rm  -e DAEMON_HOST=0.0.0.0  -v /home/toor/monero:/monero xmrto/monero --data-dir /monero

2020-12-29 20:46:56.097 I Monero 'Oxygen Orion' (v0.17.0.0-e5decd0cd)
2020-12-29 20:46:56.097 I Initializing cryptonote protocol...
2020-12-29 20:46:56.097 I Cryptonote protocol initialized OK
2020-12-29 20:46:56.098 I Initializing core...
2020-12-29 20:46:56.098 I Loading blockchain from folder /monero/lmdb ...
2020-12-29 20:46:56.140 I Loading checkpoints
2020-12-29 20:46:56.140 I Core initialized OK
2020-12-29 20:46:56.140 I Initializing p2p server...
2020-12-29 20:46:56.144 I p2p server initialized OK
2020-12-29 20:46:56.144 I Initializing core RPC server...
2020-12-29 20:46:56.144 I Binding on 0.0.0.0 (IPv4):28081
2020-12-29 20:46:56.989 I core RPC server initialized OK on port: 28081
2020-12-29 20:46:56.990 I Starting core RPC server...
2020-12-29 20:46:56.990 I core RPC server started ok
2020-12-29 20:46:56.990 I Starting p2p net loop...
2020-12-29 20:46:57.990 I 
2020-12-29 20:46:57.990 I **********************************************************************
2020-12-29 20:46:57.990 I The daemon will start synchronizing with the network. This may take a long time to complete.
2020-12-29 20:46:57.990 I 
2020-12-29 20:46:57.990 I You can set the level of process detailization through "set_log <level|categories>" command,
2020-12-29 20:46:57.990 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-12-29 20:46:57.990 I 
2020-12-29 20:46:57.990 I Use the "help" command to see the list of available commands.
2020-12-29 20:46:57.990 I Use "help <command>" to see a command's documentation.
2020-12-29 20:46:57.990 I **********************************************************************
2020-12-29 20:46:58.697 I [185.99.254.10:18080 OUT] Sync data returned a new top block candidate: 366518 -> 2263030 [Your node is 1896512 blocks (6.0 years) behind] 
2020-12-29 20:46:58.697 I SYNCHRONIZATION started
```


# Discussion History
## xiphon | 2020-12-29T21:01:38+00:00
Please provide the steps to reproduce the issue. I will look into it if i get it reproduced.

## ghost | 2020-12-29T21:05:58+00:00
this error manifests from new wallet generation as well


```
❯ docker run --rm --net host --rm  -e DAEMON_HOST=0.0.0.0  -v /home/toor/monero:/monero xmrto/monero monero-wallet-cli --create-address-file --password password --mnemonic-language English --generate-new-wallet /monero/wallet

This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Oxygen Orion' (v0.17.0.0-e5decd0cd)
Logging to monero-wallet-cli.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
Generated new wallet: 47dKqri9EfCMdz88aYxfiQHkz492cKetFU5tgjrNcF1VHqahE4XDj5aHDNEhkRjArFgFv4v3t3qk1CSLyxTuH2GZTc9eysr
View key: 1178df07828916fa3788af1b5ec80b0200d9d92ea4ecf9ee8e5b392a3a27bb01
**********************************************************************
Your wallet has been generated!
To start synchronizing with the daemon, use the "refresh" command.
Use the "help" command to see a simplified list of available commands.
Use "help all" command to see the list of all available commands.
Use "help <command>" to see a command's documentation.
Always use the "exit" command when closing monero-wallet-cli to save 
your current session's state. Otherwise, you might need to synchronize 
your wallet again (your wallet keys are NOT at risk in any case).


NOTE: the following 25 words can be used to recover access to your wallet. Write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.

poker occur calamity shelter nuisance tuesday sawmill rotate
hedgehog amply abbey aztec gadget jostle typist semifinal
pancakes dosage gnaw vexed memoir fuselage inline jingle sawmill
**********************************************************************
Warning: using an untrusted daemon at http://0.0.0.0:28081
Using a third party daemon can be detrimental to your security and privacy
You are strongly encouraged to connect to the Monero network using your own daemon
If you or someone you trust are operating this daemon, you can use --trusted-daemon
Using an untrusted daemon, skipping background mining check
If you are new to Monero, type "welcome" for a brief overview.
Starting refresh...
Error: refresh failed: refresh error: reorg exceeds maximum allowed depth, use 'set max-reorg-depth N' to allow it, reorg depth: 2182500. Blocks received: 0
Background refresh thread started
[wallet 47dKqr]: 
❯ 

```

and the new wallet is also unusable due to the `max-reorg-depth` threshold breach 

```
 docker run --rm --net host -e DAEMON_HOST=0.0.0.0 -e WALLET_PASSWD=password -v /home/toor/monero:/monero xmrto/monero monero-wallet-rpc --wallet-file wallet
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.0.0-e5decd0cd)
Logging to monero-wallet-rpc.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
2020-12-29 21:06:59.600 W Loading wallet...
2020-12-29 21:07:00.570 W Loaded wallet keys file, with public address: 47dKqri9EfCMdz88aYxfiQHkz492cKetFU5tgjrNcF1VHqahE4XDj5aHDNEhkRjArFgFv4v3t3qk1CSLyxTuH2GZTc9eysr
2020-12-29 21:07:01.660 E Blocks start before blockchain offset: 0 2182500
2020-12-29 21:07:01.767 E reorg_depth > m_max_reorg_depth. THROW EXCEPTION: error::reorg_depth_error
2020-12-29 21:07:01.771 E Wallet initialization failed: reorg exceeds maximum allowed depth, use 'set max-reorg-depth N' to allow it, reorg depth: 2182500

```

## ghost | 2020-12-29T21:16:23+00:00
summary of the problem:
- Setting the `max-reorg-depth` isn't actionable, maybe it is in a REPL mode however this is a server based RPC instance that will not be providing REPL functionality
- The threshold is breached given a clean data-dir and a new wallet which means it is in breach by default for me, surely this isn't a problem that everybody has?

```
❯ docker run --rm --net host -e DAEMON_HOST=0.0.0.0 -e WALLET_PASSWD=password -v /home/toor/monero:/monero xmrto/monero monero-wallet-rpc --help 2>&1 | grep reorg
```


## ghost | 2020-12-29T21:42:52+00:00
And I also decide to heed the warning about lockable memory availability, and ensured that it would have an unlimited amount however it did not fix the problem, but the warning went away, so as near as I can tell it is actually unrelated:
```
❯ docker run --rm --net host --ulimit memlock=-1:-1 -e DAEMON_HOST=0.0.0.0 -e WALLET_PASSWD=password -v /home/toor/monero:/monero xmrto/monero monero-wallet-rpc --wallet-file wallet
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.0.0-e5decd0cd)
Logging to monero-wallet-rpc.log
2020-12-29 21:39:51.093 W Loading wallet...
2020-12-29 21:39:51.989 W Loaded wallet keys file, with public address: 47dKqri9EfCMdz88aYxfiQHkz492cKetFU5tgjrNcF1VHqahE4XDj5aHDNEhkRjArFgFv4v3t3qk1CSLyxTuH2GZTc9eysr
2020-12-29 21:39:52.195 E Blocks start before blockchain offset: 0 2182500
2020-12-29 21:39:52.270 E reorg_depth > m_max_reorg_depth. THROW EXCEPTION: error::reorg_depth_error
2020-12-29 21:39:52.274 E Wallet initialization failed: reorg exceeds maximum allowed depth, use 'set max-reorg-depth N' to allow it, reorg depth: 2182500

```

Also, I couldn't tell just from reading that log so I stopped the primary daemon and attempted to start the wallet rpc to see if it was even connecting to the daemon at all, and I confirmed that it is, because it's giving me a different connect error before it gives me the reorg depth error, but I couldn't tell from that log:

```
❯ docker run --rm --net host --ulimit memlock=-1:-1 -e DAEMON_HOST=0.0.0.0 -e WALLET_PASSWD=password -v /home/toor/monero:/monero xmrto/monero monero-wallet-rpc --wallet-file wallet
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.0.0-e5decd0cd)
Logging to monero-wallet-rpc.log
2020-12-29 21:44:26.174 W Loading wallet...
2020-12-29 21:44:26.613 W Loaded wallet keys file, with public address: 47dKqri9EfCMdz88aYxfiQHkz492cKetFU5tgjrNcF1VHqahE4XDj5aHDNEhkRjArFgFv4v3t3qk1CSLyxTuH2GZTc9eysr
2020-12-29 21:44:26.661 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2020-12-29 21:44:26.665 E Wallet initialization failed: no connection to daemon
```

## ghost | 2020-12-29T23:03:01+00:00
Just did a little verification, and I tried all of this using version 0.15 (the oldest available tag for the Docker hub container is `xmrto/monero:v0.15.0.1` and after starting with a fresh directory and repeating all of the steps I was able to get the wallet rpc daemon to start though it came with a different set of problems, but it does work, suffice to say this problem seems to be specific to `v0.17.0.0-e5decd0cd`

```
❯ docker run --rm --net host --ulimit memlock=-1:-1 -e WALLET_PASSWD=password -v /home/toor/monero:/monero --entrypoint="" xmrto/monero:v0.15.0.1 monero-wallet-rpc --wallet-file wallet --rpc-bind-ip 0.0.0.0 --rpc-bind-port 28083 --password password --daemon-address 127.0.0.1:28081 --confirm-external-bind --disable-rpc-login
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)
Logging to monero-wallet-rpc.log
2020-12-29 23:00:40.676 W Loading wallet...
2020-12-29 23:00:40.677 I Generating SSL certificate
2020-12-29 23:00:40.791 I Generating SSL certificate
2020-12-29 23:00:40.961 W Loaded wallet keys file, with public address: 474vSn4W6PP53Sj3cefi9iDeErDUFT7k3UJSJMcQsB7oAxDY6q3cU9pbQn1viCsTeRBBo1Lj4NY2BCHixtL42ZnS1PFd336
2020-12-29 23:00:41.006 E No message store file found: wallet.mms
2020-12-29 23:00:41.281 E Blocks start before blockchain offset: 0 1958000
2020-12-29 23:00:41.329 E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2020-12-29 23:00:41.405 E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2020-12-29 23:00:41.409 I Binding on 0.0.0.0 (IPv4):28083
2020-12-29 23:00:41.409 I Generating SSL certificate
2020-12-29 23:00:42.122 W Starting wallet RPC server
2020-12-29 23:00:43.194 E Blocks start before blockchain offset: 0 1958000
2020-12-29 23:00:43.215 E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2020-12-29 23:00:43.266 E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2020-12-29 23:01:03.321 E Blocks start before blockchain offset: 0 1958000
2020-12-29 23:01:03.342 E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2020-12-29 23:01:03.392 E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2020-12-29 23:01:23.453 E Blocks start before blockchain offset: 0 1958000
2020-12-29 23:01:23.477 E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2020-12-29 23:01:23.529 E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2020-12-29 23:01:43.591 E Blocks start before blockchain offset: 0 1958000
2020-12-29 23:01:43.615 E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2020-12-29 23:01:43.668 E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2020-12-29 23:02:03.705 E Blocks start before blockchain offset: 0 1958000
2020-12-29 23:02:03.729 E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2020-12-29 23:02:03.784 E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
```

I am actually able to make use of `v0.15` for my purposes so I think I will roll with this: 

```
In [1]: from monero.wallet import Wallet 
   ...: from monero.backends.jsonrpc import JSONRPCWallet                                                                           

In [2]: w = Wallet(JSONRPCWallet(port=28083))                                                                                       

In [3]:            
```



## froyobin | 2021-01-11T23:10:08+00:00
I have the same issue which I run the wallet and daemon directly with the compiled commands. here is the error log

 y@ys-MacBook-Pro  ~/Downloads/monero-x86_64-apple-darwin11-v0.17.1.8  monero-wallet-rpc  --wallet-file test2 --rpc-bind-port 18083 --disable-rpc-login --prompt-for-password
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.0.0-e144dd5b1)
Logging to monero-wallet-rpc.log
2021-01-11 23:08:40.974 W Loading wallet...
Wallet password: 
2021-01-11 23:08:46.002 W Loaded wallet keys file, with public address: 4AMYeVU8NHsBDVEzTMukh2W1nj7HbKGa9KE13y4Msku6aMJQ1QMufrJ9iLKnWqpUBdCtXeg9Hft2hakmDqVXABwTVgVRF9m
2021-01-11 23:08:46.469 E Blocks start before blockchain offset: 0 2182500
2021-01-11 23:08:46.632 E reorg_depth > m_max_reorg_depth. THROW EXCEPTION: error::reorg_depth_error
2021-01-11 23:08:46.634 E Wallet initialization failed: reorg exceeds maximum allowed depth, use 'set max-reorg-depth N' to allow it, reorg depth: 2182500

## xiphon | 2021-01-11T23:27:02+00:00
Apply https://github.com/monero-project/monero/pull/7288 patch, the wallet won't treat this as a critical initialization error on startup.

Is your daemon synced with the network?

## froyobin | 2021-01-11T23:29:44+00:00
Thanks for your reply. 

my daemon is not fully synced.  
because I am testing now, so I use monero public daemon with parameter  `--daemon-host` to work around this error.

# Action History
- Created by: ghost | 2020-12-29T20:50:00+00:00
- Closed at: 2021-02-16T02:50:47+00:00
