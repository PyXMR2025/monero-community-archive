---
title: Add Access-Control-Allow-Origin header to Daemon RPC
source_url: https://github.com/monero-project/monero/issues/2408
author: chescos
assignees: []
labels: []
created_at: '2017-09-07T22:29:43+00:00'
updated_at: '2017-11-04T14:23:24+00:00'
type: issue
status: closed
closed_at: '2017-11-01T09:40:25+00:00'
---

# Original Description
Could the `Access-Control-Allow-Origin` header be added to the daemon RPC? Would be awesome to be able to connect to the daemon through JavaScript from a web browser.

# Discussion History
## danrmiller | 2017-09-08T14:04:54+00:00
Also related #1677 for the wallet.

## vtnerd | 2017-09-11T13:03:07+00:00
As I stated in https://github.com/monero-project/monero/issues/1677 the danger is if the user does not provide a daemon password, the attack on the local daemon becomes easier. JavaScript can issue a post without the user ever interacting with the page. Perhaps requiring a password for the mode, and a strict whitelisting of domains ... ? 

Also, its difficult for me to imagine a good use case _other_ than running loading a HTML document from the local hard drive. What is your use case @chescos ?

## chescos | 2017-09-11T14:03:23+00:00
@vtnerd I am a web developer and I would love to build a completely client-sided Monero explorer that can easily be used by non-technical users. This could be useful to users who run their own node and want to monitor and use it as their own block explorer. I would for example use it to monitor the Monero node that is running on my Rasperry Pi.

Of course I could also write such an application in PHP or NodeJS but that would make the setup more complicated for non-technical users. With pure client side JS, all that would be needed is to download a standalone .html file and open it with a browser. The user could then just enter his node credentials through a form and he's ready to go.

## joijuke | 2017-09-15T13:39:28+00:00
@chescos your idea is very cool ,maybe youcan post the idea to reddit and raise ffs 

## Timo614 | 2017-10-20T19:59:17+00:00
Working on this and #1677 at the moment. Should have something up today or early tomorrow. Just posting here so there's no duplication of effort if anyone else is looking for an issue. I have it set locally so the access control allow origin list is a whitelist passed as an rfc command and requires the rpc-login command or it throws an error.

## moneromooo-monero | 2017-11-01T09:32:49+00:00
+resolved

## chescos | 2017-11-04T14:23:23+00:00
Awesome! Thank you @Timo614 

# Action History
- Created by: chescos | 2017-09-07T22:29:43+00:00
- Closed at: 2017-11-01T09:40:25+00:00
