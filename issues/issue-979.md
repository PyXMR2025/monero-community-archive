---
title: 'Monero Community Workgroup Meeting: Saturday 16th March 15:00UTC'
source_url: https://github.com/monero-project/meta/issues/979
author: plowsof
assignees: []
labels: []
created_at: '2024-03-14T08:36:42+00:00'
updated_at: '2024-03-29T08:56:19+00:00'
type: issue
status: closed
closed_at: '2024-03-29T08:56:19+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
15:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights 
    - Monero core/gui point release soon
    - Featherwallet 2.6.5 released https://featherwallet.org/changelog/
    - Recent bump in block sizes https://bitinfocharts.com/comparison/monero-size.html#3m Automatic fee has been fixed to go between normal/low depending on mempool status. there is also a new PR to allow miners to limit block weights [here](https://github.com/monero-project/monero/pull/9234) from sech1, suggested by Rucknium
    - XMR-BCH Atomic swap update [Nitter](https://nitter.privacydev.net/mainnet_pat/status/1767641618918633669) / [X](https://twiiit.com/mainnet_pat/status/1767641618918633669)  
    - https://github.com/monero-project/monero-docs 
    - SNeedleWoods add LegacyEnoteOriginContext for Seraphis [pull request](https://github.com/seraphis-migration/monero/pull/16#issue-2026817626)
    - cats with jobs [copyCat](https://github.com/monero-project/monero/pull/9252/commits)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)    | [hinto](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422#note_23548) | [tobtoht](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/428#note_23555)
  a. [Unnamed Monero Wallet development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/437)    
  b. Payout request for monero-gui flathub proposal [comment](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/381#note_23554) 
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2024](https://monerokon.org/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/974)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2024-03-17T15:57:04+00:00
Logs 
> __< p​lowsof:matrix.org >__ Greetings https://github.com/monero-project/meta/issues/979     

> __< d​iego:cypherstack.com >__ Please do. Would be thrilled.     

> __< p​lowsof:matrix.org >__ may i ask Diego Salazar if the cypherstack bp++ 1st payment is being handled/handled?     

> __< d​iego:cypherstack.com >__ Yes it was. Thanks.     

> __< p​lowsof:matrix.org >__ thanks for confirming and success further!     

> __< r​ucknium:monero.social >__ Hi     

> __< p​lowsof:matrix.org >__ i suppose the biggest highlight of the prev 2 weeks has been the transaction spam* and the resulting discussions (ongoing)     

> __< p​lowsof:matrix.org >__ Recent bump in block sizes https://bitinfocharts.com/comparison/monero-size.html#3m Automatic fee has been fixed to go between normal/low depending on mempool status. there is also a new PR to allow miners to limit block weights [here](https://github.com/monero-project/monero/pull/9234) from sech1, suggested by Rucknium     

> __< p​lowsof:matrix.org >__ hi Rucknium, did you mention having second thoughts about the idea? or?     

> __< m​ichael:monero.social >__ Hello.     

> __< r​4v3r23:monero.social >__ yo     

> __< p​lowsof:matrix.org >__ hi     

> __< r​ucknium:monero.social >__ Miners self-limiting the size of blocks they produce? No second thoughts about adding the parameter to `get_block_template`. We don't know yet if it is  a good idea to suggest that miners actually set the param lower.     

> __< p​lowsof:matrix.org >__ ah thanks for clarifying     

> __< p​lowsof:matrix.org >__ its a shame the -events cfp has ended, maybe some talks reg the recent transaction spam could be submitted (if not already ajs_?)     

> __< nioCat >__ it's a soft deadline     

> __< p​lowsof:matrix.org >__ hello, we have a cat working for us now. she updates the copyright dates every year [copyCat](https://github.com/monero-project/monero/pull/9252/commits)     

> __< nioCat >__ articmine has submitted a talk about changes to the dynamic block protocol      

> __< nioCat >__ now back to laundry     

> __< p​lowsof:matrix.org >__ awesome, thanks!     

> __< r​ucknium:monero.social >__ IIRC, you are only supposed to update the copyright year on files that have actually been edited in that year.     

> __< nioCat >__ *including fees     

> __< p​lowsof:matrix.org >__ https://featherwallet.org/changelog/ tobtoht has been pushing out new versions 👍️ selsta says we are waiting for bF's availability to release 18.3.3 (thank you to the Gitian builders/signers!) https://github.com/monero-project/gitian.sigs     

> __< p​lowsof:matrix.org >__ seems sane Rucknium reg copyright changes, im not even sure updating that date even means anything but the core repo gets several pull requests a year of people updating them     

> __< p​lowsof:matrix.org >__ there was even an open invitation for contributors to update it posted on reddit     

> __< a​js_:matrix.org >__ CFP deadline ended yesterday, but we might still accept additional talks depending on space availability     

> __< p​lowsof:matrix.org >__ https://www.reddit.com/r/Monero/comments/1bellkj/update_github_dates_to_2024/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button     

> __< p​lowsof:matrix.org >__ events team has ALOT of updates regarding sponsor payments and other misc things. TheFuzzStone has been offering advice on how to get fiat / cash invoices paid for monerokon (while a bank account is in the workings) - one advice though, please confirm the minimum amounts with TheFuzzStone and do not under any circumstances joke about them !     

> __< p​lowsof:matrix.org >__ - https://github.com/monero-project/monero-docs     

> __< p​lowsof:matrix.org >__ sgp has set up getmonero.dev , which is a fork of https://github.com/monerodocs/md     

> __< p​lowsof:matrix.org >__ dan shared that the underlying tech is mkdocs @ https://github.com/mkdocs/mkdocs     

> __< p​lowsof:matrix.org >__ does anyone have any input on this?     

> __< r​ucknium:monero.social >__ We need to figure out domain ownership dead man switches. If they are possible somehow.     

> __< m​rcyjanek0:matrix.org >__ Very good idea, some technical introduction regarding how to build things that use monero's codebase would be good (I'm willing to contribute that), because it is quite easy to become lost when trying to use the codebase for first time.     

> __< m​rcyjanek0:matrix.org >__ So not only cli/rpc/gui docs but also wallet2_api.h and possibly libraries for other languages (rpc clients, and ffi).     

> __< p​lowsof:matrix.org >__ i was asked by at least one person why the license is changed for the unofficial version at getmonero.dev to "Copyright © MoneroDocs.org Contributors, MAGIC Grants, and Other Contributors. MIT Licensed."     

> __< p​lowsof:matrix.org >__ this was done before 'monero - docs ' on a monero-project repo was considered possible     

> __< p​lowsof:matrix.org >__ sgp has explained the reasons but theyre not at hand atm     

> __< r​ucknium:monero.social >__ AFAIK, if MAGIC Grants added any content, then you are supposed to add them to the copyright statement. The MAGIC Monero Fund _committee_ (I know it's confusing) has not helped with getmonero.dev yet by the way.     

> __< p​lowsof:matrix.org >__ they are named specifically while "Contributors" are not     

> __< p​lowsof:matrix.org >__ although on github the full list of contributors is visible     

> __< r​ucknium:monero.social >__ For example, https://monerofund.org/ has "© Open Sats Initiative and MAGIC Grants, 2024". The website code was forked from Open Sats. Then we changed the code a lot to fit our requirements.     

> __< r​ucknium:monero.social >__ Ok. Someone can make a PR to add the full list to the website footer.     

> __< p​lowsof:matrix.org >__ then we would have people complaining about the infinitely long list of contributors and how we need a javascript search function     

> __< r​ucknium:monero.social >__ For a permissionless currency, it seems you need the permission from a lot of people to set up anything in the Monero ecosystem.     

> __< p​lowsof:matrix.org >__ a deadmans switch for domain ownership 🤔 interesting.. i could imagine a few "im not dead, the reminder when to my spam box, can you transfer it back lol"     

> __< p​lowsof:matrix.org >__ anything else to discuss before getting to the ccs idea list?     

> __< p​lowsof:matrix.org >__ quick plug of a bounty for adding ipv6 to monerujo , requested by shortwavesurfer2009 https://bounties.monero.social/posts/102/1-700m-monerujo-add-full-ipv6-support     

> __< p​lowsof:matrix.org >__ SNeedleWoods add LegacyEnoteOriginContext for Seraphis [pull request](https://github.com/seraphis-migration/monero/pull/16#issue-2026817626) 🫡     

> __< p​lowsof:matrix.org >__ ok lets discuss the idea list     

> __< p​lowsof:matrix.org >__ 5. [CCS updates](https://ccs.getmonero.org/)    | [hinto](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422#note_23548) | [tobtoht](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/428#note_23555)     

> __< p​lowsof:matrix.org >__ a. [Unnamed Monero Wallet development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/437)     

> __< p​lowsof:matrix.org >__ aka xmruw     

> __< p​lowsof:matrix.org >__ Czarek Nakamoto: is here, and has provided a comment comparing his work to valdracs monero-wallet-sdk     

> __< p​lowsof:matrix.org >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/437#note_23529     

> __< m​rcyjanek0:matrix.org >__ Correct, it is quite long and technical but it comes down to the fact that both project have different goals and target different usecases.     

> __< m​rcyjanek0:matrix.org >__ > monero-wallet-sdk focuses on android while xmruw focuses on being cross platform     

> __< m​rcyjanek0:matrix.org >__ > monero-wallet-sdk focuses on stable api for developers while xmruw focuses on offering as small abstraction as possible     

> __< m​rcyjanek0:matrix.org >__ > both projects aim for good developer experience (things like IDE suggestions)     

> __< p​lowsof:matrix.org >__ r4v3r23 has suggested separating monero_c from xmruw     

> __< p​lowsof:matrix.org >__ the proposal has 2 milestones, is that everything listed under 'plans'?     

> __< m​rcyjanek0:matrix.org >__ I assume that he meant separating them into 2 CCSes. I'm slightly against this idea because it would make development more annoying and testing rather impossible, the projects monero_c, byteworks, offline_market_data, monero.dart are all separate and can be used easily by 3rd party software.     

> __< m​rcyjanek0:matrix.org >__ Yes, it is everything listed in plans + some other minor features, such as PoS mode for sellers (which is currently in works), it will allow people to input product IDs and scan them to create real-life PoS experience     

> __< r​4v3r23:monero.social >__ no, i meant removing the xmruw portion. besides feather (already establshed dev/wallet) all other wallets get funding on their own     

> __< m​rcyjanek0:matrix.org >__ and the docs update I've mentioned earlier - as I think that I've hit every possible edge case I could while working with monero code.     

> __< p​lowsof:matrix.org >__ the question is what is the sentiment here, we had comments from tobtoht (who is having a rest after release) and rbrunner. just waiting for a response     

> __< m​rcyjanek0:matrix.org >__ > all other wallets get funding on their own     

> __< m​rcyjanek0:matrix.org >__ monero-wallet-sdk did their demo wallet as a part of CCS.     

> __< m​rcyjanek0:matrix.org >__ you can consider xmruw the same, as it is really "just a demo" of all the libraries mentioned above.     

> __< p​lowsof:matrix.org >__ that came about because molly required it be created for various reasons (some security related)     

> __< r​4v3r23:monero.social >__ demo wallet is just that, a demo wallet. your asking for funding for the whole wallet project. its in the title of the ccs     

> __< r​4v3r23:monero.social >__ i guess all wallets are "just demos" of wallet2     

> __< p​lowsof:matrix.org >__ the ccs funded tesla to accept monero as payment and coral reef. anything is possible     

> __< r​4v3r23:monero.social >__ noted     

> __< m​rcyjanek0:matrix.org >__ Yes, I'm asking to support the full suite, all packages and a wallet. Developing libraries without a proper usecase for them just doesn't work. The wallet itself is not the major task here. monero_c is currently the biggest of them. monero_c wouldn't exist without xmruw, and xmruw can't exist without monero_c.     

> __< p​lowsof:matrix.org >__ lol     

> __< m​rcyjanek0:matrix.org >__ My current tests on byteworks pass 100%, but in real-world usecases I've noticed bugs. I can't separate the project without a large cost in terms of how good the software is.     

> __< m​rcyjanek0:matrix.org >__ My current tests on bytewords pass 100%, but in real-world usecases I've noticed bugs. I can't separate the project without a large cost in terms of how good the software is.     

> __< p​lowsof:matrix.org >__ there was alot of interest in having monero inside molly, this was merged. from this ccs came the need for monero-wallet-sdk (monero_c)     

> __< p​lowsof:matrix.org >__ xmruw needs monero_c     

> __< r​4v3r23:monero.social >__ monero_c doesnt need xmruw     

> __< m​rcyjanek0:matrix.org >__ Also xmruw targets platforms not officially supported by any wallets - such as SailfishOS and alpine linux (including PostmarketOS). So the entire effort also makes it easier to use monero in privacy enabled setups.     

> __< r​ucknium:monero.social >__ plowsof: I don't recall seeing comments from rbrunner and tob about this CCS. Is it in the IRC/Matrix logs?     

> __< p​lowsof:matrix.org >__ sorry moment     

> __< p​lowsof:matrix.org >__ i clipped the logs of the prev meeting half way* will fix that later     

> __< p​lowsof:matrix.org >__ tobtohts comment https://libera.monerologs.net/monero-community/20240302#c337258     

> __< m​rcyjanek0:matrix.org >__ > monero_c doesnt need xmruw     

> __< m​rcyjanek0:matrix.org >__ Making the library on its own will require me to write synthetic tests for all the libraries because I wouldn't be able to uncover bugs (such as the one in bytewords).     

> __< m​rcyjanek0:matrix.org >__ and tests are nowhere near the user testing in terms of how well they catch bugs.     

> __< m​rcyjanek0:matrix.org >__ and sure I can make demos for each project separately, but that would be just a waste of time, and wouldn't deliver any real project.     

> __< m​rcyjanek0:matrix.org >__ while now we have a cross platform wallet.     

> __< r​4v3r23:monero.social >__ also, a couple of devs asked why wallet2_api instead of wallet2.h directly     

> __< r​4v3r23:monero.social >__ mooo asked that when i firsted mentioned a C lib was being worked on     

> __< r​4v3r23:monero.social >__ tohtobt also expressed that, saying wallet2_api.h itself is an abstraction on top of wallet2.h     

> __< p​lowsof:matrix.org >__ rbrunners comments must have came some days later (i will find them unless it was a false memory)     

> __< p​lowsof:matrix.org >__ commenting on the perceived ease of adapting to seraphis     

> __< m​rcyjanek0:matrix.org >__ > tobtohts comment     

> __< m​rcyjanek0:matrix.org >__ line 63: OG response: https://pastebin.com/NQb5ejWc, I don't want to wait until wallet3 shows up, and I want to work on the project currently, when it comes I'll also do my best to enable people to have a seamless migration if they opted to use monero_c.     

> __< p​lowsof:matrix.org >__ thanks Czarek i was looking for the paste     

> __< m​rcyjanek0:matrix.org >__ > also, a couple of devs asked why wallet2_api instead of wallet2.h directly     

> __< m​rcyjanek0:matrix.org >__ Because there is api, that tends to be more stable than internal functions in general, and it was used by every single lib/wallet I've seen (except for simplewallet).     

> __< m​rcyjanek0:matrix.org >__ > tohtobt also expressed that, saying wallet2_api.h itself is an abstraction on top of wallet2.h     

> __< m​rcyjanek0:matrix.org >__ True, a stable abstraction. I didn't feel the need to invent anything from scratch, I've just wrapped already existing code.     

> __< p​lowsof:matrix.org >__ rbrunners comments a day later https://libera.monerologs.net/monero-community/20240303#c337362     

> __< m​rcyjanek0:matrix.org >__ also r4v3r23 you didn't appear to have anything against the way it is being developent, and you were pretty close to the project since day 0.     

> __< r​4v3r23:monero.social >__ tohtobt mentioned they managed to remove wallet2api and reduce to "libwalletqt -> wallet2.h in most places"     

> __< p​lowsof:matrix.org >__ "no such brand-new Monero wallet should start today and thus "this late in the game" without the dev(s) having a good long look at Jamtis and Seraphis first, and then add info to their CCS proposal how their project looks in this light."     

> __< p​lowsof:matrix.org >__ from rbrunner above^     

> __< m​rcyjanek0:matrix.org >__ sure, but that would cause reinvention of the wallet2_api.h in my usecase, which I didn't feel the need to do. There is a stable API available, so I've decided to use it.     

> __< r​4v3r23:monero.social >__ i was waiting for it to be stable before making judgement, and that was a major part of the delay     

> __< r​4v3r23:monero.social >__ this entire thing started from an experiment     

> __< m​rcyjanek0:matrix.org >__ I can't say anything else except "it happened". I agree that it shouldn't, but since most of the work is already done I think that polishing it is the way to go, to deliver a stable and cross platform wallet and libraries to power many new apps and projects.     

> __< r​ucknium:monero.social >__ Do we have time to discuss my CCS idea? It's not posted yet, but I would like input on the first draft     

> __< r​ucknium:monero.social >__ *for the first draft     

> __< m​rcyjanek0:matrix.org >__ at this point abandoning the project is not an option for me - too much time got put into it. However I need funding to continue working on it, otherwise it will cause huge delays as I'll have to work on other things first     

> __< p​lowsof:matrix.org >__ yes,   but b. Payout request for monero-gui flathub proposal [comment](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/381#note_23554)     

> __< p​lowsof:matrix.org >__ in the comment i have linked the stats showing flathub flatpak receiving updates throughout the year. the manifest is on the core repo but not complete. payout request for milestones 2 - 3 - 4 - 5     

> __< p​lowsof:matrix.org >__ if anyone wants to read / vote / comment on that please do     

> __< p​lowsof:matrix.org >__ Rucknium can you share your CCS idea(s)?     

> __< r​ucknium:monero.social >__ This would be 20 hours/week for three months of statistical research to improve Monero's privacy, guide protocol decisions, and respond to Monero developer requests for statistical analysis of code changes where needed. The start would be to analyze the suspected black marble flooding that is happening now. Effects of possible countermeasures, minimal safe parameter levels, and pr<clipped message>     

> __< r​ucknium:monero.social >__ oviding evidence for and/or against the black marble flooding hypothesis.     

> __< p​lowsof:matrix.org >__ kinghat: is a monero gui flatpak enjoyer and could offer some feedback.. selsta has seen BMP work through flatpak issues also     

> __< r​ucknium:monero.social >__ This would be in parallel to the OSPEAD work that is near completion. Basically, the flooding analysis is more urgent since it's happening now. OSPEAD probably has to wait for the next hard fork for safe implementation.     

> __< r​ucknium:monero.social >__ Other research questions could be ring member binning, Pocket Change privacy, EAE/EABE attack, fee discretization, and 10 block lock adjustment safety.     

> __< r​ucknium:monero.social >__ I could not research all those topics in a 3 month period of course, but the community can help set research priorities.     

> __< p​lowsof:matrix.org >__ would this be a similar deliverable as "analysing a flood"?     

> __< p​lowsof:matrix.org >__ the recent spam is definitely a hot topic. you even shared some figures reg possible ring size degradation     

> __< r​ucknium:monero.social >__ OSPEAD will suggest an update to Monero's decoy selection algorithm for ring signatures to mimic the real spend age distribution.     

> __< r​ucknium:monero.social >__ plowsof: The first priority is to research possible critical thresholds of flooding that would be a major threat to user privacy. See how bad it could be _if_ it is actually black marble flooding.     

> __< r​ucknium:monero.social >__ Then yes do more analysis like "Fingerprinting a Flood". I would re-run our 2021 analysis and also analyze the mempool tx arrival data that we didn't have back in 2021. And maybe try to crawl the network to figre out the possible node origin(s) of the flood.     

> __< r​ucknium:monero.social >__ There is a risk ,if the effective ring size gets too low, of chain reaction attacks.     

> __< p​lowsof:matrix.org >__ _some_ of ruckniums previous contributions are detailed here https://rucknium.me/     

> __< r​ucknium:monero.social >__ This was our analysis back in 2021 of a smaller suspected spam incident: https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60     

> __< r​ucknium:monero.social >__ The effective ring size analysis and chain reaction threshold analysis would help decide, for example, if mining pools could help by voluntarily self-limiting their block size and/or how raising the ring size to certain levels could help. And any fee changes or dynamic block size changes.     

> __< r​ucknium:monero.social >__ Any input appreciated :D     

> __< nioCat >__ will you work with ArticMine on this?     

> __< p​lowsof:matrix.org >__ positive effects if any of limiting block sizes ... how raising ring sizes could help...  looking at fees and dynamic block sizes seems important to a layman like myself     

> __< nioCat >__ or rather have input from him     

> __< r​ucknium:monero.social >__ Yes, if ArticMine wants to.     

> __< nioCat >__ him helping you direction would be great     

> __< r​ucknium:monero.social >__ ArticMine and I already discussed some preliminary analysis and proposals in #monero-research-lab:monero.social     

> __< nioCat >__ my vote is merge  :D     

> __< r​ucknium:monero.social >__ Ok I will directly ask him if he wants to work closely on this.     

> __< p​lowsof:matrix.org >__ some of it is here https://libera.monerologs.net/monero-research-lab/20240314#c347465     

> __< p​lowsof:matrix.org >__ irc users cant access the matrix logs is all     

> __< a​ck-j:matrix.org >__ +1 for Ruck CCS     

> __< r​ucknium:monero.social >__ I am working on a preliminary document that estimates empirical effective ring size if the tx volume is black marble flooding, long-term projections of effective ring size at several nominal ring size levels, and tx confirmation delay analysis.     

> __< p​lowsof:matrix.org >__ +1 here     

> __< p​lowsof:matrix.org >__ +2 if you tell me how i can get on a contributor list with the least mount of work     

> __< r​ucknium:monero.social >__ And the additional GB added to the blockchain and total fee paid by the attacker if it is an attacker.     

> __< p​lowsof:matrix.org >__ available for running scripts on server(s) as always     

> __< r​ucknium:monero.social >__ Well, you already contributed the mempool data collection, so you get a mention :)     

> __< a​ck-j:matrix.org >__ I’m in favor of having a proper security analysis of the newly proposed scaling definitions.     

> __< a​ck-j:matrix.org >__ We should have a strong idea of cost to perform a DOS or black marble attack     

> __< p​lowsof:matrix.org >__ also spackle_xmr, your churn script is gone from github, i was wondering about that     

> __< p​lowsof:matrix.org >__ thanks for sharing the idea Rucknium and those who left feedback so far     

> __< w​oodser:monero.social >__ yeah I'm also curious to see more analysis on cost to spam the blockchain     

> __< w​oodser:monero.social >__ it's not helping us if it's too cheap     

> __< r​ucknium:monero.social >__ I can add that. It was one of my items in "A Statistical Research Agenda for Monero" https://github.com/Rucknium/presentations/blob/main/Rucknium-Monerotopia-2023-Slides.pdf     

> __< r​ucknium:monero.social >__ "Monero’s dynamic block size has not received the same amount of research scrutiny as its privacy features."     

> __< 1​23bob123:matrix.org >__ “Organic” “usage”     

> __< p​lowsof:matrix.org >__ pls do not forget that the "cost" in terms of xmr is HIGH (if xmr was priced around BTC) as sech1 stated we also 5*d the fees recently     

> __< r​ucknium:monero.social >__ 1) Can the dynamic block size parameters result in undesirable outcomes, e.g. too fast or too slow block size increase?     

> __< r​ucknium:monero.social >__ 2) The interaction of block size and fee policy is supposed to adjust fee to the purchasing power of a unit of XMR in the future (a type of “oracle” problem). Can this go wrong?     

> __< r​ucknium:monero.social >__ 3) Is it possible to have a fee policy that discourages adversarial spam but provides low fees for people around the globe?     

> __< r​ucknium:monero.social >__ ^ Those were some of my research agenda questions from Monerotopia 2023     

> __< p​lowsof:matrix.org >__ i think we can put an end to the meeting and continue discussion on this. thank you all for attending and sorry for the slow  start and going over     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

continued
```
16:31:39 <m-relay> <1​23bob123:matrix.org> Probably should just fork monerodocs and modify from there, then things would get started, otherwise we have to wait for core to setup. 
16:31:40 <m-relay> <1​23bob123:matrix.org> mkdocs material has client side search so if js is disable still works
16:31:40 <m-relay> <1​23bob123:matrix.org> https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/
16:31:41 <m-relay> <1​23bob123:matrix.org> and also can be run offline
16:31:41 <m-relay> <1​23bob123:matrix.org> https://squidfunk.github.io/mkdocs-material/plugins/offline/?h=offline
16:33:39 <nioCat> plowsof: am I remembering correctly that the 5x fee increase was due to the reduction of tx size and therefore fees brought about by bulletproofs?
16:35:04 <m-relay> <p​lowsof:matrix.org> sech1^ im pretending to be afk because i dont know
16:35:46 <m-relay> <p​lowsof:matrix.org> thanks for the extra context/reasoning if true nioCat
16:36:01 <m-relay> <p​lowsof:matrix.org> thanks Dan 🤐 | alderman (Is not the man & Braxman Tomsparks Advocate )
16:37:36 <sech1> I don't remember
16:38:04 <nioCat> we went from MLSAG to CLSAG Oct 2020
16:38:34 <m-relay> <r​ucknium:monero.social> IIRC BulletProofs+ reduced tx sizes by about 10%. I am not sure, but I think the Fingerprinting a Flood analysis influenced the 5x fee increase .
16:38:35 <nioCat> I think fee change was after that 
16:39:29 <m-relay> <r​ucknium:monero.social> Fingerprinting a Flood estimated "At the time, the exchange rate for Monero was about 200 USD per XMR, so the cost of generating ~365,000 transactions would have been $1,000. A 2-in/2-out transaction weighs about 1.93 kB so these transactions would have added about 700 MB to the chain, at a cost of $1.40 per MB."
16:40:48 <nioCat> bulletproofs Oct 2018
16:44:25 <m-relay> <1​23bob123:matrix.org> https://github.com/monero-project/monero-docs. plowsof maybe luigi can enable discussion on repo?
16:44:26 <m-relay> <1​23bob123:matrix.org> https://docs.github.com/en/discussions/quickstart#enabling-github-discussions-on-your-repository
16:47:48 <m-relay> <1​23bob123:matrix.org> Dont want to have to make matrix room/irc for docs
16:53:05 <m-relay> <r​ucknium:monero.social> Some of the discussion about the 5x fee increase in the August 2022 hard fork happened here: https://github.com/monero-project/research-lab/issues/70
16:56:18 <plowsof> xmrack has one specifically for spam :P
16:57:29 <m-relay> <r​ucknium:monero.social> If we feel the need to hide how the dynamic block size works to prevent its misuse, that is not a good place to be in. Not a criticism of your decision, spackle.
```


# Action History
- Created by: plowsof | 2024-03-14T08:36:42+00:00
- Closed at: 2024-03-29T08:56:19+00:00
