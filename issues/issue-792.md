---
title: 'Seraphis wallet workgroup meeting #12 - Monday, 2023-02-06, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/792
author: rbrunner7
assignees: []
labels: []
created_at: '2023-02-03T15:36:18+00:00'
updated_at: '2023-02-13T00:12:21+00:00'
type: issue
status: closed
closed_at: '2023-02-13T00:12:21+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #787 

No proposal yet from my side what to discuss. Feel free to propose a subject. With already quite some dev work going on, maybe we can also already meet and discuss things "on the go" like in the MRL meetings.

# Discussion History
## rbrunner7 | 2023-02-06T19:15:55+00:00
```
<rbrunner7[m]1> Meeting time. Hello! Who is around?
<one-horse-wagon[> Hello.
<rbrunner7[m]1> https://github.com/monero-project/meta/issues/792
<plowsof11> hi
<Rucknium[m]> Hi
<jeffro256[m]> Howdy
<UkoeHB> hi
<JoshBabb[m]1> heya
<dangerousfreedom> Hello
<jberman[m]> hello
<rbrunner7[m]1> Nice, many people around. Anything to report about work done last week?
<rbrunner7[m]1> I myself wrote 2 new issues to document 2 possible dev tasks. I posted about them yesterday.
<rbrunner7[m]1> And I made the Seraphis and Jamtis FAQ public: https://old.reddit.com/r/Monero/comments/10ug1zt/seraphis_and_jamtis_faq/
<jeffro256[m]> This is old wallet related, but I opened a PR which drops support for the pay-to-use RPC system. The PR doesn't require much detailed wallet knowledge to review, but it is quite large (>1000 lines). I would appreciate reviewers. 
<jeffro256[m]> https://github.com/monero-project/monero/pull/8724
<rbrunner7[m]1> Saw it. That was fast, after discussion showed consensus to drop it ...
<jeffro256[m]> Also built another wallet PR on top of that PR which simplifies and centralizes wallet connection code https://github.com/monero-project/monero/pull/8734. This is all working towards the community node feature 
<UkoeHB> I spent all last week thinking about how to build async architectures. Now I'm basically satisfied with my understanding and next plan to write a threadpool (with several improvement over what we have now) + finish my task-builder toolkit. After that stuff gets out of my head I will do my pending seraphis library tasks and then maybe get started on the papers.
<blankpage[m]> Other than lack of adoption, what are the motivations for removing pay to use RPC?
<UkoeHB> jeffro256[m]: nice to see some wallet2 cleanup
<blankpage[m]> And how does removing it relate to seraphis?
<UkoeHB> blankpage[m]: https://github.com/monero-project/monero/issues/8722
<blankpage[m]> Thanks will read
<jeffro256[m]> > Other than lack of adoption, what are the motivations for removing pay to use RPC?
<jeffro256[m]> Makes wallet development much harder. Clearing out the code to keep up with that system simplifies wallet2 connection code a lot and makes new connection modes much easier  
<plowsof11> rbrunner7 if those 2 tasks could be put into a bounty (along with koes todo list), that would be great. i could add a "seraphis" tag the the bounties site (for easy sorting). the bounty that josh babb has started is already up to 6~xmr https://bounties.monero.social/posts/75/6-013m-blake2b-c-dev-challenge-seraphis
<dangerousfreedom> I prepared a quite big text... here you are:... (Two things from my side:

1. I made a very basic wallet [prototype](https://github.com/DangerousFreedom1984/seraphis_lib/compare/seraphis_lib...DangerousFreedom1984:seraphis_lib:prototype_wallet3_v1?expand=1#diff-37c927be1f864827d935fc08b48cb1becd596e00de8e9ac0debfd8485ed76acb) with the following functions: load/save a seraphis wallet (using the skeleton of wallet2), making a transaction and updating the balance using the mock seraphis functions and providing a scheme to store/load different wallet tiers. (Of course, this is only a prototype to hopefully serve as a concrete base for discussions. I dont expect any of these functions to be on the 'final' wallet version as a lot of clean up and design decisions have to be made.)

2. I believe I finished my CCS and I wrote a small report that I will publish soon. Now basically I would like to open three discussions that I would like to investigate further in another CCS that I will be writing this week.

i) Up to now I used the skeleton of wallet2 to understand and build the minimal functions to operate a wallet for jamtis/seraphis. The problem is that the current wallet has a monolithic design where basically all the functions are on wallet2.\* and simplewallet.\* files. I'm not sure that this design choice is optimized though. I have some ideas about how to go from here but would be great if we could achieve a consensus here as I believe nobody holds the truth for this matter.

ii) The most important crypto stuff going on in the wallet is the password hashing. Currently Monero uses the Cryptonight hash (cn\_slow\_hash) to feed the chacha algo to encrypt the wallets. I don't think it is unsafe but is it still the best choice? Since tevador  brought Argon2 to randomx I believe we should really consider moving to Argon2 as it is definitely safer than Cryptonight. So I would like to investigate the best parameters for it. What are your thoughts @tevador and UkoeHB ?
@tevador, just out of curiosity, what was the rationale to come up with randomx? Did you pick from Cryptonight the idea of changing algorithms plus the idea of memory-hard functions from Argon2 and came up with it? Can you say a few words about that?

iii) Regarding the [discussion](https://github.com/seraphis-migration/wallet3/issues/32) initiated by @rbrunner, I'm still not sure if dividing the different wallet tiers by classes is the optimal solution. Maybe saving the unused/unwanted private keys as zero is more efficient and scalable. It seems the best solution to me for now (I made a [prototype](https://github.com/DangerousFreedom1984/seraphis_lib/compare/seraphis_lib...DangerousFreedom1984:seraphis_lib:prototype_wallet3_v1?expand=1#diff-23dd7512c6fe57ae7eba1ab104958b091968b6c4ee52c67a0ddd9dd2dfec8d75R281) to store/load a view-balance wallet too and we could do something like that for all the wallet tiers). I can further explain it in another topic.

<jeffro256[m]> > And how does removing it relate to seraphis?
<jeffro256[m]> Doesn't really, but I remember someone mentioned that Seraphis wallets should drop it too
<jeffro256[m]> > I spent all last week thinking about how to build async architectures. Now I'm basically satisfied with my understanding and next plan to write a threadpool (with several improvement over what we have now) + finish my task-builder toolkit. After that stuff gets out of my head I will do my pending seraphis library tasks and then maybe get started on the papers.
<jeffro256[m]> Do you plan to use boost::asio? Might be easier than writing your own async threadpool
<UkoeHB> less things for seraphis wallets to implement, the better
<UkoeHB> jeffro256[m]: no, it sounds like boost::asio is not a tasking system which is what I want
<UkoeHB> can learn more here: https://www.youtube.com/watch?v=zULU6Hhp42w
<rbrunner7[m]1> Yes, but I do wonder what work to put into wallet2 is still sensible and what aspects we could endure without problems until we throw the whole sorry thing away ...
<jberman[m]> my update: as reported the other day, this multithreaded scanner impl that uses the Seraphis lib + points to a daemon + recovers the balance of a mainnet wallet is clocking in ~5-10% faster than wallet2: https://github.com/j-berman/monero-cpp/blob/36f9524d2b46074a30ec0c7168a2c59eee1a4afe/src/utils/monero_utils.cpp#L1199
<UkoeHB> rbrunner7[m]1: people are still using and building on monero
<jberman[m]> UkoeHB:  gave me a review on that code^^, which I'm going through today. I'm also planning to 1) handle pre-RCT scanning in that impl, 2) correctly handle reorgs (as the Seraphis lib expects), 3) use that code to demonstrate/document exactly how devs can utilize the Seraphis lib to scan the chain
<rbrunner7[m]1> I am thinking about work internal to wallet2, like deleting things, structuring things in a better way, etc. That does not immediately manifest itself to the outside world
<jeffro256[m]> > The problem is that the current wallet has a monolithic design where basically all the functions are on wallet2.\* and simplewallet.\* files. I'm not sure that this design choice is optimized though. I have some ideas about how to go from here but would be great if we could achieve a consensus here as I believe nobody holds the truth for this matter.
<UkoeHB> jberman[m]: I think the current enote scanning code can be refactored as an abstract state machine that both the enote store and scanning backends can implement. Not a trivial task but possible
<jeffro256[m]> dangerousfreedom[m] UkoeHB will know more about this but, the seraphis scanning should be designed in such a way to be more functional
<UkoeHB> rbrunner7[m]1: if anything it makes it easier to grok what exactly wallet2 does
<UkoeHB> if nothing else*
<jeffro256[m]> > I am thinking about work internal to `wallet2`, like deleting things, structuring things in a better way, etc. That does not immediately manifest itself to the outside world
<jeffro256[m]> That specific PR I linked does not affect behavior, but I have a PR planned which depends on that PR which actually does use those changes to make real features possible 
<jeffro256[m]> > UkoeHB:  gave me a review on that code^^, which I'm going through today. I'm also planning to 1) handle pre-RCT scanning in that impl, 2) correctly handle reorgs (as the Seraphis lib expects), 3) use that code to demonstrate/document exactly how devs can utilize the Seraphis lib to scan the chain
<jeffro256[m]> For curiosity, how are you planning on handling reorgs? Is it more or less similar to wallet2?
<ghostway[m]> <rbrunner7[m]1> "Meeting time. Hello! Who is..." <- Greetings
<shalit[m]> Hello
<jberman[m]> UkoeHB: agree
<jeffro256[m]> UkoeHB in the same vein that you were talking about yesterday regarding the http client inside the codebase, do you plan to keep using that http client in EPEE or use something else? Using libcurl could be very beneficial for SSL compatibility and TCP session compatibility. It would likely make requests more reliable 
<UkoeHB> dangerousfreedom: I have set a goal that the seraphis wallet engine (I use the word engine intentionally) should be able to concurrently operate at least 2x as many wallets as there are cores on a given machine running it. This means a monolithic design is completely a no-go.
<rbrunner7[m]1> I think nobody really started to work on connections to daemons in earnest yet, right?
<dangerousfreedom> UkoeHB: Totally agree.
<jeffro256[m]> dangerousfreedom[m] are you editing your message? It keeps showing up as a new message each time for my client
<ghostway[m]> UkoeHB: That's cool
<ghostway[m]> jeffro256[m]: For me as well
<UkoeHB> jeffro256[m]: if there is a reorg then you rewind until you find a block that is contiguous with your known blocks
<rbrunner7[m]1> Same here, yeah. It's there in Matrix now 3 times ...
<dangerousfreedom> I'm using a thread for the background command (like in the current wallet) but it should definitely use more threads... 
<dangerousfreedom> Oh sorry, yeah I edited 3 times to tag Koe and Tevador
<UkoeHB> dangerousfreedom: it also has to support running with exactly one thread (and no std::thread)
<jberman[m]> jeffro256: the seraphis lib handles reorgs internally already by keeping track of scanned block id's; if there is a misalignment between already scanned block id's and the daemon's reported block id, it should pop and rescan from the misaligned height. I don't really anticipate much work on my end for this as most of it is already done in the seraphis lib. I just didn't focus on it on my end while getting the multithreaded
<jberman[m]> structure set up
<UkoeHB> so background threads are also a no-go (hence why I want a tasking system)
<jeffro256[m]> Well yes... So is there a tools::blockchain like class which contains a list of block hashes? And are the transfer details tied to a certain block hash like in wallet2?
<UkoeHB> dangerousfreedom: your message is converted into a link, which is not picked up by IRC for tagging
<jeffro256[m]> jberman Thanks, I guess I should just go look at the code myself for details. I don't think my question made much sense 
<rbrunner7[m]1> By the way, there was something that I see as an important development that people might have missed. I allow myself to cite, UkoeHB wrote at the end of Wednesday's MRL meeting: "Fortunately or unfortunately, it seems I will be spending a lot more time on seraphis migration than I originally planned, since it looks like there is a lot of advanced architectural work that A) interests me, B) probably needs my help. Not sure
<rbrunner7[m]1> how much actual wallet-level code I'll write, but we'll see how it goes."
<blankpage[m]> dangerousfreedom[m]:  your question about the genesis of randomx: it originally started as randomJS
<blankpage[m]>  https://github.com/tevador/RandomJS 
<blankpage[m]> There is lots of discussion in that github and in the randomx github
<dangerousfreedom> For me nothing of that happened I just see one message (which I modified). Sorry wont modify again.
<rbrunner7[m]1> Might probably mean that ambitions also take some jumps up, with koe as a main architect :)
<rbrunner7[m]1> Will certainly get interesting.
<dangerousfreedom> > <@blankpage[m]:libera.chat> dangerousfreedom[m]:  your question about the genesis of randomx: it originally started as randomJS...
Thanks. I read some :)
<UkoeHB> sgp[m]: does AV flag cn_slow_hash as malware (old cryptonote pow hash algo)?
<rbrunner7[m]1> I would say it's not sure what exactly they flag. Seems pretty obscure to me sometimes, and maybe is not identical over all AV products
<rbrunner7[m]1> (It almost must be obscure, otherwise scanning would be too easy to circumvent by the bad people ...)
<jeffro256[m]> @dangerousfreedom The safest way to do password hashing would be to use an already made password hashing library which uses salts and multiple rounds of 1 very secure hashing function (preferably SHA3)
<UkoeHB> I guess it would be hard to remove cn_slow_hash as a dependency considering it's embedded in the current repo
<jeffro256[m]> Not that cn_slow_hash is unsafe, but it's not the best way to do password hashing. Other methods are more rigorously verified for security 
<rbrunner7[m]1> If that's it more or less about reports, I have something that bugs me a bit, and where I would like to hear what people think. It's about bounties.
<dangerousfreedom> jeffro256[m]: I'm not sure about that. First would be better to use some code that is already implemented. Second Argon2 is the best option.
<blankpage[m]> I wonder if they are using some version of this randomx detector
<blankpage[m]>  https://github.com/tevador/randomx-sniffer
<UkoeHB> I recommend we don't go overkill on adding things like new hashing algos that have no practical benefits.
<jeffro256[m]> We already have keccak, we could use multiple rounds of that 
<dangerousfreedom> jeffro256[m]: Yeah. That's what I wrote in my opinion.
<jberman[m]> Right UkoeHB , we would still need to read the old password hashed keys so we can't get rid of cn_slow_hash entirely
<jberman[m]> password encrypted*
<dangerousfreedom> Apparently people changed Cryptonight for a reason right?
<dangerousfreedom> What if people bruteforce a wallet?
<UkoeHB> argon2 may be in randomx, but it is not linkable from monero code so you'd have to copy in the files like what I did for blake2b
<UkoeHB> it was changed for ASIC resistance
<dangerousfreedom> I think would be nice if we have some discussion about it as it seems to me that there is a lot of room for improvement here
<dangerousfreedom> UkoeHB: Exactly
<one-horse-wagon[> dangerousfreedom[m]: That's practically impossible to do, is it not?
<UkoeHB> argon2 is also not asic resistance, otherwise we'd just use argon2 an not have randomx
<rbrunner7[m]1> Depends of course on the password
<UkoeHB> resistant*
<dangerousfreedom> The idea is to make something slow and use a lot of memory
<one-horse-wagon[> rbrunner7[m]1: I was thinking of the 25 word seed phrase.
<rbrunner7[m]1> Wallet file content encryption is something else
<rbrunner7[m]1> IMHO if it's not broken, don't fix it. I think the way we do it now is plenty secure enough.
<rbrunner7[m]1> And well, any hours we put into improving this could go into building of wallet proper ...
<UkoeHB> agreed
<jberman[m]> +1 this^ we're still going to need the current implementation in a future wallet anyway
<dangerousfreedom> I think we should deprecate cryptonight once for all when we move to seraphis
<rbrunner7[m]1> At least the capability to read wallet files, at least in part, yes
<rbrunner7[m]1> ... which probably is not possible ...
<dangerousfreedom> Yes, the code will always be there but we I dont think we should propagate it
<rbrunner7[m]1> We have now some new hashes available, don't we? Take one that does the job, probably?
<sgp[m]> <UkoeHB> "sgp: does AV flag cn_slow_hash..." <- I honestly don't know
<sgp[m]> My guess is probably
<dangerousfreedom> argon2 was the winner for password hashing so... there is a lot of reasons to use it
<jberman[m]> I agree that argon2 is the ideal choice here and there would likely be a practical benefit for shorter passwords. But I don't think changing the password key derivation function should take priority relative to other tasks to move Seraphis/Jamtis/a new wallet forward
<UkoeHB> it can be easily subbed in later as needed
<jberman[m]> yes^
<UkoeHB> assuming the code is well-factored
<dangerousfreedom> jberman[m]: Well, yeah, it will become a priority soon :p
<UkoeHB> it doesn't need to be decided until the late stages of finalizing wallet file format
<rbrunner7[m]1> Not sure I really follow. We could all play around even with unencrypted prototype wallet files for months to come, that will become important later
<blankpage[m]> It would be nice if things were built in a way so that some future monero community can eventually ditch the entire pre-seraphis history and code (e.g. in 10 years or something with plenty of warning) if they were so inclined. That is almost definitely controversial and outside of scope though.
<one-horse-wagon[> rbrunner7: What were you thinking about when you mentioned you "were not sure about bounties"?
<dangerousfreedom> Yeah, true.
<jberman[m]> this is making me think a nice task would be to factor out reading the current wallet file format from wallet2 so that reading current wallet files is reusable elsewhere
<rbrunner7[m]1> one-horse-wagon: Not terribly important, maybe we run out of time today, and I will bring it up next week
<UkoeHB> jberman[m]: agree
<rbrunner7[m]1> jberman: Yeah, that thought already crossed my mind, just did not see it as a nice separate task that possibly somebody could pick up
<rbrunner7[m]1> Until now :)
<UkoeHB> blankpage[m]: for what we are doing, legacy needs to be supported indefinitely so funds can always be recovered.
<UkoeHB> recovered and spent*
<rbrunner7[m]1> And yes, completely independent from wallet2 itself
<dangerousfreedom> That would be useful.
<blankpage[m]> I am talking about a future where people might decide they are happy for funds to not always be recoverable, in exchange for some scalability by resolving the infinitely growing chain. That is why I mentioned it is probably too controversial. 
<dangerousfreedom> Anyway it is just one function
<UkoeHB> blankpage[m]: the core software can never prune legacy, it's just not feasible. Third-party software is free to do what it wants.
<jberman[m]> there's all the serialization/data types in the wallet cache that would be nice to pull out into something independent from wallet2 too so it can be reused
<jberman[m]> not just encryption/decryption
<jeffro256[m]> I could start working on that since I have recently familarized myself with wallet2 serialization recently 
<rbrunner7[m]1> Sounds good to me, in principle. Might need some more thinking beforehand what we really need for Seraphis, but much.
<rbrunner7[m]1> *but not much
<jberman[m]> I think a solid end goal is the ability to read current wallet keys + wallet cache files in contained code independent from wallet2 that can be reused by another lib. Factoring wallet2 to reuse that would maybe be nice, but would probably also be a ton of code to review for not huge benefit. Worth exploring but not necessarily being the main goal imo
<rbrunner7[m]1> Yes, I think we really should only change something fundamental there only if we really must, so some amount of code duplication should be not too big a problem.
<rbrunner7[m]1> It may not look nice, but ...
<UkoeHB> jberman[m]: I think eventually that code should be used as part of a wallet file migration path.
<dangerousfreedom> Yeah, I'm still trying to gather all the requirements. I could keep going on and on and adding a lot of functions on top of this wallet3 with a wallet2 skeleton but it is definitely not what we want. I will come to the basis again as we are talking about threads and try to make a cleaner prototype. 
<rbrunner7[m]1> Er .. isn't that the whole motivation for this work?
<jberman[m]> agree
<UkoeHB> it should support that as a design requirement*
<UkoeHB> rbrunner7[m]1: yes but it needs to be stated explicitly
<rbrunner7[m]1> Alright
<dangerousfreedom> Haha yeah
<rbrunner7[m]1> We could put it into the Seraphis code tree to hammer the point home?
<rbrunner7[m]1> Hmm, not sure, might have drawbacks, that way nobody could use it ... but maybe we don't want anybody else than the Seraphis wallet using it.
<rbrunner7[m]1> Sleep one night over it, and things will clear up :)
<UkoeHB> doesn't need to be in seraphis code
<rbrunner7[m]1> Alright, the hour is full. Anything that somebody really wants to bring up today still, while we are all here? If not, we can close.
<rbrunner7[m]1> Nice to see how things pick up speed now. We are a big team already.
<rbrunner7[m]1> Thanks everybody for the interesting discussion.
```


# Action History
- Created by: rbrunner7 | 2023-02-03T15:36:18+00:00
- Closed at: 2023-02-13T00:12:21+00:00
