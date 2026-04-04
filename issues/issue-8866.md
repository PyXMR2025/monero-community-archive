---
title: Dockerfile not work.
source_url: https://github.com/monero-project/monero/issues/8866
author: ivose
assignees: []
labels: []
created_at: '2023-05-20T05:54:10+00:00'
updated_at: '2023-06-06T01:07:54+00:00'
type: issue
status: closed
closed_at: '2023-06-06T01:07:54+00:00'
---

# Original Description
How to use with Docker???



```
 => [stage-1 2/4] RUN set -ex &&     apt-get update &&     apt-get --no-install-recommends --yes install ca-certificates &&     apt-get clean &&     116.8s 
 => [builder 2/5] RUN set -ex &&     apt-get update &&     DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends --yes install     automak  317.8s 
 => [builder 3/5] WORKDIR /src                                                                                                                         0.1s 
 => [builder 4/5] COPY . .                                                                                                                             0.1s 
 => ERROR [builder 5/5] RUN set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -  1.2s 
------
 > [builder 5/5] RUN set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) depends target=x86_64-linux-gnu ;     else make -j$NPROC depends target=x86_64-linux-gnu ;     fi:
#0 1.089 + git submodule init
#0 1.152 fatal: not a git repository (or any of the parent directories): .git
------
failed to solve: process "/bin/sh -c set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z \"$NPROC\" ] ;     then make -j$(nproc) depends target=x86_64-linux-gnu ;     else make -j$NPROC depends target=x86_64-linux-gnu ;     fi" did not complete successfully: exit code: 128
PS C:\mylaptop\cpp>
```

# Discussion History
## selsta | 2023-05-20T21:41:20+00:00
You have to clone the repository with git.

# Action History
- Created by: ivose | 2023-05-20T05:54:10+00:00
- Closed at: 2023-06-06T01:07:54+00:00
