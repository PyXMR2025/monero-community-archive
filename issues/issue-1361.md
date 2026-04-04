---
title: Monero Site Meeting - Sat 28 March 2026, 16:00 UTC
source_url: https://github.com/monero-project/meta/issues/1361
author: redsh4de
assignees: []
labels: []
created_at: '2026-03-28T15:55:44+00:00'
updated_at: '2026-03-28T17:46:06+00:00'
type: issue
status: closed
closed_at: '2026-03-28T17:46:06+00:00'
---

# Original Description
Location: [Libera.chat, #monero-site](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-site:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-site

Time: 16:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Discussing ideas around the proposed CCS site overhaul
   - Relevant CCS proposals: [redsh4de](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/641), [SyntheticBird45](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/644)

3. Any other business

# Discussion History
## redsh4de | 2026-03-28T17:46:06+00:00
```
16:00:58 <br-m> <redsh4de:matrix.org> alright... meeting time!
16:01:04 <br-m> <redsh4de:matrix.org> 1. Greetings
16:01:18 <br-m> <syntheticbird> Hello
16:01:20 <br-m> <redsh4de:matrix.org> Hello ladies and gents
16:01:29 <br-m> <syntheticbird> don't forget agents
16:01:38 <br-m> <syntheticbird> they are a thing now
16:02:01 <br-m> <redsh4de:matrix.org> hi opus and claude
16:02:45 <br-m> <ofrnxmr:xmr.mx> cc luigi111 @diego:cypherstack.com
16:03:06 <br-m> <diego:cypherstack.com> hi I'm alive
16:07:05 <br-m> <redsh4de:matrix.org> hello!
16:07:05 <br-m> <redsh4de:matrix.org> so, @syntheticbird:monero.social and myself are planning to extend the new design of the new site page to the CCS. Page would be made in Astro, re-use a lot of the design components
16:07:05 <br-m> <redsh4de:matrix.org> Initially, the idea was just to make a new frontend design and leave it at that, but there were some ideas about adding new features - ability to track a users ccs proposal history being one of them, ability to specify "funding types" - time based, milestone, etc, and just cleaner UX while still keeping it git-based. Ad[... more lines follow, see https://mrelay.p2pool.observer/e/1oDJ9fMKb1VScnVQ ]
16:07:44 <br-m> <redsh4de:matrix.org> Syn's proposal drafting the UX for proposal pages: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/644
16:08:12 <br-m> <redsh4de:matrix.org> My proposal with some in-progress drafts and tech stack ideas with reasons behind each: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/641
16:08:28 <br-m> <redsh4de:matrix.org> @syntheticbird:monero.social: anything you'd like to add?
16:10:35 <br-m> <syntheticbird> Just that beyond new features, navigation and UX, the new informations we would like to add in the proposal page, like funding type, have the objective of a better transparency for donors of the CCS. That's really a main objective here to let a maximum of information without having to explore gitlab.
16:11:49 <br-m> <syntheticbird> The timeline idea is also very important in that regard, Ironically, The CCS website supports no JS users, but they can't find update there
16:12:02 <br-m> <syntheticbird> They are obligated to go on gitlab for consulting progress.
16:12:50 <br-m> <syntheticbird> progress means comments from the developer, confirmation that transactions are sent, etc...
16:13:27 <br-m> <syntheticbird> that's about it. happy to answer any questions
16:16:27 <br-m> <redsh4de:matrix.org> would it be a fair summary to say that the CCS page would end up being more or less a user-friendly mirror, for what is going on in Gitlab?
16:16:27 <br-m> <redsh4de:matrix.org> Proposers would only have to to interact with gitlab as far as submitting a proposal and any other "write" actions
16:16:45 <br-m> <syntheticbird> yep
16:17:16 <br-m> <syntheticbird> that's exactly it
16:17:37 <br-m> <diego:cypherstack.com> hmmm
16:17:42 <br-m> <diego:cypherstack.com> seems neat
16:19:25 <br-m> <ofrnxmr:xmr.mx> Milestome requests are usually commented, but transaction confs arent > <@syntheticbird> progress means comments from the developer, confirmation that transactions are sent, etc...
16:20:18 <br-m> <ofrnxmr:xmr.mx> luigi updates the md to add payout amount and date - this info (payout dates and milestones) are on current ccs site
16:22:15 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: Yes. Luigi sometimes (i would have hoped more) happens to inform in comment the transaction id of the payout. If he do, then it is showed in the timeline, if not, then an event is created without it, from the md
16:22:34 <br-m> <ofrnxmr:xmr.mx> What isnt there is the comments, and imo i dont think we want to mirror comments onto the main website. The comment sections can get pretty ugly depending on the proposal
16:22:52 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: We aren't planning on mirroring the comments
16:23:09 <br-m> <redsh4de:matrix.org> @syntheticbird: the data updates could be automated by a bot as well - luigi could pay out, then do something like @ccs-bot confirm-payment M1 <txid>  - it would then update the md to add payout and date which would then be reflected by the site
16:23:14 <br-m> <ofrnxmr:xmr.mx> @syntheticbird: The only time txs are commented is when it its sonething like the fcmo++ research ccs and there are mulltiple recipients and milestoens arent being closed out
16:23:16 <br-m> <syntheticbird> Only the updates, moderator selected ones
16:23:42 <br-m> <syntheticbird> @redsh4de:matrix.org: Absolutely
16:23:58 <br-m> <ofrnxmr:xmr.mx> @redsh4de:matrix.org: Lololololo
16:24:26 <br-m> <diego:cypherstack.com> @syntheticbird: gud
16:24:50 <br-m> <ofrnxmr:xmr.mx> @ofrnxmr:xmr.mx: im loling at asking luigo to do more
16:25:55 <br-m> <ofrnxmr:xmr.mx> especially commenting txids etc. He manually updates multiple ccs's with payout amounts and dates. Txids are also probably a privacy issue
16:26:02 <br-m> <ofrnxmr:xmr.mx> At least pre-fcmp
16:26:27 <br-m> <syntheticbird> pre-fcmp, proposers are sharing their address, so that's already compromised
16:26:46 <br-m> <redsh4de:matrix.org> @ofrnxmr:xmr.mx: wouldn't that make him do less? :P wouldn't have to manually dig around the .md as a result, tag the bot with commands like @ccs-bot for anything - move to funding, close, update proposal, etc
16:26:57 <br-m> <ofrnxmr:xmr.mx> If you know the txid, you know the amount and potential real spend of that txid
16:27:29 <br-m> <ofrnxmr:xmr.mx> W/o the txid, you have no idea which on-chain tx is associated with the user
16:27:35 <br-m> <redsh4de:matrix.org> @redsh4de:matrix.org: would have a access control list obv
16:27:58 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: That is fair.
16:27:58 <br-m> <ofrnxmr:xmr.mx> @redsh4de:matrix.org: The md has to be updated for these actions
16:28:23 <br-m> <syntheticbird> Then we can provide a mechanism for users to confirm that they received the transaction.
16:28:37 <br-m> <ofrnxmr:xmr.mx> And its stored on git. Unless the bot is making commits, i dont think its a replacement
16:28:40 <br-m> <syntheticbird> s/users/proposers
16:29:02 <br-m> <redsh4de:matrix.org> @ofrnxmr:xmr.mx: Yeah, i mean that the bot would have write access
16:29:11 <br-m> <redsh4de:matrix.org> otherwise wouldn't be any good
16:29:11 <br-m> <ofrnxmr:xmr.mx> Idk if that would fly
16:29:44 <br-m> <ofrnxmr:xmr.mx> I think plowsof and luigi are the only ones with write access, and luigi is the only one permitted to commit directly
16:31:06 <br-m> <ofrnxmr:xmr.mx> I'm paranoid and dont like the idea of using a bot to commit directly
16:32:49 <br-m> <syntheticbird> There is always a solution to automate. But ideas are limited to what luigi and plowsof are willing to use. The use of bot that can optionally be audited, seems to us like the best way of extending the current system.
16:33:23 <br-m> <syntheticbird> But ideas are limited to what we suppose*
16:34:01 <br-m> <redsh4de:matrix.org> it could be a small self-hosted service that runs in parallel with the gitlab instance
16:34:01 <br-m> <redsh4de:matrix.org> access-controlled to only allow actions from specific user ids (i.e. plowsof or luigi)
16:34:01 <br-m> <redsh4de:matrix.org> all that would be needed would be setting up a access token for a repo (with granular permissions obv), have the service use that token - then set up a webhook that fires on comments? maybe then infer which proposal it was run on - and then would just automate what luigi does manually
16:35:07 <br-m> <ofrnxmr:xmr.mx> Its not automated though?
16:35:29 <br-m> <ofrnxmr:xmr.mx> If he has to comment
16:35:29 <br-m> <ofrnxmr:xmr.mx> send 16.6xmr on feb 26 2026
16:35:34 <br-m> <ofrnxmr:xmr.mx> Thays not any easier than updating the md manually
16:35:53 <br-m> <ofrnxmr:xmr.mx> (afaict)
16:36:09 <br-m> <ofrnxmr:xmr.mx> Maybe he can respond when he sees this
16:37:00 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: yes, frankfully we need his input on it
16:37:45 <br-m> <ofrnxmr:xmr.mx> Eapecially since some proposals this doesnt work with
16:37:52 <br-m> <ofrnxmr:xmr.mx> Like fcmp++ research
16:37:56 <br-m> <redsh4de:matrix.org> well - kind of. i definitely don't think sending of funds should be automated, thats a whoole another security issue
16:37:56 <br-m> <redsh4de:matrix.org> if he comments something like @ccs-bot confirm-payment M1 for milestone-based proposals - the bot can just read the amount info from the frontmatter, update the .md with the date the command was invoked, etc
16:38:01 <br-m> <ofrnxmr:xmr.mx> Payments are sent w/o milestones being claimed
16:38:09 <br-m> <redsh4de:matrix.org> @ofrnxmr:xmr.mx: yeah that would require something else
16:38:23 <br-m> <redsh4de:matrix.org> but those are kind of exceptions to the rule so those could be done manually still
16:38:36 <br-m> <syntheticbird> Funding Type -> Pool
16:38:41 <br-m> <ofrnxmr:xmr.mx> It happens all the time though
16:38:57 <br-m> <ofrnxmr:xmr.mx> He often sends multiple payments at once etv
16:39:09 <br-m> <syntheticbird> etv?
16:39:11 <br-m> <redsh4de:matrix.org> the bot stuff is a nice-to-have though - not a must, doesn't change anything for proposers only can make maintainers lives a liitle bit easier only if executed right
16:39:13 <br-m> <syntheticbird> etc got it
16:39:16 <br-m> <ofrnxmr:xmr.mx> etc*
16:39:37 <br-m> <ofrnxmr:xmr.mx> I think this ^ > <@syntheticbird> yes, frankfully we need his input on it
16:39:54 <br-m> <redsh4de:matrix.org> same
16:40:05 <br-m> <syntheticbird> @redsh4de:matrix.org: A lot of stuff in the CCS have became usage yet the solution for doing it is still annoying in the long-term.
16:40:10 <br-m> <ofrnxmr:xmr.mx> Also some proposers like vt do their own MRs to update their proposal milestones
16:40:42 <br-m> <ofrnxmr:xmr.mx> So his proposals show completed milestones before payments
16:41:07 <br-m> <syntheticbird> In the timeline we make a distinction between milestone completed and payment
16:41:38 <br-m> <syntheticbird> hell, i'm hesitating to make an event "milestone claimed" instead just so we can have another event for saying it is contested
16:42:28 <br-m> <redsh4de:matrix.org> maybe the event could be queued and needs to be approved... but thats just the same merge request then
16:44:05 <br-m> <syntheticbird> I'm afraid that would justify a reject because plowsof or luigi don't wanna have to approve it.
16:44:19 <br-m> <syntheticbird> Ideally it should be automated and built solely on the gitlab MR timeline
16:44:36 <br-m> <syntheticbird> So gitlab comments and tracking of the md file
16:45:20 <br-m> <ofrnxmr:xmr.mx> if not using bot, Just track the md, since thats gospel
16:45:28 <br-m> <ofrnxmr:xmr.mx> The md cant/wont be updated if not approved
16:45:31 <br-m> <redsh4de:matrix.org> yeah, we can send out webhook events upon changes to a file
16:46:04 <br-m> <redsh4de:matrix.org> https://docs.gitlab.com/user/project/integrations/webhook_events/
16:46:09 <br-m> <syntheticbird> @redsh4de:matrix.org: If that is not possible there could always be a cache and polling solution
16:46:20 <br-m> <ofrnxmr:xmr.mx> @syntheticbird: Can even just monitor luigis acti>ity rss feed :P
16:46:42 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: yo that's a good idea, i completely forgot rss
16:47:04 <br-m> <syntheticbird> ideally not hardcoding a user would better however
16:47:22 <br-m> <ofrnxmr:xmr.mx> We montitor binary's to know when generalfund donates to a proposal
16:47:50 <br-m> <redsh4de:matrix.org> polling or is it streamed somehow? idk how RSS works too well
16:47:53 <br-m> <ofrnxmr:xmr.mx> @syntheticbird: Well, luigi is the only one merging anything or commiting directly
16:48:02 <br-m> <syntheticbird> @redsh4de:matrix.org: in RSS case, polled
16:48:06 <br-m> <ofrnxmr:xmr.mx> @redsh4de:matrix.org: You'd poll the rss feed fot updates
16:48:50 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: fair
16:49:31 <br-m> <syntheticbird> anyway i think there is a lot of solution but we need luigi approval on that. One other topic is the addition of fields in the md file
16:49:31 <br-m> <redsh4de:matrix.org> hmmm... this is me being pedantic but i like the webhook approach (respond to event) vs polling (look for event) better
16:49:31 <br-m> <redsh4de:matrix.org> can maybe do both like i had outlined in my proposal, and prioritize webhook if available, otherwise could poll the RSS
16:49:56 <br-m> <redsh4de:matrix.org> right, to seperate the types of the proposal
16:50:09 <br-m> <syntheticbird> @redsh4de:matrix.org: of course i prefer webhook too. Just searching fallback in case there is a disagreement somehow
16:50:56 <br-m> <syntheticbird> @redsh4de:matrix.org: authors too
16:51:07 <br-m> <syntheticbird> A proposal should be able to support multiple authors
16:51:24 <br-m> <ofrnxmr:xmr.mx> @syntheticbird: i think we dont like that
16:51:52 <br-m> <syntheticbird> oh
16:51:55 <br-m> <syntheticbird> was it brought up in the past?
16:51:57 <br-m> <ofrnxmr:xmr.mx> there have been a few proposals with multiple authors that fell apart due to no one taking responsibility
16:52:09 <br-m> <ofrnxmr:xmr.mx> Pointing fingers at their partner etc
16:52:29 <br-m> <ofrnxmr:xmr.mx> Yea. The "author" now should be the one owning responsibility
16:52:35 <br-m> <redsh4de:matrix.org> yeah i remember reading a few of those when lurking, makes sense
16:52:44 <br-m> <ofrnxmr:xmr.mx> And the payouts go to the author for them to deal with
16:53:12 <br-m> <syntheticbird> Fair. That again was for transparency of who was behind a proposal. Maybe we can add a co-author field then
16:53:30 <br-m> <ofrnxmr:xmr.mx> Not 2 diff authors fighting over who did what and attempting to clain milestones for other peoples work, or abandoning some milestones while author2 completes their work
16:53:31 <br-m> <syntheticbird> then we would know who is owning responsibility
16:53:35 <br-m> <redsh4de:matrix.org> sounds like a good middle ground
16:53:57 <br-m> <ofrnxmr:xmr.mx> The biggest example was the infighting with mj and endor and the crumbling of the soloptxmr ccs
16:54:28 <br-m> <ofrnxmr:xmr.mx> Mj claiming that he wants pay for endors work, endor not completibg his milestones, mj getting paid in full to abandon the ccs
16:55:15 <br-m> <syntheticbird> interesting
16:55:40 <br-m> <ofrnxmr:xmr.mx> Initially mj had claimed that he would complete the ccs regardless of whether endor delivered. In the end, mj wanted pay for all of his own completed milestones (and was paid), and the ccs was left in limbo, unfinished
16:55:47 <br-m> <ofrnxmr:xmr.mx> Where it still is today
16:56:08 <plowsof> and now drones are targeting solar panels, final nail in the coffin
16:56:32 <br-m> <ofrnxmr:xmr.mx> rip
16:56:42 <br-m> <syntheticbird> im sure one day humans would be a good energy source for mining
16:56:53 <br-m> <syntheticbird> i'm not an ai
16:57:00 <br-m> <redsh4de:matrix.org> @redsh4de:matrix.org: the seperate types would be milestone-based and time-based iirc - any other im forgetting?
16:57:20 <br-m> <syntheticbird> Pool too
16:57:25 <br-m> <syntheticbird> for cases like FCMP++ research
16:57:41 <br-m> <syntheticbird> and that's about it
16:57:57 <br-m> <ofrnxmr:xmr.mx> events are prepaid
16:58:47 <br-m> <ofrnxmr:xmr.mx> or, i guess, sometines repaid
16:58:58 <br-m> <redsh4de:matrix.org> you mean events like c3 or monerokon?
16:59:02 <br-m> <ofrnxmr:xmr.mx> Yeh
16:59:15 <br-m> <ofrnxmr:xmr.mx> They could fallbunder time-based maybe
16:59:45 <br-m> <syntheticbird> We can add a category
16:59:52 <br-m> <ofrnxmr:xmr.mx> But time-based is more for N-months work on X proposals
17:00:06 <br-m> <syntheticbird> not sure what name to choose tho
17:00:07 <br-m> <ofrnxmr:xmr.mx> @syntheticbird: My memory isnt good enough to remember our convo
17:00:22 <br-m> <ofrnxmr:xmr.mx> Getting old
17:00:27 <br-m> <syntheticbird> me too
17:00:39 <br-m> <syntheticbird> dw, it's just beam from space into our brain
17:01:08 <plowsof> https://plowsof.github.io/chatgpt-ccs-proposal-form.html
17:01:20 <br-m> <redsh4de:matrix.org> ah, what about retroactive ones? are those still a thing?
17:01:28 <br-m> <ofrnxmr:xmr.mx> Do you guys have mockups outside of whats on syn's ccs
17:01:42 <br-m> <syntheticbird> @redsh4de:matrix.org: Yes but those are an additional tag
17:01:50 <br-m> <ofrnxmr:xmr.mx> @redsh4de:matrix.org: Yea. Retroactive and prepaid are both a thing
17:02:06 <br-m> <redsh4de:matrix.org> @syntheticbird: yeah i think just tagging solves it
17:02:11 <br-m> <redsh4de:matrix.org> @ofrnxmr:xmr.mx: for the website design have some screenshots on mine
17:03:19 <br-m> <ofrnxmr:xmr.mx> Ok maybe diego can discuss with luigi about backend changes and then diego + community can talk about the frontend designs
17:03:39 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: do you tihnk its possible to have a retroactive ccs with no progress to be seen
17:03:50 <br-m> <ofrnxmr:xmr.mx> No
17:03:51 <br-m> <syntheticbird> like literally it's finished
17:03:58 <br-m> <ofrnxmr:xmr.mx> Oh
17:04:03 <br-m> <ofrnxmr:xmr.mx> Yes
17:04:19 <br-m> <ofrnxmr:xmr.mx> The fcmp++ paper was retroactive
17:04:21 <br-m> <redsh4de:matrix.org> plowsof: nice, i like this concept, could be something to integrate for ease of use for proposers
17:04:42 <br-m> <syntheticbird> ok well then i'm not sure if we should make a new type "finished" and retroactive or just tag retroactive with 1 milestone
17:05:27 <br-m> <syntheticbird> An additional point of discussion we forgot is view transition introduction in the website. > <@ofrnxmr:xmr.mx> Ok maybe diego can discuss with luigi about backend changes and then diego + community can talk about the frontend designs
17:05:31 <br-m> <syntheticbird> but that is related to my CCS only
17:05:42 <br-m> <pyxmr2025:mozilla.org> https://mrelay.p2pool.observer/m/mozilla.org/f4d4d3fa5941ebd97ea0ff12e389b52d70a409d62037939191970529280.png (image.png)
17:05:46 <br-m> <ofrnxmr:xmr.mx> The retroactive proposals would have the milestone marked as completed, yeah. Ideally the community woukd ve aware of the proposal before it is in the idea stage
17:05:57 <br-m> <pyxmr2025:mozilla.org> ‘’layout: wip‘’
17:06:06 <br-m> <ofrnxmr:xmr.mx> Iike "i plan to do abc. Will request funding if successfull"
17:06:11 <br-m> <pyxmr2025:mozilla.org> not layout:fr?
17:06:20 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: Understood
17:06:40 <br-m> <ofrnxmr:xmr.mx> Like dangerousfreedom's current ccs. Its a single milestone, and wont be claimed until successful. Its essentially retroactive
17:07:28 <br-m> <ofrnxmr:xmr.mx> DFs is an exception though, because the funds are already available
17:07:46 <br-m> <syntheticbird> btw
17:07:49 <br-m> <redsh4de:matrix.org> in this case we don't even need a seperate tag - if the proposal is in the funding stage with a completed milestone the page can infer that it is retroactive > <@ofrnxmr:xmr.mx> The retroactive proposals would have the milestone marked as completed, yeah. Ideally the community woukd ve aware of the proposal before it is in the idea stage
17:07:58 <br-m> <syntheticbird> There is a mock up for a fund calculation section in the proposal page
17:08:15 <br-m> <syntheticbird> Which shows in an intuitive manner the calculation of the price of the proposal.
17:08:35 <br-m> <ofrnxmr:xmr.mx> Some people (jeffro, myself, 0xfff) dont price in $
17:08:37 <br-m> <syntheticbird> This would ideally be converted by the frontend if it detects a section with the correct syntax. Tbd
17:08:54 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: don't worry it will be versatile enough
17:09:14 <br-m> <ofrnxmr:xmr.mx> Some aggresively price in dollars and will adjust their proposal 10x before merge if the price changes
17:09:44 <br-m> <ofrnxmr:xmr.mx> And some have been known to abandon their proposals if the $ amount falls, but to happily accept price appreciation :d
17:09:46 <br-m> <syntheticbird> @redsh4de:matrix.org: That is fair.
17:10:01 <br-m> <syntheticbird> s/fair/great idea
17:10:23 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: haveno?
17:10:40 <br-m> <ofrnxmr:xmr.mx> So, im not in favor of any $ calculation of the proposals. I dont like that people ask for $ from the ccs, or relate the ccs to dollars
17:10:58 <br-m> <redsh4de:matrix.org> i think in this case the funding properties would also have to be a part of the frontmatter, so that the website can easily parse them
17:10:58 <br-m> <redsh4de:matrix.org> amounts would still have to be in XMR
17:11:13 <br-m> <ofrnxmr:xmr.mx> If you want dollara, you should use magic
17:11:19 <br-m> <ofrnxmr:xmr.mx> i prefer CCS to remain as 1xmr = 1xmr and people should accept what they asked for and not complain
17:11:49 <br-m> <redsh4de:matrix.org> agree, if going the frontmatter route everything should be specified in XMR
17:11:49 <br-m> <redsh4de:matrix.org> with the dollar cost reasoning remaining in the comments
17:11:58 <br-m> <redsh4de:matrix.org> but the website itself would work around XMR values
17:11:58 <br-m> <ofrnxmr:xmr.mx> I mean, on proposals we raide "70xmr" not "$23100 USD"
17:12:08 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: I mean sure. That's just that because most people are explaining in their proposal how they come up with their XMR price I thought this could be parsed and displayed nicely
17:12:15 <br-m> <ofrnxmr:xmr.mx> I dont like that $ are involved in ccs at all
17:12:53 <br-m> <ofrnxmr:xmr.mx> It actually annoys me when peopke write like "$40/hr + 0.3xmr/hr" its just misleading
17:14:06 <br-m> <redsh4de:matrix.org> i think the $ stuff could just be a client side conversion or smth, but that requires a pricing api and... bleh, more moving parts
17:14:06 <br-m> <redsh4de:matrix.org> easier to just have the website work around XMR values
17:14:26 <br-m> <syntheticbird> @redsh4de:matrix.org: in my original idea, the user would provide with the syntax the conversion rate
17:14:44 <br-m> <ofrnxmr:xmr.mx> My vote is no $ on the ccs website
17:14:52 <br-m> <syntheticbird> I'm afraid what i said is not interpreted as i wanted
17:15:21 <br-m> <redsh4de:matrix.org> @syntheticbird: ah, you mean like in the frontmatter? its effectively the proposal configuration
17:15:23 <br-m> <syntheticbird> the "fund calculation" section isn't calculating any fund whatsoever. It's literally just parsing that section everyone is writing explaining how they come up with their XMR price and display it nicely
17:15:58 <br-m> <ofrnxmr:xmr.mx> I think, honestly, is discouraging for donors
17:16:09 <br-m> <ofrnxmr:xmr.mx> And gives people on the internet sonethinf tk bitch about
17:16:19 <br-m> <syntheticbird> @redsh4de:matrix.org: may it be frontmatter or body directly
17:16:44 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: They are already doing it
17:16:44 <br-m> <redsh4de:matrix.org> frontmatter would let the website easily parse it due to it being yaml
17:16:45 <br-m> <redsh4de:matrix.org> structured data ftw
17:16:46 <br-m> <syntheticbird> I mean the proposers
17:16:54 <br-m> <syntheticbird> They are already explaining there prices in comments, that changes nothing
17:16:57 <br-m> <ofrnxmr:xmr.mx> @syntheticbird: nobody every conplained about bermans ccs amounts (like 100xmr/mth) until someone put it in dollar amounts and started tweetint about ut
17:17:35 <br-m> <syntheticbird> @syntheticbird: mea culpa i meant proposers
17:18:37 <br-m> <redsh4de:matrix.org> @ofrnxmr:xmr.mx: idk, tweeter has shown that the loud peanut gallery there aren't really worth paying mind to
17:18:37 <br-m> <redsh4de:matrix.org> it's the OVK debacle and kayaba being a federal agent trying to break monero take all over again
17:18:55 <br-m> <ofrnxmr:xmr.mx> the ovk debate started here, by contributors
17:18:55 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: if twitter wanna bitch about it they will bitch about it. This explanation doesn't have to be mandatory. But there will always be people to take the total amount of XMR, dividing it and changing to usd
17:19:43 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: yeah it was lacking as much substance as twitter
17:19:44 <br-m> <redsh4de:matrix.org> tldr: haters gonna hate
17:19:52 <br-m> <ofrnxmr:xmr.mx> I agree, but im still against putting $ on getmonero
17:20:01 <br-m> <ofrnxmr:xmr.mx> @ofrnxmr:xmr.mx: Thats too "MAGIC" for me
17:20:09 <br-m> <redsh4de:matrix.org> I think that is fair
17:20:34 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: alright. I think it doesn't change anything as people are already doing it
17:20:55 <br-m> <syntheticbird> well
17:20:56 <br-m> <syntheticbird> my CCS
17:21:10 <br-m> <redsh4de:matrix.org> funding is in XMR, should be specified in XMR - the proposer is free to add dollar explanations in descriptions like people are already doing it, etc
17:21:10 <br-m> <redsh4de:matrix.org> but it makes sense for the UI elements to display XMR values
17:21:49 <br-m> <syntheticbird> @redsh4de:matrix.org: ok
17:22:20 <br-m> <redsh4de:matrix.org> i am partial to the idea of adding a client-side conversion thing that doesnt require a API though
17:23:09 <br-m> <syntheticbird> partial?
17:23:13 <br-m> <redsh4de:matrix.org> more so have a problem with specifying dollar values in the frontmatter, if that makes sense
17:23:24 <br-m> <redsh4de:matrix.org> seems "unclean"
17:23:40 <br-m> <syntheticbird> yeah that's fair
17:23:45 <br-m> <redsh4de:matrix.org> open to the idea, seems like a good way of handling it
17:23:56 <br-m> <ofrnxmr:xmr.mx> Some ppl like "using the 200ma from coingecko cuz the orice is reallt high rn"
17:23:56 <br-m> <ofrnxmr:xmr.mx> Some ppl like "using the 10ma from kraken because the price dipped this week"
17:24:07 <br-m> <ofrnxmr:xmr.mx> Ofrn loke "idgaf what price games u wanna play. How many xmr?"
17:24:58 <br-m> <ofrnxmr:xmr.mx> "+20% buffer"
17:25:14 <br-m> <syntheticbird> The meeting is near an hour and a half. Have we touched all the main topics for thinking further about it?
17:26:02 <br-m> <redsh4de:matrix.org> final thing id like to bring up are the backend changes
17:26:02 <br-m> <redsh4de:matrix.org> effectively saying bye bye to PHP
17:26:08 <br-m> <syntheticbird> YES
17:26:28 <br-m> <diego:cypherstack.com> yes please
17:26:43 <br-m> <diego:cypherstack.com> was made that way because the person pony assigned to help with the backend was proficient in PHP
17:27:38 <br-m> <redsh4de:matrix.org> damn okay good to hear there's support for that, i thought it would be much more contentious lol
17:27:49 <br-m> <redsh4de:matrix.org> in its place, we propose Deno (which has some parallels with XMR, peep the docs) and using SQLite instead of a seperate service
17:28:12 <br-m> <redsh4de:matrix.org> Deno also kind of puts Rust on the backend
17:28:30 <br-m> <syntheticbird> lowkey deno safer than apache
17:28:47 <br-m> <redsh4de:matrix.org> Here's why Deno is awesome: https://docs.deno.com/runtime/fundamentals/security/#key-principles
17:37:21 <br-m> <redsh4de:matrix.org> one thing thats cool is that if we do partial server-rendering for the CCS page, the frontend and backend could be just one repo
17:37:45 <br-m> <redsh4de:matrix.org> any questions or anything anyone would like to discuss pertaining for this?
17:39:31 <br-m> <ofrnxmr:xmr.mx> I think just for diego to consult with his team & luigi
17:39:46 <br-m> <ofrnxmr:xmr.mx> Re any backend change selection
17:40:28 <br-m> <redsh4de:matrix.org> sounds good
17:40:33 <br-m> <redsh4de:matrix.org> anything else anyone would like to talk about?
17:41:52 <br-m> <ofrnxmr:xmr.mx> Not many people here today :P, so were just discussing amongst ourselves. Hopefully people can chime in throughout the week if they have anything tl add
17:41:52 <br-m> <syntheticbird> nope
17:41:57 <br-m> <ofrnxmr:xmr.mx> Or suggest
17:42:24 <br-m> <syntheticbird> @ofrnxmr:xmr.mx: sure we're looking at this channel anyway
17:43:41 <br-m> <redsh4de:matrix.org> alright, we can end here
17:43:42 <br-m> <redsh4de:matrix.org> Thanks everyone!
17:43:49 <br-m> <syntheticbird> thanks
17:43:51 <br-m> <redsh4de:matrix.org> total runtime: 1h 43m****
```

# Action History
- Created by: redsh4de | 2026-03-28T15:55:44+00:00
- Closed at: 2026-03-28T17:46:06+00:00
