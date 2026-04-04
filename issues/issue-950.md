---
title: GUI doesn't run smooth
source_url: https://github.com/monero-project/monero-gui/issues/950
author: ghost
assignees: []
labels:
- resolved
created_at: '2017-11-12T00:13:52+00:00'
updated_at: '2019-07-04T07:36:47+00:00'
type: issue
status: closed
closed_at: '2019-07-04T07:36:47+00:00'
---

# Original Description
I notice the GUI does not run smooth sometimes, for example when I click on something in the menu. It hangs then and needs some seconds to react to the event. I also notice this when using a new installed OS. It seems something is blocking the GUI process sometimes.

Does anyone also noticed this behaviour?

# Discussion History
## sanderfoobar | 2017-11-12T00:33:09+00:00
Someone correct me if I'm wrong; this happens when the GUI is syncing the blockchain. I think an effort had been made to make the GUI more responsive but I am not sure if it is merged into a release yet.

## dEBRUYNE-1 | 2017-11-12T14:25:56+00:00
Do you have a relatively older system? If so, could you try adding this line in the daemon startup flags box:

`--max-concurrency 1 --limit-rate 500 --block-sync-size 5`

## ghost | 2017-11-12T14:28:07+00:00
No, it is a powerful and up-to-date system :)

## ITwrx | 2017-12-31T03:26:46+00:00
you might check your cpu usage. my layman's understanding is that cryptonight is expensive(resource usage wise) when verifying, by design, so when you're trying to sync it maxes out the cpu. this makes the gui slow to respond. when it gets done syncing i bet the gui is back to normal responsiveness. 

## SleepswithGators | 2018-02-22T00:37:02+00:00
Does the wallet need to restart in order to make changes?


## ITwrx | 2018-02-22T00:40:36+00:00
@SleepswithGators no, but if you want it to respond to you, it may need to be completely done syncing.

## dEBRUYNE-1 | 2019-07-04T06:57:56+00:00
This should be fixed in GUI v0.14.1.0, as xiphon added a lot of optimizations in this regard. 

## dEBRUYNE-1 | 2019-07-04T06:58:01+00:00
+resolved

# Action History
- Created by: ghost | 2017-11-12T00:13:52+00:00
- Closed at: 2019-07-04T07:36:47+00:00
