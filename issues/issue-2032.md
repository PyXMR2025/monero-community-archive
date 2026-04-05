---
title: Is it possible to set up a proxy server for connection?
source_url: https://github.com/xmrig/xmrig/issues/2032
author: wallisonfgt
assignees: []
labels:
- question
created_at: '2021-01-11T02:13:26+00:00'
updated_at: '2021-04-12T14:24:34+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:24:34+00:00'
---

# Original Description
Hello, I want to congratulate you on the project, it's just wonderful, amazing !!!

My situation is as follows:
I would like to use the miner in my work environment when the machine is idle, but the internet goes through a proxy and is blocking the connection, I would like to know if it is possible to configure the proxy server settings from where I work in the configuration files.

Thank you very much!!!

# Discussion History
## SChernykh | 2021-01-11T08:47:34+00:00
Check with your employer to see if they can add exception on their proxy. All other options mean you're doing it without approval and risk getting fired for $15-20/month from mined XMR.

## wallisonfgt | 2021-01-11T17:14:56+00:00
SChernykh, Thank You!
I thought I could manually insert the proxy, because the address via the web I can reach because the proxy is configured in the browser, but within the application I cannot, because it does not have proxy information for it to reach the destination.

## SChernykh | 2021-01-11T17:32:51+00:00
XMRig only supports socks5 proxies, not http proxies.

# Action History
- Created by: wallisonfgt | 2021-01-11T02:13:26+00:00
- Closed at: 2021-04-12T14:24:34+00:00
