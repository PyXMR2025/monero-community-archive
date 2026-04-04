---
title: add a torrent file to downloads
source_url: https://github.com/monero-project/monero-site/issues/2538
author: plowsof
assignees: []
labels: []
created_at: '2025-10-09T11:41:30+00:00'
updated_at: '2025-10-09T11:45:15+00:00'
type: issue
status: closed
closed_at: '2025-10-09T11:45:15+00:00'
---

# Original Description
duplicate of #1629 

- A multi file torrent (not the blockchain file) has a reproducible file-info hash.
- a webseed acts as a bootstrap if there are no peers seeding.
- easy to create/update https://github.com/plowsof/monero-torrent ([see releases](https://github.com/plowsof/monero-torrent/releases/tag/v0.18.4.2))
- a placeholder PR is made, however, discussion is required and if approved - the torrent file can be updated as a final release step and added to dns via downloads.getmonero.org/torrent
- To support webseed **set and forget** redirects on getmonero are required: (getmonero will only webseed the latest version)

--- 
redirect for hashes.txt
```
location ~ ^/monero-v[0-9.]+/hashes\.txt$ {
    return 302 https://www.getmonero.org/downloads/hashes.txt;
}
```
bfs gpg key:
```
location ~ ^/monero-v[0-9.]+/binaryfate\.asc$ {
    return 302 https://raw.githubusercontent.com/monero-project/monero/master/utils/gpg_keys/binaryfate.asc;
}
```
and everything else
```
location ~ ^/(monero-v[0-9.]+)/(.+)$ {
    return 302 https://dlsrc.getmonero.org/$2;
}
```

# Discussion History
# Action History
- Created by: plowsof | 2025-10-09T11:41:30+00:00
- Closed at: 2025-10-09T11:45:15+00:00
