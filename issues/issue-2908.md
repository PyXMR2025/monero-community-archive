---
title: downloading blockchain.raw extremely slow
source_url: https://github.com/monero-project/monero/issues/2908
author: linecolumn
assignees: []
labels: []
created_at: '2017-12-11T16:12:54+00:00'
updated_at: '2024-12-20T01:39:31+00:00'
type: issue
status: closed
closed_at: '2017-12-20T13:13:09+00:00'
---

# Original Description
Trying to setup slave, for the first time, it was pain to download client (gui and cli version), was taking for ages.

Then I hit extremely slow blockchain sync to the slave, so little bit of searching I found that blockchain can be downloaded in raw format and imported with verify=0.

Unfortunately, downloading the blockchain.raw is *extremely* slow, we are talking late '90 slow:

# wget https://downloads.getmonero.org/blockchain.raw

Downloading from US server, I get 8K/s, eta 25days
Downloading from EU server, I get 30K/s, eta 14days

Both servers have 100mbit/s up/down link.

I know that we should not use mirror for this files (are there any), but it is quite hard to try and do anything if this first, essential step, is so slow.

While here, off topic, can I generate address on node without fully synced blockchain on it and start mining? 

Thanks!

# Discussion History
## lemarier | 2017-12-11T18:57:23+00:00
Same here.

Caped to 30 kb/s

## danrmiller | 2017-12-11T19:37:42+00:00
@linecolumn be careful with verify=0, that isn't going to affect your download speed and could allow whoever you got the data from to rip you off. I realize you might feel that you trust the source you obtained it from, like getmonero.org, but I wouldn't mention it here, to avoid confusion.

## moneromooo-monero | 2017-12-11T20:00:43+00:00
Yes. Why would you want to not verify what you're importing from the internet ? It's a bad idea.

## keffnet | 2017-12-20T13:10:08+00:00
The US node seems to be having a bad week. Temporarily you can set downloads.getmonero.org to 151.249.91.243 in your hosts file. This is a Swedish node and is giving me good speed.

## fluffypony | 2017-12-20T13:13:09+00:00
We've moved to faster infrastructure, and using blockchain.raw to sync up is not advisable, so closing this issue.

## mtompkins | 2017-12-21T12:34:02+00:00
Terrible choice to force the peer network to be the only source of initializing the blockchain. In addition, this "faster infrastructure" is still substandard and frankly a hurdle to `monero` uptake by institutional players. We don't have 6 hours to wait for the network, nor care to.

## fluffypony | 2017-12-21T12:49:49+00:00
The p2p network is the only source of consensus, that’s how it works. I’m sorry if “institutional players” lack people with the technical know-how to explain this to them.

PS. This hasn’t prevented “institutional players” from using Bitcoin, they use SPV wallets. They’ll do the same with Monero.

## mtompkins | 2017-12-21T12:53:32+00:00
What a wonderfully specious response. It isn't a question of technical know-how or your personal perception that it's lacking, but a question of aggregation. You still have to process the blocks against p2p - your source is simply made initially efficient. You may want to check with your own sources on "how it works".

As per bitcoin, correct, there are raw repositories available for initiating the blockchain. It gets spun up in minutes instead of hours.

## fluffypony | 2017-12-21T12:56:35+00:00
You have to process the blocks in order to find the chain with the greatest cumulative proof of work difficulty. You have to do this ONCE only.

## mtompkins | 2017-12-21T12:58:21+00:00
It isn't a question of iteration, but a question of time.    

Also, give being an adult a shot; you don't need to put words in caps.    
Reserve that to your family and friends. Discourse ended - you're not worth it.

## fluffypony | 2017-12-21T12:59:09+00:00
Thanks, dad.

## thijstriemstra | 2017-12-21T13:06:29+00:00
if you have ideas for improvements go ahead and create a pull request or stfu @mtompkins 

## danrmiller | 2017-12-21T14:23:15+00:00
@mtompkins wrote:
> Terrible choice to force the peer network to be the only source of initializing the blockchain.

Wow. I strongly disagree with that and am surprised to hear it. Can you give a reason? This is a peer to peer system and the safety assumptions include that your view of blocks and transactions is not controlled. 




## taran2k | 2024-12-20T01:39:29+00:00
Yes I am going to revive a dead thread for this.
I've got 600+ Mbps at home on a good day. I get lucky when I get a few mb/s of download speed. Downloading through a browser for instance is practically impossible, as those will just cut your download off because of the low speed. What's up with this?

# Action History
- Created by: linecolumn | 2017-12-11T16:12:54+00:00
- Closed at: 2017-12-20T13:13:09+00:00
