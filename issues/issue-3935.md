---
title: Default extensive logging
source_url: https://github.com/monero-project/monero/issues/3935
author: keffnet
assignees: []
labels: []
created_at: '2018-06-05T18:08:02+00:00'
updated_at: '2018-06-06T10:58:27+00:00'
type: issue
status: closed
closed_at: '2018-06-06T10:58:27+00:00'
---

# Original Description
Hi

I recently saw that the monero cli (maybe gui also..didnt look) by default logs most that is outputed to the console
to monero-wallet-cli.log. Things like balance, transactions etc. To me this is not appropriate behavior. 
To some this is "if someone can read your files you have bigger problems" and I tend to agree but here are 
some examples why in my opinion this should not be done.

- You don't log by default ever and especially not without informing the user that you are. There is no reason what so ever
  to log all this information by _default_. Really..give me a reason :D For debugging purposes you could activate it on demand.

This should be reason enough but lets give some examples. 


- Let's say I have a wallet on my laptop. The wallet is encrypted by standard passphrase. I pass through JFK and the TSA wants to check my 
laptop

	Scenario #1 - My laptops filesystem is unencrypted so they will get a log file showing all my transactions, balance etc.
	Scenario #2 - My laptops filesystem is encrypted but they are able to dump the key from memory. Now they see all my transactions, balance etc

	Even if the log file has been deleted if not free space was wiped.

- With recent Ledger implementation etc there might be a scenario where someone would take his hw-wallet and use a public/semi-public computer
  to check his Monero wallet. This of course is not recommended but it is nice that the computer would by default write alot of his wallet info
  to disk.

---



# Discussion History
## moneromooo-monero | 2018-06-05T19:29:02+00:00
The reason is that bugs are often hard to repro, and even when there's a log it can be hard to get it from people.
Anyway, it does say it's logging and where.


## keffnet | 2018-06-06T06:11:04+00:00
True. It does say that it is logging. But to most people that would mean leaving sensitive information out. If some problems are hard to reproduce then maybe they weren't serious bugs :D But even with your reasoning I fail to see why things like balance and transaction info need to be logged in order to catch bugs. To me this is like your browser by default logging everything inside an SSL connection just to catch any TLS errors. You can't be harsh with privacy/security in one area and then ignore it in the most basic parts.

Anyway. Software that do log by default hide sensitive information and then choose to have an extra flag like "--debug-notsafe" to also write the sensitive information. If you still want to continue to log by default I suggest you resort to something like this. 

But in my opinion all logging should be disabled by default and maybe invoked with "--debug" for non-sensitive and "--debug-notsafe" to include that also. Or you can even have a separete debug binary.

But it is of course up to you guys :) I just can't wrap my head around all the other efforts you've done in regard to privacy and security and then epic failing on the most basic :)

Rant over ;) Was just shocked to see what unnecessary info was logged and I'm glad I caught it.


Is the cli version suppose to be a more dev/debug-version? Since it doesn't log the same as the gui I mean.


## moneromooo-monero | 2018-06-06T09:01:23+00:00
In fact, I'm changing my mind now, given we already have to ask people to switch to level 2 logs for most bugs anyway. I'll default to no logs.

## moneromooo-monero | 2018-06-06T09:03:06+00:00
BTW, if your threat model includes "thugs can make me give the password to my hard drive" but not "thugs can make me give the password to my monero wallet", then it might need reviewing a bit :)

## moneromooo-monero | 2018-06-06T09:16:36+00:00
https://github.com/monero-project/monero/pull/3939

## keffnet | 2018-06-06T10:58:27+00:00
No I mean coldboot attacks where the computer has been suspended or locked and they reset it without the RAM getting wiped and boot from a livecd and dump the memory or similar. This wouldn't affect the monero wallet since it might never have been open but filesystem keys often remain in RAM. But this was just paranoid examples. The main point was that imho the logging of sensitive info was unnecessary :)

I hope no one thinks what you said :D 

Anyway thanks for reconsidering :)

Next is to complain that the word "lessened" (Warning: using an untrusted daemon at %s, privacy will be lessened) is used instead of "reduced" :D



# Action History
- Created by: keffnet | 2018-06-05T18:08:02+00:00
- Closed at: 2018-06-06T10:58:27+00:00
