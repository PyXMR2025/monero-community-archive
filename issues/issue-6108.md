---
title: Monero fails to sync
source_url: https://github.com/monero-project/monero/issues/6108
author: taoeffect
assignees: []
labels: []
created_at: '2019-11-07T23:19:24+00:00'
updated_at: '2019-11-12T06:48:51+00:00'
type: issue
status: closed
closed_at: '2019-11-08T00:34:18+00:00'
---

# Original Description
I recently restarted a monero 0.14.1.2 node and now it's unable to sync:

```
2019-09-11 09:37:47.498 I Monero 'Boron Butterfly' (v0.14.1.2-release)                                                                                                                                                                     
2019-09-11 09:37:47.500 I Initializing cryptonote protocol...                                                                                                                                                                              
2019-09-11 09:37:47.500 I Cryptonote protocol initialized OK                                                                                                                                                                               
2019-09-11 09:37:47.503 I Initializing p2p server...                                                                                                                                                                                       
2019-09-11 09:37:55.041 I p2p server initialized OK                                                                                                                                                                                        
2019-09-11 09:37:55.042 I Initializing core RPC server...                                                                                                                                                                                  
2019-09-11 09:37:55.153 I Binding on 0.0.0.0:18081                                                                                                                                                                                         
2019-09-11 09:37:55.156 I Generating SSL certificate                                                                                                                                                                                       
2019-09-11 09:37:56.827 I core RPC server initialized OK on port: 18081                                                                                                                                                                    
2019-09-11 09:37:56.827 I Initializing core...                                                                                                                                                                                             
2019-09-11 09:37:56.827 I Loading blockchain from folder /home/unpriv/.bitmonero/lmdb ...                                                                                                                                                  
2019-09-11 09:37:58.965 I Loading checkpoints                                                                                                                                                                                              
2019-09-11 09:37:59.301 W WARNING: no two valid DNS TXT records were received                                                                                                                                                              
2019-09-11 09:37:59.326 I Core initialized OK                                                                                                                                                                                              
2019-09-11 09:37:59.326 I Starting core RPC server...                                                                                                                                                                                      
2019-09-11 09:37:59.326 I core RPC server started ok                                                                                                                                                                                       
2019-09-11 09:37:59.331 I Starting p2p net loop...                                                                                                                                                                                         
2019-09-11 09:38:00.331 I                                                                                                                                                                                                                  
**********************************************************************                                                                                                                                                                     
The daemon will start synchronizing with the network. This may take a long time to complete.                                                                                                                                               
                                                                                                                                                                                                                                           
You can set the level of process detailization through "set_log <level|categories>" command,                                                                                                                                               
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).                                                                                                                             
                                                                                                                                                                                                                                           
Use the "help" command to see the list of available commands.                                                                                                                                                                              
Use "help <command>" to see a command's documentation.                                                                                                                                                                                     
**********************************************************************                                                                                                                                                                     
                                                                                                                                                                                                                                           
2019-09-11 09:38:00.332 W **********************************************************************                                                                                                                                           
2019-09-11 09:38:00.332 W Last scheduled hard fork time shows a daemon update is needed soon.                                                                                                                                              
2019-09-11 09:38:00.332 W ********************************************************************** 
2019-09-11 09:38:00.788 I [xxx.xxx.xxx.xxx:18080 OUT] Sync data returned a new top block candidate: 1953546 -> 1962037 [Your node is 8491 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:38:00.878 W WARNING: no two valid DNS TXT records were received
2019-09-11 09:40:53.952 I [xxx.xxx.xxx.xxx:18080 OUT] Sync data returned a new top block candidate: 1953546 -> 1962038 [Your node is 8492 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:45:47.485 I [xxx.xxx.xxx.xxx:19385 INC] Sync data returned a new top block candidate: 1953546 -> 1962040 [Your node is 8494 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:49:27.553 I [xxx.xxx.xxx.xxx:41192 INC] Sync data returned a new top block candidate: 1953546 -> 1962042 [Your node is 8496 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:51:24.960 I [xxx.xxx.xxx.xxx:60758 INC] Sync data returned a new top block candidate: 1953546 -> 1962043 [Your node is 8497 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:51:33.521 I [xxx.xxx.xxx.xxx:57960 INC] Sync data returned a new top block candidate: 1953546 -> 1962043 [Your node is 8497 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:51:49.229 I [xxx.xxx.xxx.xxx:43392 INC] Sync data returned a new top block candidate: 1953546 -> 1962043 [Your node is 8497 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:52:03.483 I [xxx.xxx.xxx.xxx:59784 INC] Sync data returned a new top block candidate: 1953546 -> 1962043 [Your node is 8497 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:52:19.445 I [xxx.xxx.xxx.xxx:42158 INC] Sync data returned a new top block candidate: 1953546 -> 1962044 [Your node is 8498 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:53:04.969 I [xxx.xxx.xxx.xxx:33361 INC] Sync data returned a new top block candidate: 1953546 -> 1962045 [Your node is 8499 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:54:30.633 I [xxx.xxx.xxx.xxx:40250 INC] Sync data returned a new top block candidate: 1953546 -> 1962046 [Your node is 8500 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:55:28.816 I [xxx.xxx.xxx.xxx:54274 INC] Sync data returned a new top block candidate: 1953546 -> 1962047 [Your node is 8501 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:56:11.285 I [xxx.xxx.xxx.xxx:62662 INC] Sync data returned a new top block candidate: 1953546 -> 1962048 [Your node is 8502 blocks (11 days) behind] 
SYNCHRONIZATION started 
2019-09-11 09:57:11.917 I [xxx.xxx.xxx.xxx:61334 INC] Sync data returned a new top block candidate: 1953546 -> 1962049 [Your node is 8503 blocks (11 days) behind]

[ ... etc ... ]
```

