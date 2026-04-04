---
title: 'Research meeting: 23 September 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/510
author: SarangNoether
assignees: []
labels: []
created_at: '2020-09-21T00:25:58+00:00'
updated_at: '2020-09-24T12:33:56+00:00'
type: issue
status: closed
closed_at: '2020-09-24T12:33:56+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 23 September 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-09-24T12:33:56+00:00
    [2020-09-23 13:01:23] <sarang> OK, let's get started with our research meeting
    [2020-09-23 13:01:26] ⇐ intj440 quit (intj440@gateway/vpn/protonvpn/intj440): Read error: Connection reset by peer
    [2020-09-23 13:01:27] <sarang> First, greetings!
    [2020-09-23 13:01:29] <sarang> Hi
    [2020-09-23 13:01:31] <midipoet> Seriously though if anyone is interested in looking at the call, let me know.
    [2020-09-23 13:01:36] <n3ptune> Hello
    [2020-09-23 13:01:40] — Isthmus waves
    [2020-09-23 13:01:54] → intj440 joined (intj440@gateway/vpn/protonvpn/intj440)
    [2020-09-23 13:02:16] <midipoet> Horizon Europe wants consortiums built with emphasis on extra-european knowledge/partnerships. Usual budget for these things is 4-12 million.
    [2020-09-23 13:02:30] <TheCharlatan> hi
    [2020-09-23 13:02:45] — midipoet shuts up as meeting
    [2020-09-23 13:03:06] <ArticMine> hi
    [2020-09-23 13:03:45] <sarang> A brief reminder that next week's meeting will be the last that I will be leading; if anyone else wishes to take over meetings at that point, feel free to do so
    [2020-09-23 13:03:48] <sarang> Let's move to roundtable
    [2020-09-23 13:03:56] <sarang> Where anyone can share research of interest with the group
    [2020-09-23 13:04:00] <sarang> Does anyone wish to share anything?
    [2020-09-23 13:04:08] <n3ptune> I'd like to share two big SQL projects that I've just finished
    [2020-09-23 13:04:24] <n3ptune> The first is a tx_extra parser for PostgreSQL: http://github.com/neptuneresearch/tx-extra-parse
    [2020-09-23 13:04:33] <n3ptune> The point is to parse a transaction's tx_extra data (which is all packed together into one byte string) into separate database records for each sub-field tag and data, so it can be further queried on.
    [2020-09-23 13:04:40] <n3ptune> Here are some queries we ran about tag usage and statistics, and their results: http://github.com/neptuneresearch/monero-tx-extra-statistics-report
    [2020-09-23 13:05:05] <n3ptune> We presented some of this before in a Feb 2020 MRL meeting, and some various MRL github issues. There were some questions from then that are answered in here, sorry that took me so long!
    [2020-09-23 13:05:23] <n3ptune> The biggest result to me is that there are no unknown tx_extra tags being used: no one is storing any other kind of data in Monero transactions, besides the known kinds.
    [2020-09-23 13:05:59] <sarang> Huh, interesting
    [2020-09-23 13:06:34] <sarang> Do you take this to mean that a deprecation of `tx_extra` in favor of enforcing standard fields like encrypted pID would be unlikely to break existing unknown use cases?
    [2020-09-23 13:06:59] <n3ptune> Yes, regarding current usage
    [2020-09-23 13:07:17] <n3ptune> It would still break future possibilities
    [2020-09-23 13:07:25] <sarang> Sure, but that's a different problem
    [2020-09-23 13:07:45] <Isthmus> The answer to UkoeHB_ 's question is very interesting
    [2020-09-23 13:08:04] <Isthmus> Also, the single transaction that contains 1000 payment IDs, lol
    [2020-09-23 13:08:19] <Isthmus> Los of interesting stuff to unpack here
    [2020-09-23 13:08:24] <Isthmus> s/os/ots
    [2020-09-23 13:08:25] <monerobux> Isthmus meant to say: Lots of interesting stuff to unpack here
    [2020-09-23 13:08:28] <n3ptune> There are also multiple ways to write the same data, and a transaction's choice there is a fingerprint
    [2020-09-23 13:08:37] <sarang> Yep, that's certainly come up before
    [2020-09-23 13:08:41] <n3ptune> For instance, do you write "public key" and then "encrypted payment id",  or "encrypted payment id" and then "public key"
    [2020-09-23 13:08:52] <sarang> Right
    [2020-09-23 13:08:57] <n3ptune> or do you even do something unique like you add "additional public keys, 0" to every transaction
    [2020-09-23 13:09:18] <sarang> The "best" option (for some definition of "best") is to enforce a standard ordering and set of data
    [2020-09-23 13:09:27] <sarang> thereby removing the option for fingerprinting
    [2020-09-23 13:09:33] <sarang> or at least making it more difficult :)
    [2020-09-23 13:10:16] <n3ptune> Oh and also, full deprecation would stop unencrypted PID usage.
    [2020-09-23 13:10:40] <sarang> Yep
    [2020-09-23 13:10:43] <Isthmus> Yep, upvote for TLV ordering
    [2020-09-23 13:11:02] <sarang> It's nice to have some data backing this up
    [2020-09-23 13:12:33] <sarang> Anything else you'd like to share on this, n3ptune?
    [2020-09-23 13:12:36] <sarang> Or Isthmus?
    [2020-09-23 13:12:46] <n3ptune> Not on tx_extra
    [2020-09-23 13:12:49] <n3ptune> any questions welcome
    [2020-09-23 13:12:49] <n3ptune> The other SQL project I'd like to share is: http://github.com/neptuneresearch/ring-membership-sql
    [2020-09-23 13:12:55] <n3ptune> This provides a way from within PostgreSQL to build the transaction output index, and to decode a transaction's key_offsets, which together let you list a transaction's ring members.
    [2020-09-23 13:13:01] <n3ptune> This is a building block for writing more complicated queries regarding ring members, like decoy selection analysis.
    [2020-09-23 13:13:24] <sarang> Cool, so similar to what the block explorer interface does?
    [2020-09-23 13:13:32] <n3ptune> Exactly
    [2020-09-23 13:13:35] <sarang> neat
    [2020-09-23 13:14:30] <sarang> Anything interesting pop up so far when looking at that?
    [2020-09-23 13:14:39] <sarang> Or is it still a bit early for that analysis
    [2020-09-23 13:14:59] <n3ptune> This is pretty fresh yeah, we don't have any use cases yet
    [2020-09-23 13:15:18] <Isthmus> Haha we have a ton of use cases, they just haven't been coded up yet :- p
    [2020-09-23 13:15:29] <Isthmus> This will be a fun one to mess around with
    [2020-09-23 13:15:45] <sarang> Oh totally
    [2020-09-23 13:15:53] <sarang> Since decoy selection is totally up to the client
    [2020-09-23 13:15:53] <Isthmus> Especially once I add on the layer for tracking chainlets with fungibility defects
    [2020-09-23 13:17:23] <sarang> This is great!
    [2020-09-23 13:17:41] <sarang> Any questions for n3ptune and/or Isthmus?
    [2020-09-23 13:18:47] <sarang> All righty
    [2020-09-23 13:18:50] <sarang> I have a few things to share
    [2020-09-23 13:19:09] <sarang> I presented Triptych to an ESORICS workshop, which went well
    [2020-09-23 13:19:25] <sarang> I'm giving a talk on privacy at MCCVR this weekend, and participating in a panel on Bitcoin privacy
    [2020-09-23 13:20:05] <dEBRUYNE> To be clear, the talk will be separate? Because I only saw an announcement regarding the panel
    [2020-09-23 13:20:12] <sarang> I made some updates to Arcturus for a tiny efficiency bump that simplifies things a bit, as well as updated its Python proof-of-concept code to better indicate how to do efficient verification
    [2020-09-23 13:20:19] <sarang> Yes, the talk is separate and occurs just before the panel
    [2020-09-23 13:20:33] <sarang> They separately asked me to give the talk after I agreed to do the panel
    [2020-09-23 13:20:51] <sarang> I'm also updating some transaction statistics for general use
    [2020-09-23 13:21:00] <sarang> An intriguing idea came from cargodog[m] recently
    [2020-09-23 13:21:16] <cargodog[m]> Where will those be shared? I have been looking for TX stats :D
    [2020-09-23 13:21:17] <sarang> They worked up a Rust implementation of Arcturus: https://github.com/cargodog/arcturus/
    [2020-09-23 13:21:23] <cargodog[m]> :wave:
    [2020-09-23 13:21:25] <dEBRUYNE> Thanks for clarifying
    [2020-09-23 13:21:30] <sarang> cargodog[m]: I'll make them available after my scripts finish up
    [2020-09-23 13:21:47] <sarang> The scripts are in the `tracing` branch of my `skunkworks` repo
    [2020-09-23 13:22:06] <cargodog[m]> Great, thanks!
    [2020-09-23 13:22:07] <sarang> cargodog[m] had an idea to use generalized Gray codes to speed up Triptych/Arcturus/etc. operations that's intriguing
    [2020-09-23 13:22:43] <sarang> I've been doing more digging to determine the extent of such efficiency gains, the conditions under which they apply significantly, as well as to what extent they're affected by underlying crypto plumbing
    [2020-09-23 13:22:56] <sarang> cargodog[m]: you're welcome to share this work yourself, if you like!
    [2020-09-23 13:23:20] <sarang> I didn't know if you were around for this meeting
    [2020-09-23 13:23:33] <cargodog[m]> Thanks sarang: I am currently writing up a paper to formally describe the improved technique
    [2020-09-23 13:23:50] <cargodog[m]> Sorry, I was running a few minutes late :)
    [2020-09-23 13:24:26] <sarang> One thing I noticed about your one-of-many binary Gray implementation was that it performed the Gray decomposition separately from determining which coefficients to update
    [2020-09-23 13:24:30] <cargodog[m]> My goal is to have a paper (short but sweet), that can clearly explain the concept, not just as it applies to Arcturus, but Triptych, Lelantus, One-out-of-Many, etc
    [2020-09-23 13:24:49] <sarang> I am also working on the generalized version and have the Gray code stuff operating, but I want to directly integrate the coefficient changes, to avoid redundancy
    [2020-09-23 13:25:31] <cargodog[m]> Indeed. My OOM implementation is fairly specific. Most of my work right now is generalizing this stuff to make it more broadly applicable
    [2020-09-23 13:25:37] <sarang> Fortunately you can iteratively compute the `n`-Gray codes too, meaning there's a lot of room for improving how your binary method works
    [2020-09-23 13:26:26] <sarang> I implemented the iterative method from a paper; I can link some example code after the meeting
    [2020-09-23 13:26:42] <cargodog[m]> That would be great
    [2020-09-23 13:26:45] <sarang> What remains is simply to do the coefficient updating from it, which is not too complicated
    [2020-09-23 13:27:18] <sarang> I don't think there are necessarily _huge_ gains to be made doing it this way, as opposed to a non-iterated method, but this way is certainly faster
    [2020-09-23 13:27:31] <sarang> Since you're not computing all the codes from scratch
    [2020-09-23 13:28:07] <sarang> I also had commented that I had questioned your approach because of the reliance on expensive inversions, but I had totally neglected the effects of batch inversion, which both our code and yours support
    [2020-09-23 13:28:08] <cargodog[m]> Still, every gain is important
    [2020-09-23 13:28:13] <cargodog[m]> Ultimately, I hope to attract more eyes to Arcturus, and build confidence on its hardness assumption
    [2020-09-23 13:28:26] <sarang> Meaning you only have to do a single inversion, and then a nontrivial number of accumulator multiplications
    [2020-09-23 13:28:36] <sarang> I'm super excited that you implemented this cargodog[m]
    [2020-09-23 13:28:38] <sarang> :D
    [2020-09-23 13:28:47] ⇐ rot quit (~rottensox@unaffiliated/rottensox): Remote host closed the connection
    [2020-09-23 13:29:05] <cargodog[m]> Hopefully I can deliver something useful :D
    [2020-09-23 13:29:06] → rot joined (~rottensox@unaffiliated/rottensox)
    [2020-09-23 13:29:07] <sarang> FWIW each scalar inversion is equivalent to ~200 multiplications
    [2020-09-23 13:29:13] <cargodog[m]> The paper has been a breeze to work with
    [2020-09-23 13:29:25] <sarang> and the batch inversion of `k` scalars is one 200-mult inversion and another `3k` multiplications
    [2020-09-23 13:29:29] <sarang> Thanks!
    [2020-09-23 13:29:30] <cargodog[m]> ^ Ah, I was looking for that number yesterday. Thansk!
    [2020-09-23 13:29:33] <sarang> I'm glad the paper was clear
    [2020-09-23 13:30:04] <sarang> So anyway, the use of the Gray method will incur that batch inversion cost
    [2020-09-23 13:30:22] <sarang> and hence I assume there's some tradeoff that's eventually dominated by the gains from the Gray method at higher anon set sizes
    [2020-09-23 13:30:40] <sarang> You had also pointed out that in the batch verification case where anon sets are common, the gains improve even more
    [2020-09-23 13:30:43] <cargodog[m]> more important than anon set size is batch size
    [2020-09-23 13:30:47] <cargodog[m]> but yes
    [2020-09-23 13:30:47] <sarang> Of course, the effectiveness there depends on how you batch
    [2020-09-23 13:31:08] <sarang> For something like Lelantus, they reuse a huge anon set, but have to worry about things like windowing and filling up that set
    [2020-09-23 13:31:24] → nssy joined (~nssy@197.237.91.81)
    [2020-09-23 13:31:30] <sarang> For an approach more similar to ours, where we care a lot about selection age, you'd have fewer common elements in the batch
    [2020-09-23 13:31:49] <cargodog[m]> Yeah, I am skeptical how they intend to receive many common TXs to batch
    [2020-09-23 13:31:53] <cargodog[m]> but the idea is similar
    [2020-09-23 13:32:13] <sarang> Sure, but I think it means that the Gray gains are very dependent on how you select anon sets, and therefore how you batch
    [2020-09-23 13:32:33] <cargodog[m]> Yes indeed
    [2020-09-23 13:32:38] <sarang> At any rate, provided you clear the inversion computational hurdle, you'd start to see benefits
    [2020-09-23 13:32:56] <cargodog[m]> Im interested to explore ring selection techniques to maximize batching
    [2020-09-23 13:33:11] <sarang> Yeah, it's very nontrivial
    [2020-09-23 13:33:13] <cargodog[m]> An obvious approach is to increase ring size :)
    [2020-09-23 13:33:24] <sarang> Sure, but you can't ignore selection age, which is a big heuristic
    [2020-09-23 13:33:30] <sarang> and that changes dynamically
    [2020-09-23 13:33:42] <cargodog[m]> indeed. It is a very complex problem
    [2020-09-23 13:33:58] <sarang> In theory, the Lelantus-style "everyone uses a big anon set" is great for computation
    [2020-09-23 13:34:03] <cargodog[m]> Unfortunately I need to sign off earlier than expected. I will check in later, and welcome any questions or suggestions to either of my projects :)
    [2020-09-23 13:34:10] <sarang> but I fear in practice it's burdensome and could lead to age heuristics
    [2020-09-23 13:34:20] <sarang> No problem! Thanks for joining in today
    [2020-09-23 13:34:33] <cargodog[m]> I hope to be present longer in the future!
    [2020-09-23 13:34:42] <sarang> Hop in the channel any time
    [2020-09-23 13:35:15] <sarang> I'll link the inversion complexity stuff for you, as well as the `n`-Gray example code, after the meeting
    [2020-09-23 13:35:22] <sarang> Logs are available in the channel topic
    [2020-09-23 13:35:34] <sarang> Just search for mentions etc.
    [2020-09-23 13:35:40] <sarang> or perhaps your client will show mentions too, whatever
    [2020-09-23 13:35:46] <sarang> I'll get the links :)
    [2020-09-23 13:36:18] <sarang> OK, any questions on the topics I mentioned?
    [2020-09-23 13:37:50] <sarang> If not, does anyone else wish to share research topics?
    [2020-09-23 13:38:16] <Isthmus> I found a figure that is a concrete example of n3ptune's framework in action
    [2020-09-23 13:38:23] <sarang> Go on!
    [2020-09-23 13:39:03] <Isthmus> So I picked a random fungibility defect (in this case a particular extra tag) and showed how it's used to link transactions via the chain address
    [2020-09-23 13:39:04] <Isthmus> https://usercontent.irccloud-cdn.com/file/1F4ccO3H/image.png
    [2020-09-23 13:39:20] <Isthmus> So the wallet received 3 fresh external outputs, and made 16 transactions
    [2020-09-23 13:39:39] <Isthmus> But each time, the new transaction consumed a change output with the exact same defect
    [2020-09-23 13:40:13] <sarang> yikes
    [2020-09-23 13:40:16] <Isthmus> So doxxing all of the transactions was trivial
    [2020-09-23 13:40:39] <UkoeHB_> is the tag a payment ID or something?
    [2020-09-23 13:41:04] <Isthmus> Now the cool thing is that I can automate n3ptune's framework to both 1) automatically sift through data to identify the fungibility defects, and 2) automatically identify every transaction (/chain) from that wallet
    [2020-09-23 13:41:24] <Isthmus> So we can map out the transaction tree through change addresses for ANY wallet with ANY fungibility defect
    [2020-09-23 13:41:29] <Isthmus> It's a whole new montser
    [2020-09-23 13:42:27] <UkoeHB_> really impressive work guys
    [2020-09-23 13:42:32] <dEBRUYNE> +1
    [2020-09-23 13:42:34] <n3ptune> Thanks :)
    [2020-09-23 13:42:43] <Isthmus> I think it was the `n_extra_nonce` tag?
    [2020-09-23 13:42:46] <dEBRUYNE> I guess standardizing the tx_extra format would help in this regard
    [2020-09-23 13:42:49] <sarang> yep
    [2020-09-23 13:43:34] <Isthmus> Standardizing tx_extra would entirely shut down this kind of analysis, if the protocol only allowed keys and an encrypted PID
    [2020-09-23 13:44:07] <sarang> Well, in theory
    [2020-09-23 13:44:19] <sarang> You can't actually enforce the encrypted pID properly at the consensus level
    [2020-09-23 13:44:36] <Isthmus> Well, true, the fungibility defects could also be things like unlock time, unusual fees, etc.
    [2020-09-23 13:44:48] <sarang> You could use authenticated encryption to avoid the recipient accepting such a txn if you wanted to...
    [2020-09-23 13:44:58] <sarang> No, I mean you can set "the pID" to be anything you want
    [2020-09-23 13:45:00] <sarang> all zeros
    [2020-09-23 13:45:03] <moneromooo> Is that extra valid as per the wallet parsing rules ?
    [2020-09-23 13:45:04] <sarang> your phone number
    [2020-09-23 13:45:06] <sarang> whatever
    [2020-09-23 13:45:20] <n3ptune> I think that was a valid tag
    [2020-09-23 13:45:23] <moneromooo> There was a claim before of non non standard fields used, so I'm guessing it's vlaid.
    [2020-09-23 13:45:37] <moneromooo> So it's vlaid but out of order compared to what monerod outputs ?
    [2020-09-23 13:45:50] <n3ptune> I think it was an extra nonce, in a user transaction
    [2020-09-23 13:46:03] <n3ptune> Which Monero Core wouldn't ever write?
    [2020-09-23 13:46:23] <moneromooo> a 32 byte one ?
    [2020-09-23 13:46:31] <moneromooo> It would not anymore.
    [2020-09-23 13:47:04] <n3ptune> As in, not any kind of payment id. Neither 020901 or 022100.  Just an 02 with a valid size
    [2020-09-23 13:47:15] <moneromooo> Oh. OK.
    [2020-09-23 13:47:44] <moneromooo> So our monero code would not write that by itself.
    [2020-09-23 13:47:45] <dEBRUYNE> <sarang> your phone number <= Wouldn't those still be indistinguishable due to the random element?
    [2020-09-23 13:47:55] <sarang> ?
    [2020-09-23 13:48:06] <sarang> What random element?
    [2020-09-23 13:48:16] <sarang> The network can't verify that you encrypted a payment ID
    [2020-09-23 13:48:28] <dEBRUYNE> Ignore me, I am conflating things
    [2020-09-23 13:48:30] <sarang> You could arrange it so the _recipient_ could
    [2020-09-23 13:48:34] <sarang> but not at the consensus level
    [2020-09-23 13:48:42] <sarang> The best you can do is have the recipient not spend such an output
    [2020-09-23 13:48:43] <Isthmus> ^zcash does this, for example
    [2020-09-23 13:48:51] <sarang> The recipient? Yes
    [2020-09-23 13:49:29] <moneromooo> Having the recipient not spend actual money they got ? Fat chance it's gonna happen.
    [2020-09-23 13:49:30] <sarang> that's entirely possible (but not free from a space perspective)
    [2020-09-23 13:50:18] <dEBRUYNE> We could add a warning though
    [2020-09-23 13:50:18] <sarang> Isthmus: FWIW that's all on the client
    [2020-09-23 13:50:22] <dEBRUYNE> If such an output would be received
    [2020-09-23 13:50:24] <sarang> You could write a Zcash client that spends it anyway
    [2020-09-23 13:50:29] <sarang> Network can't tell
    [2020-09-23 13:50:38] <Isthmus> Yep
    [2020-09-23 13:51:22] <sarang> dEBRUYNE: we'd have to do an AEAD method and change the way that encryption happens
    [2020-09-23 13:51:46] <sarang> We'd probably end up including all recipient-encrypted data in that, which is much cleaner from a protocol perspective
    [2020-09-23 13:51:58] <sarang> and share a single AEAD tag
    [2020-09-23 13:52:56] <sarang> Anyway
    [2020-09-23 13:53:01] <sarang> We're coming to the end of the hour
    [2020-09-23 13:53:12] <sarang> Were there any other points relating to this that ought to be discussed now?
    [2020-09-23 13:53:57] <Isthmus> gg
    [2020-09-23 13:54:25] <sarang> If anything, I think this provides further evidence that enforcing standard TLV fields in `tx_extra` would be very useful
    [2020-09-23 13:54:42] <sarang> and the data indicate that there are no obvious existing use cases for nonstandard fields that would be disrupted
    [2020-09-23 13:55:37] <sarang> OK, any other research topics to share before the time is up?
    [2020-09-23 13:55:56] ⇐ vtnerd_ quit (~vtnerd@50-81-138-206.client.mchsi.com): Ping timeout: 260 seconds
    [2020-09-23 13:57:05] <sarang> If not, we can adjourn!
    [2020-09-23 13:57:09] → vtnerd_ joined (~vtnerd@50-81-138-206.client.mchsi.com)
    [2020-09-23 13:57:10] <sarang> Thanks to everyone for attending

# Action History
- Created by: SarangNoether | 2020-09-21T00:25:58+00:00
- Closed at: 2020-09-24T12:33:56+00:00
