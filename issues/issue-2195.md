---
title: keepalive config ignored
source_url: https://github.com/xmrig/xmrig/issues/2195
author: jtgrassie
assignees: []
labels: []
created_at: '2021-03-19T17:47:03+00:00'
updated_at: '2021-03-20T09:23:53+00:00'
type: issue
status: closed
closed_at: '2021-03-20T09:01:34+00:00'
---

# Original Description
When a pool reports it supports the keepalive extension, the the miner will always send keepalive messages, regardless if the user has specified `keepalive:false` or `keepalive:0` in their miner config.

# Discussion History
## xmrig | 2021-03-20T07:07:27+00:00
This is how it is supposed to be: If pool put `keepalive` to extensions list it means pool supports it and wants this feature to be enabled. It's zero configuration same way as pool override `algo` option.

If a pool didn't put it to the extensions list or don't have this list all works the same way since the beginning of time. This is wrong https://github.com/jtgrassie/monero-pool/pull/74 `keepalive` option work as expected. Likely confused with this https://github.com/xmrig/xmrig/blob/master/src/base/net/stratum/Client.h#L152
Thank you.


## jtgrassie | 2021-03-20T07:12:28+00:00
If the client (xmrig) sets `keepalive:false` in their config, I'd expect the client would *not* send keepalives. The fact a pool does or does not support a feature should not dictate whether a client uses that feature.

> all works the same way since the beginning of time

This is not the case. The behavior changed at some point in the miner (~2019). It _used_ to send keepalives if the client configured it (via `keepalive:true`), then at some point this changed and now the only way keepalives are sent (and are always are sent, regardless of the miner config), is when the pool sends the keepalive support in the login extension.

## xmrig | 2021-03-20T07:40:58+00:00
Behavior of `keepalive:true` not changed just added one extra way to enable it (on pool side).
Thank you.


## jtgrassie | 2021-03-20T07:52:58+00:00
> This is wrong jtgrassie/monero-pool#74 keepalive option work as expected

I'm sorry, but this is not the case. Here is what happens with and without the #2194...

Without #2194:

- If a pool doesn't send the extension=keepalive, no matter what miner config is used, no keepalives will be sent, period. This seems reasonable, although before the extension was added, keepalives would be sent if configured in the miner (commandline flag or config.json).
- If a pool _does_ flag support in the login extension, _there is no way_ for the miner to disable (keepalive:false|0 config/flag is simply ignored). This is the crux of the problem.

With #2194:

- If the pool sends the extension _and_ the miner has keepalive:true|N>0, then keepalives are sent. This seems the intuitively the correct behavior, as the pool is saying whether it supports keepalive, but allows the miner to choose (configure) if they want to send them or not.

> ...all works the same way since the beginning of time

For reference, https://github.com/xmrig/xmrig/commit/be5d609856f1db604f8b3203b10d7c7c9f630a32 changed the behavior in the miner to _require_ the pool to notify the miner it supports keepalive (via the login extension).

## xmrig | 2021-03-20T08:05:23+00:00
Did you check it https://github.com/xmrig/xmrig/blob/master/src/base/net/stratum/Client.h#L152 my quick check shows it works as expected. Maybe I miss some bug that prevent keepalive sent? If `keepalive:true` not work without extension this is bug.

## jtgrassie | 2021-03-20T08:12:34+00:00
> Did you check ... my quick check shows it works as expected. Maybe I miss some bug that prevent keepalive sent? If keepalive:true not work without extension this is bug.

Yes i did check and no keepalive is sent unless the pool sends support via the login extension. That's why moneromoo added the patch to the pool in the first place. It was then after more testing, I discovered the miner cannot disable it (when the pool says it can handle it). Hence the PR here and detail in the [comment](https://github.com/xmrig/xmrig/issues/2195#issuecomment-803268064) above.

## jtgrassie | 2021-03-20T08:20:56+00:00
https://github.com/xmrig/xmrig/blob/master/src/base/net/stratum/Client.h#L152 is the crux of the problem, because if the pool sends support for keepalive extension, the miner cannot switch off sending keepalives (no matter what they configure, keepalives will be sent because the pool says it supports them).

## xmrig | 2021-03-20T08:32:51+00:00
Sorry I can't confirm the bug https://i.imgur.com/W5gS6kn.png don't forget, you must use high diff, every share submit resets keepalive timer.

Purpose of keepalive extension is to override user defined keepalive option, your PR breaks it, so it breaks xmrig-proxy and other pools which rely on this behavior, eg https://hashvault.pro/

## jtgrassie | 2021-03-20T08:40:41+00:00
> Purpose of keepalive extension is to override user defined keepalive option

Well in that case we don't want that extension in the pool. I'll revert the pool PR. 

## xmrig | 2021-03-20T08:44:37+00:00
And please record there was none of breaking changes in ~2019.
Thank you.


## jtgrassie | 2021-03-20T08:57:39+00:00
I never said it was a _breaking_ change in 2019, just that there were changes in behavior - no harm no foul.

And we couldn't see keepalives happening _without_ the login extension being sent from the pool. You've detailed how you intend it to be enforced by the pool, which you have your reasons for, which is my misunderstanding for assuming the miner should be able to enable/disable it (per the config or commandline option). 

And if you're happy with how it currently works, that's fine I can close this issue, the referenced PR, and remomove the extension from the pool.

Thank you.

## xmrig | 2021-03-20T09:07:43+00:00
> And we couldn't see keepalives happening without the login extension being sent from the pool.

But https://i.imgur.com/W5gS6kn.png hint: supportxmr.com doesn't support login extension.

## jtgrassie | 2021-03-20T09:18:13+00:00
Fine, maybe we needed to set a higher diff or something. We both tested and clearly both made the same mistake. The PR for this issue was about the inability of the miner to switch off keepalives if the pool reported via the extension. As I said, if that's how you intend it to work then fine, I've closed the issue and PR. Apologies for implementing in the pool and sending a PR for the miner for what was assumed a bug not a feature.

## xmrig | 2021-03-20T09:23:53+00:00
It's OK, you're welcome.


# Action History
- Created by: jtgrassie | 2021-03-19T17:47:03+00:00
- Closed at: 2021-03-20T09:01:34+00:00
