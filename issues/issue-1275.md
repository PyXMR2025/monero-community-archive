---
title: Mine to daemon
source_url: https://github.com/xmrig/xmrig/issues/1275
author: TheDevMinerTV
assignees: []
labels: []
created_at: '2019-11-11T10:31:18+00:00'
updated_at: '2020-01-05T12:26:28+00:00'
type: issue
status: closed
closed_at: '2020-01-05T12:26:28+00:00'
---

# Original Description
How can I mine to my Turtlecoin daemon?

The option is in the config.json file but it's not being used
![image](https://user-images.githubusercontent.com/29845135/68580495-c53d4380-0476-11ea-80ae-0f194137a34a.png)

(don't tell me, that they forked, I know that...)

# Discussion History
## xmrig | 2019-11-12T13:14:02+00:00
Default JSON RPC port for TurtleCoin **11898** according the docs https://docs.turtlecoin.lol/developer/api/daemon-json-rpc-api and they forked so you should use `argon2/chukwa` algorithm and this algorithm supported only by CPU backend.
Thank you.

## TheDevMinerTV | 2019-11-13T14:37:51+00:00
I know that, the thing is that I don't get any shares or blocks.
I'm working on a fork of Turtlecoin whihch uses `cn-pico/trtl`

## xmrig | 2019-11-13T14:54:26+00:00
What exactly fork?

If miner successfully connected to daemon you should saw lines like:
`...use daemon...`
`...new job...`

or errors like: `[192.168.189.69:32769] connect error: "connection timed out"`.

If nothing above happens, something wrong, unexpected API response, etc.
Thank you.

## TheDevMinerTV | 2019-11-13T14:57:27+00:00
Fork is [Xenium](https://github.com/xenium-project/xenium)

There's no output after the header
![Output of XMRig](https://user-images.githubusercontent.com/29845135/68775019-307d4600-062e-11ea-9343-3fecab0dcb3b.png)

![Config for pools](https://user-images.githubusercontent.com/29845135/68775074-40952580-062e-11ea-93a7-4a3dc4745f87.png)


## Spudz76 | 2019-11-18T20:00:05+00:00
Doesn't seem like port 32769 is speaking JSON-RPC

## TheDevMinerTV | 2019-11-20T11:17:41+00:00
We have forked to port 32779 as JSON-RPC about four days ago, still not working.
![image](https://user-images.githubusercontent.com/29845135/69234596-d3cedd80-0b8f-11ea-935a-a49c6704f5fa.png)


## TheDevMinerTV | 2020-01-05T12:26:28+00:00
I tried this again in version v5.5.0 and it works fine. Closing.

# Action History
- Created by: TheDevMinerTV | 2019-11-11T10:31:18+00:00
- Closed at: 2020-01-05T12:26:28+00:00
