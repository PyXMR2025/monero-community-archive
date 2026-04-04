---
title: Clearnet + I2P torrenting built into monerod
source_url: https://github.com/monero-project/meta/issues/634
author: carrington1859
assignees: []
labels: []
created_at: '2021-11-24T01:05:31+00:00'
updated_at: '2021-11-25T19:19:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Presently, distribution of the core Monero software mostly relies on getmonero.org or github. Now that we have reproducible builds, we should work towards distributing this critical software in a decentralized way. By giving monerod the capability to seed the source code and/or compiled software, Monero nodes will become self-replicating and the Monero network will become more resilient. Of course, if you don't already have a node you would access these torrents in the regular clearnet/i2p ways. The idea here is that anyone who runs a node can easily become a seeder to those who need to download.

Integrated torrenting capabilities could also serve as an update mechanism for the core software. 

For example, the I2P(Java) router can receive updates over an I2P torrent for Linux, Windows and MacOS. A release package is built to the .su3 file specification. The .su3 file is a signed compressed file (ZIP/EXE/DMG) to be downloaded by the i2p torrent client. Upon a new release, the I2P newsfeed operators generate a magnet link and create new files [HERE](https://github.com/i2p/i2p.newsxml/tree/master/data) (releases.json + entries.html). The newsfeed operators run the ./news.sh script (in the repo root), and the torrent is embedded in the RSS feed. The router downloads the newsfeed (a different "XML type" .su3 file) from the newsfeed operators which contains an RSS feed. If there's a new release torrent, the router uses the magnet link to download (via I2PSnark) the .su3 release and a platform-specific process prepares the update to occur on the next router restart. The aforementioned RSS feed also distributes release notes, news & blocklists. By default, the router seeds the updates such that I2P now has a very small distribution burden. The newsfeed operators do represent a centralizing/bootstrapping element, but release packages are signed separately from the signing of the newsfeed and anyone can setup a newsfeed server over I2P with Docker.  (Thanks to IDK at I2P for the explanation)

We can, of course, imagine variations on the above system and the procedure for how the "official" torrents for each release get created should be discussed. There are other possibilities such as whether the source code itself should be distributed via torrent or how this could be integrated into the GUI.

It seems that moving towards a torrent-based distribution and update system would significantly lower the maintenance burden and attack surface resulting from the present systems. It has also been noted that the present reliance on getmonero.org for a CDN has caused bottlenecks in development of other aspect of the website. Monero shouldn't rely on expensive centralized infrastructure [reliant on sponsorships](https://github.com/monero-project/monero-site/pull/1888).

This idea started as a [Monero Bounty](https://bounties.monero.social/posts/40/clearnet-i2p-torrenting-built-into-monerod), but seeing as there is quite a big scope here I think it warrants a wider community discussion.

Previous discussion on using torrents for Monero software distribution:

https://github.com/monero-project/monero-site/issues/1629
https://github.com/monero-project/monero-site/issues/508
https://github.com/monero-project/monero-site/pull/515
https://www.reddit.com/r/Monero/comments/7oznm8/help_verify_and_then_seed_monero_cligui_torrents/

Some of the older discussions are from before Monero had reproducible builds, which I think changes the context somewhat. Several older discussions focused on the maintenance burden of creating torrents for each release, but maybe if the torrents were also the main updating mechanism for Monero node then that small maintenance burden could ease pressure in other areas.

There is no perfect solution and there will always be bootstrapping problems, but I believe that these discussions will only become more relevant as Monero grows. Hopefully, a discussion of the problems can lead to defining some narrow [bounties](https://bounties.monero.social) or encourage [CCS proposals](https://ccs.getmonero.org/) to move the project forward in this area.

Edit: Some further discussion [here](https://www.reddit.com/r/Monero/comments/r1hblq/selfreplicating_monero_nodes_on_the_horizon_with/).

# Discussion History
# Action History
- Created by: carrington1859 | 2021-11-24T01:05:31+00:00
