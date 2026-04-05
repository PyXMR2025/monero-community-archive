---
title: Incoming nodes disconnecting on new block in stressnet
source_url: https://github.com/seraphis-migration/monero/issues/140
author: j-berman
assignees: []
labels: []
created_at: '2025-10-06T19:17:15+00:00'
updated_at: '2025-10-21T17:41:16+00:00'
type: issue
status: closed
closed_at: '2025-10-21T17:41:16+00:00'
---

# Original Description
Reported by @nahuhh

```
2025-10-06 15:16:21.826 I Synced 2849623/2849623                                                                                                                                                                                                                                                                                                                                                                                                                    [52/1645]
2025-10-06 15:16:59.171 I [146.70.237.155:19803 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                                                                                                                                                                           
2025-10-06 15:16:59.171 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                                                                                                                                                                            
2025-10-06 15:16:59.175 I [146.70.237.155:31469 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                                                                                                                                                                           
2025-10-06 15:16:59.175 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                                                                                
2025-10-06 15:16:59.591 I [146.70.237.155:37469 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                                                                               
2025-10-06 15:16:59.591 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                                                                                
2025-10-06 15:17:07.340 W There were 18 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.                                                                                                                  
2025-10-06 15:17:18.728 I [146.70.237.155:49480 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                                                                               
2025-10-06 15:17:18.728 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:17:18.844 I [146.70.237.155:7489 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:17:18.844 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:17:33.598 I [146.70.237.155:21077 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                 
2025-10-06 15:17:33.598 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:17:37.764 I [46.19.136.242:48030 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:17:37.765 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:17:45.072 I [202.169.99.195:60261 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                 
2025-10-06 15:17:45.073 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:17:47.739 I [37.67.73.63:17376 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                    
2025-10-06 15:17:47.739 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:17:51.499 I [146.70.237.155:28126 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                 
2025-10-06 15:17:51.499 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:17:53.019 I [100.14.80.141:51494 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:17:53.019 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:17:54.985 I [148.63.215.132:49268 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                 
2025-10-06 15:17:54.985 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:17:55.363 I [46.19.136.242:54244 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:17:55.363 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:00.108 I [37.67.73.63:17456 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                    
2025-10-06 15:18:00.108 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:00.305 I [100.14.80.141:39394 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:00.305 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:02.478 I [100.14.80.141:39402 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:02.479 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:02.482 I [148.63.215.132:49316 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                 
2025-10-06 15:18:02.482 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:02.906 I [46.19.136.242:60940 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:02.906 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:03.473 I [202.169.99.195:18412 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                 
2025-10-06 15:18:03.473 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:04.562 I [100.14.80.141:39416 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:04.562 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:06.056 I [146.70.237.155:38490 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                 
2025-10-06 15:18:06.057 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:06.625 I [100.14.80.141:46142 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:06.625 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:08.684 I [100.14.80.141:46146 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:08.684 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:09.886 I [88.99.195.15:36368 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                   
2025-10-06 15:18:09.886 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:18.478 I [100.14.80.141:46154 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:18.478 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:20.417 I [89.233.207.111:33930 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                 
2025-10-06 15:18:20.417 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:20.578 I [100.14.80.141:45642 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:20.578 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:24.509 I [46.19.136.242:57720 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:24.509 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:24.509 I [100.14.80.141:45652 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:24.509 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:25.635 I [108.94.105.78:52714 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:25.635 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:26.697 I [100.14.80.141:60230 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:26.697 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:27.359 I [109.54.10.145:44524 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:27.359 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:28.101 I [108.94.105.78:52720 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:28.101 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:28.193 I [146.70.237.155:35535 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                 
2025-10-06 15:18:28.193 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:18:29.106 I [46.19.136.242:57732 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:18:29.106 I SYNCHRONIZATION started                                                                                                                                                                                                                                                                  
2025-10-06 15:19:10.686 I [108.94.105.78:52724 INC] Sync data returned a new top block candidate: 2849623 -> 2849624 [Your node is 1 blocks (2.0 minutes) behind]                                                                                                                                                  
2025-10-06 15:19:10.686 I SYNCHRONIZATION started     
```

And log level 2:

