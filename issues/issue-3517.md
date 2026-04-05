---
title: 'error: "method not found" error: -32601 ?'
source_url: https://github.com/xmrig/xmrig/issues/3517
author: alabasterclay
assignees: []
labels: []
created_at: '2024-07-28T04:27:54+00:00'
updated_at: '2025-06-18T22:08:56+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:08:56+00:00'
---

# Original Description
Have ran rx.unmineable.com:3333 with xmrig wizard config settings no problem.
Changed to ghostrider.unmineable.com:3333 (and tried other ports and ssl) but get error:
**error: "method not found" error: -32601**
Searched and can not find reference to reason or error code.
Have tried turning off and on various config settings but no luck.
Don't know what the error is referencing.

# Discussion History
## SChernykh | 2024-07-28T07:06:25+00:00
This url uses a different algorithm. You need to add `-a gr` to XMRig command line to use GhostRider algorithm. https://xmrig.com/docs/miner/command-line-options

## MTCHANNELL | 2024-07-28T23:17:13+00:00
example ;

GR : xmrig.exe -a gr -o stratum+ssl://ghostrider-us.unmineable.com:443 -u walletaddress.workername -p x

RX : xmrig.exe -a rx -o stratum+ssl://rx-us.unmineable.com:443 -u walletaddress.workername -p x

## alabasterclay | 2024-07-28T23:19:30+00:00
Solved with using strictly terminal start-up referenced by above comments.
Was using config.json with algo=auto and it would fail.

## juniormayhe | 2024-10-31T18:52:19+00:00
in config json you can set an entry 

"algo": "gr"

that will make it use ghostrider, so you don't need to customize the cli command.
I guess this algo may yield better results on gpu 

# Action History
- Created by: alabasterclay | 2024-07-28T04:27:54+00:00
- Closed at: 2025-06-18T22:08:56+00:00
