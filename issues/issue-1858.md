---
title: 'Terminology Clarification: Stealth Address'
source_url: https://github.com/monero-project/monero/issues/1858
author: ajs-xmr
assignees: []
labels: []
created_at: '2017-03-09T22:52:10+00:00'
updated_at: '2017-03-16T19:11:34+00:00'
type: issue
status: closed
closed_at: '2017-03-16T19:11:34+00:00'
---

# Original Description
There are 4 views of what a "stealth address" means:

1. wallet address = stealth address (_because wallet addresses do not appear in the blockchain_)

2. output = one-time public key = one-time output key = output public key = stealth address (_because addresses that appears in the blockchain are not “real” addresses, but are destinations where the funds go to_)

3. “stealth address” describes the overall process of unlinkability

4. Abandon the term 

Support for view 1: http://monero.stackexchange.com/questions/2926/terminology-clarification-stealth-address

Support for view 2: https://steemit.com/monero/@luigi1111/understanding-monero-cryptography-privacy-part-2-stealth-addresses

Support for view 3: https://getmonero.org/knowledge-base/moneropedia/stealthaddress

Contributors, what is your view on this?

EDIT:
added "output public key" meaning output as well in 2 and added 4th option

# Discussion History
## kenshi84 | 2017-03-09T23:02:26+00:00
3

(or 4: abandon the term entirely to avoid confusion)

## moneroexamples | 2017-03-09T23:11:28+00:00
Stleath address is tx  public key, anwser no 2.

Please have a look at fluffyponyza clarification of this issue, with examples of stealth addresses:

- https://www.reddit.com/r/Monero/comments/4wupab/why_doesnt_my_monero_address_change_after_every/d6a99dl/?context=3

Edit. It should be "output  public key"

# Action History
- Created by: ajs-xmr | 2017-03-09T22:52:10+00:00
- Closed at: 2017-03-16T19:11:34+00:00
