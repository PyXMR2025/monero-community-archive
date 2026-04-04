---
title: 'Research meeting: 8 January 2020 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/425
author: SarangNoether
assignees: []
labels: []
created_at: '2019-12-30T18:04:07+00:00'
updated_at: '2020-01-08T19:13:13+00:00'
type: issue
status: closed
closed_at: '2020-01-08T19:13:13+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 8 January 2020 @ 18:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-01-08T19:13:13+00:00
    [2020-01-08 13:01:18] <sarang> GREETINGS to everyone
    [2020-01-08 13:01:46] <almutasim> Hi.
    [2020-01-08 13:02:01] <binaryFate> hi hi
    [2020-01-08 13:02:23] — Isthmus waves
    [2020-01-08 13:02:39] <sarang> Let's start with ROUNDTABLE
    [2020-01-08 13:03:02] <sarang> The preprint for Triptych, a new linkable ring signature construction that can be extended for use in transactions, is on the IACR archive
    [2020-01-08 13:03:12] <sarang> Link: https://eprint.iacr.org/2020/018
    [2020-01-08 13:03:20] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Quit: Leaving
    [2020-01-08 13:03:37] <sarang> CoinTelegraph just released an article about it (but note there are some errors in the data presented there, that I'm told will be fixed)
    [2020-01-08 13:04:12] <sarang> I plan to make an update on the size and time data, to properly account for batch verification and ensure fair comparison
    [2020-01-08 13:04:54] <sarang> More work was done on the multi-index version of Triptych, fixing soundness in exchange for a separate proof relation that we need to show is equivalent to another proof relation
    [2020-01-08 13:05:00] <sarang> This would allow even better performance
    [2020-01-08 13:05:23] <sarang> I worked out an MPC for that version of Triptych as well, which would be useful for multisig
    [2020-01-08 13:06:11] <sarang> And I'm presently working on some questions relating to Omniring math that I've brought up with that paper's authors
    [2020-01-08 13:07:08] <sarang> Does anyone else wish to share interesting research work?
    [2020-01-08 13:07:12] <almutasim> When the time is right, at a key juncture, we could have a press release on Triptych. Monero Outreach could support that. Maybe when it is established that it is going into a release.
    [2020-01-08 13:07:38] <sarang> To be clear, there are no guarantees that Triptych, or any presently-known construction, is fit for deployment
    [2020-01-08 13:07:45] <almutasim> Right.
    [2020-01-08 13:07:53] <Isthmus> I've got some fingerprinting stuff, and n3ptune just completed a pretty cool network analysis
    [2020-01-08 13:07:57] <sarang> Ooh
    [2020-01-08 13:08:31] <sarang> Isthmus: what sort of data have you uncovered?
    [2020-01-08 13:09:30] <Isthmus> Ah my fingerprinting notes are nothing new or exciting, just an idea that might make data presentation more intuitive. So, I tend to think about wallet fingerprinting in a kind of abstract way - every transaction sits at some corner of a hypercube in a high-dimensional space made of different heuristics yadda yaddaaa yadda
    [2020-01-08 13:09:44] <Isthmus> So even though I work with sets of boolean features on the backend, wanted a good way to show results
    [2020-01-08 13:09:56] <Isthmus> This is my first attempt: https://mitchellpkt.github.io/fingerprint.html
    [2020-01-08 13:10:03] <sarang> What, you can't accurately present visualizations of high-dimensional hypercubes? =p
    [2020-01-08 13:10:23] <Isthmus> llol
    [2020-01-08 13:10:33] <Isthmus> This is somewhat by @suraeNoether adding human-interpretable output to the graph matching
    [2020-01-08 13:10:39] <sarang> I like the idea of enumeration like that
    [2020-01-08 13:11:52] <Isthmus> thanks! It figure it's also an easy way to pass around data in a 2-column CSV chart, and researchers can do substring matching on portions that they find relevant to a given analysis
    [2020-01-08 13:12:14] <suraeNoether> Ack sorry! I'm here! Time change got me unawares
    [2020-01-08 13:13:11] <sarang> Isthmus: is there anything to share about the network analysis you mentioned?
    [2020-01-08 13:13:40] <n3ptune> Re: questions on block propagation timing asked last month, I've collected and analyzed block receipt timing data from our global nodes recorded during the past 6 months
    [2020-01-08 13:13:57] <sarang> Nice!
    [2020-01-08 13:14:04] <sarang> What conclusions?
    [2020-01-08 13:14:16] <n3ptune> Isthmus has notes about interpretation and I have more to write but you can look at the graphs here https://github.com/noncesense-research-lab/archival_network/wiki/Block-propogation-time
    [2020-01-08 13:14:21] <Isthmus> This was RE a question that @moneromooo asked, right?
    [2020-01-08 13:14:52] <Isthmus> Units are size in bytes and timestamps in milliseconds, right?
    [2020-01-08 13:15:00] <suraeNoether> that was my question ^
    [2020-01-08 13:15:04] <n3ptune> we used this formula where NRT is Node Received Timestamp:  prop_time_lower_bound(h) = MAX[NRT(h,1), NRT(h,2), NRT(h,3)] - MIN[NRT(h,1), NRT(h,2), NRT(h,3)]
    [2020-01-08 13:15:28] <sarang> What are the changing indices there?
    [2020-01-08 13:15:38] <sarang> Different nodes?
    [2020-01-08 13:15:49] <sgp_> hello
    [2020-01-08 13:15:50] <n3ptune> yeah, that goes up to 3 but there are 4 nodes total
    [2020-01-08 13:16:01] <sarang> got it
    [2020-01-08 13:16:03] <suraeNoether> so block prop time is reliably at least 0.1s. interesting.
    [2020-01-08 13:16:23] <Isthmus> Oh scatter heatmap is height from dark=old to light=new
    [2020-01-08 13:17:20] <Isthmus> ^ color scale
    [2020-01-08 13:18:41] <sarang> And those are the differences between the miner-reported timestamp and the node's wall clock upon receipt?
    [2020-01-08 13:19:16] <Isthmus> Miner reported timestamps are not considered anywhere in this study
    [2020-01-08 13:19:22] <Isthmus> But we did that elsewhere
    [2020-01-08 13:19:25] — Isthmus digs around github
    [2020-01-08 13:19:51] <suraeNoether> hm then what is being measured for prop time?
    [2020-01-08 13:19:58] <sarang> So these are blocks only passed between your nodes?
    [2020-01-08 13:20:10] <sarang> Where you look at local times on send and receipt?
    [2020-01-08 13:20:27] <Snipa> ^ Was going to ask that, as the min propogation time seems particularly low, as 100msec is quite low in our experience to cross the globe.
    [2020-01-08 13:20:31] <sarang> Or better question: how is NRT computed
    [2020-01-08 13:20:35] <n3ptune> it's the difference in timing between different nodes receiving the same blocks
    [2020-01-08 13:20:46] <sarang> Ah, ok
    [2020-01-08 13:20:49] <Isthmus> Yea, not passing between our nodes, but passing through our nodes
    [2020-01-08 13:20:50] <n3ptune> NRT is recorded from the node system time when a block arrives
    [2020-01-08 13:20:55] <sarang> Independent of the peer from which they receive
    [2020-01-08 13:21:01] <sarang> (which would differ)
    [2020-01-08 13:21:59] <sarang> Seeing the difference between miner-reported time (which could be inaccurate) and wall-clock receipt time would also be interesting
    [2020-01-08 13:22:08] <suraeNoether> hmmmm
    [2020-01-08 13:22:21] <endogenic> o/
    [2020-01-08 13:22:25] <Isthmus> https://usercontent.irccloud-cdn.com/file/brPsQyeU/image.png
    [2020-01-08 13:22:27] <Isthmus> @sarang just for you
    [2020-01-08 13:22:42] <sarang> So what we're really seeing here is not propagation time directly, but variability in one layer of propagation time
    [2020-01-08 13:22:50] <sarang> here = the initial plots, not this one
    [2020-01-08 13:23:08] <Snipa> I'll have to check pool log data, as I might be able to give some extra data points if you're interested.  We started to log the time in which a pool node finds a block, versus when that block is stored into our database, which means it's been processed by the local node, as we skip all monerod timings on the pool itself.
    [2020-01-08 13:23:19] <suraeNoether> oooop
    [2020-01-08 13:23:21] <suraeNoether> that's cool
    [2020-01-08 13:23:32] <sarang> Very high times
    [2020-01-08 13:23:36] <Isthmus> @Snipa very nice!
    [2020-01-08 13:23:47] <Isthmus> "So what we're really seeing here is not propagation time directly, but variability in one layer of propagation time" < can you elaborate?
    [2020-01-08 13:24:19] <suraeNoether> isthmus well it's how long it takes for the block to propagate from one of your nodes to another of your nodes; not time it takes to propagate from a miner to one of your nodes
    [2020-01-08 13:24:25] <sarang> I mean that for the initial plots you showed, you can't directly interpret the time for the block to reach your node after it's mined
    [2020-01-08 13:24:32] <sarang> suraeNoether: no
    [2020-01-08 13:24:41] <suraeNoether> no?
    [2020-01-08 13:24:45] <Isthmus> Yea, we very deliberately labeled all of the axes "prop time lower bound" for that reason
    [2020-01-08 13:25:05] <Isthmus> Also, we could always posit that there is an old PC on dialup somewhere in Nebraska with a 4 minute prop time, but that's not meaningful
    [2020-01-08 13:25:10] <sarang> suraeNoether: it's looking at the difference in receipt time, whichever path the block took in total propagation
    [2020-01-08 13:25:28] <Snipa> Hrm, auctually, I can provide a data stream of our global block propgations, as every node has a local reporter that we can hook.
    [2020-01-08 13:25:45] <Isthmus> @Snipa yes please!
    [2020-01-08 13:25:49] <suraeNoether> sarang that's true also
    [2020-01-08 13:25:54] <n3ptune> that data would be awesome to work with
    [2020-01-08 13:25:57] <Isthmus> I'll posit something that might be wrong:
    [2020-01-08 13:26:06] <Isthmus> It's a hacky data science way of thinking -
    [2020-01-08 13:26:17] <Snipa> Hit me up a bit later and we can discuss how to get it to you, and go over data formats.
    [2020-01-08 13:26:39] <Isthmus> Shoot, I gotta get off the bus
    [2020-01-08 13:26:43] <suraeNoether> isthmus: you have two sensors set up to detect propagation time. but you need 3 to triangulate, ala seismic detection of epicenters
    [2020-01-08 13:26:45] — Isthmus sticks a pin in it, and will be back in 3 - 6 min
    [2020-01-08 13:26:52] <sarang> Don't leave us with that cliffhanger Isthmus!
    [2020-01-08 13:26:58] <suraeNoether> i'm on the edge of my seat
    [2020-01-08 13:27:01] <suraeNoether> i spilled my tea
    [2020-01-08 13:27:13] <suraeNoether> i'm so upset at isthmus right now i could just light myself on fire
    [2020-01-08 13:27:31] <sarang> Stay on the bus Isthmus... it'll loop back around to your stop eventually
    [2020-01-08 13:27:52] <sarang> In the meantime, any other interesting tidbits on this work?
    [2020-01-08 13:27:56] <sarang> This is very interesting data
    [2020-01-08 13:28:16] <suraeNoether> while we are waiting on Isthmus, I'll give my super-brief update: after some discussions with endo, my matching code has been made significantly more efficient, easy to understand, and easier to debug; i'll be making a push later today. my two categories of work today are re-reviewing CLSAG and working on matching
    [2020-01-08 13:28:39] <n3ptune> that's it for now, we will update
    [2020-01-08 13:28:45] <endogenic> his pseudocode now fits onto one sheet of notepad paper..
    [2020-01-08 13:28:55] <suraeNoether> isthmus and i also technically had a conversation about writing up a proposal to encrypt and enforce all lock times, but we haven't gotten details worked out yet
    [2020-01-08 13:29:32] <sarang> You mean using DLSAG-style commitments?
    [2020-01-08 13:29:40] <sarang> We'd discussed it earlier in a meeting
    [2020-01-08 13:29:54] <suraeNoether> yep, last meeting iirc. but i actually had a call with isthmus about it. i view this move as a very good boost in privacy in the sense that it covers up a source of non-randomness in the large data sets that isthmus likes to comb through.
    [2020-01-08 13:30:11] <sarang> I can work out the size and time implications on that if you like
    [2020-01-08 13:30:19] <suraeNoether> i'm not convinced it is worth the additional cost to our txn sizes, but we'll see how it shakes out
    [2020-01-08 13:30:24] <sarang> Since it could be bundled into the existing bulletproof
    [2020-01-08 13:30:26] <suraeNoether> ^ ah
    [2020-01-08 13:30:37] <sarang> Yeah, size is not the issue here due to the logarithmic scaling
    [2020-01-08 13:30:55] <suraeNoether> yeah, and verification times are speedy as a cheetah's balls
    [2020-01-08 13:31:16] <suraeNoether> pardon me, this is a public meeting, i should be less vulgar. please accept my apologies.
    [2020-01-08 13:31:17] <sarang> Right... there's a linear increase in verification time, but with the benefits of multiexp that's reduced a bit
    [2020-01-08 13:31:27] <sarang> CoinTelegraph has updated their article: https://cointelegraph.com/news/moneros-triptych-research-could-vastly-improve-its-anonymity
    [2020-01-08 13:31:44] <sarang> Thanks to the author for taking care of that so quickly
    [2020-01-08 13:33:23] <almutasim> A press release could get more coverage, when and if it is desired.
    [2020-01-08 13:33:32] <sarang> suraeNoether: interestingly, due to bulletproof padding, for many transactions there would be no size increase aside from the space taken up by the commitment data
    [2020-01-08 13:33:34] <suraeNoether> good on cointelegraph
    [2020-01-08 13:33:40] <sarang> (as opposed to a smaller plaintext representation)
    [2020-01-08 13:34:00] <suraeNoether> sarang: could a similar approach be used to include a ciphertext of a message?
    [2020-01-08 13:34:35] <suraeNoether> ie moneroMail
    [2020-01-08 13:34:43] <Isthmus> Sorry somebody got in a fight with the bus driver right before my stop
    [2020-01-08 13:34:47] <sarang> Not really... there's some spare space in bulletproofs that could hold something 1-2 proof elements of arbitrary data by controlling randomness (I'd need to check the details)
    [2020-01-08 13:34:48] <Isthmus> Sigh San Francisco
    [2020-01-08 13:35:02] <sarang> Welcome back Isthmus
    [2020-01-08 13:35:02] <Isthmus> Ok lemme whiteboard some stuff 1 sex
    [2020-01-08 13:35:14] <Isthmus> n3ptune: do you want to share the padding?
    [2020-01-08 13:35:19] <Isthmus> In the blocks
    [2020-01-08 13:35:52] <n3ptune> sure
    [2020-01-08 13:35:54] <suraeNoether> sarang so enough for a key exchange but unlikely enough for a ciphertext?
    [2020-01-08 13:36:19] <sarang> Well, you're limited by space
    [2020-01-08 13:36:37] <n3ptune> Is there a known purpose for the null padding tag in tx_extra?
    [2020-01-08 13:36:45] <sarang> I don't remember if Poelstra and friends found 32 or 64 bytes of space
    [2020-01-08 13:36:58] <sarang> n3ptune: good question for moneromooo et al.
    [2020-01-08 13:39:37] <sarang> While we await Isthmus' continued update, anything else of interest to share?
    [2020-01-08 13:39:48] <sarang> Or ACTION ITEMS, according to the agenda?
    [2020-01-08 13:40:36] <suraeNoether> i want to provide final comments to you on clsag but i'm very unlikely to get that finished today
    [2020-01-08 13:40:42] <suraeNoether> but it's on my mind for this week
    [2020-01-08 13:40:51] <Isthmus> Back
    [2020-01-08 13:40:58] <suraeNoether> Front
    [2020-01-08 13:41:16] <sarang> Mine are to get CLSAG submitted (after review), to hopefully nail down this Omniring issue and pass it to the authors, work on a few EC curve library updates for proof of concept code, and get preprint stuff taken care of via monero-site MR
    [2020-01-08 13:41:26] <sarang> Isthmus: please go ahead
    [2020-01-08 13:42:36] <sarang> (oh, and update the Triptych preprint performance data with better clarity)
    [2020-01-08 13:42:37] <Isthmus> https://usercontent.irccloud-cdn.com/file/gAM3VbDV/1578508953.JPG
    [2020-01-08 13:42:59] <sarang> wat dis
    [2020-01-08 13:44:43] <Isthmus> So let's say that we have 100 of n3ptune/NRL's archival nodes running
    [2020-01-08 13:46:30] <Isthmus> If we have only 2 nodes, then our propagation envelope will have a lot of variability, be topology dependent (assume archival nodes don't connect to each other), and just t_second - t_first
    [2020-01-08 13:46:56] <Isthmus> As we add a 3rd node, it has the possibility of increasing the measured prop time (since it could hear before or after) but can't decrease the prop time since it's max-min
    [2020-01-08 13:48:27] <Isthmus> As we get up to 100 nodes, the variability will probably smooth out and we approach the true reasonable prop time (from miner to global nodes with broadband internet)
    [2020-01-08 13:48:32] <sarang> Doesn't prop time depend on max/min among all nodes? So the third node could fall outside the envelope of the other two and affect the value?
    [2020-01-08 13:48:41] <Isthmus> Yeah, that's the point
    [2020-01-08 13:49:05] <sarang> OK, I must have misinterpreted
    [2020-01-08 13:49:22] <sarang> Oh, can't _decrease_
    [2020-01-08 13:49:24] <sarang> nvm
    [2020-01-08 13:49:24] <Isthmus> Painting very broadly, when we adad the 3rd node there's a 2/3 chance that it'll fall outside the N=2 and increase the prop time, and a 1/3 chance that it'll be between the first 2 nodes.
    [2020-01-08 13:49:51] <Isthmus> Sorry, I'm giving a kind of scattered description cuz I just realized this on the bus
    [2020-01-08 13:50:14] <almutasim> Max-Min is a very sensitive metric, sensitive to outliers.
    [2020-01-08 13:51:27] <Isthmus> Hmm lemme ponder on that
    [2020-01-08 13:51:37] <Isthmus> Skipping over that for now
    [2020-01-08 13:51:54] <Snipa> How're you pulling the time in which the block is received?  Tweaked monerod/using it's logs or polling on the RPC interface to determine when it's auctually viably added to the box?
    [2020-01-08 13:52:29] <Isthmus> That's a n3ptune question, they do all the DevOps and data engineering. All ended up in a SQL database by the time I got to it
    [2020-01-08 13:52:39] <n3ptune> tweaked monerod
    [2020-01-08 13:52:50] <Snipa> On P2P receive then?
    [2020-01-08 13:53:06] → nssy2 joined (~nssy@197.237.91.81)
    [2020-01-08 13:53:20] <Isthmus> So for each height we have epsilon (green line) which our many-node approximation of global prop time
    [2020-01-08 13:53:27] <n3ptune> you can also use monerod --block-notify, if you point that to a shell script that writes the timestamp
    [2020-01-08 13:54:11] <Snipa> --block-notify waits until the block is committed, which is why I ask, because nodes that do not use NVMe have much slower propagation times in general, as you're waiting on disks to write.
    [2020-01-08 13:54:15] <n3ptune> i like that better because then you can use the stock daemon. but we don't use that yet
    [2020-01-08 13:54:19] <sarang> OK, so using the max-min metric, assuming relatively even node placement across the network topology?
    [2020-01-08 13:54:44] <Isthmus> Yeah, though after @almutasim I'm considering a few other less sensitive metrics
    [2020-01-08 13:54:52] <Isthmus> slap all those epsilons into a histogram, and that's the plot on the right.
    [2020-01-08 13:54:59] <sarang> The outliers being nodes close to the miner and far from it, topologically
    [2020-01-08 13:55:16] <Isthmus> Uhm, the outlier might be only 2 hops away but one of the hops is really slow
    [2020-01-08 13:55:21] <n3ptune> P2P Receive:  no it happens when it adds it to the blockchain, after it determines whether or not it's an alt block.  this was because we had another original goal to capture alt blocks data.  the daemon patch is shared here https://github.com/neptuneresearch/monerod-archive
    [2020-01-08 13:55:58] <Isthmus> @sarang so it depends if topological distance definition is just the p2p connectivity graph or takes into account time between vertices
    [2020-01-08 13:56:32] <sarang> right
    [2020-01-08 13:57:22] <Isthmus> And that epsilon plot is basically what n3ptune shared earlier except instead of "max-min with 4 nodes" it is "asymptotic approximation of global prop time"
    [2020-01-08 13:57:34] <Isthmus> ^talking about x-axis of histogram
    [2020-01-08 13:57:47] <n3ptune> --block-notify waits until the block is committed >>   oh then i guess this method of doing it in blockchain::add_new_block() at least occurs before block-notify would.  but yes it isn't *immediately* on receive
    [2020-01-08 13:59:37] <sarang> Since we're just about out of time, any last bits of information before adjourning (discussion can of course continue) for log purposes?
    [2020-01-08 13:59:58] <Isthmus> Oh yea
    [2020-01-08 14:00:20] <Isthmus> just a quick note that tx_padding is used in the wild, but unclear why
    [2020-01-08 14:00:42] <Isthmus> In the scatter plot showed earlier, the vertical bands from left to right are empty blocks and then N=1,2,3... transaactions
    [2020-01-08 14:00:56] <sarang> That's a question for someone like moneromooo
    [2020-01-08 14:01:12] <Isthmus> Of course there's variability in the horizontal width of the vertical bands due to transaction size differences, but the variability in coinbase-only blocks was straange
    [2020-01-08 14:01:13] <Isthmus> https://xmrchain.net/tx/acdf8eac41a7a76fd899e09640db34023abff66b3ae2c9ea86e49f19c0720af4
    [2020-01-08 14:01:30] <Snipa> Not really, coinbase only blocks are quite common due to pool design.
    [2020-01-08 14:01:45] <Isthmus> No no, the size*variability* in coinbase-only was strange
    [2020-01-08 14:01:52] <Isthmus> Turns out some (now fingerprinted) miners are using lots of null padding, check out the tx_extra for this coinbase
    [2020-01-08 14:01:59] <sarang> gadzooks
    [2020-01-08 14:02:13] <Snipa> Not super surprising.
    [2020-01-08 14:02:28] <Isthmus> Looks like bloat to me
    [2020-01-08 14:02:36] <Isthmus> Bunch of blocks waste space with nulls in tx_extra
    [2020-01-08 14:02:41] <Snipa> Possibly, it's also something that can be requested by a pool.
    [2020-01-08 14:02:51] <Snipa> As that's the block padding that we use for extra nonce storage space.
    [2020-01-08 14:03:23] <Isthmus> "As that's the block padding that we use for extra nonce storage space." block nonce or transaction nonce? This is padding in the coinbase transaction
    [2020-01-08 14:03:35] <Snipa> Oh sorry, txn, my bad.
    [2020-01-08 14:04:17] <Isthmus> Do you know why some miners use the padding and some don't?
    [2020-01-08 14:04:31] — Isthmus is very naive about practical mining stuff
    [2020-01-08 14:04:45] <Snipa> Lemme look through some of my decoding code I wrote for that.
    [2020-01-08 14:05:15] ⇐ rex4539 quit (~rex4539@balticom-197-78.balticom.lv): 
    [2020-01-08 14:05:19] ⇐ sech1 quit (~sech1@31-208-119-248.cust.bredband2.com): Read error: Connection reset by peer
    [2020-01-08 14:05:21] <Isthmus> I'd been comparing:
    [2020-01-08 14:05:24] <Isthmus> https://xmrchain.net/search?value=1988283
    [2020-01-08 14:05:25] <Isthmus> and
    [2020-01-08 14:05:30] <Isthmus> https://xmrchain.net/search?value=1985042
    [2020-01-08 14:05:39] <Isthmus> Since they seem to be exactly the same besides different padding
    [2020-01-08 14:05:45] — Isthmus wraps up that train of thought
    [2020-01-08 14:06:48] <Isthmus> Anyways, thanks for letting me ramble and shifting meeting time
    [2020-01-08 14:07:22] <Snipa> For quick reference: The block's CB TXN contains an "extras" section, which is requested from Monerod as the extra space in which arbitary data can be written.  This data is used by pool implementations to implement the per-pool nonces as well as any custom nonce data used by more advanced techniques.
    [2020-01-08 14:07:46] → sech1 joined (~sech1@31-208-119-248.cust.bredband2.com)
    [2020-01-08 14:08:16] <Isthmus> "extra space in which arbitrary data can be written"
    [2020-01-08 14:08:17] — Isthmus cringes
    [2020-01-08 14:08:44] <Snipa> You can use this data in a number of ways, particularly with knowledge of pool design, as the two main pool implementations use this space similarly, but have different sizes based on various addon support.
    [2020-01-08 14:09:00] <Isthmus> Ooh, what are the current use cases?
    [2020-01-08 14:09:16] <Snipa> You also can identify what pool instances are submitting blocks, as pools use unique identifiers in particular bytes.
    [2020-01-08 14:09:17] <Isthmus> (I have no knowledge of pool design)
    [2020-01-08 14:09:39] <Snipa> https://github.com/Snipa22/nodejs-pool/blob/master/lib/coins/xmr.js#L115
    [2020-01-08 14:09:43] <suraeNoether> For those of you who are interested in helping out with Monero Kon 2020 in Berlin, there is a meeting happening right now for prospective volunteers. This is research related, but otherwise off-topic, so I'm just dropping this here.
    [2020-01-08 14:10:08] <Snipa> ^ is the implementation you'll find on pools that support the XNP extensions I wrote awhile ago.
    [2020-01-08 14:10:24] <sarang> Yeah, we can formally adjourn the meeting, but carry on the conversation
    [2020-01-08 14:10:27] <sarang> Thanks to everyone for attending


# Action History
- Created by: SarangNoether | 2019-12-30T18:04:07+00:00
- Closed at: 2020-01-08T19:13:13+00:00
