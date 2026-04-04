---
title: v0.14.0.1 release date?
source_url: https://github.com/monero-project/monero/issues/5243
author: gituser
assignees: []
labels: []
created_at: '2019-03-06T22:26:49+00:00'
updated_at: '2019-03-07T12:14:00+00:00'
type: issue
status: closed
closed_at: '2019-03-07T12:14:00+00:00'
---

# Original Description
Hi. 

You said the release should be ready within 24 hours. 

It's been already 3 days since it has been tagged on github.

Any update?

Seems some services already disabled their Monero support temporarily until you release fixed version:
* Coinpayments
* Kraken

There might be others as well..

# Discussion History
## gituser | 2019-03-06T22:28:59+00:00
Ping @fluffypony @dEBRUYNE-1 

## SamsungGalaxyPlayer | 2019-03-06T23:44:17+00:00
@gituser this is irrelevant, since these services typically build from source.

## gituser | 2019-03-06T23:58:12+00:00
@SamsungGalaxyPlayer that's what I thought initially, but why would they suspend XMR deposits/withdrawals then?

## gituser | 2019-03-07T00:01:20+00:00
Still there was a 24 hours promise for the immediate release and release is still not there!

## trasherdk | 2019-03-07T00:02:25+00:00
Kraken is still trading.

Latest upgrades for one of my servers:

	Jul 30  2018 monero-v0.12.2.0
	Jul 31  2018 monero-v0.12.3.0
	Oct 12 09:35 monero-v0.13.0.2
	Oct 26 00:51 monero-v0.13.0.4
	Mar  1 07:28 monero-v0.14.0.0
	Mar  4 13:09 monero-v0.14.0.1


## gituser | 2019-03-07T01:19:23+00:00
@trasherdk are you sure about deposits/withdrawals? https://status.kraken.com/incidents/stby8jkcnkg6
I never said that trading has been halted. Trading never stops.

Regarding building manually - sure it's a good practice, but it seems not everyone is aware of the new version and most prefer to use binaries instead of building from the source or applying the patch manually.

And from the mailing lists we got this:
```
 If you are running a
wallet on an exchange, payment gateway, or service, then you can
update to 0.14.0.1 using the appropriate tag, as in 'git checkout
v0.14.0.1'. Binaries for this release should be completed and uploaded
in the next 24 hours.
```
But it seems either monero CI/CD failed or something or @fluffypony went on vacation? :)

## trasherdk | 2019-03-07T03:32:22+00:00
Yes. I'm sure it's trading. Watching live.

![image](https://user-images.githubusercontent.com/5003891/53930380-a9052d80-40c3-11e9-8b95-cc7f477f4a86.png)

And I'm running latest:

    2019-03-07 03:29:48.498     7f8e94f23780        INFO    global  src/daemon/main.cpp:287 Monero 'Boron Butterfly' (v0.14.0.1-release)
    2019-03-07 03:29:48.498     7f8e94f23780        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
    2019-03-07 03:29:48.498     7f8e94f23780        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK

    2019-03-07 03:32:02.194 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182        [139.162.24.74:18080 OUT]  Synced 1786152/1786152
    2019-03-07 03:32:02.194 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1576        SYNCHRONIZED OK


## dEBRUYNE-1 | 2019-03-07T08:21:03+00:00
@gituser - The full release will be 0.14.0.2, which should be tagged today as far as I know. We're incrementing to .2 to include some additional fixes (e.g. the Ledger bug). Thus, v0.14.0.1 will merely be a tag, whereas v0.14.0.2 will be a full release. 

## gituser | 2019-03-07T12:14:00+00:00
@dEBRUYNE-1 thank you for the update.

Waiting for `v0.14.0.2`

# Action History
- Created by: gituser | 2019-03-06T22:26:49+00:00
- Closed at: 2019-03-07T12:14:00+00:00
