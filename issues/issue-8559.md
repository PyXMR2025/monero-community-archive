---
title: Daemon failing to start
source_url: https://github.com/monero-project/monero/issues/8559
author: EmbeddedAndroid
assignees: []
labels: []
created_at: '2022-09-09T01:27:35+00:00'
updated_at: '2022-09-09T17:45:27+00:00'
type: issue
status: closed
closed_at: '2022-09-09T17:45:27+00:00'
---

# Original Description
A few hours ago my daemon crashed, and wont start now.

`2022-09-09 01:21:34.764 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-09-09 01:21:34.764 I Initializing cryptonote protocol...
2022-09-09 01:21:34.765 I Cryptonote protocol initialized OK
2022-09-09 01:21:34.765 I Initializing core...
2022-09-09 01:21:34.765 I Loading blockchain from folder /var/monero/lmdb ...
2022-09-09 01:21:34.847 I Loading checkpoints
2022-09-09 01:21:34.849 I Core initialized OK
2022-09-09 01:21:34.849 I Initializing p2p server...
2022-09-09 01:21:35.204 I Deinitializing core...
2022-09-09 01:21:35.212 I Stopping cryptonote protocol...
2022-09-09 01:21:35.212 I Cryptonote protocol stopped successfully
2022-09-09 01:21:35.212 E Exception in main! Failed to initialize p2p server.
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 172.105.70.100:443...
* Connected to gui.xmr.pm (172.105.70.100) port 443 (#0)
* ALPN: offers h2
* ALPN: offers http/1.1
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: none
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [122 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [25 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [4018 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [264 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [52 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN: server accepted http/1.1
* Server certificate:
*  subject: CN=gui.xmr.pm
*  start date: Aug 17 08:08:07 2022 GMT
*  expire date: Nov 15 08:08:06 2022 GMT
*  subjectAltName: host "gui.xmr.pm" matched cert's "gui.xmr.pm"
*  issuer: C=US; O=Let's Encrypt; CN=R3
*  SSL certificate verify ok.
} [5 bytes data]
> GET /files/block.txt HTTP/1.1
> Host: gui.xmr.pm
> User-Agent: curl/7.83.1
> Accept: */*
>
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [57 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [57 bytes data]
* old SSL session ID is stale, removing
{ [5 bytes data]
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx
< Date: Fri, 09 Sep 2022 01:21:35 GMT
< Content-Type: text/plain
< Content-Length: 10066
< Last-Modified: Sun, 21 Aug 2022 21:26:49 GMT
< Connection: keep-alive
< ETag: "6302a319-2752"
< Accept-Ranges: bytes
<
{ [10066 bytes data]
100 10066  100 10066    0     0  26208      0 --:--:-- --:--:-- --:--:-- 26213
* Connection #0 to host gui.xmr.pm left intact`

At this point monerod exits non-zero. 

Edit: Set debug to level 3

