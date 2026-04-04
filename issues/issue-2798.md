---
title: '[Fiat API] Error: "Problem with reply from server. Check connectivity." -
  fiatPriceError: Invalid ticker value: 0'
source_url: https://github.com/monero-project/monero-gui/issues/2798
author: jonathancross
assignees: []
labels:
- bug
created_at: '2020-03-06T14:19:04+00:00'
updated_at: '2020-04-23T22:46:01+00:00'
type: issue
status: closed
closed_at: '2020-04-22T20:46:54+00:00'
---

# Original Description
Release: `v0.15.0.4`

When connecting to a remote node on MacOS 10.14.6, I am unable to retrieve any fiat exchange rates:
```
2020-03-06 14:09:17.899	D fiatPriceError: Invalid ticker value: 0
2020-03-06 14:09:17.899	D undefined
2020-03-06 14:09:24.286	D "Fetching: https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd"
2020-03-06 14:09:24.287	E [Fiat API] Error: "Problem with reply from server. Check connectivity."
```

I have tried:
* with different circuits
* with USD and EUR
* 3 of the available providers in the GUI

None succeeded.

**Update:** This error is not Tor specific.

# Discussion History
## tficharmers | 2020-03-07T10:34:13+00:00
Yes. 0.15.0.1 successfully shows a fiat price conversion for me. 0.15.0.4 just has question marks (?.??) for both EUR and USD conversions. Also, this isn't through Tor.

MacOS Catalina 10.15.3

<img width="287" alt="Screenshot 2020-03-07 at 10 32 28" src="https://user-images.githubusercontent.com/23356013/76141741-16dd8f80-605f-11ea-96e3-68efaebe65e8.png">


## jonathancross | 2020-03-07T13:35:39+00:00
Confirmed on MacOS 10.14.6 _without_ Tor -- still no fiat.

## selsta | 2020-03-07T13:43:13+00:00
Will be fixed with v0.15.0.5

## selsta | 2020-03-07T14:03:11+00:00
Can also reproduce on Linux. Works on Windows.

## selsta | 2020-04-22T20:46:54+00:00
Fixed in source code, will be included with next release.

## jonathancross | 2020-04-23T22:39:57+00:00
@selsta Can you please link to the commit fixing this? Thanks.

## xiphon | 2020-04-23T22:42:03+00:00
@jonathancross 
https://github.com/monero-project/monero-gui/commit/55b548f31cc87d36193a578b00d5a55e35e421f1

# Action History
- Created by: jonathancross | 2020-03-06T14:19:04+00:00
- Closed at: 2020-04-22T20:46:54+00:00
