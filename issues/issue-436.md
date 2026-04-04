---
title: 'Research meeting: 12 February 2020 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/436
author: SarangNoether
assignees: []
labels: []
created_at: '2020-02-06T14:24:32+00:00'
updated_at: '2020-02-12T19:04:04+00:00'
type: issue
status: closed
closed_at: '2020-02-12T19:04:04+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 12 February 2020 @ 18:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-02-12T19:04:04+00:00
    [2020-02-12 13:00:41] <sarang> Greetings!
    [2020-02-12 13:00:51] <ArticMine> Hi
    [2020-02-12 13:01:45] <UkoeHB_> Hiya
    [2020-02-12 13:01:55] <n3ptune> Hello
    [2020-02-12 13:01:59] <UkoeHB_> Thanks selsta I'll look
    [2020-02-12 13:02:15] ⇐ kico quit (~kico@gateway/tor-sasl/kico): Quit: brb
    [2020-02-12 13:03:08] <sarang> I suppose we can move to roundtable discussion
    [2020-02-12 13:03:15] <sarang> Who wishes to share interesting research?
    [2020-02-12 13:03:20] <sgp_> hello
    [2020-02-12 13:03:43] <n3ptune> Something quick from NRL
    [2020-02-12 13:03:51] <n3ptune> We've been looking at some results regarding the extra field in transactions.  We have one thing to share today
    [2020-02-12 13:04:10] <n3ptune> Here is an analysis of Payment id usage since v10 when unencrypted payment ids were deprecated:
    [2020-02-12 13:04:10] <n3ptune> https://usercontent.irccloud-cdn.com/file/Xf1uZRsZ/image.png
    [2020-02-12 13:04:32] <n3ptune> (Sorry there is an uncorrected typo: "Unencrypted Included x Encrypted Absent" should be 232980 (not 232972) and "Unencrypted Absent x Encrypted Included" should be 1904765)
    [2020-02-12 13:04:46] → kico joined (~kico@gateway/tor-sasl/kico)
    [2020-02-12 13:05:08] <sarang> ^ moneromooo etc.
    [2020-02-12 13:05:23] <UkoeHB_> It's actually not 'mandatory', just part of the core wallet's behavior
    [2020-02-12 13:05:39] <UkoeHB_> As jtgrassie liked to insist :p
    [2020-02-12 13:05:48] <sarang> Nothing stops a wallet from simply including a fixed default value either
    [2020-02-12 13:05:58] <sarang> (can't enforce "uniformly random" in that way)
    [2020-02-12 13:07:36] <sarang> Once again touches on the idea of extra parsing/enforcement
    [2020-02-12 13:08:33] <sarang> Are there other indications of what non-standard software it might be?
    [2020-02-12 13:09:22] <sgp_> 17% is a good amount that didn't update properly
    [2020-02-12 13:09:23] ⇐ kico quit (~kico@gateway/tor-sasl/kico): Ping timeout: 240 seconds
    [2020-02-12 13:09:32] <sgp_> do they save slightly on fees?
    [2020-02-12 13:09:35] <n3ptune> That's a good question, we didn't look into the transactions but there may be other things going on that make more of a fingerprint
    [2020-02-12 13:10:02] — n3ptune notes this to look into
    [2020-02-12 13:10:36] <sarang> Thanks n3ptune
    [2020-02-12 13:11:02] <n3ptune> Thanks! Just sharing these numbers today
    [2020-02-12 13:11:11] → kico joined (~kico@gateway/tor-sasl/kico)
    [2020-02-12 13:11:15] <sgp_> if the fees are lower, I can see someone setting it up this way if they process many transactions
    [2020-02-12 13:12:02] <moneromooo> Looking at long payment id usage since 1.7e6 is a bit pointless. What is it from 1.98e6 ?
    [2020-02-12 13:12:41] <n3ptune> I can check
    [2020-02-12 13:12:45] <UkoeHB_> n3ptune: the core wallet only creates encrypted payment IDs for all 2-output tx, would you mind looking into the distinction (proportion encrypted IDs with 2-output and >2 output)>
    [2020-02-12 13:13:26] <UkoeHB_> moneromooo: was the dummy encrypted payment ID also since 1.98e6?
    [2020-02-12 13:13:34] <n3ptune> Another good question
    [2020-02-12 13:14:36] <moneromooo> I think before.
    [2020-02-12 13:15:00] <moneromooo> It was merged late january 2019.
    [2020-02-12 13:16:02] <moneromooo> Yes, it was included in the release for that height.
    [2020-02-12 13:16:05] <Isthmus> I don't think we looked at long PID
    [2020-02-12 13:16:09] <Isthmus> Sorry, here is the updated figure
    [2020-02-12 13:16:11] <Isthmus> https://usercontent.irccloud-cdn.com/file/t5ozuruh/image.png
    [2020-02-12 13:17:11] <n3ptune> ?  Long PID = Unencrypted PID, yes
    [2020-02-12 13:17:24] <moneromooo> Yes.
    [2020-02-12 13:17:26] <Isthmus> Oh, I was thinking integrated
    [2020-02-12 13:17:43] <Isthmus> Sorry, on 4 hours of sleep, no coffee, and in presentations at a crypto compliance company all morning
    [2020-02-12 13:17:57] <Isthmus> But they're cool with me being half in MRL, obviously they've been pretty supportive of my research over the past year :- )
    [2020-02-12 13:19:00] <sarang> How ominous
    [2020-02-12 13:19:52] <UkoeHB_> it might just mean more significant implementations exist than just core, which might be good news also
    [2020-02-12 13:20:39] <sarang> Well, not if the result is fingerprinting
    [2020-02-12 13:20:52] <UkoeHB_> n3ptune: also, afaik coinbase transactions do not use payment IDs (a round 200k tx over that period)
    [2020-02-12 13:22:20] <n3ptune> The numbers should be for non-coinbase only
    [2020-02-12 13:23:43] <sarang> Well, in the interest of time, shall we continue? Hopefully we can get more detailed data, which can help any future decisions about parsing
    [2020-02-12 13:24:28] <sarang> Thanks for the data Isthmus and n3ptune
    [2020-02-12 13:24:49] <n3ptune> Thx, I'll check out those questions
    [2020-02-12 13:25:48] <sarang> Other research to discuss or share?
    [2020-02-12 13:26:50] <sarang> UkoeHB _ ?
    [2020-02-12 13:26:52] <sarang> suraeNoether ?
    [2020-02-12 13:27:57] <sarang> OK, I can discuss a few short items
    [2020-02-12 13:28:01] <UkoeHB_> ok, I sketched out a light node proposal https://github.com/monero-project/research-lab/issues/69 pls leave your thoughts there if interested
    [2020-02-12 13:28:05] <sarang> Ah ok, nvm
    [2020-02-12 13:28:07] <sarang> go ahead UkoeHB_
    [2020-02-12 13:28:53] <UkoeHB_> ZtM2 I got through multisig and the draft of that chapter is done, started working on escrowed marketplace chapter which will be done by next meeting https://www.pdf-archive.com/2020/02/12/zerotomoneromaster-v1-0-25/zerotomoneromaster-v1-0-25.pdf
    [2020-02-12 13:29:06] <UkoeHB_> thats all from me
    [2020-02-12 13:29:13] <Isthmus> @UkoeHB_ just scoped that proposal last night, looks like great stuff
    [2020-02-12 13:29:27] <sarang> Looks to be similar to SPV structure?
    [2020-02-12 13:29:54] <UkoeHB_> possibly, idk anything about SPV
    [2020-02-12 13:31:27] ⇐ midipoet quit (uid316937@gateway/web/irccloud.com/x-rrgiwaafzjlgluyi): Quit: Connection closed for inactivity
    [2020-02-12 13:32:44] <sarang> I worked out data storage inside RCT3 proofs (both single- and multi-input) as well as storage in multi-input Triptych
    [2020-02-12 13:32:57] <sarang> Finished code and tests for new transaction proofs
    [2020-02-12 13:33:08] <sarang> did some Dandelion++ review
    [2020-02-12 13:33:16] <gingeropolous> yay triptych!
    [2020-02-12 13:33:32] <sarang> Wrote some code to demo spend/non-spend status proofs that have been discussed previously
    [2020-02-12 13:33:47] <sarang> and overhauled the Omniring/RCT3/Triptych key image multisig construction protocol
    [2020-02-12 13:34:04] <ArticMine> Any size indications for triptych?
    [2020-02-12 13:35:01] <sarang> Individual transactions? Sure, that's been available for some time
    [2020-02-12 13:35:40] <sarang> https://github.com/SarangNoether/skunkworks/blob/sublinear/triptych.md
    [2020-02-12 13:36:01] <sarang> Now that I have I/O structure data from n3ptune, I can run some chain-wide estimates based on that
    [2020-02-12 13:36:15] <sarang> since different tx protocols imply different tradeoffs as I/O structure changes
    [2020-02-12 13:39:02] <ArticMine> It seems to me a move in the reference tx size from 3000 bytes to 4000 bytes would be needed
    [2020-02-12 13:39:30] <ArticMine> Which is very reasonable given the mixin privacy gains
    [2020-02-12 13:39:44] <UkoeHB_> why increase?
    [2020-02-12 13:39:52] <sarang> It depends on what protocol (if any) is chosen, what parameters used, etc.
    [2020-02-12 13:40:21] <UkoeHB_> ah i see, for 1024 ring size
    [2020-02-12 13:40:40] <ArticMine> I am saying with N = 512 or 1024
    [2020-02-12 13:42:08] <gingeropolous> what are the hurdles for tryptich? besides me wanting to spell it wrong all the time
    [2020-02-12 13:42:09] <ArticMine> If this goes through, by the time it makes it to the main chain the drop in block reward would easily cover the fee increase
    [2020-02-12 13:42:50] <ArticMine> If we increase the penalty free block weight to 400000 bytes
    [2020-02-12 13:43:29] <sarang> gingeropolous: no peer review yet
    [2020-02-12 13:43:47] <sarang> I also need to know the practical drawbacks to the more complex multisig operations
    [2020-02-12 13:43:58] <sarang> especially on lower-powered devices
    [2020-02-12 13:44:17] <sarang> They'd need to support Paillier encryption/decryption for multisig with any of the sublinear protocols
    [2020-02-12 13:44:19] <ArticMine> We must also keep in mind this is less than a year of Nielsen's Law of Internet Bandwidth
    [2020-02-12 13:44:45] <gingeropolous> ugh. what, for those silly hardware wallets?
    [2020-02-12 13:45:00] <sarang> Well, anything that would need to participate in multisig
    [2020-02-12 13:45:12] → Febo joined (~Febo@89-212-17-205.static.t-2.net)
    [2020-02-12 13:45:28] <sarang> The process involves doing peer-to-peer Paillier operations, some Schnorr and commitment stuff, etc.
    [2020-02-12 13:45:29] <UkoeHB_> would multi-tryptich work with any kind of join protocol?
    [2020-02-12 13:45:50] <sarang> Unclear. It's still in the early stages
    [2020-02-12 13:47:36] <UkoeHB_> before this meeting gets wrapped up, I am curious about the state of discussion around Monero's difficulty algorithm; zawy12 seems to have done a lot of research on the topic of difficulty algos https://github.com/zawy12/difficulty-algorithms/issues/50
    [2020-02-12 13:47:50] <UkoeHB_> and suraeNoether was at one point doing research on that area
    [2020-02-12 13:48:25] <UkoeHB_> apparently Monero's algorithm is quite bad, relatively speaking
    [2020-02-12 13:48:34] <sarang> Interesting; I had seen some of their earlier work, but not this summary
    [2020-02-12 13:48:57] → midipoet joined (uid316937@gateway/web/irccloud.com/x-tqprrulcnaneouzc)
    [2020-02-12 13:51:35] <sarang> The conclusion seems to be that the potential oscillations would be of much greater importance for uses with large mining variance
    [2020-02-12 13:52:00] <sarang> (which isn't really part of the design choice)
    [2020-02-12 13:54:09] <sarang> Worth a read, now that we have the link
    [2020-02-12 13:54:33] <sarang> UkoeHB_: did you want to discuss extra sorting, given its relationship to the information from n3ptune and Isthmus?
    [2020-02-12 13:55:23] <UkoeHB_> I feel Ive made my case for it, although Isthmus says they are working on a big comprehensive report so at that time I may recapitulate
    [2020-02-12 13:56:34] <sarang> Fair enough. Trying to enforce better uniformity and order is a good idea, so I agree
    [2020-02-12 13:57:03] <sarang> It may come down to questions of efficiency and "someone needs to write it", but who knows
    [2020-02-12 13:57:44] <UkoeHB_> enforcing it should be less than 100 lines of code IMO
    [2020-02-12 13:57:57] <sarang> Sounds like someone is volunteering :D
    [2020-02-12 13:58:18] <sarang> Anyway, there is a Konferenco meeting starting presently, so any final comments or thoughts before adjourning?
    [2020-02-12 14:00:12] <sarang> Righto; thanks for attending, everyone


# Action History
- Created by: SarangNoether | 2020-02-06T14:24:32+00:00
- Closed at: 2020-02-12T19:04:04+00:00
