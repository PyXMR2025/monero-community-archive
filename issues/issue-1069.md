---
title: 'Monero Tech Meeting #86 - Monday, 2024-09-09, 18:00'
source_url: https://github.com/monero-project/meta/issues/1069
author: rbrunner7
assignees: []
labels: []
created_at: '2024-09-06T14:41:13+00:00'
updated_at: '2024-09-09T18:46:45+00:00'
type: issue
status: closed
closed_at: '2024-09-09T18:46:45+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1066).


# Discussion History
## rbrunner7 | 2024-09-09T18:46:45+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1069
<s​needlewoods> hey
<tobtoht_> Hi
<d​angerousfreedom> Hi
<r​brunner7> Welcome back :)
<d​angerousfreedom> Not so fast, I have some (good or bad) news haha
<j​berman> *waves*
<d​angerousfreedom> So, I engaged in some personal projects and won't be able to dedicate much time to Monero for one year at least. Therefore, I have to give up my CCS and apologize to everyone who donated for it. I'm sure plowsof  and ofrnxmr  will find good projects to redirect the funds. I dont feel really bad because the project changed quite a bit since I proposed and I'm sure jeffro256 , jberm<clipp
<d​angerousfreedom> an , SNeedlewoods  , kayabanerve , tobtoht , rbrunner7 and the others here will deliver a great wallet for the FCMP update. With that said, it means that I won't be active in the group meetings anymore but will be improving my skills and will try to contribute whenever I can. In the end privacy wins, otherwise it is not the end yet :)
<sneedlewoods> +1
<jeffro256> +1
<syntheticbird> +1
<rucknium> +1
<ofrnxmr> +1
<j​effro256> howdy
<r​brunner7> dangerousfreedom: Thanks for the frank reports. Things like that happen. I am sure you will be able to coordinate with plowsof about the funds.
<dangerousfreedom> +1
<k​ayabanerve> *waves*
<j​effro256> dangerousfreedom: I'm sad to see you go, but I wish you the best of luck in your personal projects ;)
<dangerousfreedom> +1
<r​brunner7> Do you have anything to release, even if pretty rough and unfinished?
<s​needlewoods> happy for you, sad for us dangerousfreedom
<dangerousfreedom> +1
<k​ayabanerve> Really sorry to hear df, but I really appreciate your honesty in the manner :)
<dangerousfreedom> +1
<j​berman> Ditto @jeffro256 , that's an unfortunate loss for us :( best of luck @dangerousfreedom
<dangerousfreedom> +1
<r​brunner7> Well, that year may be over faster that you are able to blink a few times :)
<r​brunner7> And Monero will wait for you, I am sure
<d​angerousfreedom> Well, I was writing my understanding about FCMP but did not finish yet. My contribution will be to update the monero-inflation-checker with some resources of FCMP when it is live. I will continue working on that project and continue to 'audit' Monero in my way for my understanding (at least).
<jeffro256> +1
<jberman> +1
<r​brunner7> Nice.
<s​yntheticbird> I'll write a hall of fame website just for you (you can't refuse)
<dangerousfreedom> +1
<sneedlewoods> +1
<jberman> +1
<r​brunner7> Alright, what do other people have to report
<tobtoht_> More progress on fcmp++ release builds. All targets now build and are reproducible on x86_64 based machines. There is some complex non-determinism when building on aarch64 that I hope I'll be able to resolve without hacks.
<s​needlewoods> Working on rbrunners review comments and suggestions [here](https://github.com/monero-project/monero/pull/9464). Again really appreciate the feedback, it's very motivating.
<s​needlewoods> Last commit was not really push-worthy, but still wanted to share the current state.
<s​needlewoods> In regards to our conversation about `EnoteDetails` and `TransactionInfo` I made some progress, but due to sub-optimal time management I can't adequately comment how that will go yet. Though I think with further iterations and some feedback it should be achievable in a reasonable amount of time.
<r​brunner7> SNeedlewoods: More and more I feel thankful that you march on despite the work balooning under your hands and getting more complex. Other people might have thrown in the towel already.
<j​effro256> I have quotes/proposals back from all auditors that acknowledged my requests (4) to audit Carrot. Implemented kayaba's feedback into the spec document, hoping to PR the integration within the next week
<r​brunner7> So it's auditor decision week?
<j​berman> me: implemented trimming the curve trees tree on reorg/pop blocks, all tests now passing, doing some touch-ups. I've been working over in this fcmp++-devel branch and my thinking is to push when I complete a task like this and update the PR description accordingly: https://github.com/j-berman/monero/commits/fcmp%2B%2B-devel/
<r​brunner7> jberman: Now with df taking a sabbathical, I think there is no lack of work for you after this PR ...
<j​effro256> Seconding rbrunner7 . I'm impressed at the amount of work SNeedlewoods has put into this new API, even though I haven't yet allotted time to sit down and review it in detail (my bad)
<j​effro256> Aren't you excited Justin???????????
<r​brunner7> Lol
<j​berman> +1 this @SNeedlewoods thank you very much for pushing this forward, very grateful. I'm also sorry I haven't dug deeper into it I feel like I have a large backlog of review to get through
<s​needlewoods> I'll give my best, honestly would love to do more, but with real live jobs and responsibilities it can get stressful because of high expectations for myself
<j​berman> *laughs*
<r​brunner7> Don't worry, often complex design work needs time. You can't just rush it, even if you had more time probably.
<j​effro256> Yup, there's always review backlog in Monero, but now it feels 5x worse that a lot of devs are tied up writing new code related to the FCMP++ upgrade whether that be crypto, core integration, build architecture, wallet API changes, etc
<j​effro256> It will get done eventually (maybe)
<r​brunner7> After "the video", I guess there will be serious attempts to build trees wallet-side? Where do we currently stand there?
<s​yntheticbird> It will get done.*
<s​yntheticbird> because you guys are the best, don't give up
<j​effro256> Once I can take a breather after Carrot integration, wallet-side trees will be the first thing I work on if it isn't yet taken
<jberman> +1
<r​brunner7> Splendid. I think people will be glad to hear that. For some people the video was quite a downer, especially people who are not following technicals or the "Breaking Monero" videos closely
<r​brunner7> Regarding review, maybe people could be a tad more pro-active mentioning long-waiting PRs in the -dev room, as a step towards improving the situation?
<j​effro256> It was all known attacks which is good, the only really surprising thing to me was the depth of traffic knowledge Chainalysis had at their fingertips
<r​brunner7> Not nagging of course, just informing, not everybody hunts through the open PRs in search of something to review
<j​effro256> Yes
<j​effro256> It would be nice if Github had a vote system for open PRs so that people looking to perform review work could quickly glance and see which PRs are desired the most / need review the most
<s​needlewoods> I feel guilty of not reviewing enough
<j​effro256> I feel bad for vtnerd since he's got a lot of really important outstanding PRs that do need a lot of review, that would get a lot of attention in another other time besides preparing for a hard fork
<r​brunner7> Is that really missing? There may be tons of overlooked features?
<r​brunner7> (on GitHub)
<j​effro256> I feel bad for vtnerd since he's got a lot of really important outstanding PRs that do need a lot of review, that would get a lot of attention in any other time besides preparing for a hard fork
<r​brunner7> Yeah, it's almost as if you get punished for doing complex work ...
<r​brunner7> Which is of course quite unfortunate
<tobtoht_> jeffro256: sorting PRs by thumbs up and hearts is possible
<j​effro256> oh nice I didn't know that
<j​effro256> thanks
<r​brunner7> But well, some of them are also decidedly non-trivial to review, I guess
<r​brunner7> Ok. Any special additional subject to discuss today? Maybe not, with everybody being working so busily :)
<s​needlewoods> Nothing from me
<j​effro256> Should I propose putting Carrot proposal discussion on the agenda for Wednesday or is that too short of a notice?
<r​brunner7> Hmm. I would propose. People can move it 1 week if they feel like it in the meeting, IMHO.
<j​berman> Wednesday discussion sounds good to me
<j​effro256> Yeah we don't have to decide immediately obv
<r​brunner7> Well then. Thanks everybody for attending, read you again next week!
<s​needlewoods> thank you guys, bye
<j​effro256> Thanks everybody!
<d​angerousfreedom> Before I go, I want to emphasize that it was really a pleasure meeting each of you. I have worked in some places and traveled quite a bit and can say that it is really hard to see brilliant and dedicated people like you guys. Keep strong on your side and I will keep improving on my side. See you someday ;)
<sneedlewoods> +1
<r​brunner7> Word.
<r​brunner7> Come back, don't dare to become self-sufficient farmer on some remote island instead :)
<dangerousfreedom> +1
<j​berman> Will miss you @dangerousfreedom hope that day is soon!!
<k​ayabanerve> Even if wallet trees is done by time of fork, I do have to call for an RPC route for the path even if deprecated out of the box.
<o​frnxmr> dangerousfreedom @dangerousfreedom:monero.social:  see you around!
````


# Action History
- Created by: rbrunner7 | 2024-09-06T14:41:13+00:00
- Closed at: 2024-09-09T18:46:45+00:00
