---
title: Monero daemon stop syncing
source_url: https://github.com/monero-project/monero/issues/5625
author: trasherdk
assignees: []
labels: []
created_at: '2019-06-11T10:02:05+00:00'
updated_at: '2019-06-27T05:57:39+00:00'
type: issue
status: closed
closed_at: '2019-06-27T05:57:39+00:00'
---

# Original Description
I'm running `Monero 'Boron Butterfly' (v0.14.0.2-release)`
on a `Linux compaq-laptop 4.4.172 #2 SMP Wed Jan 30 17:11:07 CST 2019 x86_64 Intel(R) Core(TM)2 Duo CPU     T8100  @ 2.10GHz GenuineIntel GNU/Linux`

The host is behind a firewall, but that should not matter, right?

Looking at the logfile, I noticed the deamon had stopped syncing with the network.

```
2019-06-11 07:22:24.156 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310 [73.184.42.223:18080 OUT] Sync data returned a new top block candidate: 1853420 -> 1854404 [Your node is 984 blocks (1 days) behind] 
SYNCHRONIZATION started
2019-06-11 07:22:59.286 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310 [197.232.65.203:18080 OUT] Sync data returned a new top block candidate: 1853420 -> 1854404 [Your node is 984 blocks (1 days) behind] 
SYNCHRONIZATION started
2019-06-11 07:23:41.559 [P2P3]  WARN    cn      src/cryptonote_core/cryptonote_core.cpp:1767    There were 0 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack. Or it could be just sheer bad luck.
2019-06-11 07:24:17.347 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310 [173.255.205.142:18080 OUT] Sync data returned a new top block candidate: 1853420 -> 1854405 [Your node is 985 blocks (1 days) behind] 
SYNCHRONIZATION started
2019-06-11 07:24:46.873 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310 [149.202.94.125:18080 OUT] Sync data returned a new top block candidate: 1853420 -> 1854405 [Your node is 985 blocks (1 days) behind] 
SYNCHRONIZATION started
2019-06-11 07:25:12.708 [P2P1]  WARN    cn      src/cryptonote_core/cryptonote_core.cpp:1767    There were 0 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack. Or it could be just sheer bad luck.
```
Issuing an `status` command:
```
2019-06-11 09:18:57.934 [P2P2]  WARN    cn      src/cryptonote_core/cryptonote_core.cpp:1767    There were 0 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack. Or it could be just sheer bad luck.
status
Height: 1853420/1853420 (100.0%) on mainnet, not mining, net hash 279.46 MH/s, v11, up to date, 8(out)+0(in) connections, uptime 2d 5h 39m 48s
```
I'm told that I'm 100% in sync, but the blockheight is wrong.

After restarting the daemon, normal sync is resumed.
```
2019-06-11 09:23:27.579 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1598
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2019-06-11 09:23:29.052 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310 [13.231.81.228:18080 OUT] Sync data returned a new top block candidate: 1853420 -> 1854469 [Your node is 1049 blocks (1 days) behind] 
SYNCHRONIZATION started
```
And a little later:
```
2019-06-11 09:45:46.807 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310 [95.216.159.70:18080 OUT] Sync data returned a new top block candidate: 1853880 -> 1854483 [Your node is 603 blocks (0 days) behind] 
SYNCHRONIZATION started
2019-06-11 09:46:21.479 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182        [13.231.81.228:18080 OUT]  Synced 1853900/1854483
2019-06-11 09:47:44.852 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182        [13.231.81.228:18080 OUT]  Synced 1853920/1854484
2019-06-11 09:48:39.150 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182        [13.231.81.228:18080 OUT]  Synced 1853940/1854483
2019-06-11 09:49:36.577 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310 [107.191.99.95:18080 OUT] Sync data returned a new top block candidate: 1853940 -> 1854484 [Your node is 544 blocks (0 days) behind] 
SYNCHRONIZATION started
```


# Discussion History
## dEBRUYNE-1 | 2019-06-11T10:17:55+00:00
Would you mind compiling master to see whether that fixes the issue? 

