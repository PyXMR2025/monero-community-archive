---
title: Monero Space Meeting - Saturday 22 January 2022 @ 17 UTC
source_url: https://github.com/monero-project/meta/issues/645
author: scottAnselmo
assignees: []
labels: []
created_at: '2022-01-04T00:56:56+00:00'
updated_at: '2022-01-26T19:29:53+00:00'
type: issue
status: closed
closed_at: '2022-01-26T19:29:53+00:00'
---

# Original Description
**_Note that this is 1 week later than the third Saturday of the month it's usually held on._**

**Location**

[Libera.chat, #monero-space ](https://libera.chat/)| [Matrix](https://matrix.to/#/#monero-space:monero.social?via=matrix.org&via=monero.social)

**Time**

2022/01/22 17:00 UTC

[Use this timezone calculator to convert UTC to your time](https://www.timeanddate.com/worldclock/converter.html?iso=20220122T170000&p1=1440&p2=28&p3=111&p4=tz_et&p5=49&p6=179&p7=70&p8=224&p9=48&p10=136&p11=248)

**Agenda**

1. Greetings
2. Monero Space updates (what we all have been working on)
3. Other Monero community project updates
4. What's happening in the next month
5. Ideas time

# Discussion History
## scottAnselmo | 2022-01-26T19:29:53+00:00
1/22/2022, 17:00:40 - xmrscott: Alright, meeting time
1/22/2022, 17:01:25 - xmrscott: Meeting agenda can be found here and as always is relatively light: https://github.com/monero-project/meta/issues/645
1/22/2022, 17:01:36 - xmrscott: 1. Greetings
1/22/2022, 17:02:01 - bridgerton: <sgp> Hello!
1/22/2022, 17:02:39 - bridgerton: <sgp> Messages are lagging heavily on the matrix side for me so I'll use Discord
1/22/2022, 17:03:29 - w: Morning!
1/22/2022, 17:04:18 - xmrscott: 2. Monero Space updates (what we all have been working on)
1/22/2022, 17:05:01 - bridgerton: <sgp> We had a Monero Meet 2 weeks ago: https://www.youtube.com/watch?v=KkshQgwVHPs
1/22/2022, 17:05:40 - bridgerton: <sgp> Shoutout to the VDO.ninja developer for adding Jitsi-like placeholders for people who are audio-only! I sent them a donation (not in XMR sadly)
1/22/2022, 17:08:52 - bridgerton: <sgp> besides that, nothing really on the monero space side for me specifically
1/22/2022, 17:09:52 - xmrscott: Worked on misskey more. So while I had set up a misskey instance and got a S3 rep to help w/ a non-AWS config, misskey didn't have the third party integration with it's API that I wanted for one or two things, so switching to Mastodon which does and that'll hopefully be the last test in the pathfinding of setting up a fediverse SNS that meets the deliverables I'm hoping for
1/22/2022, 17:10:51 - bridgerton: <sgp> I was somewhat looking forward to the quirky misskey, but mastodon is far better known
1/22/2022, 17:11:30 - xmrscott: (That's it for me)
1/22/2022, 17:11:50 - bridgerton: <sgp> I know a bunch of people that I primarily talk to on twitter who want to use something like this. Which makes sense since it's a twitter clone
1/22/2022, 17:12:20 - bridgerton: <sgp> Does this have an invitation system so we can use that to hype it up?
1/22/2022, 17:13:59 - xmrscott: Should; Pleroma and misskey both do in some capacity
1/22/2022, 17:14:39 - bridgerton: <sgp> cool, let's hype it up in the monero, techlore, and seth for privacy communities to start then 🙂 Give them all invites
1/22/2022, 17:15:09 - bridgerton: <sgp> do you have availability to work on this soon or are you caught up in other things for a while?
1/22/2022, 17:16:56 - xmrscott: My Sundays are completely consumed for the next three weeks on personal stuff, but I should be able to get it up soon^TM
1/22/2022, 17:17:27 - xmrscott: Mainly right now I'm asking around about best way to run ops on it (e.g. Docker vs Ansible playbook)
1/22/2022, 17:18:11 - sgp_: I'm trying to think of a better subdomain than mastodon.monero.space. even blog.monero.space, lol
1/22/2022, 17:18:34 - xmrscott: Which I suppose I can ask the question here and now, any preference on subdomain? I'm done some looking at other instances and am partial to tusk or mast, but open to alternatives
1/22/2022, 17:19:19 - sgp_: I'm not really a fan of "tusk"
1/22/2022, 17:19:38 - sgp_: I assume people still don't like social.monero.space?
1/22/2022, 17:20:22 - xmrscott: I personally don't because it could get confusing with Core's owning and using of monero.social for Matrix
1/22/2022, 17:20:23 - sgp_: maybe monero.social can redirect to social.monero.space?
1/22/2022, 17:20:29 - xmrscott: But I'm only one person
1/22/2022, 17:21:05 - xmrscott: Also there's the argument that isn't a forum a social space as well?
1/22/2022, 17:21:15 - sgp_: maybe we could just use monero.space for this directly, and set up about.monero.space or something
1/22/2022, 17:21:48 - xmrscott: Sure, that'd work
1/22/2022, 17:22:12 - xmrscott: I'm struggling to think of whatever services we'd use that would be as primary as a fediverse SNS
1/22/2022, 17:22:21 - xmrscott: And thus a better use of monero.space
1/22/2022, 17:22:44 - sgp_: While I like the design on Flarum, I kinda lean dropping that for the fediverse reddit clone
1/22/2022, 17:23:54 - xmrscott: There are advantages to Flarum in that it's geared towards long form/term conversation
1/22/2022, 17:24:08 - xmrscott: And it doesn't cost too much to run it IMO
1/22/2022, 17:24:29 - xmrscott: So we could run both Lemmy and Flarum for relatively cheap
1/22/2022, 17:24:42 - sgp_: it might be fine to use use m.monero.space, and just redesign monero.space to have big easy buttons to click to get to it
1/22/2022, 17:24:56 - sgp_: same with l.monero.space or whatever for lemmy
1/22/2022, 17:25:06 - sgp_: sure it's 1 extra click, but power users will pick up fast
1/22/2022, 17:25:43 - sgp_: and if they forget, just remember monero.space and it's 1 click away
1/22/2022, 17:26:05 - Rucknium: Just curious: what is the capital and labor cost to run the monero.social Matrix server?
1/22/2022, 17:26:37 - sgp_: to run one well for a large audience, it takes quite a bit afaik
1/22/2022, 17:26:58 - xmrscott: Sure, the fediverse space is relatively light on services so I don't think we'd run into name conflicts with one letter subdomains
1/22/2022, 17:27:51 - xmrscott: Only other major one might be PeerTube if we wanted to do that for whatever reason although storage would be expensive even with S3 as time goes on
1/22/2022, 17:28:29 - bridgerton: <sgp> yeah we would need some revenue or something before considering peertube imo
1/22/2022, 17:28:51 - bridgerton: <sgp> I'm most looking forward to mastodon
1/22/2022, 17:31:02 - xmrscott: <@rucknium:monero.social "Just curious: what is the capita..."> Trying to find one of the Matrix as a Service vendors that I know exist, but I want to say offhand with them last year it was around $30-40/month.
1/22/2022, 17:31:30 - xmrscott: monero.social is ran by Core though and isn't through a MSP
1/22/2022, 17:31:32 - bridgerton: <sgp> CypherStack offers this but idk their costs
1/22/2022, 17:36:16 - xmrscott: We can move on to 3. Other Monero community project updates
1/22/2022, 17:36:41 - w: crypto_grampy and plowsof wrote a script to automate the install of an monero node on android (via termux). It was recently updated with a few features that make it easier to run and almost "app like" for end users.

Crypto_grampy's repo
https://github.com/CryptoGrampy/android-termux-monero-node

Install instructions:
https://github.com/nahuhh/android-termux-monero-node/releases/tag/v4.0.1
1/22/2022, 17:36:47 - xmrscott: Although since -community meetings happen regularly just pointing people to read the logs is sufficient
1/22/2022, 17:37:16 - xmrscott: Nice!
1/22/2022, 17:38:43 - sgp_: w: that's a really cool project! Good job!
1/22/2022, 17:40:25 - sgp_: The MAGIC Monero Fund committee has its first meeting tomorrow
1/22/2022, 17:40:50 - sgp_: my main focus on the community side has been on that
1/22/2022, 17:41:30 - sgp_: I also was at TNABC this week and talked to an endless stream of people about monero haha https://www.reddit.com/r/Monero/comments/s9emaj/tnabc_monero_booth_recap_it_was_great/
1/22/2022, 17:42:08 - sgp_: we're going to need some strong marketing pushes though, since a lot of people who joined in 2020-2021 have NO idea what monero is
1/22/2022, 17:42:38 - sgp_: clearly monero means money wasn't a big enough stunt itself :p
1/22/2022, 17:42:55 - xmrscott: At cons now that they're starting up again physically or elsewhere?
1/22/2022, 17:43:36 - sgp_: since a lot of crypto people have relatively dismissive opinions about covid, most of those are in-person now yes
1/22/2022, 17:43:56 - Rucknium: Monero gets shilled a lot on r/CryptoCurrency though. Do we need to publicize Monero on Facebook? 😬
1/22/2022, 17:44:09 - sgp_: the big bitcoin one is in april, at the same time as monerotopia
1/22/2022, 17:44:24 - w: <@sgp_:monero.social "we're going to need some strong ..."> I'm working on my people locally. 

A lot of smoke and mirrors have people completely unaware. First question people ask me when I mention crypto is "btc or eth? neither?. Oh, doge? Shib?"

Xmr
"Never heard iof it"
1/22/2022, 17:44:37 - sgp_: <@rucknium:monero.social "Monero gets shilled a lot on r/C..."> good point, r/cryptocurrency has monero content relatively often. Not hugely often, but monero punches above its weight there
1/22/2022, 17:44:42 - msvb-web: Is the committee meeting public, how can I attend?
1/22/2022, 17:45:08 - sgp_: <@msvb-web:libera.chat "Is the committee meeting public,..."> committee meeting isn't public, but the meeting notes will be made public
1/22/2022, 17:45:09 - xmrscott: Yeah, that's kind of what I was driving at, is it better to focus on digital marketing on some platform where wherever these people congregate most?
1/22/2022, 17:45:50 - sgp_: yeah, I think focusing on 1) tiktok, 2) youtube, 3) facebook, is important. maybe facebook least of those 3
1/22/2022, 17:46:08 - sgp_: yeah actually "replace" facebook with instagram acaict
1/22/2022, 17:46:31 - Rucknium: In a certain way, the low knowledge of Monero is encouraging. At least it isn't the case that Monero usage is low-ish because people know about it and don't want to use it. People don't know about it in the first place, which is easier to rectify than some fundamental problem with the tech.
1/22/2022, 17:47:49 - w: Once people know... xmr is gonna be 👑 of transaction coins. (It already is the best. Just needs people to use it)
1/22/2022, 17:48:44 - sgp_: people have been rallying on twitter or whatever about price suppression of monero, but frankly there isn't really much "new money" and "new people" coming into it like they are NEAR or whatever else
1/22/2022, 17:49:41 - sgp_: monero has a strong - but isolated - community
1/22/2022, 17:50:19 - sgp_: hopefully the mastodon will help us grow more among privacy enthusiasts at least
1/22/2022, 17:50:58 - Rucknium: A lot of the other coins have enormous marketing budgets since they have premining, or devtax, or venture capital money, etc.
1/22/2022, 17:52:01 - sgp_: of course, and then you get the shared hype with shared investment, etc etc etc
1/22/2022, 17:52:21 - sgp_: point is monero needs to make up ground so more people know about it imo
1/22/2022, 17:53:27 - w: Super bullish. As Rick said, if people were aware if xmr and still didn't buy, I'd have uncertainty. But none of the new money knows what it is.

