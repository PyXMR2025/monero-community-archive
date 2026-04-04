---
title: Deamon starts, network sync complete Wallet-CLI wont connect
source_url: https://github.com/monero-project/monero/issues/3101
author: digitalhuman
assignees: []
labels: []
created_at: '2018-01-11T11:42:32+00:00'
updated_at: '2024-02-27T18:08:40+00:00'
type: issue
status: closed
closed_at: '2018-01-11T17:20:34+00:00'
---

# Original Description
Hi there,

The monerod started fine. It synct perfectly and when I don't use --detach i can see the status etc. No problem. When use --detach I can not see anything but thats fine.

status
Height: 1484738/1484738 (100.0%) on mainnet, not mining, net hash 585.31 MH/s, v6, up to date, 9(out)+0(in) connections, uptime 0d 0h 6m 13s
sync_info
Height: 1484738, target: 1484738 (100%)


When I look at netstat -ln I see the RPC deamon is binded to 127 and port 18081. 

tcp        0      0 0.0.0.0:18080           0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:18081         0.0.0.0:*               LISTEN

You think, well, sounds good lets start the wallet-cli. Its starts, asks for the password etc. Then I get:

**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
Error: wallet failed to connect to daemon: 127.0.0.1:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or restart the wallet with the correct daemon address.
Error: wallet failed to connect to daemon: 127.0.0.1:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or restart the wallet with the correct daemon address.

Background refresh thread started

[wallet 494XKV (no daemon)]: help

Any idea what is going on? I can't seem to figure it out.



# Discussion History
## moneromooo-monero | 2018-01-11T12:24:01+00:00
I assume you're doing this on the same VM/machine.

Can you connect using telnet ?  telnet 127.0.0.1 18081


## digitalhuman | 2018-01-11T13:01:57+00:00
Yes same machine. Yeah I can connect with telnet. No problem.

monero]# telnet 127.0.0.1 18081
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
^C
Connection closed by foreign host.



## moneromooo-monero | 2018-01-11T14:09:55+00:00
Start both monerod and monero-wallet-cli with `--log-level 1,*rpc*:DEBUG,*wallet*:DEBUG` and see if you get any errors/warnings.

## digitalhuman | 2018-01-11T14:34:53+00:00
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
Error: wallet failed to connect to daemon: http://127.0.0.1:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or restart the wallet with the correct daemon address.
Error: wallet failed to connect to daemon: http://127.0.0.1:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or restart the wallet with the correct daemon address.
Background refresh thread started

[wallet 494XKV (no daemon)]:


## digitalhuman | 2018-01-11T14:35:11+00:00
No errors, debug messages, nothing

## moneromooo-monero | 2018-01-11T16:27:57+00:00
The prompt means you've got that from the console, not the log file, right ? The wallet doesn't print logs to the console.
About the daemon, since there are already logs with default log level, there's bound to be some unless there's a typo in the parameter.

## digitalhuman | 2018-01-11T16:33:23+00:00
Exactly, from the console. 
Started with: 
monerod --data-dir=/mnt/blockchain/monero --log-file /var/log/monero.log --log-level 1 --no-igd --rpc-bind-ip 127.0.0.1 --rpc-login ****


2018-01-11 16:34:02.606     7fbe6c6a4780        INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.1.0-release)
2018-01-11 16:34:02.607     7fbe6c6a4780        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2018-01-11 16:34:02.607     7fbe6c6a4780        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2018-01-11 16:34:02.607     7fbe6c6a4780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-01-11 16:34:02.764     7fbe6c6a4780        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2018-01-11 16:34:02.765     7fbe6c6a4780        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2018-01-11 16:34:02.765     7fbe6c6a4780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2018-01-11 16:34:02.765     7fbe6c6a4780        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2018-01-11 16:34:02.765     7fbe6c6a4780        INFO    global  src/daemon/core.h:73    Initializing core...
2018-01-11 16:34:02.765     7fbe6c6a4780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /mnt/blockchain/monero/lmdb ...
2018-01-11 16:34:02.987     7fbe6c6a4780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:421     Loading checkpoints
2018-01-11 16:34:03.027     7fbe6c6a4780        INFO    global  src/daemon/core.h:78    Core initialized OK
2018-01-11 16:34:03.027     7fbe6c6a4780        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
2018-01-11 16:34:03.027 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok
2018-01-11 16:34:03.027 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2018-01-11 16:34:04.028 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1258
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2018-01-11 16:34:04.275 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [94.23.41.130:18080 OUT] Sync data returned a new top block candidate: 1484903 -> 1484904 [Your node is 1 blocks (0 days) behind]
SYNCHRONIZATION started
2018-01-11 16:34:06.231 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    [94.23.41.130:18080 OUT]  Synced 1484904/1484904
2018-01-11 16:34:06.231 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    SYNCHRONIZED OK
2018-01-11 16:34:06.231 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1543
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-01-11 16:34:06.542 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    SYNCHRONIZED OK


## digitalhuman | 2018-01-11T16:36:20+00:00
Again tried with: monero-wallet-cli --log-level 1,*rpc*:DEBUG,*wallet*:DEBUG --daemon-host 127.0.0.1

No error, no entry in the logfile, nothing on screen

Error: wallet failed to connect to daemon: http://127.0.0.1:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or restart the wallet with the correct daemon address.
Error: wallet failed to connect to daemon: http://127.0.0.1:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or restart the wallet with the correct daemon address.
Background refresh thread started

#News

When I tunnel port 18081 with: 18081:127.0.0.1:18081 en visit the site it works. It asks for a username and password.
When logging in I get:

This 127.0.0.1 page can’t be found
No webpage was found for the web address: http://127.0.0.1:18081/
HTTP ERROR 404

## moneromooo-monero | 2018-01-11T16:57:54+00:00
That last message doesn't look like a monero error message. Do you have some MITM software that's maybe intercepting data ?

## digitalhuman | 2018-01-11T16:59:23+00:00
@moneromooo-monero No thats just the HTML browser output. Nothing special. With postman I get:

<html><head><title>Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html>

I used this https://github.com/digibyte/digibyte/tree/master/share/rpcuser to create a RPC auth string that I use for --rpc-login parameter.

## moneromooo-monero | 2018-01-11T17:10:31+00:00
OK, so a HTML browser will not speak JSON RPC. The RPC end point is at json_rpc anyway.
You didn't run monerod with the full log command btw.

## digitalhuman | 2018-01-11T17:14:41+00:00
Hoever I do see my attempts. Is the RPC auth string for --rpc-login correct? What did I miss for 'full log' then?

018-01-11 16:37:02.190     7fe637121740        INFO    msgwriter       src/common/scoped_message_writer.h:102  Background refresh thread started
2018-01-11 16:37:02.270     7fe637121740        ERROR   net.http        contrib/epee/include/net/http_client.h:421      Client has incorrect username/password for server requiring authentication


## digitalhuman | 2018-01-11T17:20:34+00:00
Apperently I had --daemon-login not identical to the --rpc-login value when starting monerod.

## ff0255 | 2024-02-11T01:00:12+00:00
JM2C
This error messages of monero-wallet-cli could be more informative and less misleading... I spent several hours trying to figure out what's wrong with daemon until found this issue...

## blackout314 | 2024-02-27T18:08:39+00:00
> JM2C This error messages of monero-wallet-cli could be more informative and less misleading... I spent several hours trying to figure out what's wrong with daemon until found this issue...

and error is?


# Action History
- Created by: digitalhuman | 2018-01-11T11:42:32+00:00
- Closed at: 2018-01-11T17:20:34+00:00
