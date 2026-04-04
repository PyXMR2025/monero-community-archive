---
title: 'Proposal: download first, verify later for intermittent internet connections'
source_url: https://github.com/monero-project/monero/issues/8257
author: Gingeropolous
assignees: []
labels: []
created_at: '2022-04-13T04:57:56+00:00'
updated_at: '2022-05-29T15:32:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Initial block sync is painfully slow, and will continue to be. It's the nature of the beast. 

The existing software gobbles some data from the net, then verifies that batch of data, and then gobbles some more. This makes the sync time much longer than the actual time necessary to download a 120 gig bunch of data.

While this makes sense (for the verification and trust issues stuff), I think it would be beneficial to have an option to download the blockchain from the network, and then verify later. Primarily, this use case would be for users that have spotty / intermittent internet connection, which one could imagine might occur in a hostile environment (yah know, like a war).

Of course, there's the problem of trusting the peers you are downloading from (at least for initial sync), but much like everything else I yammer on about, I think headers first sync + peer consensus could be useful here. Basically, you connect to your standard 12 peers, get the header chain, check that they all agree, and then start the download process (from all 12, presumably). The data gets stored in like 1 hour because torrent-like behavior like woh. Then, wouldn't you know it, your internet goes out because I dunno someone blew up something. Doesn't matter, you got the data. Now your node can churn through all these goram ring signatures and have a fully functioning node by the time the internet comes back up. Sure, you'll have to sync up with a new live connection, but that'll be nothing compared to trying to sync the blockchain with 1-2 hour bursts of internet on a random laptop you found in an abandoned house as you make your way through a bombed out wasteland. 

And sure, bootstrap thing might provide the same thing, but its not as good. 

And sure, one could just download the blockchain.raw from the monero website, but thats relying on centralized things

# Discussion History
## Gingeropolous | 2022-04-17T15:47:19+00:00
i mean, these are obvious numbers, but for a laptop built in 2007 that has a 7200 rpm spinny and a Intel(R) Core(TM)2 Duo CPU T8100  @ 2.10GHz, it took 3 weeks to synchronize from the network. 

When I transferred the file from another box on the network, the transfer took  "real 27m36.383s" to the same box. 

when i downloaded a data.mdb from a remote server over the internet, it took real    105m10.797s

if you are in a situation with spotty internet, are you more likely to have 3 weeks of uninterupted internet, whereas the whole thing could be downloaded in hours and then processed offline?




## selsta | 2022-04-18T22:22:44+00:00
> And sure, bootstrap thing might provide the same thing, but its not as good.

I think the bootstrap file is perfect for this scenario compared to adding a whole bunch of code for a niche scenario.

## trasherdk | 2022-04-19T07:36:58+00:00
```sh
# uname -a
Linux compaq-laptop 4.4.301 #1 SMP Mon Jan 31 20:27:28 CST 2022 x86_64 Intel(R) Core(TM)2 Duo CPU T8100 @ 2.10GHz GenuineIntel GNU/Linux
```
Even with SSD  it was painfully slow :laughing: 

# Action History
- Created by: Gingeropolous | 2022-04-13T04:57:56+00:00
