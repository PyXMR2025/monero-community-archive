---
title: Cannot Sign or Verify any Messages
source_url: https://github.com/monero-project/monero-gui/issues/4456
author: marvagabi
assignees: []
labels: []
created_at: '2025-06-10T18:19:37+00:00'
updated_at: '2025-06-26T16:25:06+00:00'
type: issue
status: closed
closed_at: '2025-06-26T16:25:06+00:00'
---

# Original Description
Hello, I use my Trezor with the GUI wallet and I seem to not be able to sign/verify any messages signed with primary account. I did some googling but couldn't' find anything. I've tried it on both the Mac and windows versions of the Monero GUI with the same results. Am I missing something? Or it something up with my hardware wallet?

![Image](https://github.com/user-attachments/assets/e1dc5e8e-8cfd-48dd-badc-b95dca199bca)

# Discussion History
## marvagabi | 2025-06-10T20:24:05+00:00
As a test I created a new wallet not tied to my Trezor and sign/verify worked fine. So is this just unsupported for hardware backed wallets? 

If so is this documented anywhere? I feel like it should be shown when setting up a hardware backed wallet that you won't be able to do certain things.

## selsta | 2025-06-11T14:32:57+00:00
Yes, this feature is not implemented together with Trezor. The UI not making this clear is an oversight.

## marvagabi | 2025-06-11T14:41:14+00:00
> Yes, this feature is not implemented together with Trezor. The UI not making this clear is an oversight.

Thank you for the confirmation, is support for this planned or just an accepted limitation of using hardware wallets?

## selsta | 2025-06-26T16:24:24+00:00
It's likely not going to be implemented any time soon, unless someone volunteers to add the functionality.

# Action History
- Created by: marvagabi | 2025-06-10T18:19:37+00:00
- Closed at: 2025-06-26T16:25:06+00:00
