---
title: 'Proposal: Disband Core'
source_url: https://github.com/monero-project/meta/issues/921
author: fluffypony
assignees: []
labels: []
created_at: '2023-11-05T14:02:23+00:00'
updated_at: '2024-07-23T20:32:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently the Monero Core Team is responsible for a number of things that are critical to Monero, and as a result there is a great level of trust implicit in them. For instance, a malicious Monero Core Team member could hijack the domain, and serve up malicious Monero downloads right after a new release. No matter how quickly this is detected, there will be many affected downloads, and could cause massive financial and privacy-related network damage. The recent CSS wallet incident is also an example of risks that the Core Team presents.

Additionally, this has been a thankless job that the Core Team has taken on (for no compensation), although even if there were compensation and constant praise it would still be a centralising force that we should try and eviscerate.

My suggestion, and I encourage us to use this thread to iterate on it in public, is to break the Core Team up into 6 self-assembling workgroups. This is not a complicated exercise, apart from the community coming to consensus as to who should form part of the workgroups. I would suggest we aim for a January 1st, 2024, cutover date for this.

Existing Core Team members can, naturally, choose to join a particular workgroup (or workgroups), if the community agrees they should. I, personally, will not be participating in any of these proposed working groups, and will use this as an opportunity to step back from any last vestiges of administrative involvement or perceived leadership in Monero.

Open questions that we should use this thread to answer is: (1) what should we use to quickly spin up some sort of loose consensus mechanism for the workgroups (eg. Strawpoll)? (2) how many members should be part of each workgroup?

Some basics that I think should be set in stone are: given the sensitivity of these workgroups, community members that do not have a long multi-year history should simply not be considered. Community members should also be familiar with secure communications platforms, GPG, and similar. Their GPG keys should preferably be a matter of public record already, or inserted into source tree as soon as possible. Many of the roles and responsibilities aren't just technical, but require building a deep relationship with service providers who are familiar with the sensitive nature of Monero's software and support the project's mission, so it would generally require individuals in those particular roles to not be abrasive, and to be warm and understanding and friendly with the individuals they deal with at those service providers. Finally, some of these workgroups simply CANNOT have any form of multisig / ACL / group access, and by definition each individual on the workgroup can exercise complete control and abuse their position (or be wrench-attacked, or be compromised). I've tried to note that below.

**General Donation Fund Workgroup**

This workgroup can use multisig to share control.

Responsible for determining what General Donation Funds should be spent on, and dispensing them. The download server and CDN are the primary recurring costs, and we have a whole structure setup that pays those monthly via card / wire transfer and is reimbursed by the GF. They can choose to continue to use that, or they can do their own thing.

**CCS Workgroup**

This workgroup can use multisig on the wallet, but some other aspects might inherently be more centralised.

Responsible for managing the CCS, approving proposals, managing milestones, etc. This obviously includes dispensing funds.

**IP and DNS Workgroup**

This workgroup can democratise some aspects of it, but ultimately there will need to have a super-administrator for both domains and DNS (this can be a shared account).

Responsible for IP (as in intellectual property) which includes domains, trademarks, copyrights, service marks, anything along those lines. They're mostly going to be responsible for renewing the domains on an annual basis, ensuring the domains aren't stolen / socially engineered (I built an extremely deep relationship with our registrar, Gandi, over the last decade to prevent these attacks which occur very frequently). For multiple reasons we use Cloudflare to handle the DNS (including their embracing and facilitating Tor routing and access from Tor exit nodes, and their exceptional DDoS prevention). Of course, this workgroup is welcome to transfer the domains somewhere else, as well as move the DNS elsewhere.

**Servers and CDN Workgroup**

This workgroup might be able to democratise some access, but as with the previous one there is a need for some super-administrator access (this can be a shared account).

