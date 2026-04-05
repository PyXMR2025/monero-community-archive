---
title: Xmrig with built-in TOR
source_url: https://github.com/xmrig/xmrig/issues/2209
author: paolosezart
assignees: []
labels:
- wontfix
created_at: '2021-03-25T19:51:57+00:00'
updated_at: '2021-10-06T14:05:52+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:48:37+00:00'
---

# Original Description
Is an xmrig version with built-in TOR expected? That is, without an intermediate proxy. It would be very convenient and more anonymous if xmrig already had the ability to mine directly to onion addresses. There would be no need to install a separate program for TOR.

# Discussion History
## 00-matt | 2021-04-01T09:45:13+00:00
Embedding Tor is quite difficult. You could bundle the Tor daemon with XMRig, and use a script to launch it if the system doesn't already have Tor running, which I believe is how the Feather wallet works.

## paolosezart | 2021-10-06T05:36:37+00:00
So what about embedding tor into xmrig?
Are there any decisions on this matter?

## 00-matt | 2021-10-06T14:05:52+00:00
Going by the wontfix label, I think you have your answer ;D

The best thing to do (on most Linux distros) is make a custom XMRig package that depends on Tor, and ship a config that defaults to `127.0.0.1:9050` as SOCKS address.  Or use some other config management tool like Ansible to set it all up for you.

# Action History
- Created by: paolosezart | 2021-03-25T19:51:57+00:00
- Closed at: 2021-04-12T13:48:37+00:00
