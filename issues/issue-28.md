---
title: validation missing if transaction amount = balance
source_url: https://github.com/monero-project/monero-gui/issues/28
author: medusadigital
assignees: []
labels: []
created_at: '2016-09-20T16:36:07+00:00'
updated_at: '2016-10-27T06:18:45+00:00'
type: issue
status: closed
closed_at: '2016-10-27T06:18:45+00:00'
---

# Original Description
if i try to send a transaction with the amount exactly matching my balance, it looks like this: 

![mainnet_send2_testdevdonationfail](https://cloud.githubusercontent.com/assets/17108301/18679636/d17c02f6-7f60-11e6-8e91-bbcbfe151fde.jpg)
- Confirmation message is wrong
- transaction should get rejected with "not enough money" reject message

after i pressed ok, nothing happend.

--> Ubuntu 16.04 on mainnet together with pull request #23


# Discussion History
## Jaqueeee | 2016-10-07T15:19:13+00:00
How about this one? Wasn't able to reproduce. Already solved? @medusadigital


## medusadigital | 2016-10-11T19:24:46+00:00
fixed --> works ---> closed


## medusadigital | 2016-10-27T06:18:44+00:00
all fine 


# Action History
- Created by: medusadigital | 2016-09-20T16:36:07+00:00
- Closed at: 2016-10-27T06:18:45+00:00
