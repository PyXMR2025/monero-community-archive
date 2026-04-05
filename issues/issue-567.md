---
title: 'libmicrohttpd.so.10: cannot open shared object file: No such file or directory'
source_url: https://github.com/xmrig/xmrig/issues/567
author: wsm3
assignees: []
labels: []
created_at: '2018-04-20T03:32:21+00:00'
updated_at: '2018-11-05T13:28:32+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:28:32+00:00'
---

# Original Description
Hi!

```
root@server:~//xmrig/build# ./xmrig
./xmrig: error while loading shared libraries: libmicrohttpd.so.10: cannot open shared object file: No such file or directory
```


What is the problem?

# Discussion History
## k0ste | 2018-04-20T07:23:26+00:00
Obviously `libmicrohttpd` is updated, so you should rebuild your `xmrig`.

## rexsllemel | 2018-07-24T18:16:20+00:00
I got same problem using kali linux but there is no error in ubuntu ,what could cause the problem? should I rebuild also the xmrig? how can it be done?

## ki9us | 2018-10-25T03:04:15+00:00
> how can it be done?

The instructions at [github.com/xmrig/xmrig/wiki/Build](https://github.com/xmrig/xmrig/wiki/Build) worked for me

# Action History
- Created by: wsm3 | 2018-04-20T03:32:21+00:00
- Closed at: 2018-11-05T13:28:32+00:00
