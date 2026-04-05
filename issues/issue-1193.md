---
title: Problem with NUMA Support on Intel(R) Xeon(R) CPU E5-2680 v2
source_url: https://github.com/xmrig/xmrig/issues/1193
author: latency0ms
assignees: []
labels:
- bug
created_at: '2019-09-23T22:06:36+00:00'
updated_at: '2021-05-10T19:08:41+00:00'
type: issue
status: closed
closed_at: '2019-11-15T07:26:17+00:00'
---

# Original Description
As described in https://github.com/xmrig/xmrig/issues/1111#issuecomment-534121523 I have some issues with NUMA support on my dual Intel(R) Xeon(R) CPU E5-2680 v2 rig.

NAME="Ubuntu"
VERSION="18.04.2 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.2 LTS"
VERSION_ID="18.04"

[topology.txt](https://github.com/xmrig/xmrig/files/3644329/topology.txt)

[lscpu.txt](https://github.com/xmrig/xmrig/files/3644340/lscpu.txt)

Thank you for your support. 

# Discussion History
## xmrig | 2019-09-24T09:19:26+00:00
It very strange according topology and lscpu miner generate perfect configuration.

Use tools like `htop` to verify miner really use first 20 cores if this OK, try run miner only on one CPU, check hashrate, run 2 instances, etc.

1. `./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 --cpu-affinity 0x3FF` (cores 0-9, first CPU)
2. `./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 --cpu-affinity 0xFFC00` (cores 10-19, second CPU)
3. `./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 --cpu-affinity 0x3FF00000` (cores 20-29, first CPU)
4. `./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 --cpu-affinity 0xFFC0000000` (cores 30-39, second CPU)

`sudo` not required I also omit other useless for test options.
Use command `sensors` from lm-sensors package, temperatures helps understand real CPUs load.

Last resort use numactl:

1. `numactl -N 0 -m 0 ./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10` (first CPU).
2. `numactl -N 1 -m 1 ./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10` (second CPU)

## latency0ms | 2019-09-24T09:50:03+00:00
I can confirm that with `./xmrig -a rx/test -o stratum+tcp://randomx-benchmark.xmrig.com:7777 -k -r 5 --asm=AUTO --donate-level=1 --print-time=5 --log-file=/var/log/xmrig_rxtest.log` all 20 Cores are being used:

![2019-09-24_112404](https://user-images.githubusercontent.com/55700671/65499565-1e004f00-debe-11e9-9b2d-9872ee7172ed.png)
![2019-09-24_112440](https://user-images.githubusercontent.com/55700671/65499661-41c39500-debe-11e9-8e47-815a531416ab.png)

Option 1 (./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 --cpu-affinity 0x3FF (cores 0-9, first CPU))
![2019-09-24_113053](https://user-images.githubusercontent.com/55700671/65500063-f5c52000-debe-11e9-9021-dad7e865c9ac.png)
![2019-09-24_113117](https://user-images.githubusercontent.com/55700671/65500074-f958a700-debe-11e9-86ef-44c997695f0c.png)

Option 2 (./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 --cpu-affinity 0xFFC00 (cores 10-19, second CPU))
![2019-09-24_113404](https://user-images.githubusercontent.com/55700671/65500279-5a807a80-debf-11e9-8d82-45d1b460d03a.png)
![2019-09-24_113431](https://user-images.githubusercontent.com/55700671/65500283-5c4a3e00-debf-11e9-80fc-660442c579ad.png)

Option 3 (./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 --cpu-affinity 0x3FF00000 (cores 20-29, first CPU))
![2019-09-24_113748](https://user-images.githubusercontent.com/55700671/65500642-e4304800-debf-11e9-9764-b3a884993eb7.png)
![2019-09-24_113815](https://user-images.githubusercontent.com/55700671/65500719-01651680-dec0-11e9-91ca-10a910828c2d.png)

Option 4 (./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 --cpu-affinity 0xFFC0000000 (cores 30-39, second CPU))
![2019-09-24_114204](https://user-images.githubusercontent.com/55700671/65500977-6caee880-dec0-11e9-92e8-e64b5c505b54.png)
![2019-09-24_114217](https://user-images.githubusercontent.com/55700671/65500985-6fa9d900-dec0-11e9-9785-58b298c73f83.png)

numactl -N 0 -m 0 ./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 (first CPU).
![2019-09-24_114532](https://user-images.githubusercontent.com/55700671/65501249-ed6de480-dec0-11e9-97c3-698b54951119.png)
![2019-09-24_114550](https://user-images.githubusercontent.com/55700671/65501254-f068d500-dec0-11e9-8414-05e2ad57c841.png)

numactl -N 1 -m 1 ./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 10 (second CPU)
![2019-09-24_114823](https://user-images.githubusercontent.com/55700671/65501433-4b023100-dec1-11e9-93e0-3d7fa669b200.png)
![2019-09-24_114840](https://user-images.githubusercontent.com/55700671/65501439-4dfd2180-dec1-11e9-9d8c-1d74553f4e32.png)





## xmrig | 2019-09-24T10:41:41+00:00
DDR3 memory is bottleneck, you should use at least 4 modules for 4 channel memory mode, DDR3 memory is limited to about 1500-2000 H/s per channel, sorry I missed that part where you mention only 2 modules.

`./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 1 --cpu-affinity 0x1` (just one thread) will show you maximum possible hashrate per core if you have enough memory channels.

## latency0ms | 2019-09-24T10:54:26+00:00
This makes sense, yes! I will get another 2 sticks of the same Memory and test again; I'll keep you posted.

Using `./xmrig -o randomx-benchmark.xmrig.com:7777 --randomx-no-numa --threads 1 --cpu-affinity 0x1` gives me 412 H/s 
![image](https://user-images.githubusercontent.com/55700671/65507669-b1da1700-dece-11e9-8dee-c734147db50c.png)

Multiplied by 20 I should get about 8240 H/s with 4 DDR3 8192 MB sticks.




## pawelantczak | 2019-11-06T10:20:42+00:00
@latency0ms did you manage to add more ram? Can you share your last results?

## latency0ms | 2019-11-06T12:15:54+00:00
Yes, I now have 32GB of memory installed.

With `./xmrig -a rx/test -o stratum+tcp://randomx-benchmark.xmrig.com:7777 -k -r 5│--asm=intel --print-time=5 --log-file=/var/log/xmrig_rxtest.log`

I am getting:

![image](https://user-images.githubusercontent.com/55700671/68297517-6901aa80-0097-11ea-83f2-d5bde493453e.png)



## coolhaircut | 2021-05-10T19:08:41+00:00
The E5 Xeons have weird affinities like this to try to make sure the workload is split evenly in dual sockets if you just specify the first half of the cores. So for a 2x 20 core CPUs, specifying 0-19 would recruit 0-9 from cpu1 and 10-19 from cpu2.

`CPU1: 0-9, 20-29`
`CPU2: 10-19,30-39`

To override this, just manually declare the cores in the `cpu` part of the config for your algo. So to use 100% cpu1 and 0% cpu2 on Randomx, set the config to this:

`"cpu":{"rx/0":[0,1,2,3,4,5,6,7,8,9,20,21,22,23,24,25,26,27,28,29]}`

# Action History
- Created by: latency0ms | 2019-09-23T22:06:36+00:00
- Closed at: 2019-11-15T07:26:17+00:00
