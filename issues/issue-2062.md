---
title: v6.7.2 stopped working right after the launch of v6.8.0
source_url: https://github.com/xmrig/xmrig/issues/2062
author: matheusbach
assignees: []
labels:
- question
created_at: '2021-01-26T11:45:08+00:00'
updated_at: '2021-09-11T09:57:56+00:00'
type: issue
status: closed
closed_at: '2021-01-26T12:20:59+00:00'
---

# Original Description
Software was running normally before the update. Right after the release of the new version, when closing and reopening XMRig it displays the error read error: "end of file"

Screenshot:
![xmrig-v6 7 2-error](https://user-images.githubusercontent.com/35426162/105841005-b32fbe00-5fb2-11eb-8eeb-a1f0588bfba4.png)

My Config File:
[config.json](https://github.com/xmrig/xmrig/files/5873067/config.json.txt)


Tested with the same configuration file model on several computers and all presented the same error


# Discussion History
## matheusbach | 2021-01-26T11:59:41+00:00
I tested dozens of combinations of settings in my configuration file and found that the error happens at line  ``"url": "xmr-us-west1.nanopool.org:14433",`` of my config.json file. It always worked using the ``xmr-us-west1.nanopool.org:14433`` url, but now it is no longer working, but using the XMRig donation url ``donate.v2.xmrig.com:3333`` it works. v6.8.0 is also showingthe same problem 

## xmrig | 2021-01-26T12:07:44+00:00
Seems this issue with nanopool and at least `xmr-us-east1.nanopool.org:14433` works. This is not related to the miner.
Thank you.


## matheusbach | 2021-01-26T12:20:59+00:00
Very thanks. Sorry for the mistake caused by the coincidence of the facts. Working now

## FibreFoX | 2021-09-10T21:59:31+00:00
Using `Stratum Port` (14444) instead of `SSL/TLS Port` (14433) works fine, maybe something wrong with the TLS/SSL of nanopool. Had the same problem, but got this working without secure connection.

EDIT: I just realized, that when connecting to `SSL/TLS Port` (14433) I had to add the parameter `--tls` to the command, then everything worked out okay.

# Action History
- Created by: matheusbach | 2021-01-26T11:45:08+00:00
- Closed at: 2021-01-26T12:20:59+00:00