https://github.com/monero-project/monero#compiling-monero-from-source

>The host is behind a firewall, but that should not matter, right?

Whilst it results in you not being able to serve the blockchain to others, it does not inhibit the daemon (monerod) from syncing properly. 

## moneromooo-monero | 2019-06-11T10:20:29+00:00
This is a known bug which is fixed in master.

## BKdilse | 2019-06-11T10:38:48+00:00
Hey guys, I've been getting a similar issue, over the last few days.  I am actually running from master:
`v0.14.1.0-5fbfa8a`.  Do you have fixes in after this release?

Sometimes, the `status` command takes over 1 minute to respond.

This morning, my Daemon fell behind by 4 hours.

## trasherdk | 2019-06-11T10:43:42+00:00
Okay compiled, downloaded and started `Monero 'Boron Butterfly' (v0.14.1.0-51766d02)`.

And now I'm getting
```
Migrating blockchain from DB version 4 to 5 - this may take a while:
358000 / 1854502 
```
Let's see what happens over the next few days.


## moneromooo-monero | 2019-06-11T11:05:37+00:00
set_log 1
See if you get any errors.

## trasherdk | 2019-06-11T13:58:11+00:00
Looks like it's running normal. It's stuff like:
`2019-06-11 13:43:55.160 W [71.237.4.241:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)`
```
Failed to connect to any, trying seeds
Connect failed to 195.154.123.123:18080
Failed to connect to any of seed peers, continuing without seeds
```
But it's syncing.

Then there's these that just started after 3 hour uptime.
```
2019-06-11 13:50:19.312 E [85.93.7.12:18080 OUT] [levin_protocol] -->> start_outer_call failed
2019-06-11 13:50:19.313 E [149.202.216.125:18080 OUT] [levin_protocol] -->> start_outer_call failed
2019-06-11 13:50:19.313 E [78.46.106.176:18080 OUT] [levin_protocol] -->> start_outer_call failed

2019-06-11 13:51:32.671 W [153.92.132.84:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)

2019-06-11 13:52:22.107 E [176.58.114.43:18080 OUT] [levin_protocol] -->> start_outer_call failed
2019-06-11 13:52:22.107 E [147.175.187.111:18080 OUT] [levin_protocol] -->> start_outer_call failed
2019-06-11 13:52:22.108 E [95.216.96.167:18080 OUT] [levin_protocol] -->> start_outer_call failed
2019-06-11 13:52:22.108 I [153.92.132.84:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)

```


## BKdilse | 2019-06-11T21:26:08+00:00
Just updated mine to the latest Master.  Will report back findings.

## BKdilse | 2019-06-11T21:33:50+00:00
@moneromooo-monero Just check with logs set to 1, and I'm getting similar logs to @trasherdk 

My pool is failing to connect to Daemon:
`{"code":"ETIMEDOUT","errno":"ETIMEDOUT","syscall":"connect","address":"127.0.0.1","port":18081}
`
We've discussed similar issues in the past, and I've stated that I am running this on HDD, not SSD.  Could this be an issue?

## moneromooo-monero | 2019-06-11T22:43:01+00:00
A timeout can be caused by a large number of things. There's no a priori reason to think that your timeouts are caused by the same reason as the other person's timeouts.

