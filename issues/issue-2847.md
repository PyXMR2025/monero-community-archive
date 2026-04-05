---
title: Nvidia rtx
source_url: https://github.com/xmrig/xmrig/issues/2847
author: anon-user-com
assignees: []
labels: []
created_at: '2021-12-30T11:20:23+00:00'
updated_at: '2021-12-30T16:43:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have start mining monero and I want to use my RTX 2070 but isn't now showing on my taskbar only cpu usage not gpu.

# Discussion History
## Spudz76 | 2021-12-30T12:43:08+00:00
Need to get [xmrig-cuda plugin](https://github.com/xmrig/xmrig-cuda/releases) and extract to xmrig directory.

Then set config.json cuda->enabled: true and it should detect.

## anon-user-com | 2021-12-30T12:57:06+00:00
xmrig.exe --cuda -o pool.minexmr.com:4444 -u Wallet Address -p Rig
Name (but it’s not working I have seen on a YouTube channel)

I have use this command line also I have add cuda plugin files. Do i need
to disable cpu mine?

On Thu, 30 Dec 2021 at 13:43, Tony Butler ***@***.***> wrote:

> Need to get xmrig-cuda plugin
> <https://github.com/xmrig/xmrig-cuda/releases> and extract to xmrig
> directory.
>
> Then set config.json cuda->enabled: true and it should detect.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2847#issuecomment-1003013177>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/APKOHRPSGFVFMVQCSOHNDQLUTRHWNANCNFSM5K7RQQIQ>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


## Spudz76 | 2021-12-30T13:01:30+00:00
Really need to see startup output to tell what's going on, description is vague.

## anon-user-com | 2021-12-30T13:07:07+00:00
> Really need to see startup output to tell what's going on, description is vague.

In output cmd it detect everything and everything is okay but in task manager it show only cpu usage. Maybe I need to use "xmrig.exe --no-cpu --cuda" on command line. 

## Spudz76 | 2021-12-30T13:13:58+00:00
If it failed to detect you might have to edit config.json like I said, to enable it.

Sometimes command line arguments are ignored if already present in config.json.

## anon-user-com | 2021-12-30T13:15:28+00:00
Okay I will use config.json instead. Can I keep cpu and gpu true or I have to make cpu false. 

## Spudz76 | 2021-12-30T13:33:29+00:00
It is possible to run both in one and if you are processing just one algo then it's fine.

But for actual profits you probably rather set up two xmrigs where one is cpu (no gpu) and one is gpu (no cpu).  And MoneroOcean allows processing other coins for XMR pay.

## Spudz76 | 2021-12-30T13:34:21+00:00
Unless it's Kawpow or something that has no CPU support at all.  Or one of the algos with no GPU support.

## anon-user-com | 2021-12-30T16:43:29+00:00
I will try it and I will tell results 

# Action History
- Created by: anon-user-com | 2021-12-30T11:20:23+00:00
