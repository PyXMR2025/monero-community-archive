---
title: Monero Research Lab Meeting - Wed 11 February 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1340
author: Rucknium
assignees: []
labels: []
created_at: '2026-02-11T01:50:41+00:00'
updated_at: '2026-02-25T16:20:59+00:00'
type: issue
status: closed
closed_at: '2026-02-25T16:20:59+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. FCMP code integration audit prep.

4. [FCMP alpha stressnet](https://monero.town/post/6763165).

5. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1337 

# Discussion History
## Rucknium | 2026-02-18T16:49:26+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1340     

> __< rucknium >__ 1. Gtreetings     

> __< rbrunner >__ Hello     

> __< jberman >__ waves     

> __< articmine >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< jberman >__ me: PR followup, set up a 4-phase plan to get the FCMP++ integration audited, got pre-fork multisig working / tests passing     

> __< rucknium >__ 3. FCMP code integration audit prep.     

> __< syntheticbird >__ Hi     

> __< jberman >__ My current plan on the table is to have the fcmp++-stage in the seraphis-migration repo ready for auditing. I'd like to audit the integration code in 4 phases: 1) Crypto, 2) Crypto Integration, 3) Tree building / prove / verify, 4) Consensus integration     

> __< jberman >__ Each subsequent phase essentially utilizes the building blocks of its preceding phase      

> __< vtnerd >__ Hi     

> __< jberman >__ So right now, I have PR's prepped (and am working with jeffro to get those PR's merged), and then would like to get started with auditing on a specific commit of fcmp++-stage     

> __< vtnerd >__ Sorry for late followup: me: testing changes to boost beast in lwsf. Getting monero_c/lwsf to work on macos should be completed      

> __< rbrunner >__ So with possible working-in of the results of one phase's audit results before going to the audit of the next phase?     

> __< jberman >__ Of note, I've already opened a couple PR's upstream, which jeffro and vtnerd reviewed. I'm proposing we get that code + other related building block crypto audited as well     

> __< jberman >__ rbrunner: Yes. I'm thinking about a distinct CCS like kayaba's where I raise funds for the audits in advance, to minimize downtime between each phase      

> __< rbrunner >__ I see.     

> __< rbrunner >__ Makes sense     

> __< rbrunner >__ Will be interesting to see how long the whole process takes, over all 4 phases     

> __< jberman >__ Here are the specific sections I want to get audited: https://paste.debian.net/hidden/82c00500     

> __< jberman >__ rbrunner: I think 3 months is a reasonable expectation. First 2 audit phases ~1 month, and the latter 2 ~two months     

> __< rbrunner >__ Sounds like a good sprint :)     

> __< rbrunner >__ Hopefully without burnout at the end ...     

> __< rucknium >__ Do you have specific firm(s) in mind?     

> __< jberman >__ Will probably start with CS if they have availability between the other work     

> __< rucknium >__ Code auditing plan sounds good to me. I am no code auditing expert of course :)     

> __< rucknium >__ Anything else on this agenda item?     

> __< jberman >__ Nothing from me :)     

> __< rucknium >__ 4. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< jberman >__ It seems ofrnxmr:monero.social has identified a new issue to work through when blocks increase in size that I'll look into today. Tx relay v2 appears to be running smoothly     

> __< jberman >__ We're still going on beta tasks (scaling, finalizing code, awaiting kayaba's availability to open up as well)     

> __< rucknium >__ Sounds good. Anything else about stressnet?     

> __< jberman >__ Nothing from me     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      

> __< jberman >__ thank you     

> __< syntheticbird >__ A short meeting that's rare     

> __< syntheticbird >__ thx     



# Action History
- Created by: Rucknium | 2026-02-11T01:50:41+00:00
- Closed at: 2026-02-25T16:20:59+00:00
