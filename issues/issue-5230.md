---
title: '`Illegal instruction: 4` on monero-wallet-cli run.'
source_url: https://github.com/monero-project/monero/issues/5230
author: domol
assignees: []
labels: []
created_at: '2019-03-05T09:46:11+00:00'
updated_at: '2019-04-03T18:51:22+00:00'
type: issue
status: closed
closed_at: '2019-04-03T18:51:22+00:00'
---

# Original Description
Hey!
I just downloaded new command-line tools but I have problem running it. All I get as a response is:
`Illegal instruction: 4`
Mac OS: Mojave(10.14.1)
Monero CLI version: 0.14.0.0


# Discussion History
## moneromooo-monero | 2019-03-05T11:36:49+00:00
What architecture/processor (as detailed as you can get) ?

## selsta | 2019-04-02T12:17:02+00:00
@Domol Do you have an anti-virus program running?

## sedited | 2019-04-02T13:26:25+00:00
@Domol can you run monerod? Does it run with just  `-- help` as an argument? 

## domol | 2019-04-03T18:51:22+00:00
Hey guy sorry for not responding. I started using Docker and linux release. Anyway the problem is gone with v0.14.0.2-release. 
If you still want some info let me know.

# Action History
- Created by: domol | 2019-03-05T09:46:11+00:00
- Closed at: 2019-04-03T18:51:22+00:00
