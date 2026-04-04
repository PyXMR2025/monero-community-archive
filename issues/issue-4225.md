---
title: MoneroD initializes cryptonote protocol
source_url: https://github.com/monero-project/monero-gui/issues/4225
author: I-got-mine
assignees: []
labels: []
created_at: '2023-10-10T17:45:39+00:00'
updated_at: '2023-10-10T17:50:17+00:00'
type: issue
status: closed
closed_at: '2023-10-10T17:50:16+00:00'
---

# Original Description
I installed the GUI to Debian from binaries. When monerod(v0.18.2.2-release) starts it says "Crypronote protocol initialized OK." It is my understanding that randomX is completely separate from crypronote. Am I misunderstanding something, or is monerod initializing the wrong protocol?

# Discussion History
## selsta | 2023-10-10T17:50:16+00:00
RandomX is the mining algorithm used, CryptoNote is the name of the software monero is originally based on.

There's nothing wrong with the message you are seeing.

# Action History
- Created by: I-got-mine | 2023-10-10T17:45:39+00:00
- Closed at: 2023-10-10T17:50:16+00:00
