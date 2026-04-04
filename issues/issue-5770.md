---
title: Cannot run compiled binaries on OpenBSD-current
source_url: https://github.com/monero-project/monero/issues/5770
author: The-King-of-Toasters
assignees: []
labels: []
created_at: '2019-07-22T09:33:24+00:00'
updated_at: '2019-08-19T22:35:42+00:00'
type: issue
status: closed
closed_at: '2019-08-19T22:35:42+00:00'
---

# Original Description
When compiling on OpenBSD-current, I found that none of the programs in `bin` will run.
Steps to reproduce:

```sh
doas pkg_add cmake gmake zeromq cppzmq libiconv boost git
git clone https://github.com/monero-project/monero --recursive
cd monero
git checkout v0.14.1.2
ulimit -d 2000000
env DEVELOPER_LOCAL_TOOLS=1 BOOST_ROOT=/usr/local gmake release-static
./build/OpenBSD/_HEAD_detached_at_v0.14.1.2_/release/bin/monerod
```

Trying to run any of the binaries located at `build/build/OpenBSD/_HEAD_detached_at_v0.14.1.2_/release/bin` produces the following error:

```
./build/OpenBSD/_HEAD_detached_at_v0.14.1.2_/release/bin/monerod: syntax error: `^Q-' unexpected
```

# Discussion History
## iDunk5400 | 2019-07-22T11:20:00+00:00
#5569

# Action History
- Created by: The-King-of-Toasters | 2019-07-22T09:33:24+00:00
- Closed at: 2019-08-19T22:35:42+00:00
