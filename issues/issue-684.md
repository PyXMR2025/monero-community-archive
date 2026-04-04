---
title: ' Monero Dev Meeting: v15 network upgrade - Sat 16 April 2022 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/684
author: erciccione
assignees: []
labels: []
created_at: '2022-04-03T06:33:59+00:00'
updated_at: '2022-04-18T13:20:16+00:00'
type: issue
status: closed
closed_at: '2022-04-18T13:20:16+00:00'
---

# Original Description
Dev meeting dedicated to the v15 network upgrade. We will check the status of the network upgrade and decide on a date.

Last meeting (with logs): https://github.com/monero-project/meta/issues/680

#### Location

#monero-dev: [IRC/Libera](irc://irc.libera.chat/#monero-dev) and [Matrix](https://matrix.to/#/!VDQXWJoFsesLtbGdTT:monero.social)

#### Time and date

Saturday 16 April 2022 17:00 UTC. [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20220129T170000&p1=1440).

Expected duration: ~1h.

#### Topics in discussion

1. Greetings
2. Situation of multisig (https://github.com/monero-project/monero/pull/8149 and https://github.com/monero-project/monero/pull/8220). We have to decide how to do the review
3. Decide dates of the network upgrade
4. ?

Please let me know if you want to add/edit meeting items.

Chat log will be posted below after meeting has concluded.

#### Moderator

ErCiccione

# Discussion History
## rbrunner7 | 2022-04-17T05:21:50+00:00
```
ErCiccione> Hey folks, it's meeting time. The agenda is here:  https://github.com/monero-project/meta/issues/684
<ErCiccione> today we are going to see the status of the PRs that are going to go in for the network upgrade and especially the multisig PRs,
<ErCiccione> but first, a round of greetings to see who is here
<ErCiccione> Hello everyone!
<rbrunner> Hi there
<arnuschky> Hello there! RINO representative here. Just observing the proceedings ;)
<ErCiccione> We should set the date of the network upgrade today. I do hope there are more people around 🙂
<ErCiccione> hi arnuschky, thanks for being here
<jberman[m]> Hello
<xmrscott[m]> 'ello
<Rucknium[m]> Hi
<binaryFate> hello
<arnuschky> binaryFate should be floating around too, afaik
<arnuschky> ahah
<ErCiccione> ok, let's go on, hopefully more people will join later
<sech1> hello
<ErCiccione> so, the list of PRs are here: https://github.com/monero-project/meta/issues/680#issuecomment-1079924577
<rbrunner> A ping for UkoeHB ... maybe deep into programming, forgetting time :)
<ErCiccione> Bulletproof+ has been merged, so one it's done
<ErCiccione> View tags are approved, but need to be rebased and a final approval before they get merged: https://github.com/monero-project/monero/pull/8061
<ErCiccione> so i guess there isn't much to say about it. Correct?
<jberman[m]> On it
<kayabanerve[m]> Few minutes late, happy to be here :)
<ErCiccione> alright, then there are articmine's fee changes. We have one approval from https://github.com/monero-project/monero/pull/7819. This has been ready for quite a while and only needs to be merged i guess.
<ErCiccione> Could use another approval or two btw, then we only need to merge it. Any comments on #7819?
<selsta> 7819 is already in the merge list
<ErCiccione> perfect!, then the only real stuff left is multisig. Two PRs:  https://github.com/monero-project/monero/pull/8220 and https://github.com/monero-project/monero/pull/8149, but an intermediate PR is needed IIRC.
<rbrunner> Some more details are here: https://github.com/monero-project/monero/issues/8237
<ErCiccione> great link, thanks rbrunner
<arnuschky> Basically there is a mandatory one: https://github.com/monero-project/monero/pull/8149
<arnuschky> Ukoe rebased it already to BP+ but it's still missing view tags
<arnuschky> There are 4 "good to have ones": #8220, #????, #8203, #7852
<arnuschky> From what Ukoe said, #8149 is the only one with crypto changes, all the rest relates to the KEX protocol changes and cleanup
<arnuschky> (just repeating here what I gathered from Ukoe, since he's absent) He wrote  https://github.com/monero-project/monero/issues/8237
<rbrunner> And optimization, in the case of #8203
<ErCiccione> We still need to find somebody willing to review 8149's crypto
<ErCiccione> that's the main roadblocker that we haven't fixed yet
<kayabanerve[m]> I volunteered to review those and do intend to, probably around the 20th. I've been talking with koe a lot recently around multisig and so on as I recently implemented it in Rust (using FROST as the backend instead of DH).
<ErCiccione> kayabanerve: Sounds good. Would you implement the crypto part?
<ErCiccione> s/implement/review
<ErCiccione> well, "will you". I'm tired today 🙂
<UkoeHB> Hi sorry I’m late
<kayabanerve[m]> It's my plan. I also want to work towards versioning so we can ship upgrades outside of hardforks.
<UkoeHB> 8149 is going to need another review after rebasing, is vtnerd around and able to do it?
<UkoeHB> Just to check the rebase
<kayabanerve[m]> UkoeHB did version it IIRC using magic bytes, yet I'd optimally like that moved into an actual field where the protocol version used is the lowest of all participants (and then at hardfork we can ban old versions). That's for furthering development beyond this next set of changes though.
<ErCiccione> ok, good. So we have reviews planned for the key PRs. After those are done we can focus on the "good to have ones", i would say
<binaryFate> UkoeHB: currently I don't think he is available, I'm not sure when he'll be back
<ErCiccione> UkoeHB: As far as i understood, i don't think so
<ErCiccione> but kayabanerve is going to review, so at least we know someone is reviewing it
<ErCiccione> Does anyone have anything to talk about multisig?
<selsta> binaryFate: I think vtnerd said he is a bit available now, a couple hours per week
<binaryFate> nice
<ErCiccione> that's good news
<binaryFate> what about a review from Sarang? Provided he is willing and available
<ErCiccione> can somebody take care of contacting him and ask vtnerd if he is willing to do some reviews? Haven't seen him around these rooms lately
<UkoeHB> I don’t think that will happen
<ErCiccione> i find it unlikely too
<binaryFate> I will check with him 
<binaryFate> selsta: you contact vtnerd?
<ErCiccione> Anything to add? Otherwise the summary seems to be: everything mostly ready except multisig, which needs to be reviewed (+ review of the crypto)
<ErCiccione> I would say makes sense to set tentative dates?
<rbrunner> Any news already about the hardware wallet stuff?
<rbrunner> As I remember from the last meeting that can be a big unknown regarding dates ...
<selsta> vtnerd wrote in this channel a couple days ago
<ErCiccione> rbrunner: They need to have enough time to upgrade, for sure
<selsta> I still think that we might have to integrate it ourselves
<ErCiccione> IMO the important is to set dates, so that hw providers know there is a deadline
<rbrunner> And we also have a deadline for the other PRs that are still on their way
<rbrunner> The non-consensus / non-critical ones
<rbrunner> A little bit of pressure can work :)
<ErCiccione> yeah, i would say everything is ready to set dates. Anyone?
<rbrunner> Testnet in 1 month, Mainnet in 2?
<ErCiccione> This is how it was planned before we suspended it:
<ErCiccione> Branch/feature complete: Jan 15th, 2022
<ErCiccione> Release date: Feb 15th, 2022
<ErCiccione> Testnet hard-fork: Feb 1st, 2022
<ErCiccione> Stagenet hard-fork: Mar 1st, 2022
<ErCiccione> Mainnet hard-fork: Mar 15th, 2022
<ErCiccione> branch in a month from now, Release in two, Testnet in 3 and mainnet in 4?
<moneromooo> Previously, about one month (at least) was needed between release and fork. So a month between testnet and fork is not possible if you want the testnet to be useful.
<moneromooo> (useful being defined as, if something borked is seen on testnet, you can fix it before release)
<rbrunner> So Testnet hardfork before release, do I get this right?
<moneromooo> Yes, unless the idea is to assume nothing will break, and if something does, re-release and mainnet fork gets pushed back.
<moneromooo> Which, in fairness, it's unlikely to happen.
<rbrunner> We have for certain a number of breaking changes for sure, where other software needs to catch up
<rbrunner> Beside bugs we produced ourselves, I mean
<rbrunner> E.g. blockchain explorers, because of viewtags
<moneromooo> I'd fork testnet a few days after the last consensus PR is merged.
<moneromooo> Then once you've checked nothing breaks, you can set a fork date.
<moneromooo> Which you could have set before with a "assuming nothing goes boom" beforehand of course.
<ErCiccione> i see your point, but we do need to set the date of the hard fork as soon as possible. A couple of months before (which i assume would be the timeline) is not enough
<moneromooo> Then again, you need testers for testnet to be useful.
<sech1> testnet should be switched to v0.18 as soon as branch is created and PRs merged to it
<sech1> I actually need testnet to test p2pool with view tags
<ErCiccione> sounds good, i would still set a date for the mainneft hard fork the moment we set one for testnet
<ErCiccione> in case it can be pushed back, but people can start to get ready
<rbrunner> So maybe we can try to branch in 1 month, with Testnet fork, then release (hopefully) in 2 months, and fork mainnet in 3 months?
<moneromooo> I don't really have a horse in this, but you don't have to branch to fork testnet.
<sech1> yes, but all consensus changing PRs need to be merged before testnet
<ErCiccione> so, practically speaking. What about:... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/860e1f71107836fea38759ee5403a4216dfc5316)
<moneromooo> The branch has to come at/after the release, since its point is to avoid all the new changes to master, to have its own stable-plus-fixes history.
<rbrunner> Sound reasonable, yes.
<ErCiccione> we also need selsta's opinion on how to proceed. I assumed we were going to use the same process of past hard forks
<selsta> I didn't fully follow now
<rbrunner> Anyway, we will surely get that right with the order of things. I think we need to be comfortable and careful with the dates.
<selsta> moneromooo was involved in the most HFs so it's probably best to fork testnet first
<rbrunner> And man, if we don't manage to fork Mainnet in 3 months ... :)
<ErCiccione> Branch: May 16th
<ErCiccione> testnet fork: right after
<ErCiccione> release: June 16th
<ErCiccione> Mainnet for: July 16th
<ErCiccione> ?
<selsta> why not just fork testnet once we have everything consensus merged to master? we don't need a date for it
<sech1> yes, testnet fork can be done "when it's ready"
<sech1> even before 16th May
<ErCiccione> We could keep may 16th as the latest date? I do think we need to put a bit of pressure and a deadline helps a lot in making sure things don't get delayed
<rbrunner> But well, that may be our guestimate when everything is reviewed, rebased, and merged :)
<jberman[m]> AFAICT the last 3 consensus changing PR's are view tags + ring size bump + fee changes. Fee changes are in the merge queue. I'll rebase view tags + ring size bump today
<ErCiccione> yeah, more like "let's get everything done before may 16th"?
<ErCiccione> we could also say end of the month 🙂
<ErCiccione> if we are confident we can get everything merged within 2 weeks?
<ErCiccione> s
<ErCiccione> seems like it at least
<rbrunner> The multisig PR might take a bit longer, and although not "consensus" should be in IMHO
<sech1> Block 2668888 - 8:13:20 pm CEST | Saturday, July 16, 2022
<sech1> nice number
<sech1> and fork on Saturday like it used to be before
<rbrunner> That's a pretty convincing argument. 8's are lucky, after all.
<ErCiccione> Ok so to wrap up: Branch as soon as possible, but not later than May 16th. testnet fork right after branching, release June 16th and mainnet network upgrade July 16th?
<ErCiccione> a round of opinion on this and if we all agree we can set it
<binaryFate> sounds good
<sech1> yes
<UkoeHB> Btw I’m thinking we should aim for a seraphis hf on the 10yr anniversary, who’s with me?
<sech1> a bit too early to discuss it :D
<rbrunner> lol
<UkoeHB> Lol :p
<ErCiccione> selsta moneromooo? You ok with those dates?
<ErCiccione> lol one fork at the time 😛
<xmrscott[m]> A noble goal to be sure
<UkoeHB> Almost exactly 2yrs from today
<rbrunner> And not altogether impossible, I hope
<ErCiccione> Any last comments about the dates? Otherwise we can close here
<w[m]> And objections? 
<w[m]> * Any objections? 
<SerHack> It seems fine 
<ErCiccione> ok, let's close with these dates. Hopefully people will comment if they disagree or have better options
<ErCiccione> thanks everybody for being here today. The dates are:
<ErCiccione> Branch with all the needed PRs for the hard fork: May 16th
<ErCiccione> Network upgrade (hard fork) on testnet: right after
<ErCiccione> 0.18 release: June 16th
<ErCiccione> Network upgrade (hard fork on mainnet): 16th July, Block 2668888
```


# Action History
- Created by: erciccione | 2022-04-03T06:33:59+00:00
- Closed at: 2022-04-18T13:20:16+00:00
