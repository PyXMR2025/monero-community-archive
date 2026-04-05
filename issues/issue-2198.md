---
title: issue after build macOS BigSur MBP 16" (AMD 5500m)
source_url: https://github.com/xmrig/xmrig/issues/2198
author: AMJ-7
assignees: []
labels: []
created_at: '2021-03-21T17:39:57+00:00'
updated_at: '2021-04-12T13:51:17+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:51:17+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

Steps to reproduce the behavior.
- building successfully but the "xmrig" can't compile GPU!

 - Miner log as text or screenshot
![Screen Shot 2021-03-21 at 5 51 44 PM](https://user-images.githubusercontent.com/931567/111914939-c0ca6700-8a7c-11eb-9146-d49f74bc5b2a.png)

 - Config file or command line (without wallets)
 - without config file

 - OS: 
 - MacOS Big Sur (lasted Version)

 - For GPU related issues: information about GPUs and driver version:
-AMD Redoen Pro 5500M 4GB




# Discussion History
## SChernykh | 2021-03-22T09:59:51+00:00
If you google `cvms_element_build_from_source` you'll see it has been a common problem with MacOS OpenCL for a long time, not only with XMRig. OpenCL support is very bad on MacOS.

## AMJ-7 | 2021-03-22T13:51:24+00:00
> If you google `cvms_element_build_from_source` you'll see it has been a common problem with MacOS OpenCL for a long time, not only with XMRig. OpenCL support is very bad on MacOS.

but Ethminer working well!
https://github.com/ethereum-mining/ethminer/releases/download/v0.18.0/ethminer-0.18.0-cuda-9-darwin-x86_64.tar.gz

## SChernykh | 2021-03-22T14:02:51+00:00
ETH is a different algorithm with different code, also you gave a link to CUDA version, how does it work on your AMD GPU?

## AMJ-7 | 2021-03-22T14:05:34+00:00
> ETH is a different algorithm with different code, also you gave a link to CUDA version, how does it work on your AMD GPU?

>Ethereum miner with OpenCL, CUDA and stratum support

look: https://github.com/ethereum-mining/ethminer

## SChernykh | 2021-03-22T14:17:07+00:00
ETH is not Kawpow though, Kawpow is much more complex. MacOS OpenCL driver is unreliable and can fail at compiling different code. The error it printed (`cvms_element_build_from_source`) is a bug in driver, not a problem with the source code.

## AMJ-7 | 2021-03-22T17:25:51+00:00
no, I don't think the bug in the `OpenCL` driver, see this article shows how error after building `Xmrig` and how has fix print the GPU devices:

https://s4m0ht.medium.com/how-to-mine-monero-on-your-macbook-and-tweak-the-source-code-although-you-shouldnt-8d57d966ac26

## SChernykh | 2021-03-22T17:36:56+00:00
The error described in that article is totally unrelated.

# Action History
- Created by: AMJ-7 | 2021-03-21T17:39:57+00:00
- Closed at: 2021-04-12T13:51:17+00:00
