---
title: '[Proposal/WIP] Display Fiat Balance within the Monero GUI'
source_url: https://github.com/monero-project/monero-gui/issues/1484
author: gene-telligent
assignees: []
labels:
- resolved
created_at: '2018-07-02T21:02:14+00:00'
updated_at: '2019-07-04T06:45:46+00:00'
type: issue
status: closed
closed_at: '2019-07-04T06:45:46+00:00'
---

# Original Description
There has been some discussion about displaying a fiat balance of wallets within the Monero GUI (https://github.com/monero-project/monero-gui/issues/621 , also discussed in https://github.com/monero-project/monero-gui/issues/869); I view it as a necessary quality of life feature that most other wallet solutions provide out of the box. Of course, with Monero's focus on security, having the GUI communicate with a third party API by default would be no good.

I've been working on this feature on my own time, and wanted to get this issue up as a placeholder and for discussion. 

My design philosophy has been:
- Implement as much within C++ as possible -- I'm using [QNetworkAccessManager](http://doc.qt.io/qt-5/qnetworkaccessmanager.html). Adding XHRs directly in QML/Javascript would add to rendering overhead and doesn't fit within the general principles of the wallet.
- Feature is off by default, and needs to be enabled within settings before any external communication is performed. I'm contemplating adding an additional warning popup/confirmation before it's enabled.
- Feature can be enabled/disabled at compile time by setting a flag (similar to WITH_SCANNER) which will allow for secure builds which completely exclude this functionality.
- Currently API sources are hard coded in C++, but eventually would like to allow for the end user to specify custom JSON endpoints, either in a configuration file or directly added through the UI.

In addition, I'm not a skilled UI developer, and didn't want to add additional bloat to the already crowded screen real estate. For the time being, I'm implementing the display of the converted fiat as a mouseover event, but will provide other easy QML hooks for more aesthetically-minded individuals to run with.
![monero-gui-mouseover](https://i.imgur.com/j1q5ku3.gif)

It's about 75% done right now, with some refactoring, polish, memory profiling necessary, but I wanted to make sure that no one else was busy working on this! 


# Discussion History
## sanderfoobar | 2018-07-28T19:15:18+00:00
I like it.

Would be nice to have those connections go through Kovri. I'm not sure if Kovri is far enough, perhaps you could already test with it.

In addition; do you have a link to your code or a PR?

## SamsungGalaxyPlayer | 2018-07-30T15:26:02+00:00
@skftn I love this idea. I think it would be perfect if we could have the wallet communicate with other I2P services. This will allow for more wallet flexibility without losing a significant amount of privacy.
This fiat balance display is a useful feature.

## jonathancross | 2018-09-15T20:29:30+00:00
Nice!

RE: I2P...

Although Kovri integration would be ideal, it seems unnecessary for the initial version of this feature (being that it is _disabled_ by default).   Unfortunately we have no idea how long it will be before Kovri is integrated with the monero daemon. There is no reason that should hold up such a great UI feature.

Once I2P support is implemented for the wallet, it should be easy to request this exchange rate feed over I2P as well.

I'm curious: what service are you using for Fiat exchange rates? I'm assuming they don't offer an eepsite anyway, do they?

I believe we would need a user setting to specify the feed URL (recommend leaving blank initially). This should help to address privacy / centralization concerns. You can then  _suggest_ a feed URL here or on Reddit, later.

## scottAnselmo | 2019-04-08T07:23:11+00:00
Nice work by those involved. It would be nice at some point to see this incorporated into other sections (namely history) and it takes into account time as while XMR may be volatile, one for example in reality only spent $50 April/May for utilities, not $25/$400 or something wacky like that. 

Applying fiat value to history is something that is arguably more dangerous though in that it reveals exact actual spend dates tied by a single IP (assuming the user does nothing to obfuscate) and potentially weakens the privacy of the blockchain as a whole. Thus it may be best to save that until after i2p-zero or a similar solution is integrated/bundled. Even then these services may see such a low volume(?) of requests for price history that a sudden burst of price history requests from different i2p addresses still has a high degree of inference of being from the same person and may be of some value in trying to deanonymize the blockchain.

Some other techniques like polling for a random time within 30 min of the tx etc rather than the actual time might also help mitigate.

## dEBRUYNE-1 | 2019-07-04T06:32:04+00:00
This is implemented in GUI v0.14.1.0. 

## dEBRUYNE-1 | 2019-07-04T06:32:09+00:00
+resolved

# Action History
- Created by: gene-telligent | 2018-07-02T21:02:14+00:00
- Closed at: 2019-07-04T06:45:46+00:00
