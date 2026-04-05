---
title: Unknown File Request in Output
source_url: https://github.com/xmrig/xmrig/issues/2096
author: AntlerDM
assignees: []
labels:
- question
created_at: '2021-02-11T21:27:14+00:00'
updated_at: '2021-08-18T19:14:41+00:00'
type: issue
status: closed
closed_at: '2021-02-14T18:21:10+00:00'
---

# Original Description
**Describe the bug**
I am seeing the following lines periodically in the output of xmrig 6.8.0 (pre-compiled macOS Binary)...

[2021-02-11 12:50:04.289] 192.168.95.1 GET / 404 289 6006ms "(null)"
[2021-02-11 12:50:04.321] 192.168.95.1 GET /nice%20ports%2C/Tri%6Eity.txt%2ebak 404 289 0ms "(null)"

**Required data**
 - I am using the following command line option to start XMRig...

./xmrig --api-worker-id xmrig_V --http-host 0.0.0.0 --http-port 8888 -o 192.168.95.40:18089 -u <wallet> --coin monero --daemon

 - OS:  macOS Big Sur (11.2.1)

 - GPU:  CPU mining only.

**Additional context**
IP address in the launch command is my local daemon.
IP address in the output is my router.
File name in output is not familiar and searching reveals no files with that name (or "Trinity.txt.bak")
Mac firewall is enabled and XMRig is set to allow incoming connections


# Discussion History
## ghost | 2021-02-12T09:03:20+00:00
I suggest to create config.json with your valued and add false in log line. This will prevent any check for log file.

## xmrig | 2021-02-12T09:30:29+00:00
Someone or something makes HTTP requests from 192.168.95.1 to the miner API so likely your network is compromised.
[The code](https://github.com/xmrig/xmrig/blob/master/src/base/net/http/HttpResponse.cpp#L98) - every unsuccessful HTTP request is logged.
Thank you.


## AntlerDM | 2021-02-14T18:21:10+00:00
After a bit of digging, it appears this may be an nmap probe from my router's (Unifi) Endpoint Scanner.

Whew!

## PathToLife | 2021-08-18T06:09:07+00:00
@AntlerDM Did you manage to confirm this?

I also have nmap enabled on unifi os, noticed this in the logs of my development server.

`GET /nice%20ports%2C/Tri%6Eity.txt%2ebak 404`

## AntlerDM | 2021-08-18T19:14:40+00:00
I believe so. I found a post on the Ubiquiti Community site that confirmed that nmap was attempting to write a file to determine access to any httpd on the network. I disabled Endpoint Scanning and the message never appeared again.

# Action History
- Created by: AntlerDM | 2021-02-11T21:27:14+00:00
- Closed at: 2021-02-14T18:21:10+00:00
