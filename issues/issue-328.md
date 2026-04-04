---
title: Daemon stall due to threading
source_url: https://github.com/monero-project/monero/issues/328
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-06-21T20:09:02+00:00'
updated_at: '2015-07-31T10:25:15+00:00'
type: issue
status: closed
closed_at: '2015-07-31T10:25:14+00:00'
---

# Original Description
Apparently this is some threading issue. I'm running Lubuntu 64 bit, last update was ~4 weeks ago. bitmonero v0.8.8.7-1720aff.

System behavior: bitmonero, when working normally (and mining on one thread), varies between 100 - 120 %CPU. When this bug manifests, it stays at a steady ~200%. %mem is 6.5% on a 4 gig box. 

The print_cn is where the double threading can be observed, with the two headers.  

print_cn
2015-Jun-21 16:02:58.945555 Read command: print_cn
2015-Jun-21 16:02:58.971285 Remote Host                   Peer id             Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Dow
n(now)     Up (kB/s) Up(now)

Remote Host                   Peer id             Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)


# Discussion History
## Gingeropolous | 2015-06-22T23:07:59+00:00
Additional notes: doesn't seem to manifest on testnet. Ran for 24 hours without stall while mining on testnet. 

Might be due to mining: ran for 24 hours on main-net without mining and it didn't stall. 


## Gingeropolous | 2015-06-23T02:50:10+00:00
sent a bunch of transactions on testnet, still no problem. 


## Gingeropolous | 2015-06-29T10:03:25+00:00
Just happened on v0.8.8.7-1720aff  (2 print_cn headers), but simplewallet is able to synchronize and the daemon is still functioning. 

edited to add: nevermind - simeplwallet stalled as well. Was crawling (still refreshing) but ultimately became impatient. 

###FASCINATING!!!! 

If you try to exit the daemon (using the exit command) you can kill the rogue new thread! I went from 2 print_cn headers to 1. Oh lemme see if I can't grep this. Bah. set_log 2 is just too much. 


## Gingeropolous | 2015-07-31T10:25:14+00:00
new daemon seems to have fixed this


# Action History
- Created by: Gingeropolous | 2015-06-21T20:09:02+00:00
- Closed at: 2015-07-31T10:25:14+00:00
