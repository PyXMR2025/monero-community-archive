---
title: XMRig static Linux executable compilation issue
source_url: https://github.com/xmrig/xmrig/issues/3016
author: matmad
assignees: []
labels: []
created_at: '2022-04-09T17:23:37+00:00'
updated_at: '2025-06-28T10:40:44+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:40:44+00:00'
---

# Original Description
I have a problem with compilation of XMRig into static Linux executable. When I compile it using instructions given in the documentation I get "Segmentation fault (core dumped)" on fresh Linode (Ubuntu 21.10) installation. I am compiling on Kali. At the same time static executable, that I can download from official XMRig website works perfect on fresh Linode. I have tried compiling using Alpine docker and compiled executable worked on the docker and on Kali machine, but does not work on Linode. I am using compilation code of conduct and parameters given in the documentation: cmake .. -DXMRIG_DEPS=scripts/deps -DBUILD_STATIC=ON

Long story short - I would like to compile XMRig to static executable that works on most Linux distributions (like the one that you can download from official XMRig website). Inb4 I have NOT made any changes to the source code yet - first I am trying to figure out the proper compilation method.

Any ideas?

# Discussion History
# Action History
- Created by: matmad | 2022-04-09T17:23:37+00:00
- Closed at: 2025-06-28T10:40:44+00:00
