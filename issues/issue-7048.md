---
title: Stagenet wallet from scratch only syncs up to block 570429.
source_url: https://github.com/monero-project/monero/issues/7048
author: normoes
assignees: []
labels: []
created_at: '2020-11-30T17:41:03+00:00'
updated_at: '2021-01-09T23:22:22+00:00'
type: issue
status: closed
closed_at: '2021-01-09T23:22:22+00:00'
---

# Original Description
I am talking about `monero-wallet-rpc`, version `v0.17.1.5`.

I had troubles with the wallet and deleted the entire file, since this used to help.

It started to work, taking its time, but then it stopped and died with:
```
2020-11-30 16:01:44.048 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2020-11-30 16:01:44.053 E pull_blocks failed, try_count=3
2020-11-30 16:01:44.053 E Wallet initialization failed: no connection to daemon
```

I tried a few more times and noticed, that it only synchronized the wallet up to (and including) block number `570429`. This block contains one of my transactions.

---

The wallet file, once completely synchronized (using a backup file), is `213 MB` in total.

# Discussion History
## moneromooo-monero | 2020-12-05T14:41:53+00:00
Can you share the seed ? You can encrypt it with my key (in utils).

## normoes | 2020-12-05T17:32:28+00:00
I will.

By the way @moneromooo-monero , not sure if you are aware of this, your key will expire in a few days:
```
pub   rsa4096 2014-10-06 [SC] [expires: 2020-12-10]
      48B08161FBDADFE393ADFC3E686F07454D6CEFC3
uid           [ unknown] moneromooo-monero <moneromooo-monero@users.noreply.github.com>
sub   rsa4096 2014-10-06 [E] [expires: 2020-12-10]
```

## normoes | 2020-12-05T17:46:13+00:00
Here you can find the seed: https://paste.debian.net/1175750/

A lot is happening in that wallet for around two years.

## moneromooo-monero | 2020-12-05T18:10:53+00:00
Oh, thanks. I always forget :)

## moneromooo-monero | 2020-12-07T01:01:39+00:00
It gets past that for me. Try master :)

## normoes | 2020-12-07T11:00:16+00:00
Thanks! I can try that. Although, for `stagenet` and `mainnet` I usually don't. Let's see.

## moneromooo-monero | 2021-01-09T01:40:03+00:00
Did you try ?

## normoes | 2021-01-09T14:56:18+00:00
Oh yes, sorry.

It works with `master`.

## moneromooo-monero | 2021-01-09T23:22:22+00:00
Thanks, closing then.

# Action History
- Created by: normoes | 2020-11-30T17:41:03+00:00
- Closed at: 2021-01-09T23:22:22+00:00
