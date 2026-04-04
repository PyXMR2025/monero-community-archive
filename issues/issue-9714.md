---
title: Monerod.exe did start the synchronization, en then only fails to get data.
source_url: https://github.com/monero-project/monero/issues/9714
author: LateAtNight25
assignees: []
labels:
- question
created_at: '2025-01-16T21:32:46+00:00'
updated_at: '2025-02-19T18:09:45+00:00'
type: issue
status: closed
closed_at: '2025-02-19T18:09:44+00:00'
---

# Original Description
Monerod.exe did start the synchronization, en then only fails to get data.
This is what I get:

2025-01-16 20:56:36.949 I SYNCHRONIZATION started
2025-01-16 20:56:37.889 E Error adding block with hash: <5321b0d7537456fde7d6e1208a66bb67ee16a53d6accd33f20256ddcafd59213> to blockchain, what = Attempting to add transaction that's already in the db (tx id 2690000)
2025-01-16 20:56:39.556 E Failed to get tx meta from txpool
2025-01-16 20:56:39.557 E Failed to get tx meta from txpool
2025-01-16 20:56:39.557 E Failed to get tx meta from txpool.....
and ends with 
2025-01-16 21:12:47.065 E Error adding block with hash: <5321b0d7537456fde7d6e1208a66bb67ee16a53d6accd33f20256ddcafd59213> to blockchain, what = Attempting to add transaction that's already in the db (tx id 2690000)
2025-01-16 21:12:47.066 I Host 54.36.174.4 blocked.
2025-01-16 21:12:50.427 E Error retrieving blocks, missed 16 transactions for block with hash: <db265a65666621f29c201453ca6cd33f57240e251a6db89002c4dd6ad7c6d330>

Finding a solution for this problem on the internet is horrific. Like moving through a swamp of unrelevant information with very, very slow progress. Especially after many years reinstalling and restarting  a fresh monero GUI, version  0.18.3.4-unknown (Qt 5.15.14). But this seems the only place where there is hope..
I also don't know why there is "unkown" in the description. When does that happen?

Monero GUI is installed in C:\programs. The Blockchain data in E:\BlockM


# Discussion History
## selsta | 2025-01-17T04:55:02+00:00
Did you have a power outage during sync? It seems the blockchain is corrupted.

## LateAtNight25 | 2025-01-17T09:24:47+00:00
Thanks for reacting. I don't exactly know how it happened, but after an
hour or two, it started synchronizing. Maybe because I disabled the VPN

Op vr 17 jan. 2025 05:55 schreef selsta ***@***.***>:

> Did you have a power outage during sync? It seems the blockchain is
> corrupted.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/9714#issuecomment-2597433647>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BONT7CFWVBGJYLTGREO4Y5D2LCELZAVCNFSM6AAAAABVKR3Z5CVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDKOJXGQZTGNRUG4>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


## LateAtNight25 | 2025-01-17T09:28:29+00:00
But it is nice to know that there are still people who cares about  Monero
and the user.

Op vr 17 jan. 2025 10:24 schreef John Schubert ***@***.***>:

> Thanks for reacting. I don't exactly know how it happened, but after an
> hour or two, it started synchronizing. Maybe because I disabled the VPN
>
> Op vr 17 jan. 2025 05:55 schreef selsta ***@***.***>:
>
>> Did you have a power outage during sync? It seems the blockchain is
>> corrupted.
>>
>> —
>> Reply to this email directly, view it on GitHub
>> <https://github.com/monero-project/monero/issues/9714#issuecomment-2597433647>,
>> or unsubscribe
>> <https://github.com/notifications/unsubscribe-auth/BONT7CFWVBGJYLTGREO4Y5D2LCELZAVCNFSM6AAAAABVKR3Z5CVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDKOJXGQZTGNRUG4>
>> .
>> You are receiving this because you were mentioned.Message ID:
>> ***@***.***>
>>
>


## selsta | 2025-02-19T18:09:44+00:00
Closing as it seems the issue is resolved. If not, please re-sync your blockchain from scratch.

# Action History
- Created by: LateAtNight25 | 2025-01-16T21:32:46+00:00
- Closed at: 2025-02-19T18:09:44+00:00
