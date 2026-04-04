---
title: '[Bug] Different destination address shown on Ledger device'
source_url: https://github.com/monero-project/monero-gui/issues/3960
author: ghost
assignees: []
labels: []
created_at: '2022-07-04T10:15:30+00:00'
updated_at: '2022-07-07T10:19:53+00:00'
type: issue
status: closed
closed_at: '2022-07-07T10:19:53+00:00'
---

# Original Description
I was going to send some XMR from my ledger. Before sending I checked the destination address on both GUI and my ledger device.
The address shown on the GUI was fine. However, the address shown on Ledger is incorrect.
I made five attempts before posting here. Here's the destination address shown on my Ledger device: 

`46uz AyK9 bL2f hMz3 2Y5P W3di QR6C XNo2 4VEg P8cv qUvj VqLC 6abt EidM 6Co7 8WAT J2KS rykx Q5Ru GKqU FJKo Tsht 3Z51 QQU`

I have no idea if this is a bug of Ledger Firmware or Monero GUI. I checked the checksum of Monero GUI and Ledger Live and they're both legit. I also opened my Ledger to see if it's a modified version. It is completely the same as what I see online.

[Monero GUI log.md](https://github.com/monero-project/monero-gui/files/9038500/Monero.GUI.log.md)

I don't really know what helps you to figure out if it's a bug. So please tell me what to upload here. Thank you.

`35a0fa65bdf109abcaed6eb004ecf3126cc4f206ea10c3c7ecd21981e45202d6` sha256sum of that log file.

# Discussion History
## selsta | 2022-07-06T02:48:08+00:00
Please see https://github.com/LedgerHQ/app-monero/issues/66

If it was an integrated address (106 characters), Ledger will display the base address instead (95 characters). This was reported to Ledger a while ago, as you can see in the issue above, but it's unfortunately not fixed yet.

You can use the following website to test the address: https://xmr.llcoins.net/addresstests.html

If you enter the address in field 8 and click "Check Address" your Ledger should show the address from field 15.

# Action History
- Created by: ghost | 2022-07-04T10:15:30+00:00
- Closed at: 2022-07-07T10:19:53+00:00
