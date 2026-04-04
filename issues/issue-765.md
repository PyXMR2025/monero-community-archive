---
title: 'Seraphis wallet workgroup meeting #5 - Monday, 2022-12-12, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/765
author: rbrunner7
assignees: []
labels: []
created_at: '2022-12-10T15:01:27+00:00'
updated_at: '2023-01-16T17:27:34+00:00'
type: issue
status: closed
closed_at: '2023-01-16T17:27:34+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #762

For this meeting I see two possible points to discuss and hopefully bring closer to consensus: the issue of the length of Jamtis addresses, and my draft for a text to announce our need for devs helping to implement Seraphis and Jamtis.

For the first point I prepared the following: [Info collection about Jamtis addresses, with focus on the issue of their length](https://github.com/seraphis-migration/wallet3/issues/41)

For the second I wrote this, already somewhat refined based on feedback and discussion in our Matrix room: [Developer Opportunities at the Monero Project](https://github.com/seraphis-migration/wallet3/issues/40)

If you find time please do read the text about Jamtis addresses as a preparation for the meeting. Thanks!

# Discussion History
## rbrunner7 | 2022-12-12T19:14:46+00:00
````
<rbrunner7[m]1> Hello! Meeting time - https://github.com/monero-project/meta/issues/765
<rbrunner7[m]1> Who is around?
<one-horse-wagon[> Hello.
<dangerousfreedom> Hello
<UkoeHB> hi
<plowsof11> hi
<jberman[m]> hello
<Rucknium[m]> Hi
<rbrunner7[m]1> In preparation of today's meeting, a wrote an "info collection" about Jamtis addresses. I posted only last Saturday, but I hope some people had time for a read:
<rbrunner7[m]1> https://github.com/seraphis-migration/wallet3/issues/41
<SerHack> Hi
<ofrnxmr[m]> Greetings
<rbrunner7[m]1> The idea behind this: We can try whether we can come nearer to some sort of consensus, or else unearth things that are still controversial
<rbrunner7[m]1> because having the addresses kind of "finalized" would certainly be nice
<rbrunner7[m]1> My own comments / conclusion are in the text itself: Personally, very short, I would say go for that
<rbrunner7[m]1> Anybody comment?
<dangerousfreedom> I dont have a strong opinion on this. I would be fine with base32 or 58
<ofrnxmr[m]> No comment on hw wallets. Concerns about NFC might not be a problem by the time seraphis rolls around 
<ofrnxmr[m]> 888byte tags arent too hard to come by 
<plowsof11> thank you for condensing it all rbrunner, its clear the address size increase is needed for all these features and the RID is a UX+. i still dont like the lowercase address, im already squinting my hardest trying to see the current monero address on a ledger screen 
<ofrnxmr[m]> +1
<Rucknium[m]> Small comment: reformat the example address so it doesn't require scrolling to view. Or maybe that was intentional: Showing that you have to scroll.
<one-horse-wagon[> I asked this a couple days ago but no one commented.  Are hardare wallets really used in commerce out there or are they just "toys" to show and brag to friends?
<dangerousfreedom> Now I have an opinion about the address tag though. I believe that 4th solution (proposed by tevador) is the best that satisfies all the needs.
<Stnby[m]> Rucknium[m]: I would prefer if it was multiline
<Stnby[m]> * I would prefer if it was multiline (at least whenever it has to be displayed in UIs)
<rbrunner7[m]1> Ok, no problem to reformat for clarity, to see more of the length at a single glance.
<rbrunner7[m]1> In my text, I mean
<jberman[m]> I second dangerousfreedom[m] 's comments
<Stnby[m]> is there a real reason to have the 'xmr' prefix?
<rbrunner7[m]1> I think we have some more time to decide how exactly we will use the address tag, as long as nobody questions its length
<UkoeHB> I strongly disagree with doing anything in the protocol for accounts
<UkoeHB> it over-inflates the importance of core wallet
<rbrunner7[m]1> But the tag "stands" with or without accounts in the lowest protocol level, right?
<UkoeHB> yes
<rbrunner7[m]1> About the prefix: Not sure, seems nice however to me.
<Rucknium[m]> People complain about hardware wallet support for Monero regularly.
<Stnby[m]> rbrunner7[m]1: as we already have the monero: URI
<rbrunner7[m]1> The "1" is a version, if I remember correctly.
<rbrunner7[m]1> After the "xmr"
<Stnby[m]> Seems like chars wasted
<Stnby[m]> * Seems like 3 chars wasted
<plowsof11> btc has "bc1" and testnet "tc1" - if another coin forks the project the addresses might be confused with each other
<rbrunner7[m]1> Right. Some Monero forks have added something like a prefix because of this, I think
<Stnby[m]> Well then I guess its fine if forks arrise we save them the headache
<rbrunner7[m]1> In any case, it's about 1.5% of the length :)
<UkoeHB> imo the prefix is an important visual anchor
<Rucknium[m]> If we assume that wallet UIs will show sets of first and last characters, then the "xmr1" may be some waste.
<Stnby[m]> Dont forget tags have to encode other info in the URI not only the address, it will be pretty interesting how it works out
<Stnby[m]> Like amount, description how much space we will have left for those
<rbrunner7[m]1> It may be that the "show some first and some last characters" will be replaced by RID display
<rbrunner7[m]1> Or maybe both, it's probably hard to say now.
<rbrunner7[m]1> Well, we probably all agree that 200 is long, very long. But did somebody get away from reading my text with a good idea how to make them significantly shorter? If yes, speak freely :)
<rbrunner7[m]1> Are we still all online?
<one-horse-wagon[> yes
<rbrunner7[m]1> I think any shortening would go hand-in-hand with proposing different trade-offs. Like "We don't really need protection against that attack there"
<rbrunner7[m]1> Or the other nice things that one key more brings.
<rbrunner7[m]1> Janus attack, that's what my mind was searching
<dangerousfreedom> <UkoeHB> "it over-inflates the importance..." <- Why do you think so? If the protocol is well specified then I believe there wont be ambiguities so doesnt matter if the wallet implementation is the core wallet or not.
<rbrunner7[m]1> Maybe I try to prepare a similar text for next week, but about the variants regarding accounts?
<rbrunner7[m]1> So we have a common base for discussion. Not all people may know "variant 4" :)
<jberman[m]> Regarding base58 vs. base32, without a strong opinion on changing to base58, I think it's reasonable to move forward with the spec as is (base32) for now. It's a justified decision
<one-horse-wagon[> +1
<rbrunner7[m]1> Just 2 days ago I saw a video how a Ledger shows our current addresses in its tiny display. That already does not really work, if you ask me. I hope in 2 or 2.5 years devices like the new Ledger Stax will be the hit amount Monero fans.
<plowsof11> +1
<plowsof11> Sizes of signed/unsigned transactions compared to monero currently? (Thinking of cold signing projects)
<rbrunner7[m]1> Yeah, they contain addresses, but I don't know how many % of total size typically goes to those
<plowsof11> We went from needing 70 ish qr codes to needing only.7 to send/receive unsigned txs. Would be nice to keep an eye on them
<rbrunner7[m]1> Good idea, but I don't think that technically we have much "wiggle room" there. What info is needed is probably pretty clear, and doesn't compress in any way.
<rbrunner7[m]1> Do people here think it would be a good idea to post something on Reddit, with a link to my text, to get some additional opinions? I would hesitate, frankly. Some things are pretty technical to follow.
<Rucknium[m]> I would support. You did a good job of making it less technical. I don't think many people know that Seraphis will increase the address length so much. Your GH issue is the justification for the increase.
<rbrunner7[m]1> "GH"?
<Rucknium[m]> GitHub
<rbrunner7[m]1> Ah, ok
<jberman[m]> reddit post seems like a fine idea to me
<Rucknium[m]> You can just paste the full text of the issue in a Reddit post. Just paste markdown to markdown. Be careful of too many URL links.
<rbrunner7[m]1> The whole text in the hope that more people read?
<Rucknium[m]> Yes. So people don't have to click through
<rbrunner7[m]1> Ok, why not. Maybe will also be interesting to see where the community currently stands regarding Seraphis and Jamtis.
<rbrunner7[m]1> (How many people will be fully surprised, for example.)
<rbrunner7[m]1> So I will probably add some info about QR codes for cold signing, and about possible OpenAlias and URI length problems, and make a Reddit post, probably tomorrow.
<Rucknium[m]> +1
<rbrunner7[m]1> But anyway, one important result for me is what IMHO did not happen today, that somebody opposes and has arguments to back it up. Does not prove something, but still is something,
<rbrunner7[m]1> Maybe we can switch subject and talk a little bit in the remaining time about my sort-of "job advert" for Monero devs: https://github.com/seraphis-migration/wallet3/issues/40
<rbrunner7[m]1> I see two remaining issues there: Do we better add some more details about MAGIC?
<rbrunner7[m]1> And: Where to publish?
<Rucknium[m]> Did ofrnxmr give comments to that?
<rbrunner7[m]1> I am not sure who exactly said that maybe more details about MAGIC could be a good idea
<UkoeHB> dangerousfreedom: it's not a question of ambiguity, it's a question of scope creep
<Rucknium[m]> If it's in a basically finished state, then I can ask MAGIC for input. 
<rbrunner7[m]1> Ah, you mean, other people there in addition to you. Well, I myself right now do not plan to change on my own.
<rbrunner7[m]1> So maybe asking for feedback there could start.
<Rucknium[m]> MAGIC advantages over CCS: Can pay in basically any crypto or fiat currency. Quick review and approval/rejection of proposal. Disadvantage: Payout requires KYC.
<rbrunner7[m]1> And of course people can propose places to publish in the issue as well.
<Rucknium[m]> Intended audience matters, too.
<rbrunner7[m]1> Not sure what you mean. Are there different kinds of devs to target, and target differently?
<dangerousfreedom> UkoeHB: But if I understood correctly it is not adding more space on the blockchain as the account and address tags will be derived from a key exchange, right? You mean it leaves space for people adding more things to the protocol in the future?
<Rucknium[m]> rbrunner7: My first reaction is: of course there are different types of devs who could fill the roles.
<dangerousfreedom> If we reach consensus now then changing the protocol later will be really hard I think.
<Rucknium[m]> There are "blockchain" devs, FOSS devs, ex-FAANG devs (or whatever the acronym is now)
<Rucknium[m]> C++ FOSS devs are probably our best target
<rbrunner7[m]1> Agreed, but I am not sure how I would target them differently. Except maybe really making sure that some arrangements similar to a salary may be possible, thanks to MAGIC, if I understand that correctly
<UkoeHB> dangerousfreedom: yes, setting a precedent would be a long-term blow
<Rucknium[m]> It's also a question of where this is posted. I'm not saying that we need different version for different places. Just want to make sure that we don't omit something that is important for certain prospective recruits..
<rbrunner7[m]1> +1
<rbrunner7[m]1> I think there was the idea to make the text into a blog post on GetMonero.org. How does that sound to the people here?
<dangerousfreedom> UkoeHB: I dont know. Looks to me that once we reach consensus about the address scheme and the protocol then changing it would be very hard. So it wont leave space for lobbyists that easy.
<UkoeHB> from an extreme perspective, allowing purely UX-oriented design changes increases the chances of future hard forks - the opposite of what we want for project/protocol longevity
<one-horse-wagon[> rbrunner7[m]1: Sounds reasonable.
<Rucknium[m]> +1
<Stnby[m]> +1
<rbrunner7[m]1> Would be my first, I think :)
<jberman[m]> Deciding to support accounts at the protocol level maximizes UX for all users using feedback from supporting accounts since subaddresses were introduced. It's not as though we're shooting in the dark here, it's a well informed decision that I think is reasonable to entrench at this point
<rbrunner7[m]1> Ok, we are nearing the full hour. Any last comments? other than the subjects of accounts is still surprisingly hot :)
<UkoeHB> and if this were anything other than a cryptocurrency protocol design discussion, I'd agree with you
<UkoeHB> cryptocurrency protocol design requires uncompromising idealism
<one-horse-wagon[> +1
<rbrunner7[m]1> I have a hunch that consensus about accouts will be harder to reach, and will take longer, than a reasonably strong consensus about those long addresses ...
<dangerousfreedom> I have some questions to Koe but we can discuss after the meeting
<rbrunner7[m]1> Maybe because the arguments seem less "clear-cut".
<one-horse-wagon[> Last thought.  I don't have a clue how your post on Reddit about long addresses will be accepted.  It will be most interesting to see.
<dangerousfreedom> UkoeHB:  In a hypothetical scenario, if person A makes a valid image-enote with the membership and composition proofs and shares it and the openings for the amount commitments with person B, then person B would be able to steal the funds of person A by creating an enote directed to him with a valid balance proof, right?
<rbrunner7[m]1> Agreed, and I will survive some snippish comments "Too long, man, too long" :)
<rbrunner7[m]1> Alright, if that's ok for people, I close the meeting proper. Thanks to all attending!
<dangerousfreedom> Thanks rbrunner7[m] 
<one-horse-wagon[> Thank you again.
````


# Action History
- Created by: rbrunner7 | 2022-12-10T15:01:27+00:00
- Closed at: 2023-01-16T17:27:34+00:00
