---
title: Using Chaos Mesh to enhance monero
source_url: https://github.com/monero-project/monero/issues/6742
author: zhouqiang-cl
assignees: []
labels: []
created_at: '2020-08-05T05:41:00+00:00'
updated_at: '2022-02-19T04:20:36+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:20:35+00:00'
---

# Original Description
Hello, I am [Chaos Mesh](https://github.com/chaos-mesh/chaos-mesh) Maintainer. Chaos Mesh is an open-source and free Chaos Engineering platform, it can be directly used without modifying any code.

Blockchain is a very promising industry. Congratulations on doing such a promising project,  Blockchain is a subdivision that is widely used in the distributed field. For distributed system, the stability and correctness of the cluster are very important. The nodes of the blockchain may be distributed in any corner of the world. Its terminal equipment are also different and the problems that appear will be strange, such as network partitions, high node pressure, and various other failures. Blockchain programs need to ensure reliability in such an unstable state, which is a very difficult task. We felt particularly deeply about this in the testing process.

You may also have heard that chaos engineering can guarantee the stability of the system to a certain extent, especially after the system is large enough, the simulation of real faults is particularly important. You can know what situation your program is in under what circumstances. In PingCAP (PingCAP is a world-renowned open source company, its products include [TiDB](https://github.com/pingcap/tidb)/[TiKV](https://github.com/tikv/tikv) ([TiDB](https://github.com/pingcap/tidb) has a 24.5k star on GitHub. [TiKV](https://github.com/tikv/tikv) has a 7.7k star)), we use chaos engineering to find the distributed database quite a lot of bugs, some of which are recorded in https://github.com/orgs/chaos-mesh/projects/1


On December 31, 2019, we open sourced our chaos engineering platform [Chaos Mesh](https://github.com/chaos-mesh/chaos-mesh) and entered the CNCF Sandbox on July 15 this year. It is currently the industry’s leading cloud-native chaos engineering platform. Now it has 2k stars on Github. In addition to general k8s operations, it also includes a simplified dashboard that can easily perform chaos operations on the front-end page. It also includes an observable data source that integrates chaos events and services. metric combination.

At present, in addition to our own use of Chaos Mesh to enhance the stability of our TiDB, some other companies such as Xiaopeng Motors, Meituan, Youzan, Dailymotion, NetEase Fuxi Lab, JuiceFS, Apache pulsar,Youzan etc. are using Chaos Mesh to enhance system stability. In addition, we can also see some open source projects integrating Chaos Mesh as part of the test system, such as [datastax/fallout](https://github.com/datastax/fallout/pull/1)  [ethersphere/beekeeper](https://github.com/ethersphere/beekeeper/pull/22) [cncf/cnf-conformance](https://github.com/cncf/cnf-conformance/commit/b9227dd4b2262d05eb80b435d931216b084c6a42) [Experiment-catalog](https://github.com/open-chaos/experiment-catalog/tree/master/local/choas-mesh-turbulence) [RCNIT](https://github.com/ungurflorin/RCNIT) [Shortlink](https://github.com/batazor/shortlink) [Fdb-k8s-chaos](https://github.com/PierreZ/fdb-k8s-chaos/)

As I said before, some users have integrated Chaos Mesh as part of their test system. In the blockchain field, you can see the Ethereum official storage project ([ethersphere/beekeeper](https://github.com/ethersphere/beekeeper/pull/22) ) Use Chaos Mesh to ensure the stability of their system

In a few days ago, there is an attack in ETC(https://news.bitcoin.com/single-miner-reorgs-ethereum-classic-devs-report-a-chain-split/)  it may be caused by a network partition. If it is, then this kind of scenario can be simulated by Chaos Mesh

In Chaos Mesh, we have many injection functions, such as pod/container kill, network partition, network interruption, CPU/memory usage, time rollback, disk failure, etc.

Welcome to use Chaos Mesh to enhance the stability of monero. It is opensource and free.  If you have any questions, or submit an issue at https://github.com/chaos-mesh/chaos-mesh, or send me an email zhouqiang@pingcap. com

Sorry for disturb

# Discussion History
## moneromooo-monero | 2020-08-05T12:25:57+00:00
In theory, it looks like an interesting thing to use.

## zhouqiang-cl | 2020-08-05T15:25:24+00:00
> In theory, it looks like an interesting thing to use.

Aha, I am very glad you think so. We very appreciate if you can use it
If you have any trouble in using it, feel free to contact us

Thank you very much

## selsta | 2022-02-19T04:20:35+00:00
Closing, the bug tracker isn't really the place for this suggestion / recommendation.

# Action History
- Created by: zhouqiang-cl | 2020-08-05T05:41:00+00:00
- Closed at: 2022-02-19T04:20:35+00:00
