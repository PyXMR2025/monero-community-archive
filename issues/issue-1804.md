---
title: 'turtlecoin GPU mining not starting up. '
source_url: https://github.com/xmrig/xmrig/issues/1804
author: Therealjosephchrzempiec
assignees: []
labels: []
created_at: '2020-08-09T05:25:02+00:00'
updated_at: '2020-08-28T16:29:07+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:29:07+00:00'
---

# Original Description
Hello I finally got CPU mining working great thank you to all the help from this great community. I was originally trying to get GPU mining but i couldn't so i only did CPU mining. However i would love to get GPU mining working. 
These are the  steps i took to install.

sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig-cuda.git
mkdir xmrig-cuda/build
cd xmrig-cuda/build
cmake .. -DCUDA_LIB=/usr/local/cuda/lib64/stubs/libcuda.so -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda
make -j$(nproc)

After i did that i went to https://xmrig.com/wizard to build the config file so i did that and i made a config file problem is in ubuntu i don't know how to start xmrig from commandline. I normally do things from the desktop in program. So i have no clue how to start the program from terminal Can someone please help me with that.

If i go into the normally xmrig/build folder and i do the command ./xmrig -a argon2/chukwa --threads=3 --api-port 3335 --api-worker-id i76700 -o trtl.pool.mine2gether.com:3335 -u mywallet -p gtx1060 -k i can get that to work for cpu mining.  But if i go into the xmrig-cuda/build folder give ./xmrig --donate-level 1 --no-cpu --cuda -o trtl.pool.mine2gether.co:3335 -u mywallet -p GTX1080 -k -a argon2/chukwa it gives me a error saying  No such file or directory.  Can some one help me to figure this out please why i can not start a gpu for xmrig?


Joseph

# Discussion History
## SChernykh | 2020-08-09T19:16:12+00:00
Argon2 is supported only for CPU, there is no OpenCL or CUDA code for it in XMRig.

## Therealjosephchrzempiec | 2020-08-09T19:38:11+00:00
Hello thank you. I finally stuck with cpu mining using the xmrig.


Joseph

# Action History
- Created by: Therealjosephchrzempiec | 2020-08-09T05:25:02+00:00
- Closed at: 2020-08-28T16:29:07+00:00