Showing people monero is ridiculously easy. Even have some of my team running nodes (via CG script).

Soon as I explain xmr to people, they are in. 

1/22/2022, 17:53:32 - sgp_: Rucknium: something you'll need to figure out for community building with the fund committee :P Tag you're it!
1/22/2022, 17:53:54 - xmrscott: Sure. It may be worth exploring settings up a monthly bounty or something on plowsof's tool for marketing purposes
1/22/2022, 17:54:31 - sgp_: I was skeptical of the bounty system personally but it seems to be a huge success
1/22/2022, 17:54:48 - sgp_: so we need more things like that
1/22/2022, 17:55:11 - plowsof: xmrscott: getwishlisted.xyz/flask 👍️
1/22/2022, 17:56:58 - xmrscott: We have about 3 minutes left in the meeting. Anything people want to quickly discuss before it ends and the next one is on the next 3rd Sat?
1/22/2022, 17:57:44 - Rucknium: sgp_: Yes, it is amazing that when there are incentives, people alter their actions to take advantage of them :P
1/22/2022, 17:57:46 - sgp_: I'm considering moving the monero meet forward a week to Feb 5th, thoughts?
1/22/2022, 17:58:10 - Rucknium: (Although I assume that you mean that you were surprised that people would donate significant quantities of XMR)
1/22/2022, 17:58:56 - xmrscott: No issues here. Probably depends most on the general schedules of the people you might want for that one
1/22/2022, 17:59:22 - sgp_: okay, I'll move it forward then and adjust later if necessary
1/22/2022, 18:00:24 - xmrscott: That's a wrap! Thanks everyone who was able to attend!

# Action History
- Created by: scottAnselmo | 2022-01-04T00:56:56+00:00
- Closed at: 2022-01-26T19:29:53+00:00
