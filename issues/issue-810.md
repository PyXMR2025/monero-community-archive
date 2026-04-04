---
title: remove sign/verify feature from monero-core Desktop version
source_url: https://github.com/monero-project/monero-gui/issues/810
author: medusadigital
assignees: []
labels:
- resolved
created_at: '2017-08-08T00:32:30+00:00'
updated_at: '2018-12-17T12:18:31+00:00'
type: issue
status: closed
closed_at: '2018-12-17T12:18:31+00:00'
---

# Original Description
since this is also missing on the mobile version, it would just be consequent.

also i do not think that feature is in use, besides being cool.

it may additionally help free up some space.

other opinions very welcome. 

related too (something we wouldnt need to do) : https://github.com/monero-project/monero-core/issues/174



# Discussion History
## danrmiller | 2017-08-09T02:04:46+00:00
NACK. I don't know how to argue for its importance or back it up, other than my opinion and that I like it.

## Ashaman- | 2018-03-30T12:46:54+00:00
This is a terrible idea. Just one use case that it breaks: Monero pools generally don't have an account you sign up for - your account is your XMR address. If you were to ever need to contact your pool for any kind of technical support, literally the only way you can prove who you are to the pool operator is with a signed message. And the reduction in size of the application that might come from removal of this features would be absolutely negligible because the libraries it uses is cannot be removed since they are the same ones used for constructing and verifying transactions.

## mmbyday | 2018-12-17T09:08:48+00:00
+resolved

## dEBRUYNE-1 | 2018-12-17T11:51:52+00:00
As far as I know, the rough consensus is to keep this feature in advanced mode. I, therefore, am going to close this issue. 


## dEBRUYNE-1 | 2018-12-17T11:51:56+00:00
+resolved

# Action History
- Created by: medusadigital | 2017-08-08T00:32:30+00:00
- Closed at: 2018-12-17T12:18:31+00:00
