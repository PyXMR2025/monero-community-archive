---
title: Segfault after BlockchainLMDB::do_resize
source_url: https://github.com/monero-project/monero/issues/402
author: pmknutsen
assignees: []
labels: []
created_at: '2015-09-12T05:53:20+00:00'
updated_at: '2015-09-15T15:22:42+00:00'
type: issue
status: closed
closed_at: '2015-09-15T15:22:42+00:00'
---

# Original Description
bitmonerod silently fails when launched after executing BlockchainLMDB::do_resize. I have reset the database, and re-synced with the same result. The following is the last output when running the deamon. Box runs Ubuntu 14.04 LTS, with 8GB RAM and tons of HDD space to spare:

```
2015-Sep-11 22:47:38.748646 BlockchainLMDB::need_resize
2015-Sep-11 22:47:38.748851 DB map size:     1073741824
2015-Sep-11 22:47:38.749055 Space used:      967413760
2015-Sep-11 22:47:38.749251 Space remaining: 106328064
2015-Sep-11 22:47:38.749446 Size threshold:  0
2015-Sep-11 22:47:38.749818 Percent used: 0.9010  Percent threshold: 0.8000
2015-Sep-11 22:47:38.751299 Threshold met (percent-based)
2015-Sep-11 22:47:38.751443 LMDB memory map needs resized, doing that now.
2015-Sep-11 22:47:38.751589 BlockchainLMDB::do_resize
2015-Sep-11 22:47:38.751828 LMDB Mapsize increased.  Old: 1024MiB, New: 2048MiB
```

Segfault as reported in /var/log/syslog

```
kernel: [859428.738710] bitmonerod[8170]: segfault at 72a0001c ip 083ec820 sp bf814980 error 4 in bitmonerod[8048000+58e000]
kernel: [859502.299108] bitmonerod[8180]: segfault at 72a0001c ip 083ec820 sp bf8658e0 error 4 in bitmonerod[8048000+58e000]
kernel: [859520.137126] bitmonerod[8188]: segfault at 72a0001c ip 083ec820 sp bfa2fb90 error 4 in bitmonerod[8048000+58e000]
```


# Discussion History
## pmknutsen | 2015-09-15T15:22:42+00:00
Found the cause of this segfault. Bitmonero was running on 32-bit Ubuntu. Problem resolved when updating OS to 64 bit.


# Action History
- Created by: pmknutsen | 2015-09-12T05:53:20+00:00
- Closed at: 2015-09-15T15:22:42+00:00
