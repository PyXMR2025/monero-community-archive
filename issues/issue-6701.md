---
title: Daemon stuck at 12 days old block
source_url: https://github.com/monero-project/monero/issues/6701
author: rafafaf29
assignees: []
labels: []
created_at: '2020-07-08T10:23:14+00:00'
updated_at: '2020-07-09T14:57:03+00:00'
type: issue
status: closed
closed_at: '2020-07-09T14:57:03+00:00'
---

# Original Description
Hello,
First issue report, i hope i will do things correctly.

I run my own monerod, dockerized. Today, i looked at it, and realized it was 12 days late, and stuck at block 2128871, although a top block candidate of 2137617 (number evolving) is returned. I was using v16.0.0 until today, where i updated to 16.0.1 (keeping same blockchain files). No pruning, as far as i can tell.
I have a feeling that i am on an alternative chain, but not sure at all.

At the daemon launch, i have 2 lines like this : 
`2020-07-08 09:59:44.574	W ge_frombytes_vartime failed at 481`

Then, my log is full of 
```
2020-07-08 09:59:56.325	I SYNCHRONIZATION started
2020-07-08 09:59:59.742	I [88.99.167.39:45912 INC] Sync data returned a new top block candidate: 2128871 -> 2137617 [Your node is 8746 blocks (12.1 days) behind]
```
and sometimes of 
`2020-07-08 10:01:32.751	I Host 62.210.104.31 blocked.`

If i enter `set_log 1` , then i have often red lines like this : 
`2020-07-08 10:10:14.016	E Setting timer on a shut down object`
and sometimes red lines like these ones : 
```
2020-07-08 10:13:06.597	E Block recognized as orphaned and rejected, id = <6550014da1ac8639fbcfad1d5fc8418053d7a87060d93e9e542c8f7aaa426993>, height 2128872, parent in alt 0, parent in main 0 (parent <5ab9220271f804e50964bd7705f971985b9c8cdb7c1ab7eee3e68a23e4910b1b>, current top <9cfab0f4780b6ed976e562367bde5507eaaad0f30af122fcc5974742f62e34ca>, chain height 2128871)
```
and also line like these ones :
```
2020-07-08 10:14:46.116	W [64.227.56.122:18080 OUT] Failed to invoke COMMAND_PING to 64.227.56.122:18080(-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-07-08 10:14:46.116	I [64.227.56.122:18080 OUT] [0] state: closed in state before_handshake
2020-07-08 10:14:46.116	I [64.227.56.122:18080 3115a722-6418-434e-abe6-dd5a018779af OUT] CLOSE CONNECTION
2020-07-08 10:14:46.121	I Failed to invoke command 1007 return code -3
2020-07-08 10:14:46.121	W [64.227.56.122:39588 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
```