```monero-p2p-monero-1  | 2022-09-09 01:41:07.225  T mdb_txn_safe: destructor
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  I Pruned blockchain in 2 ms: 0 MB (0 MB) pruned in 0 records (0/4063621 4096 byte pages), 0/0 pruned records
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  T mdb_txn_safe: destructor
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  I Core initialized OK
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  I Initializing p2p server...
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  T Blockchain::get_current_blockchain_height
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  T BlockchainLMDB::height
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  T BlockchainLMDB::block_rtxn_start
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  T mdb_txn_safe: destructor
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  D Found 0 out connections having height >= 2706019
monero-p2p-monero-1  | 2022-09-09 01:41:07.228  I Resolving node address: host=node.supportxmr.com, port=18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.270  I Added node: 46.4.52.92:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.270  I Added node: [2a01:4f8:140:11fe::2]:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.270  I Resolving node address: host=opennode.xmr-tw.org, port=18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.297  I Added node: 85.245.24.44:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.297  I Added node: 95.17.121.35:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.297  I Added node: 68.6.155.23:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.297  I Added node: 85.214.173.243:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.297  I Added node: 107.141.227.162:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.297  I Resolving node address: host=node.moneroworld.com, port=18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.320  I Added node: 104.238.221.81:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.320  I Added node: 204.27.62.98:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.320  I Added node: 51.79.173.165:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.320  I Added node: 100.14.73.50:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.320  I Added node: 96.43.139.226:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.320  I Resolving node address: host=uwillrunanodesoon.moneroworld.com, port=18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.346  I Added node: 100.14.73.50:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.346  I Added node: 96.43.139.226:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.346  I Added node: 104.238.221.81:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.346  I Added node: 204.27.62.98:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.346  I Added node: 51.79.173.165:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.346  I Resolving node address: host=nodes.hashvault.pro, port=18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.425  E Failed to resolve host name 'nodes.hashvault.pro': Host not found (authoritative):1
monero-p2p-monero-1  | 2022-09-09 01:41:07.425  E Failed to parse or resolve address from string: nodes.hashvault.pro:18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.425  E Failed to handle command line
monero-p2p-monero-1  | 2022-09-09 01:41:07.433  I Deinitializing core...
monero-p2p-monero-1  | 2022-09-09 01:41:07.433  T Miner has received stop signal
monero-p2p-monero-1  | 2022-09-09 01:41:07.433  T Not mining - nothing to stop
monero-p2p-monero-1  | 2022-09-09 01:41:07.433  T Blockchain::deinit
monero-p2p-monero-1  | 2022-09-09 01:41:07.433  T Stopping blockchain read/write activity
monero-p2p-monero-1  | 2022-09-09 01:41:07.433  T BlockchainLMDB::close
monero-p2p-monero-1  | 2022-09-09 01:41:07.433  T BlockchainLMDB::sync
monero-p2p-monero-1  | 2022-09-09 01:41:07.441  T Local blockchain read/write activity stopped successfully
monero-p2p-monero-1  | 2022-09-09 01:41:07.441  T BlockchainLMDB::~BlockchainLMDB
monero-p2p-monero-1  | 2022-09-09 01:41:07.441  T Miner has received stop signal
monero-p2p-monero-1  | 2022-09-09 01:41:07.441  T Not mining - nothing to stop
monero-p2p-monero-1  | 2022-09-09 01:41:07.441  T Blockchain::deinit
monero-p2p-monero-1  | 2022-09-09 01:41:07.441  T Stopping blockchain read/write activity
monero-p2p-monero-1  | 2022-09-09 01:41:07.441  I Stopping cryptonote protocol...
monero-p2p-monero-1  | 2022-09-09 01:41:07.441  I Cryptonote protocol stopped successfully
monero-p2p-monero-1  | 2022-09-09 01:41:07.441  E Exception in main! Failed to initialize p2p server.```

Is this a transient network failure? TIA

# Discussion History
## selsta | 2022-09-09T17:22:44+00:00
```
monero-p2p-monero-1  | 2022-09-09 01:41:07.346  I Resolving node address: host=nodes.hashvault.pro, port=18080
monero-p2p-monero-1  | 2022-09-09 01:41:07.425  E Failed to resolve host name 'nodes.hashvault.pro': Host not found (authoritative):1
monero-p2p-monero-1  | 2022-09-09 01:41:07.425  E Failed to parse or resolve address from string: nodes.hashvault.pro:18080
```

Config issue?

## EmbeddedAndroid | 2022-09-09T17:38:42+00:00
> ```
> monero-p2p-monero-1  | 2022-09-09 01:41:07.346  I Resolving node address: host=nodes.hashvault.pro, port=18080
> monero-p2p-monero-1  | 2022-09-09 01:41:07.425  E Failed to resolve host name 'nodes.hashvault.pro': Host not found (authoritative):1
> monero-p2p-monero-1  | 2022-09-09 01:41:07.425  E Failed to parse or resolve address from string: nodes.hashvault.pro:18080
> ```
> 
> Config issue?

This daemon had been running before the hard fork without issue or change to config. It continued to crash throughout yesterday with the errors above. I checked this morning and it was able to recover, and has since been running without issue. I have not updated the configuration or code since a few days before the HF.

Lets say it is a config issue, or a network issue. If a single node's hostname cannot be resolved, shouldn't that throw a warning rather than an error which halts the daemon? 

Basically, I trying to understand what I can do in the future to avoid this from happening again. The answer might simply be prune that node from the config, but I want to double check this isn't a scenario where we could handle the error better.

## selsta | 2022-09-09T17:39:52+00:00
Can you post your config? Also I don't see any crash in the logs you posted, it simply doesn't start due to your config.

## EmbeddedAndroid | 2022-09-09T17:45:18+00:00
> Can you post your config? Also I don't see any crash in the logs you posted, it simply doesn't start due to your config.

Ugh, my fault. I found where i'm setting these nodes up as priority nodes. This was self inflicted as you were indicating.

Sorry for the noise!

# Action History
- Created by: EmbeddedAndroid | 2022-09-09T01:27:35+00:00
- Closed at: 2022-09-09T17:45:27+00:00