```
2025-10-06 16:25:23.110 I [169.150.242.16:56720 INC] Sync data returned a new top block candidate: 2849631 -> 2849632 [Your node is 1 blocks (2.0 minutes) behind]                                                                                           [171/1951]
2025-10-06 16:25:23.110 I SYNCHRONIZATION started                                                                                                                                                                                                                      
2025-10-06 16:25:23.110 D Space remaining: 148158963712                                                                                                                                                                                                                
2025-10-06 16:25:23.110 D Size threshold:  0                                                                                                                                                                                                                           
2025-10-06 16:25:23.110 I [169.150.242.16:56720 INC] Remote blockchain height: 2849632, id: <a0816d6050a5869e62cf92072d58847388f473af8cbf67ddee823981920d9df2>                                                                                                         
2025-10-06 16:25:23.110 D [169.150.242.16:56720 INC] requesting callback                                                                                                                
2025-10-06 16:25:23.110 D Percent used: 15.6474  Percent threshold: 90.0000                                                                                                             
2025-10-06 16:25:23.110 I [169.150.242.16:56720 INC] [0] state: requesting callback in state synchronizing                                                                              
2025-10-06 16:25:23.111 D Spawned connection #6701 to 0.0.0.0 currently we have sockets count:12                                                                                        
2025-10-06 16:25:23.111 D connections_ size now 2                                                                                                                                       
2025-10-06 16:25:23.113 I Transaction added to pool: txid <44e0eec231f2c12206f0be82734d9dd67789081b7512e39f21b364f71c0bc861> weight: 6498 fee/byte: 20000, count: 18573                 
2025-10-06 16:25:23.113 D [169.150.242.16:56720 INC] COMMAND_HANDSHAKE                                                                                                                  
2025-10-06 16:25:23.113 D DB map size:     175642472448                                                                                                                                 
2025-10-06 16:25:23.113 D Space used:      27483557888                                                                                                                                  
2025-10-06 16:25:23.113 D Space remaining: 148158914560                                                                                                                                 
2025-10-06 16:25:23.113 D Size threshold:  0                                                                                                                                            
2025-10-06 16:25:23.113 D Percent used: 15.6474  Percent threshold: 90.0000                                                                                                             
2025-10-06 16:25:23.114 D tx added to pool: <44e0eec231f2c12206f0be82734d9dd67789081b7512e39f21b364f71c0bc861>                                                                          
2025-10-06 16:25:23.114 I [169.150.242.16:56720 INC] 2909 bytes sent for category command-1001 initiated by us                                                                          
2025-10-06 16:25:23.114 D [169.150.242.16:56720 INC] LEVIN_PACKET_SENT. [len=2909, flags2, r?=?, cmd = 1001, ver=1 
2025-10-06 16:25:23.114 D [169.150.242.16:56720 INC] callback fired                                                                                                                     
2025-10-06 16:25:23.114 I [169.150.242.16:56720 INC] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=32                                                                                    
2025-10-06 16:25:23.114 D [169.150.242.16:56720 INC] post N10cryptonote20NOTIFY_REQUEST_CHAINE -->                                                                 
2025-10-06 16:25:23.114 I [169.150.242.16:56720 INC] 1047 bytes sent for category command-2006 initiated by us                                                                                                                        
2025-10-06 16:25:23.115 D [169.150.242.16:56720 INC] LEVIN_PACKET_SENT. [len=1047, flags1, r?=?, cmd = 2006, ver=1                                                                      
2025-10-06 16:25:23.115 I [169.150.242.16:56720 INC] [0] state: requesting chain in state synchronizing                                                                                 
2025-10-06 16:25:23.115 D bulletproof+ clawback: 0                                                                 
2025-10-06 16:25:23.115 D tx <c4f941844e10c8675b18cc74c2726eeed88bec95e9dc774baeef818363b6f806>already have transaction in tx_pool                                                                                                    
2025-10-06 16:25:23.115 D Transaction <c4f941844e10c8675b18cc74c2726eeed88bec95e9dc774baeef818363b6f806> not added to pool                                                                                                            
2025-10-06 16:25:23.116 D bulletproof+ clawback: 0                                                                                 
2025-10-06 16:25:23.116 D tx <5b2994f4a7226d1472afe11a89efe91d7c9da20758fa97fab6af01cc768676d4>already have transaction in tx_pool                                                                                                                                     
2025-10-06 16:25:23.116 D Transaction <5b2994f4a7226d1472afe11a89efe91d7c9da20758fa97fab6af01cc768676d4> not added to pool                                                                                                                                             
2025-10-06 16:25:23.117 D DB map size:     175642472448                                                                            
2025-10-06 16:25:23.117 D Space used:      27483557888                                                                             
2025-10-06 16:25:23.117 D Space remaining: 148158914560                                                                            
2025-10-06 16:25:23.117 D Size threshold:  0                     
2025-10-06 16:25:23.117 D Percent used: 15.6474  Percent threshold: 90.0000                                                        
2025-10-06 16:25:23.120 D Queueing 1 transaction(s) for Dandelion++ fluffing                                                       
2025-10-06 16:25:23.121 D bulletproof+ clawback: 0                                                                                 
2025-10-06 16:25:23.121 D tx <44e0eec231f2c12206f0be82734d9dd67789081b7512e39f21b364f71c0bc861>already have transaction in tx_pool                                                                                                                                     
2025-10-06 16:25:23.121 D Transaction <44e0eec231f2c12206f0be82734d9dd67789081b7512e39f21b364f71c0bc861> not added to pool                                                                                                                                             
2025-10-06 16:25:23.122 D bulletproof+ clawback: 0                                                                                 
2025-10-06 16:25:23.122 D tx <61a782a790aa0bcf7605b9a3ecea9ebfa5e0c054090076f2e33ab52fde7f5400>already have transaction in tx_pool                                                                                                                                     
2025-10-06 16:25:23.122 D Transaction <61a782a790aa0bcf7605b9a3ecea9ebfa5e0c054090076f2e33ab52fde7f5400> not added to pool                                                                                                                                             
2025-10-06 16:25:23.285 I Target height decreasing from 2849632 to 2849631                                                         
2025-10-06 16:25:23.285 I [169.150.242.16:56720 INC] [0] state: closed in state synchronizing                                                                                                                                                                          
2025-10-06 16:25:23.285 I [169.150.242.16:56720 934e0896-ffab-4f9d-a1a3-2e0a73d067b0 INC] CLOSE CONNECTION     
```