I read issue #3734 , so here are the commands results : 
`status` : 
```
Height: 2128871/2137628 (99.6%) on mainnet, not mining, net hash 1.58 GH/s, v12, 8(out)+38(in) connections, uptime 0d 0h 7m 52s
```
`sync_info` : 
```
Height: 2128871, target: 2137628 (99.5903%)
Downloading at 79 kB/s
Next needed pruning seed: 1
44 peers
51.89.181.95:46637        de85e3bb8f875c9f  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.79.117.97:58025        27d2e3c4a0bb4f72  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
54.39.75.53:44927         17ecab92ac0e469e  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
66.70.255.248:41921       ae94eb71c2d36499  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
138.201.19.111:54322      936bcd741ac3048f  normal            0         1  0 kB/s, 0 blocks / 0 MB queued
94.23.169.209:42603       fc48216a1ab7c593  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.89.181.105:40871       d183952bd285b1cb  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
151.80.17.140:48523       c49225b69dfcb8a2  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.77.136.40:56347        b59d4f213d6652c8  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
54.39.75.69:50063         42d9994d12800828  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
147.135.190.201:33465     5e5ecafd4c9522c4  normal            0         2128871  0 kB/s, 0 blocks / 0 MB queued
51.89.133.122:58413       fb6d1bf46094d047  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
94.23.147.238:55039       9c328c37e6f8af77  normal            0         2128871  0 kB/s, 0 blocks / 0 MB queued
51.77.227.128:60805       bf93ed2fd54f5cfe  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.83.124.103:57665       54110ee70d033846  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.89.181.97:56685        5d7b583bd3210395  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.68.220.13:36089        960c39bec6090879  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
66.70.207.166:52205       ac0220d1d2d4ee2d  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
178.33.101.193:35643      7a3a656ae42ac6f0  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.83.124.103:18080       abe91fdcc5659610  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.79.54.168:48293        449a659a348df375  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.68.215.64:58263        9567d91f2d2fcf73  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.79.51.28:37099         200c582add423b93  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
54.39.75.70:45103         f406c006838c874c  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
139.162.55.118:50798      47d51cf1c7ab8aed  normal            0         1  4 kB/s, 0 blocks / 0 MB queued
51.79.50.44:53619         67ba237ca18b22e7  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.89.181.106:45487       5d0f59ed3c714aee  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.89.164.226:55805       1419426b7051d0e2  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
144.217.241.28:33809      ff77cc02f6a6327c  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
144.217.224.26:2796       fc53e25f05586d91  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.79.52.228:37377        d65aaf5ee721806a  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
94.23.169.209:13902       b2f4baba627a2cbf  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
75.114.200.197:50000      5337ae27756bc88b  normal            0         2020304  0 kB/s, 0 blocks / 0 MB queued
51.77.202.219:38563       f58316389ae5d06f  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.68.214.143:53915       44d90ca365e26c20  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.89.181.105:3121        5104770201f69b3c  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.75.70.225:41051        47a8d7bcd8da1fb2  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.79.117.98:4169         609430ecdc82aef2  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
54.39.75.73:33583         401541fefc94ec1c  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
147.175.187.93:42764      b7d50a9f2b2267dd  synchronizing     184       2137628  1 kB/s, 0 blocks / 0 MB queued
192.99.154.164:18080      6014fa992f6348dc  normal            0         2128871  0 kB/s, 0 blocks / 0 MB queued
51.77.136.40:18080        70272a9164791ec4  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.91.8.178:48943         311d2a734430ab56  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
51.79.49.41:48229         ecf9facc0a5a0abb  normal            0         2128871  2 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]
```
`print_cn` : 
```
Remote Host                   Type    SSL   Peer id             Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)      

INC 51.79.117.98:45281        IPv4    no    343b2f4a27ea64b4    1                   468(2)/15760(2)               normal                   23                  0           0             0         0            
INC 144.217.241.118:39089     IPv4    no    ea6443cb0d88c22b    1                   468(2)/15536(2)               normal                   24                  0           0             0         0            
INC 51.89.181.95:46637        IPv4    no    de85e3bb8f875c9f    1                   26938(10)/27813(10)           normal                   71                  0           0             0         1            
INC 51.79.117.97:58025        IPv4    no    27d2e3c4a0bb4f72    1                   26938(10)/27791(10)           normal                   71                  0           0             0         1            
INC 51.79.117.99:48835        IPv4    no    95c991df265e0245    1                   382(7)/15381(7)               normal                   8                   0           0             1         1            
INC 54.39.75.53:44927         IPv4    no    17ecab92ac0e469e    1                   27024(3)/28259(3)             normal                   85                  0           0             0         0            
INC 66.70.255.248:41921       IPv4    no    ae94eb71c2d36499    1                   27024(5)/27566(5)             normal                   86                  0           0             0         0            
INC 138.201.19.111:54322      IPv4    no    936bcd741ac3048f    1                   869(51)/27189(51)             normal                   106                 0           0             0         1            
INC 94.23.169.209:42603       IPv4    no    fc48216a1ab7c593    1                   27110(9)/27808(9)             normal                   110                 0           0             0         0            
INC 54.39.75.69:50063         IPv4    no    42d9994d12800828    1                   53537(1)/37520(1)             normal                   133                 0           0             0         0            
INC 51.75.157.195:52241       IPv4    no    e8eb30c26157e04a    1                   382(0)/15406(0)               normal                   1                   0           0             15        1            
INC 94.23.147.238:55039       IPv4    no    9c328c37e6f8af77    1                   27024(2)/28003(2)             normal                   84                  0           0             0         0            
OUT 51.83.124.103:18080       IPv4    no    abe91fdcc5659610    1                   114822(10)/38580(10)          normal                   232                 0           0             0         0            
INC 51.79.54.168:48293        IPv4    no    449a659a348df375    1                   106649(4)/49799(4)            normal                   256                 0           0             0         0            
INC 51.68.215.64:58263        IPv4    no    9567d91f2d2fcf73    1                   133162(5)/53851(5)            normal                   306                 0           0             0         0            
INC 54.39.75.70:45103         IPv4    no    f406c006838c874c    1                   27067(4)/28006(4)             normal                   96                  0           0             0         0            
INC 139.162.55.118:50798      IPv4    no    47d51cf1c7ab8aed    1                   192987(14)/52881(14)          normal                   331                 0           0             0         0            
INC 51.79.50.44:53619         IPv4    no    67ba237ca18b22e7    1                   133119(1)/54104(1)            normal                   301                 0           0             0         0            
INC 51.89.181.106:45487       IPv4    no    5d0f59ed3c714aee    1                   26895(1)/27074(1)             normal                   61                  0           0             0         1            
INC 51.89.164.226:55805       IPv4    no    1419426b7051d0e2    1                   186446(5)/94922(5)            normal                   467                 0           0             0         0            
INC 144.217.241.28:33809      IPv4    no    ff77cc02f6a6327c    1                   212873(0)/97526(0)            normal                   492                 0           0             0         0            
OUT 144.217.224.26:2796       IPv4    no    fc53e25f05586d91    1                   194490(5)/55647(5)            normal                   409                 0           0             0         0            
INC 51.79.52.228:37377        IPv4    no    d65aaf5ee721806a    1                   212916(1)/97611(1)            normal                   522                 0           0             0         0            
OUT 94.23.169.209:13902       IPv4    no    b2f4baba627a2cbf    1                   247602(1)/95909(1)            normal                   525                 0           0             0         0            
OUT 75.114.200.197:50000      IPv4    no    5337ae27756bc88b    1                   77343(0)/8738533(0)           normal                   534                 0           0             15        0            
INC 51.77.202.219:38563       IPv4    no    f58316389ae5d06f    1                   80179(10)/45248(10)           normal                   221                 0           0             0         0            
INC 51.68.214.143:53915       IPv4    no    44d90ca365e26c20    1                   213045(5)/97828(5)            normal                   537                 0           0             0         0            
OUT 51.89.181.105:3121        IPv4    no    5104770201f69b3c    1                   247602(8)/95314(8)            normal                   533                 0           0             0         0            
INC 51.75.70.225:41051        IPv4    no    47a8d7bcd8da1fb2    1                   186403(6)/94678(6)            normal                   458                 0           0             0         0            
OUT 51.79.117.98:4169         IPv4    no    609430ecdc82aef2    1                   247856(2)/97741(2)            normal                   545                 0           0             0         0            
INC 54.39.75.73:33583         IPv4    no    401541fefc94ec1c    1                   27110(8)/27507(8)             normal                   110                 0           0             0         0            
INC 147.175.187.93:42764      IPv4    no    b7d50a9f2b2267dd    1                   119485(4)/43388(4)            synchronizing            153                 0           0             0         0            
OUT 192.99.154.164:18080      IPv4    no    6014fa992f6348dc    1                   247856(2)/98191(2)            normal                   548                 0           0             0         0            
OUT 51.77.136.40:18080        IPv4    no    70272a9164791ec4    1                   247856(1)/97914(1)            normal                   546                 0           0             0         0            
INC 51.91.8.178:48943         IPv4    no    311d2a734430ab56    1                   186360(10)/95864(10)          normal                   451                 0           0             0         0            
INC 54.39.75.56:43919         IPv4    no    982510d7a9de35b9    1                   382(7)/15578(7)               normal                   8                   0           0             1         1            
INC 51.79.49.41:48229         IPv4    no    ecf9facc0a5a0abb    1                   212916(4)/96835(4)            normal                   507                 0           0             0         0            
202
```

