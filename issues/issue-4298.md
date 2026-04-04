---
title: Log menu outputs inaccurate mining info
source_url: https://github.com/monero-project/monero-gui/issues/4298
author: PPPDUD
assignees: []
labels: []
created_at: '2024-03-31T14:08:41+00:00'
updated_at: '2024-03-31T15:02:52+00:00'
type: issue
status: closed
closed_at: '2024-03-31T15:02:51+00:00'
---

# Original Description
Earlier today, I started p2pool mining on the Mini chain.

Next, out of curiosity, I visited Settings>Log and typed the "status" command.

It said the following: `Height: 3117113/3117113 (100.0%) on mainnet, not mining, net hash 1.81 GH/s, v16, 12(out)+0(in) connections, uptime 0d 0h 7m 42s`, despite the fact that I'm actively mining.

I'm using Monero GUI Fluorine Fermi (v0.18.3.2-release) on Windows 11 Pro.

# Discussion History
## selsta | 2024-03-31T14:10:01+00:00
You were mining with p2pool and not monerod. monerod does not know about p2pool mining so it can't display the correct mining status in this case.

## PPPDUD | 2024-03-31T15:02:51+00:00
That will explain a lot! Thanks!

On Sun, Mar 31, 2024, 10:10 AM selsta ***@***.***> wrote:

> You were mining with p2pool and not monerod. monerod does not know about
> p2pool mining so it can't display the correct mining status in this case.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/4298#issuecomment-2028760875>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AZTWPZMNRAYZTRPQGPV66DDY3AKM3AVCNFSM6AAAAABFQONFYCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDAMRYG43DAOBXGU>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


# Action History
- Created by: PPPDUD | 2024-03-31T14:08:41+00:00
- Closed at: 2024-03-31T15:02:51+00:00
