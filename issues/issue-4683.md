---
title: Optional extra entropy during wallet creation
source_url: https://github.com/monero-project/monero-gui/issues/4683
author: EntropyHoover
assignees: []
labels: []
created_at: '2026-08-25T05:09:33+00:00'
updated_at: '2026-08-25T05:09:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The monero library already implemented add_extra_entropy_not_thread_safe in crypto/random.c. This function should be utilized in GUI wallet creation for allowing user to manually inject extra entropy. There should be an optional drawing board for collecting random mouse movement and keystrokes, and these information should be injected into the internal random state before key creation. 

If the add_extra_entropy_thread_safe() is implemented correctly, this would only increase the entropy and makes key generation safer. In very unlikely events, for example the OS entropy pool not implemented correctly, this would probably save the user from coldcard catastrophe.

# Discussion History
# Action History
- Created by: EntropyHoover | 2026-08-25T05:09:33+00:00
