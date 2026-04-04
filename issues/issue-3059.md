---
title: 'RPC: Wrongly formatted RFC 2616/2617 header'
source_url: https://github.com/monero-project/monero/issues/3059
author: CamilleScholtz
assignees: []
labels: []
created_at: '2018-01-03T21:26:43+00:00'
updated_at: '2022-04-08T14:33:30+00:00'
type: issue
status: closed
closed_at: '2022-04-08T14:33:30+00:00'
---

# Original Description
https://www.ietf.org/rfc/rfc2617.txt

The wallet RPC header:

```
[Digest qop="auth",algorithm=MD5,realm="monero-rpc",nonce="1b4e8/tzwgdTEPyeJ2QUDA==",stale=false Digest qop="auth",algorithm=MD5-sess,realm="monero-rpc",nonce="1b4e8/tzwgdTEPyeJ2QUDA==",stale=false]
```

`algorithm` should be `"MD5"` but is `MD5`.

This causes the vast majority of (golang) digest libraries to not work, see https://github.com/One-com/digest/issues/1 for an example.


  
  

# Discussion History
## vtnerd | 2018-01-10T05:58:10+00:00
Eh, the situation is the opposite. The golang libraries have the bug, and this is using the correct syntax. Here is the grammar from the RFC:
```EBNF
       algorithm         = "algorithm" "=" ( "MD5" | "MD5-sess" |
                           token )
```
If quotes were included it would be `"algorithm" "="` instead of `algorithm=`. Or another example from the RFC:
```EBNF
       response         = "response" "=" request-digest
       request-digest = <"> 32LHEX <">
       LHEX             =  "0" | "1" | "2" | "3" |
                           "4" | "5" | "6" | "7" |
                           "8" | "9" | "a" | "b" |
                           "c" | "d" | "e" | "f"
```
If the quotes were included you would have `"response" "=" ""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""a""` as the value.

EDIT: Sorry for those reached via email, botched my counter-examples because they are so awkward.
  

## CamilleScholtz | 2018-01-10T08:18:54+00:00
Upon closer reading you might indeed be right. I can't figure out from the RFC document if (and when) they mean literal quotation marks (as in this pare should be between quotes) and when they are simply quoting parts of code.

## moneromooo-monero | 2018-06-27T08:50:33+00:00
I think vtnerd's interpretation from the RFC text is the most sensible.

## selsta | 2022-04-08T14:33:30+00:00
https://github.com/monero-project/monero/pull/3060#issuecomment-455600952

# Action History
- Created by: CamilleScholtz | 2018-01-03T21:26:43+00:00
- Closed at: 2022-04-08T14:33:30+00:00
