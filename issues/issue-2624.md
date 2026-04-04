---
title: Scan of wallet export qr code using an iPhone camera app dials the phone number
  147000 automatically.
source_url: https://github.com/monero-project/monero-gui/issues/2624
author: satoshi-n
assignees: []
labels: []
created_at: '2019-12-17T07:29:25+00:00'
updated_at: '2022-03-16T19:48:41+00:00'
type: issue
status: closed
closed_at: '2022-03-16T19:48:41+00:00'
---

# Original Description
Might get someone in trouble one day. Seems like a very odd issue I know but who knows what it will resolve fixing this. My battery is low I’ll add a demo in an update. 


Also why do we need so many external links in pdf user guides? Damn I need to contribute 

# Discussion History
## selsta | 2021-07-02T01:15:42+00:00
Can't reproduce with the latest version of iOS.

## rating89us | 2021-07-02T14:43:49+00:00
I can reproduce this bug. Go to Seed & Keys page, select "View-only wallet" and scan QR code with the Iphone. It will try to call a telephone number that represents restore height: `&height=1810000` iPhone recognizes as a call to 1 (810) 000

## rating89us | 2021-07-02T14:45:41+00:00
I'm not sure if it is a bug, since my Iphone doesn't have any app that recognizes `monero_wallet:` URI

## selsta | 2022-03-16T19:48:41+00:00
I think there isn't much we can do here. iOS parsing the URI and deciding that a number in the strings means it's a phone number.

# Action History
- Created by: satoshi-n | 2019-12-17T07:29:25+00:00
- Closed at: 2022-03-16T19:48:41+00:00