# Discussion History
## j-berman | 2025-10-07T02:10:38+00:00
@spackle-xmr said in the alpha stressnet channel:

> sometimes after finding a block my monerod will report being disconnected from the network a few seconds later

I think it may be the block finder's node closing connections here. @spackle-xmr do you by chance have log level 2 with this error too?

## spackle-xmr | 2025-10-07T02:30:38+00:00

I believe this is in the log I captured, along with the entries for [Issue 141](https://github.com/seraphis-migration/monero/issues/141)
The node found a block at ln 841939 and was disconnected at ln 844267, about 5 seconds later.
[log2.txt.gz](https://github.com/user-attachments/files/22733729/log2.txt.gz)

## spackle-xmr | 2025-10-07T15:58:49+00:00
I was able to reproduce the issue on a better connected node; the node was both mining and spamming. 
The node initially had 9(out) connections, which decreased slowly over a half hour until the node was completely disconnected.
The entire log for this is 1.4 GB (180MB compressed). In place of the full log, here are the final 1.2 million lines. They include the disconnection on ln 203048 and the mined block preceding it on ln 103002.

[ending.log.gz](https://github.com/user-attachments/files/22749125/ending.log.gz)


## j-berman | 2025-10-07T16:29:17+00:00
The problem is that the node is relaying the full fluffy block to its peers, and that full fluffy block can exceed the byte limit of 4mb:

```
[0m[0;32m2025-10-07 15:28:32.359	D [0;32m[62.38.144.238:28080 OUT] RELAYING FLUFFY BLOCK TO PEER
[0m[0;32m2025-10-07 15:28:32.359	D [0;32m[85.86.209.47:28080 OUT] RELAYING FLUFFY BLOCK TO PEER
[0m[0;32m2025-10-07 15:28:32.359	D [0;32m[181.89.154.82:28080 OUT] RELAYING FLUFFY BLOCK TO PEER
[0m[0;32m2025-10-07 15:28:32.359	D [0;32m[172.103.161.225:28080 OUT] RELAYING FLUFFY BLOCK TO PEER
[0m[0;36m2025-10-07 15:28:32.361	I [0;36m[172.103.161.225:28080 OUT] 4213921 bytes sent for category command-2008 initiated by us
[0m[0;32m2025-10-07 15:28:32.361	D [0;32m[172.103.161.225:28080 OUT] LEVIN_PACKET_SENT. [len=4213921, flags1, r?=?, cmd = 2008, ver=1
[0m[0;36m2025-10-07 15:28:32.362	I [0;36m[62.38.144.238:28080 OUT] 4213921 bytes sent for category command-2008 initiated by us
[0m[0;32m2025-10-07 15:28:32.362	D [0;32m[62.38.144.238:28080 OUT] LEVIN_PACKET_SENT. [len=4213921, flags1, r?=?, cmd = 2008, ver=1
[0m[0;36m2025-10-07 15:28:32.362	I [0;36m[181.89.154.82:28080 OUT] 4213921 bytes sent for category command-2008 initiated by us
[0m[0;32m2025-10-07 15:28:32.362	D [0;32m[181.89.154.82:28080 OUT] LEVIN_PACKET_SENT. [len=4213921, flags1, r?=?, cmd = 2008, ver=1
[0m[0;36m2025-10-07 15:28:32.362	I [0;36m[85.86.209.47:28080 OUT] 4213921 bytes sent for category command-2008 initiated by us
[0m[0;32m2025-10-07 15:28:32.362	D [0;32m[85.86.209.47:28080 OUT] LEVIN_PACKET_SENT. [len=4213921, flags1, r?=?, cmd = 2008, ver=1
```

4213921 bytes exceeds the [fluffy block limit of 4mb (or 4194304 bytes)](https://github.com/monero-project/monero/blob/8e9ab9677f90492bca3c7555a246f2a8677bd570/src/cryptonote_basic/connection_context.cpp#L63).  Nodes will close connections that send packets that exceed the limit in `handle_recv`.

Seems related to https://github.com/monero-project/monero/issues/10151 

The node shouldn't need to relay the full fluffy blocks, and there should probably be some saner code that paginates requested txs from a fluffy block (if not already there).

This is probably also related to #139, since I imagine disconnects upon block relay would slow down block propagation.

## j-berman | 2025-10-07T18:37:56+00:00
A node closing an incoming connection as a result of a large new fluffy block would see the following log reported by u/mayhem69 from this error:

```
2025-10-07 18:25:26.571 E [169.150.242.16:50518 INC] Maximum packet size exceed!, m_max_packet_size = 4194304, packet header received 4255488, command 2008, connection will be closed.
```

It looks like there actually is a distinct (potentially related) issue going on causing the disconnects in the OP, since the logs don't show that.

## j-berman | 2025-10-07T19:52:04+00:00
Correction: ignore below. `NOTIFY_RESPONSE_CHAIN_ENTRY` would not hit the 4mb limit here because it's just the block's tx hashes, not the block contents.
_____

The OP error looks like it's probably related to the same problem.

@nahuhh's node is requesting `NOTIFY_REQUEST_CHAIN`. The responding node then handles that, and looks like it's probably [including a block in the response](https://github.com/monero-project/monero/blob/0d500f534941b072a3af9689482a76955ba2c003/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1808) ~~that is larger than the 4mb limit on the [`NOTIFY_RESPONSE_CHAIN_ENTRY` max byte size](https://github.com/monero-project/monero/blob/0d500f534941b072a3af9689482a76955ba2c003/src/cryptonote_basic/connection_context.cpp#L60-L61).~~ (not correct)

EDIT: except would have expected the max packet size error to appear in @nahuhh's logs too, handling command [2007](https://github.com/monero-project/monero/blob/0d500f534941b072a3af9689482a76955ba2c003/src/cryptonote_protocol/cryptonote_protocol_defs.h#L291).

## j-berman | 2025-10-09T03:04:26+00:00
@jeffro256 pointed out that when `monerod` handles a found block (either when it mines the block, or a found block is submitted via the RPC), it relays the full fluffy block [here](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/cryptonote_core/cryptonote_core.cpp#L1309-L1331). @spackle-xmr's logs are consistent with that.

Some simple improvements that may be worth implementing:
1) Relay an empty fluffy block in that spot (definite yes imo).
2) Bump the fluffy block byte limit to match new block byte limit (because it can potentially be a full block).

A more involved, and better long term fix than (2) may be to limit the number of txs that `handle_request_fluffy_missing_tx` includes, making sure the final payload is <4mb. The node handling the fluffy block could then just make rounds of requests for the remaining missing txs to peers.

EDIT: removed mention of NOTIFY_RESPONSE_CHAIN_ENTRY because that it is actually probably not the cause of any issues here, see above.

## j-berman | 2025-10-21T01:45:20+00:00
@nahuhh do you still see this issue with v1.2? This should be fixed by #160

## nahuhh | 2025-10-21T05:26:29+00:00
> @nahuhh do you still see this issue with v1.2? This should be fixed by #160

it seems to be much improved since peers updated to 1.2

instead of disconnecting repeatedly for minutes and struggling to sync the block, it syncs the block in a few (~5) seconds.

I do think ive still seen sync_info look like connections drop while syncing blocks, but i'll have to double check. Its definitely not the same symptom as OP


## j-berman | 2025-10-21T17:41:16+00:00
> I do think ive still seen sync_info look like connections drop while syncing blocks, but i'll have to double check. Its definitely not the same symptom as OP

If you find good logs showing this happening, that would be very helpful / worth a new issue I think. Closing this issue since it seems solved.

# Action History
- Created by: j-berman | 2025-10-06T19:17:15+00:00
- Closed at: 2025-10-21T17:41:16+00:00
