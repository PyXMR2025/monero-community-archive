---
title: Centos 8 build instructions
source_url: https://github.com/xmrig/xmrig/issues/1484
author: coinmaster-svg
assignees: []
labels: []
created_at: '2020-01-04T17:24:17+00:00'
updated_at: '2020-05-08T07:38:11+00:00'
type: issue
status: closed
closed_at: '2020-01-11T06:39:03+00:00'
---

# Original Description
sudo dnf install -y epel-release
sudo yum config-manager --set-enabled PowerTools
sudo dnf install -y https://extras.getpagespeed.com/release-el8-latest.rpm
sudo dnf install -y libuv-static
sudo dnf install -y git make cmake gcc gcc-c++ libstdc++-static hwloc-devel openssl-devel
git clone https://github.com/xmrig/xmrig.git
cd xmrig && mkdir build && cd build
cmake .. -DUV_LIBRARY=/usr/lib64/libuv.a
make


# Discussion History
## nullgenome | 2020-01-05T14:26:36+00:00
thanks for this, the two lines:
 
> sudo yum config-manager --set-enabled PowerTools
> sudo dnf install -y https://extras.getpagespeed.com/release-el8-latest.rpm

proved to be the fixer for me!

## xmrig | 2020-01-11T06:39:03+00:00
Docs updated https://xmrig.com/docs/miner/centos8-build
Thank you.

## jimchun | 2020-05-08T07:38:10+00:00
$ sudo dnf install -y git make cmake gcc gcc-c++ libstdc++-static hwloc-devel openssl-devel libuv-static
Last metadata expiration check: 0:00:16 ago on Fri 08 May 2020 07:36:18 AM UTC.


Package git-2.18.2-2.el8_1.x86_64 is already installed.
Package make-1:4.2.1-9.el8.x86_64 is already installed.
=======================================================================
Some packages in your transaction are brought to you by GetPageSpeed: 
 - libuv-static-1:1.37.0-1.el8.x86_64
 - libuv-1:1.37.0-1.el8.x86_64
 - libuv-devel-1:1.37.0-1.el8.x86_64
To enable package installs, subscribe using the following link:

https://www.getpagespeed.com/repo-subscribe?server_ip=52.168.104.38
=======================================================================

what is going on ???? centOS8

# Action History
- Created by: coinmaster-svg | 2020-01-04T17:24:17+00:00
- Closed at: 2020-01-11T06:39:03+00:00
