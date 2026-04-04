---
title: 'Monero Dev Meeting #82 - Monday, 2024-08-12, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1053
author: rbrunner7
assignees: []
labels: []
created_at: '2024-08-09T14:33:50+00:00'
updated_at: '2024-08-12T19:46:30+00:00'
type: issue
status: closed
closed_at: '2024-08-12T19:46:30+00:00'
---

# Original Description
Time of these regular meetings is 18:00 UTC on each Monday. "Location" is the Matrix room *Monero Dev*, #monero-dev:monero.social ([Matrix.to link](https://matrix.to/#/#monero-dev:monero.social)), Libera IRC channel #monero-dev.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1050

These Monday meetings were originally for the *Seraphis wallet workgroup*, but in August 2024 it was decided to broaden the meetings to general dev meetings as they existed until a few years back, and relocate to the proper dev room and IRC channel.

# Discussion History
## rbrunner7 | 2024-08-12T19:46:30+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1053
<j​berman> *waves*
<s​needlewoods> hey
<o​ne-horse-wagon> Hello.
<v​tnerd> Hi
<d​angerousfreedom> Hi
<sech1> Hello
<0​xfffc> Hi everyone
<tobtoht_> hi
<sech1> Is there an agenda for this meeting?
<h​into> hello
<o​frnxmr> No
<j​effro256> howdy
<r​brunner7> Before we come to the reports: We have a surprising amount of ideas floating around how many dev meetings with what kind of foci in which rooms we should hold.
<r​brunner7> I propose to keep discussion about this *out of this meeting*
<r​brunner7> I think we should use the time to discuss dev related things.
<rottenwheel> +1
<r​brunner7> Meta-discussion about meetings should go, IMHO, in a new issue in -meta on GitHub
<o​frnxmr> Since were in dev, lets start with pressing dev matters.
<o​frnxmr> 1. We have to tag by wednesday
<0xfffc> +1
<r​brunner7> If people are ok with that, I can open such an issue later.
<r​brunner7> What is there to report from last week?
<o​frnxmr> Is everybody ready to tag, or are there any issues or PR's that need review or implementation asap
<r​brunner7> Can you please hold back for 5 minutes more, so we can get the usual overview who did what during the last week? Thanks.
<sech1> I'll release p2pool v4.1 today which needs to be included in monero-gui v0.18.3.4
<rottenwheel> +1
<strawberry> +1
<neromonero1024> +1
<o​frnxmr> +1
<dangerousfreedom> +1
<s​needlewoods> added missing functions to the API, now just TODO's and QUESTIONs to fix, I think I can see the finish line, but it will probably still take a while
<o​frnxmr> Sneedlewoods, this for what?
<o​frnxmr> Seraphis?
<j​berman> me: finalizing a draft PR + writeup for the fcmp++ integration, shooting to submit that PR by tomorrow. The PR so far includes a Rust FFI to use @kayabaNerve's fcmp++ crate, code to migrate existing cryptonote outputs into a merkle tree for fcmp++'s, growing the tree as the node syncs, an algo to trim the tree,  and changes to the `cryptonote::transaction` class for fcmp++. I plan to also implement tx construction & verification, and consensus changes in that PR
<rottenwheel> +1
<jeffro256> +1
<system> file df_draft_fcmp_v1.pdf too big to download (1184797 > allowed size: 1000000)
<jeffro256> +1
<d​angerousfreedom> df_draft_fcmp_v1.pdf
<d​angerousfreedom> This week I continued reading the code and theory of FCMP. I still don't understand the details of the circuits in the `prove` and `verify` functions and the exact details to fetch and store the tree in the database but I will improve my understanding with time since I'm much more familiar with the code and terms used. I believe it would be better to try to do something concrete n<clipped message>
<d​angerousfreedom> ow. Here is a draft of my understanding so far of some concepts. There may be big errors and imprecisions and it is still very shallow. Take it with a big grain of salt. I will improve it as I also improve my understanding.
<r​brunner7> @jberman: What will you PR against?
<j​effro256> me: polishing the carrot doc and soliciting auditors (I have one meeting planned thus far)
<j​berman> master in core Monero
<rbrunner7> +1
<rottenwheel> +1
<<o​frnxmr>> +1
<s​needlewoods> Also started to prepare my incoherent notes of things I found during the API work all over the place and plan to create a github issue for that. Not sure if I should put it into monero-project issues though, because it's a bunch and I don't think it makes sense to create a github issue for everything I found suspicous.
<r​brunner7> So much about "future stuff" :)
<0​xfffc> Me: since Wednesday I was reviewing different PR. The big one is reproducible build PR 8929. Which review is almost complete.
<<o​frnxmr>> +1
<tobtoht> +1
<o​frnxmr> off topic
rbrunner, dont bait me
<r​ottenwheel:kernal.eu> Will that go into a separate fcmp branch for the time being? Can't be marged on master till it's ready, no?
<o​frnxmr> You asked nicely to leave that discussion out of this meeting
<r​brunner7> Alright, understood.
<<o​frnxmr>> +1
<j​effro256> It could be merged but not activated
<o​frnxmr> Similar to some of koe's seraphis preparedness prs
<j​berman> @rottenwheel I'm thinking it could remain a WIP draft PR until it's ready
<<o​frnxmr>> +1
<rottenwheel> +1
<v​tnerd> Me: worked on socks v5 - adding ipv6 support to proxy requests. Also worked on LWS frontend API project
<r​brunner7> So soon people will be able to run their own LWS instances, are you nearing completion?
<o​frnxmr> They already can
<s​needlewoods> sorry ofrn, I'm slow, I think here you can get enough information what I'm working on in general https://github.com/monero-project/monero/pull/9368#issuecomment-2168451558
<v​tnerd> They are already able to run their own LWS instances, there just isn't many wallets supporting it because there's a decent amount of work to tx construction in particular
<r​brunner7> I see.
<v​tnerd> The LWS API is json, and is pretty straightforward I think
<0​xfffc> One important thing is the PR 9404 [1] needs reviewer. The PR has been running on stressnet with different scenarios. And no issues has been reported. With this PR, we have instantaneous start up.
<<o​frnxmr>> +1
<0​xfffc> 1. https://github.com/monero-project/monero/pull/9404
<endogenic> i've already done all that work
<endogenic> vtnerd and rbrunnner
<plowsof> thank you endogenic 
<endogenic> i've told you this a few times, but i havent ever been contavted by vtnerd
<endogenic> I told him a few times, but somehow we didn't end up being able to collaborate yet
<endogenic> The problem is that I haven't published it yet
<o​frnxmr> endogenic, show and tell
<endogenic> The only reason I haven't done that is because I don't have help
<endogenic> you say show it but what happens is that everyone else is just going to use my stuff before I get to actually launch my own product - this is just because I don't have any funding or any help from anyone
<endogenic> so it sounds a little bit like a Catch-22, but I swear that I have done all of the work already
<endogenic> it's directly from wallet2
<endogenic> i'm sure we can figure something out, but I literally am programming right now and I'm so close to releasing this stuff but I've just had to make it better because of the fact that all this other work is happening meaning I have to progress even further before I can release
<endogenic> so if we had worked together, then I think it would've been released already
<endogenic> it's just not fair to me either
<r​brunner7> Alright, looks like we are through with the reports. ofrnxmr , we have a pressing issue, tagging a new release?
<endogenic> it's actually been really difficult
<endogenic> to see this
<endogenic> geez so cold?
<o​frnxmr> yes. We have to tag the new release by wednesday
<v​tnerd> Is it in a private GitHub repo, or something completely offline?
<endogenic> me? vtnerd?
<endogenic> private repos
<endogenic> yes
<endogenic> long history
<endogenic> many commits
<r​brunner7> Pardon my ignorance, why do we *have* to tag? Would a long pause result if we don't?
<<o​frnxmr>> +1
<endogenic> i've been homeless at times.. and many other things no one would believe lol
<o​frnxmr> Im not sure about the reasoning dor 18.3.4, id have thought it should be 18.4.0 (?) Major minor patch, this isnt just a bugfix release.
<v​tnerd> Then just make it public, it's the least friction. Theres probably no shot at keeping it private, it's unlikely people will support private wallet code
<endogenic> I don't intend to keep it private at all
<endogenic> it's not intended to be private
<endogenic> it's just intended to be ready before it's released publicly
<endogenic> But it puts me at a major disadvantage to release all my work when everyone else has so much funding and help
<endogenic> especially because my work is actually pretty interesting
<endogenic> I have a huge write up..
<o​frnxmr> and selsta would be the one to ask about "why" wednesday, im just relaying the message
<r​brunner7> Ok, do we have @selsta around, they may have the best overview what is needed in order to tag.
<r​ottenwheel:kernal.eu> Endogenic has been delivering groundbreaking code since before the 2000s!
<endogenic> vtnerd would you be open to collaborating with me privately on the lws support for 2-3 weeks max? then it all goes public
<r​brunner7> Is anybody here right now directly involved in that release? With contributing PRs that may still not be re ready?
<r​ottenwheel:kernal.eu> He just hasn't been able because the life threats and lack of funding guys!
<endogenic> rottenwheel please, man, you're going to eat your words
<endogenic> you have no idea
<endogenic> what i have been through..
<o​frnxmr> endo, please ignore
<endogenic> lws support is done tbh
<endogenic> on my side
<r​brunner7> rottenwheel, @endogenic, maybe this special topic can wait until after this very meeting?
<rottenwheel> +1
<endogenic> i just need to update ny client for vtnerds new api
<endogenic> as you know he added spenda and recvs
<plowsof> i think it both a negative and positive we have duplicated efforts around endogenics area of work/expertise. neg being the dupl efforts, positive being we have more than 1 developer who understands the problem and can pick apart each others implementation. but i think we should leave it at that for this meeting unless it is on the agenda
<endogenic> this was one of the things I was going to announce
<o​frnxmr> create a private repo and invite vtnerd as collaborator?
<r​brunner7> Whatever does not derail this meeting. Please?
<endogenic> The only thing is that vtnerd might have confidentiality agreements, or he might not be willing to enter into a confidentiality agreement with me
<endogenic> that's why I was really trying to just launch everything
<endogenic> to be honest, honest with you, it's going to be trivial for me to update my client to work with vtnerds new api format
<endogenic> it's just that I was having a little bit of difficulty getting something compiling and stuff like this just takes more time
<r​brunner7> I don't have admin or any other special rights in here, by the way. If people insist on sabotaging this meeting, they will probably succeed.
<endogenic> there's no communication between me and him and so I can't just ask him about stuff
<endogenic> in other words, it's not like I'm paying him for his time so I don't feel comfortable asking him
<o​frnxmr> **Regarding the release** << are there any prs that anyone is trying to get into the release or issues that need to be resolved?
<endogenic> we've asked a lot from him already to be honest
<o​frnxmr> Plowsof has matrix ops
<j​effro256> vtnerd: sorry I meant to address your comments on https://github.com/monero-project/monero/pull/9135 earlier this week; thanks for the review. In your opinion after looking at the PR's code, once those issues are addressed, do you think it worth including in the next release?
<s​elsta> yes I'm around
<v​tnerd> jeffro256: I recall it being pretty much ready for inclusion
<o​frnxmr> This is running on stressnet, but were unsure if it caused an increase in reorgs (?) Rucknium:
<j​effro256> Btw that PR is running on the stressnet currently
<<o​frnxmr>> +1
<o​frnxmr> The reorg increase _may_ have been due to a very poorly connected miner though
<j​effro256> I was looking into this too, I *think* there were just more reorgs this time around, but I'm actively looking into it
<<o​frnxmr>> +1
<r​ucknium> ofrnxmr: jeffro256 These was an increase in re-orgs around the time that we put that PR into release, but other code was put in release, too. It's not a controlled experiment.
r​brunner7: nothing is needed anymore on the -cli side, but if something is ready and well reviewed we can include it with the next round of merges
18:27m-relay
<r​ucknium> And miner behavior isn't a controlled variable, either
18:27m-relay
<j​effro256> There were already mass reorg messages before, but they didn't feel *as* common. Of course, there's been a lot of variables changed with the new fork<r​brunner7> Alright, seems I am back on track.
<j​effro256> Sorry I keep duplicating people's thoughts delayed by 15 seconds lol
<j​effro256> I will compile a stressnet node without the PR and observer reorg behavior
<j​effro256> At any rate, it appears that the nodes are syncing just fine even with the increased messages
<r​brunner7> @jeffro: I also saw the reorgs with a stressnet daemon without your PR ...
<o​frnxmr> (Reorgs have calmed down a lot on both new and old stressnet)
<r​ucknium> New stressnet isn't being spammed yet FWIW.
<r​brunner7> Ok, looks like we have the release and the tagging sorted, yes? At least as far as meeting participants are concerned.
<sech1> gui is tagged separately?
<o​frnxmr> Rbrunner, spackle was having almost every block reorged. I hypothesise unrelate to jeffro's pr, and related to a poorly connected miner
<sech1> I still need to have p2pool v4 in the next gui release
<selsta> sech1: yes separately
<o​frnxmr> You had aksed "why wednesday", im not sure thats been answered
<o​frnxmr> I can only imagine luigi will be away for some time afterwards
<plowsof> proprietary 
<r​brunner7> Everything can run towards release without them after tagging? Surprises me a bit, but I don't know the details
<selsta> rbrunner7: yes, apart from the auto-updater
<r​brunner7> GitHub compiles, or people compile repeatable builds, and binaryfate signs and uploads?
<selsta> yes
<r​brunner7> Ok, nice.
<r​brunner7> Ok, hopefully news about the wednesday deadline will reach everybody
<0​xfffc> There is this one too ^.
<o​frnxmr> https://github.com/monero-project/monero/pull/9404 << for people on irc
<o​frnxmr> (0xfffc's reference)
<r​brunner7> You hope to have that reviewed and included until Wednesday?
<selsta> 9404 is a bit risky to include in this release in my opinion
<o​frnxmr> https://github.com/monero-project/monero/pull/9376
<o​frnxmr> This one as well
<0​xfffc> I am not hopeful about the “included” part.
<0​xfffc> I believe is safe to include. IMHO.
<j​berman> shooting to review 9404 this week. I can shoot to have it done by wed, but doesn't seem required for this release to me
<selsta> would be nice if 9376 gets a second review
<j​effro256> agreed
<selsta> including deep internal changes in the daemon last minute isn't good
<r​brunner7> I could have a look tomorrow at 9376
<<o​frnxmr>> +1
<o​frnxmr> 9376 has been running on stressnet for a while now and works as expected. Much. Much faster started speed when txpool is large
<r​brunner7> Yeah, if there is something wrong at all then maybe an unintended side effect, influence on something not yet thought about.
<r​brunner7> Ok. Do we have some other subject to discuss now? Is the dev here that, with their question, made the ball roll towards a broader dev-meeting? Something with binary stuff in JSON maybe?
<o​frnxmr> Yes
<r​brunner7> Do you have a pointer?
<o​frnxmr> rbrunners serialization / strings issue (he has a pr on stressnet) imho needs to be investigated and property implemented asap
<o​frnxmr> Block sync size + the serialization issue = problems that we dont want on mainnet
<r​brunner7> Yes, needs a taker, a dev with some free time on their hand. Which may be rare right now ...
<vthor_> rbunner7: well, I have extended monero-wallet-rpc with two endpoint for binary blob key image export/import, don't know if that fits here, and it would be cool if it could be included
<0​xfffc> ( Very important )
<r​brunner7> I think the connection is with cuprate
<r​ucknium> hinto hinto suggested the binary JSON-RPC deprecation
<o​frnxmr> We need to implement a dynamic BSS and/or need to fix the serialization / strings limitations
<vthor_> sorry, didn't want to disturb :/
<j​effro256> BSS
<j​effro256> ?
<r​brunner7> How many blocks to sync in one gulp
<o​frnxmr> bss= block sync size
<h​into> hello, yes the issue could maybe use more discussion from other devs although I think any approach within reason will be reasonable: https://github.com/monero-project/monero/issues/9422
<r​brunner7> Ah, ok, there is already an issue as a nice place to discuss. So just needs more eyes, and people opining :)
<h​into> I'm willing to make the changes to `monerod` although it may be faster if someone more familiar were to do it, at the very least I can review
<r​brunner7> Do we run into nasty coordinating proplems if we change that with clients that use these endpoints?
<h​into> jberman suggested deprecating the endpoints within 12 months, I'd assume they'd still work afterwards but are not recommended in documentation
<o​frnxmr> ((We also need to stop using words interchangeably, ie "block" and "ban". Dns blocklist, banlist, block size, block time (ban), block time (blocks) 
<o​frnxmr> block-sync-size really means "batch size"))
<r​brunner7> For the record, the issue that needs a competent dev for implementing a good longterm solution, about that "BSS" issue: https://github.com/spackle-xmr/monero/pull/12
<o​frnxmr> ^^ this is high priority imo
<0​xfffc> I can take this. The bandwidth efficient propagation will be delayed though
<rbrunner7> +1
<r​brunner7> If nobody finds time near- or mid-term, we could probably just go with what I did for a first quick fix, just rising those limits. After some testing whether it really does not blow up somewhere.
<j​effro256> Which limit type was actually hit in the stressnet case? Objects, fields, or strings?
<r​brunner7> Strings.
<o​frnxmr> We still have a max packet size of 100mb. If we were to play it safe, we should mimic stressnet and change bss  from 20 > 5 and implement rbrunners suggestion. 
<o​frnxmr> but neither of those is a long term solution
<r​brunner7> At least. But I did not rise the limits one-by-one.
<0​xfffc> ( multiple limitations at play here )
<o​frnxmr> strings was the error that 0xfffc's debugger showed
<r​ucknium> 0xfffc: IMHO it makes sense for you to try to solve the BSS issue. The efficient tx propagation proposal has some privacy issues that the dev & researcher community may want to discuss more.
<o​frnxmr> Simply raising serialization limits can eventually also hit the packet size limit. 
<o​frnxmr> dynamic bss is best solution to the static bss=20 imo
<r​ucknium> And the current stressnet will last for about two months longer
<r​ucknium> This is the efficient tx propagation issue: https://github.com/monero-project/monero/issues/9334
<0​xfffc> I am all ears. If community thinks this is more important. I will switch immediately.
<o​frnxmr> Unrestricted rpc will fail to connect when txpool > 100mb
<o​frnxmr> Restricted batches rpc calls into 100tx/call. We need to fix this for unrestricted rpc jberman @jberman:
<r​brunner7> Hmm, gut feeling tells me that this efficient tx propagation thing might take quite a while to get merge-ready, maybe really a good idea to attack that BSS issue first.
<r​brunner7> And well, it may take a while until we have the next spam wave, or organic traffic in stressnet amounts
<0​xfffc> Sure. Then I am switching to fixing serialization limit right now. ( will go back to bandwidth efficient propagation after that )
<o​frnxmr> bss or serialization?
<r​brunner7> Splendid!
<0​xfffc> Serialization will be easier to attack at first IMHO. What do you guys think? Which one we should start with?
<o​frnxmr> Serialization only helps up to 5mb blocks
<0​xfffc> Keep in mind the multiple limitations 👆🏻
<o​frnxmr> Bss can be reduced to 5 (like stressnet) to add a stop-gap measure
<0​xfffc> My impression was we hit the serialization first.
<o​frnxmr> But dynamic bss is a better solution (which would allow <=100mb blocks)
<0​xfffc> So it is better to start from the bottleneck.
<r​brunner7> In my understanding things are linked. With a good algorithm to dynamically adjust BSS to traffic and block sizes the serialization limits are not that critical, and we can stay with relatively low "sanity checks"
<o​frnxmr> Yes. We hit serialization at 1.5mb blocks
<o​frnxmr> after Fixing serialition, we hit packet at 5mb blocks
<o​frnxmr> If dynamic bss, we hit serialization at 30mb blocks
<o​frnxmr> After fixing serialization + dynamic bss, we hit packet at 100mb blocks
<r​brunner7> Alright, 0xfffc , I think things will clear up as soon as you wrap your head around the hole story :)
<r​brunner7> *whole story
<0​xfffc> ( So in every case we hit serialization limitation. )
<o​frnxmr> No
<0​xfffc> But rbrunner7 thinks the dynamic bss is more important than serialization limit.
<o​frnxmr> The final boss is packet
<0​xfffc> That is the monster at the end of story :))
<j​berman> this likely needs testing, but just changing `std::numeric_limits<size_t>::max()` to something sane like 1000 may be fine here:  https://github.com/monero-project/monero/blob/caa62bc9ea1c5f2ffe3ffa440ad230e1de509bfd/src/rpc/core_rpc_server.cpp#L660
<o​frnxmr> right, bss gets us further (to 30mb blocks) than serialization (5mb blocks)
<j​berman> it shouldn't break wallet2, but could break other clients that rely on it
<o​frnxmr> This was my suggestion (1000 = 100kb(max block size) * 1000 = below the packet size limit)
<0​xfffc> Important point: all of those limitations need to be fixed. Let me review each of them. We debugged it once. 
<0​xfffc> Start from the compromise of (simpler + more important)
<o​frnxmr> "this" = changing the max tx pull to <1000
<k​ayabanerve> ofrnxmr: FCMP is not 12m away. We're looking at a PR for a lot of the framework within the next few weeks. Academia is also near complete, and a variety of the libraries are about to head to auditing.
<j​effro256> 100mb packet probably doesn't need to be touched
<o​frnxmr> To mainnet?
<o​frnxmr> Kaya
<k​ayabanerve> The moment that PR is open, it's monero-dev.
<0​xfffc> I agree. If we have good dynamic bss algorithm. 100mb should be more than important.
<0​xfffc> s/important/enough/
<j​effro256> IMO 0xfffc your time would be really well spent reviewing vtnerd's serialization library changes since those changes would make the limits less important since the serializer is inherently more efficient, and parsing rogue messages is less of a risk
<k​ayabanerve> jeffro256: Happy to help with auditors :) Feel free to reach out.
<jeffro256> +1
<0​xfffc> Great suggestion. I think I have missed those PRs. What was the number?
<j​berman> I think all fcmp integration code (not including reproducible build-related) in the monero repo can be completed within 4 months
<k​ayabanerve> Re: RPC method deprecation, given how FCMP++ will change the definition of the output distribution (it's a new pool superseding all others) and TX creation code, do we want to take advantage of the amount of changes to argue hard breaks on other methods? Deprecate prior to HF, remove entirely with the bin that HFs?
<j​effro256> Here the PR for the overall tracking: https://github.com/monero-project/monero/pull/8867. Here's the currently opened piecemeal PR: https://github.com/monero-project/monero/pull/8970
<k​ayabanerve> I'd hope for mainnet within a year, ofrnxmr.
<k​ayabanerve> Sorry for not being present earlier and responding to what's relevant on my end now.
<j​effro256> It's a pretty huge task, but replacing the DOM serialization, especially for large funky messages, will help DoS mitigation a lot
<o​frnxmr> Isnt this 7999 redux?
<0​xfffc> Great. Well before the time I joined monero community. I was not aware of these. Thanks for mentioning.
<0​xfffc> Just the final question. I am between two tasks right now. Fixing out serialization limit, or reviewing vtnerd serialization PR. 
<0​xfffc> Which one I should tackle?
<j​effro256> https://github.com/monero-project/monero/pull/7999#issuecomment-938098462
<j​berman> Full wallets shouldn't need an RPC route for anything like getting the output distribution at all (only light wallets should need to fetch decoy paths), but generally ya the get_output_distribution endpoint can be set to be deprecated in theory when fcmp's are required, and that is a better deprecation timeline we can aim for
<o​frnxmr> Jbernan, thoughts on 7999 vs 8867?
<k​ayabanerve> jberman: we still need decoy requests for paths, as you say. How does that enable deprecating getting the output distribution?
<k​ayabanerve> My comment was how if we're already making notable changes necessary for practical operation, we can also make breaking changes and provide a single migration guide (instead of two releases with such notable changes).
<j​effro256> I really don't see the point in removing the `get_output_distribution` RPC method (even the "broken" JSON one) since it *works* now for the custom JSON parser, and doesn't really affect other code in the codebase
<k​ayabanerve> The broken JSON one is a sin, it should be removed ASAP.
<j​effro256> Obviously I see the value of *also* having a JSON compliant endpoint
<j​effro256> I disagree. Current services depend on it, and removing it for the sake of removing is just annoying to people building things in Monero
<k​ayabanerve> We should not have an endpoint which is fundamentally broken to its definition.
<j​berman> 8867 seems like it would be fine compared to 7999 for those reasons. If it solves the issue presented in the PR, then fine with me. Would be curious to see how it performs relative to 7999 too
<r​brunner7> Alright. We are well past the hour. Allow me to close the meeting proper while the detailed discussions about serialization and other things go on of course. Thanks everybody for attending, read you again in 1 week, place to be decided.
<k​ayabanerve> It claims to be JSON. It is not. It at least needs to be made hex.
<0​xfffc> I have feeling we have opened a can of worms. 
<0​xfffc> ( 7999 vs 8867 vs fixing serialization limit )
<o​frnxmr> 7999 vs 8867 can was opened 2+yrs ago
<k​ayabanerve> Also, it's unclear how to parse it with a custom parser. It isn't spec compliant? Is its binary guaranteed to not to have instances of "? Are some sequences unrepresentable?
<s​needlewoods> thank you everyone, seems there are enough topics to justify a dev-meeting
<k​ayabanerve> If it's not spec compliant, it's not properly documented, and it's quite possibly incomplete, it needs revamping.
<0​xfffc> I belie we can use the serialization as standalone library. Why not write a benchmark suite, and winner takes all.
<o​frnxmr> SNeedlewoods @sneedlewoods:  i was never against a dev meeting, ftr
<j​berman> hinto's proposal I believe to keep the code so it continues to function as is, and mentioning it's deprecated in documentation seems fine to me
<0​xfffc> Not gonna lie. -dev meeting was more interactive :))
<h​into> If FCMP++ breaks the endpoint semantics anyway, can't it stay until post HF, then be removed afterwards?
<j​effro256> A benchmark shouldn't be the ONLY factor, since readability and maintainability is also important for open-source health
<j​berman> I see, ya, merging timelines with fcmp's make sense on that front
<j​effro256> FCMP++ doesn't inherently break `get_output_distribution` semantics though
<0​xfffc> At least it is an objective starting point though.
````


# Action History
- Created by: rbrunner7 | 2024-08-09T14:33:50+00:00
- Closed at: 2024-08-12T19:46:30+00:00
