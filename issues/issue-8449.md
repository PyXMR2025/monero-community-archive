---
title: 'Unable to build from source - /usr/bin/ld: (.text+0xc1): undefined reference
  to `event_base_set'''
source_url: https://github.com/monero-project/monero/issues/8449
author: rblaine95
assignees: []
labels: []
created_at: '2022-07-21T08:59:05+00:00'
updated_at: '2022-07-21T19:42:38+00:00'
type: issue
status: closed
closed_at: '2022-07-21T19:42:38+00:00'
---

# Original Description
I'm unable to build `v0.18.0.0` in my [Docker Build](https://github.com/rblaine95/docker_monero) and I'm unsure how to troubleshoot.

Build logs are available [here](https://github.com/rblaine95/docker_monero/runs/7445673300?check_suite_focus=true#step:5:4629).

Any help would be greatly appreciated.

# Discussion History
## selsta | 2022-07-21T13:31:39+00:00
See https://github.com/monero-project/monero/issues/8439

You can install `apt install libevent-dev`, and maybe some of the other libs listed in this issue and then check if it builds correctly.

Also ping @sethforprivacy since you also had similar issues with docker.

## sethforprivacy | 2022-07-21T13:53:55+00:00
> I'm unable to build `v0.18.0.0` in my [Docker Build](https://github.com/rblaine95/docker_monero) and I'm unsure how to troubleshoot.
> 
> Build logs are available [here](https://github.com/rblaine95/docker_monero/runs/7445673300?check_suite_focus=true#step:5:4629).
> 
> Any help would be greatly appreciated.

There was a change that now requires `libunbound-dev` to be installed at compile time. You may also need to install it in your final image, as I wasn't able to get it to properly statically link anymore.

## sethforprivacy | 2022-07-21T13:56:18+00:00
This Dockerfile builds and runs properly now, see commit history for specifics: https://github.com/sethforprivacy/simple-monero-wallet-rpc-docker/blob/main/Dockerfile

## selsta | 2022-07-21T13:58:45+00:00
@sethforprivacy this is how you would have to compile unbound to get proper static binaries: https://github.com/monero-project/monero-gui/pull/3696/files

## sethforprivacy | 2022-07-21T14:02:54+00:00
> @sethforprivacy this is how you would have to compile unbound to get proper static binaries: https://github.com/monero-project/monero-gui/pull/3696/files

Ah, that's not bad at all! Will explore that shortly. Thanks!

## sethforprivacy | 2022-07-21T14:30:41+00:00
Working on it now: https://github.com/sethforprivacy/simple-monerod-docker/pull/61

## rblaine95 | 2022-07-21T19:42:38+00:00
Build seems to be working now, thank you @selsta and @sethforprivacy 🎉

# Action History
- Created by: rblaine95 | 2022-07-21T08:59:05+00:00
- Closed at: 2022-07-21T19:42:38+00:00
