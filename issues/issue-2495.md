---
title: Kevacoin Hash Rate drops from 1K to 300
source_url: https://github.com/xmrig/xmrig/issues/2495
author: apellini
assignees: []
labels: []
created_at: '2021-07-25T20:58:34+00:00'
updated_at: '2021-07-25T21:59:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
On Friday I have seen a drop of Hash Rate from 1KH to 300H without experiencing any hardware issue on my rig.

I could not find any log on file that could explain it.

It happens something not documented in blockchain?

Regards,

Aldo

# Discussion History
## SChernykh | 2021-07-25T21:26:01+00:00
This is a known issue with Windows, read more here: https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide
You need to turn off memory compression and RunFullMemoryDiagnostic task.

## apellini | 2021-07-25T21:59:08+00:00
I'm using Ubuntu Server distro.

Regards,

Aldo Pellini

Il giorno dom 25 lug 2021 alle ore 23:26 SChernykh ***@***.***>
ha scritto:

> This is a known issue with Windows, read more here:
> https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide
> You need to turn off memory compression and RunFullMemoryDiagnostic task.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2495#issuecomment-886259940>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AN5J7TUZO73BZLWNK7SRQ6TTZR6PJANCNFSM5A64RVVA>
> .
>


# Action History
- Created by: apellini | 2021-07-25T20:58:34+00:00
