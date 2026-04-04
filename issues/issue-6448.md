---
title: Regarding simplewallet's new "address one-off <major> <minor>" command
source_url: https://github.com/monero-project/monero/issues/6448
author: sumogr
assignees: []
labels: []
created_at: '2020-04-13T12:33:32+00:00'
updated_at: '2020-04-14T15:16:27+00:00'
type: issue
status: closed
closed_at: '2020-04-14T15:16:27+00:00'
---

# Original Description
https://github.com/monero-project/monero/pull/6394 seems buggy.
steps to replicate
Create a new wallet, create an one-off subaddress by setting a non existing major index (say 1) and any minor, it still creates a sub address, send some coins back to this address, poof! no key to find them **(do that on testnet of course not with actual xmr :P)**

# Discussion History
## moneromooo-monero | 2020-04-13T14:15:30+00:00
Yes, it's annoying. Maybe it should create an account to go with it. Doing so optionally means you can get money and still keep it "hidden" until such time you want to spend it.  Thoughts ?

## sumogr | 2020-04-13T14:33:22+00:00
> Yes, it's annoying. Maybe it should create an account to go with it. Doing so optionally means you can get money and still keep it "hidden" until such time you want to spend it. Thoughts ?

I can think of no other way than creating a new major index (when the chosen account does not exist) along with the one-off. Just think of a way to remind people that they keep hidden money in that account cause there is going to be confusion :D

## moneromooo-monero | 2020-04-13T14:58:19+00:00
That'd be counter productive, wouldn't it. It would not be hidden by definition :P

## sumogr | 2020-04-13T15:03:08+00:00
> That'd be counter productive, wouldn't it. It would not be hidden by definition :P

I guess,  if possible, just a check then that the major index selected for the one-off already exists
EDIT: also when minor is occupied then the one-off spawns the subaddress already occupying that place. so i guess both major and minor checking before generating would be appropriate

## moneromooo-monero | 2020-04-13T15:40:52+00:00
Maybe a "sweep_account" command would be better, since you really don't want to create an account with a very high index, it'd take a lot of time (and space).

## sumogr | 2020-04-13T15:45:36+00:00
true the command can easily be abused. well the advantages of it start to seem less than the disadvantages. I dont know i cant think of anything clever

## moneromooo-monero | 2020-04-13T18:37:56+00:00
https://github.com/monero-project/monero/pull/6449

# Action History
- Created by: sumogr | 2020-04-13T12:33:32+00:00
- Closed at: 2020-04-14T15:16:27+00:00
