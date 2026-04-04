---
title: Trojan JS:ScriptIP-Inf [Trj] found on "moneropools.com" by Avast
source_url: https://github.com/monero-project/monero-site/issues/495
author: ThibaultJanBeyer
assignees: []
labels: []
created_at: '2017-12-05T20:57:21+00:00'
updated_at: '2017-12-07T08:22:16+00:00'
type: issue
status: closed
closed_at: '2017-12-07T08:22:16+00:00'
---

# Original Description
So I don’t know what it is but when clicking on the link in:
`Pools A listing of trusted Monero pools is found here.`
on https://getmonero.org/get-started/mining/ page.

Avast claims to block an infection which is: `JS:ScriptIP-Inf [Trj]`

A quick search gave me ([source](https://www.im-infected.com/trojan/jsscriptip-inf-trj.html)):
```
JS:ScriptIP-Inf [Trj] is a dangerous computer infection that comes in a Java Script file. It can do many bad things to a computer once it gains an access.
```
That does not seem very trustworthy. I could not find the corresponding github page to look into that sites code. So maybe someone could check it out or we could find another site listing pools that does not contain the trojan…


# Discussion History
## noameppel | 2017-12-06T07:07:18+00:00
Hi @ThibaultJanBeyer, 

Can you try another web browser and see if you get the same Avast warning?

Sucuri Website Scanner, GravityScan.com and OpenDNS did not detect any issues with moneropools.com.

## ThibaultJanBeyer | 2017-12-06T09:45:45+00:00
Same result
I tried in Chrome `Version 62.0.3202.94 (Official Build) (64-bit)`.
I tried in Firefox `Version 57.0`
on `Mac OS 10.13.1`.
With Avast `Version 13.2`

Do you know where it comes from? Maybe it’s some kind of weird tracker implemented…

## mattcode55 | 2017-12-06T15:20:14+00:00
Some desktop anti-virus packages/firewalls are starting to block Monero pools.

There's nothing wrong with moneropools.com, it just makes requests to pool servers to gather statistics.

Please could you try http://preview.moneropools.com/ and tell me if that gets blocked by Avast too? All of the data is gathered centrally instead of being polled from all of the pools to reduce load (and hopefully get around the annoying firewalls).

## mattcode55 | 2017-12-06T15:21:29+00:00
+invalid
+wontfix

## ThibaultJanBeyer | 2017-12-06T19:53:03+00:00
yes, I can reach http://preview.moneropools.com/ .
Yes, it’s a better approach like that anyways.
Please use that link instead of the other one. Seeing antivirus/firewall issues might scare people away from this great coin!

## mattcode55 | 2017-12-06T22:01:10+00:00
>Please use that link instead of the other one.

No need to update the link, moneropools.com will be updated with the new site "Soon™" 👍 

## ThibaultJanBeyer | 2017-12-07T08:22:16+00:00
Ok then let’s close this

# Action History
- Created by: ThibaultJanBeyer | 2017-12-05T20:57:21+00:00
- Closed at: 2017-12-07T08:22:16+00:00