Don't hesitate asking if any info is needed, and thanks for the help !

# Discussion History
## moneromooo-monero | 2020-07-08T11:02:52+00:00
Restart with --log-level 1, and print the verification errors from the log, along with a dozen lines before and after it to make sure we have everything interesting.

## rafafaf29 | 2020-07-08T14:17:11+00:00
Hi. I'm not sure which line is the verification error. I searched for "verification" and had only 1 line, so here it is (i put it between spaces) : 
```
2020-07-08 14:07:03.257	I Transaction added to pool: txid <1ff76171a6ba2a0606e88d7848408b971b968d66f9610c3e49b3ef8fcf8a676a> weight: 2599 fee/byte: 10638.7
2020-07-08 14:07:03.262	I Transaction added to pool: txid <a53d9c669174c5add8b16e938082ba1f27e91a5a7dd327c587135ebc23d92123> weight: 2600 fee/byte: 10638.5
2020-07-08 14:07:03.267	I Transaction added to pool: txid <01cf8fdde4e0f2b8eead5a1af30bcfaf0d0a7f1693bb54ad87ec251c8029fddd> weight: 2601 fee/byte: 10638.2
2020-07-08 14:07:03.274	I Transaction added to pool: txid <0cce4f0144bb92ad53bd9277773dee9d7eec82b13aef2801d196d831ea37a3cc> weight: 2603 fee/byte: 10637.7
2020-07-08 14:07:03.279	I Transaction added to pool: txid <40e5ae1dbb3e438553645f98db65615bbfe2313350bad9ac10b8be76772f5870> weight: 2603 fee/byte: 10637.7
2020-07-08 14:07:03.284	I Transaction added to pool: txid <4c9571d836f9562362fb3d9e50c0da7a0f7bf1b14a2b3e61a6a0529303b80404> weight: 2603 fee/byte: 10637.7
2020-07-08 14:07:03.288	I Transaction added to pool: txid <63114a489df6deb4d3bac186b8a6a0fa462b71a7e71d620edd512d3dee174b98> weight: 2605 fee/byte: 10637.2
2020-07-08 14:07:03.293	I Transaction added to pool: txid <c1d018200f9f89ed06eb00d799e349b5dfaddc729dfdaada219571ce7f5bb85c> weight: 2605 fee/byte: 10637.2
2020-07-08 14:07:03.296	W ge_frombytes_vartime failed at 481
2020-07-08 14:07:03.298	I verRctMGSimple failed for input 0
2020-07-08 14:07:03.298	E Failed to check ringct signatures!
2020-07-08 14:07:03.298	I Transaction added to pool: txid <b288eb5af2ee786e700387f1e843f6e532ad40861dd2948867c2d1f16591b013> weight: 2606 fee/byte: 10637

2020-07-08 14:07:03.298	I [89.176.232.111:18080 OUT] Block verification failed, dropping connection

2020-07-08 14:07:03.298	I [68.183.192.69:18080 OUT] 243 bytes sent for category command-1001 initiated by us
2020-07-08 14:07:03.299	E Setting timer on a shut down object
2020-07-08 14:07:03.299	I [89.176.232.111:18080 OUT] [0] state: closed in state synchronizing
2020-07-08 14:07:03.299	I [89.176.232.111:18080 b876ea67-0039-4414-bb9e-616c235f95b2 OUT] CLOSE CONNECTION
2020-07-08 14:07:03.323	W [<none> OUT] back ping connect failed to 211.103.24.110:18080
2020-07-08 14:07:03.343	I [51.77.192.92:5913 OUT] 10 bytes received for category command-1003 initiated by peer
2020-07-08 14:07:03.343	I [51.77.192.92:5913 OUT] 38 bytes sent for category command-1003 initiated by peer
2020-07-08 14:07:03.348	I [211.103.24.110:51284 INC] 29 bytes received for category command-1007 initiated by us
2020-07-08 14:07:03.626	I [211.103.24.110:51284 INC] 10 bytes received for category command-1007 initiated by peer
2020-07-08 14:07:03.626	I [211.103.24.110:51284 INC] 29 bytes sent for category command-1007 initiated by peer
2020-07-08 14:07:03.920	I [68.183.192.69:18080 OUT] 10 bytes received for category command-1007 initiated by peer
2020-07-08 14:07:03.920	I [68.183.192.69:18080 OUT] 29 bytes sent for category command-1007 initiated by peer
2020-07-08 14:07:03.975	I Failed to invoke command 1001 return code -3
```

