---
title: Wallet shows "Unlocked balance (waiting for block)" but functions normally
source_url: https://github.com/monero-project/monero-gui/issues/2261
author: exotic-particle
assignees: []
labels: []
created_at: '2019-07-04T02:36:41+00:00'
updated_at: '2019-11-25T08:59:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
GUI wallet shows "Unlocked balance (waiting for block)."
- The unlocked balanced is the same as the balance.
- Wallet fully synced.
- Daemon fully synched and height verified with moneroblocks.info.
- Other wallets loaded into the same GUI do not have this issue. 
- I have restarted the daemon, wallet, and computer multiple times over the weeks since the issue first occurred. 
- Issue originated with GUI v0.14.0.0 and persists in v0.14.1.0.

### Issue's origin
This is a lingering issue after I had a stuck pending transaction that never broadcast to the network. 

The stuck transaction occurred after I generated a transaction then canceled it to edit the description field. The wallet was still syncing as I filled out the amount and address fields, and when I clicked to add the description, the banner at the top went away, causing the GUI to page up half an inch, making me click Send instead.

The transaction never broadcast to the network (I verified on moneroblocks.info.)

I took the following steps to 'unstick it.'

- Entered `flush_txpool` into Settings > Log > Command box.
- Rescanned wallet under Settings > Wallet > Rescan.

Problem solved. The stuck transaction now shows "Blockheight FAILED" in History. I can send and receive in the wallet just fine, but it still shows the "waiting for block" message next to "Unlocked balance." 
 

### System Information:

- GUI v0.14.1.0 (Issue originated on v0.14.0.0)
- Advanced Mode
- MacOS 10.13.6

# Discussion History
## selsta | 2019-09-01T01:20:59+00:00
Is this issue still happening? Does the same happen when using the CLI?

## dEBRUYNE-1 | 2019-11-25T08:59:28+00:00
Ping @exotic-particle.

# Action History
- Created by: exotic-particle | 2019-07-04T02:36:41+00:00
