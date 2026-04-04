---
title: Can't send transaction with multiple integrated addresses
source_url: https://github.com/monero-project/monero/issues/1505
author: gituser
assignees: []
labels:
- enhancement
- invalid
created_at: '2016-12-26T11:21:25+00:00'
updated_at: '2019-03-21T14:09:35+00:00'
type: issue
status: closed
closed_at: '2019-03-21T14:09:35+00:00'
---

# Original Description
Hi.

I've got a problem when sending out transaction to multiple destinations which include >1 integrated addresses (even if I use the same address twice):
``` 
array (
    'code' => -5,
    'message' => 'A single payment id is allowed per transaction',
  ),```

is there a workaround for this or this is not allowed at all?

# Discussion History
## moneromooo-monero | 2016-12-26T11:45:54+00:00
There are several ways to do this, and it's not clear what's best.
The core could automatically make multiple transactions.
The core could allow duplicate payment ids and merge, but then the recipient would be seeing just one single transfer of the whole amount.


## gituser | 2016-12-26T11:48:44+00:00
I'm not sure what's the best way, but my main idea is to reduce locked balance by sending multiple transactions in 1 transaction.

I think it's ok if recipient sees single transaction instead of multiple ones. I think it's already like that for regular addresses.

You didn't answer though to my main question. Is it possible to send a transaction to multiple integrated addresses or is there an option to make this work?

Thanks.

## moneromooo-monero | 2016-12-26T12:03:33+00:00
It is possible (if the payment ids are the same). The tool does not allow you. There is no option for this.

## gituser | 2016-12-26T12:13:42+00:00
OK, so to sum things up:
* you can't send in one transaction to multiple different integrated addresses
* you can send in one transaction to 1 integrated address and multiple regular
* you can't send in one transaction to the same integrated address (at the moment) if you pass the same integrated address to destinations array more than 1 time

So, the best approach for sending XMR to integrated addresses is to send XMR in a separate transaction to each address.

## gituser | 2017-01-09T08:44:19+00:00
@moneromooo-monero can you confirm what I wrote in previous post?

thanks.

## moneromooo-monero | 2017-01-09T19:00:55+00:00
I'm not sure whether the second one works if the multiple regular have one payment id. It's all down to wallet behvior, but there's no spec for this. Not sure about 3 either, as I think the wallet is supposed to merge destinations, but then there are people who think this is wrong in the first place, as it prevents splitting coins in more than two bits when sending to yourself, which is a valid and useful use case.


## dEBRUYNE-1 | 2018-01-08T12:44:58+00:00
+enhancement

## zeshanvirk | 2018-05-15T05:52:50+00:00
I'm trying to send one transaction to one integrated Address but getting the error

 "code": -5,
        "message": "A single payment id is allowed per transaction"

whats is the solution?

## moneromooo-monero | 2018-05-29T15:24:47+00:00
Give the entire command you're sending.

## moneromooo-monero | 2018-09-04T23:16:29+00:00
ping, give the entire JSON query you're sending to get that error.

## moneromooo-monero | 2018-10-26T11:01:55+00:00
Works for me at the moment with:

curl -k -X POST http://127.0.0.1:28081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"transfer_split","params":{"destinations":[{"address":"A3R9yd7we7uX9pj9WSAMLvA7z5CFDCX7Na2gr82eotVEa8dEWJKPduMcvBLs22tPpGDFLp2kqenBXeyH26TQoKtq7h7fMaCSfErNnEAFjj","amount":1000000000000}],"fee":50000000000,"mixin":10,"unlock_time":0, "trusted_daemon":true,"do_not_relay":false}}' -H 'Content-Type: application/json'

So I'll call that user error unless more information is given. Or maybe there was a bug which got fixed, but I think pool would have screamed as people typically use this to send to exchanges.


## moneromooo-monero | 2019-03-21T14:05:46+00:00
Worked for me, no replies in a long time. Reopen with more info if it still does not work with current master.

+invalid

# Action History
- Created by: gituser | 2016-12-26T11:21:25+00:00
- Closed at: 2019-03-21T14:09:35+00:00
