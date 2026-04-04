---
title: Addresses on Receive page should indicate futher characters beyond edge
source_url: https://github.com/monero-project/monero-gui/issues/564
author: ghost
assignees: []
labels:
- resolved
created_at: '2017-03-18T18:53:37+00:00'
updated_at: '2018-11-18T18:18:32+00:00'
type: issue
status: closed
closed_at: '2018-11-18T18:18:32+00:00'
---

# Original Description
Right now there's no indication that there are additional characters beyond the edge of the wallet on the Receive page. For example, somebody new to Monero would copy the string with their mouse only to the last characters, and then try to paste it but it wouldn't be the full 95-character address.

![screen-shot-2017-03-18-at-2 48 30-pm](https://cloud.githubusercontent.com/assets/21302237/24075036/9c10fe84-0bea-11e7-945e-23ed8023e4f4.png)

Ideally the address should end in ... or some other indication that the address continues off the page edge.

# Discussion History
## ghost | 2017-03-19T07:21:15+00:00
Thinking more about this, it's probably an option to explore to display the entire 95-character address by having it span multiple lines, eg a bigger address box.

This is helpful because people new to Monero will immediately realize what an address is, versus what we have right now where somebody will see their entire address only after they've pasted it somewhere. In summary, this option would reduce the learning curve a little.

## ghost | 2017-03-19T19:04:51+00:00
This problem also exists in the "Address" field on the Send page. There should be some sort of indication (probably "...") that the address continues beyond the edge.

## ghost | 2017-03-19T20:27:13+00:00
It would be ideal if we could get this also in the transaction confirmation box:

![screen-shot-2017-03-19-at-4 25 29-pm](https://cloud.githubusercontent.com/assets/21302237/24084446/e4d11b5a-0cc0-11e7-85cf-c62bb1c2ccbe.png)

## erciccione | 2018-11-18T13:14:29+00:00
+resolved

# Action History
- Created by: ghost | 2017-03-18T18:53:37+00:00
- Closed at: 2018-11-18T18:18:32+00:00
