---
title: Am I misunderstanding daemon sync messages - after v7 seems to have changed.
source_url: https://github.com/monero-project/monero/issues/3575
author: Admiral-Noisy-Bottom
assignees: []
labels:
- invalid
created_at: '2018-04-07T03:06:17+00:00'
updated_at: '2018-04-10T00:06:32+00:00'
type: issue
status: closed
closed_at: '2018-04-07T08:00:44+00:00'
---

# Original Description
Prior the v7 fork I didn't seem to see messages about being x blocks behind. But since the fork I'm seeing it a lot, but I think I'm misreading what it's telling me.

SYNCHRONIZATION started
2018-04-07 02:20:38.321	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[66.27.158.224:50172 INC] Sync data returned a new top block candidate: 1546063 -> 1546392 [Your node is 329 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-04-07 02:26:58.024	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[66.27.158.224:50292 INC] Sync data returned a new top block candidate: 1546063 -> 1546392 [Your node is 329 blocks (0 days) behind] 
SYNCHRONIZATION started
status
Height: 1546067/1546067 (100.0%) on mainnet, not mining, net hash 1.15 GH/s, v7, up to date, 16(out)+7(in) connections, uptime 0d 2h 7m 40s

In the above I was reading this to mean I was behind the network, yet the status tells me I'm 100% up to date.

Are these messages really telling me that another node connected to me is behind rather than me?

I've spent hours tweaking network settings, in_peers, out_peers, limit_up, limit_down etc and nothing has changed. 

I check other pools to see what height they are at and it's the same as me. Can anyone clarify?

# Discussion History
## moneromooo-monero | 2018-04-07T07:58:48+00:00
It's the ASICs that stayed on v6 because they can't do v7, you can ignore them.

+invalid

## Psyral | 2018-04-08T15:24:13+00:00
@Admiral-Noisy-Bottom Not related to issue but we could use your expertise on a crypto issue. Please check you twitter or stop by https://discord.gg/N2s2VD . Need help with a Windows GUI wallet you created. Thanks.

## Admiral-Noisy-Bottom | 2018-04-10T00:06:32+00:00
@Psyral Can you send me another invite into discord, the other one has expired and I'm locked out.

# Action History
- Created by: Admiral-Noisy-Bottom | 2018-04-07T03:06:17+00:00
- Closed at: 2018-04-07T08:00:44+00:00
