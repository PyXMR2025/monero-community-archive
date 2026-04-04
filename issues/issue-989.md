---
title: Monero Research Lab Meeting - Wed 10 April 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/989
author: Rucknium
assignees: []
labels: []
created_at: '2024-04-10T12:36:53+00:00'
updated_at: '2024-04-17T19:41:18+00:00'
type: issue
status: closed
closed_at: '2024-04-17T19:41:18+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Research [Pre-Seraphis Full-Chain Membership Proofs](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86). 

4. Cypher Stack CCS proposals: [Generalized Bulletproofs Security Proofs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/443) and [Seraphis General Paper Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441)

5. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#986 

# Discussion History
## Rucknium | 2024-04-10T19:37:00+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/989     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< o​ne-horse-wagon:monero.social >__ Hello!     

> __< rbrunner >__ Hello     

> __< vtnerd >__ hi     

> __< a​rticmine:monero.social >__ Hi     

> __< tevador >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< tobtoht_ >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< plowsof >__ hi     

> __< vtnerd >__ I made a new 0.3 release for LWS - fixing some bugs in recent PRs along the way     

> __< vtnerd >__ otherwise working on multi-machine scanning stil     

> __< isthmus >__ hey     

> __< r​ucknium:monero.social >__ me: Starting to develop the tradeoff function between raising tx fees and raising the ring size, measured by cost to a flooding adversary, node operator, and users. Feedback welcome on how to measure the cost.     

> __< tevador >__ I've been working on new elliptic curves for FCMP: https://gist.github.com/tevador/4524c2092178df08996487d4e272b096     

> __< r​ucknium:monero.social >__ My black marble flooding preliminary analysis was cited in Germany's biggest bitcoin blog, according to janowitz: https://bitcoinblog.de/2024/04/04/spam-welle-auf-monero-der-angriff-des-schwarzen-marmors/     

> __< r​ucknium:monero.social >__ I read Cypher Stack's Bulletproofs++ peer review and posted it to MoneroResearch.info: https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=217     

> __< c​haser:monero.social >__ nice! just curious, how long did it take to find the curves?     

> __< r​ucknium:monero.social >__ 3) Discussion: Research Pre-Seraphis Full-Chain Membership Proofs.  https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86     

> __< s​gp_:monero.social >__ Hello     

> __< tevador >__ The script takes a couple hours to find the curves. It took me a couple days to tune the script.     

> __< a​rticmine:monero.social >__ I have been researching asymmetric internet connections and DOCSIS . (Data over cable systems interface specification)     

> __< a​rticmine:monero.social >__ This can have a significant impact on Monero scaling, because of low upload bandwidth.     

> __< a​rticmine:monero.social >__ The good news is that there is a very significant economic pressure against this. The cable companies are being forced to accept reality     

> __< r​ucknium:monero.social >__ tevador: I don't know much about this, but is the way that you find the curves consistent with the advice on curves, e.g. at https://safecurves.cr.yp.to/ . You are using "an algorithm described in the 2007 paper "Constructing elliptic curves of prime order""     

> __< r​ucknium:monero.social >__ Ah, I see later in the gist you say that it meats some of the SafeCurves criteria     

> __< rbrunner >__ I thought that CypherStack already submitted their CCS for the GBP review or how they are called, to supersede "Seraphis General Paper Review", but don't see anything on our GitLab instance     

> __< r​ucknium:monero.social >__ meets*     

> __< s​gp_:monero.social >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/443     

> __< rbrunner >__ Ah, no, "Generalized Bulletproofs Security Proofs" - it's there, sorry     

> __< rbrunner >__ My bad     

> __< tevador >__ My writeup includes the evaluation of the safecurves criteria. We don't meet 4 of the less important ones.     

> __< r​ucknium:monero.social >__ I think we can discuss Cypher Stack's CCS proposals with the FCMP agenda item because they are related.     