## trasherdk | 2019-06-12T03:43:58+00:00
I had to restart daemon today, because I lost connection to the host.  
No problems between daemon host and internet.  
After restart I noticed this: **monerod is now disconnected from the network**
```
2019-06-12 02:54:11.234 I [122.116.59.198:18080 OUT] Sync data returned a new top block candidate: 1855002 -> 1855003 [Your node is 1 blocks (0 days) behind] 
SYNCHRONIZATION started
2019-06-12 02:54:15.573 I Synced 1855003/1855003
2019-06-12 02:54:15.573 I SYNCHRONIZED OK
2019-06-12 03:03:26.625 W monerod is now disconnected from the network
2019-06-12 03:06:03.538 I [82.128.227.182:18080 OUT] Sync data returned a new top block candidate: 1855008 -> 1855011 [Your node is 3 blocks (0 days) behind] 
SYNCHRONIZATION started
2019-06-12 03:06:17.559 I Synced 1855011/1855011
2019-06-12 03:06:17.560 I SYNCHRONIZED OK
```
Seems that the GUI wallet have some problems syncing.
```
2019-06-12 03:16:22.864 I Synced 1855016/1855016
2019-06-12 03:16:22.864 I SYNCHRONIZED OK
status 
Height: 1855016/1855016 (100.0%) on mainnet, not mining, net hash 324.39 MH/s, v11, up to date, 4(out)+0(in) connections, uptime 0d 0h 26m 21s
2019-06-12 03:19:36.370 W monerod is now disconnected from the network
set_log 1
Log level is now 1
2019-06-12 03:19:52.093 I 0[priority]Connect failed to 192.168.1.39:18080
2019-06-12 03:19:52.414 I [24.5.71.36:18080 e667e2b4-324b-4903-a4bc-ab6b59c68eda OUT] NEW CONNECTION
```
I do have a `--add-priority-node 192.168.1.39` on the daemon, causing the `connect failed`in the log.  
GUI Wallet 0.14.0.0 is running on `192.168.1.39`, and is syncing, but very slowly.

I get a bunch of `transaction with hash <hash> not found in db` on a 200Mb fiber.
but that's not a problem as I understand.

All in all, it seems to be running.

## trasherdk | 2019-06-12T04:19:51+00:00
I'm not sure what kind of log entries you are looking for, so I'll just add what I think could be interesting. 
```
2019-06-12 04:15:56.264 I transaction with hash f20acc0e3af8cbbb36b4efe015af7d41f86d4ada9f23d155d7b65f9a85726507 not found in db
2019-06-12 04:15:56.438 I Transaction added to pool: txid <f20acc0e3af8cbbb36b4efe015af7d41f86d4ada9f23d155d7b65f9a85726507> weight: 1772 fee/byte: 17934.5
2019-06-12 04:15:56.538 E Transaction not relayed - no peers available
2019-06-12 04:15:56.538 I Received NOTIFY_NEW_FLUFFY_BLOCK <5c4c377704e1ec80e16b8850f5925ac64391a34b620edbafda8da52d3c418f02> (height 1855026, 0 txes)
```

## trasherdk | 2019-06-12T04:32:17+00:00
Now gui wallet has disconnected.
```
2019-06-12 04:19:44.988 I [75.80.213.251:18080 OUT] Timeout on invoke operation happened, command: 1001 timeout: 5000
2019-06-12 04:19:44.989 I Failed to invoke command 1001 return code -4
2019-06-12 04:19:44.989 W There were 9 blocks in the last 60 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack. Or it could be just sheer bad luck.
2019-06-12 04:19:44.989 I HTTP [192.168.1.39] GET /json_rpc
2019-06-12 04:19:44.989 W [75.80.213.251:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2019-06-12 04:19:44.989 W [75.80.213.251:18080 OUT] COMMAND_HANDSHAKE Failed
2019-06-12 04:19:44.989 I [75.80.213.251:18080 OUT] Failed to HANDSHAKE with peer 75.80.213.251:18080
2019-06-12 04:19:44.990 I [192.168.1.39:64358 INC] Calling RPC method get_version
2019-06-12 04:19:44.990 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.991 I Including transaction <5335a318920a93d43262a11ab3804184f45fc2a3bb01779b2c83423f64d205e9>
2019-06-12 04:19:44.993 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.993 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.994 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.994 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.994 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.995 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.995 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.995 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.995 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.995 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.995 W Failed to get remote endpoint: Transport endpoint is not connected:107
2019-06-12 04:19:44.997 I HTTP [192.168.1.39] GET /json_rpc
2019-06-12 04:19:44.997 I [192.168.1.39:64998 INC] Calling RPC method get_version
2019-06-12 04:19:45.060 I HTTP [192.168.1.39] GET /json_rpc
2019-06-12 04:19:45.060 I [192.168.1.39:64998 INC] Calling RPC method get_info
2019-06-12 04:19:45.296 I [74.103.142.198:18080 cac6e781-1a12-43d5-9d3a-d1c63691d036 OUT] NEW CONNECTION
2019-06-12 04:19:46.548 I [75.80.213.251:18080 OUT] -->>NOTIFY_RESPONSE_CHAIN_ENTRY: m_start_height=200322, m_total_height=1855026, m_block_ids.size()=10000
```
Wallet reconnected, by itself, at 27 blocks behind.  
While the wallet was syncing around 5000 blocks, I was prompted for password 3 times, ~~causing the sync to pause, while waiting for me to notice~~.  
Something else caused the wallet sync to pause.


