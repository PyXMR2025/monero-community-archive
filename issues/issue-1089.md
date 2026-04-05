---
title: 2.90.{2|3}-beta SEGV
source_url: https://github.com/xmrig/xmrig/issues/1089
author: paulpas
assignees: []
labels:
- need feedback
created_at: '2019-07-31T15:31:09+00:00'
updated_at: '2019-08-05T15:41:43+00:00'
type: issue
status: closed
closed_at: '2019-08-05T15:41:43+00:00'
---

# Original Description
Ubuntu 18.04LTS Ryzen 5 3600 but compiling on an i5-2410M is fine.

```
VERSION=v2.99.3-beta
git clone https://github.com/xmrig/xmrig.git
cd xmrig
git checkout $VERSION
mkdir bin
cd bin
cmake ..
make
```

Running via systemd
```
accepted (2/0) diff 75000 (123 ms)
accepted (3/0) diff 75000 (119 ms)
accepted (4/0) diff 75000 (118 ms)
new job from loki.pool.mine2gether.com:3331 diff 112501 algo rx/loki height 326404
speed 10s/60s/15m 6325.5 n/a n/a H/s max 6326.1 H/s
xmrig.service: Main process exited, code=killed, status=11/SEGV
xmrig.service: Failed with result 'signal'.
```

Running on the CLI
```
Jul 31 14:32:03 node-10-255-254-118 kernel: traps: xmrig[4379] trap invalid opcode ip:7efbff668b9d sp:7efb39dfed60 error:0
Jul 31 14:32:03 node-10-255-254-118 kernel: traps: xmrig[4378] general protection ip:5655557351db sp:7efb3abfed48 error:0
Jul 31 14:32:03 node-10-255-254-118 kernel:  in xmrig[565555553000+312000]
```

# Discussion History
## SChernykh | 2019-08-01T08:33:59+00:00
Does 2.90.1 work fine for you? And 2.90.2/3 crashes on Ryzen 5 3600 but works fine on i5-2410M, did I get it right?

## paulpas | 2019-08-05T15:41:41+00:00
You can close this.  It ended up being related to the overclocking that I had setup.


# Action History
- Created by: paulpas | 2019-07-31T15:31:09+00:00
- Closed at: 2019-08-05T15:41:43+00:00
