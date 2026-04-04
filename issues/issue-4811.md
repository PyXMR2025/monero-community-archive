---
title: Dockerfile is broken
source_url: https://github.com/monero-project/monero/issues/4811
author: korjavin
assignees: []
labels: []
created_at: '2018-11-06T13:55:33+00:00'
updated_at: '2018-11-06T17:25:54+00:00'
type: issue
status: closed
closed_at: '2018-11-06T17:25:54+00:00'
---

# Original Description
there is the log of building from Dockerfile

[build_10_step_104_container_0.txt](https://github.com/monero-project/monero/files/2553406/build_10_step_104_container_0.txt)


# Discussion History
## moneromooo-monero | 2018-11-06T14:14:54+00:00
Do you have docker 17.05 or more recent?

## korjavin | 2018-11-06T14:26:58+00:00
Yes,
on Circle-ci:
Docker version 18.06.1-ce, build e68fc7a
and now I am also trying to build on docker hub




## korjavin | 2018-11-06T15:14:09+00:00
Yes. the same problem with dockehub
https://hub.docker.com/r/korjavin/docker-monero-node/builds/b6a5xfsg7e94d69unqnefdk/

## xiphon | 2018-11-06T15:31:30+00:00
Clone full monero repo with all its contents, not just a Dockerfile.

## korjavin | 2018-11-06T17:25:54+00:00
Fuh, I had the wrong impression that Dockerfile is enough

# Action History
- Created by: korjavin | 2018-11-06T13:55:33+00:00
- Closed at: 2018-11-06T17:25:54+00:00
