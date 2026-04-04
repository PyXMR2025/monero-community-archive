---
title: 'Error : Segmentation fault in private testnet'
source_url: https://github.com/monero-project/monero/issues/8821
author: 19231224lhr
assignees: []
labels: []
created_at: '2023-04-11T04:38:59+00:00'
updated_at: '2023-06-06T01:09:22+00:00'
type: issue
status: closed
closed_at: '2023-06-06T01:09:22+00:00'
---

# Original Description
These days I'm learning Monero and try to study how to use private testnet, I found an example by [moneroexamples](https://github.com/moneroexamples) which is https://github.com/moneroexamples/private-testnet.
By its steps, I start to develop a private testnet(No data syncing is required since this is a private test network).But I met some questions, Here are the details.

### First, I Created two wallets:
`wallet01`：
```shell
monero-wallet-cli --testnet --generate-new-wallet ~/testnet/wallet_01.bin  --restore-deterministic-wallet --electrum-seed="sequence atlas unveil summon pebbles tuesday beer rudely snake rockets different fuselage woven tagged bested dented vegan hover rapid fawns obvious muppet randomly seasons randomly" --password "" --log-file ~/testnet/wallet_01.log;
```
its address is : `9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8`
`wallet02`：
```shell
monero-wallet-cli --testnet --generate-new-wallet ~/testnet/wallet_02.bin  --restore-deterministic-wallet --electrum-seed="deftly large tirade gumball android leech sidekick opened iguana voice gels focus poaching itches network espionage much jailed vaults winter oatmeal eleven science siren winter" --password "" --log-file ~/testnet/wallet_02.log;
```
its address is : `9wq792k9sxVZiLn66S3Qzv8QfmtcwkdXgM5cWGsXAPxoQeMQ79md51PLPCijvzk1iHbuHi91pws5B7iajTX9KTtJ4bh2tCh`

So I get two wallets: `wallet_01` and `wallet_02`, Then exit.

