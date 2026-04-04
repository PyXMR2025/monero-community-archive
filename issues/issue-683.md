---
title: option to generate paymentID from any plaintext [enhancement]
source_url: https://github.com/monero-project/monero/issues/683
author: rariro
assignees: []
labels: []
created_at: '2016-02-21T12:13:01+00:00'
updated_at: '2017-08-25T21:26:37+00:00'
type: issue
status: closed
closed_at: '2017-08-25T21:26:37+00:00'
---

# Original Description
An idea to make it more "human". For example, I want a friend to pay me a beer and I tell him to use his name as payment ID. The wallet would then hash his plaintext to actual payment ID used, and I'd be able to credit the payment to him without even knowing the actual payment ID.
Of course, there's the concern of hash collisions, but it'd just be for convenience anyway.


# Discussion History
## moneromooo-monero | 2016-02-24T21:29:55+00:00
You can't hash, as you can't easily find X for which hash(X)=something unless X is within a small already known set of possible inputs.
If you wanted to store "human readable" stuff in the payment id, I'd limit it to 32 characters of free text, and use that as is. But of course if someone has a long name, you get into problems.
For use with simplewallet, you can, eg, echo -n rariro | od -t x1 -An | tr -d \ 
Then fill up with zeroes. I imagine a GUI might even have a way to automate that.


## rariro | 2016-02-25T04:23:13+00:00
Yeah, filling with 0-s would work, with some char to terminate the string, and have wallets display nice, readable strings. But as you say, they'd be cut-off. However, this way the receiver can read the string immediately.
The idea with hashing was somewhat different, as the string would have to be communicated off the chain. Like: Hey, I sent you the payment, check under "rariro", then, I'd know what to look for - hash the string and compare to payment IDs received.
Now that I write it this way, I see how it would not be very user-friendly. Maybe the proposal should instead be be to add what you described to the wallet, just encode to/from string.


# Action History
- Created by: rariro | 2016-02-21T12:13:01+00:00
- Closed at: 2017-08-25T21:26:37+00:00