> __< r​ucknium:monero.social >__ Generalized Bulletproofs Security Proofs  https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/443     

> __< c​haser:monero.social >__ re FCMP+SA+L: I welcome the new direction, just want to highlight that this is 12 months out at the very best. so Rucknium's and Artic's effort is very much welcome and, *if* it bears good fruit in time, I think that would justify a fork before FCMP.     

> __< r​ucknium:monero.social >__ Seraphis General Paper Review https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441     

> __< r​ucknium:monero.social >__ AFAIK, some people in #monero-community:monero.social  want the MRL meeting to confirm that the GBP Security Proofs CCS should be merged ASAP (i.e. MRL supports it and then the rest of the CCS process can continue). And that the Seraphis General Paper Review should not go to funding right now, but that it should be discussed in the near future.     

> __< r​ucknium:monero.social >__ "Some people" includes plowsof, who is the CCS coordinator, too.     

> __< r​ucknium:monero.social >__ chaser: Of course I would agree that all eggs should not be placed in one basket :)     

> __< plowsof >__ it would also be a step forward for MRL in terms of autonomy / speed of merges for these research related CCS'     

> __< a​rticmine:monero.social >__ If the Seraphis General Paper Review does not also down FCMP then this community concern can be addressed.     

> __< s​gp_:monero.social >__ I see no reason not the merge the GBP proposal asap     

> __< rbrunner >__ In my understanding we had "lose consensus" for going GBP review first, and I am not aware something special or drastic came to light in the week that passed that may change that     

> __< rbrunner >__ (at the end of last week's meeting, I mean)     

> __< r​ucknium:monero.social >__ I also agree that there is MRL loose consensus for Generalized Security Security Proofs going to Funding Required.     

> __< rbrunner >__ We had veritable rows of donations to the GF of 100 XMR each, and lastly even 200, if that party thinks favorably of FCMPs they might fund that alone :)     

> __< c​haser:monero.social >__ IIRC from last week, most research on the path to FCMP+SA+L will be useful for Seraphis+FCMP, including GBP, so I would agree it's a good idea.     

> __< tevador >__ Yes, the CCS should be merged ASAP.     

> __< a​rticmine:monero.social >__ I know FCMP is very big.     

> __< tobtoht_ >__ +1 GBP merge     

> __< dEBRUYNE >__ <tevador> Yes, the CCS should be merged ASAP. <= +1     

> __< dEBRUYNE >__ cc luigi1111 luigi1111w :-P     

> __< tevador >__ Btw, I posted some notes about new pre-Seraphis wallet tiers we might get with FCMPs: https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86?permalink_comment_id=5014753#gistcomment-5014753     

> __< rbrunner >__ What would happen to those "OVK" wallets with a switch to Seraphis and (full) Jamtis?     

> __< luigi1111 >__ Sgp mostly a question around volatility funds. Not a big deal I'll get it straightened out with Diego today probably      

> __< r​ucknium:monero.social >__ For the forward secrecy against a quantum adversary, that's just against discovery of the truly spent output, correct? A quantum adversary could still create counterfeit XMR under all proposals (regular Seraphis, FCMP, etc.), right? So eventually quantum-resistance would required some outputs to be unspendable(?)     

> __< tevador >__ rbrunner: Nothing. After Seraphis, all legacy wallets will use the Jamtis keys. The difference would be only for pre-Seraphis outputs.     

> __< rbrunner >__ So there would just be more pre-Seraphis "stuff" to support indefinitely into the future?     

> __< s​gp_:monero.social >__ this can be done under MAGIC Grants if desired. Or CCS if resolved     

> __< plowsof >__ thanks luigi1111     

> __< d​iego:cypherstack.com >__ What if 1 XMR stops being 1 XMR? That's the volatility risk.     

> __< tevador >__ You can say pre-Seraphis FCMPs is "stuff to support idenfinitely into the future".     

> __< d​iego:cypherstack.com >__ I jest of course.     

