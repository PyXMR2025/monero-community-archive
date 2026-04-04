---
title: ' `GLIBC_2.23'' not found '
source_url: https://github.com/monero-project/monero/issues/6860
author: pavoltravnik
assignees: []
labels: []
created_at: '2020-10-04T10:15:04+00:00'
updated_at: '2020-10-04T10:42:24+00:00'
type: issue
status: closed
closed_at: '2020-10-04T10:42:23+00:00'
---

# Original Description
```
./monerod
./monerod: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.23' not found (required by ./monerod)

ldd --version
ldd (Debian GLIBC 2.19-18+deb8u10) 2.19
Copyright (C) 2014 Free Software Foundation, Inc.
```
i am unable to run latest monero daemon on latest Debian 10


# Discussion History
## pavoltravnik | 2020-10-04T10:42:23+00:00
installed new clean version of debian 10 and it works
closing this issue

# Action History
- Created by: pavoltravnik | 2020-10-04T10:15:04+00:00
- Closed at: 2020-10-04T10:42:23+00:00
