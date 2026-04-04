---
title: 'Community Workgroup Meeting: 5 January 2019 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/297
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2019-01-04T20:35:41+00:00'
updated_at: '2019-01-07T16:46:26+00:00'
type: issue
status: closed
closed_at: '2019-01-07T16:46:26+00:00'
---

# Original Description
**Location**

[Freenode](https://kiwiirc.com/nextclient/#irc://irc.freenode.net/#monero-community) | [OFTC](https://webchat.oftc.net/) | [Mattermost](https://mattermost.getmonero.org) | [Slack](https://monero.slack.com/) | Irc2P

Please test the relays shortly before using. If there are any issues, please use Freenode IRC directly.

Please PM [SGP on Reddit](https://www.reddit.com/message/compose/?to=SamsungGalaxyPlayer&subject=Monero%20Slack%20invite%20(from%20GitHub)&message=Hello%20please%20send%20a%20Monero%20Slack%20invite%20to%20the%20following%20email:) with your email for a Slack invite if desired.

 - `#monero-community`

**Time**

17:00 UTC
12:00 ET
11:00 CT
09:00 PT

[Use this timezone calculator to convert UTC to your time zone](https://www.timeanddate.com/worldclock/converter.html?iso=20190105T170000&p1=tz_et&p2=28&p3=111&p4=49&p5=179&p6=70&p7=224&p8=48&p9=136).

**Proposed Meeting Items**

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

0. Introduction
1. Greetings
2. Community highlights
3. FFS updates
4. Workgroup report
5. Kovri discussion
6. Open ideas time
7. Confirm next meeting date/time
8. Conclusion

# Discussion History
## JustFranz | 2019-01-05T03:38:48+00:00
I have not followed the development of Monero or Kovri in detail, but I have some questions that I feel should be answered and ideas considered. 

**Kovri needs a post-mortem, some of the things that should be investigated and answered are:**

- 1.1 How did Kovri as a need come about? What did Monero need, as identified then? What did Kovri set out to do and did its goals match the needs of Monero?
-  1.2 Besides coming up with Kovri, what other technological solutions were explored? How did they not meet the needs of Monero? Couldn't they have been worked with (existing technologies, development teams, communities)? Who not?
-  1.3 Equivalent technologies to Kovri - tor, l2p etc. are very long lasting projects with a lot of development behind them. Was Kovri a realistic solution considering our available resources (people, money, time, (urgency?)). Was there hubris? Could there have been a better target to spend immediate resources on?
- 1.4 What was the Kovri project in relation to the Monero project in terms of cooperation, communication and sharing of resources? If Kovri was separate and set out to do its own thing then why wasn't Kovri engineered to be the "best" solution for its problem (sorry for the inane question)? If Kovri was spawned to support Monero, then was it spawned in a shape and fashion that actually supports Monero the best?

_Please correct, expand, refine and concretize these points._ 


**Monero project questions:**

- 2.1 Do we have an actual roadmap? A list of tasks?
- 2.2 Does that roadmap have an accompanying design document? A design document should analyze the state of the application and ecosystem/ take a task, idea or technology and flesh it out/ break it up into sub components/ analyze from all relevant angles/  justify it with research, other projects, decisions reached in meetings / tie components together. What work is being done, where, problems, everything. It should be a resource for new and existing developers to orient themselves in the project and for informed decisions to be taken.

Feels like what we have now are irc conversations of past, abandoned subreddits, numerous githubs exploring different concepts, and a whole bunch of developers with different ideas in their heads just plugging away at the codebase. There needs to be some kind of an overarching goal and direction. 

- 2.3 With no leadership, do we need to develop a community protocol to keep things running smoothly? 


**What happened with Kovri?**

- When did anominal realize that Kovri was not going to work?
- How were the concerns voiced and how was it met?
- If the lead dev and pretty much the only dev realized that Kovri is a broken mess and insufficient, why did work continue?
- How did things escalate to a point where in actuality Kovri was abandoned and under the guise of working on it another project was being developed? 
- How did our lead Kovri dev screw himself with cryptos and tax and jeapordize the project?
- If at a point in time money is committed in the form of XMR and done so months in advance, how can we allow for the possibility of the certainly unstable crypto prices to harm the work being done? Can't we work a stable-coin into the scheme? 


I have to cut it short here. I just feel like the future of Monero is at steak if problems with leadership or how the community leads itself are not worked out.

Should a report be made on what happened and why and where to now?

## michaesc | 2019-01-05T10:30:28+00:00
Hello @SamsungGalaxyPlayer,

Please add to the agenda:

- Hardware team report (5 minutes)
    - Hardware project listing
    - Dedicated hardware wallet status
- Defcon 27 village status (2 minutes)

Thanks, see you then.

Cheers,
Michael

## anonimal | 2019-01-05T12:50:31+00:00
Since Justin gave less than 24 hours of warning to talk about me behind my back, I had to respond [here](https://www.reddit.com/r/Monero/comments/acgr0q/anominal_statement_on_secreta_and_kovri/edan760/) since I can't attend the meeting. Please, do read his utterly stupid statement so you can better understand my response.

@JustFranz Monero is not an authority on Kovri. If you have any Kovri questions, you should contact the Kovri Core Team for accurate information. https://gitlab.com/kovri-project/kovri#contact-and-support

## anonimal | 2019-01-05T13:32:31+00:00
My [post](https://www.reddit.com/r/Monero/comments/acgr0q/anominal_statement_on_secreta_and_kovri/edan760/), although it's abrasive because I'm under attack, may answer some of these questions @JustFranz.

>When did anominal realize that Kovri was not going to work?

This is implying that I don't think "Kovri was not going to work". I never said this. But, before the project started, I warned fluffypony to not fork the codebase and proposed that I be allowed to do this correctly from the beginning - from scratch. I literally said (paraphrasing) "this codebase will not achieve what we want to achieve". No one listened. No one cared. The sentiment was more along the lines of "gimmie action now, we deal with problems later".

That's not my style but I "did my job" anyway since I was under contract. I listed all the problems along the way in my FFS too. I've voiced this frequently over the years on IRC. None of this is a surprise. No one cared. The largest "input" from the majority of the "community" was "gimmie gimmie when?". Almost no one cared to better understand the network anonymity engineering process. Basically no one from the Monero "community" wanted to get involved with Kovri core code development yet the vast majority of the "community" kept shilling my work as their own "community-driven" work. Pathetic. (The only people who get that credit is the Translation Team and some web devs. Spectacular work, and for that I'm very grateful.)

Do note, as stated in my post, my contract will be fulfilled one way or another. I've been doing Monero a service by not letting them shoot themselves in the foot and yet I continue to receive years of attack. It certainly would've been easier to lie to everyone and say everything is grand and that Kovri is the only solution so give me more money for years to come because you need Kovri and only Kovri - but that's not my style.

Most of the Monero "community" has really screwed the Kovri Project, and I don't even know why I'm dealing with these people anymore. I helped build Monero Project from the ground-up since 2015 - Monero Project, not just Kovri - but my incentive to stick around is dwindling with all these childish stupid attacks (not you @JustFranz, I'm speaking of others).

>How were the concerns voiced and how was it met?

As stated above.

>If the lead dev and pretty much the only dev realized that Kovri is a broken mess and insufficient, why did work continue?

Because there hadn't been a better solution at the time - until I invented Sekreta. Sekreta is the solution that Monero needs because it uses *every* available anonymity system that a user wishes to use in a way that increases privacy and data confidentiality. But, before that, myself and the "community" did the best with what he all had at the time. My post above might explain more, as well as the actual [draft itself](https://gitlab.com/sekreta/sekreta/blob/master/README.md).

>How did things escalate to a point where in actuality Kovri was abandoned and under the guise of working on it another project was being developed?

It's not abandoned. Who keeps spreading this FUD?

>How did our lead Kovri dev screw himself with cryptos and tax and jeapordize the project?

I had said this before, in other posts, which Justin conveniently didn't repeat: ironically, 3+ years in this community and no one mentioned that cryptocurrency income is taxable income. Combine that with volatile price movements and the 2018 bear market: the math explains itself.

## JustFranz | 2019-01-05T22:47:43+00:00
Thank you for the reply Anonimal.

As for taxes, all income is taxable, you can be paid in real estate, gym memberships, potatoes, anything... if it is valued then its taxed according to its value. Your tax man will of course want £€$ from you, which will turn out to be a problem when you are paid in anything else than FIAT currrency or stable liquid assets and you don't have other income.

If you get a lumpsum of 100 BTC then according to most tax legislations its going to be valued according to the price at the time of payment. If it lands in your coibase account and you do not immediately sell what is needed for taxes and the price drops then you are screwed the difference. 

The tax laws for crypto are mostly fucked or non-existent in most jurisdictions and crypto is treated unfairly as a result.

Keep your crypto that you won't sell off of exchanges and sell as needed. My guess is that just declaring the FIAT that lands in your bank is enough in most places. The IRS of the US of A forced coinbase to hand over the transaction data of all US residents over a certain sum, going years back. Initially they wanted all the data. If 5 years from now someone wants to fuck you for not following the letter of the stupid law despite complying in spirit then they will fuck you and there is nothing you can do about it.

Limit your exposure. **Spend crypto**, sell through many diverse channels. Spending 1-2% middle man fee to spend crypto is worth not getting hit with unjust fines, accumulating interest, trouble and jail or even considering the possibility.
-----------------------------------

I agree on the insufficiency of the TOR and similar ecosystems going forward. We need something easy to use for devs and users and something ubiquitous. 

Only thing I can see improving the current privacy situation of the internet is global satellite internet that is free and does not require authorization. Also mesh networks but I have a hard time seeing how that could be realized.

 

# Action History
- Created by: SamsungGalaxyPlayer | 2019-01-04T20:35:41+00:00
- Closed at: 2019-01-07T16:46:26+00:00
