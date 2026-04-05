---
title: More control over Miner behaviour.
source_url: https://github.com/xmrig/xmrig/issues/3619
author: Acceleration2299
assignees: []
labels: []
created_at: '2025-01-19T07:40:26+00:00'
updated_at: '2025-01-21T05:31:47+00:00'
type: issue
status: closed
closed_at: '2025-01-21T05:31:47+00:00'
---

# Original Description
Hello, I use XMRig in a more casual sense then full-on, using whole computers for nothing but mining.

I've been trying to headbutt my way though the config.json/commandline arguments, but it doesnt seem to be working.

I've been trying to get XMRig to *not touch* the first 4 logical processors of my system, as i would like those free for my operating system, and or most applications to use them in its place.

My config file reads out as...

[config.json](https://github.com/user-attachments/files/18468052/config.json)
and my .cmd reads out as
``@echo off``
``cd /d "%~dp0"``
``xmrig.exe -o rx.unmineable.com:3333 -a rx -k -u DOGE:DDAZ4MMLEFZPScPKtcBeWjoGPTXS9iDgFG.LeinCPU -p x``
``pause``

which, now that i'm writing this issue, i realise it's not even acknowledging the config file, is it?

# Discussion History
## geekwilliams | 2025-01-19T08:10:25+00:00
Because you're passing parameters in your cmd file xmrig is ignoring config.json.  Try changing your cmd file so that the only params passed to xmrig are -c config.json 

## Acceleration2299 | 2025-01-20T19:17:21+00:00
I did try this, and it's working well now, Thank you.

On Sun, Jan 19, 2025, 03:10 geekwilliams ***@***.***> wrote:

> Because you're passing parameters in your cmd file xmrig is ignoring
> config.json. Try changing your cmd file so that the only params passed to
> xmrig are -c config.json
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3619#issuecomment-2600750844>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BAOSLGMNLOURTWJKOPYRJND2LNMYPAVCNFSM6AAAAABVONYVFOVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDMMBQG42TAOBUGQ>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


# Action History
- Created by: Acceleration2299 | 2025-01-19T07:40:26+00:00
- Closed at: 2025-01-21T05:31:47+00:00
