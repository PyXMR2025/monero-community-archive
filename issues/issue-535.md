---
title: Monero Space Meeting - Sunday 3 January 2021 @ 18 UTC
source_url: https://github.com/monero-project/meta/issues/535
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2020-12-30T20:45:08+00:00'
updated_at: '2021-01-05T15:13:19+00:00'
type: issue
status: closed
closed_at: '2021-01-05T15:13:19+00:00'
---

# Original Description
### Meeting location:

#monero-space on Freenode IRC

Relayed on Matrix/Element

### Time

18 UTC (noon CT Chicago)

### Agenda

0. Introduction/Greetings
1. Monero Space updates (what we all have been working on)
2. Other Monero community project updates
3. What's happening in the next week
4. Services maintenance improvements (xmrscott)
5. Ideas time

# Discussion History
## scottAnselmo | 2021-01-03T01:21:47+00:00
Proposed agenda items:

- Reducing mean time to repair (MTTR):
 - Before releasing a service to the public the following criteria should be followed:
  1. **(Mandatory)** All faceless/system account names, and passwords if applicable must be documented
  2. **(Mandatory)** Basic infrastructure documented (e.g. is there a local SMTP server, or is email sent out via API)
  3. (Encouraged) Two+ people are 'trained' in at least the basic infrastructure of a service. Presumably this would be the person who spun up said service originally, and one+ shadow. Expectation of the shadow is that they'd be capable to upgrade a service (e.g. Flarum 0day happens, a critical security patch is put out that needs to be installed while the 'main' is out)
-  (Open for any comments on things people feel should be gatekeepers for a release)
[...]
- Documentation: Where/how to best document the above info and how best to limit access?

# Action History
- Created by: SamsungGalaxyPlayer | 2020-12-30T20:45:08+00:00
- Closed at: 2021-01-05T15:13:19+00:00
