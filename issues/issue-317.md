---
title: HTTPS API ?
source_url: https://github.com/xmrig/xmrig/issues/317
author: MetallianFR68
assignees: []
labels:
- wontfix
created_at: '2018-01-04T17:18:16+00:00'
updated_at: '2018-11-05T07:08:02+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:08:02+00:00'
---

# Original Description
Simple question : 

I'm mining MONERO on every computer of the company I own
Some are mining using XMRIG
Some are mining using javascript miner

I want the javascript miner to turn off if XMRIG is running on the computer.
The easiest way to detect if XMRIG is running from javascript is to check if the API is running on http://localhost

The problem is my website is HTTPS
So he refuses to check the API on insecure HTTP

_The page at 'https://optimus.adaris.org/tools/minage/index.php' was loaded over HTTPS, but requested an insecure XMLHttpRequest endpoint 'http://localhost:4446/_

Is there a way to run the API on HTTPS ?


# Discussion History
## snipeTR | 2018-01-04T17:20:58+00:00
Use xmrigCC

## xmrig | 2018-01-04T18:23:20+00:00
It complicated, libmicrohttpd must be build with libgnutls support, if it be solved, next trouble will appear, still need valid/trusted certificate for localhost.
Thank you.

## MetallianFR68 | 2018-01-05T17:43:10+00:00
You can't get a certificate for localhost. Only qualified domain can. However in Chrome you can set : chrome://flags/#allow-insecure-localhost. Activating HTTPS on the api would then solve the problem.

# Action History
- Created by: MetallianFR68 | 2018-01-04T17:18:16+00:00
- Closed at: 2018-11-05T07:08:02+00:00
