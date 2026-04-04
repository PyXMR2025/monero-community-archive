---
title: 'Feature request: daemon functional in push-only mode'
source_url: https://github.com/monero-project/monero/issues/832
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-05-02T01:26:55+00:00'
updated_at: '2016-10-04T02:36:48+00:00'
type: issue
status: closed
closed_at: '2016-10-04T02:36:48+00:00'
---

# Original Description
Create a daemon setting (load flag or while-running toggle) that shuts off any incoming data from the network but still allows pushing data (a transaction created by simplewallet) _to_ the network. 

This would give the user the freedom to synchronize with the blockchain when they desire, and still be able to submit transactions to the network. 


# Discussion History
## iamsmooth | 2016-05-16T02:22:01+00:00
I'm not sure how useful this is. Why not just submit the transactions to a public node instead? Having your own unsynced node seems rather useless.


## Gingeropolous | 2016-08-24T02:48:36+00:00
> Why not just submit the transactions to a public node instead?

At the moment, pushing a transaction to a public node exposes stuff. Running a push-only daemon would allow you to have the same resource load as a remote-node, but with a lot more trust. 

> I'm not sure how useful this is. 

The other use case is a mobile node / wallet, be it either on someones laptop or phone. You may want to purchase something without having your daemon gobbling all the bajillions of transactions that are coming through the network (this will happen because Monero scales on chain. I really think designing with this in mind will be helpful.)

When you push a transaction, the only thing you need is the database up to the point you last did something with your account. 


## Gingeropolous | 2016-10-04T02:36:48+00:00
By the Power bestowed upon me as the Creator of the Issue, I hereby close this issue with the logic that the core implementation need not worry itself with such frivolous functionality. This functionality can be introduced into some other monero client designed for the SPV-type thing. 


# Action History
- Created by: Gingeropolous | 2016-05-02T01:26:55+00:00
- Closed at: 2016-10-04T02:36:48+00:00
