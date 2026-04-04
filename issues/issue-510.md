---
title: 'OSX: Daemon does not shut down if GUI is closed'
source_url: https://github.com/monero-project/monero-gui/issues/510
author: ghost
assignees: []
labels: []
created_at: '2017-02-28T04:48:30+00:00'
updated_at: '2017-03-03T17:01:00+00:00'
type: issue
status: closed
closed_at: '2017-03-03T17:01:00+00:00'
---

# Original Description
The first time the daemon is started, it starts fine. But if I "X" out of the GUI in OSX 10.12.3 and open it a few hours later, the wallet doesn't seem to start the daemon. I then clicked "Show Status" in Settings and saw that the daemon had been running for over two hours, even though the GUI was closed.

# Discussion History
## Jaqueeee | 2017-02-28T05:09:12+00:00
This is intentional. You need to close the daemon manually if you don't want it running. 

## ghost | 2017-02-28T05:10:26+00:00
Really? I don't know if I like this. This means anybody who runs the GUI will (without their knowledge) be turning their computers into full time nodes?

## ghost | 2017-03-01T08:09:29+00:00
This is a non obvious behaviour for non experts. I think it should change to shut down automatically but present an option somewhere in the preferences for experts to 'leave daemon running in background after gui shuts down'

## Jaqueeee | 2017-03-01T21:53:36+00:00
@xmr-eric @NanoAkron 
Added a confirmation popup on exit in #515 to let the user choose to shutdown daemon or keep it running in bg. 

## ghost | 2017-03-01T22:35:13+00:00
@jaqueeee You are the man!!

## ghost | 2017-03-03T00:12:42+00:00
@Jaqueeee Side question, why was the functionality added to keep the daemon running in the background after the GUI is closed? Multiple GUI instances or something?

## Jaqueeee | 2017-03-03T10:50:20+00:00
There was a discussion in #monero-dev and also this request https://github.com/monero-project/monero-core/issues/484

IMO it's more convenient having it running in the background. Minimal sync time when starting up wallet.

@xmr-eric 

# Action History
- Created by: ghost | 2017-02-28T04:48:30+00:00
- Closed at: 2017-03-03T17:01:00+00:00
