---
title: Monero Research Lab Meeting - Wed 25 February 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1346
author: Rucknium
assignees: []
labels: []
created_at: '2026-02-25T16:28:03+00:00'
updated_at: '2026-03-11T16:44:14+00:00'
type: issue
status: closed
closed_at: '2026-03-11T16:44:14+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294).

4. [`carrot-core` implementation audit](https://github.com/cypherstack/carrot_core-audit).

5. [FCMP alpha stressnet](https://monero.town/post/6763165).

6. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1343 

# Discussion History
## Rucknium | 2026-03-04T16:04:11+00:00
Log


> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1346     

> __< rucknium >__ 1. Greetings     

> __< jberman >__ waves     

> __< gingeropolous >__ hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< articmine >__ Hi     

> __< gingeropolous >__ monerosim is at a point where i think its done. It could probably use some more user-friendly polish, but i've run multiple runs of the 1k simulation. I'm open to suggestions on how to verify this to complete my CCS milestone.      

> __< rucknium >__ gingeropolous:monero.social: Great! What kind of output does it produce?     

> __< jberman >__ me: continuing final tasks in prep for beginning the FCMP++ integration audit (this PR contains the last major items: https://github.com/seraphis-migration/monero/pull/286 ), and reviewing jeffro256's FCMP++ scaling PR in prep for beta: https://github.com/seraphis-migration/monero/pull/282     

> __< gingeropolous >__ Well, at the base level, the logs from all of the monerod processes and the wallets are created. There's also an analysis function that parses all of these logs and analyzes them, but the analysis portion is still very early, and because i'm no statistician i can't speak to their validity.      

> __< gingeropolous >__ but really, just imagine you can create a network from scratch that produces logs from all of the monerods in the network of 1k nodes.. that you then have direct access to. One of the analyses I like is extracting the dandelion stem path.     

> __< rucknium >__ Later, could you point me where to find the logs and the early analysis on the MRL research computing server? I could start to verify the output there.     

> __< gingeropolous >__ yeah, sounds good. thanks!     

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294).     

> __< jberman >__ I'm working on finalizing FCMP++ integration code in this PR https://github.com/seraphis-migration/monero/pull/286 , and once that's settled, will open the final 2 upstream PR's from "Audit 1: Crypto" (torsion clearing and ed25519 -> wei conversion)     

> __< jberman >__ Then will move forward with audit plans and CCS fundraising. I'm still thinking of doing a 4-phase audit, and 1 CCS proposal that raises what should be enough to cover all phases similar to how we've done it for FCMP++ audits     

> __< jberman >__ Also of note, I opened this upstream PR for the key image generator and unbiased/ biased hash-to-point yesterday (intended to be in scope for Audit 1: Crypto): https://github.com/monero-project/monero/pull/10338     

> __< rucknium >__ Anything more on this agenda item?     

> __< jberman >__ nothing from me     

> __< rucknium >__ 4. carrot-core implementation audit (https://github.com/cypherstack/carrot_core-audit).     

> __< rucknium >__ Last meeting, this audit has just been published. Does anyone have comments or questions after digesting it?     

> __< jberman >__ Haven't had the chance to digest yet on my end. Will do so asap     

> __< rucknium >__ 5. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< jberman >__ The latest alpha generally seems to be running smooth judging by the lack of complaints in the stressnet channel. The latest commentary in the channel looks related to something with LWS, possibly ZMQ in monerod, but haven't dug much into it myself     

> __< vtnerd >__ Damnit forgot this again, here now     

> __< vtnerd >__ Yes I'm going to try to identify the xmr chat issue over the next couple of days. It's difficult to diagnose as missed mempool txes could be dropped in several places     

> __< rucknium >__ Anything else on stressnet?     

> __< jberman >__ Nothing from me     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      

> __< vtnerd >__ I'll give an update since I missed it earlier. I've been working on lws web socket "push" which gives a real time mempool and block feed to clients. It should be less load on server as there's no polling after initial setup, just keep alive pings and small messages. Got some initial unit tests and its looking good     

> __< vtnerd >__ The initial sync should be faster too as it will have better subaddress support in the API and supports magpack which is a few ticks faster with all the binary data     

> __< vtnerd >__ *msgpack     


# Action History
- Created by: Rucknium | 2026-02-25T16:28:03+00:00
- Closed at: 2026-03-11T16:44:14+00:00
