---
title: 'Cannot get xmrig to allocate all CPUs and threads '
source_url: https://github.com/xmrig/xmrig/issues/1608
author: Ogden-Morrow
assignees: []
labels: []
created_at: '2020-03-25T17:12:27+00:00'
updated_at: '2020-08-28T16:32:31+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:32:31+00:00'
---

# Original Description
I have a VM with 48x Intel Xeon E5-2670 running at 2.5 GHz.

The miner allocates 24C/48T on NUMA 1. (CentOS)
I've altered the boot allocation of CPU on the server.
I tried specifying the exact amount on the CLI.
It allocates the same every time. 1gb pages is also enabled on the vm, but xmrig says its unsupported.

I know I'm probably missing something. When I try to use a .json config I get the same thing and/or an error I know is the result of my faulty formatting. This is my last attempt. I've exhausted the recommendations when I google the problems. 

Please advise, kindly.
[cpu hashrate.txt](https://github.com/xmrig/xmrig/files/4382367/cpu.hashrate.txt)
![NPROC   XMRIG](https://user-images.githubusercontent.com/62663947/77565203-416e7b80-6e9a-11ea-995e-6f1a63c38a3d.PNG)
![XMRIG START](https://user-images.githubusercontent.com/62663947/77565205-416e7b80-6e9a-11ea-9be1-647de6c981c4.PNG)




# Discussion History
# Action History
- Created by: Ogden-Morrow | 2020-03-25T17:12:27+00:00
- Closed at: 2020-08-28T16:32:31+00:00