### Second, I started two nodes, using:
```shell
monerod --testnet --no-igd --hide-my-port --data-dir ~/testnet/node_01 --p2p-bind-ip 127.0.0.1 --log-level 1 --add-exclusive-node 127.0.0.1:38080  --fixed-difficulty 50 --disable-rpc-ban
```
and
```shell
monerod --testnet --p2p-bind-port 38080 --rpc-bind-port 38081 --zmq-rpc-bind-port 38082 --no-igd --hide-my-port  --log-level 1 --data-dir ~/testnet/node_02 --p2p-bind-ip 127.0.0.1 --add-exclusive-node 127.0.0.1:28080 --fixed-difficulty 50 --disable-rpc-ban
```
So I get two nodes, like this:
`node1`
![image](https://user-images.githubusercontent.com/70199004/231055679-90d154e9-6431-4228-ae00-ab8312053b22.png)
![image](https://user-images.githubusercontent.com/70199004/231055706-e883356c-1229-46fa-a321-2ef8e2e5a84c.png)
`node2`
![image](https://user-images.githubusercontent.com/70199004/231055773-32e77300-020b-4dfc-b711-871460548e05.png)
![image](https://user-images.githubusercontent.com/70199004/231055811-fbe10861-6525-473f-9a98-761e0f814082.png)

### Third, I restart two wallets to connect to nodes:
```shell
monero-wallet-cli --testnet --trusted-daemon --wallet-file ~/testnet/wallet_01.bin --password '' --log-file ~/testnet/wallet_01.log
```
and
```shell
monero-wallet-cli --testnet --daemon-port 38081 --trusted-daemon --wallet-file ~/testnet/wallet_02.bin --password '' --log-file ~/testnet/wallet_02.log
```
However, it will report an Error:`Segmentation fault (core dumped)`
Left is node's and Right is wallet's.
![image](https://user-images.githubusercontent.com/70199004/231056116-08991913-cb1c-4454-931d-919b0f9d426e.png)
the second node has the same error.
But if I restart the node, There has no error and the wallet can connect to the node:
![image](https://user-images.githubusercontent.com/70199004/231056295-a75570ea-cb64-4c0e-9862-6c8aeaa3953a.png)

### Mining also has an error
But then,I want to mine some money to transfer.I use the example's code:
```shell
start_mining 9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8 1
```
However, It also has an error:
`Wrong address prefix: 53, expected 18 or 19 or 42. Segmentation fault (core dumped)`
![image](https://user-images.githubusercontent.com/70199004/231056562-18473424-9342-47c0-bea2-39d8a3693e62.png)
The second node has the same error.

I dont know how to solve this problem as a new beginner. Thanks for your answer.
My computer is Ubuntu20.04.

# Discussion History
## plowsof | 2023-04-11T09:00:20+00:00
enabling background mining wasn't the issue. user is going to sync a testnet node and just try to start_mining to remove doubts  (perhaps its a hardware/resource issue of the virtual machine)

## selsta | 2023-04-11T10:50:43+00:00
Start `monerod` in `gdb` to get a backtrace from the crash. Do you know how to do that or should I post more detailed instructions?

## 19231224lhr | 2023-04-11T11:11:01+00:00
> Start `monerod` in `gdb` to get a backtrace from the crash. Do you know how to do that or should I post more detailed instructions?

Sorry I don't how to do that. If you can give a detailed instruction , it may be ok!

## selsta | 2023-04-11T13:39:56+00:00
Install `gdb` and start monerod with the added arguments.

```
sudo apt-get install gdb
gdb --args ./monerod --testnet --no-igd --hide-my-port --data-dir ~/testnet/node_01 --p2p-bind-ip 127.0.0.1 --log-level 1 --add-exclusive-node 127.0.0.1:38080  --fixed-difficulty 50 --disable-rpc-ban
```

Then enter

```
run
```

it should now start monerod, wait for it to crash and then enter

```
thread apply all bt
```

and post the output here.


## 19231224lhr | 2023-04-12T05:22:35+00:00
> Install `gdb` and start monerod with the added arguments.
> 
> ```
> sudo apt-get install gdb
> gdb --args ./monerod --testnet --no-igd --hide-my-port --data-dir ~/testnet/node_01 --p2p-bind-ip 127.0.0.1 --log-level 1 --add-exclusive-node 127.0.0.1:38080  --fixed-difficulty 50 --disable-rpc-ban
> ```
> 
> Then enter
> 
> ```
> run
> ```
> 
> it should now start monerod, wait for it to crash and then enter
> 
> ```
> thread apply all bt
> ```
> 
> and post the output here.

Very Thanks. I will test it.

## 19231224lhr | 2023-04-12T05:38:22+00:00
> enabling background mining wasn't the issue. user is going to sync a testnet node and just try to start_mining to remove doubts (perhaps its a hardware/resource issue of the virtual machine)

I find that it can run well in the offical testnet...
![image](https://user-images.githubusercontent.com/70199004/231360965-d3c5548d-3d85-446f-8848-58acfa77f8cd.png)


## Wolf54 | 2023-04-23T23:26:49+00:00
I am doing exactly the same what @19231224lhr does, learning monero and would like to bring up a test network. Running into the same problem. On mining start, the daemon crashes. I saw the suggestion from @selsta to run monero under gdb and post the stack trace here. Haven't seen any uploaded yet. So, I attach the gdb output I got, showing the problem. Here is what I got:

[mining-crash.log.gz](https://github.com/monero-project/monero/files/11305234/mining-crash.log.gz)

Any hints how to fix this are appreciated. Thanks!

## selsta | 2023-04-24T01:27:29+00:00
@Wolf54 In your case it's not crash like the other original issue creator, RandomX just fails to initialize. How much free RAM do you have before entering start_mining?

## Wolf54 | 2023-04-24T01:54:14+00:00
I checked with htop while two instances of monero were running, one of them under gdb.
It tells me 10.4GB used of 39GB total, so more than 28GB should be still available.

    1[|||||||||||||||                                                                            14.7%]     5[||||||||                                                                                    7.0%]
    2[|||||                                                                                       3.9%]     6[||||||||                                                                                    7.7%]
    3[||||||||                                                                                    7.1%]     7[|||||                                                                                       3.8%]
    4[||||                                                                                        2.6%]     8[||||||                                                                                      5.1%]
  Mem[|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||10.4G/39.0G]   Tasks: 254, 2067 thr; 2 running
  Swp[                                                                                        0K/20.0G]   Load average: 0.66 0.50 0.36
                                                                                                          Uptime: 1 day, 07:22:47


## selsta | 2023-04-24T01:58:23+00:00
@Wolf54 which OS are you using? Is this self compiled? If yes, can you reproduce with getmonero.org binaries?

## Wolf54 | 2023-04-24T02:08:27+00:00
@selsta This is running on a System76 Lemur Pro with Pop!_OS 22.04. I got the monero source from github and compiled it myself. I tried first a release build, which gave me the same error. Then I compiled a debug build, but no change in behavior.
I'll have to step out for today, but will try the same setup with the pre-build binaries. I have one instance running as a node on mainnet, but I am not mining on that one yet. I will respond tomorrow what the pre-build binaries produce.

## selsta | 2023-04-24T02:10:07+00:00
For some reason it fails to initialize the RandomX cache. You have enough free RAM so it shouldn't be an issue. I don't think prebuilt binaries will help but still worth a try. Have to wait until someone else can reply.

## selsta | 2023-04-24T17:07:09+00:00
Another thing you can try is compile randomx-tests and then post the output here.

https://github.com/tevador/RandomX#linux

## Wolf54 | 2023-04-24T21:52:28+00:00
I ran the same test with downloaded binaries. Same problem:

`2023-04-24 21:38:52.044 I [127.0.0.1:38080 OUT] 172 bytes sent for category command-1002 initiated by us
2023-04-24 21:38:52.044 I [127.0.0.1:37268 INC] 172 bytes sent for category command-1002 initiated by us
2023-04-24 21:38:52.044 I [127.0.0.1:38080 OUT] 172 bytes received for category command-1002 initiated by us
2023-04-24 21:38:52.044 I [127.0.0.1:37268 INC] 172 bytes received for category command-1002 initiated by us
start_mining 9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8 1
2023-04-24 21:39:36.607 I Wrong address prefix: 53, expected 18 or 19 or 42
Mining to a testnet address, make sure this is intentional!
[New Thread 0x7fff6fafe640 (LWP 2039246)]
2023-04-24 21:39:36.612 I Mining has started with 1 threads, good luck!
[New Thread 0x7fff6f5fd640 (LWP 2039247)]
[New Thread 0x7fff6edfc640 (LWP 2039248)]
[New Thread 0x7fff6e5fb640 (LWP 2039249)]

Thread 30 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fff6f5fd640 (LWP 2039247)]
0x0000555555c7e2cf in randomx_init_dataset ()
(gdb)
`
Then I ran the RandomX tests as suggested by @selsta. Here is the output:

`└─(16:42:24 on master)──> ./randomx-tests                                                                                                                                                            ──(Mon,Apr24)─┘
[ 1] Cache initialization                     ... PASSED
[ 2] SuperscalarHash generator                ... PASSED
[ 3] randomx_reciprocal                       ... PASSED
[ 4] randomx_reciprocal_fast                  ... PASSED
[ 5] Dataset initialization (interpreter)     ... PASSED
[ 6] Dataset initialization (compiler)        ... PASSED
[ 7] AesGenerator1R                           ... PASSED
[ 8] IADD_RS (decode)                         ... PASSED
[ 9] IADD_RS (execute)                        ... PASSED

    <snip>

[87] Hash test 2d (compiler)                  ... PASSED
[88] Hash test 2e (compiler)                  ... PASSED
[89] Cache initialization: SSSE3              ... PASSED
[90] Cache initialization: AVX2               ... PASSED
[91] Hash batch test                          ... PASSED
[92] Preserve rounding mode                   ... PASSED

All tests PASSED
┌─(~/Software/Git/monero-all/RandomX/build)──────...───(xxxx@yyyy:pts/5)─┐
└─(16:42:38 on master)──>                                                                ──(Mon,Apr24)─┘
` 

Looks like my machine does something different than others. I keep digging.


## tevador | 2023-04-25T18:54:25+00:00
If RandomX tests complete without errors, then it's not a cache initialization issue. It could be a bug in monerod, e.g. accidentally passing `NULL` when calling `randomx_init_dataset` due to some race condition.

## Wolf54 | 2023-04-25T21:44:29+00:00
Yes, it might be a bug in monerod. I mean, this code section is not really that much used anymore, I believe. nobody is mining like this anymore. I assume everybody is mining via a pool or p2pool these days. Correct me if I'm wrong with this assumption. I will dig into this deeper and try to find out. But thanks to all of you trying to help.

## selsta | 2023-04-27T14:30:16+00:00
Fixed in https://github.com/monero-project/monero/pull/8831

## Wolf54 | 2023-04-27T17:43:33+00:00
I applied the patch and ran a test. I can confirm that the patch is working. Mining starts up and is working as expected. Thanks to all team members. 

# Action History
- Created by: 19231224lhr | 2023-04-11T04:38:59+00:00
- Closed at: 2023-06-06T01:09:22+00:00
