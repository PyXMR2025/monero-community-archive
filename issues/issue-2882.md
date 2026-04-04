---
title: Missing make release-static-linux-x86_64
source_url: https://github.com/monero-project/monero/issues/2882
author: StiiCeva
assignees: []
labels: []
created_at: '2017-12-03T11:31:59+00:00'
updated_at: '2017-12-07T14:19:46+00:00'
type: issue
status: closed
closed_at: '2017-12-07T14:19:46+00:00'
---

# Original Description
Is there anyway to make a portable static build for POSIX? 

# Discussion History
## moneromooo-monero | 2017-12-03T12:28:59+00:00
A portable build for POSIX ? Surely it will depend on arch.
Also, the title is unclear. What is missing ? That target exists.

## StiiCeva | 2017-12-03T13:13:22+00:00
In the dev branch or the stable release? 

I'm using the v0.11.0.0  and it does not have that target.

## danrmiller | 2017-12-03T13:49:54+00:00
It is in both the master branch and in the release-v0.11.0.0 branch:

https://github.com/monero-project/monero/blob/c328163ffa28fee3236ddc7a958a50cede727ba6/Makefile#L91-L93

## StiiCeva | 2017-12-07T14:19:43+00:00
my bad some other script replaced it. Sorry about that!

# Action History
- Created by: StiiCeva | 2017-12-03T11:31:59+00:00
- Closed at: 2017-12-07T14:19:46+00:00
