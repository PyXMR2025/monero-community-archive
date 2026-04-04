---
title: monerod crashes after failing to store HTTP SSL cert/key for RPC server
source_url: https://github.com/monero-project/monero/issues/8487
author: bloatmode
assignees: []
labels: []
created_at: '2022-08-07T03:43:23+00:00'
updated_at: '2022-08-16T18:19:59+00:00'
type: issue
status: closed
closed_at: '2022-08-10T17:35:49+00:00'
---

# Original Description
I set up monerod to start on login on my Arch Linux installation but lately it has been crashing every time due to the error named in the title.  
Here are my [systemd unit file](https://gist.github.com/bloatmode/8d06f012fb86c4579ca59f4bdd50867e#file-monerod-service), my [config file](https://gist.github.com/bloatmode/8d06f012fb86c4579ca59f4bdd50867e#file-monerod-conf), the [log file portion from the last time it was started](https://gist.github.com/bloatmode/8d06f012fb86c4579ca59f4bdd50867e#file-log-txt).

# Discussion History
## selsta | 2022-08-07T12:59:47+00:00
Are you sure this isn't some permission issue?

## bloatmode | 2022-08-07T14:24:20+00:00
It could be. Right now the only directories owned by user (or group) `monero` on my system are `/var/log/monero` and `/var/lib/monero`.  
[The latter should be the home directory of user `monero`](https://wiki.archlinux.org/title/Web_application_package_guidelines) and it has `rwx` permissions for both user and group `monero`, but it contains no files.  
`/var/log/monero` has `rw` permissions for user `monero` and `r` for group `monero`.

## boldsuck | 2022-08-07T18:22:02+00:00
You forgot permission for confdir ;-)
```
# /etc/monero
ConfigurationDirectory=monero
ConfigurationDirectoryMode=0710
```
[My complete systemd](https://gist.github.com/boldsuck/468036b5123320608c4f4f5fc70e90f5)


## selsta | 2022-08-07T18:24:19+00:00
Closing this as it seems like a permission issue. If the suggestion above doesn't work comment and I can reopen.

## bloatmode | 2022-08-08T03:08:21+00:00
@boldsuck My config file is `/etc/monerod.conf`, as can be seen from my unit file. That file has read permission for everybody, so that's not it. While I think it's possible that mine is a permission issue I don't think that's the case as monerod was running fine as of July 13, the first time I can find the error is in the log from July 22.  
I upgraded monero from version 0.17.3.2 to 0.18.0.0 on July 22 at 23:47:31 CEST, started monerod at 23:49:50 CEST and the first time the error was logged was at 23:54:07 CEST.

EDIT: I downgraded to version 0.17.3.2 and synchronization started without any issues. Here's the log from today:

```
2022-08-08 03:14:47.780     7f047efbca00        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-08-08 03:14:47.780     7f047efbca00        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-08-08 03:14:47.815     7f047efbca00        INFO    global  src/daemon/main.cpp:296 Monero 'Oxygen Orion' (v0.17.3.2-release)
2022-08-08 03:14:47.816     7f047efbca00        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2022-08-08 03:14:47.816     7f047efbca00        WARNING daemon  src/daemon/executor.cpp:61      Monero 'Oxygen Orion' (v0.17.3.2-release) Daemonised
2022-08-08 03:14:47.816     7f047efbca00        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2022-08-08 03:14:47.816     7f047efbca00        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2022-08-08 03:14:47.817     7f047efbca00        INFO    global  src/daemon/core.h:64    Initializing core...
2022-08-08 03:14:47.817     7f047efbca00        INFO    global  src/cryptonote_core/cryptonote_core.cpp:517     Loading blockchain from folder /home/media.homedir/Pubblici/monerod/lmdb ...
2022-08-08 03:17:46.253     7f047efbca00        INFO    global  src/cryptonote_core/cryptonote_core.cpp:692     Loading checkpoints
2022-08-08 03:17:46.290     7f047efbca00        INFO    global  src/daemon/core.h:81    Core initialized OK
2022-08-08 03:17:46.290     7f047efbca00        INFO    global  src/daemon/p2p.h:64     Initializing p2p server...
2022-08-08 03:17:46.357     7f047efbca00        INFO    global  src/daemon/p2p.h:69     p2p server initialized OK
2022-08-08 03:17:46.357     7f047efbca00        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2022-08-08 03:17:46.357     7f047efbca00        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 192.168.1.110 (IPv4):18081
2022-08-08 03:17:48.471     7f047efbca00        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2022-08-08 03:17:48.471     7f047efbca00        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2022-08-08 03:17:48.471 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2022-08-08 03:17:48.471 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:79     Starting p2p net loop...
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    **********************************************************************
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    The daemon will start synchronizing with the network. This may take a long time to complete.
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    You can set the level of process detailization through "set_log <level|categories>" command,
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    Use the "help" command to see the list of available commands.
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    Use "help <command>" to see a command's documentation.
2022-08-08 03:17:49.472 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    **********************************************************************
2022-08-08 03:17:49.739 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:411     [185.141.253.68:18080 OUT] Sync data returned a new top block candidate: 2665382 -> 2684811 [Your node is 19429 blocks (27.0 days) behind] 
2022-08-08 03:17:49.739 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:411     SYNCHRONIZATION started
```

@selsta could you please reopen the issue?

## selsta | 2022-08-08T17:29:09+00:00
As a first step can you try starting monerod manually without any systemd?

## bloatmode | 2022-08-09T19:12:00+00:00
I tried `sudo -u monero /usr/bin/monerod --config-file /etc/monerod.conf` and the output I get is
```
2022-08-09 19:07:45.550	I Monero 'Fluorine Fermi' (v0.18.0.0-release)
2022-08-09 19:07:45.550	I Initializing cryptonote protocol...
2022-08-09 19:07:45.550	I Cryptonote protocol initialized OK
2022-08-09 19:07:45.551	I Initializing core...
2022-08-09 19:07:45.551	I Loading blockchain from folder /home/media.homedir/Pubblici/monerod/lmdb ...
2022-08-09 19:07:45.639	I Loading checkpoints
2022-08-09 19:07:45.667	I Core initialized OK
2022-08-09 19:07:45.667	I Initializing p2p server...
2022-08-09 19:07:45.675	I p2p server initialized OK
2022-08-09 19:07:45.675	I Initializing core RPC server...
2022-08-09 19:07:45.675	I Binding on 192.168.1.110 (IPv4):18081
2022-08-09 19:07:45.684	F Error starting server: use_private_key_file: Permission denied (system library, fopen) [asio.ssl:33558541]
2022-08-09 19:07:45.685	I Deinitializing p2p...
2022-08-09 19:07:45.689	I Deinitializing core...
2022-08-09 19:07:45.717	I Stopping cryptonote protocol...
2022-08-09 19:07:45.718	I Cryptonote protocol stopped successfully
2022-08-09 19:07:45.718	E Exception in main! Failed to initialize core RPC server.
```

After trying `sudo /usr/bin/monerod --config-file /etc/monerod.conf` everything works and it starts synchronizing. It seems like a permission issue but everything worked fine in the previous version so I have no idea why the private key file cannot be accessed.

## selsta | 2022-08-09T23:02:32+00:00
ping @jeffro256 any idea?

## bloatmode | 2022-08-10T03:31:41+00:00
It would help to know in which file this private key is stored so that I could check what its permissions are

## jeffro256 | 2022-08-10T05:56:08+00:00
@bloatmode It is `rpc_ssl.key` and `rpc_ssl.crt` in the data directory. They both need to be able to be readable by the `monero` user if that's what you're running the command as.

If they don't exist, make sure that the `monero` user has permission to add files to the data directory.

Could you please run `ls -alF <YOUR DATA DIRECTORY>` and post the results? Also let us know if/what fixes your issue, since some code which touches those files was modified (by yours truly) and could have caused some backwards-incompatible behavior. I would like to make those errors more user-friendly if possible.

## boldsuck | 2022-08-10T11:54:32+00:00
Monero system-wide install Data directory is default:
data-dir=/var/lib/monero/.bitmonero
```
root@crypto-01:/var/lib/monero/.bitmonero# lr
drwxr-xr-x 3 monero monero   4096 Jul 23 12:22 .
drwx--x--- 3 monero monero   4096 Mar 26 18:30 ..
drwxr-xr-x 2 monero monero   4096 Jul 21 17:57 lmdb
-rw-r--r-- 1 monero monero 250325 Aug 10 13:38 p2pstate.bin
-r--r--r-- 1 monero monero   1606 Jul 23 12:22 rpc_ssl.crt
-r-------- 1 monero monero   3268 Jul 23 12:22 rpc_ssl.key
```
@bloatmode Your keys should be here:
data-dir=/home/media.homedir/Pubblici/monerod

Maybe Seth's guide is helpful:
[run-a-monero-node-advanced/](https://sethforprivacy.com/guides/run-a-monero-node-advanced/)

If they aren't there, you can create them yourself. I just tested on my Stagenet node with unusual datadir:
`data-dir=/data/monero`
monero-gen-ssl-cert --certificate-filename monerod.crt --private-key-filename monerod.key
I copied the keys to '/etc/monero/ssl/' and specified them in monerod.conf:
```
rpc-ssl-private-key=/etc/monero/ssl/monerod.key
rpc-ssl-certificate=/etc/monero/ssl/monerod.crt

```



## bloatmode | 2022-08-10T17:35:49+00:00
@jeffro256 This is the result of `ls -alF ./` in the data directory:
```
total 163
drwxr-xr-x 3 user     user          6 Aug  9 21:01 ./
drwxrwxrwx 4 media    media         5 Jun 23 19:45 ../
drwxrwxrwx 2 media    media         4 Aug  8 05:14 lmdb/
-rw-rw-rw- 1 media    media    162230 Aug  9 21:07 p2pstate.bin
-r--r--r-- 1 root     root       1606 Aug  9 21:01 rpc_ssl.crt
-r-------- 1 root     root       3272 Aug  9 21:01 rpc_ssl.key
```

Setting permissions this way fixed my issues and now monerod runs without issues:

+ Data directory
```
total 163K
drwxrwxr-x 3 monero monero    6 Aug  9 21:01 ./
drwxrwxrwx 4 media  media     5 Jun 23 19:45 ../
drwxrwxr-x 2 monero monero    4 Aug  8 05:14 lmdb/
-rw-rw-r-- 1 monero monero 159K Aug  9 21:07 p2pstate.bin
-rw-rw-r-- 1 monero monero 1.6K Aug  9 21:01 rpc_ssl.crt
-rw-rw---- 1 monero monero 3.2K Aug  9 21:01 rpc_ssl.key
```

+ lmdb

```
total 129G
drwxrwxr-x 2 monero monero    4 Aug  8 05:14 ./
drwxrwxr-x 3 monero monero    6 Aug  9 21:01 ../
-rw-rw-r-- 1 monero monero 138G Aug  9 21:07 data.mdb
-rw-rw-r-- 1 monero monero 8.0K Aug  9 21:07 lock.mdb
```

## sethforprivacy | 2022-08-16T18:16:38+00:00
If anyone running BTCPay Server with Monero support enabled, you can follow this to correct it: https://gist.github.com/sethforprivacy/ce9e81a896c423e318821ed69dfae4d0

Those steps can be adapted for "normal" daemon usage as well, FWIW.

## sethforprivacy | 2022-08-16T18:19:59+00:00
This PR was the change that is causing some issues for people with SSL if their data directory permissions are improperly set:

https://github.com/monero-project/monero/commit/602926fe9d2dabb099a32313175a4acb84846cd9

# Action History
- Created by: bloatmode | 2022-08-07T03:43:23+00:00
- Closed at: 2022-08-10T17:35:49+00:00
