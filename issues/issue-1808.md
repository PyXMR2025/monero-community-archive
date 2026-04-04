---
title: --log-file is now ignored in monero-wallet-cli
source_url: https://github.com/monero-project/monero/issues/1808
author: potyt
assignees: []
labels: []
created_at: '2017-02-26T19:49:19+00:00'
updated_at: '2017-08-13T15:48:12+00:00'
type: issue
status: closed
closed_at: '2017-08-13T15:48:12+00:00'
---

# Original Description
No matter what you specify in this option, the log file is always created in the current directory and named monero-wallet-cli.log, basically the command line option is ignored. This wasn't the situation previously (~6 months)

# Discussion History
## moneromooo-monero | 2017-02-26T21:35:50+00:00
I can see it too. Somehow, the command line code is claiming --log-file isn't given, when it is. Looking...

## moneromooo-monero | 2017-02-26T23:00:53+00:00
https://github.com/monero-project/monero/pull/1813

Surprisingly annoying to fix :)

## moneromooo-monero | 2017-08-13T15:45:41+00:00
+resolved

# Action History
- Created by: potyt | 2017-02-26T19:49:19+00:00
- Closed at: 2017-08-13T15:48:12+00:00
