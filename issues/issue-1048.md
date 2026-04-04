---
title: This process has no code signature
source_url: https://github.com/monero-project/monero-gui/issues/1048
author: akseeker
assignees: []
labels:
- resolved
created_at: '2017-12-25T02:25:02+00:00'
updated_at: '2018-07-17T15:18:29+00:00'
type: issue
status: closed
closed_at: '2018-07-17T15:18:29+00:00'
---

# Original Description
I run Little Snitch on my Mac, and when I run the Monero GUI,  it warns me numerous times "The process has no code signature. The executable can be maliciously modified without being detected." for many, many IP addresses.

Is this normal?

I see a lot of outgoing traffic, too, and I'm curious: why is Monero so chatty through a process that has no code signature and is susceptible to being modified? Isn't that a fairly large security risk?

Sorry if this is an inappropriate  question for this forum. I would appreciate if you could point me to a (not overly technical) FAQ with this info. 

# Discussion History
## pebroz | 2018-01-17T22:17:16+00:00
Yes, this is normal. I just allow until quit. Little Snitch will not allow permanent rules for apps running in a sandbox on macOS.

## sanderfoobar | 2018-07-17T15:13:13+00:00
+resolved

# Action History
- Created by: akseeker | 2017-12-25T02:25:02+00:00
- Closed at: 2018-07-17T15:18:29+00:00
