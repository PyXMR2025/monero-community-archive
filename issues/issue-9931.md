---
title: monerod --check-for-updates download fails SSL
source_url: https://github.com/monero-project/monero/issues/9931
author: plowsof
assignees: []
labels: []
created_at: '2025-05-21T14:09:27+00:00'
updated_at: '2025-05-22T13:47:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
2025-05-21 13:29:28.333	E SSL certificate is not in the allowed list, connection dropped
2025-05-21 13:29:28.363	E SSL handshake failed, connection dropped: unregistered scheme
2025-05-21 13:29:28.364	W Failed to establish SSL connection
2025-05-21 13:29:28.364	E Failed to connect to https://updates.getmonero.org/cli/monero-linux-x64-v0.18.4.0.tar.bz2
2025-05-21 13:29:28.364	E Failed to download https://updates.getmonero.org/cli/monero-linux-x64-v0.18.4.0.tar.bz2
```
--check-for-updates added here : https://github.com/monero-project/monero/commit/f640512c53caca9d7c3c69802841d174818cf953

failed to connect error comes from here : https://github.com/monero-project/monero/blob/125622d5bdc42cf552be5c25009bd9ab52c0a7ca/src/common/download.cpp#L58

i thought ` --rpc-ssl-allow-any-cert` could help but this is for rpc 

# Discussion History
# Action History
- Created by: plowsof | 2025-05-21T14:09:27+00:00
