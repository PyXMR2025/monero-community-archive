---
title: Monero Research Lab Meeting - Wed 20 July 2022
source_url: https://github.com/monero-project/meta/issues/720
author: Rucknium
assignees: []
labels: []
created_at: '2022-07-18T16:35:09+00:00'
updated_at: '2022-07-25T15:09:10+00:00'
type: issue
status: closed
closed_at: '2022-07-25T15:09:10+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

5. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#719 

# Discussion History
## UkoeHB | 2022-07-20T18:30:12+00:00
```
[07-20-2022 16:59:45] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/720
[07-20-2022 16:59:45] <UkoeHB> 1. greetings
[07-20-2022 16:59:45] <UkoeHB> hello
[07-20-2022 16:59:57] <tevador> Hi
[07-20-2022 17:00:03] <hyc> hi
[07-20-2022 17:00:06] <dangerousfreedom> Hello
[07-20-2022 17:00:13] <Rucknium[m]> Hi
[07-20-2022 17:00:23] <gingeropolous> hi
[07-20-2022 17:00:23] <FAA45> Hi
[07-20-2022 17:00:33] <jberman[m]> hi
[07-20-2022 17:02:13] <UkoeHB> 2. updates, what's everyone working on?
[07-20-2022 17:03:54] <tevador> Working on an X25519 implementation for Jamtis to replace ed25519 in shared secret calculations.
[07-20-2022 17:04:40] <UkoeHB> me: did some planning and initial work for integrating legacy cryptonote outputs into my seraphis lib. My goal is to provide enough utilities that a standalone wallet can be built, completely independent of wallet2. So, the new lib should be able to do balance recovery on the entire legacy chain plus spend any of those old outputs.
[07-20-2022 17:04:51] <jberman[m]> not research related, but continuing review on 8076 (hopefully will be complete today), moving on to 7999/vtnerd's alternative next, and opened a CCS
[07-20-2022 17:04:58] <Rucknium[m]> Working on OSPEAD. I reduced an algorithm with naive implementation computational cost of O(N^2) to approximately O(N) computational cost 😎
[07-20-2022 17:05:33] <Rucknium[m]> I am also putting the research computing server to the test with https://github.com/Rucknium/misc-research/tree/main/General-Blockchain-Age-of-Spent-Outputs
[07-20-2022 17:05:41] <dangerousfreedom> I have been trying to solve the mystery of a wrong signature validation using my Python tools and found out that Monero is performing a wrong operation for certain cases which leads to a malleability issue. Not exploitable or exploited as far I know by now. The details I will publish on my website and on github soon (tonight or tomorrow morning). :)
[07-20-2022 17:05:41] <gingeropolous> got the storage up and running (14T on SSD, 76T on HDD). reminder that if anyone needs compute resources, feel free to contact me.
[07-20-2022 17:08:26] <UkoeHB> 3. discussion; today we should start by returning to the jamtis address index/tag question (whether to use 64 bits for the tag -> 56 bit address index + 8 bit MAC, or increase to something like 144 bits -> 128 bit index + 16 bit MAC); this was previously discussed in this meeting https://github.com/monero-project/meta/issues/697 and also here https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024
[07-20-2022 17:10:11] <tevador> it's a costs vs benefits question
[07-20-2022 17:12:04] <UkoeHB> personally, some extra bytes in outputs and addresses is worth it for peace of mind
[07-20-2022 17:12:24] <UkoeHB> my more technical arguments are in the jamtis gist
[07-20-2022 17:14:17] <UkoeHB> I guess, does anyone have any questions on that topic? Or is everyone reading? lol
[07-20-2022 17:14:40] <jberman[m]> I think the benefit of secure client-side random address generation compatible with an ubiquitous simple global standard like UUID's (128 bit index achieves this) + reducing/removing the incentive for a 3rd party scanner to collect full balance keys to offer better UX (16 bit MAC achieves this) = significant
[07-20-2022 17:15:42] <dangerousfreedom> UkoeHB: I'm not familiar with it yet, sorry :p
[07-20-2022 17:16:43] <Rucknium[m]> We need to get ISO and NIST in on this ;)
[07-20-2022 17:16:43] <Rucknium[m]> More seriously, I do not feel that I have the necessary knowledge base or skills to have much of an opinion on it.
[07-20-2022 17:16:55] <tevador> jberman[m]: can you elaborate about the 16-bit MAC argument?
[07-20-2022 17:18:23] <tevador> you mean people would give up their view-balance key to speed up their wallet sync?
[07-20-2022 17:19:27] <jberman[m]> "Does saving 5 seconds per wallet sync for a subset of Monero users justify the costs?" > I think the answer to this question is yes. I think a MyMonero-like service would emerge that takes view balance keys and users wouldn't care
[07-20-2022 17:19:47] <jberman[m]> users of that service
[07-20-2022 17:20:35] <jberman[m]> ideally the UX is as close to 0 time spent syncing the wallet as possible so that kind of service has no incentive to do it
[07-20-2022 17:21:39] <Rucknium[m]> An implementation of fee fingerprinting for MyMonero transactions could help us estimate the current on-chain transaction volume (if not proportion of users) of lws-like services.
[07-20-2022 17:22:24] <jberman[m]> I also think the "light wallet scanning" use case where you run a server for family and friends, without having access to amounts nor definitive knowledge of spends/receives is highly attractive. I think this use case *could* end up a larger subset of Monero users and is worth optimizing for
[07-20-2022 17:23:05] <tevador> Fair points.
[07-20-2022 17:23:21] <moneromooo> 5 seconds on how much ? Half an hour ? I've not synced a wallet in ages.
[07-20-2022 17:24:24] <tevador> it would be something like 5 seconds vs 0.1 seconds with the larger MAC
[07-20-2022 17:24:49] <moneromooo> On top of how much ?
[07-20-2022 17:25:45] <moneromooo> I mean, you can optimize a step from 5 seconds to 0 seconds, but if the other steps tkae half an hour, it's de minimis.
[07-20-2022 17:25:49] <tevador> This is the whole sync time from the moment you log in to the remote service.
[07-20-2022 17:26:32] <UkoeHB> moneromooo: it's for view scanning with a remote helper like MyMonero (lws)
[07-20-2022 17:26:52] <UkoeHB> local full-scanning wouldn't be materially impacted
[07-20-2022 17:26:58] <moneromooo> I assume you're assuming new wallets, created after jamtis would be added then ?
[07-20-2022 17:27:36] <UkoeHB> yes this is only for scanning seraphis enotes
[07-20-2022 17:28:53] <tevador> I think this assumed ~250M seraphis outputs. The view tag will filter that to 1M and the 8-bit MAC to 3.9K, the 16-bit MAC to a handful.
[07-20-2022 17:28:57] <UkoeHB> it would also impact old wallets that get migrated and then get set up with a remote scanner
[07-20-2022 17:30:32] <tevador> We could also do 48+16 if we really wanted a 16-bit MAC, but decided to keep the address tag at 8 bytes.
[07-20-2022 17:30:45] <moneromooo> Does the client scan the 3.9k ? If so, it provides the client with some layer of privacy vs winnowing really really well.
[07-20-2022 17:31:16] <UkoeHB> winnowing?
[07-20-2022 17:31:25] <moneromooo> pruning ?
[07-20-2022 17:31:29] <moneromooo> Filtering
[07-20-2022 17:31:36] <tevador> The client scans the 1M outputs.
[07-20-2022 17:32:27] <tevador> 3.9K outputs would pass the 8-bit MAC, so the client would have to calculate the output key and check it
[07-20-2022 17:32:56] <tevador> with the 16-bit MAC, there would be almost no false positives
[07-20-2022 17:34:15] <rbrunner> There is a separate key that I could hand over to somebody to do MAC scanning for me, right?
[07-20-2022 17:34:18] <tevador> I guess the actual async time would be determined by the time to download the several MB of candidate outputs
[07-20-2022 17:34:28] <moneromooo> So in addition to the 5 seconds or 0.1 seconds, you have to also add the download time for those million outputs too.
[07-20-2022 17:35:13] <tevador> rbrunner: that's the full view key
[07-20-2022 17:35:25] <tevador> you would not normally give it away
[07-20-2022 17:35:58] <rbrunner> Ah, ok, that's too powerful then. But what is then the least powerful key I can give to any kind of third-party service?
[07-20-2022 17:36:27] <tevador> the key to calculate the shared secret and the view tag
[07-20-2022 17:37:20] <rbrunner> I see, thanks. So that will filter down to 1M in your example.
[07-20-2022 17:37:20] <jberman[m]> the "find-received key"
[07-20-2022 17:38:22] <tevador> it would be roughly 100 MB
[07-20-2022 17:39:10] <UkoeHB> tevador: this CBC ciphertext stealing is an ugly mess for our use-case, can I just stick with my original idea? It's way easier to understand, read, and validate.
[07-20-2022 17:39:49] <tevador> what is the problem with it? I think it just swaps the order of the last two blocks
[07-20-2022 17:40:35] <UkoeHB> yes swapping the data around makes it an ugly mess, because with my version you can do operations on the ciphertext/plaintext directly
[07-20-2022 17:40:45] <tevador> so that the block that contains the MAC is the first 16 bytes of the ciphertext
[07-20-2022 17:42:27] <UkoeHB> but with this CBC cts you have to move data around in buffers...
[07-20-2022 17:42:37] <tevador> It seemed like a good idea to use an existing standard for the encryption. Not rolling our own.
[07-20-2022 17:43:42] <UkoeHB> in practice everyone who looks at this does the same set of steps: understand why the method works, read the code to see if it does that
[07-20-2022 17:44:03] <UkoeHB> CBC ciphertext stealing is more complicated and harder to read, but does the same thing
[07-20-2022 17:45:13] <UkoeHB> I'd rather say "equivalent to CBC ciphertext stealing" and then anyone who cares about the standard can go look at it
[07-20-2022 17:45:30] <tevador> OK
[07-20-2022 17:46:17] <UkoeHB> sweet thank you! and thanks for pointing out this standard, I had no idea it existed
[07-20-2022 17:47:52] <rbrunner> Does something get slightly longer now with this decision? The address, because some more bytes?
[07-20-2022 17:48:02] <UkoeHB> tevador: "rbrunner: that's the full view key" -> actually you can do this with the generate address key
[07-20-2022 17:48:28] <UkoeHB> but there is not much advantage there, because MAC scanning is so cheap
[07-20-2022 17:48:40] <UkoeHB> I guess data transmission*
[07-20-2022 17:48:44] <jberman[m]> > My point was that MAC addresses work with a global 48-bit space.
[07-20-2022 17:48:45] <jberman[m]> AFAIU MAC addresses need only be unique to a local network and it's not generally expected that local networks will have millions of devices connected the next 100 years
[07-20-2022 17:48:49] <tevador> there is an advantage for the download size
[07-20-2022 17:49:00] <jberman[m]> On the contrary, it's easy to envision internet businesses generating millions of addresses. The 3 bullets here make me feel uncomfortable even with a 56-bit address space: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4238074#gistcomment-4238074
[07-20-2022 17:49:27] <jberman[m]> And a collision is harmful to privacy, it doesn't only have the propensity to bork a distributed system that doesn't properly account for it. The downsides seem more significant in our case
[07-20-2022 17:50:10] <UkoeHB> tevador: ah, actually download size isn't helped due to the self-send optimizatioin
[07-20-2022 17:50:18] <UkoeHB> you need all view tag matches to find selfsends
[07-20-2022 17:51:58] <rbrunner> I am a bit lost: The proposal that is now "on the table", how many bits does that have in this regard? More than those 56 bits?
[07-20-2022 17:52:17] <UkoeHB> rbrunner: I proposed 128-bit address indices
[07-20-2022 17:52:47] <tevador> rbrunner: with the 64-bit index, addresses are 180 characters and with the 144-bit index, the are slightly longer at 196 characters
[07-20-2022 17:53:09] <tevador> output size is also slightly larger with the longer tag
[07-20-2022 17:53:14] <rbrunner> That clears it up, thank you.
[07-20-2022 17:54:02] <rbrunner> Seems to me if we accept 180 characters we can also accept 196 if it has tangible benefits. This is anyway already beyond bad :)
[07-20-2022 17:54:57] <rbrunner> A bit unfortunate for QR codes however
[07-20-2022 17:55:40] <tevador> I think there still isn't a good argument for the 16-bit MAC. Lazy users might still want to give up their view keys to avoid the 100MB data download.
[07-20-2022 17:56:51] <tevador> the collision resistance of the longer tag is a clear benefit, so perhaps something like a 120+8 setup might be better even if that wastes 1 bit in the base32 encoding
[07-20-2022 17:57:21] <rbrunner> 128+8?
[07-20-2022 17:57:42] <tevador> 120+8, so we can use one block of the cipher
[07-20-2022 17:57:50] <rbrunner> Ah, ok
[07-20-2022 17:57:51] <tevador> UUIDs are 122 bits anyways
[07-20-2022 17:59:19] <rbrunner> Your argument is basically "Who spends the time to download 100MB does not care too much whether scanning through that is 5s or 0.1s". Did I get this right?
[07-20-2022 17:59:33] <UkoeHB> I prefer a full 128 bits for the index to avoid imposing a 'magic number' on users.
[07-20-2022 18:00:06] <tevador> rbrunner: exactly
[07-20-2022 18:00:23] <tevador> UkoeHB: the index is hidden from users
[07-20-2022 18:00:28] <UkoeHB> 16 bytes is a universal size, 15 bytes would be a special magic size
[07-20-2022 18:00:50] <UkoeHB> like I said in the gist, users as in whoever is trying to use the index in their application
[07-20-2022 18:01:08] <tevador> they will not use the index, the API will return some other identifier
[07-20-2022 18:01:29] <UkoeHB> byte field, whatever
[07-20-2022 18:01:29] <tevador> just like they will not be applying the Twofish cipher
[07-20-2022 18:01:50] <tevador> the returned byte field can be 16 bytes
[07-20-2022 18:02:17] <rbrunner> So it's down to API implementers who have to known about those 120 bytes?
[07-20-2022 18:02:24] <tevador> you can stuff the 120 bits into an UUID, for example
[07-20-2022 18:02:40] <tevador> and set two bits from the network flag
[07-20-2022 18:02:44] <UkoeHB> I'm saying the API user has to know how many bytes they get to define...
[07-20-2022 18:02:54] <UkoeHB> 16 is a universal amount, 15 is a magic number
[07-20-2022 18:03:06] <rbrunner> Maybe you two talk about different APIs?
[07-20-2022 18:03:14] <tevador> The API user doesn't define. They ask for an address.
[07-20-2022 18:03:47] <UkoeHB> I'm talking about the deeper API of the protocol itself, not any higher layer
[07-20-2022 18:03:56] <moneromooo> 15 is the max number you can represent on a nybble in 2's complement. A very universal number.
[07-20-2022 18:04:09] <rbrunner> :)
[07-20-2022 18:04:27] <UkoeHB> moneromooo: lol
[07-20-2022 18:05:13] <moneromooo> Actually, scratch the 2's complement part.
[07-20-2022 18:05:21] <rbrunner> Might be that in the real world pretty few people will ever step down so deep that they will see this 120. A handful of library implementers maybe.
[07-20-2022 18:05:30] <Rucknium[m]> IMHO, if 15 is advantageous compared to 16, my low-info preference is to go with 15. Satoshi was the first to use base58 after all, since it fit a specific need.
[07-20-2022 18:06:02] <UkoeHB> the only advantage here is saving 2 bytes
[07-20-2022 18:06:06] <tevador> 120+8 avoids the block cipher gymnastics
[07-20-2022 18:06:15] <UkoeHB> and a slightly less complicated cipher
[07-20-2022 18:06:24] <rbrunner> Sounds good?
[07-20-2022 18:06:37] <UkoeHB> not to me lol
[07-20-2022 18:07:11] <rbrunner> Yeah, because you are one of those unlucky few library implementers who get to see the sheer ugliness of 120 :)
[07-20-2022 18:07:45] <UkoeHB> well so far I have avoided making ugly decisions, after 35k+ lines of code, and I certainly don't want to start...
[07-20-2022 18:07:46] <tevador> I'm still not convinced we are not leaking information by using ECB on 2 overlapping blocks.
[07-20-2022 18:08:12] <tevador> even if the first block covers the whole secret index
[07-20-2022 18:09:00] <UkoeHB> tevador: it's not ECB, it's an overlapping CBC
[07-20-2022 18:09:12] <UkoeHB> ECB doesn't have any XORing
[07-20-2022 18:09:20] <tevador> it's CBC with an IV of all zeroes
[07-20-2022 18:11:54] <tevador> btw 120 bits is not ugly, I'm using it for the hash identifier here since it's divisible by 5 bits for easy base32 encoding: https://github.com/tevador/id32
[07-20-2022 18:12:08] <rbrunner> Maybe a stupid question, but what happens if somebody cracks that encryption and gets to see those bits in clear? How bad would that be?
[07-20-2022 18:12:29] <UkoeHB> it's ugly for a generic bytefield that anyone can freely define
[07-20-2022 18:12:38] <Rucknium[m]> Seraphis is currently 35k+ lines of code? Impressive, koe
[07-20-2022 18:12:54] <UkoeHB> Rucknium[m]: well that's the diff on my branch vs master
[07-20-2022 18:13:34] <UkoeHB> rbrunner: you learn the address index that's all - it depends on how that index was defined, whether it means something
[07-20-2022 18:14:20] <tevador> how about an UUID that has 122 bits you can define? :P
[07-20-2022 18:14:40] <rbrunner> Ok. But of course still bad if somebody would catch to leak some info here. And the obligatory "Monero is finally cracked" articles ...
[07-20-2022 18:14:50] <rbrunner> *would catch us
[07-20-2022 18:15:00] <UkoeHB> tevador: the overlapping cipher is similar to ciphering the same block twice in a row; if that could leak information, then I don't see how ciphering would be secure
[07-20-2022 18:15:18] <jberman[m]> The ease to develop: generate UUID -> address index, sounds very nice to me as well fwiw
[07-20-2022 18:16:40] <rbrunner> But for that we would need the full 128 bits, right?
[07-20-2022 18:17:28] <rbrunner> because 122
[07-20-2022 18:18:44] <jberman[m]> I should say, the ease to develop: generate UUID v4 -> address index...
[07-20-2022 18:19:39] <tevador> 128 bits would have the advantage of supporting all versions of UUIDs
[07-20-2022 18:19:46] <rbrunner> Hmm, maybe a bit overkill if you could as well just randomly choose those bits?
[07-20-2022 18:20:01] <rbrunner> Or I don't get fully get your idea
[07-20-2022 18:20:07] <rbrunner> *yet
[07-20-2022 18:20:18] <jberman[m]> "128 bits would have the advantage of supporting all versions of UUIDs" -> true
[07-20-2022 18:24:14] <jberman[m]> Compatibility with a UUID system enables e.g. a merchant system to use UUID's to identify orders in their system and then use as input to generate addresses. It's more of a compatibility/standardized integration thing. Sure people could just use random bytes instead of UUID's in all cases, but UUID's are an ubiquitous identifier standard people opt for instead
[07-20-2022 18:24:57] <rbrunner> I see
[07-20-2022 18:25:36] <rbrunner> Also has trust on its side
[07-20-2022 18:25:44] <rbrunner> As some sort of psychological benefit
[07-20-2022 18:26:09] <rbrunner> And the DB would already complain if there was a collision, right?
[07-20-2022 18:26:54] <rbrunner> But well, it would do that also with the corresponding number of random bytes ...
[07-20-2022 18:29:18] <UkoeHB> We are well past the hour on the meeting, so I think I'll call it here. The subject of jamtis address tags hasn't found a conclusion, but at least it's quite easy to change the implementation if needed.
[07-20-2022 18:29:22] <UkoeHB> Thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-07-18T16:35:09+00:00
- Closed at: 2022-07-25T15:09:10+00:00
