---
title: 'Seraphis wallet workgroup meeting #14 - Monday, 2023-02-27, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/802
author: rbrunner7
assignees: []
labels: []
created_at: '2023-02-24T16:28:54+00:00'
updated_at: '2023-03-03T20:20:36+00:00'
type: issue
status: closed
closed_at: '2023-03-03T20:20:36+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #799 

I don't have a special proposal for something to discuss, we will see what presents itself.

# Discussion History
## rbrunner7 | 2023-02-27T18:52:42+00:00
````
<UkoeHB> it's good to disambiguate member variables from other variables in member functions). Updating that will cause quite a big diff, so sorry in advance for anyone rebasing.
<UkoeHB> I won't make it to the meeting today.
<UkoeHB> My update is I merged dangerousfreedom's seraphis knowledge proofs PR and updated it with various cleanup/fixes/improvements to get it in a production-ready state.
<UkoeHB> The files are `src/seraphis_main/sp_knowledge_proof_*`.
<UkoeHB> Next, I decided to remove the `m_` prefix from the members of data-only structs for simplicity and consistency (a prefix is only useful in behavioral objects where
<ghostway[m]> Hello 2 minutes early
<ghostway[m]> * minutes early people
<rbrunner7[m]> Woah there
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/802
<rbrunner7[m]> Who is around?
<one-horse-wagon[> Hello.
<dangerousfreedom> Hello
<Rucknium[m]> Hi
<jberman[m]> hello
<rbrunner7[m]> UkoeHB left a report about 1 hour ago, he is still heavily "cleaning up" his Seraphis library as it seems, keeping dangerousfreedom[m] busy with rebasing or so :)
<rbrunner7[m]> Won't make it to this meeting
<rbrunner7[m]> Other reports about work done, or interesting work in progress?
<dangerousfreedom> UkoeHBdid a great review on the proofs I wrote. I forgot to include some tests and he promptly saw it. I think we are done now for the moment with these proofs.
<dangerousfreedom> I started looking at the transaction_history_component that would be a part of the wallet. Briefly the idea is to create a component to handle outgoing transactions (txs not enotes) so it should: 1) collect authored txs. 2) can keep track of what is offchain, unconfirmed, onchain. 3) return useful information. This information should also be used as inputs for the knowledge proofs that I also would like to integrate in
<dangerousfreedom> the wallet (both for legacy and seraphis).
<dangerousfreedom> I opened a [CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377) too. Please let your comments and opinions :)
<rbrunner7[m]> I myself started to look into existing wallet interfaces, and I am comparing `wallet2`, the "Wallet2 API" that the Monero GUI is using, the Monero RPC interface, and woodser 's `monero_cpp`. Intent is to be able to "distill" some hints how the top-level interface of our Seraphis wallet classes could look.
<rbrunner7[m]> dangerousfreedom[m]: Time flies, time for another CCS :)
<dangerousfreedom> Yeah, I had no idea about what Seraphis was some months ago and I believe I understand all the crypto going on and I'm getting familiar with Koe's coding style.
<rbrunner7[m]> In the last meeting we were, among other things, discussing reviews, and somebody mentioned that the Rust people have some nice system in place. So I had a look.
<dangerousfreedom> I due it to UkoeHB 's help too. Would be impossible without his support.
<rbrunner7[m]> What I found was some quite elaborate system that looks like it's a bit overkill for us:
<rbrunner7[m]> https://github.com/rust-lang/rust-forge/blob/master/src/compiler/reviews.md
<rbrunner7[m]> See also this interesting discussion - they have, not surprisingly - many of the same problems as we have:
<rbrunner7[m]> https://internals.rust-lang.org/t/did-we-start-reviewing-prs-slower/18033
<rbrunner7[m]> All in all, personally I did not see something that I would propose we try to copy immediately, but maybe other people come to other conclusions.
<jberman[m]> My update: I'm still working on hardening the legacy scanner pointing it to a local daemon + started thinking through integrating it with the CLI wallet
<jberman[m]> On integration, I'm thinking as of right now it would be simplest to replace the existing scanner code with the Seraphis lib code inside wallet2, which to be clear would mean keeping wallet2 but down-sizing it by replacing huge sections of its core logic. From there the CLI/RPC/any wallets using wallet2 would be set up structurally to scan Seraphis txs, so we could move closer toward a testnet. But granted, that would mean
<jberman[m]> keeping wallet2 for the testnet and shooting for replacing wallet2 entirely at a later stage, so it's definitely a task worth discussing
<ghostway[m]> that sounds interesting
<rbrunner7[m]> That's a surprising approach. Have to think about it. So that would never enter production, but would only live on the Seraphis dev branch, right?
<jberman[m]> that's what I'm thinking for right now. The Seraphis lib is built to be used in a wallet post-Seraphis (it doesn't support building legacy txs e.g.), so technically unless legacy tx construction is rebuilt in the Seraphis lib, then any wallet deployed to handle the update would still need to use some stuff currently in wallet2
<rbrunner7[m]> In any case what this certainly allowed would be very early and yet thorough tests of the Seraphis library code under realistic conditions.
<dangerousfreedom> <jberman[m]> "On integration, I'm thinking..." <- Is it too dificult to isolate these functions to scan the blocks separately? 
<rbrunner7[m]> > any wallet deployed to handle the update would still need to use some stuff currently in wallet2
<rbrunner7[m]> Yeah, I think in the last meeting we recognized the separation of code capable to load wallets from `wallet2` itself as a dev task that could start now already, exactly to prevent that we need `wallet2` for the update.
<dangerousfreedom> jberman[m]: I dont follow. If we have a seraphis wallet then we would have in the worst case a type 1 or type 2 tx as input and it would output an enote. Right? Why would you need to build the constructors for legacy? And I believe Koe already did it.
<jberman[m]> > <@rbrunner7:monero.social> > any wallet deployed to handle the update would still need to use some stuff currently in wallet2
<jberman[m]> > Yeah, I think in the last meeting we recognized the separation of code capable to load wallets from `wallet2` itself as a dev task that could start now already, exactly to prevent that we need `wallet2` for the update.
<jberman[m]> Right by "some stuff" here in today's meeting I meant business logic, not just reading old wallet files like we talked about last meeting
<jberman[m]> > Is it too dificult to isolate these functions to scan the blocks separately?
<jberman[m]> scanning blocks is already separate/isolated, but plugging into wallet2 means scanning into wallet2's existing data structures and calling the callback functions like `on_money_received` etc.
<jberman[m]> > I dont follow. If we have a seraphis wallet then we would have in the worst case a type 1 or type 2 tx as input and it would output an enote. Right? Why would you need to build the constructors for legacy? And I believe Koe already did it.
<jberman[m]> koe implemented spending legacy enotes alongside Seraphis enotes, in the same tx
<jberman[m]> in the same Seraphis tx*
<jberman[m]> before the Seraphis hard fork, wallets would still need to construct pre-Seraphis txs as they currently do
<rbrunner7[m]> Without thinking too much about it, I would say whether this endevour is worthwhile or not depends on how much time you need to implement it. I mean, this gets you quite some "Frankenstein" wallet 2 and a half that will later die anyway ... If no other advantage than providing some good testing I don't see this being worth more than 1 or 2 workweeks
<rbrunner7[m]> jberman[m]: Is that a given? No way around it?
<jberman[m]> I'm thinking I could have something solid within 2-3 days
<rbrunner7[m]> Looks pretty unfortunate
<dangerousfreedom> Yeah, the data structure we wont get rid of as we have to be able to properly read (and write) old wallets. So the functions to do it have to be in the seraphis wallet. I just accepted that fact. I dont see though how using walllet2 would be beneficial as we could use that time to build something for seraphis. Instead the other way round.
<rbrunner7[m]> Not sure about writing old wallets, why would that be?
<jberman[m]> > Is that a given? No way around it?
<jberman[m]> I don't see a way around this but UkoeHB could confirm. We wouldn't want any updated wallet pre-Seraphis hard fork to be fingerprintable for one, so it would need to have the same logic as existing wallets for that reason alone. And pretty sure to construct txs the way the Seraphis lib does (e.g. spending pre-RCT + post-RCT in the same tx) would require a hard fork itself. 
<rbrunner7[m]> I guess if we don't want to force people to juggle with two versions of the Monero software that has to work somehow. That's bad.
<dangerousfreedom> But yeah, for the transitions period it might be reasonable to "prepare" or "improve" wallet2 for the upcoming fork than writing a lot of new things on the seraphis wallet that would be deprecated soon.
<rbrunner7[m]> Well, that fingerprinting would be weak and maybe only for a few weeks or so.
<dangerousfreedom> If thats what you mean
<rbrunner7[m]> jberman[m]: Is that the famous optimism of the youth? :) If true I would say go for it!
<jberman[m]> fingerprint is a fingerprint, plus I would think we'd want seraphis compatible wallets to be out and available to use longer than a few weeks
<rbrunner7[m]> I am pretty sure anyway we will simply have to try things, and if something does not work, which will probably be the case several times, backtrack, regroup and try something else. So we can let this question develop and mature.
<jberman[m]> > Is that the famous optimism of the youth? :) If true I would say go for it!
<jberman[m]> I hope not haha, the meat of it is already done, it's just gluing stuff together
<rbrunner7[m]> Hmm, curious to hear UkoeHB 's feedback after reading this log. Having `wallet2` somehow still inside the first Seraphis release is a big ugly toad to swallod
<rbrunner7[m]> *swallow
<dangerousfreedom> Haha yeah
<jberman[m]> yea :/
<rbrunner7[m]> But maybe not the last surprising insight of this caliber, as we move along and things slowly slowly become clearer
<rbrunner7[m]> Ok, very interesting, let's see how you progress with that, jberman 
<rbrunner7[m]> One would think there must be some insanely clever trick to avoid that without causing havoc ...
<rbrunner7[m]> Something for sleepless nights :)
<dangerousfreedom> jberman[m]: if you want, you can use a poor prototype I have to open/close a wallet2/wallet3 and try to build something on it.
<dangerousfreedom> Dont know if it is useful
<rbrunner7[m]> Alright, anything else to discuss today?
<jberman[m]> dangerousfreedom[m]: is that code along the lines of what we were discussing last meeting? isolated code that can read the wallet files wallet2 uses?
<dangerousfreedom> I did it once, just trimmed down the most basic code to read a wallet2 file
<dangerousfreedom> Wait a sec, I guess I deleted the branch I will have to upload again if I did. One minute
<jberman[m]> will take a look/think on it :)
<rbrunner7[m]> I think for the general audience we can close the meeting here a bit early. Thanks for attending!
````


# Action History
- Created by: rbrunner7 | 2023-02-24T16:28:54+00:00
- Closed at: 2023-03-03T20:20:36+00:00
