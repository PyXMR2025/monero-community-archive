---
title: I am mining monero but nothing monero coins on my wallet
source_url: https://github.com/monero-project/monero/issues/3853
author: wmoreno3
assignees: []
labels: []
created_at: '2018-05-24T12:10:52+00:00'
updated_at: '2018-05-24T16:22:24+00:00'
type: issue
status: closed
closed_at: '2018-05-24T14:54:59+00:00'
---

# Original Description
`uname -a
FreeBSD mydomain 11.1-RELEASE-p6 FreeBSD 11.1-RELEASE-p6 #3: Wed Feb 14 05:28:12 -05 2018     root@mydomain:/usr/obj/usr/src/sys/TCPOPEN  amd64`
`root@server:~ # pkg info | grep monero
monero-cli-0.12.0.0_2`
`root@server:~ # monerod status
Height: 1579753/1579753 (100.0%) on mainnet, mining at 66 H/s, net hash 450.52 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 1d 17h 33m 10s`
`Monero 'Lithium Luna' (v0.12.0.0-master-release)
Logging to monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): my wallet name
Wallet and key files found, loading...
Wallet password:
Opened wallet: my monero wallet
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 232
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 425vFt        0.000000000000        0.000000000000       Primary account
----------------------------------------------------------------------------------
          Total        0.000000000000        0.000000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000
Background refresh thread started`

As I can see, monerod is mining but nothing of monero coins are in my wallet.
What happen ?

# Discussion History
## el00ruobuob | 2018-05-24T12:23:25+00:00
You did not found any block. That's all.
Please see [monerominig subredit](https://www.reddit.com/r/MoneroMining/) if you have questions about mining. 

This is a bugtracker.

## wmoreno3 | 2018-05-24T12:55:42+00:00
Thanks you for answer me and inform me.

Please tell me: Do you mean "any block" this:
`root@server:~ # tail -80 /var/log/monerod.log | grep block
2018-05-24 10:31:19.823 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] 0x142b446 <_ZN10cryptonote10Blockchain16store_blockchainEv+0x133a6> at /usr/local/bin/monerod
2018-05-24 10:31:19.824 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] 0x142b446 <_ZN10cryptonote10Blockchain16store_blockchainEv+0x133a6> at /usr/local/bin/monerod
2018-05-24 10:31:19.825 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] 0x142b446 <_ZN10cryptonote10Blockchain16store_blockchainEv+0x133a6> at /usr/local/bin/monerod`

## el00ruobuob | 2018-05-24T13:41:31+00:00
I don't see anything like "found block" here. Again, please go to Reddit for asking questions. Issues on GitHub are for bugs.

## el00ruobuob | 2018-05-24T13:43:45+00:00
Btw. According to your hashpower you should found blocks every 26 years in average.

## wmoreno3 | 2018-05-24T13:46:31+00:00
Thanks

## wmoreno3 | 2018-05-24T13:51:15+00:00
The information that you share with me is very important, Thanks again.

## wmoreno3 | 2018-05-24T13:59:49+00:00
You helped me a lot. I was thinking that maybe this is a bug, but now I only stopped mining and `monerod` seems to be ready on my system FreeBSD. I am exiting on `monero-wallet-cli` 
`root@server:~ # monerod status
Height: 1579807/1579807 (100.0%) on mainnet, not mining, net hash 456.06 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 1d 19h 22m 51s`

## wmoreno3 | 2018-05-24T16:22:24+00:00
I started `monero-wallet-cli`, but without mining.
`ps -auxww
USER       PID  %CPU %MEM      VSZ     RSS TT  STAT STARTED       TIME COMMAND
xmrig    30956 798.5  0.2    95620   28432  -  Ss   06:18   1846:33.51 /usr/local/bin/xmrig --config=/usr/local/etc/xmrig/config.json
monero    2284   2.1 29.5 89497032 4920828  -  I    Tue13   9358:24.30 /usr/local/bin/monerod --data-dir=/var/db/monero --detach --log-file=/var/log/monerod.log --non-interactive --p2p-bind-ip=0.0.0.0 --p2p-bind-port=18080 --pidfile=/var/run/monerod.pid`

# Action History
- Created by: wmoreno3 | 2018-05-24T12:10:52+00:00
- Closed at: 2018-05-24T14:54:59+00:00
