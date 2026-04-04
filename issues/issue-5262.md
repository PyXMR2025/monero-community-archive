---
title: Buss error (core dumped) while upgrading database
source_url: https://github.com/monero-project/monero/issues/5262
author: zahyur
assignees: []
labels: []
created_at: '2019-03-09T14:56:40+00:00'
updated_at: '2022-04-08T16:35:01+00:00'
type: issue
status: closed
closed_at: '2022-04-08T16:35:01+00:00'
---

# Original Description
Fedora 29, 64 bit
Both monerod 0.13.0.4 and 0.14.0.2
Crashes at:
"2019-03-09 14:25:43.095	    7fe64f0a4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:4139	updating txs tables:"
I tried --db-salvage with no difference.

# Discussion History
## cavapoo2 | 2020-03-11T17:18:39+00:00
Also getting this. Ubuntu 1804, managed to download 50% of blockchain yesterday, today it just core dumps. 

2020-03-11 17:17:26.002	I Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
2020-03-11 17:17:26.002	I Moving from main() into the daemonize now.
2020-03-11 17:17:26.003	I Initializing cryptonote protocol...
2020-03-11 17:17:26.003	I Cryptonote protocol initialized OK
2020-03-11 17:17:26.003	T Blockchain::Blockchain
2020-03-11 17:17:26.003	I Initializing core...
2020-03-11 17:17:26.003	T BlockchainLMDB::BlockchainLMDB
2020-03-11 17:17:26.003	T BlockchainLMDB::get_db_name
2020-03-11 17:17:26.003	I Loading blockchain from folder /home/base/.bitmonero/lmdb ...
2020-03-11 17:17:26.003	D option: fast
2020-03-11 17:17:26.003	D option: async
2020-03-11 17:17:26.003	D option: 250000000bytes
2020-03-11 17:17:26.003	T BlockchainLMDB::open
2020-03-11 17:17:26.003	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2020-03-11 17:17:26.004	T BlockchainLMDB::need_resize
2020-03-11 17:17:26.004	D DB map size:     10035043072
2020-03-11 17:17:26.004	D Space used:      8835379200
2020-03-11 17:17:26.004	D Space remaining: 1199663872
2020-03-11 17:17:26.004	D Size threshold:  0
2020-03-11 17:17:26.004	D Percent used: 88.0453  Percent threshold: 90.0000
Bus error (core dumped)


where is coredump located nowadays ?

## selsta | 2020-03-11T17:23:18+00:00
Did you computer crash / shut down improper?

## cavapoo2 | 2020-03-12T19:21:51+00:00
yes. I think it might be doing CTRL C while its resizing the database ?. Anyway yesterday i did CTRL-C while it was syncing, that shut down nicely. Its also quite slow to shutdown, so if your impatient then its easy to kill it while its doing something critical maybe. Some feedback would be nice, periodically say "shutting down in progress ". If its slow to shutdown its easy to assume its crashed when no feedback is given.  

## selsta | 2020-03-12T19:46:39+00:00
It takes like 1 second on my system. How slow is it for you?

## cavapoo2 | 2020-03-13T14:12:07+00:00
I'm thinking in minutes not seconds that's how long. Just a question about node syncing. The first 50% was quite quick 3-4 hrs, but ever since > 50%, its now about its like 5% increase for > 4 hrs. I wonder why it changes so much after the first 50%. Is there any good info about how node syncing works for monero?. 

## selsta | 2020-03-13T14:19:53+00:00
The first 50% was in the early days of Monero, meaning less transaction volume to verify. Also in the beginning there was no RingCT (hidden amounts) which also adds verification times.

Multiple minutes for stopping the daemon does not sound right unless you stop in the middle of a db conversion.

## cavapoo2 | 2020-03-13T14:50:43+00:00
yeah just timed it about 30 seconds for me while its syncing. its longer during db resize , but don't want to try that again since it might end up core dumping again.

## selsta | 2020-03-13T14:51:23+00:00
What hardware are you using?

## cavapoo2 | 2020-03-13T15:25:41+00:00
i7 laptop , 16G ram , (6 years old though) with one of those hybrid disk drives . i think it more like a disk drive than anything close to SSD 

## selsta | 2022-04-08T16:35:01+00:00
No reports about this in a while. Closing.

# Action History
- Created by: zahyur | 2019-03-09T14:56:40+00:00
- Closed at: 2022-04-08T16:35:01+00:00
