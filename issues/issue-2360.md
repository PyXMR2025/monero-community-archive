---
title: Enable docker container to be run headlessly
source_url: https://github.com/monero-project/monero/issues/2360
author: levino
assignees: []
labels: []
created_at: '2017-08-27T10:03:42+00:00'
updated_at: '2017-08-28T08:11:37+00:00'
type: issue
status: closed
closed_at: '2017-08-28T08:11:37+00:00'
---

# Original Description
See [this issue first](https://github.com/monero-project/monero/issues/1598)

So one can only run the docker image in "interactive" mode. If not it fails with non comprehensible errors.

One should make sure that the docker container also runs headlessly.

# Discussion History
## moneromooo-monero | 2017-08-27T11:08:05+00:00
To run as a (non interactive) daemon, use --detach.


## levino | 2017-08-27T13:08:36+00:00
Still it feels wrong to have to use `docker run -i` or `stdin_open: true` in docker compose, to keep STDIN open even if not attached. Why is this necessary? No other daemon docker container that I know of has this requirement...

## moneromooo-monero | 2017-08-27T18:10:55+00:00
I have no idea about docker, so I can't answer that.

## MoroccanMalinois | 2017-08-28T01:01:41+00:00
> No other daemon docker container that I know of has this requirement...

@Levino : I'll bet than none of these daemons have a console for humans to interact with them

"Interactive" option in docker means "Keep STDIN open even if not attached".
It's distinct from the idea of foreground/background mode. So the docker container **can** run headlessly. For that, it's the docker option "-d". So, one can do : 

    docker run -i -d ....

(monerod **must not** use --detach when used inside docker)

JFTR, i've been using docker for monero for more than a year now (and on multiple hosts). Never had any pb, but i've only used mounted volumes for the data-dir. Otherwise, Docker uses [AUFS](https://en.wikipedia.org/wiki/Aufs), which doesn't look great to combine with lmdb. 


## MoroccanMalinois | 2017-08-28T01:51:11+00:00
Alternatively, there is also the option `--non-interactive` in monerod, so that it doesn't need to be activated at docker's level. 

    docker run -d monero monerod --non-interactive

Here is an example with opened ports and using a mounted volume

    docker run -d  -p 18080:18080 -p 127.0.0.1:18081:18081 -v /host/path/to/data/dir:/root/.bitmonero monero monerod --rpc-bind-ip=0.0.0.0 --confirm-external-bind --non-interactive


## levino | 2017-08-28T08:11:37+00:00
Starting monerod non-interactively makes the most sense for me. Will overwrite the entrypoint. Thanks for clarification. Closing this issue.

# Action History
- Created by: levino | 2017-08-27T10:03:42+00:00
- Closed at: 2017-08-28T08:11:37+00:00
