---
title: I tried to transfer to an exchange
source_url: https://github.com/monero-project/monero/issues/908
author: Elmit2015
assignees: []
labels: []
created_at: '2016-07-12T23:52:09+00:00'
updated_at: '2016-07-13T00:04:27+00:00'
type: issue
status: closed
closed_at: '2016-07-13T00:04:27+00:00'
---

# Original Description
It is my first try. About 2 hours ago I initialized the command:

`transfer 0 463tWEBn5XZJSxLU6uLQnQ2iY9xuNcDbjLSjkn3XAXHCbLrTTErJrBWYgHJQyrCwkNgYvyV3z8zctJLPCZy24jvb3NiTcTJ 55.4 a4d724b542d841c1b494509741c0cbb2261160076f02475ea12da9f8109addd5`

No error message, ...

I got from the Exchange the Address and the Payment_ID
Poloniex suggested to use transfer 0

After 2 hours, the balance command shows still my entire 55.4 XMR.

Do I do something wrong?


# Discussion History
## Elmit2015 | 2016-07-13T00:04:21+00:00
I figured it out with the help of the wallet log: mixin must be 3, that increases the fee, ... but solved now.


# Action History
- Created by: Elmit2015 | 2016-07-12T23:52:09+00:00
- Closed at: 2016-07-13T00:04:27+00:00
