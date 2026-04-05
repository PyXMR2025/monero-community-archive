---
title: message came the password was cracked
source_url: https://github.com/xmrig/xmrig/issues/1738
author: theshadowpeople
assignees: []
labels: []
created_at: '2020-06-21T21:57:04+00:00'
updated_at: '2020-08-19T01:12:00+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:12:00+00:00'
---

# Original Description
Hello,
i use xmrig v6.2.0-beta and got the message that my password was cracked.

There was a transaction and my account is empty.

I use my own Linux-Pool-Server and some CPU with XMRIG. My Windows 10 with XMRIG close the programm and give me the massage .......

# Discussion History
## snipeTR | 2020-06-22T14:43:43+00:00
your own fault.
mnemonics seed, private key / spend key, you couldn't protect your information. Did you write your private key in miner or your own pool?
you couldn't protect your wallet.
please read. https://www.crypto-news-flash.com/monero-wallet-test-guide-review/

## theshadowpeople | 2020-06-22T20:17:30+00:00
I also think it was my mistake.
The private key was not saved anywhere.
It was not an external attack but an internal one.
On this client was only xmrig and no password.
On this client I had a small window saying that the key was cracked. unfortunately i closed it because i didn't think there was an attack.
Is it possible that the password was hacked if i didn't use encryption internally like SSL/TLS?

## snipeTR | 2020-06-23T07:51:09+00:00
Coins cannot be stolen without private key? if you are using local wallet. the situation is more complicated if you are using online wallet. There is no way to steal your coins related to xmrig. it may be related to the pool you have set up. Did you write your private key to pool? Is your private key registered in any file on pc?

# Action History
- Created by: theshadowpeople | 2020-06-21T21:57:04+00:00
- Closed at: 2020-08-19T01:12:00+00:00