## dEBRUYNE-1 | 2019-06-12T06:33:17+00:00
>GUI Wallet 0.14.0.0 

There may be compatibility issues here which cause issues. In addition, there were some problems related to SSL that got fixed in a pull request that was only recently merged (i.e. #5622). 

Could you perhaps recompile from the `release-v0.14` branch? 

## dEBRUYNE-1 | 2019-06-12T06:35:16+00:00
@BKdilse - A few more pull requests have been merged. Could you perhaps recompile (preferably from the `release-v0.14` branch)? 

## trasherdk | 2019-06-12T08:10:16+00:00
Running `Monero 'Boron Butterfly' (v0.14.1.0-538fae4e)` waiting for something to happen :)

## trasherdk | 2019-06-12T11:05:08+00:00
Latest build `Boron Butterfly' (v0.14.1.0-538fae4e)` is running without any problems showing in the log.
Let me know if I can run a later build for you.


## moneromooo-monero | 2019-06-12T12:12:11+00:00
> I had to restart daemon today, because I lost connection to the host.
> No problems between daemon host and internet.

What is "I" here ?


## trasherdk | 2019-06-12T18:19:33+00:00
My ssh connection to the host running the monerod daemon was disconnected, probably because of a switch lost power supply. I (Me) had to reconnect, restart the daemon, to see what is going on.

The monero host is connected directly to the router, and not through the switch, and did not suffer from the power glitch.

Anyway. The latest build `538fae4e` is running smooth, without too much noise in the log.

## moneromooo-monero | 2019-06-12T20:23:33+00:00
FWIW, "what is going on" is logged in ~/.bitmonero/bitmonero.log (unless overridden).

## BKdilse | 2019-06-15T19:46:57+00:00
Guys, don't want to speak too soon, but since I migrated my pool off HDD to SSD, my issues seem to have gone away.  Daemon has not fallen behind, and I don't see any failures to read block data.

## dEBRUYNE-1 | 2019-06-26T17:39:55+00:00
@trasherdk - Can you confirm your issue has been resolved?

## trasherdk | 2019-06-27T02:24:36+00:00
@dEBRUYNE-1 Yes, I'm all synced up, pruned and no unexpected noise in the log.

Synced 1383 blocks in 00:25:46 :)
```
2019-06-27 01:28:12.369 I Monero 'Boron Butterfly' (v0.14.1.0-29a505d1c)
...
2019-06-27 01:28:25.591 I [24.31.217.75:18080 OUT] Sync data returned a new top block candidate: 1864367 -> 1865750 [Your node is 1383 blocks (1 days) behind] 
SYNCHRONIZATION started
2019-06-27 01:28:42.408 I Synced 1864387/1865750 (99%, 1363 left)
2019-06-27 01:28:51.400 I Synced 1864407/1865750 (99%, 1343 left)
...
2019-06-27 01:53:40.093 I Synced 1865755/1865755
2019-06-27 01:54:11.037 I Synced 1865756/1865756
2019-06-27 01:54:11.038 I SYNCHRONIZED OK
```


## dEBRUYNE-1 | 2019-06-27T05:48:20+00:00
All right, going to mark this as resolved then. 

## dEBRUYNE-1 | 2019-06-27T05:48:25+00:00
+resolved

# Action History
- Created by: trasherdk | 2019-06-11T10:02:05+00:00
- Closed at: 2019-06-27T05:57:39+00:00
