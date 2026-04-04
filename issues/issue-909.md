---
title: 'Seraphis wallet workgroup meeting #41 - Monday, 2023-10-16, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/909
author: rbrunner7
assignees: []
labels: []
created_at: '2023-10-13T15:18:00+00:00'
updated_at: '2023-10-16T18:50:35+00:00'
type: issue
status: closed
closed_at: '2023-10-16T18:50:35+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/907

# Discussion History
## rbrunner7 | 2023-10-16T18:50:35+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/909
<d​angerousfreedom> Hello
<j​berman> hello
<j​effro256> Howdy
<plowsof> waves
<kevino> waves
<r​brunner7> So, what's there to report?
<r​brunner7> Nice to see jeffro256 around today
<j​effro256> Thanks, I need to keep better track of when the meetings are going to happen, I miss them a lot accidentally
<r​brunner7> Well, I hope the number of meetings is still reasonable :)
<j​berman> Submitted final TODO's on background sync PR 8619, submitted a PR to convert legacy tx outputs into Seraphis lib compatible "enotes" which is useful for scanning legacy txs  with the Seraphis lib (https://github.com/seraphis-migration/monero/pull/11), started exploring integrating the rust full chain membership proofs into the monero repo, and high on my list is taking a look at dangerousfreedom 's PR this week
<jeffro256> +1
<d​angerousfreedom> I didnt do much last week. I started looking at jberman background-sync and I'm struggling to accept the idea of the possibility of having the same password for the bg-sync. I'm trying to generate an automatic script to initialize the bg-sync with the same password considering that my private-keys wont be stolen if someone gets access to my computer. Maybe I should create a passwo<clipped 
<d​angerousfreedom> rd manager somehow...
<r​brunner7> I wasn't well last week and couldn't do the reviews I had hoped for. But I did have a first look at dangerousfreedom 's PR: https://github.com/seraphis-migration/monero/pull/1
<r​brunner7> I have some comments to that.
<r​brunner7> The code in there does a lot of things, and a lot of quite different things. I think in this form we will get into troubles when discussing any review results in no time.
<r​brunner7> I think what would be much easier to work through would be series of PRs, maybe 5 or so for 5 areas touched, with narrow focus.
<r​brunner7> We could then also discuss with a good focus, if you know what I mean.
<d​angerousfreedom> Yeah that's a good point. I'm expecting actually a more high level comment about the direction it is going. I see three components that would necessarily need to be there. This TransactionHistory (to store tx info like ephemeral_keys), EnoteStore (to store enotes), KeyContainer (to store the private/public keys)
<d​angerousfreedom> It is really basic what I did
<j​effro256> I could be misunderstanding the design, but doesn’t it isn’t the password that’s stored, it’s a chacha key derived from the main chacha key yeah?
<d​angerousfreedom> But I think that should be direction. So we have things in a modular way
<r​brunner7> Not sure I understand. I think it should be well possible to make a PR with only the TransactionHistory stuff, and pretty much nothing else.
<r​brunner7> Just as an example.
<d​angerousfreedom> Yes, that would be possible. Then the knowledge proofs depend on the TransactionHistory
<j​berman> this is right. when the user chooses the background sync option ReusePassword, the encryption key used to encrypt the background cache and keys filed is derived from the root `m_cache_key` which is derived from the user's wallet password
<r​brunner7> At least for me it would be a boon to have only that one component in front of me to look at, and then meditate on that :)
<j​berman> the reason it's like that is that it enables a wallet to call `start_background_sync` without requiring user input their password, since `m_cache_key` is available in memory
<d​angerousfreedom> Yeah, but if I have to initialize the wallet.background file, I need to enter the same password of my wallet. So how do I hide that in a way that if it gets compromised then I dont compromise my wallet file?
<j​berman> actually that was the initial reasoning behind it, I could just use a separate key in all cases now given how it's designed
<j​berman> ah right, ya I was concerned about that too
<j​effro256> I think transactionhistory and enote store can be merged, since what we really care about are enotes, and transactions are “attached” to those
<j​berman> ideally you wouldn't use the background sync option "ReusePassword" if that's your goal, you would use the other CustomPassword option
<r​brunner7> I see a second problem with dangerousfreedom 's PR. It now modifies things that belong to the Seraphis library. I know that this would add to your work, and complicate coordination, but I strongly advice to PR that to the Seraphis library repository.
<r​brunner7> I think we get into merge hell if we make Seraphis library changes directly in our repository.
<d​angerousfreedom> Yeah sure. Actually some of the stuff were already PR'ed into Seraphis but I will review again.
<r​brunner7> Anyway, I can say that if you do make small and focussed PRs I will do my best to review quickly, so things can move forward.
<j​effro256> Are you feeling any better this week?
<r​brunner7> Yeah, thanks for asking :)
<jberman> +1
<dangerousfreedom> +1
<jeffro256> +1
<j​effro256> Is there more stuff which can be PR’ed into Seraphis library by itself from that PR without affecting the behavior otherwise ?
<d​angerousfreedom> Yeah okay. I considering someone lazy and stupid (a lot of times myself) that would just use it in the most lazy and wrong way :p
<r​brunner7> A quick question about your wallet2 reading PR, jeffro256 : Not sure you are aware with all that stuff you juggle, but I deposited a question there, that story about reading ASCII files.
<r​brunner7> What would you say, we merge now and you care about that in a later, separate PR?
<r​brunner7> That wallet2 stuff is very handy, and dangerousfreedom needs it
<d​angerousfreedom> I will double check again this week and will separate the dependencies.
<rbrunner7> +1
<d​angerousfreedom> Well I need it for some knowledge_proof stuff but since we agreed to separate the PR then I will do it this week.
<j​effro256> Yes sorry I saw that and I’ve meant to get to that, but I was putting Seraphis stuff on hold this last week and a half. I was working with Rucknium on OSPEAD and fixing a minor decoy selection statistical issue
<plowsof> +1
<r​brunner7> Well, I think it's ok except for that little problem, we could merge and write an issue somewhere to document the "To do" if you are ok with that
<r​ucknium> Right. wallet2's decoy selection algorithm looks a lot less mysterious now.
<plowsof> +1
<dangerousfreedom> +1
<r​brunner7> Drop me a note about it :)
<r​brunner7> Just thinking. We are nearing a full year of work on the wallet, and meetings here. What would people say about a Reddit post written by me to give an update to the broad public?
<plowsof> +1
<r​brunner7> I recently answered a question about a possible time horizon for the hardfork to Seraphis, and it got a lot of attention / upvotes. I think interest is there.
<r​brunner7> Quite in general, not a lot of info from the "dev scene" makes it to Reddit ...
<d​angerousfreedom> Yeah sure. We dont have much to show but we are steadily gathering consensus about what to do :)
<j​effro256> Yeah also a call for developers could also maybe be a good idea. We’ve got a lot of good people working on it, but we could use more reviewers, testers, and people able to write higher level utilities
<dangerousfreedom> +1
<r​brunner7> We had one such call, already months back, for what it's worth. But yeah, certainly a good idea to mention that if I do write an update
<jeffro256> +1
<r​brunner7> February: https://www.getmonero.org/2023/02/02/seraphis-jamtis-developer-opportunities.html
<r​brunner7> Waiting for the "But who reads our blog" comments :)
<r​brunner7> Alright. We do pick up speed now, definitely.
<r​brunner7> Anything else to discuss today?
<r​brunner7> Doesn't look like it. thanks for attending, read you again next week.
<d​angerousfreedom> Thank you rbrunner7 !
<j​effro256> Thanks
````


# Action History
- Created by: rbrunner7 | 2023-10-13T15:18:00+00:00
- Closed at: 2023-10-16T18:50:35+00:00
