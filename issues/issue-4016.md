---
title: '[Need Lib Update] Libssl incompatible with 1.0.2 (porting to libssl1.0.2 or
  libssl1.1)'
source_url: https://github.com/monero-project/monero/issues/4016
author: Jorropo
assignees: []
labels: []
created_at: '2018-06-18T04:47:57+00:00'
updated_at: '2018-07-19T17:55:54+00:00'
type: issue
status: closed
closed_at: '2018-07-19T17:55:22+00:00'
---

# Original Description
I was setuping an node on debian but monerod doesn't support libssl1.0.2, just 1.0.0, but libssl1.0.0 isn't any more in the stable repo.
So for not use an very old package that starting to be removed from repo and make installation very much easier, an update to libssl1.0.2 or the best libssl1.1 need to be consider.
PS: libssl1.1 is in debian stable, ubuntu 18.04 repo's

# Discussion History
## moneromooo-monero | 2018-06-18T09:36:12+00:00
Post the errors. I am using one of the 1.0.2...

## pazos | 2018-06-21T01:01:04+00:00
@Jorropo: Debian Stretch & Ubuntu Bionic ship the same version (1.0.2-n). From my ubuntu box: 

```
apt-cache madison libssl1.0-dev
libssl1.0-dev | 1.0.2n-1ubuntu5 | http://es.archive.ubuntu.com/ubuntu bionic/main amd64 Packages
```

This works ok for build this repo and can coexist with libssl1.1

## moneromooo-monero | 2018-07-09T09:30:03+00:00
If no evidence of the claims soon, I'll close since it works for me.

## moneromooo-monero | 2018-07-18T17:33:39+00:00
ping, last chance

## Jorropo | 2018-07-19T17:55:54+00:00
I retry on same condition and the bug doesn't appear anymore

# Action History
- Created by: Jorropo | 2018-06-18T04:47:57+00:00
- Closed at: 2018-07-19T17:55:22+00:00
