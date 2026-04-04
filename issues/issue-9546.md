---
title: blocklist.moneropulse.xx TXT DNS replies too big to be handled by dnscrypt-proxy
source_url: https://github.com/monero-project/monero/issues/9546
author: kaczybar
assignees: []
labels:
- question
- low priority
created_at: '2024-10-26T19:17:32+00:00'
updated_at: '2025-02-20T21:10:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Im hosting a monero node and at the same time I use dnscrypt-proxy for my network. I noticed I cannot resolve the "blocklist.moneropulse.xx" queries. Reached out to dnscrypt-proxy developer (https://www.reddit.com/r/dnscrypt/comments/1g6txma/network_error_when_querying_txt/), his answer:

`"The response is unreasonably large, more than 4096 bytes which is the maximum size dnscrypt-proxy accepts as a response. (...) That blocklist should be split across multiple DNS records. Stuffing all these IPs in a single one is not going to scale.`"

I had to disable enable-dns-blocklist, have to maintain my own static list. 

# Discussion History
# Action History
- Created by: kaczybar | 2024-10-26T19:17:32+00:00
