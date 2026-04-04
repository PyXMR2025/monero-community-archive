---
title: Trezor T passphrase prompt in Monero GUI
source_url: https://github.com/monero-project/monero/issues/6491
author: requestor1607
assignees: []
labels: []
created_at: '2020-05-01T11:57:12+00:00'
updated_at: '2021-08-13T04:39:52+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:39:52+00:00'
---

# Original Description
Currently a driver update has been rolled out by Trezor, since then the prompt for input of passphrases is not on the Trezor anymore. In the Monero GUI only at startup the passphrase is requested via the wallet. Then several times the Trezor blinks to enter the passphrase, but Monero does not show a dialog box. 
The end result: no synchronized wallets and lots of people afraid loosing their transactions etc.

People who use the command line editor force the Trezor to use the Trezor, solving the issue. However, people who donwload the GUI are most probable not able to do that.

https://www.reddit.com/r/monerosupport/comments/gb1981/enter_passphrase/


# Discussion History
## selsta | 2020-05-01T11:59:19+00:00
This should be solved with v0.15.1.0 which should be out in 1-2 weeks.

## requestor1607 | 2020-05-01T12:01:04+00:00
> This should be solved with v0.15.1.0 which should be out in 1-2 weeks.

That sounds great! Did not know it was already on the radar.

## selsta | 2020-05-01T12:02:06+00:00
There are both CLI and GUI PRs that should fix this but the firmware update was a bit too fast for us to put out an update in time.

# Action History
- Created by: requestor1607 | 2020-05-01T11:57:12+00:00
- Closed at: 2021-08-13T04:39:52+00:00