EDIT: now noticing a few lines claiming different protocol versions (?) (12, 13, and 60), from the 11 that I have, but I'm running the latest version that's on the website AFAICT...

```
2019-09-11 10:09:46.234 W [xxx.xxx.xxx.xxx:41124 INC]  peer claims higher version that we think (60 for 1969435 instead of 11) - we may be forked from the network and a software upgrade may be needed
2019-09-11 10:11:17.408 I [xxx.xxx.xxx.xxx:55025 INC] Sync data returned a new top block candidate: 1953546 -> 1962054 [Your node is 8508 blocks (11 days) behind] 
SYNCHRONIZATION started
2019-09-11 10:14:36.618 I [xxx.xxx.xxx.xxx:55390 INC] Sync data returned a new top block candidate: 1953546 -> 1962055 [Your node is 8509 blocks (11 days) behind] 
SYNCHRONIZATION started
2019-09-11 10:17:43.622 W [xxx.xxx.xxx.xxx:50154 INC]  peer claims higher version that we think (60 for 1969436 instead of 11) - we may be forked from the network and a software upgrade may be needed
2019-09-11 10:18:21.905 I [xxx.xxx.xxx.xxx:45926 INC] Sync data returned a new top block candidate: 1953546 -> 1962056 [Your node is 8510 blocks (11 days) behind] 
SYNCHRONIZATION started
2019-09-11 10:18:25.461 I [xxx.xxx.xxx.xxx:48608 INC] Sync data returned a new top block candidate: 1953546 -> 1962057 [Your node is 8511 blocks (11 days) behind] 
SYNCHRONIZATION started
2019-09-11 10:18:55.169 I [xxx.xxx.xxx.xxx:35294 INC] Sync data returned a new top block candidate: 1953546 -> 1962057 [Your node is 8511 blocks (11 days) behind] 
SYNCHRONIZATION started
2019-09-11 10:19:20.698 I [xxx.xxx.xxx.xxx:62756 INC] Sync data returned a new top block candidate: 1953546 -> 1962059 [Your node is 8513 blocks (11 days) behind] 
SYNCHRONIZATION started
2019-09-11 10:21:28.578 I [xxx.xxx.xxx.xxx:51624 INC] Sync data returned a new top block candidate: 1953546 -> 1962060 [Your node is 8514 blocks (11 days) behind] 
SYNCHRONIZATION started
2019-09-11 10:22:54.271 W [xxx.xxx.xxx.xxx:58170 INC]  peer claims higher version that we think (13 for 1999999 instead of 11) - we may be forked from the network and a software upgrade may be needed
2019-09-11 10:22:56.027 W [xxx.xxx.xxx.xxx:12966 INC]  peer claims higher version that we think (12 for 1999999 instead of 11) - we may be forked from the network and a software upgrade may be needed
2019-09-11 10:24:41.253 W [xxx.xxx.xxx.xxx:36980 INC]  peer claims higher version that we think (12 for 1999999 instead of 11) - we may be forked from the network and a software upgrade may be needed
```

# Discussion History
## taoeffect | 2019-11-07T23:36:40+00:00
*Edited issue to note new error messages about protocol version

## xiphon | 2019-11-07T23:40:10+00:00
Could you collect the logs with `--log-level 2`?
(just check them for sensitive info before posting)

## taoeffect | 2019-11-07T23:51:51+00:00
@xiphon sure, here's a few minutes output: https://pastebin.com/mTn4zCvz (pastie expires after a few days)

## xiphon | 2019-11-08T00:02:48+00:00
Please check your clock/timezone settings

```
[0m[31m2019-09-11 10:39:10.686	E Timestamp of block with id: <e604db9c6254b4f664f73c769eb7f1f6aac3dceb9b014517722a35be8db2b98e>, 1572144491, bigger than adjusted time + 2 hours
[0m[31m2019-09-11 10:39:10.686	E Block with id: <e604db9c6254b4f664f73c769eb7f1f6aac3dceb9b014517722a35be8db2b98e>
has invalid timestamp: 1572144491
[0m[36m2019-09-11 10:39:10.686	I [5.xxx.xxx.xxx:57494 INC] Block verification failed, dropping connection
```

## taoeffect | 2019-11-08T00:34:18+00:00
*Doh!* That appears to have fixed it. Can't believe I didn't notice that. Thanks so much for your help! Hopefully this will help others who run into this same issue.

It also reminds me again of [the idea of a PoW algorithm that doesn't rely on clocks...](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2018-February/015774.html)

## jhb9 | 2019-11-12T06:13:56+00:00
Could you please explain how to correct this timestamp issue? I appear to have the same thing but do not understand how to correct it.

## trasherdk | 2019-11-12T06:48:51+00:00
Make sure your computer, the one running monerod, has the correct timezone set, and sync the clock regularly.

# Action History
- Created by: taoeffect | 2019-11-07T23:19:24+00:00
- Closed at: 2019-11-08T00:34:18+00:00
