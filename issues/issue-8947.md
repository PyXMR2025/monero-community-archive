---
title: '`tools::wallet2::is_deterministic()` always returns `false` when account keys
  are encrypted in memory'
source_url: https://github.com/monero-project/monero/issues/8947
author: jeffro256
assignees: []
labels:
- pending review
created_at: '2023-07-13T16:58:10+00:00'
updated_at: '2023-12-07T20:29:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`wallet2`, when `m_ask_password == AskPasswordToDecrypt && !m_unattended && !m_watch_only` is true, will encrypt the spend key in memory, requiring a password to decrypt if it is to be used in any cryptographic operations. The way that the `is_deterministic` method figures whether the wallet is deterministic is that it does the spend key -> view key derivation and sees if the stored keys line up as they should in a deterministic wallet. This doesn't work, however, when the spend key is encrypted. So for this method to work properly again, either 1) a password needs to be passed to this method to decrypt the spend key and then do the calculation or 2) this calculation needs to be done once and the result cached as a class field to be retrieved later so decryption is no longer needed.

https://github.com/monero-project/monero/blob/00fd416a99686f0956361d1cd0337fe56e58d4a7/src/wallet/wallet2.cpp#L1363-L1369

# Discussion History
# Action History
- Created by: jeffro256 | 2023-07-13T16:58:10+00:00
