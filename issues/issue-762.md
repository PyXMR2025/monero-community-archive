---
title: 'Seraphis wallet workgroup meeting #4 - Monday, 2022-12-05, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/762
author: rbrunner7
assignees: []
labels: []
created_at: '2022-12-02T14:50:03+00:00'
updated_at: '2022-12-30T14:58:39+00:00'
type: issue
status: closed
closed_at: '2022-12-30T14:58:39+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #758

For the new meeting, I propose to have a look at all known points that are still somewhat in flux with Seraphis and Jamtis on the protocol / construction level, and discuss their importance in relation to the starting implementation work: Which points would be nice to have decided early if possible, and which points would have only weak interaction with implementation and could be changed later with reasonable effort even with code already existing?

Thus the point of the meeting would not be to get any decisions, but to get a better overview, and maybe a ranking of importance based on potential difficulties caused for the coding if left open for a longer time.

I will try to document possible such points here, as meeting preparation.

# Discussion History
## rbrunner7 | 2022-12-02T14:56:01+00:00
One thing still in flux for Jamtis, but inching toward resolution as it seems, is the question of the Jamtis address checksum algorithm. Details are e.g. [here](https://github.com/seraphis-migration/wallet3/issues/37).

Potential to hold up wallet programming seems low, but on the other hand it would be nice to be able to give Jamtis addresses that will (most probably) stand early on.

## rbrunner7 | 2022-12-02T15:04:35+00:00
A second thing I know of is the question whether accounts will be part of the "core" protocol itself, by embedding account indexes somewhere somehow, or wether at the base only indexes are known that you can interpret to mean accounts and addresses within those accounts somewhere "higher up" in the hierarchy if wanted / needed.

This was quite intensively discussed over the last couple of days by @UkoeHB and @Tevador on the Jamtis "gist", starting about [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4382657). See also [this workgroup isse](https://github.com/seraphis-migration/wallet3/issues/21) for some background info.

To me it's not clear now what it means for wallet programming (and maybe even the Seraphis library) if it takes longer to settle this question.

## rbrunner7 | 2022-12-02T15:14:06+00:00
@Tevador has written a [[Draft] Zero-cost post-quantum mitigations for Seraphis](https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a), but I don't know whether having this implemented and available already after the (first) hardfork to Seraphis is in the realm of the possible, or pretty much out of question.

## One-horse-wagon | 2022-12-02T15:45:19+00:00
Would tevador be interested in a CCS proposal to implement his proposals into Seraphis?  IMO, quantum technology is moving secretly ahead with billions of dollars being spent by several companies and countries.  Whether or not they succeed will be unknowable for some time.  OpenSSL has instituted some quantum protection in their protocol and we would be more than prudent to do the same.  

## rbrunner7 | 2022-12-05T07:17:20+00:00
I think after all that discussion in the Matrix room we can add the issue of Jamtis addresses to the list, with things to look at like: their length (at least 181 characters, maybe over 200 after a modification of the scheme), the "alphabet" used to encode them (*Base32* versus *Base58* or maybe even *Base64*), and maybe even the added features that lead to the massive length increase compared with CryptoNote addresses with their length of 95 characters.

## rbrunner7 | 2022-12-05T19:16:52+00:00
````
<one-horse-wagon[> Hello.
<ghostway[m]> Hello
<rbrunner7[m]1> Well, yes, you people are 2 minutes early, but hello! Meeting time. Issue is here: https://github.com/monero-project/meta/issues/762
<UkoeHB> hi
<rbrunner7[m]1> My idea for today is having a look at Seraphis and Jamtis as designs, as constructs, get a list what is still somewhat in flux there, and see how those things would influence wallet development in important ways.
<jberman[m]> hello
<ofrnxmr[m]> Greetings
<dangerousfreedom> Hello
<rbrunner7[m]1> Did something important happening on the implementation front over the last week that you would like to report first?
<Rucknium[m]> Hi
<dangerousfreedom> rbrunner7[m]: This week I looked at the checksum algo and implemented the BCH code as specified by Tevador in his Python snippet (https://github.com/DangerousFreedom1984/seraphis_lib/blob/simple_prototype/src/seraphis/jamtis_account.cpp#L186) so if we reach a consensus about the address tag (which I dont have an opinion now) then we should be good for generating the addresses. 
<Rucknium> +1
<dangerousfreedom> I have also been looking at the transaction proofs and should write something (to Koe) by the weekend.
<UkoeHB> I have continued to do cleanup/review, made some PRs to start upstreaming the library, and finally decided to accept tevador's blake2b address tag hint quest.
<rbrunner7[m]1> That was a quite long thread about that ...
<rbrunner7[m]1> The question was not the tag or its width per se, but how to encrypt it?
<UkoeHB> yes
<jberman[m]> No implementation work to report on my end yet. I'm very nearly done with tx pool stress testing (should be 1-2 days left) then moving over to Seraphis impl work
<rbrunner7[m]1> Good to hear!
<rbrunner7[m]1> The checksum was one of the things I knew are still under discussion, but it seems this also "converges". dangerousfreedom[m] , can you confirm that calculating the checksum is very easy?
<rbrunner7[m]1> The checksum as proposed now
<ghostway[m]> the one proposed here? https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4382275#gistcomment-4382275
<rbrunner7[m]1> Yup.
<dangerousfreedom> Yeah, it is pretty straight forward as you can see in the implementation I did from tevador's code. I checked the logic and it seems that this constant is fine.
<dangerousfreedom> ghostway[m]: Yes
<rbrunner7[m]1> So people should not have much difficulties implementing this in other programming languages, for many different possible frontends?
<ghostway[m]> I did already in c++, if you want that
<dangerousfreedom> rbrunner7[m]: No, it is simple.
<JoshBabb[m]> rbrunner7[m]1: other language guy here, yes it looks handleable
<Rucknium[m]> I'll let you know if I can implement it in R :)
<rbrunner7[m]1> +1
<Josh Babb> +1
<plowsof> +1
<tevador> Regarding the checksum, I contacted Pieter Wuille (the author of bitcoin's bech32 address format) and got some hints how to find an even better performing generator, so I'd like to try that. This would only change the "GEN" variable in the python code I posted.
<ofrnxmr[m]> +1
<dangerousfreedom> Nice.
<ghostway[m]> cool, so no implementation changes.. will you also try tuning M in some way? or is it not reasonable?..
<tevador> Yes, that requires a fixed generator, so it can be done afterwards.
<ghostway[m]> +1
<rbrunner7[m]1> Good to hear. So it seems regarding public addresses their enormous length is the single thing left, as discussed here extensively yesterday. There we had the Base32 versus Base58 question on the table and wondered about a comment of yours, tevador , that Base32 would be better for QR codes. Can you elaborate?
<tevador> Best if gingeropolous can provide me with some CPU time.
<tevador> QR codes have a more efficient encoding for case-insensitive data.
<ofrnxmr[m]> Ginger has posted that the server is available tevador: gingeropolous: 
<rbrunner7[m]1> It seems the addresses will get about 205 characters long with Base32, and about 175 or so with Base58.
<rbrunner7[m]1> You mean the same bits get a smaller QR code? Not sure I follow.
<rbrunner7[m]1> If we don't have uppercase as well as lowercase?
<tevador> I calculated 196 characters with base32 if we keep the 18-byte tag.
<tevador> https://en.wikipedia.org/wiki/QR_code#Storage
<rbrunner7[m]1> Is the length of the tag, with 18 bytes, still in active discussion?
<rbrunner7[m]1> Anyway, probably good to get an overview, so the important question for this right now probably is: Does the exact address format hold us up in any significant way? Don't think so, right?
<plowsof> lowercase sucks and an address length double than what we have now sucks too 
<ghostway[m]> rbrunner7[m]1: what do you mean doesn't hold up? 
<plowsof> and an increase in address size is unavoidable* so i don'tcontest this 
<rbrunner7[m]1> Whether it interferes with starting to program parts of the wallet in dangerous ways.
<rbrunner7[m]1> Because if today we find something like that, that would be a very important result
<UkoeHB> tevador: do QR codes normal encode the address string instead of raw bytes?
<ghostway[m]> rbrunner7[m]1: what about RIDs? why is it that of a problem? 
<UkoeHB> normally*
<tevador> UkoeHB: yes, both current Monero wallets and Bitcoin encode the string.
<rbrunner7[m]1> I guess the way we intend to use QR codes for address "Input" it's indeed the strings.
<rbrunner7[m]1> Maybe even with things like "monero:" in front, for "protocol" recognition
<rbrunner7[m]1> ghostway: I don't think RIDs pose a problem for starting with wallet programming in earnest now.
<ghostway[m]> I'm not saying RIDs pose a problem, Im I'm trying to understand why 205 characters is bad
<ghostway[m]> * is bad (saying RIDs are a solution)
<rbrunner7[m]1> Well, opinions seem to widely differ whether 200 characters are a problem, and if yes how big a problem :)
<tevador> If it's a problem, I don't see how it can be avoided. Perhaps by discontinuing plaintext addresses altogether, which won't fly.
<UkoeHB> to recap, here are the reasons for longer addresses: we added a third key to the address to mitigate the Janus attack (this also allows using X25519 for significant speedups during scanning - 40-60% depending on hardware iirc, and also prevents someone from combining a find-received service and generate-address hub into a payment validator), we added the 18-byte address tag to eliminate the subaddress lookahead (for 
<UkoeHB> seraphis - you still need it for legacy 
<UkoeHB> balance recovery) and allow robust random unsynchronized address generation
<ghostway[m]> +1
<plowsof> +1
<rbrunner7[m]1> Thanks for that info, koe. Alright, as we probably won't arrive at any consensus right here, in this meeting, maybe we move on to some other point, to get at an overview.
<rbrunner7[m]1> The second thing that I know about is that question whether accounts are "in" or "out" regarding the core of the protocol.
<jberman[m]> ghostway: it's difficult to visually compare 205 characters in the wallet UI to the address on the point of sale system. RIDs make it easier to visually compare to make sure the address is correct
<rbrunner7[m]1> That may look a bit more consequential for programming.
<ghostway[m]> jberman[m]: so its the solution of it..
<ghostway[m]> > <@jberman:matrix.org> ghostway: it's difficult to visually compare 205 characters in the wallet UI to the address on the point of sale system. RIDs make it easier to visually compare to make sure the address is correct
<ghostway[m]>  * so is it not a solution?
<one-horse-wagon[> jberman[m]: You could also use a Q-R code at the point of sale too.  Even easier.
<wormrobot> meeting? am i late?
<jberman[m]> @woodser brought up solid UX arguments about how larger address strings still need to be handled cleanly in a UI, and the larger the string, the more difficult it gets to handle displaying them cleanly. so he requested considering to reduce the string length if possible, hence the discussion on base encoding of the address string
<tevador> With RIDs, wallet UI does not actually need to display the whole address.
<Rucknium[m]> UkoeHB: How many bytes does the extra key for Janus attack mitigation, etc., add?
<jberman[m]> one-horse-wagon: it's not always practical to use a QR code e.g. if you're on your desktop buying something online using a desktop wallet. plus you'd still want to verify the QR code scanned address is correct
<UkoeHB> it's a 32 byte key
<Rucknium> +1
<UkoeHB> you also get view received without amounts, which has privacy benefits for the remote scanning scenario
<jberman[m]> I would think every wallet would still need an input field somewhere for an address so a user can copy paste
<ghostway[m]> UkoeHB: how does it work btw? I read about it in the "paper" ( :) )
<rbrunner7[m]1> Maybe postpone that question to after the meeting ... we already struggle to get an overview and leave the address topic behind :)
<ghostway[m]> +1
<Rucknium[m]> QR code generation leaves a small crack for a vulnerability in a merchant/wallet interaction. Ask plowsof . Can't just rely on getting the QR code transmission and receipt correct.
<rbrunner7[m]1> Soooo ... maybe continue to that accounts "in" or "out" of the protocol core. I guess a change in the account index system would also touch the Seraphis library?
<rbrunner7[m]1> This looks a bit heavier as a question that mere address details, I guess?
<rbrunner7[m]1> s/that/than/
<jberman[m]> UkoeHB tevador did your discussion on the mac have any impact on the account discussion?
<UkoeHB> ghostway[m]: you can check this https://www.youtube.com/watch?v=fEJpE7LumG8&list=PLsSYUeVwrHBndRQoQ-vLezzlHPLRDNzaw&index=14 it's mostly up to date
<ghostway[m]> +1
<tevador> For accounts, my recommendation is: 1. If we want mandatory accounts, use "option 4" (encoded in the public key), otherwise "option 1" (sub-divded index).
<rbrunner7[m]1> I suspect however that it will take quite a while until we reach anything that has to do with accounts in our wallet programming.
<UkoeHB> I'm still in camp option 1
<Rucknium[m]> The further Monero is from how other coins operate, the harder it is to implement Monero on multi-coin wallets, merchant software, and exchanges. At this point I think it's a good idea to keep accounts.
<rbrunner7[m]1> Er ... which many other coins don't have?
<rbrunner7[m]1> As far as I know
<Rucknium[m]> Which coins don't have accounts?
<rbrunner7[m]1> As part of the protocol? Are there any that do? Maybe I just don't know enough.
<rbrunner7[m]1> Don't tell me that Bitcoin has accounts as part of its core protocol ...
<Rucknium[m]> Bitcoin has accounts for HD Wallets. So many UTXO coins follow the bitcoin spec on that
<ofrnxmr[m]> Dero uses an account model iirc
<rbrunner7[m]1> Ok, so I have to look up something.
<rbrunner7[m]1> But anyway, does anybody see the "account question" as a danger for our workgroup programming that will shortly pick up steam?
<rbrunner7[m]1> I mean, as an immediate / short-term danger
<UkoeHB> pretty sure the bitcoin et al accounts are branches off the core wallet seed
<Rucknium[m]> Yes it's built into the derivation path.
<Rucknium[m]> Use ian coleman's BIP39 tool.
<rbrunner7[m]1> What about the Jamtis key hierarchy? Does that stand solid already? I vaguely remember that Tevador made a new proposal there once, even more elaborate. Is that still in the race?
<rbrunner7[m]1> The number of secret keys and how they are derived
<jberman[m]> Sorry, backing up to the different options for accounts
<jberman[m]> The primary UX thorn option 1 introduces is how different wallets should cleanly manage the user's chosen sub-divided index
<jberman[m]> Couple questions on my mind that I'll keep thinking on: should the user's choice be embedded as a flag in their seed?
<jberman[m]> Should users have a choice when creating/restoring a wallet what strategy they want to use?
<UkoeHB> jberman[m]: I don't think the other options actually solve that problem, because there is no truly generic format.
<tevador> If we want both the ability to have a randomly generated 16-byte index and accounts without having the user choose, option 4 provides that.
<UkoeHB> yes I agree - basically if you want to do more stuff you need more bytes
<rbrunner7[m]1> Ok, as we seem to run out of time to get a complete overview today: Does anybody want to sound an immediate alarm about something regarding Seraphis and Jamtis in relation to the starting of implementation work? Something that was not yet mentioned?
<jberman[m]> no immediate alarm on my end :)
<tevador> I'm not aware of any critical issues. But accounts are probably going to come up soon during implementation.
<Rucknium[m]> Just to be sure: changing course on binning and decoy algorithm enforcement would not require a deep rework of anything, right? Still need research and discussion on those.
<jberman[m]> I thought tevador 's option 4 didn't need extra bytes in the address/enote
<UkoeHB> binning would probably take a few days to replace, or more
<rbrunner7[m]1> But probably not ripple much further out than your library?
<UkoeHB> jberman[m]: it adds implicit bytes to the index
<UkoeHB> rbrunner7[m]1: hmm don't think so
<rbrunner7[m]1> That's the positive effect of a good library :)
<rbrunner7[m]1> Ok, so maybe at last, more for curiousity, where does that "quantum proposal" currently stand? What's a possible time horizon there?
<UkoeHB> I disagree about implementing that
<jberman[m]> adding implicit bytes to the index seems ok to me
<rbrunner7[m]1> https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a
<UkoeHB> we have to draw the line about adding stuff somewhere
<UkoeHB> right now the protocol is very solid
<rbrunner7[m]1> You mean regarding what goes into the first Seraphis hardfork?
<jberman[m]> UkoeHB: would you agree that option 4 avoids a user having to make a choice on account strategy, where sub-dividing the index does not?
<rbrunner7[m]1> I am not sure as well making transactions much larger will go down too well short-time
<rbrunner7[m]1> (talking about that quantum-related proposal)
<jberman[m]> ah
<jberman[m]> tevador's option 4 doesn't make txs larger
<tevador> BTW, we've already done a "post-quantum" improvement of Jamtis by removing the ability for a quantum attacker to learn the real spend. I'm quite satisfied with that solution.
<ofrnxmr[m]> +1
<rbrunner7[m]1> Alright, still so many things to discuss, and decide once, but at least that meeting here reached the full hour without any catastrophe looming on the horizon, sooo ... thanks everybody!
<UkoeHB> thanks tevador
<one-horse-wagon[> Great meeting.
````


# Action History
- Created by: rbrunner7 | 2022-12-02T14:50:03+00:00
- Closed at: 2022-12-30T14:58:39+00:00