> __< rbrunner >__ Of course, but I think this would come on top, no?     

> __< tevador >__ It's only in the wallet code. Nodes don't care about it.     

> __< luigi1111 >__ Key image bug is fixed Diego!     

> __< rbrunner >__ More changes to `wallet2` spaghetti code :)     

> __< rbrunner >__ I am not sure that's really welcome ...     

> __< rbrunner >__ From a dev perspective     

> __< tevador >__ As I said, if we don't implement it officially, some 3rd party will.     

> __< rbrunner >__ Do you have somebody in particular in mind? I somehow doubt that somebody would be so adventurous, and so knowledgable     

> __< dEBRUYNE >__ diego: Do you think you can make the requested changes today? Would be nice to have it open for funding later today or latest tomorrow     

> __< u​ntraceable:monero.social >__ +1 GBP merge     

> __< tevador >__ No, but it's an extra feature that users want, so there is incentive.     

> __< rbrunner >__ Maybe I skimmed to quickly: What's the top, the main attraction of those OVK keys and wallets?     

> __< d​iego:cypherstack.com >__ It will be done today.     

> __< tevador >__ No need to "import key images" into view-only wallets.     

> __< d​iego:cypherstack.com >__ Just to be clear the changes requested are to remove the buffer and amend to 100% payout up front.     

> __< d​iego:cypherstack.com >__ Is that right Luigi?     

> __< rbrunner >__ Ok. For that I personally would probably risk that somebody overtakes us and implements that on their own accord.     

> __< plowsof >__ 100% upfront depends on quick funding to handle volatility. i suggested some % pre funded / upfront directly from the general fund      

> __< dEBRUYNE >__ tevador: Would this 'new view key' be difficult to implement (code)?     

> __< d​iego:cypherstack.com >__ See, it's not even decided what to change things to. :P     

> __< rbrunner >__ I see this a bit as a "offer them a finger and they take the whole hand" situation. First it was FCMPs before Seraphis, now it's "Jamtis light" on top ...     

> __< tevador >__ I think it would be a relatively small amount of code compared to the rest of FCMPs. But I might be wrong.     

> __< s​gp_:monero.social >__ I know kayaba isn't here, but my understanding is that this stuff is not a lot of extra work. The cost of the additional scope is minimal     

> __< rbrunner >__ And then forward secrecy ... quantum resistance ... do those cryptographers never sleep :)     

> __< tevador >__ It doesn't solve all issues of cryptonote addresses. Just 2 of them (outgoing view keys and separated address generation).     

> __< rbrunner >__ We already *drown* in work, with not really much dev capacity around. People.     

> __< tevador >__ It's optional. It can be implemented at any later time after FCMPs. Perhaps someone will volunteer or make a CCS.     

> __< rbrunner >__ If we can reasonably leave out that additional burden, even if slow, I would not touch that.     

> __< rbrunner >__ *even if small     

> __< d​iego:cypherstack.com >__ Ill be honest plowsof, I'm not in removing volatility buffer unless it's paid up front once funded. I accept the risk of price movement while waiting for funding.     

> __< plowsof >__ 100% upfront to remove the 10% volatility buffer upon full funding of the CCS is the offer put to luigi1111 to figure out today then yes?     

> __< d​iego:cypherstack.com >__ Yep     

> __< rbrunner >__ Yeah, news today is that maybe Kraken will delist XMR in the EU. The price may make some jumps downwards sometime in the near future.     

> __< plowsof >__ okok lets fo the figuring out asap, thank you     

> __< plowsof >__ s/fo/do     

> __< luigi1111 >__ Yeah it was a suggestion but I don't see why not. Helps us and you. Ccs doesn't earn interest on money waiting to be paid     

> __< a​rticmine:monero.social >__ OVK may help with this.     

> __< rbrunner >__ Then Seraphis and Jamtis may help even more - if we can get them out of the door, which we maybe can if we are careful with out dev resources     

