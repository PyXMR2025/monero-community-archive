---
title: boost_serialization_helper.h:108 Exception at [unserialize_obj_from_file],
  what=unsupported version
source_url: https://github.com/monero-project/monero/issues/849
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-05-24T12:16:40+00:00'
updated_at: '2016-08-10T16:11:40+00:00'
type: issue
status: closed
closed_at: '2016-08-10T16:11:40+00:00'
---

# Original Description
just cloned repository, so:
Latest commit a837c9c  7 days ago

2016-May-24 06:58:14.717997 Initializing core...
2016-May-24 06:58:14.728190 ERROR /home/gbone/bitmonero_head/src/common/boost_serialization_helper.h:108 Exception at [unserialize_obj_from_file], what=unsupported version
2016-May-24 06:58:14.728349 Loading blockchain from folder /home/gbone/.bitmonero/lmdb ...


# Discussion History
## moneroexamples | 2016-05-26T00:29:22+00:00
What os?


## Gingeropolous | 2016-05-31T00:27:22+00:00
gbone@gbone-therock:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.4 LTS
Release:        14.04
Codename:       trusty


## Gingeropolous | 2016-08-10T16:11:40+00:00
This issue has been fixed (somehow)


# Action History
- Created by: Gingeropolous | 2016-05-24T12:16:40+00:00
- Closed at: 2016-08-10T16:11:40+00:00
