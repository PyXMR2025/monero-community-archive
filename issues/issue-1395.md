---
title: GUI Appears to ignore /etc/hosts file
source_url: https://github.com/monero-project/monero-gui/issues/1395
author: stevesbrain
assignees: []
labels: []
created_at: '2018-05-10T00:15:29+00:00'
updated_at: '2018-07-17T13:48:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi all,

Setting a remote node with a DNS name that's only specified in `/etc/hosts` (but resolves to a different IP via DNS) seems to get ignored. It will never connect (given the port in question isn't listening on the IP that DNS resolves to) unless I enter the IP that's specified in the `/etc/hosts` file. Is this by design?

# Discussion History
## sanderfoobar | 2018-07-17T13:48:44+00:00
Possibly related to #933

# Action History
- Created by: stevesbrain | 2018-05-10T00:15:29+00:00