Responsible for the CDN and server infrastructure. Currently there is a single, very beefy server on a 10gbps unmetered, well-peered uplink, that serves the Monero website and the downloads. We have a [well architected, hardened configuration](https://github.com/monero-project/meta/blob/master/SERVER_SETUP_HARDENING.md) that was designed by Gus, formerly of Tari Labs, and Dan (pigeons), from Cypherstack. The CDN is one that we specifically chose because it has a network of endpoints in China, and thus bypasses the Chinese GFW to serve the Monero website and downloads. Of course, this workgroup is absolutely entitled to move the infrastructure elsewhere, switch off the CDN, etc.

**Git Workgroup**

This workgroup likely can't democratise much at a high level (some nuance below), and will also require a super-administrator account (this can be a shared account).

Responsible for the monero-project GitHub organisation, managing GitHub issues and pull requests, managing maintainers, and managing releases. There is some democratisation in the form of individual repo access. In other words, an individual who isn't even part of the workgroup can be given write access (ie. maintainer role) on an individual repo. They are welcome to re-run the experiment we ran with self-hosted GitLab a few years ago, but I think we've demonstrated that GitHub is fine as a platform for collaboration, knowing that we will detect any malicious activity on GitHub's part really quickly as git acts almost as a blockchain, distributing the code (and its branches and history of changes) on the computers of thousands of Monero contributors and users.

**Community Channels Workgroup**

This workgroup can democratise some individual channels, but it will require a require a super-administrator account (this can be a shared account).

Responsible for managing the various community channels, like the Telegram groups, the subreddit, the IRC channels, etc. Obviously these channels already exist, and this workgroup might choose to fold the existing moderators of the subreddit (for instance) into the workgroup. They could also exist as a distinct workgroup, working with those moderators and letting them handle changes to their moderation team. They would generally be expected to maintain some of the guidelines and standards we have for community channels (eg. no price talk in most channels / forums, there are specific places for that) and ensure that these guidelines are largely accepted and enforced where relevant. They would also be responsible for some more sensitive things like controlling the Monero namespace on Libera (the IRC server we use), which is an elevated level of access that allows the workgroup to take over any channel that starts with "monero" (useful for channels that are trying to scam or impersonate).

# Discussion History
## jwinterm | 2023-11-05T14:23:15+00:00
Thank you for all the time and energy you have donated over the years. I think this seems like a good plan for an immediate course of action. My only comment would be that perhaps the GitHub Workgroup should be the Git Workgroup and needn't imply that the the MS hub of gits will always an forever be the holy source of original source code.

## fluffypony | 2023-11-05T14:28:19+00:00
> Thank you for all the time and energy you have donated over the years. I think this seems like a good plan for an immediate course of action. My only comment would be that perhaps the GitHub Workgroup should be the Git Workgroup and needn't imply that the the MS hub of gits will always an forever be the holy source of original source code.

Great catch, I'll edit the post to reflect the change in that proposed workgroup's name

## ACK-J | 2023-11-05T16:16:37+00:00
I appreciate everything core has done for monero over the years behind the scenes and support this proposal. 
Some thoughts on how these workgroups could function and be structured:
- Each workgroup could produce quarterly (Bi-annually?) community reports that provide updates on the decisions made along with reasoning behind them.
- Elections should consider candidates technical abilities as well as longstanding community involvement. I see vetting candidates to weed out malicious actors as a difficult task.

## fluffypony | 2023-11-05T16:27:02+00:00
> * Each workgroup should produce quarterly (Bi-annually?) community reports that provide updates on the decisions made along with reasoning behind them.

I love that idea - even if the report is "nothing changed in the last 6 months" it's still worth writing it up.

> * Elections should consider candidates technical abilities as well as longstanding community involvement. I see vetting candidates to weed out malicious actors as a difficult task.

Absolutely - and, as I mentioned on IRC, not every workgroup requires people who are deeply technical or are good at dealing with external service providers.

## ACK-J | 2023-11-05T16:31:54+00:00
Agreed, a report with no changes is still an update to the community.

## hyc | 2023-11-05T16:47:14+00:00
This ticket shows that the project has a lot of dependencies that require great trust. Bringing them to light is good, but I believe it's going to take a long time to mitigate them. Currently the path forward seems to require that only people who have been fully vetted can step into the necessary roles. Which means none of them will have anonymity, or any protection from being targeted. What solutions are there to manage risks like these?

## fluffypony | 2023-11-05T17:02:25+00:00
It's fine for existing pseudonymous contributors to participate, I don't think any of these functions require real world identities.

## fluffypony | 2023-11-05T17:53:12+00:00
Some additional feedback from ArticMine that I'm cross-posting here:

(1) The Github workgroup should be called the Merge work-group . We need to describe the activity as opposed to a specific proprietary product.
(2) The "Domains" work-group should be expanded to encompass all types of IP not just domain names. In particular Trademarks ? Service marks, Patents and Copyrights. I would suggest reaming it the IP work group 
(3) The separation of the CCS and GF workgroups is a great idea. This being said I believe there is room for further diversification here particularly with the CCS. The one size fits all approach is becoming less tenable every day with the changing regulatory environment. We need multiple different approacheds to meet the needs of both donors and developers. The Magic fund is a good start here, but is is only a start
(4) Regulatory and compliance. Is it best to have this spread out over multiple work groups or one work group or somewhere in between
(5) Legal Should we have a work group for this or again spread it out. I see pros and cons both ways

I'm going to update the post to reflect 2, as 1 is already done. 4 and 5 are open for discussion in this thread and then I can append the post with additional proposed workgroups.

## krfb2brthrowaway | 2023-11-05T20:34:42+00:00
nice attempt fluffypony, couldn't expect less than someone who actively in collaboration with feds to de-stabilize the Monero and create mass manipulation like you always did. 
It's time for core-team to make **important decisions!**

## Chubbeth | 2023-11-05T21:41:54+00:00
Hell no! 

The only core member who should be disbanded and kicked out it is Fluffypony.

Especially how he was in charge of the CCS wallet and it got “hacked”. Wink wink we all know what happened.

## fmarkor | 2023-11-05T23:39:03+00:00
Your keen interest in the Monero core again after being absent for so long right after the theft of approx. 500,000 USD worth of funds that would've been used for novel R&D as well as implementation.

A wallet which you theoretically could access, since you helped create it.

Do you think you're the right person to be suggesting such a change?

## monerobull | 2023-11-06T01:04:48+00:00
What is this, the clown cart arrived?

@krfb2brthrowaway brand new account
@Chubbeth brand new account
@fmarkor a fucking Discreet dev LMAO (scam bullshit that's been in ICO-presale limbo for years and spamming Monero threads on 4chan with their shilling) 

Nobody here is stupid enough to fall for your bullshit, just get out.

## Chubbeth | 2023-11-06T01:15:33+00:00
> What is this, the clown cart arrived?
> 
> @krfb2brthrowaway brand new account @Chubbeth brand new account @fmarkor a fucking Discreet dev LMAO (scam bullshit that's been in ICO-presale limbo for years and spamming Monero threads on 4chan with their shilling)
> 
> Nobody here is stupid enough to fall for your bullshit, just get out.

Sorry did I lose 500k usd worth of funds and refuse accountability? 

## S4ndr4fuchs | 2023-11-06T05:36:35+00:00
This is not the place to say it, but it needs to be said: Caesar's wife must be above suspicion. I, for one, will welcome fluffypony's resignation. If you yield power, you must be accountable to that power entrusted to/with you. With this being said, working for XMR is work, and work should be paid and paid fairly. If we care for XMR that much, we must agree that there is no free lunch in this world, and part of accountability we owe to ourselves, XMR, the team and the rest of the world, is to decide to put our XMR where our mouths are. The op-sec for the wallet was deplorable, and should be seen as plain treason, if not proven otherwise. But once again, we are all responsible for letting this slide, we were complacent and no one wanted to properly look into the matter. That made us all, oblivious partners to the theft. Somebody more dedicated than the rest of us combined, saw this as an opportunity and made way with it. One should never trust someone with something valuable and nothing to lose! It is the price we have to pay for our lack of understanding for this situation. Could have been worst. And this is the cost of the lesson so far.  

## fluffypony | 2023-11-06T08:32:41+00:00
Just to make it abundantly clear, as there seems to be some confusion that I'm trying to hold on to a role: I *am* resigning from the core team. This has ALWAYS been the plan, from 2018 already:

![Screenshot 2023-11-06 at 10 11 02 AM](https://github.com/monero-project/meta/assets/1944293/a5f7ff00-0e8e-48b5-b2b8-7ab2561a6a7c)

In fact, even recently (last year or the year before) I explicitly refused any reinstatement of access / responsibilities. Any remaining access I have had has been vestigial, a holdover from when I was the lead maintainer, stuff that nobody else wants to do or is quite painful to change.

GitHub issue noting this here: https://github.com/monero-project/meta/issues/922

Edit: just noticed that I accidentally put Jan 1, 2025, as the proposed date in the original post. I meant 2024, as in very very very soon, not 2025. I apologies if I gave anyone the impression that I wanted to hang around with any sort of privileged access for another 14 months.

## S4ndr4fuchs | 2023-11-06T10:16:02+00:00
You and Luigi1111 had access, but as far as bearing the weight of the responsibilities, and more importantly, the accountability, this is a story for another time. To be fair, you should have been compensated for the work, and anyone involved with the project should have had a right to fill in some suggestion for the op-sec. Is it not ironic that a for project claiming decentralization, the CCS was so centralized? That "trust-less" was so trusty? XMR is what we make of it, and the matter is and has always been in our hands. We have been complacent and complacency always comes at a price. 

## erciccione | 2023-11-06T10:16:22+00:00
While i do agree that there is need of a deep restructuring of the core team, i'm not sure this proposal would be beneficial, actually i think dismantling the core team could be a deadly mistake.

I see a number of possible issues:

- Having 7 different workgroups to replace the core team increases decentralization (and i'm not really sure about this either), but not stability. The fragmentation would make much more complex to get things done, because a person might need to talk with 2-3 different workgroups before getting something done. For example, for some changes to the website it might be needed to talk with the: git workgroup, ip and dns workgroup, Servers and CDN Workgroup and possibly the community workgroups. This would result in inevitable delays and possibly things getting lost in between the many communications.
- This new structure would not remove or decrease trust, but just move it to many different structures. Which could be beneficial in theory, but i don't think in this case it would be.
- Opening core aspects of the inner functioning of Monero to the public is extremely risky. While having "benevolent dictators" is far for optimal, having core aspect of the project managed according to the popular feeling of the moment is much worse, especially because public perception can be easily gamed by malicious actors, something that the Monero community has already seen in multiple occasions. The result will be that politics will be much more a part of Monero, because if there are elections, there is politics. 
- who assures these entities will all agree with each other? Because if they don't, critical aspect of the project could halt entirely and might require a long time before all the moving parts agree. It could result in splits, factions and forks.
- Without a strong uninterested entity managing important parts of the project, other more interested entities will probably start a race to control as many as Monero's core functions as possible. I'm talking about companies working on or with Monero, that could see this as a great opportunity to increase their influence in the project and stir it according to their interests. They might also have the economical capabilities to make "donations" to workgroups to increase their influence in it. They could also hire members of these groups or simply use their authority/name/money to push one of their members in a key workgroup.


These are just points that come to mind at the moment. While i do appreciate the intentions of core here, i think a restructuring of the way the core team work and offloading some key tasks would be better then completely getting rid of the core team.

In any case, this change would probably be the biggest change in the way Monero works and could change the project drastically. I think two months of discussions are too few to decide on such change.

## fluffypony | 2023-11-06T10:52:15+00:00
@erciccione all salient points, I only suggested the date as a forcing function, as some of this stuff might be broken up - eg. let's take the domains, binaryFate could setup a Gandi account and they could all transfer into there, and then he'd be a de facto member of that workgroup. Who joins him could be a matter for discussion and debate, and doesn't have to be rushed.

With respects to the entities agreeing with each other, I have two thoughts on that. Firstly, I think having a common member (or members) between those workgroups will solve that whilst still having providing some strong degree of decentralisation. Secondly, the challenge with a singular entity (the core team) is that it provides a commensurate degree of centralisation that an actor can target.

Even if a malicious actor doesn't use direct, frontal attacks against the Core Team (or individual members), they could use false flag operations etc. Introducing constant churn into a singular group that wields such control seems immensely dangerous.

I'd also hazard, without speaking on their behalf, that some Core Team members may not want such responsibility forever. Breaking it up into smaller chunks would allow for a reduced workload and footprint for individual members.

## janowitz | 2023-11-06T12:19:00+00:00
First of all thank you for all work you have done for this project fluffypony, it wouldn't be the same without your contributions!

I agree on the aspect of decentralisation of trust into single entities and some aspects can be solved technically (like multisig on the donation wallets) but some things like domains or hosting can not really be decentralised. A shared account is way more conflicting than a single account when it comes to troubles, like the current CCS incident. Also elections are not easy to manage in a pseudonymous world, since we don't have governance tools on the Monero blockchain yet (and probably won't have those anytime soon - maybe wouldn't even want those). Already this issue on Github showed up several fresh accounts with most probably malicious incentives.

So please, in favor for the whole project don't rush your decisions giving up all of your prior burdens towards some kind of community workgroups. Those should establish well before given all options, I still probably have more trust in you, binaryfate and several other community members than in some newly established workgroups.

## Chubbeth | 2023-11-06T12:46:33+00:00
> Already this issue on Github showed up several fresh accounts with most probably malicious incentives.

what malicious incentives do I have? Did I have access to 500k XMR and “lose it”. Then do a trust me bro statement and refuse any accountability? 

## fluffypony | 2023-11-06T12:56:42+00:00
> what malicious incentives do I have? Did I have access to 500k XMR and “lose it”. Then do a trust me bro statement and refuse any accountability?

To be clear, I have not refused accountability. I have expressly said on IRC that it's entirely possible that I messed up when generating the seed, or when transferring it to Luigi.

## S4ndr4fuchs | 2023-11-06T12:59:34+00:00
We must draw some solid conclusions from this fuck up and regularly up our game. The seed should have been generated on a cold computer, with no physical means to get on the internet, even using TAILS solely for this single purpose, and switching it off, afterwards. Also, not making use of multi key signatures protocol, not even using a Yubikey for the process of physically accessing the wallet, keeping the full wallet on a PC running on Windows, with a working node, makes no sense whatsoever, unless you would need a highly implausible explanation for a simpler one. I am not buying the "Ooops! Sorry!" theory. 

## Chubbeth | 2023-11-06T13:18:15+00:00
> > what malicious incentives do I have? Did I have access to 500k XMR and “lose it”. Then do a trust me bro statement and refuse any accountability?
> 
> To be clear, I have not refused accountability. I have expressly said on IRC that it's entirely possible that I messed up when generating the seed, or when transferring it to Luigi.

Then allow the community to investigate. Give us the transaction keys and such 

## janowitz | 2023-11-06T13:41:41+00:00
> > Already this issue on Github showed up several fresh accounts with most probably malicious incentives.
> 
> what malicious incentives do I have? Did I have access to 500k XMR and “lose it”. Then do a trust me bro statement and refuse any accountability?

If you don't have any, just disclose who you are.

I have given up my pseudonymity years ago, fluffypony and binaryfate, too. I can live with pseudonyms who build up their trust over years without giving up their anonymity, however it's remarkable that we see several fresh accounts in an mostly internal issue. Yeah, there was a loss but not 500k XMR. And I don't think anyone involved with the whole situation is comfortable with it. First of all it was a design problem and we should have moved to multisig years ago. Yeah, I know the issues with multisig on Monero, however if not a community fund what then would be the best showcase for multisig? If funds have been lost due to technical problems, most of us could accept it better than a human failure.

## luigi1111 | 2023-11-06T13:46:39+00:00
> keeping the full wallet on a PC running on Windows, with a working node, makes no sense whatsoever, unless you would need a highly implausible explanation for a simpler one. I am not buying the "Ooops! Sorry!" theory.

The full wallet wasn't on Windows. The sub wallet that was on Windows is intact.

## luigi1111 | 2023-11-06T13:51:06+00:00
> Then allow the community to investigate. Give us the transaction keys and such

I'm not against sharing the wallet if there is a compelling reason. I don't see it as obviously beneficial and zero harm currently though.

## Chubbeth | 2023-11-06T14:12:19+00:00
> > Then allow the community to investigate. Give us the transaction keys and such
> 
> I'm not against sharing the wallet if there is a compelling reason. I don't see it as obviously beneficial and zero harm currently though.

2,762 of crowdfunded xmr is enough of a compelling reason. 

A full investigation should happen. There is only benefit within this.

The lackadaisical response to this is insulting to everyone.

There has been no consequences nor retributions.





## selsta | 2023-11-06T14:16:25+00:00
The sweep transaction was sent from a different wallet cache, the transaction key isn't known.

## janowitz | 2023-11-06T14:35:56+00:00
I mean, Monero has been built to be as private as possible, what do we know? We can trace the transactions with 100+ inputs which have been known, but we can only guess further. We don't even know if the funds have been moved or not. However we can determine if they have been used in a ring signature... But does it make any difference?

## tarris034otheracc | 2023-11-06T16:55:46+00:00
I think we should continue the discussion on stolen funds here:
https://github.com/monero-project/meta/issues/916

## anhdres | 2023-11-06T21:25:15+00:00
I for one appreciate the work you've done during all those years being the CEO of Monero. Really.

I think breaking apart some of the roles of core into smaller workgroups is a sensible choice, where that is possible (or makes sense). Things that touch the realworld(tm) will always be kinda centralized, like the hosting or DNS, PGP keys, etc. There's no multisig solution for that afaik, but the more virtual, DAO-like stuff like wallets and approve projects, moderate channels, are totally worth it.

Bottom line I think we need some tweaks, but not too much that we end up creating a Monero Foundation and become what we've criticized so much. 

## userofreddit44 | 2023-11-07T21:22:11+00:00
I will reiterate my thoughts here.
Each workgroup should have detailed documentation on the getmonero site as to the practises/guidelines that are taken to serve the purpose, this allows for suggestions if anything is deemed suboptimal from whatever perspective (security/tech etc).

More specifically each workgroup should document what attack vectors their current security practises account for and publicate it on getmonero. This allows the workgroup to say if XYZ occurs then we will graciously get fucked because it is such a low probability of materializng and low criticality to which it is not worth accounting for.

I think the incident is more so exemplary of badly managed risks than risks inherent to the core team itself, this new architecture might allow for more focus within each workgroup but at the least transparent practises would allow for identification of badly managed risks. All this would be reassuring for donations that monies won't dissipate because of negligent opsec but instead go towards the intended purpose.

Gentoo sets some sort of a model imo, look at how structured their shit is for instance:
https://wiki.gentoo.org/wiki/Project:Infrastructure
https://wiki.gentoo.org/wiki/Project:Infrastructure/Incident_reports

Who's willing to implement?

## umma08 | 2023-11-18T22:45:55+00:00
I think a good start to manifesting this proposal would be to understand what "trusted" members of the community wish to be in which WG. 

Also i am not convinced that Luigi should be in any workgroup that handles funds, unfortunately. Once bitten, twice shy. 

I also think it would be immensely beneficial to understand which members of Core other than fluffy and Luigi wish to maintain responsibility for things, as that has not been clarified. 

It would also be super helpful if respected members of the community commented or voiced opinion on this, as many have been fairly silent and, to be honest, it's not that helpful when weighty voices remain silent about serious issues. 

Personally, i (midipoet) am happy to be involved in the CCS WG and can be involved with the multisig, if required. 

## Gingeropolous | 2023-11-28T12:18:03+00:00
i'll step up to do something, whatever people think I'm capable of doing. 

Over the winter I'll get my keys and such in order. 

## jwinterm | 2023-11-29T15:59:25+00:00
> i'll step up to do something, whatever people think I'm capable of doing.
> 
> Over the winter I'll get my keys and such in order.

Ditto

## anhdres | 2023-12-04T14:22:12+00:00
You all know that my background is not IT, but if decentralization is the goal, I can also step up and do my best to learn whatever security procedure is needed so as to sign stuff, approve, etc.

## michaesc | 2023-12-08T10:09:31+00:00
The core team have done a great job and because none of the concerns @fluffypony mentions have happened, it implies that **keeping the existing organisation would work fine.**

Nevertheless, it was Fluffy and core that made the organisational choices that have succeeded until now. If the core team agrees with the changes that Fluffy recommends, then I'm convinced it would work just as well and that **we should support the changes by implementing them.**

## dan-is-not-the-man | 2024-05-28T08:51:49+00:00
Please close this, ain't going to happen.

## fluffypony | 2024-05-28T09:41:00+00:00
> Please close this, ain't going to happen.

Be the change you want.

## nahuhh | 2024-05-28T11:09:15+00:00
> > Please close this, ain't going to happen.
> 
> Be the change you want.

You wouldnt endorse me

edit:
can you clarify who is still on core, and whether they are active or when they were last active?

active:
- Luigi
- BinaryFate
- Articmine
- and?


stepped down:
- fluffypony
- and?

inactive
- ...
- and?


## HardenedSteel | 2024-07-23T20:32:15+00:00
@Rucknium @mainnet-pat would like to hear opinions, suggestions and how does BCH manages to this?

# Action History
- Created by: fluffypony | 2023-11-05T14:02:23+00:00
