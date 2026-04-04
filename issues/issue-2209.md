---
title: Ledger issues bundled
source_url: https://github.com/monero-project/monero-gui/issues/2209
author: ghost
assignees: []
labels: []
created_at: '2019-06-11T08:46:16+00:00'
updated_at: '2019-10-23T16:21:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Issue (1) - GUI freezes:** When creating a new wallet after clicking "Export View Key" on Ledger Nano S the GUI doesn't react for about 15 seconds and Windows 10 comes up with _"Program is not reacting. Force close?"_ (not the exact wording). The user must click on _"Wait for program"_ (or similar) and about 10 seconds later the GUI is back again and asking for a new password. All fine - just bad user experience if you're a noob.

___

**Issue (2) - Improvements when denying "Export View Key":**
![image](https://user-images.githubusercontent.com/46682965/64290805-1573c300-cf67-11e9-9d49-a78d7e8bc570.png)
- The user should be informed _"You have denied the export of your public view key, therefore calculations will have to be done on your hardware wallet. This may take a very long time."_
- `Wallet blocks remaining: 12345 blocks` should be updated every block - not every 999 blocks. (1 block takes about 1 second with Ledger Nano S and subaddress lookahead 1:1)
- Clicking on the "close wallet" icon in the balance card shouldn't close the GUI. (A bug, IMO.)

___

**Issue (3) - Splash screen when opening a wallet:**
![image](https://user-images.githubusercontent.com/46682965/64289632-dfcdda80-cf64-11e9-9470-64934e80c9ba.png)
Add text: _"Please check your hardware wallet - your input may be required."_ (This text was already added for the **creating** and **transacting** splash screen by @selsta in #2353.)

___

**Issue (4) - `Account` and `Receive` page load slow:**
Clicking on these pages has a delay, results in a bad experience. Probably subaddress related, the UI loading gets blocked by something subaddress related. Solution would e.g. be load the page first and load the subaddresses afterwards.

# Discussion History
## selsta | 2019-09-04T18:54:21+00:00
Maybe you could open one issue that bundles all the current Ledger performance issues.

## ghost | 2019-09-04T21:04:15+00:00
Done. All bundled here.

## selsta | 2019-09-05T21:34:40+00:00
Can you add https://github.com/monero-project/monero-gui/issues/2072 to this post?

## ghost | 2019-09-05T21:39:24+00:00
Done.

# Action History
- Created by: ghost | 2019-06-11T08:46:16+00:00
