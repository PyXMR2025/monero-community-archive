---
title: Monero isn't detecting my wallet [ASAP]
source_url: https://github.com/monero-project/monero/issues/7490
author: funtasma16
assignees: []
labels: []
created_at: '2021-03-09T21:55:59+00:00'
updated_at: '2022-07-19T19:46:41+00:00'
type: issue
status: closed
closed_at: '2022-07-19T19:46:41+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/80351877/110543598-e82a4700-8100-11eb-8f12-9879a8e10205.png)


# Discussion History
## vtnerd | 2021-03-09T22:05:10+00:00
What about `netstat` to show/check the open ports? This typically means the process isn't listening on the port or the other software is connecting to the wrong port.

## funtasma16 | 2021-03-09T22:24:40+00:00
> What about `netstat` to show/check the open ports? This typically means the process isn't listening on the port or the other software is connecting to the wrong port.

All the ports are opened, the configuration of the pool program is the default (Daemon ip: 127.0.0.1 | Daemon port: 18081). Also im using the default configuration of monero, i just maked the program and started it.

## luquinhas8551 | 2021-03-09T22:29:21+00:00
Funtasma16 i have exactly the same problem, i cant start a pool with monero daemon because it say connection refussed.

## moneromooo-monero | 2021-03-10T16:41:41+00:00
Has it finished syncing ? You can tell by running getinfo on the daemon RPC, and checking height.

## selsta | 2022-07-19T19:46:41+00:00
Closing as there was no reply.

# Action History
- Created by: funtasma16 | 2021-03-09T21:55:59+00:00
- Closed at: 2022-07-19T19:46:41+00:00
