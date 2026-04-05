---
title: XMR Static compile issue.
source_url: https://github.com/xmrig/xmrig/issues/564
author: xmrguy
assignees: []
labels: []
created_at: '2018-04-19T18:43:37+00:00'
updated_at: '2018-11-21T02:04:54+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:30:27+00:00'
---

# Original Description
I can't still understand how to make a fully static bin .
My OS is Ubuntu 16.04 , could someone help me ?

# Discussion History
## dunklesToast | 2018-04-21T17:33:56+00:00
### Prepare
First you need to install all dependencies:
`sudo apt-get instal build-essential cmake libuv1-dev libmicrohttpd-dev`

You can leave `libmicrohttpd-dev` if you do not need the API.
After you installed these, `cd` in your xmrig Folder (where you have the source code) and create a directory called `build`
```sh
mkdir build
cd build
```

### Configure
Then you need to compile the xmrig Source code using this command:
With API:
`cmake .. -DUV_LIBRARY=<path to libuv> -DMHD_LIBRARY=<path to microhttpd>`

Without API:
`cmake .. -DUV_LIBRARY=<path to libuv> -DWITH_HTTPD=OFF`

The default paths are:

|      Library      |  Path |
|:-------------:|:------:|
|  libuv | /usr/lib/x86_64-linux-gnu/libuv.a |
|    libmicrohttpd   |   /usr/lib/x86_64-linux-gnu/libmicrohttpd.a |


If you can't find the librarys there, search them:
libuv: `ldconfig -p | grep libuv`
libmicrohttpd: `ldconfig -p | grep libmicrohttpd`

You should get output like this:
`libmicrohttpd.so (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libmicrohttpd.so`
Just take the path at the end and change the `.so` to `.a`

### Build
After the cmake ran successfully, simply type `make` and hit enter. It should now compile your miner!



I hope that helped you!

## xmrguy | 2018-04-22T18:49:03+00:00
First of all thank you really much for your time & help.
I tried this method but i can't still get it Fully Static:
`file xmrig `
`xmrig: ELF 64-bit LSB executable, x86-64, version 1 `(GNU/Linux),` dynamically linked, interpreter /lib/ld64.so.1, for GNU/Linux 2.6.32, BuildID[sha1]=c6ee8b905e955fd800380641d277b050dcf76e8e, stripped`


Also ldd shows still a lot of library which uses.


## M0x65 | 2018-11-21T02:04:54+00:00
https://github.com/M0x65/xmrig-portable fully static / portable miner here!

# Action History
- Created by: xmrguy | 2018-04-19T18:43:37+00:00
- Closed at: 2018-11-05T13:30:27+00:00