> __< rbrunner >__ *our     

> __< c​haser:monero.social >__ how?     

> __< d​iego:cypherstack.com >__ Luigi these changes will be made within 2 hours     

> __< d​iego:cypherstack.com >__ I will let you know and then it can be merged.     

> __< rbrunner >__ Well, I am not sure what exactly ArticMine has in mind, but I am quite sure Seraphis and full Jamtis have more of that :)     

> __< dEBRUYNE >__ rbrunner: As far as I can see it concerns only Ireland and Belgium     

> __< a​rticmine:monero.social >__ It allows a user to provide the view   key to a withdrawal address given to an exchange     

> __< rbrunner >__ Yeah, hopefully. Still, speculators may try to take opportunity and depress the price for a while. I don't think we go towards *lower* volatility, in any case     

> __< dEBRUYNE >__ rbrunner: ArticMine may be referring to exchanges?     

> __< c​haser:monero.social >__ rbrunner: announcing/delivering upgrades explicitly to improve price action -- I hope we're not going there     

> __< c​haser:monero.social >__ got it, thanks     

> __< rbrunner >__ No, that's probably I misunderstanding. I was trying to show sympathy to Cyper Stacks insinstence on a volatility buffer     

> __< a​rticmine:monero.social >__ The user can preserve privacy by a further churn      

> __< a​rticmine:monero.social >__ This is about optics     

> __< o​ne-horse-wagon:monero.social >__ chaser: He was refering more to funding CCS proposal in a somewhat volatile market.     

> __< a​rticmine:monero.social >__ I don't have an issue with identifying the compliance benefits of a proposed hard fork. Particularly when it makes something that has been a part of Monero since the beginning work properly     

> __< r​ucknium:monero.social >__ "Paranoid about the Seraphis upgrade" https://monero.town/post/2733485     

> __< r​ucknium:monero.social >__ "TLDR: I am afraid the Seraphis upgrade might make it possible for governments to pass legislation demanding all businesses and exchanges to collect wallet view keys from users for any and all transactions involving Monero and maintain records, hence allowing state sponsored blockchain analysis companies the abilty to ‘Trace’ Monero transactions."     

> __< r​ucknium:monero.social >__ IIRC this is a criticism of Jamtis/Seraphis outgoing view keys.     

> __< rbrunner >__ That's of course a whole other can of worms that complicated discussion further     

> __< a​rticmine:monero.social >__ They won't . Make one churn.     

> __< rbrunner >__ I was more talking from dev capacity / project management point of view     

> __< rbrunner >__ We once had a single monster project ahead of us, Seraphis plus Jamtis. We just added a second monster, FCMP before Seraphis. Can we please pay a bit respect to the situation?     

> __< r​ucknium:monero.social >__ You would need to move to another wallet, right? Or can you make an outgoing view key for a specific address?     

> __< rbrunner >__ And don't pretend our resources are ample many enough for all that stuff     

> __< a​rticmine:monero.social >__ Create a new wallet.     

> __< tevador >__ Btw, currently existing view keys can act as OVKs with about a 99% accuracy. That point is moot.     

> __< s​gp_:monero.social >__ agreed. Worrying about the availability of a new key isn't worthwhile imho. People could always just demand the other key or even the private spend key     

> __< a​rticmine:monero.social >__ This is my point. It is really about optics. The capability has been there all the time.     

> __< rbrunner >__ And we have to rush into that "optics" so pressingly? That it can't wait a year or two more for Seraphis and Jamtis?     

> __< tevador >__ I heard 3-5 years.     

> __< r​ucknium:monero.social >__ The 99% accuracy only works if the tx produces a change output, right?     

> __< rbrunner >__ That was a worst-case estimate of koe, looking that the *currently* already completed stuff in the Seraphis wallet repo.     

> __< tevador >__ rucknium: correct     

