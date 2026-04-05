---
title: Compilled binary ignore cmd arguments and want to load config file
source_url: https://github.com/xmrig/xmrig/issues/3651
author: avb1213
assignees: []
labels: []
created_at: '2025-04-13T10:38:39+00:00'
updated_at: '2025-06-18T22:38:18+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:38:18+00:00'
---

# Original Description
Hello.
I made a fresh compillation xmrig with CMAKE variables: 
cmake .. -DWITH_EMBEDDED_CONFIG=OFF -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DWITH_CN_FEMTO=OFF -DWITH_ARGON2=OFF -DWITH_KAWPOW=OFF -DWITH_GHOSTRIDER=OFF -DWITH_TLS=ON -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_HTTP=OFF -DBUILD_STATIC=OFF -DUV_LIBRARY=/home/user/deps/lib/libuv.a -DUV_INCLUDE_DIR=/home/user/deps/include -DHWLOC_LIBRARY=/home/user/deps/lib/libhwloc.a -DHWLOC_INCLUDE_DIR=/home/user/deps/include

Try to run xmrig with command line arguments:
./xmrig -o stratum://x.x.x.x:port --tls-u address -a rx/0 -k -p $HOSTNAME

and get this error:
[2025-04-13 14:23:33.121] unable to open "/user/config.json".
[2025-04-13 14:23:33.121] unable to open "/user/.xmrig.json".
[2025-04-13 14:23:33.121] unable to open "/user/.config/xmrig.json".
[2025-04-13 14:23:33.121] no valid configuration found, try https://xmrig.com/wizard
and xmrig exit.

It is posible to run xmrig with command line arguments only? 

# Discussion History
## SChernykh | 2025-04-15T09:04:12+00:00
```
./xmrig -o stratum://x.x.x.x:port --tls-u address -a rx/0 -k -p $HOSTNAME
```
You have no space between `--tls` and `-u`

## avb1213 | 2025-04-16T06:46:28+00:00
No, deal not in the space. I just typo when wrote issue). 

./xmrig -o stratum://x.x.x.x:port --tls -u address -a rx/0 -k -p $HOSTNAME
[2025-04-16 10:43:24.479] unable to open "/root/config.json".
[2025-04-16 10:43:24.479] unable to open "/root/.xmrig.json".
[2025-04-16 10:43:24.479] unable to open "/root/.config/xmrig.json".
[2025-04-16 10:43:24.479] no valid configuration found, try https://xmrig.com/wizard

# Action History
- Created by: avb1213 | 2025-04-13T10:38:39+00:00
- Closed at: 2025-06-18T22:38:18+00:00
