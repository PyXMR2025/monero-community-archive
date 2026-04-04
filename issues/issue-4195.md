---
title: Verifying signature on MacOS results in a spinning wheel
source_url: https://github.com/monero-project/monero-gui/issues/4195
author: recanman
assignees: []
labels: []
created_at: '2023-07-12T20:35:43+00:00'
updated_at: '2023-08-13T23:47:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Unfortunately, I don't have much experience with debugging applications on MacOS. Here are the reproduction steps:

1. Open wallet in `monero-wallet-gui`
2. Go to `Advanced` tab
3. Click on `Sign/verify` tab
4. Paste in a signature, address, and message. Doesn't matter if they are valid or not.
5. Click `Verify Message`
6. The application hangs until it is killed

I have not checked this with file signature verification.

**MacOS Version:** Ventura 13.4 (22F66)
**monero-wallet-gui Version:** 0.18.2.2-release (Qt 5.12.8)

Please let me know if I should provide any more information.

# Discussion History
## selsta | 2023-07-13T11:55:45+00:00
Can reproduce with release binaries, does not seem to happen when self compiled.

## selsta | 2023-08-13T23:47:23+00:00
This will likely require an update of the Qt dependency to 5.15.

# Action History
- Created by: recanman | 2023-07-12T20:35:43+00:00
