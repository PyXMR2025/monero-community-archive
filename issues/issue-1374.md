---
title: Monero Site Meeting - Sat 25 April 2026, 16:00 UTC
source_url: https://github.com/monero-project/meta/issues/1374
author: redsh4de
assignees: []
labels: []
created_at: '2026-04-19T18:04:48+00:00'
updated_at: '2026-04-25T18:40:03+00:00'
type: issue
status: closed
closed_at: '2026-04-25T18:40:03+00:00'
---

# Original Description
Location: [Libera.chat, #monero-site](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-site:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-site

Time: 16:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Following up on Core Team feedback w.r.t. CCS proposals [1](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/641) and [2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/644)

3. Any other business

Previous meeting logs: [here](https://github.com/monero-project/meta/issues/1361)

# Discussion History
## redsh4de | 2026-04-25T18:40:03+00:00
Logs:
```
16:00:57 <br-m> <redsh4de:matrix.org> Meeting time, hello!
16:01:02 <br-m> <redsh4de:matrix.org> https://github.com/monero-project/meta/issues/1374
16:01:11 <br-m> <redsh4de:matrix.org> 1. Greetings
16:01:37 <br-m> <syntheticbird> Hi
16:02:20 <br-m> <ofrnxmr:xmr.mx> Mornin
16:03:11 <br-m> <redsh4de:matrix.org> 2. Following up on Core Team feedback w.r.t. CCS proposals https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/641 and https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/644
16:03:24 <plowsof> hi
16:03:32 <br-m> <ofrnxmr:xmr.mx> cc @diego:cypherstack.com  if youre around
16:04:04 <br-m> <syntheticbird> I didn't see, has their been any new written feedback in the PRs threads ?
16:04:16 <plowsof> no
16:04:20 <br-m> <syntheticbird> alright
16:05:08 <br-m> <redsh4de:matrix.org> so, to summarize (correct me if i am misremembering) - the feedback is to for now focus on just on the frontend aspect of things, and leave backend as is? What about implementing View Transitions, was there smth mentioned on that?
16:05:28 <br-m> <syntheticbird> i was going to ask this exact question
16:05:42 <br-m> <syntheticbird> There has been no mention of View transitions and CCS transitions/animations
16:05:53 <br-m> <syntheticbird> which is 3/4 of my CCS.
16:06:41 <br-m> <syntheticbird> without forgetting that my CCS also cover the beta getmonero.org website. So if they want one feature on a website and not in the other I would need to know that.
16:06:57 <br-m> <redsh4de:matrix.org> +, would be good to get clarity on that
16:07:44 <plowsof> which one requires the "add javascript to getmonero" discussion? 
16:07:53 <br-m> <syntheticbird> mine.
16:08:48 <plowsof> do you want that discussion or is it possible to focus on the none javascript things for now 
16:09:06 <br-m> <ofrnxmr:xmr.mx> Am i correct in understanding that redsh4de's proposals is implementation, and syn's is design?
16:09:57 <br-m> <syntheticbird> we can focus on the non javascripts things for now, but I would like to have that discussion sooner or later
16:10:43 <br-m> <syntheticbird> ofrnxmr: I am doign implementation when it comes to transitions and animations, and it overlaps with redsh4de when sketching components of the page.
16:10:52 <br-m> <ofrnxmr:xmr.mx> Core isnt a fan of
16:10:53 <br-m> <ofrnxmr:xmr.mx> * adding animations
16:10:53 <br-m> <ofrnxmr:xmr.mx> * backend changes
16:10:53 <br-m> <ofrnxmr:xmr.mx> [... more lines follow, see https://mrelay.p2pool.observer/e/lpWf9_wKdlJja3Nr ]
16:11:23 <br-m> <redsh4de:matrix.org> @ofrnxmr:xmr.mx: its a mixed bag, theres some overlap but thats mostly the split yes
16:11:58 <br-m> <redsh4de:matrix.org> @ofrnxmr:xmr.mx: would they be receptive to maybe adding some new features to the backend? i imagine with the QoL features we discussed previously we'd run into needing that eventually
16:13:04 <br-m> <redsh4de:matrix.org> @syntheticbird: +1, it kind of touches on the getmonero page too. im still a fan of the theme toggle idea due to how trivial and non-invasive it is
16:13:22 <br-m> <ofrnxmr:xmr.mx> I think theres np with adding some stuff like date the proposal went to funding etc
16:13:49 <br-m> <ofrnxmr:xmr.mx> and some general qol stuff
16:13:53 <plowsof> that was trivial to add to the current one iirc 
16:14:42 <plowsof> the beauty of diegos masterpiece is that its just a json file 
16:15:17 <br-m> <ofrnxmr:xmr.mx> I think the easiest path forward is probably minimal, reskin etc. And leave the bigger design changes & backend stuff for some wider / long term discussion
16:15:35 <br-m> <redsh4de:matrix.org> plowsof: i guess as long as the main stack and functioanlity remains the same (output into JSON), then all is fair game? submit PRs to ccs-back?
16:16:50 <br-m> <ofrnxmr:xmr.mx> Its probably also (probably) important that its relatively maintenance-free
16:17:13 <br-m> <ofrnxmr:xmr.mx> As you can tell, gitlab and ccs back/front end dont ever get or need to be updated
16:17:46 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: we know there is a problem yet no one is granted to resolve the problem
16:18:16 <br-m> <ofrnxmr:xmr.mx> which problem? (aside from it being broken bcuz the server is out of storage :D)
16:19:00 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: outdated stack, inactive repositories, 5 million bots invasion
16:19:12 <br-m> <redsh4de:matrix.org> fwiw im not a fan that are still using PHP in the big year of 2026 when there exist much better runtimes - but i get that nobody has the time to bother with going over a rewrite from scratch so i guess thats that
16:19:27 <br-m> <syntheticbird> @redsh4de:matrix.org: i mean we do bother
16:19:47 <br-m> <redsh4de:matrix.org> well yeah, with implementing - but then theres reviewing, sanity checking, etc etc
16:20:03 <br-m> <redsh4de:matrix.org> Core would be running it so it'd be on them to handle
16:20:10 <br-m> <redsh4de:matrix.org> or a trusted party to do it
16:20:36 <br-m> <syntheticbird> you have already emitted ideas before in this channel to make the task much easier for this party.
16:20:45 <br-m> <syntheticbird> I include sanity checking and review into the "we do bother" part
16:22:10 <br-m> <redsh4de:matrix.org> ig, would Core ever be open to upgrading the backend? or is it just a "too much at once" kind of situation
16:22:39 <br-m> <ofrnxmr:xmr.mx> I think its a "if it aint broke, dont fix it" thing
16:23:11 <plowsof> most QoL things can easily be added to the current one like http://node3.monerodevs.org:8082/funding-required/ 
16:23:49 <plowsof> date to funding.. "zero conf" ... its keep it simple stupid stuff.
16:24:03 <plowsof> --tx-notify to run a script is not rocket science
16:24:11 <br-m> <ofrnxmr:xmr.mx> As of current, i think the "need" is consistency with beta website. Anything else is a "want", and harder to sell with any urgency
16:24:37 <br-m> <ofrnxmr:xmr.mx> Right ^ and qol stuff
16:24:39 <plowsof> QoL improvements to the back end is an over saturated market, where as front end design isnt 
16:27:42 <plowsof> and the ccs back end , out of the box, can be pointed to github (decentralisation tears) and work np 
16:28:25 <plowsof> unrelated though, hotfix for gitlab out of space
16:30:07 <plowsof> syntheticbird just say that the back end is insecure and you are ddossing it until the ccs is moved forward 
16:30:52 <br-m> <syntheticbird> shit
16:30:58 <br-m> <syntheticbird> you saw through our plans
16:31:23 <plowsof> the logs say "using space as an excuse?? rekt by shade and syn hahahha"
16:32:36 <br-m> <redsh4de:matrix.org> well, since the PHP backend stays (until the now-exposed ddos attack plan), then i'll be adjusting my proposal to focus on frontend, with potential PRs to ccs backend if the need arises for anything
16:32:50 <br-m> <redsh4de:matrix.org> off the top of my head, this is the list of the new features we discussed in the last meeting:
16:32:50 <br-m> <redsh4de:matrix.org> * proposer history viewable from frontend
16:32:50 <br-m> <redsh4de:matrix.org> * co-author field (don't remember if we reached consensus on this)
16:32:50 <br-m> <redsh4de:matrix.org> * funding type classification (milestone/time/pool), retroactive tag
16:34:53 <br-m> <ofrnxmr:xmr.mx> co-author nack. Proposer should own the resposibility
16:35:06 <br-m> <ofrnxmr:xmr.mx> What is "pool" again?
16:35:26 <br-m> <redsh4de:matrix.org> things like the FCMP++ research one, where it doesnt have a milestone or time expiry, like a vault in a sense?
16:35:28 <br-m> <syntheticbird> fcmp++ research ccs
16:35:30 <br-m> <syntheticbird> fund pool
16:35:32 <br-m> <syntheticbird> for audits
16:39:14 <br-m> <ofrnxmr:xmr.mx> Proposer history can be good, but as we saw recently, 0x, fyodor, and navid all opened proposals
16:41:37 <br-m> <redsh4de:matrix.org> wouldnt that be a argument for? dont get it
16:41:56 <br-m> <redsh4de:matrix.org> easier auditability and whatnot
16:42:17 <br-m> <ofrnxmr:xmr.mx> well, one or two of those handles were pretending that this was their first ccs
16:42:52 <br-m> <ofrnxmr:xmr.mx> Its not an arguement for or against, just saying that its good for honest proposers, but doesnt help wuth auditability of dishonest ones
16:43:21 <plowsof> it would stop me from seeing poeple not care about hyperlinks not being clickable in their proposal 
16:43:33 <plowsof> in their who section
16:44:15 <br-m> <redsh4de:matrix.org> @ofrnxmr:xmr.mx: yeah, doesnt do much if someone has smurf accounts but honest actors do outweight the bunch, at least rn
16:44:55 <br-m> <syntheticbird> If anything the changes should be focused on helping honest proposers and visitors. The QoL improvements have always had this spirit
16:45:18 <br-m> <syntheticbird> There is nothing the UX can do to fight against bad actors. That's just an unrelated problem
16:45:21 <plowsof> everyone? links their prev proposals, so it could make things look better and remove noise from the proposal, hinto had several ccs names for example, so pooling his together .. and others i forgot cause a little issue 
16:45:52 <plowsof> btw i nack anything that makes it easier to create a cs proposal 
16:46:05 <plowsof> sorry
16:46:30 <plowsof> kuno is there and people expose so much during the 'how to ccs' process 
16:46:37 <plowsof> OSINT
16:47:19 <plowsof> gpt made this years ago https://plowsof.github.io/chatgpt-ccs-proposal-form.html
16:47:19 <br-m> <redsh4de:matrix.org> not even a proposal template generator? :P i get filtering via skill issue detection though > <plowsof> btw i nack anything that makes it easier to create a cs proposal 
16:47:52 <br-m> <syntheticbird> love the broken sun icon
16:47:52 <plowsof> that was for the $xx + x.x xmr an hour mental warfare 
16:49:27 <plowsof> template generator  linked at the very end of the hot to ccs in small text is fine probably
16:50:59 <br-m> <redsh4de:matrix.org> yeah, i imagine if its made way too easy (2 button process kind of thing) it will lower the barrier of entry for borderline scam entries that need to be filtered through
16:55:15 <plowsof> prior to me asking people to end on newline - not having a templater caused the maintainer alot of headaches with things not appearing on the funding required page. this has been turned into presenting the proposer with a linter that should tell them whats wrong and they must fix the issue
16:57:28 <br-m> <redsh4de:matrix.org> alrightt. templater is a go then
16:57:38 <br-m> <redsh4de:matrix.org> anything else i didnt mention? @syntheticbird:monero.social
16:58:02 <br-m> <syntheticbird> None in the non-javascript discussion, but I would have imagined having the js discussion now
16:58:05 <br-m> <syntheticbird> but it's the end of the meeting
16:58:35 <br-m> <redsh4de:matrix.org> yeah, i think its important to cover js even though wed be running over a bit
16:58:45 <br-m> <syntheticbird> fine with it ?
16:58:47 <br-m> <syntheticbird> plowsof
16:58:57 <br-m> <syntheticbird> ofrnxmr
16:59:16 <br-m> <syntheticbird> otherwise I may for a meeting next sunday
17:01:36 <br-m> <ofrnxmr:xmr.mx> hopefully attendees of community meeting will show up
17:02:40 <plowsof> the javascript thing did playout somewhat recently for jermas? original getmonero redesign proposal 
17:04:06 <plowsof> us 4 can say that optional miniscule javascript is fine but the wider audience will clown you 
17:05:05 <br-m> <redsh4de:matrix.org> *might
17:05:42 <br-m> <syntheticbird> I am fine with X clowning me, I mind convincing you and core as the reasoning behind total js ban is frankly stupid.
17:07:23 <br-m> <redsh4de:matrix.org> I think JavaScript usage is acceptable as long as it meets two criteria:
17:07:23 <br-m> <redsh4de:matrix.org> * easily auditable (compact, readable)
17:07:23 <br-m> <redsh4de:matrix.org> * non-essential (functionality doesn't break without it)
17:07:31 <br-m> <syntheticbird> Exactly
17:08:24 <br-m> <syntheticbird> Not only are non-js users perfectly happy and can use the website. But there is no change in security risk for the users.
17:09:18 <br-m> <syntheticbird> and since the changes are compact, bloat is also not a concern
17:11:29 <plowsof> no javascript mentioned as a selling point for getmoneros redesign in 2017 https://www.getmonero.org/2017/04/09/overview-and-logs-for-the-dev-meeting-held-on-2017-04-09.html and reinforced in redshades proposal 
17:11:59 <plowsof> several generations have been born into -no javascript- , this is an uphill battle
17:12:32 <br-m> <syntheticbird> > <i2p-relay> {-olark} Will these sites still be usable with javascript disabled?
17:12:32 <br-m> <syntheticbird> > <rehrar> No JavaScript will be used.
17:12:34 <br-m> <syntheticbird> only two mentions of javascript. I won't call that a selling point
17:12:35 <br-m> <redsh4de:matrix.org> i mean, even in there the person that asked the JS question was more concerned about if the site will be usable without JS
17:15:07 <plowsof> https://www.getmonero.org/get-started/contributing/ 
17:15:20 <plowsof> Jekyll. No javascript 😅
17:15:31 <br-m> <redsh4de:matrix.org> hm
17:15:55 <br-m> <redsh4de:matrix.org> maaaybe a addendum of "required"...? 😅
17:17:04 <br-m> <redsh4de:matrix.org> fwiw docs.getmonero.org already has a small non-essential JS bundle for UX
17:17:19 <br-m> <syntheticbird> let's not talk about repo.getmonero.org gitlab
17:17:33 <plowsof> X doesnt care about reading docs
17:17:38 <br-m> <redsh4de:matrix.org> so there already is a bit of a "soft" precedent
17:17:43 <br-m> <syntheticbird> X gotta hate
17:17:53 <br-m> <syntheticbird> whatever we do
17:17:53 <plowsof> the soft precedant would be for a feature with utility 
17:18:08 <br-m> <syntheticbird> I've seen people claiming to be monero users and hating FCMP++
17:18:09 <plowsof> that we didnt ask anyone about
17:18:13 <br-m> <syntheticbird> for various reasons
17:18:38 <br-m> <syntheticbird> would that be soft ?
17:18:52 <br-m> <syntheticbird> if it has utility i bet the no-js people are gonna scream about not being able to use that utility
17:19:34 <br-m> <redsh4de:matrix.org> theme toggle does have some utility, and docs has JS for the same reason iirc, havent inspected if its used for anything else
17:19:36 <plowsof> for docs they are told to use offline 
17:19:51 <plowsof> for that search feature
17:20:26 <plowsof> and docs isnt core infrastructure so its the wild west 
17:20:50 <br-m> <syntheticbird> endorsed by core tho
17:21:00 <br-m> <syntheticbird> since docs moved from getmonero.org to docs
17:22:15 <br-m> <redsh4de:matrix.org> it would be valuable to get the input of community meeting attendees though
17:22:27 <br-m> <syntheticbird> i agree
17:22:28 <br-m> <redsh4de:matrix.org> as users
17:23:10 <br-m> <syntheticbird> but ofrnxmr should agree tho because I bet that's going to stir up the meeting into some big debate
17:23:13 <br-m> <syntheticbird> and he maybe want a calm meeting
17:23:30 <br-m> <syntheticbird> which i would understand
17:24:06 <br-m> <redsh4de:matrix.org> yeah, def controversial topic
17:24:13 <br-m> <redsh4de:matrix.org> wdyt @ofrnxmr:xmr.mx
17:26:52 <br-m> <ofrnxmr:xmr.mx> aye.. i'd just play it on the safe side
17:26:59 <br-m> <ofrnxmr:xmr.mx> Core already doesnt want animations, so what would we need js for
17:27:06 <br-m> <syntheticbird> wait
17:27:33 <br-m> <syntheticbird> up until now you said they "weren't fan", not "they won't want". One is an opinion, the other is a statement.
17:28:33 <br-m> <syntheticbird> so I to be sure, is that a confirmation that animations is refused, or is discussion still in the iar
17:28:45 <br-m> <syntheticbird> s/iar/air
17:29:00 <br-m> <ofrnxmr:xmr.mx> for now, unless a public statement is said to the contrary, i read it as refused
17:29:12 <br-m> <syntheticbird> ack.
17:30:23 <br-m> <syntheticbird> Do you think we can still gather a consensus for you to communicate to core ?
17:30:35 <br-m> <syntheticbird> in the hope that it will change their mind
17:30:46 <br-m> <ofrnxmr:xmr.mx> Plowsof is the better communicator :P
17:31:05 <br-m> <syntheticbird> alright, well plowsof wdyt
17:34:16 <br-m> <syntheticbird> he is afk, he will respond eventually. @redsh4de:matrix.org you can close the meeting i think
17:35:19 <br-m> <redsh4de:matrix.org> yeah, we can end the meeting here
17:35:24 <br-m> <redsh4de:matrix.org> thanks everyone for attending!
```

# Action History
- Created by: redsh4de | 2026-04-19T18:04:48+00:00
- Closed at: 2026-04-25T18:40:03+00:00
