---
title: Move Monero Project to GitLab before the Next Spawn of Satan buys them out
  too
source_url: https://github.com/monero-project/meta/issues/236
author: anonimal
assignees: []
labels: []
created_at: '2018-06-05T22:16:47+00:00'
updated_at: '2020-07-21T10:43:01+00:00'
type: issue
status: closed
closed_at: '2020-07-21T10:43:01+00:00'
---

# Original Description
At least two options:

1. We currently have the mirror https://github.com/monero-project/meta/issues/10 but this has proven to be difficult to adequately maintain for full-scale 24x7 usage (see also #235). If we move there, we'll need to have more resources on deck to maintain.
 
2. We may have the option to [move to a gitlab.com high-end plan for free](https://twitter.com/gitlab/status/1004033746897719298). If not, the lower-end plans may be suitable as well.

# Discussion History
## anonimal | 2018-06-05T22:17:33+00:00
Why move? At least two reasons: because of Microsoft's impeccable record of privacy, and because the "writing is on the wall" with their more-is-less approach to everything they've done since Windows 95.

We can either let time do the elaboration, or we can be prepared to keep ourselves afloat.

## el00ruobuob | 2018-06-05T22:36:18+00:00
2 Is not possible here:
> Open source projects: any project that uses a standard open source license and is non-commercial. It should not have paid support or paid contributors.

Better pay for a plan than loose @moneromooo-monero contributions. 

## SRCoughlin | 2018-06-05T22:41:19+00:00
Re: paid support. This is where we need to be pedantic about the community being the funding provider and not the project itself. So it's likely that this GitLab requirement is satisfied.

## el00ruobuob | 2018-06-05T22:54:16+00:00
It's walking on thin ice. IMO, no matter who is paying, contributors are paid to contribute. Are they referring to the project paying or to contributors who are paid? That's the question.

## anonimal | 2018-06-05T22:56:34+00:00
>This is where we need to be pedantic about the community being the funding provider and not the project itself. So it's likely that this GitLab requirement is satisfied.

Referencing #217. Hopefully that will help.

>Are they referring to the project paying or to contributors who are paid? That's the question.

Good point. They should be clearer. And do they recognize cryptocurrency as "payment"?

## el00ruobuob | 2018-06-05T22:57:38+00:00
"To have paid contributors" could mean "To have contributors who are paid" rather than "To pay contributors"

## anonimal | 2018-06-05T22:59:53+00:00
Another argument for moving: the massive centralization of open source repositories has always been a nagging hangnail in the back of mind since we started mirroring. If Monero Project aims to be decentralized, it would seem more fitting to host multiple self-hosted gitlab instances which are controlled by various members of the core team - but not all instances controlled by one or more core team members. I'm not suggesting that as our next step but as a possible long-term solution.

## ghost | 2018-06-06T20:58:15+00:00
I am strongly in favor of moving to Gitlab in light of this announcement, if such a move is possible.

There are many avenues for user and developer tracking available to Microsoft, which I expect them to use fully. I also expect them to cooperate (willingly or not) with government requests, which could easily be a serious threat to Monero's development and user base. For a privacy-oriented project, this is more likely than for most projects. 

For that matter, we should not trust Github alone, whether they are owned by Microsoft or not. Multiple self-hosted Gitlab instances is a good long term idea IMHO. 



## anonimal | 2018-06-06T21:20:04+00:00
>For that matter, we should not trust Github alone, whether they are owned by Microsoft or not. Multiple self-hosted Gitlab instances is a good long term idea IMHO.

Absolutely, I agree. This would also move us forward with #237.

## scottAnselmo | 2018-06-08T06:57:00+00:00
~~Out of curiosity has anyone contacted GitLab about Monero being considered eligible for GitLab Ultimate yet? Might get a quicker response if someone with a @getmonero.org does it or is handled by someone who is good at being...pedantic? I can shoot a quick and simple email if no one has already and at least we'll have that question answered.~~

~~Re: What are paid contributors... I can see people playing devil's advocate with bounties for Linux zero days, etc. that should be considered paid contributions. I think Monero aligns with the general spirit of the requirements and FLOSS. Worst case we can use CE and do an analysis on feature parity with GitHub to see if needs are met before migrating.~~ (Edit: commentary not relevant given self hosting is not feature constrained it seems)

Speaking more personally, GitLab does not allow you to hide your email currently...of which creating a quasi-burner email to counter any scraping may be an annoying upfront cost to contributors, but this may ultimately pale in comparison to the cons of continuing to use GitHub as a primary. https://gitlab.com/gitlab-org/gitlab-ce/issues/43521

## fluffypony | 2018-06-08T06:59:12+00:00
I think we should move to self-hosted, and then mirror out to GitHub and GitLab, otherwise we’re swapping one master out for another. You can disable most of the features on GH so people can’t submit PRs to that repo and so on.

## ghost | 2018-06-08T20:58:28+00:00
The biggest problem I can see with multiple self-hosted repos is issue tracking. This may be less of a problem for devs because things can be coordinated through IRC, but it could be a hassle for random users to figure out where to submit an issue, how to avoid duplicates, etc. 

If we rely solely on a  Github (or even Gitlab) mirror for issues, it's still a single point of failure/privacy issue. Directing people to a single self-hosted Gitlab instance would be better than using Github or Gitlab for privacy, though it would be an extra maintenance burden and still a single point of failure. 

## fluffypony | 2018-06-08T21:06:57+00:00
@jsfierro I don’t think anyone is suggesting we use GitLab.com except as a mirror (at least, I hope they aren’t!!) The self-hosted GitLab instance would be the master of everything, and issues / wiki / projects / PRs would be disabled on GitHub and GitLab.com

## ghost | 2018-06-08T21:15:10+00:00
@fluffypony 

OK, that sounds better. 

The long-term idea that @anonimal had about multiple self-hosted Gitlab instances spread among various devs is where I think we'd run into trouble, though I agree that it would be a good goal to move towards. 

## scottAnselmo | 2018-06-08T21:22:38+00:00
For what it's worth there's also the alternative of using Linux's Kernel bot that redirects people who try to contribute which may or may not be useful for us in redirecting people who don't read the readme to the selfhosted GitLab to file issues, etc:

> Thanks for your contribution to the Linux kernel!
> 
> Linux kernel development happens on mailing lists, rather than on GitHub - this GitHub repository is a read-only mirror that isn't used for accepting contributions. So that your change can become part of Linux, please email it to us as a patch.
> 
> [...]
> 
> This message was posted by a bot - if you have any questions or suggestions, please talk to my owners, @ajdlinux and @daxtens, or raise an issue at https://github.com/ajdlinux/KernelPRBot.

Source: https://www.reddit.com/r/linux/comments/8oh778/microsoft_acquires_github_for_75_billion/e03slb1/?utm_content=permalink&utm_medium=user&utm_source=reddit&utm_name=frontpage

## fluffypony | 2018-06-08T21:22:43+00:00
@jsfierro yeah multi-homing like that is pointless, it just creates confusion. The best thing we can do is completely centralise this, and then make backups available for download. Maybe we can even do incrementals, but even if it’s just a full daily dump it’s enough, people will download a copy every now and then even if it’s just for posterity. That way ANYONE can spin up a replacement, with PRs and issues, if that central source is taken offline.

## yrashk | 2018-06-14T21:04:19+00:00
@fluffypony totally shameless plug, but I'll be happy to show what [SIT](https://sit.fyi) can do in this regard -- you can actually have issues and merge requests to be free and independent of some central server -- i.e. downloaded and worked on as first-class citizens. Combined with the code repository, there are some very interesting things you can do with it -- like amending issues from within patches (great for dependent changes) or being able to see a snapshot of any issue for any revision.

## erciccione | 2018-06-25T09:12:43+00:00
I think the discussion on EFForg/https-everywhere#15615 contains some useful infos about this specific matter. Worth a read

## anonimal | 2018-09-07T08:38:18+00:00
Ironically, this happened a week before the code freeze of the first kovri release. One of the worst times for something like this to happen. Banned for days at a time because the Microsoft migration is going as planned.

https://twitter.com/whoisanonimal/status/1019360748491849728

![ban0](https://user-images.githubusercontent.com/12156341/45207516-ab531000-b277-11e8-9cb0-4f019c9cc6aa.jpg)

https://twitter.com/whoisanonimal/status/1019360971171614720

![ban1](https://user-images.githubusercontent.com/12156341/45207526-b312b480-b277-11e8-8212-919075fc31d4.jpg)

So, on `#monero-dev`:

```
2018-07-16 23:30:39     anonimal        For those not idling #kovri-dev, I've been blocked from logging into github at the IP level throughout this week, and today was 2FA. The 2FA block is the nail in the coffin.
2018-07-18 21:10:30     @fluffypony     [16:31:31] anonimal: I'll sit with pigeons and try figure out a plan
```

When Ric says something like that, 90% of the time it means nothing will happen until someone else does it (see the past 3 years of monero-project history for proof, the only time I can attest to) and the other 10% means something will happen within a year's timeframe if we're lucky (3 months on this issue alone so far).

For the time being, I've moved kovri to https://gitlab.com/kovri-project. From there I'll build out infrastructure as needed.  

For the worry-warts: Kovri/Monero code plans don't change, my FFS doesn't change, only development and community infrastructure changes.

## scottAnselmo | 2018-09-10T05:37:53+00:00
@anonimal Out of curiosity have you heard of anything similar happening on other FLOSS projects like Tor outside of what @erciccione linked to? If what you experienced is part of a larger trend on FLOSS on GitHub it may be worthwhile to start the Monero Project migration sooner than later (e.g. after some minor bug fix release after the October release rather than say, a year down the line). 

It is also worth noting that Debian, GNOME (who just had their first release that was "produced and verified using the CI infrastructure in GitLab") (LinuxJournal) and GNU have their own GitLab instances at this point. For better or worse, continuing to use proprietary infrastructure like GitHub while other FLOSS has moved off GitHub does send a certain message.

## erciccione | 2018-09-10T10:50:16+00:00
@sanecito Sia moved to gitlab as well and with good reasons: https://blog.sia.tech/moving-to-gitlab-4140773b376f

## erciccione | 2019-07-23T14:19:32+00:00
It's almost one year since we started testing the [self-hosted GitLab](https://repo.getmonero.org), i think **it's time to sum up the situation and decide how to move forward**. I'm gonna write down the results of this test according to my experience/opinion and what i think should be changed or introduced.

## How GitLab is doing
Beside a not-great UI and a weird notification system, i like GitLab and **i think we should go forward with the migration**, but we should solve the 'big deals in next section. The general UX for both maintainers and contributors can be greatly improved by using the various features that GitLab offers. I'm gonna talk about some of them briefly in this issue, but in general i think it's something we should talk about later, let's complete this migration first.

We encountered some issues during this year, but they were all fixed when met (thanks @moneromooo-monero), except for a minor one. Basically the reviews in one Merge Request on monero-site disappeared from one day to another without leaving trace. I and mooo investigated the problem, but there was nothing in the logs and we didn't manage to reproduce the bug. Since this happened only once and since then the hosted instance was updated to a new version with numerous bugfixes, i don't think we should worry much. There some other issues that i consider a big deal.
  
## The big deals
The issues are 2 and at the moment they create a bad user experience and make contributions much harder:

+ **SSH access is not working** (see [issue](https://repo.getmonero.org/monero-project/monero-site/issues/950) on Gitlab). This makes committing and access in general painful.
+ **Who joins repo.getmonero using their GitHub account find themselves unable to fork projects** and therefore contribute. This is particularly annoying because these users must be manually unlocked (usually by moneromooo) to be able to fork a repo. The problem is solved by asking people to create new accounts, but this is not optimal because (i) if they were following the project on GitHub, they now have to go to the process to create a new account on repo.getmonero and set it up (ii) this new account could have a different nickname, making harder to link gilab and github users.


## Project management
The Monero Project has a singular way to handle management in its repositories on GitHub. For example, all repos are owned by a fake user (Monero-project) instead of an organization and an issue-bot is used instead of the integrated labelling system that GitHub offers. Labelling system that is not consistently used. This could sound like a minor detail, but **it's very important to have a well organized repository, otherwise community involvement and the development workflow will be much harder**. I created not long ago a [very minimal triage system](https://repo.getmonero.org/monero-project/monero-site/boards) in the [issue board](https://repo.getmonero.org/monero-project/monero-site/issues) of the monero-site repo and the it's starting to have the first effects: **Issues are easier to consult and community members easily spot and pick up issues** labelled '[⛑️ help needed](https://repo.getmonero.org/monero-project/monero-site/issues?label_name%5B%5D=%E2%9B%91%EF%B8%8F++help+needed)'. This is a *very minimal* approach, i have many other ideas on how to improve the general management system of the project, but that's out of scope for this issue.

I think this migration to GitLab is good excuse to finally create a minimally organized and consistent system. Much can be done, but I think **we should start with the way repositories and contributors access is managed**, so that will be able to build everything else on top of that.

## So?

So, we should take a final decision about transferring the remaining repos on repo.getmonero. If we do, **i propose to introduce a minimal system that will provide a better approach on access management**.

I suggest to procede this way:

1. Create a [GitLab Group](https://docs.gitlab.com/ee/user/group/). Transfer all Monero repositories on repo.getmonero into this group.
2. Migrate into the GitLab Group the repositories from GitHub.com/monero-project. Now all repos are under the same top group.
3. Manage access control using groups. Subgroups should be created with this structure:

+ **Monero Project** - master group, where all the repos are hosted
  - **Core Team** - Members of this subgroup has 'owner' access (full power) to all repos in the master group
  - **GUI** - 1 member of the core team with 'owner' access (needed). All other members have '[reporter](https://docs.gitlab.com/ee/user/permissions.html#project-members-permissions)' status in the monero-gui repo (ideally, these are the same people with access to the labelbot on GitHub)
  - **CLI/Daemon** - same as above, but for the core repo
  - **CCS** - ^
  - **website** - ^
  - **?** - we can add as many subgroups as we think are necessary 

This is just a *bare minimal set up* aimed to mostly **simulate the access control situation we have on GitHub**, but using the feature gitlab offers and set a **more transparent and clear mangement**. In this system, subgroups member will take care of repositories and manage them (GUI group would take care of monero-gui, etc.), but only core members (members of the 'Core Team' subgroup) will have push access.

I have ideas to extend this system, but **i think we should agree on the base first**. Beside a clear and easy access control, this simple structure set the base for a better reviewing environment and make community participation easier.

This system make possible a lot of other options: Single members of groups can also be added with different access. For example: there is a new contributor that will like to help with the GUI and would like issues to be assigned to him/her. They can be added to the main 'Monero-Project' group as 'guest' and issues can be assigned to them. Subgroups are also a quick way to mention people; do you need the opinion of the GUI workgroup? ping them all in an issue/PR using @monero-project/GUI. Members of the group can assign issues to each other and label them, creating a more organized and clear dev environment.

**I would like to know the opinion of the community: are we all ok with migrating to gitlab?** because we should really make a decision now, having the project split in two platfroms is not nice. If yes, **what do you think about my proposal?**.

I'm available to assist the core team in this migration to apply the suggested process, if needed.

## erciccione | 2019-07-23T14:40:02+00:00
Just one consideration. If we decide to stay on GitHub, i think the way the access control and the reviewing system is managed should change anyway. I will wait to propose the changes until a decision about the migration will be made.

## sanderfoobar | 2019-07-23T14:45:42+00:00
nay for gitlab, it was a nice trial peroid but I am certain [gitea](https://gitea.io/en-us/) is a better fit for us.

## scottAnselmo | 2019-07-23T15:28:02+00:00
My one of two comments is that gitea seems to be missing some decent sized quality of life features according to their comparison page: https://docs.gitea.io/en-us/comparison/  The most prominent one being "related issues" which would help keep down the issue count and avoid duplicates.

My other comment would be that given GNOME, Purism, and other major FOSS players have migrated to GitLab, GitLab is more likely to be invested/contributed to thus further improved over other solutions like Gitea.

I defer to people who frequently commit to GUI, CLI, and website repo's on the ACL model for those for the most part (Edit: And on Gitea vs GitLab since they're the primary stakeholders). From an IT perspective, I think it would be best to have at least two core members rather than one to avoid single point of failure issues (hit by a bus, out on vacation, etc)

I would like to have issue close powers for meta in GitLab so as to keep it clean of old meetings, old infrastructure issues, etc., but that's just a random personal thing.

Edit: As highlighted by Sarang on IRC in -community, CCS and the sites repo would also have to be migrated if a non-GitLab route is taken which may pose some issues (namely CCS)

## el00ruobuob | 2019-07-23T17:26:40+00:00
I like @erciccione proposal. The website and CCS seems to be fitting well on gitlab, and with a well-managed permission system added on top of them, I am in favor of moving everything else out of github.  
Regarding the spof mentioned by @sanecito, I guess more than one core member should have write access to any sub project for vacation purposes, but I also hope that root credentials are also shared among some members, in case of bus (or boating) accidents...

## erciccione | 2019-07-27T09:15:11+00:00
From a brief conversation on `#monero-community` looks some community members would prefer to stay on GitHub, i don't agree, but i can understand. GitHub's UI and notification system are better than GitLab's.

Still, if we look the bigger picture is undeniable that a platform owned by Microsoft and that must operate according to the US legislation is not the best place to develop Monero, an universal technology that should have no borders.
This is happening in these days:
[GitHub starts blocking developers in countries facing US trade sanctions](https://www.zdnet.com/article/github-starts-blocking-developers-in-countries-facing-us-trade-sanctions/).

Monero is an open community and everyone should be encouraged to participate. Staying on GitHub means be forced to obey to what the US dictates, and Monero shouldn't care. People coming from places with economic sanctions are the ones who will need Monero the most. **We need to be on a self-hosted instance**, whatever it is.

I ask the core team to evaluate the situation and restart the discussion about the migration, because i have the feeling that will only be worse. @luigi1111 @fluffypony @articmine @binaryFate

edit: Beside which platform to choose. Now we have the repositories split between GitLab and GitHub and this fragmentation is not a good idea.

## erciccione | 2019-07-27T11:09:00+00:00
To reiterate: at the moment **Monero is not a fully permissionless and borderless technology**. People from **countries facing sanctions from the US cannot contribute to Monero's development as long as its codebase stays on GitHub**. These countries are: Crimea, Cuba, Iran, North Korea, and Syria ([source](https://help.github.com/en/articles/github-and-trade-controls#on-which-countries-and-territories-are-us-government-sanctions-applied)).

Let's keep in mind the people who needs Monero the most are the ones whose monetary freedom is limited.

*edit: corrected list of countries where sanctions applies and added source.*

## scottAnselmo | 2019-07-27T18:21:46+00:00
Yes for further context see this which seems to be the trigger point in the news cycle: 
![GitHubCensorship](https://user-images.githubusercontent.com/3056597/61998115-ea40ae80-b05f-11e9-91b6-40cd940b04c8.png)
Source: https://github.com/tkashkin/GameHub/issues/289
Decent news article: https://www.zdnet.com/article/github-starts-blocking-developers-in-countries-facing-us-trade-sanctions/

Because GitHub could arguably just as easily arbitrarily shutdown Monero out of privacy concerns for something like Department of Justice's Barr comments on encryption it's probably best to make GitLab self hosted primary ASAP so that project contributions are censorship resistant much like the Monero technology itself.

I'll ping fluffy and -dev in general to see if the current hosting provider is in a privacy respecting country.

## fluffypony | 2019-07-29T17:14:52+00:00
Sorry for the delay in replying to this, I've not been well. I support the move to GitLab, but bear in mind that the box is currently configured and maintained by @moneromooo-monero. If we're going to move everything over then I'd suggest we use the dedicated box that GloBee sponsors for the site / downloads, and have a separate Docker specifically for this, so that compromising one doesn't compromise the other. That box is currently configured / maintained by @danrmiller (pigeons) and hardened by the security team at Tari Labs, so it's pretty solid.

## dEBRUYNE-1 | 2019-07-30T13:56:04+00:00
>People from countries facing sanctions from the US cannot contribute to Monero's development as long as its codebase stays on GitHub. 

This is erroneous, see the clarification by Github's CEO:

>Public repos remain available to developers everywhere – open source repos are NOT affected.

https://twitter.com/natfriedman/status/1155311122137804801

Thus, **no one is currently excluded from contributing**, as Monero uses open source repositories. 

I am currently opposed to a move to GitLab, as (i) the user experience is currently subpar to Github and (ii) Github is kind of incumbent in the cryptocurrency ecosystem and developers are thus more familiar with it (I fear a switch to Gitlab will result in a drop off in code contributions). 

I do support setting up a mirror to back up the code. This would furthermore allow us to make an immediate switch in case sanctions do start to affect fully open source repositories. I personally do not see a benefit in switching as long as we are not affected. 

## selsta | 2019-07-30T14:12:01+00:00
Adding to @dEBRUYNE-1 points, moving to Gitlab would also result in yet another responsibility for pigeons / core team.

## lh1008 | 2019-07-31T21:25:04+00:00
Hey everyone,

I strongly support the migration of the Monero code. I'm not a coder, maybe my voice is quite silent in here but Monero shouldn't be at risk of any blockage by any jurisdiction. Is quite easy to say we are not at risk, but we are. 

I support @erciccione proposal, is the one that has been worked and tested for several months now. If other solutions come, I believe when the time is needed we will all work on it. 

## Thunderosa | 2019-07-31T22:09:41+00:00
At Monero Outreach we've been having our own broad discussion on decentralization. This has ranged from how to encourage miners to consider smaller pools, to publishing without permission and this; Microsoft's GitHub.

Like lh1008, I'm not a dev, just a script kiddie who's say should be take be taken with a grain of salt because we're not in the same trenches. But I do think we're all here sharing the principles and thinking that the best way to avoid evil is to not touch it in the first place.

I see this problem as an opportunity for Monero to lead by example, like it or not, we're looked up to in that way. Debruyne has a good point that it's not in the doorway because we're an open source project, and Anonimal has an equally valid point about the writing the wall. It's forever been a slippery slope, but it does seem that the floor has become more tilted than it's ever been and we'll need to decide sooner or later. But I'll contribute my time and ability to making it happen sooner.



## xmrhaelan | 2019-07-31T23:47:14+00:00
Earlier @fluffypony suggested it be self hosted, then mirrored on GitLab and GitHub. Are there self-hosting programs that are server-less? Could we build one? If possible that might be the most decentralized option, no?

I am also not a developer. Just a guy who cares about Monero :) 

Hoping the questions help the discussion.

## erciccione | 2019-08-01T08:43:00+00:00
> This is erroneous, see the clarification by Github's CEO:

You are right, this has been clarified by @hyc during the last dev meeting, i forgot to update that post. The point is that this is still a very fragile situation. Tomorrow GitHub or the US could make stricter rules about the definition of "commercial partner" and as a result repositories will be closed down with no warning. For example, what would happen if a project pay for a github integration (in the marketplace)? Even just doing that would put a project at risk of being erased, because now you became a commercial partner of GitHub without even realizing it. It's really too risky, we should stay on a self-hosted instance where we make our own rules.

> I am currently opposed to a move to GitLab, as (i) the user experience is currently subpar to Github and (ii) Github is kind of incumbent in the cryptocurrency ecosystem and developers are thus more familiar with it (I fear a switch to Gitlab will result in a drop off in code contributions)

About (i), yes i agree GitHub has a better UI at the moment, but gitlab has some nice features that GitHub doesn't have. I don't agree with (ii). Since GitHub was bought by microsoft a huge number of repositories moved to gitlab and also some cryptocurrencies.
I also don't think that a switch to gitlab would result in less contributions. monero-site has the same active ocmmunity members as in past and actually more contributors now than when it was on GitHub. The new CCS repository on GitLab is heavily used by the community (much more than the old forum).

> I do support setting up a mirror to back up the code. This would furthermore allow us to make an immediate switch in case sanctions do start to affect fully open source repositories

This could result in loss of pull requests and issues, but beside, i think staying on GitHub with the fear that from one day to another we have to migrate to another platform is a bad idea. In that case we will have a community that will suddently have to switch and actively use another platform. But the point is that we cannot just "wait and hope" while there is fire all around us, expecially since the only strong reason i've seen until now supporting staying on GitHub is that it has a better user interface. 

> Adding to @dEBRUYNE-1 points, moving to Gitlab would also result in yet another responsibility for pigeons / core team.

@selsta I don't see this as a valid point. At the moment pigeons and the core team + moneromooo already maintain the gitlab instance and @luigi1111 has stated that is unlickely for him that the repos now on gitlab would move back to GitHub. I would argue that maintain the development on both GitLab and GitHub is more cumbersome than move to a single instance (beside the fact that have our repos on two different platform isn't good for contributors).

> Are there self-hosting programs that are server-less? Could we build one? If possible that might be the most decentralized option, no?

@xmrhaelan What you are looking for is a federated git platform and at the moment there isn't such a thing (at least not stable enough to be used for a project like Monero). Yes, that would be the optimal choice.

## fluffypony | 2019-10-31T14:13:40+00:00
To add to @erciccione's response, git itself is already decentralised in that everyone that clones the repo has the code and it's history, so there are literally tens of thousands of copies of Monero's code out there. The thing that GitHub provides is the ability to easily manage pull requests (ie. new code patches submitted by developers) as well as the discussion around them, including the discussion we're having right now.

I must admit that our self-hosted GitLab's fork-and-PR process feels a LOT chunkier than GitHub's. I worry that the added friction will make it difficult for first-time and/or less experienced developers to contribute - perhaps we could try and get a few first-time contributors to try submit a PR to the website (which is already on GitLab) and get feedback on their experience?

## lh1008 | 2019-11-02T22:32:48+00:00
We could try it out as @fluffypony says.

## erciccione | 2019-11-09T10:19:38+00:00
> I must admit that our self-hosted GitLab's fork-and-PR process feels a LOT chunkier than GitHub

I think what feels chunkier is the UI of the notification system, which is much more intruitive and immediate on GitHub. Forking and PR is IMO the same as on GitHub (except for this issue: https://repo.getmonero.org/monero-project/monero-site/issues/998).

> I worry that the added friction will make it difficult for first-time and/or less experienced developers to contribute

Worth noting that repo.getmonero is used by Merchants submitting their business for listing on the Merchant page of the website (roughly about 4-5 merchants each month). These people are often non tech-savy, register for the first time and seem to find no problem in opening issues and keeping track of them. They also use with no problems the issue template specifically created for merchants.

## binaryFate | 2019-11-13T04:56:06+00:00
> Worth noting that repo.getmonero is used by Merchants submitting their business for listing on the Merchant page of the website (roughly about 4-5 merchants each month). These people are often non tech-savy, register for the first time and seem to find no problem in opening issues and keeping track of them.

Unlike other contributors they have an economic incentive to figure things out though.

## selsta | 2020-01-09T19:38:18+00:00
After spending a bit more time with Gitlab (and Gitlab CI) here are some limitations / points I’ve found.

- Gitlab CI does not work on merge requests. This is a huge limitation, seeing if something compiles **before** merging is its main use case. More info: https://gitlab.com/gitlab-org/gitlab-foss/issues/23902
- Github Actions, Travis CI (which we both currently use) have no GitLab integration. I’ve looked into Azure Pipelines, Cirrus CI, Circle CI, but it appears there is also also no proper integration. There is AppVeyor but it only includes 1 concurrent job for open source project.
- No git SSH support, would apparently require Cloudflare.
- No approve PR button in the CE edition. We could apply for a commercial license.
- Self hosted means keeping up to date with GitLab Critical Security Release, something we don’t have to worry about with GitHub.

## erciccione | 2020-03-27T14:14:40+00:00
I meant to make this comment earlier, but i managed to do it only now, apologies.

About migrating to GitLab, after months of testing and heavy use of the platform i changed my mind and now **i too agree that we should move back at least the monero-site repo to GitHub.**

Even if i still believe that staying on GitHub is far from ideal and there are good chances that could result in future problems, even if i stand behind the points i made in past (starting from https://github.com/monero-project/meta/issues/236#issuecomment-514230593 ), i think moving back to GitHub is the best option we have at the moment for the following reasons:

- The ideal solution would be a federated git platform, but that doesn't exist (even if git itself is federated)
- The best second solution would be a self hosted platform, but at the moment the existing ones do not deliver the same quality as GitHub does (i will talk about the problems of the self-hosted gitlab in the next paragraphs) or are fairly new and cannot be trusted to host a sensitive project as Monero is.
- Gitlab misses some important features and have some critical problems that oversize the positive aspects.

Specifically about the last point, @selsta mentions some missing features, which is annoying to not have, but the biggest problems in my opinion are:

- Gitlab CI is simply stupid. Not giving the possibility to test incoming Pull Request is probably the biggest deal breaker that would make our development workflow much harder. This is not a huge issue for the website, but it is for the rest of our resources (CLI, GUI, etc). Gitlab is aware of this problem, but they left it unresolved for years, and it still is.

- The platform is often ignored by other developers. This is not strictly gitlab related, but having all the main repositories on GitHub and then a single one on Gitlab creates a separation between the 2 dev environments, which causes people to ignore gitlab, especially if they need to subscribe to it when they are already on GitHub. This leads to much less dev activity on Gitlab.

- Clunky 2 factors authentication process. This is an important security measure that it's extremely annoying to use on Gitlab because it changes the way git is used locally. Specifically, it requires people to use a Personal Access Token instead of their password. This doesn't help not technical people to use it. The process is instead very simple on GitHub.

- No SSH, as selsta pointed out that's broken and makes the life harder for people who often push content on the repo.

- Gitlab, the company, seem to have became much more business oriented than it was before. Many features which are loudly asked by the community are stuck for years, while enterprise facing features keep being added.

So, in definitive, i would have been ok with having less features if in exchange we would have received our own functional platform, but this is not the case and for me the broken CI which haven't been fixed in years is the deal breaker. GitHub is also constantly delivering new and cool features that will make our dev workflows easier and faster. Gitlab on the countrary, is very slow and static from that point of view and as i mentioned, they seem to be more focused on businesses.

To reiterate, even if i'm not enthusiast at all about it, i think would be better to just move back to GitHub, but creating a good backup system for issues and history in general, in case we decide to switch to a better solution in the future and we should if we find a better alternative.

## ghost | 2020-04-17T16:41:43+00:00
I was disappointed with this news (I got from RSS feed) but now I see the reasoning is logical. Hopefully there will be better solution in future or Gitlab gets better at listening to community.

Thank you for being transparent about little things like this. <3

## erciccione | 2020-04-24T09:07:55+00:00
For the records: The monero-site repository has migrated back to GItHub. The transfer was tracked on https://github.com/monero-project/monero-site/issues/894 and announced on getmonero: https://web.getmonero.org/2020/04/13/migration-github.html

The CCS-related repositories are staying on Gitlab.

## erciccione | 2020-07-21T10:28:19+00:00
Now that we migrated, this issue can be closed.

# Action History
- Created by: anonimal | 2018-06-05T22:16:47+00:00
- Closed at: 2020-07-21T10:43:01+00:00