If you are talking about the "block detected as orphaned" error, here it is : 
```
2020-07-08 14:07:23.741	I [51.79.117.99:39711 06f47aff-39fd-40ea-92fb-7c2d2f2aca35 INC] NEW CONNECTION
2020-07-08 14:07:23.746	I [51.79.117.99:39711 INC] 244 bytes received for category command-1001 initiated by peer
2020-07-08 14:07:23.746	I [51.79.117.99:39711 INC] 10 bytes sent for category command-1007 initiated by us
2020-07-08 14:07:23.747	I [51.79.117.99:39711 INC] 15126 bytes sent for category command-1001 initiated by peer
2020-07-08 14:07:23.832	I [51.79.117.99:18080 b7320196-9bdd-4002-906f-f82ed3fd2fb6 OUT] NEW CONNECTION
2020-07-08 14:07:23.832	I [51.79.117.99:18080 OUT] 10 bytes sent for category command-1003 initiated by us
2020-07-08 14:07:23.835	I [51.79.117.99:39711 INC] 29 bytes received for category command-1007 initiated by us
2020-07-08 14:07:23.894	I [89.176.232.111:33148 INC] 791573 bytes received for category command-2004 initiated by peer
2020-07-08 14:07:23.894	I [89.176.232.111:33148 INC] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks)
2020-07-08 14:07:23.894	I [89.176.232.111:33148 INC] [0] state: received objects in state synchronizing
2020-07-08 14:07:23.896	I [89.176.232.111:33148 INC] [0] state: adding blocks in state synchronizing
2020-07-08 14:07:23.896	I Restarting adding block after idle for 11.9416 seconds

2020-07-08 14:07:23.896	E Block recognized as orphaned and rejected, id = <6550014da1ac8639fbcfad1d5fc8418053d7a87060d93e9e542c8f7aaa426993>, height 2128872, parent in alt 0, parent in main 0 (parent <5ab9220271f804e50964bd7705f971985b9c8cdb7c1ab7eee3e68a23e4910b1b>, current top <9cfab0f4780b6ed976e562367bde5507eaaad0f30af122fcc5974742f62e34ca>, chain height 2128871)

2020-07-08 14:07:23.896	I [89.176.232.111:33148 INC] Block received at sync phase was marked as orphaned, dropping connection
2020-07-08 14:07:23.896	E Setting timer on a shut down object
2020-07-08 14:07:23.896	I [89.176.232.111:33148 INC] [0] state: closed in state synchronizing
2020-07-08 14:07:23.896	I [89.176.232.111:33148 548edef9-8db9-48b4-9ff4-d17d9dba09ca INC] CLOSE CONNECTION
2020-07-08 14:07:23.917	I [51.79.117.99:18080 OUT] 38 bytes received for category command-1003 initiated by us
2020-07-08 14:07:23.917	E Setting timer on a shut down object
2020-07-08 14:07:23.917	I [51.79.117.99:18080 OUT] [0] state: closed in state before_handshake
2020-07-08 14:07:23.917	I [51.79.117.99:18080 b7320196-9bdd-4002-906f-f82ed3fd2fb6 OUT] CLOSE CONNECTION
2020-07-08 14:07:24.170	I [51.89.181.105:50967 INC] 10 bytes received for category command-1003 initiated by peer
2020-07-08 14:07:24.170	I [51.89.181.105:50967 INC] 38 bytes sent for category command-1003 initiated by peer
2020-07-08 14:07:24.289	I [46.165.232.165:18080 OUT] 792193 bytes received for category command-2004 initiated by peer
2020-07-08 14:07:24.289	I [46.165.232.165:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks)
```

