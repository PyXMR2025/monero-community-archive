---
title: Add build instructions for ArchLinux
source_url: https://github.com/xmrig/xmrig/issues/776
author: ordtrogen
assignees: []
labels:
- review later
created_at: '2018-10-04T14:21:24+00:00'
updated_at: '2023-05-05T22:18:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
ArchLinux, verified on Manjaro 

Minimal version:

sudo pacman -S base-devel cmake 
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build && cd $_
cmake .. -DWITH_HTTPD=OFF
make

In order to use the web API, you need to add the libmicrohttpd package to the pacman command and omit the option -DWITH_HTTPD=OFF from cmake


# Discussion History
## k0ste | 2018-10-05T01:44:47+00:00
If you on ArchLinux is enough to just run build from [aur/xmrig](https://aur.archlinux.org/packages/xmrig): `yaourt -S xmrig`.

## ordtrogen | 2018-12-03T02:06:03+00:00
Yaourt appears to be discontinued. On the page: 
https://wiki.archlinux.org/index.php/AUR_helpers

![image](https://user-images.githubusercontent.com/15184875/49348871-43f70180-f6a8-11e8-8517-2d11cc5dc3ea.png)



## k0ste | 2018-12-28T04:36:02+00:00
@ordtrogen It's just a wrapper. Still works perfect.

## SlowestTurtle | 2019-05-13T22:54:50+00:00
You saved my life.

## ki9us | 2022-02-10T17:17:54+00:00
I also needed `hwloc` to run cmake. 

```
sudo pacman -S hwloc
```

source: #1085

## fredy44 | 2023-05-05T22:18:22+00:00
hello how can i start it after compilling


# Action History
- Created by: ordtrogen | 2018-10-04T14:21:24+00:00
