---
title: 'thread #0 failed with error Unsupported algorithm'
source_url: https://github.com/xmrig/xmrig/issues/3253
author: gitguitar
assignees: []
labels: []
created_at: '2023-04-18T19:19:23+00:00'
updated_at: '2023-04-18T19:36:56+00:00'
type: issue
status: closed
closed_at: '2023-04-18T19:36:55+00:00'
---

# Original Description
Hi all,

i was following a bunch of instructions to get xmrig working with GPU mining for monero. with CPU no problem. By using GPU i get a

`nvidia   thread #0 failed with error Unsupported algorithm`

First, GPU Mining monero with xmrig is possible at all?

next, unpacking xmrig-v6.19.2-mo1-win64 and copying the files from xmrig-cuda-6.17.0 to the xmrig.exe folder seems to let it happen.

also using a json file or giving attributes while starting the exe stars a CMD box successfully with an ass full of information

`xmrig.exe --no-cpu --cuda -o gulf.moneroocean.stream:10128 -u WALLET-ADDRESS -k --coin monero -a rx/0`

but there is no connection to the pool also after a hour or so.

so, is rx/0 unsupported in xmrig?

what am i doiung wrong?

thank a lot in advance

# Discussion History
## SChernykh | 2023-04-18T19:25:06+00:00
GPU mining Monero is supported. What you're doing wrong is not running the official XMRig release. XMRig-mo release, when connecting to MoneroOcean, will most likely give you a different algorithm which is not supported by CUDA plugin.

## gitguitar | 2023-04-18T19:36:55+00:00
thank you @SChernykh , totally missed that one. using the official release is working on the fly.

# Action History
- Created by: gitguitar | 2023-04-18T19:19:23+00:00
- Closed at: 2023-04-18T19:36:55+00:00