Please tell me if i'm wrong !

## moneromooo-monero | 2020-07-08T14:35:42+00:00
Looks like you've got corrupted data in your blockchain, and it's using it to verify an incoming tx, and failing.

You can either:

(1) Delete your chain and resync
(2) build with a patch I'd give you which would print the data it's using so we can work out what data is bad

Ultimately, you'll probably end up doing 1 after 2 anyway since we can't know whether what we find is the only corrupt data or not.

## rafafaf29 | 2020-07-08T14:47:01+00:00
It's not a problem for me to delete and resync all the blockchain.
I mainly reported this bug hoping it could help isolating and fixing a bug in the software. If there is nothing useful, we can close it.
It's just weird, i don't remember having any bug/crash on my daemon nor my server.

By the way, i have some lines like this : 
```
2020-07-08 14:07:03.142	I CHECKPOINT PASSED FOR HEIGHT 2046000 <5e867f0b8baefed9244a681df97fc885d8ab36c3dfcd24c7a3abf3b8ac8b8314>
2020-07-08 14:07:03.142	I CHECKPOINT PASSED FOR HEIGHT 2092500 <c4e00820c9c7989b49153d5e90ae095a18a11d990e82fcc3be54e6ed785472b5>
2020-07-08 14:07:03.142	I CHECKPOINT PASSED FOR HEIGHT 2125000 <a8e49c62792a2aa56ba62603fe015303647e2c19203c56999c7f6f2498cd3e6d>
```
immediately followed by lines like this : 
```
2020-07-08 14:07:03.143	I transaction with hash c46b44c45bf8a5492a98f840d1a429ed2f3ec05ea9cc04ed3e0ba46efe3043fb not found in db
2020-07-08 14:07:03.148	I transaction with hash a9c0b8c05b4888f7ee39ad265fafda1371d63a86e15f33c9b699a111c8bd13a5 not found in db
2020-07-08 14:07:03.153	I transaction with hash 1a5b582f1cb1240c141b2f02a12f6c8b70726a1e58bd533e822489aae5ce44d7 not found in db
```
As some checkpoints seems to be OK, couldn't the daemon auto-resync from last good checkpoint if something like this happens ?

Thank you for the help anyway (and for Monero, actually) :)

## moneromooo-monero | 2020-07-08T15:13:47+00:00
No, this is not what a checkpoint is.

## rafafaf29 | 2020-07-08T15:51:42+00:00
If i understand correctly, based on this : https://www.reddit.com/r/Monero/comments/84a4j0/does_monero_have_checkpoints/ and the linked code, checkpoints are used to ensure authenticity of the blockchain, rejecting chains not including these blocks.
As long as I'm sure that my data is correct at least until block 2125000, is there a way to force resynchronisation only from this block ?

Or, more simply put, is there a way to force resync from some height, while keeping all the data before this height ?

Again, it's mainly to understand better, no problem for me to resync everything :)

## moneromooo-monero | 2020-07-08T16:14:32+00:00
Yes, pop_blocks N, with N being current height minus 2125000.

## rafafaf29 | 2020-07-09T14:57:03+00:00
It took some time, but `pop_blocks 10000` have worked perfectly !
Thank you :)

# Action History
- Created by: rafafaf29 | 2020-07-08T10:23:14+00:00
- Closed at: 2020-07-09T14:57:03+00:00
