---
title: 'Seraphis wallet workgroup meeting #9 - Monday, 2023-01-16'
source_url: https://github.com/monero-project/meta/issues/780
author: rbrunner7
assignees: []
labels: []
created_at: '2023-01-13T17:52:00+00:00'
updated_at: '2023-02-10T15:29:58+00:00'
type: issue
status: closed
closed_at: '2023-02-10T15:29:58+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #777

Beside things that other people want to bring up we could discuss the following two issues:

1. Do we agree on some comment formatting style for the code we write, and if yes, how could that look? Also see [this older issue](https://github.com/seraphis-migration/wallet3/issues/26) and the comments so far there
2. Do people see the term *account* used for two different things as a problem, and if yes, how could the solution look? For background, see [this new issue from today](https://github.com/seraphis-migration/wallet3/issues/44)

# Discussion History
## rbrunner7 | 2023-01-16T19:01:02+00:00
````
<one-horse-wagon[> Hello everyone!
<ghostway[m]> Hello to you too 
<rbrunner7[m]1> Hello, yeah, meeting time!
<rbrunner7[m]1> https://github.com/monero-project/meta/issues/780
<dangerousfreedom> Hello
<gingeropolous> ahoy
<jberman[m]> hello
<ofrnxmr[m]> Greetings
<rbrunner7[m]1> Anything to report from work done during the past week?
<rbrunner7[m]1> Alright, then. I prepared 2 things that we can talk about today. Both not terribly important, but maybe in the category "good we talked about it", at least once
<rbrunner7[m]1> The first is the question of this earlier issue:
<rbrunner7[m]1> https://github.com/seraphis-migration/wallet3/issues/26
<dangerousfreedom> From my side I'm still working on the knowledge proofs. I believe I will be able to present a first complete draft (all knowledge proofs implementations with unit_tests) by next week hopefully.
<ghostway[m]> +1
<rbrunner7[m]1> Sounds good, dangerousfreedom[m] !
<ghostway[m]> rbrunner7[m]1: I'd imagine doxygen with clang format would be okay, no? Just the familiar stuff
<rbrunner7[m]1> What those comments in "Doxygen style" look like can be seen e.g. here in this file of the existing Monero codebase:
<rbrunner7[m]1> https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.h
<jberman[m]> I used koe's Seraphis lib to scan a legacy testnet chain from scratch and recover a wallet's balance: https://github.com/j-berman/monero-cpp/commit/bb270104b83c4d660cecfe5122fcd0f98a6f01bd
<Rucknium[m]> +1
<JoshBabb[m]1> +1
<ghostway[m]> +1
<rbrunner7[m]1> +1
<dangerousfreedom> rbrunner7[m]: Koe changes the library every 5 days, everytime I sync with his library my code brokes. But I'm getting used to seraphis so I think it will be possible.
<dangerousfreedom> > <@ghostway[m]:libera.chat> > <@rbrunner7:monero.social> https://github.com/seraphis-migration/wallet3/issues/26
<dangerousfreedom> > 
<dangerousfreedom> > I'd imagine doxygen with clang format would be okay, no? Just the familiar stuff
<dangerousfreedom> I agree too.
<jberman[m]> I'm currently working on cleaning it up + the more production ready framework to handle multithreaded scanning, it's going smooth I think. No significant snags at this point and in discussions with UkoeHB , I've got a good approach to structuring the code I'm working through
<dangerousfreedom> And I believe Koe is doing that already
<rbrunner7[m]1> UkoeHB used something similar, but condensed, in his header files of the Seraphis library
<rbrunner7[m]1> I browsed the Doxygen manual and saw that the system itself is quite big, in its entirity:
<rbrunner7[m]1> https://doxygen.nl/manual/docblocks.html
<rbrunner7[m]1> Looks a bit like overkill to me.
<ghostway[m]> Yep, but using just a subset is still ok. The thing going for it is familiarity
<rbrunner7[m]1> I am not sure that what koe is doing would go through any Doxygen supporting tool - he drops the "@" markers - but maybe that's not terribly important?
<rbrunner7[m]1> More important to have more or less consistent comments in headers
<ghostway[m]> Yea. Llvm's source code is a good reference (sometimes)
<rbrunner7[m]1> Does or did somebody here actually use such tools, to "automatically generate documentation"? I think that would be a bit optimistic in the particular case of the Monero codebase
<dangerousfreedom> Yes. The thing that annoyed me the most in the beginning was the lack of specification for formatting. Auto-format does not work as Koe's standards are different from anything of the clang-format styles (LLVM, Google, Chromium, Mozilla, WebKit, Microsoft).
<rbrunner7[m]1> You mean that some tool automatically generates the frame for the comments from the C++ declaration?
<Rucknium[m]> I use roxygen for R. I'm not sure if that's the same thing. Almost everyone who is writing R packages uses roxygen
<Rucknium[m]> Do you want to be worse than R programmers? (we are pretty bad) ;)
<rbrunner7[m]1> Don't you, but that sounds probable.
<rbrunner7[m]1> *Don't know
<dangerousfreedom> It was Yes for ghostway comment.
<dangerousfreedom> Koe does not use any of these things and since he is maintaining the library and the standards I believe it wont be used either.
<rbrunner7[m]1> I share koe's feeling that those "@"s are just plain ugly, and I worry about the comments "rotting", e.g. if you add parameters with the comments already existing.
<rbrunner7[m]1> But maybe that's more a question of discipline then.
<dangerousfreedom> So the idea will be: follow the standard of the library which has no written standard :p
<rbrunner7[m]1> I tend to agree: That does not look too bad, and people seem to think it's useful. Tools are not seen as terribly important, as I get it.
<JoshBabb[m]1> doxygen-generated comments aren't terribly useful in my experience, but I appreciate them alongside a code styles and linting because they remind us to comment by providing a designated and pre-styled place for them
<JoshBabb[m]1> I appreciate code styles in that they help reduce merge conflicts.  I don't worry about tabs or spaces while coding
<JoshBabb[m]1> s/styles/style/
<rbrunner7[m]1> Ok, if nobody strongly objects, we land at a recommondation to more or less follow koe's style as visible in the header files of the Seraphis library, and as I said, "good that we talked about it" :)
<rbrunner7[m]1> Yeah, good point about reducing merge conflicts.
<UkoeHB> Yes I adjusted the comment formatting to be more pleasant
<rbrunner7[m]1> Alright.
<rbrunner7[m]1> Second thing I wanted to bring up today is a terminology question that I only became aware of recently. I described it here:
<rbrunner7[m]1> https://github.com/seraphis-migration/wallet3/issues/44
<rbrunner7[m]1> We have sort of a clash, with using account for at least 2 different things
<rbrunner7[m]1> And maybe we find a way to circumvent that
<rbrunner7[m]1> Without too many contortions
<rbrunner7[m]1> @tinyvoice commented that the use of account as a synonym for wallet is not very widespread in the world of Monero. Would you agree?
<JoshBabb[m]1> I agree, wallets may have multiple accounts, right?
<rbrunner7[m]1> Yes, that's the other use of the term.
<rbrunner7[m]1> And the clash would be a sentence like "An account can have multiple accounts" ...
<JoshBabb[m]1> Not everyone uses accounts nor subaddresses
<rbrunner7[m]1> As I mention in the issue, in the Monero codebase there is currently a class with a name of account in the first sense
<rbrunner7[m]1> Well, it's not a question who uses what, and how often, IMHO. I think we should not have the same name for two different things, if we can help ourselves.
<UkoeHB> Imo a wallet is a stateful thing, while an account is more abstract.
<UkoeHB> Calling the base keys your wallet creates ambiguity
<rbrunner7[m]1> Right. If only we had a nice and concise term for that "thing" that a single spend secret key controls ...
<rbrunner7[m]1> Not wallet of course
<JoshBabb[m]1> I understood accounts as like different derivation paths of the same seed.  How should they be described/understood?
<UkoeHB> JoshBabb[m]1: that’s how the word is usually used
<rbrunner7[m]1> Yes, that's what I mean. That's one thing that is called account, but there is a second
<UkoeHB> There is a ‘master account’ from which all ‘sub accounts’ are derived.
<JoshBabb[m]1> Are the differences between accounts and subaddresses relevant/helpful?  Will either approach be used or helpful under Seraphis?
<rbrunner7[m]1> No, it has nothing to do with subaddresses.
<rbrunner7[m]1> Just take a sentence where you have the word "wallet", and replace that with "account".
<rbrunner7[m]1> "Go into the GUI wallet, and select a file name to open your **account**"
<rbrunner7[m]1> (Just an example, I don't think our GUI wallet app uses the term like that=
<ghostway[m]> Accounts could be implemented as other addresses I imagine?
<rbrunner7[m]1> Pure terminology question that I mean here. Nothing to do whatsoever with implementation. Just two things called the same
<rbrunner7[m]1> with a potential for confusion
<rbrunner7[m]1> which I witnessed myself, on Reddit, and on IRC
<rbrunner7[m]1> One person talking about the one kind of account, the other person of the other kind, and misunderstanding resulting
<rbrunner7[m]1> You can also check this article: https://www.getmonero.org/resources/moneropedia/account.html
<JoshBabb[m]1> oughta edit that
<rbrunner7[m]1> Argues for account = wallet (the whole, full, single wallet)
<one-horse-wagon[> Technically, there is very little difference between the two terms--account and wallet.  I would suggest just getting rid of the term account and stick with wallets.
<rbrunner7[m]1> No big problem, but then we would also steer clear of that account class name we currently have in code, and use another name for the Seraphis equivalent
<rbrunner7[m]1> So account will always be subaccounts, compartments within a single wallet
<one-horse-wagon[> Could you not substitute sub-address for subaccounts?
<rbrunner7[m]1> jberman, dangerousfreedom[m] , what do you say about that class name proposal, to avoid *account* in the CryptoNote class sense?
<rbrunner7[m]1> one-horse-wagon: That's no good idea, because those are two clearly different things, and alright, because nothing clashes anywhere :)
<dangerousfreedom> I like the following hierarchy wallet->account->addresses
<dangerousfreedom> We wont have subaddresses anymore so I think it is a straight heirarchy
<rbrunner7[m]1> And something in code is only allowed to carry the name account if it's about accounts in this sense, right?
<dangerousfreedom> I guess so but then we would need to use the word wallet everywhere for the master keys
<dangerousfreedom> Thats a personal view
<rbrunner7[m]1> Exactly! Or come up with a better term for that class that manages keys!
<rbrunner7[m]1> I tried, but failed. Not the least because account always pops up and disturbs the thinking :)
<rbrunner7[m]1> But maybe something quite technical like key_container will do quite fine.
<rbrunner7[m]1> Ok, maybe no point in belaboring this more. We can let that sink in, and when coding reaches that point, we will see.
<dangerousfreedom> Yeah, I dont know :p
<rbrunner7[m]1> As I said, not terribly important, but not having the same term for two things would be nice :)
<rbrunner7[m]1> Alright, anybody with anything else they would like to mention?
<rbrunner7[m]1> If not, thanks to all for enduring my formatting and terminology musings, and until next week!
<jberman[m]> As was basically said, I feel the term "account" is used by users to describe the feature to divide wallets by accounts, and the CryptoNote class "account" is moreso used internally in the code and is not commonly understood by users to be anything but the former. At least that's been my impression
<jberman[m]> I would agree that it makes more sense to move toward changing the latter than the former to avoid confusing users
<jberman[m]> And I think key_container is an improvement
````


# Action History
- Created by: rbrunner7 | 2023-01-13T17:52:00+00:00
- Closed at: 2023-02-10T15:29:58+00:00