> __< rbrunner >__ But yeah, if we fancy all possible additional stuff pre-Seraphis and Jamtis, this will almost turn into a self-fullfilling prophecy :)     

> __< rbrunner >__ Worst case you can hold up that almost indefinitely. Just keep everybody busy, done.     

> __< r​ucknium:monero.social >__ I was going to suggest ending the meeting, but I see kayabanerve typing     

> __< k​ayabanerve:matrix.org >__ Apologies for not being present. I do believe GBPs should move forward.     

> __< k​ayabanerve:matrix.org >__ I'm not immediately advocating the OVK solution as prior discussed. It could be an additional update or externally done. Accordingly, it's not taking more (whole new wallet format) than discussed (privacy)     

> __< k​ayabanerve:matrix.org >__ The forward secrecy commentary is just another increment in privacy, and why I originally viewed two-term output keys. It was just harder to come up with the forward secret opening proof, hence why I only posted the OVK commentary initially.     

> __< tevador >__ I think forward secrecy is something that can wait for Seraphis.     

> __< a​rticmine:monero.social >__ Does adding OVK after FCMP require a hard fork?     

> __< tevador >__ No. It only requires a wallet software update.     

> __< dEBRUYNE >__ rbrunner: If OVK can be added fairly easily I am not sure why we would wait     

> __< dEBRUYNE >__ If it is a complex undertaking, might be worthwhile to just focus on FMCP     

> __< tevador >__ It could be a "point release" after FCMPs.     

> __< dEBRUYNE >__ FCMP*     

> __< a​rticmine:monero.social >__ Thank. That is what I thought.     

> __< rbrunner >__ Maybe what I see as a problem will "solve" itself, if FCMPs should take considerably more time to implement and hardfork to than estimated today     

> __< dEBRUYNE >__ As a side note, is anyone willing to write a brief blog / primer on FCMP that can be posted on the Getmonero.org website?     

> __< dEBRUYNE >__ I think this would be beneficial for potential donors as well     

> __< rbrunner >__ Which of course will never happen, who has heard of IT projects that take longer than anticipated :)     

> __< r​ucknium:monero.social >__ I think what rbrunner was saying is that it seems like a complex undertaking for wallet software even if the cryptography is "simple". Mainnet Monero still has multisig marked as experimental. The only GUI implementation is Rino.  tobtoht is working on a usable Feather implementation.     

> __< rbrunner >__ Ah, yes, that little detail of "experimental" multisig only     

> __< rbrunner >__ Maybe we could "repair" that first?     

> __< r​ucknium:monero.social >__ IIRC koe thought getting it out of experimental should be a priority, in mid-2022 after the last hard fork.     

> __< rbrunner >__ Ok, I am rambling a bit now, sorry, it's a bit much, and it was a long meeting.     

> __< tobtoht_ >__ I'm making steady progress towards releasing a feather multisig beta.     

> __< tevador >__ Speaking of which: kayabanerve does your FCMP protocol work with multisig?     

> __< r​ucknium:monero.social >__ Thank you, t​obtoht. We can end the meeting. Feel free to continue discussing.     

> __< rbrunner >__ Thanks, Rucknium.     

> __< s​gp_:monero.social >__ thank you     

> __< dEBRUYNE >__ <d​iego:cypherstack.com> I will let you know and then it can be merged. <= Let's get it to funding required!     

> __< a​rticmine:monero.social >__ Thanks     

> __< d​iego:cypherstack.com >__ The proposal text has been adjusted and the front matter/milestones have been adjusted. Please look it over and if it is ready to merge, please do so.     

> __< d​iego:cypherstack.com >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/443     

> __< k​ayabanerve:matrix.org >__ tevador: Yes. You'd do a multisig GSP. It's proper transcripting and usage of a DKGd nonce for the private key column.  

# Action History
- Created by: Rucknium | 2024-04-10T12:36:53+00:00
- Closed at: 2024-04-17T19:41:18+00:00
