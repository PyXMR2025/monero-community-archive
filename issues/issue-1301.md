---
title: 'Monero Community Workgroup Meeting: Nov 22nd 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1301
author: plowsof
assignees: []
labels: []
created_at: '2025-11-22T12:28:23+00:00'
updated_at: '2025-12-02T13:28:26+00:00'
type: issue
status: closed
closed_at: '2025-12-02T13:28:26+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time:
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
    - Monero v0.18.4.4 release [getmonero blog](https://www.getmonero.org/blog/)
    - [Jberman CCS update](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/600#note_33193)
    - https://ccs.getmonero.org/funding-required/
    - Skylight Wallet (Connects to any monero-lws instance via clearnet or tor) [github apk](https://github.com/MAGICGrants/skylight-wallet/releases/tag/v1.0.1) via sgp_ MAGICGrants , ajs_ hosting public monero-lws instance @ https://lws.moneromerchant.com/ (inquire how to join)
    - monero-site has its first "release" on github ever after rando suggested a changelog [github release page](https://github.com/monero-project/monero-site/releases)
    - DataHorder doing things (fairly untested and work in progress) [Helios and Selene, in Go a curve cycle towering Ed25519](https://git.gammaspectra.live/P2Pool/helioselene)    
    - Getmonero redesign in progress @ https://getmonero-redesign-impl.vercel.app/ by redshade
    - ofrnxmr release basicswap-bash update [monero.observer](https://monero.observer/nahuhh-releases-basicswap-bash-v0.15.1/)
    - monero-torrent updated to latest release [github releases](https://github.com/plowsof/monero-torrent/releases) - plowsof
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This week in Monero](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [39C3 Support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2026](https://MoneroKon.org/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [FCMP++ Stressnet updates](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1293)    

Meeting logs will be posted here afterwards.   

# Discussion History
## plowsof | 2025-11-22T17:19:42+00:00
thoughts and prayers for monerologs.net
```
Sat, Nov 22, 2025, 16:00:26 - plowsof: Meeting time https://github.com/monero-project/meta/issues/1301 
Sat, Nov 22, 2025, 16:00:29 - plowsof: greetings
Sat, Nov 22, 2025, 16:01:07 - SH3LLC0D3R joined the room
Sat, Nov 22, 2025, 16:02:04 - plowsof: v0.18.4.4 has been released https://github.com/monero-project/monero/releases 
Sat, Nov 22, 2025, 16:04:16 - ofrnAI: Morning
Sat, Nov 22, 2025, 16:04:19 - plowsof: https://ccs.getmonero.org/funding-required/ 🙏
Sat, Nov 22, 2025, 16:05:04 - ArticMine left the room
Sat, Nov 22, 2025, 16:05:47 - plowsof: how is stressnet going? jbermans CCS comment contains recent updates https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/600#note_33193 
Sat, Nov 22, 2025, 16:06:26 - ofrnAI: Important update for ledger owners
Sat, Nov 22, 2025, 16:07:08 - ofrnAI: People testing pre-release builds of 1.5
Sat, Nov 22, 2025, 16:07:35 - ofrnAI: Syncing on 2gb ram systems is possible
Sat, Nov 22, 2025, 16:07:48 - ofrnAI: (which is probably better than current master ...o
Sat, Nov 22, 2025, 16:07:50 - ofrnAI: )
Sat, Nov 22, 2025, 16:08:16 - ofrnAI: I also noticed that, without checkpoints, you can greatly increase sync speed by setting prep-block-threads=$(nproc)
Sat, Nov 22, 2025, 16:08:49 - plowsof: thanks tobtoht for the ledger fix 🥲 refusing to export view key on ledger results in an error. and avoids invalid subaddresses being generated there after 😬
Sat, Nov 22, 2025, 16:08:55 - ofrnAI: So even when doong a checkpointed sync, it should speed up the last few thousand blocks that are after the checkpoints
Sat, Nov 22, 2025, 16:10:36 - ofrnAI: I think the subaddrs are "valid" in that you can send xmr to them, but invalid in that you cannot access the funds after 
Sat, Nov 22, 2025, 16:11:47 - plowsof: yes, can still be recovered if you restore the wallet , not too evil 
Sat, Nov 22, 2025, 16:12:15 - ofrnAI: Have to do some special recovery though
Sat, Nov 22, 2025, 16:12:26 - ofrnAI: With llcoins or smthn, iirc
Sat, Nov 22, 2025, 16:12:51 - ofrnAI: Anyway, thx ledger
Sat, Nov 22, 2025, 16:13:24 - plowsof: luigi1111s address generator https://xmr.llcoins.net/
Sat, Nov 22, 2025, 16:15:00 - plowsof: getmonero redesign in progress @ https://getmonero-redesign-impl.vercel.app/ by redsh4de , monero-sites first release page xD https://github.com/monero-project/monero-site/releases 
Sat, Nov 22, 2025, 16:15:48 - plowsof: Skylight Wallet (Connects to any monero-lws instance via clearnet or tor) [github apk](https://github.com/MAGICGrants/skylight-wallet/releases/tag/v1.0.1) via sgp_ MAGICGrants , ajs_ hosting public monero-lws instance @ https://lws.moneromerchant.com/ (inquire how to join)
Sat, Nov 22, 2025, 16:16:20 - plowsof: whats new in basicswap-bash? [monero.observer](https://monero.observer/nahuhh-releases-basicswap-bash-v0.15.1/)
Sat, Nov 22, 2025, 16:17:57 - ofrnAI: Just better mac support, latest release of basicswap was just a couple bug fixes and firo hard fork
Sat, Nov 22, 2025, 16:18:20 - ofrnAI: Working on "light" support (electrum etc, without nodes)
Sat, Nov 22, 2025, 16:18:51 - ofrnAI: Make it easier for takers to use and install it
Sat, Nov 22, 2025, 16:20:31 - plowsof: all of the CCS proposals have been merged, bar 39C3 which left off at it being a pre-announcement with people asking for a cost breakdown , so not much to argue about today
Sat, Nov 22, 2025, 16:20:42 - plowsof: would anyone like to bring something up?
Sat, Nov 22, 2025, 16:21:31 - nioc: DONATE
Sat, Nov 22, 2025, 16:21:36 - Diego Salazar: <@sashimi420:matrix.org "people that cant have arguments ..."> Mm? I didn't ban anyone in research lounge?
Sat, Nov 22, 2025, 16:22:03 - nioc: please donate  :)
Sat, Nov 22, 2025, 16:22:37 - Diego Salazar: <@plowsof:matrix.org "all of the CCS proposals have be..."> Oh right. I have the budget now. 
Sat, Nov 22, 2025, 16:23:47 - Diego Salazar: 2025 Budget CDC 39C3 (rev2) - main(2).pdf (Media omitted)
Sat, Nov 22, 2025, 16:24:39 - Diego Salazar: Two columns. CDC and RIAT. RIAT is stuff covered by them. CDC is stuff we are requesting being covered by sponsors and/or CCS.
Sat, Nov 22, 2025, 16:25:58 - plowsof: Open Hardware badge section caught my eye
Sat, Nov 22, 2025, 16:26:09 - plowsof: thanks for the detailed breakdown 
Sat, Nov 22, 2025, 16:27:27 - Diego Salazar: Yes they're building a hardware badge this year
Sat, Nov 22, 2025, 16:30:28 - Diego Salazar: Any questions on the budget? Happy to answer them if so.
Sat, Nov 22, 2025, 16:34:41 - Diego Salazar: Perfect, as all questions seem to be answered I suppose we can move forward. :D
Sat, Nov 22, 2025, 16:35:51 - rottenwheel: Did you upload it to the MR on repository too?
Sat, Nov 22, 2025, 16:36:35 - plowsof: the Badge development is a significant % of the entire budget, reminds me of https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/397#budget 
Sat, Nov 22, 2025, 16:36:40 - Diego Salazar: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622#note_33203
Sat, Nov 22, 2025, 16:36:42 - Diego Salazar: cerjtainly did
Sat, Nov 22, 2025, 16:37:50 - Diego Salazar: If it makes you feel better, we're not asking for the full amount of expected costs
Sat, Nov 22, 2025, 16:38:06 - Diego Salazar: 70k requested (at current price) out of 115k
Sat, Nov 22, 2025, 16:38:22 - Diego Salazar: with 18k being badge costs requested from sponsors/ccs (the rest given by RIAT)
Sat, Nov 22, 2025, 16:38:38 - Diego Salazar: so if you don't like the open hardware portion, we can just say the Monero money doesn't go to that
Sat, Nov 22, 2025, 16:39:21 - ofrnAI: 3800 for 4 daya at a hotel?
Sat, Nov 22, 2025, 16:39:32 - ofrnAI: Does it come with blow?
Sat, Nov 22, 2025, 16:40:10 - ofrnAI: Like, 3000 worth of blow?
Sat, Nov 22, 2025, 16:40:10 - Diego Salazar: It's the one attached to the site
Sat, Nov 22, 2025, 16:40:25 - rottenwheel: The nerve of this fool, opening his loudmouth ass to talk crap about yours, while he forced himself into getting funded for whopping 1685 XMR under a "supervisor" role. 🤣
Sat, Nov 22, 2025, 16:40:26 - Diego Salazar: although come to think of it, I'm the moderator and I specifically requested not to be included there
Sat, Nov 22, 2025, 16:40:32 - rottenwheel: https://ccs.getmonero.org/proposals/ofrnxmr_basicswap.html
Sat, Nov 22, 2025, 16:40:30 - Diego Salazar: so I'll have him remove that
Sat, Nov 22, 2025, 16:40:37 - ofrnAI: You can probably get a whole houae airbnb with 4 rooms, 3 bathrooms and pool for less than that
Sat, Nov 22, 2025, 16:40:48 - rottenwheel: One thousand, six hundred, eighty five XMR. 🤣
Sat, Nov 22, 2025, 16:41:02 - Diego Salazar: we're talking about C3 budget atm, stay on topic plz
Sat, Nov 22, 2025, 16:41:12 - ofrnAI: Wow, rotten unblocked me 
Sat, Nov 22, 2025, 16:41:27 - Diego Salazar: I have a policy of always staying in attached hotel. Always.
Sat, Nov 22, 2025, 16:41:34 - rottenwheel left the room
Sat, Nov 22, 2025, 16:41:53 - Diego Salazar: I do a monstrous amount of work at these conferences, and need to be able to get back to my room quickly to recharge.
Sat, Nov 22, 2025, 16:42:27 - Diego Salazar: that said, I'm not having you all pay for it ;)
Sat, Nov 22, 2025, 16:43:27 - Diego Salazar: any other thoughts or concerns?
Sat, Nov 22, 2025, 16:43:38 - Diego Salazar: obviously you can bring them up in the MR or in this room at a later time also
Sat, Nov 22, 2025, 16:44:03 - Diego Salazar: although with C3 getting close, would be nice to get this approved or denied so we can know whether to go elsewhere for money if needed
Sat, Nov 22, 2025, 16:47:39 - Diego Salazar: that said, given the slow donations of current proposals in FR I don't foresee it getting funded quickly even if merged
Sat, Nov 22, 2025, 16:48:23 - Diego Salazar: Either way, nothing else from me. :)
Sat, Nov 22, 2025, 16:48:31 - dukenukem (Rotten) joined the room
Sat, Nov 22, 2025, 16:53:09 - plowsof: thanks for joining 🫡 as for the funding required page,  its been less than 24 hours , please have faith in our glorious supporters https://ccs.getmonero.org/funding-required/ 
Sat, Nov 22, 2025, 16:58:17 - SH3LLC0D3R left the room
Sat, Nov 22, 2025, 17:00:57 - plowsof: hour is up, thanks all for joining the cosy meeting, and good luck to those seeking funding at this moment 
Sat, Nov 22, 2025, 17:04:13 - ofrnAI: Thanks
Sat, Nov 22, 2025, 17:11:37 - plowsof: BigmenPixel: can you provide an update/payout request please for the remaining 3.5 xmr https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/381#note_33204 
```

## hinto-janai | 2025-12-01T22:00:01+00:00
@plowsof could this be added to the next meeting?: https://github.com/gupax-io/gupax/issues/137

## plowsof | 2025-12-01T22:05:12+00:00
Thanks for sharing, definitely 

# Action History
- Created by: plowsof | 2025-11-22T12:28:23+00:00
- Closed at: 2025-12-02T13:28:26+00:00
