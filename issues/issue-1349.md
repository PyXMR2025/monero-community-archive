---
title: Monero Research Lab Meeting - Wed 04 March 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1349
author: Rucknium
assignees: []
labels: []
created_at: '2026-03-04T16:05:48+00:00'
updated_at: '2026-03-18T16:24:31+00:00'
type: issue
status: closed
closed_at: '2026-03-18T16:24:31+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294).

4. [FCMP alpha stressnet](https://monero.town/post/6763165).

5. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1346 

# Discussion History
## Rucknium | 2026-03-11T16:44:06+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1349     

> __< rucknium >__ 1. Greetings     

> __< boog900 >__ Hi     

> __< jberman >__ waves     

> __< vtnerd >__ yi     

> __< vtnerd >__ *hi     

> __< rbrunner >__ Hello     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< vtnerd >__ me: finally looking at the 0-conf issue in fcmp++/monerod/lws. Otherwise was working on the new /feed (/push) protocol on lws     

> __< rbrunner >__ Wrote a report after completing my investigation into Polyseed use in Monero wallets: https://github.com/tevador/polyseed/issues/13#issuecomment-3980281619     

> __< jberman >__ me: prepared FCMP++ crypto for audit, the PR's are upstreamed to the monero repo, reviewed jeffro's FCMP++ scaling PR, implemented the wallet-side max fee     

> __< boog900 >__ I have finally opened the PR to update cuprates databases to the new tapes db and fjall. Once this is merged cuprate will have a smaller and faster DB. Especially noticeable on HDDs or other storage I/O constrained computers.      

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294).     

> __< jberman >__ All the PR's there are open, planning to communicate with audit firms in this next week to audit those PR's     

> __< jberman >__ Will get quotes, and then aiming to use that as a basis for a CCS to then raise funds for all 4 stages of the audit     

> __< rucknium >__ Sounds good to me. Anything more on this agenda item?     

> __< jberman >__ nothin from me     

> __< rucknium >__ 4. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< jberman >__ No update on alpha. The only current lingering item is that 0-conf issue vtnerd mentioned. I think we're in position to remove alpha from the agenda and move on to beta     

> __< rucknium >__ Can --max-connections-per-ip be set to 10 by default for beta stressnet?     

> __< rucknium >__ Helps when multiple nodes are behind the same IP address.     

> __< jberman >__ it currently defaults to 100 looks like, you want it limited further?     

> __< rucknium >__ I thought it's 1     

> __< rucknium >__ Nevermind if it's already set to 100.     

> __< jeffro256 >__ Howdy sorry I'm late      

> __< rucknium >__ 5. Any other business.     

> __< jberman >__ rucknium: reviewing     

> __< jeffro256 >__ https://github.com/monero-project/monero/blob/ea9be68fb66f66605d857e1ee13e92fb1d50423b/src/p2p/net_node.cpp#L172     

> __< jberman >__ I think what I mentioned was for RPC, and you're right p2p max is 1. I don't see an issue with raising that to 10     

> __< jeffro256 >__ RPC is 3 https://github.com/monero-project/monero/blob/ea9be68fb66f66605d857e1ee13e92fb1d50423b/src/cryptonote_config.h#L133     

> __< jeffro256 >__ I also don't see an isue raising the default for stressnet. I can add it to the TODO list      

> __< jberman >__ I was (mistakenly) corresponding that daemon flag with this default: https://github.com/monero-project/monero/blob/ea9be68fb66f66605d857e1ee13e92fb1d50423b/src/cryptonote_config.h#L135     

> __< rucknium >__ You can mark the commit raising it to 10 as only for stressnet. The Monero Research Computing Cluster, i.e. the source of much of the tx spam, usually has multiple nodes behind a single IP.     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< jeffro256 >__ Thanks everyone     






# Action History
- Created by: Rucknium | 2026-03-04T16:05:48+00:00
- Closed at: 2026-03-18T16:24:31+00:00
