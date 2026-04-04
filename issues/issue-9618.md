---
title: Build failed
source_url: https://github.com/monero-project/monero/issues/9618
author: ghost
assignees: []
labels:
- more info needed
created_at: '2024-12-14T13:47:53+00:00'
updated_at: '2024-12-14T15:50:14+00:00'
type: issue
status: closed
closed_at: '2024-12-14T15:50:14+00:00'
---

# Original Description
I do everything according to the instructions, but during assembly I always get an error:

```
 implicit declaration of function 'strdup'; did you mean 'strcmp'? [-Wimplicit-function-declaration]
   60 |         elt->descURL = strdup(dev->descURL);
      |                        ^~~~~~
      |                        strcmp
/monero/external/miniupnp/miniupnpc/listdevices.c:60:22: error: assignment to 'char *' from 'int' makes pointer from integer without a cast [-Wint-conversion]
   60 |         elt->descURL = strdup(dev->descURL);
      |                      ^
```

# Discussion History
## selsta | 2024-12-14T14:17:49+00:00
Please share more information. Which OS are you using? Can you share the exact steps you used to build?

## ghost | 2024-12-14T14:37:18+00:00
I use arch,
First I installed all the necessary dependencies with the command:
`sudo pacman -Syu --needed base-devel cmake boost openssl zeromq libpgm unbound libsodium libunwind xz readline expat gtest python3 ccache doxygen graphviz qt5-tools hidapi libusb protobuf systemd`

Then I cloned the monero repository:
`git clone --recursive https://github.com/monero-project/monero`

After cloning, I going to the directory with the command:
`cd monero && git submodule init && git submodule update`

And I started building:
`make`

## selsta | 2024-12-14T15:50:14+00:00
Appears to be a duplicate of #9359.

The solution is to update the miniupnp submodule, like for example in #9367, or to use the workaround https://github.com/monero-project/monero/issues/9359#issuecomment-2308956945

# Action History
- Created by: ghost | 2024-12-14T13:47:53+00:00
- Closed at: 2024-12-14T15:50:14+00:00
