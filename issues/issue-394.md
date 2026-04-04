---
title: 'Research meeting: 23 September 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/394
author: SarangNoether
assignees: []
labels: []
created_at: '2019-09-23T02:31:15+00:00'
updated_at: '2019-09-23T17:39:41+00:00'
type: issue
status: closed
closed_at: '2019-09-23T17:39:41+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 23 September 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [FC 2020](https://fc20.ifca.ai/index.html) submission, [Lelantus](https://eprint.iacr.org/2019/373) proof modifications, [RCT3](https://eprint.iacr.org/2019/508) revision
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-09-23T17:39:40+00:00
    [2019-09-23 13:00:50] <sarang> First up, GREETINGS
    [2019-09-23 13:00:55] <suraeNoether> howdy!
    [2019-09-23 13:01:36] <sarang> And, I suppose, ROUNDTABLE as well
    [2019-09-23 13:01:39] <sarang> suraeNoether: care to go first?
    [2019-09-23 13:02:16] <suraeNoether> sure, I spent all weekend working on the CLSAG paper for submission
    [2019-09-23 13:02:22] <suraeNoether> the deadline is 5am (my time) tomorrow morning
    [2019-09-23 13:02:29] <sarang> Some really good changes to definitions
    [2019-09-23 13:02:31] <suraeNoether> i've been up past 2am for the past few nights trying to get it all done
    [2019-09-23 13:02:40] <sarang> Better capturing forgeries, and cleaning up linking :D
    [2019-09-23 13:02:52] <suraeNoether> yeah, the paper is actually v gorgeous now, and i'm excited to update the preprint after submission
    [2019-09-23 13:03:07] <suraeNoether> also, reviewing the DLSAG paper today for submission to the same proceedings
    [2019-09-23 13:03:17] <suraeNoether> i missed the deadline for getting thring signatures out there, but 2/3 ain't bad
    [2019-09-23 13:03:27] <suraeNoether> once that deadline passes, i'm shifting gears back to code for a few days
    [2019-09-23 13:03:30] <sarang> Oh well, there are other good destinations too
    [2019-09-23 13:03:30] <suraeNoether> aaaand that's it
    [2019-09-23 13:03:37] <suraeNoether> yes for sure
    [2019-09-23 13:03:48] <sarang> Some with rolling deadlines, which may be much more convenient
    [2019-09-23 13:03:56] ⇐ WoomyZoomy quit (~Android@172.58.223.67): Ping timeout: 276 seconds
    [2019-09-23 13:04:02] <sarang> I've been working on a hodgepodge of items
    [2019-09-23 13:04:09] <sarang> FC 2020 submission review
    [2019-09-23 13:04:26] <sarang> Ongoing work with the Lelantus author on ideas and constructions for removing its sender tracing issue
    [2019-09-23 13:04:28] — suraeNoether kind of likes having a hard deadline outside of my control, it puts a fire underfoot
    [2019-09-23 13:04:56] <sarang> It's proving surprisingly tricky to get a Lelantus construction that admits both one-time addresses and prevents sender linking
    [2019-09-23 13:05:17] <sarang> It has to do with how range proofs are constructed using the one-time address, since this is used directly in a commitment
    [2019-09-23 13:05:57] <sarang> In the case without one-time addresses, the recipient generates a representation proof that assures verifiers the range proof is with respect to generators with unknown discrete log relationships
    [2019-09-23 13:06:12] <sarang> In the case with one-time addresses, I don't know a way to achieve this
    [2019-09-23 13:06:22] <sarang> So, work continues on it
    [2019-09-23 13:06:55] <sarang> Finally, the RCT3 authors released an update to their preprint
    [2019-09-23 13:07:29] <sarang> This is quite exciting... it modifies how public keys are used within spend proofs to fix a problem with a particular proof (which would otherwise lead to an exploit)
    [2019-09-23 13:07:40] <sarang> but it also permits the use of a single log-sized proof across all spends
    [2019-09-23 13:07:54] <sarang> So there are substantial changes to review and test
    [2019-09-23 13:08:20] <suraeNoether> i'm eager to get further into the details of them. i'm still skirting the edges of lelantus, ringct3, etc. HALO was a surprisingly short paper, and so many recent results are showing us all how important it is to formalize our transaction protocol as a circuit...
    [2019-09-23 13:08:56] <sarang> Halo is quite interesting, but seems to be widely misreported as something that is practically usable now for chain verification, which it is not
    [2019-09-23 13:09:38] <sarang> There is also not a soundness proof, but there are for some of the underlying constructions (which bodes well)
    [2019-09-23 13:10:50] <sarang> Sean (the author) thought there might be an interesting application to how Bulletproofs' inner-product arguments are batched
    [2019-09-23 13:11:04] <sarang> so it's neat stuff
    [2019-09-23 13:11:25] <suraeNoether> i liked the response "big if sound"
    [2019-09-23 13:11:31] <sarang> Heh, me too
    [2019-09-23 13:11:41] <suraeNoether> i don't know who tweeted that, but it's working it's way into my daily vocabulary.
    [2019-09-23 13:12:11] <suraeNoether> at the grocery store, looking at humongous squashes. Knock on the squash. "Big if sound."
    [2019-09-23 13:12:29] <sarang> -___-
    [2019-09-23 13:12:47] <sarang> Does anyone else have interesting work to share, or questions on anything?
    [2019-09-23 13:13:31] — suraeNoether was working on the squash joke for a full minute
    [2019-09-23 13:13:52] <mikerah> Can you go into more details about specifying the monero transaction protocol into a circuit
    [2019-09-23 13:13:54] <suraeNoether> its*
    [2019-09-23 13:14:36] <defterade_> What are the chances of CSLAG making it in the April hardfork?
    [2019-09-23 13:14:43] <suraeNoether> mikerah: long story short: a lot of the ZK proof systems out there rely on showing "Given an arithmetic circuit that describes a function f(-), here is y and a proof p that I know a secret x such that y = f(x)."
    [2019-09-23 13:14:46] <sarang> Specifying transaction requirements as a language suitable for various proving systems is useful for broader application
    [2019-09-23 13:15:00] <suraeNoether> the function f formalizes the language sarang just mentioned
    [2019-09-23 13:15:06] <sarang> defterade_: depends entirely on audits, which I'd like to address momentarily
    [2019-09-23 13:15:40] <suraeNoether> it can be complicated to take a statement like "I know one of these ring members, and the associated commitment opening" and turn it into an arithmetic circuit
    [2019-09-23 13:15:52] <suraeNoether> or, the resulting circuit could be really slow
    [2019-09-23 13:15:58] <suraeNoether> or too large or what have you
    [2019-09-23 13:16:13] <suraeNoether> so there's a challenge in formalizing our ring confidential transaction "statements" into an arithmetic circuit
    [2019-09-23 13:16:19] <sarang> Well, systems like Omniring take such statements, formalize them into a language, and then construct a proving system for that language
    [2019-09-23 13:16:24] <sarang> (albeit less generally)
    [2019-09-23 13:16:29] → WoomyZoomy joined (~Android@172.58.223.67)
    [2019-09-23 13:16:33] <mikerah> Have there been other attempts at specifying ring signatures in arithmetic circuits
    [2019-09-23 13:16:41] <kenshamir[m]> eprint 1076 also uses recursive proofs. The benchmarks are asymptotically equal to Marlon though.
    [2019-09-23 13:16:50] <suraeNoether> we can exploit a lot of available proving systems out there, possibly yielding more efficient ring confidential transactions, given a description of such a circuit
    [2019-09-23 13:16:58] ⇐ adhux0x0f0x3f quit (~adhux0x0f@gateway/tor-sasl/adhux0x0f0x3f): Remote host closed the connection
    [2019-09-23 13:17:10] <sarang> Not without trust requirements at this point
    [2019-09-23 13:17:29] → adhux0x0f0x3f joined (~adhux0x0f@gateway/tor-sasl/adhux0x0f0x3f)
    [2019-09-23 13:17:33] <kenshamir[m]> There was no comparison to Halo because Halo was too informalq
    [2019-09-23 13:17:54] <sarang> Proving systems specific to particular language constructions (Bulletproofs range proofs, Omniring, RCT3, etc.) tend to be reasonably efficient for having no private setup
    [2019-09-23 13:18:19] <suraeNoether> mikerah: not that i know of, yet... certainly not in the DDH + ROM setting without trusted setup
    [2019-09-23 13:18:43] <sarang> As far as CLSAG goes, OSTIF informs me that one code reviewer quoted $24750 (code only, not the paper)
    [2019-09-23 13:18:45] <mikerah> Ooh. Another research project idea!
    [2019-09-23 13:18:52] <kenshamir[m]> <mikerah "Have there been other attempts a"> I think you can do it, but it would not be efficient; a statement like Pubkey 1 OR pubkey2 OR ... PubkeyN
    [2019-09-23 13:18:53] <sarang> And one math reviewer quoted $7200 (paper only, not the code)
    [2019-09-23 13:18:58] <sarang> They are looking into it more
    [2019-09-23 13:19:46] <suraeNoether> i have to go for a doctor's appointment; please accept my apologies for bailing early. sarang, care to take it from here?
    [2019-09-23 13:19:47] <sarang> The math review could be completed by the end of November in this case
    [2019-09-23 13:19:54] <sarang> sure suraeNoether, see ya
    [2019-09-23 13:20:00] <suraeNoether> that's a decent deal for the math review tbh. who is it?
    [2019-09-23 13:20:16] <sarang> It isn't clear if I can share that publicly before they've made a formal commitment
    [2019-09-23 13:20:21] <sarang> but it's someone quite respected
    [2019-09-23 13:21:00] <mikerah> If I'm going to take a guess, I think it's Dmitry Khovatovich
    [2019-09-23 13:21:09] <mikerah> Not sure if I spelt his name correctly
    [2019-09-23 13:21:35] <sarang> Unclear about the timeline for the code review
    [2019-09-23 13:21:44] <sarang> OSTIF is inquiring with other groups
    [2019-09-23 13:22:51] <sarang> Any other questions or items to share before moving on?
    [2019-09-23 13:23:36] <sarang> All right then; on to ACTION ITEMS
    [2019-09-23 13:23:59] <sarang> This week, I'll be completing the edits and submission for FC 2020 (and updating on IACR and MRL archive)
    [2019-09-23 13:24:16] ⇐ midipoet quit (uid316937@gateway/web/irccloud.com/x-sbigusztxwedlpyo): Quit: Connection closed for inactivity
    [2019-09-23 13:24:29] <sarang> and continuing review of the updated RCT3 proofs and proving system
    [2019-09-23 13:24:47] <sarang> there's a lot of stuff to unpack with that
    [2019-09-23 13:25:48] <sarang> Anything else before we adjourn?
    [2019-09-23 13:25:55] <defterade_> Do the changes made in CLSAG warrant a level of audits to the extent of RandomX? (i.e. >= 3 code reviews)
    [2019-09-23 13:26:28] ⇐ midnightmagic quit (~midnightm@unaffiliated/midnightmagic): Ping timeout: 264 seconds
    [2019-09-23 13:26:45] <sarang> The code changes for the basic signature scheme (and some underlying plumbing) aren't terribly complex... there are plenty of other code changes that plug it in to the rest of the codebase
    [2019-09-23 13:27:36] <sarang> The math isn't very different from MLSAG, but is different enough to warrant a formal review... additionally, the proofs in the original MLSAG paper weren't very formal either, and we've worked to make the CLSAG definitions and proofs more extensive
    [2019-09-23 13:28:55] <sarang> That being said, I would be surprised if 3 separate code audits would be of value in this case, depending on the scope
    [2019-09-23 13:29:30] <sarang> Getting review of the math, whether by the usual peer-review process or a paid review, is certainly a good idea
    [2019-09-23 13:30:18] <ArticMine> So are looking instead at one maybe two audits?
    [2019-09-23 13:30:26] <sarang> It's not up to me
    [2019-09-23 13:30:54] ⇐ sech1 quit (~sech1@31-208-119-248.cust.bredband2.com): Read error: Connection reset by peer
    [2019-09-23 13:31:18] <defterade_> But it would be fair to say the financial burden for the community is expected to be lower than RandomX?
    [2019-09-23 13:31:32] <sarang> Given the numbers presented so far, it seems so
    [2019-09-23 13:31:55] <sarang> The sum of the two current quotes (code and math) is $31950
    [2019-09-23 13:32:28] <sarang> Hopefully the code quote will be reduced once the scope is more clearly (and perhaps narrowly) defined
    [2019-09-23 13:33:02] <sarang> There's the code that produces and checks signatures, and then there's the code that integrates these into transactions etc.
    [2019-09-23 13:34:35] <defterade_> Has there been any discussion on changing the ring size when CLSAG goes live?
    [2019-09-23 13:34:52] <sarang> There has been
    [2019-09-23 13:35:18] <sarang> IIRC increasing from 11 to 13 would retain the same verification time as we have now
    [2019-09-23 13:35:51] <sarang> Whether or not this marginal increase is "worth it" is an open question
    [2019-09-23 13:36:14] <defterade_> Doesn't break the prime sequence, nice
    [2019-09-23 13:36:17] <defterade_> Okay
    [2019-09-23 13:36:51] <sarang> Righto, thanks to everyone for attending; logs will be posted to the GitHub issue shortly


# Action History
- Created by: SarangNoether | 2019-09-23T02:31:15+00:00
- Closed at: 2019-09-23T17:39:41+00:00
