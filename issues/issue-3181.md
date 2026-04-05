---
title: trying to mine on ArcoLinux
source_url: https://github.com/xmrig/xmrig/issues/3181
author: abe-danger
assignees: []
labels: []
created_at: '2022-12-16T21:14:57+00:00'
updated_at: '2025-06-18T22:49:17+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:49:17+00:00'
---

# Original Description
Hello, first timer on GitHub here, been using ArcoLinux (an Arch based OS) for the past while on a secondary system and I would like to mine on it, because I heard mining on linux is way better than on windows, however, when configuring the config file, it keeps giving me the error "/usr/bin/config.json<line:1, position:1>: "Invalid value.""
config files used (copied as .txt since .json doesnt work):


[config.txt](https://github.com/xmrig/xmrig/files/10249412/config.txt)
[config2.txt](https://github.com/xmrig/xmrig/files/10249413/config2.txt)
![ArcoLinux_2022-12-16_22-11-54](https://user-images.githubusercontent.com/120753787/208190064-5267e8c8-4b9c-4679-9397-f25ba965265a.png)

I hope you guys can help me out so I can help decentralize the network just that tiny bit more. :)

# Discussion History
## SChernykh | 2022-12-16T23:01:52+00:00
Your `/usr/bin/config.json` is not for xmrig because it starts with `[`. You need to put the real config.json in the same folder as xmrig.

## abe-danger | 2022-12-17T09:41:09+00:00
the config file is already in the same folder as xmrig, with a copied version in /usr/bin/ and both dont begin with a [

## SChernykh | 2022-12-17T10:13:34+00:00
The screenshot says otherwise. The line:1, position:1 of /usr/bin/config.json is `[` - read the text there. It show the position of error with `^` symbol and it points on line above it.

## abe-danger | 2022-12-17T12:33:32+00:00
Changed all possible ['s to {'s, now it's saying that the { at pos 1 is invalid.

![ArcoLinux_2022-12-17_13-31-08](https://user-images.githubusercontent.com/120753787/208242041-dbfe6002-b453-41c0-aad1-2beb8a4e135f.png)
![ArcoLinux_2022-12-17_13-32-00](https://user-images.githubusercontent.com/120753787/208242043-e3101a9c-2377-43dd-a768-5a594eb3d5b4.png)

# Action History
- Created by: abe-danger | 2022-12-16T21:14:57+00:00
- Closed at: 2025-06-18T22:49:17+00:00
