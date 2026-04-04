---
title: './monero-wallet-rpc: /lib64/libc.so.6: version `GLIBC_2.25'' not found (required
  by ./monero-wallet-rpc)'
source_url: https://github.com/monero-project/monero/issues/6396
author: GongSuiLi
assignees: []
labels: []
created_at: '2020-03-20T08:10:27+00:00'
updated_at: '2020-04-04T18:19:39+00:00'
type: issue
status: closed
closed_at: '2020-04-04T18:19:39+00:00'
---

# Original Description
When I start monero-wallet-rpc v0.15.0.5 use ./monero-wallet-rpc --config-file= ,connect monerod failed, return ./monero-wallet-rpc: /lib64/libc.so.6: version `GLIBC_2.25' not found (required by ./monero-wallet-rpc).

OS: centos7
version: v0.15.0.5

# Discussion History
## dEBRUYNE-1 | 2020-03-20T09:20:16+00:00
Similar issue reported here:

https://www.reddit.com/r/monerosupport/comments/flq740/error_with_01505_cli_and_ubuntu_1604/

## selsta | 2020-03-20T09:35:58+00:00
Did v0.15.0.1 start correctly?

## xiphon | 2020-03-20T10:42:24+00:00
~~Reproducible binaries don't support anything older than Ubuntu bionic 18.04~~

~~If you are using an old OS, the best way would be to build Monero from sources following the manual https://github.com/monero-project/monero#compiling-monero-from-source~~

## xiphon | 2020-03-20T12:09:00+00:00
Ignore my previous comment, while inspecting the binaries i misread `gnu_get_libc_version@@GLIBC_2.2.5` as `GLIBC_2.25`.

## xiphon | 2020-03-20T12:51:19+00:00
The reason is bumped libsodium `1.0.18` version. Libsodium uses `getrandom(...)` which has been added in glibc `2.25`.

## sumogr | 2020-03-20T12:53:26+00:00
> The reason is bumped libsodium `1.0.18` version. Libsodium uses `getrandom(...)` which has been added in glibc `2.25`.

It might be one of the reasons. make release-static fails as well on xenial
I think its a python3 issue

## GongSuiLi | 2020-03-20T13:24:00+00:00
> Did v0.15.0.1 start correctly?

v0.15.0.0 start correctly

## BKdilse | 2020-03-20T13:37:41+00:00
same issue for me.  15.0.1 worked fine, but 15.0.5 causing this issue.

## selsta | 2020-03-20T14:26:11+00:00
We could move back to libsodium 1.0.16, there is still a mirror on Github: https://github.com/jedisct1/libsodium/releases/download/1.0.16/libsodium-1.0.16.tar.gz

@TheCharlatan what is your opinion?

## sedited | 2020-03-20T14:33:09+00:00
I should have checked for version increases, sorry everybody! I'll work on tooling to catch this in the future. It's probably easiest to revert the version, yes. It's not just the rpc client effected, it's the wallet as well. Alternatively we could see if we can do some clever patching with it, but this will require some time.

## xiphon | 2020-03-20T15:26:58+00:00
I'm looking into patching libsodium during depends build

## GongSuiLi | 2020-03-21T01:08:43+00:00
> I should have checked for version increases, sorry everybody! I'll work on tooling to catch this in the future. It's probably easiest to revert the version, yes. It's not just the rpc client effected, it's the wallet as well. Alternatively we could see if we can do some clever patching with it, but this will require some time.

We update version to v0.15.0.5 because of the two security vulnerabilities disclosed by the Monroe project. Now we have to revert the version. Can we use it safely? Or do we stop using the old node version until the new solution

## GongSuiLi | 2020-03-21T01:11:43+00:00
> I'm looking into patching libsodium during depends build

Will there be a new version?

## selsta | 2020-03-21T01:13:56+00:00
The first reported issue (https://hackerone.com/reports/803028) is only GUI related and can not be exploited.

The second issue (https://hackerone.com/reports/766963) only applies for Tor/I2P nodes and at worst it can reveal the public IP address. If you run a normal node, this is nothing that can be exploited.

It is safe to use v0.15.0.1 in the meantime.

## GongSuiLi | 2020-03-21T01:18:31+00:00
> The first reported issue (https://hackerone.com/reports/803028) is only GUI related and can not be exploited.
> 
> The second issue (https://hackerone.com/reports/766963) only applies for Tor/I2P nodes and at worst it can reveal the public IP address. If you run a normal node, this is nothing that can be exploited.
> 
> It is safe to use v0.15.0.1 in the meantime.

What about v0.15.0.0, we are using this version online now.

## selsta | 2020-03-21T01:19:48+00:00
If you run into issues I would upgrade to v0.15.0.1, else v0.15.0.0 is ok too.

## GongSuiLi | 2020-03-21T01:26:38+00:00
> The first reported issue (https://hackerone.com/reports/803028) is only GUI related and can not be exploited.
> 
> The second issue (https://hackerone.com/reports/766963) only applies for Tor/I2P nodes and at worst it can reveal the public IP address. If you run a normal node, this is nothing that can be exploited.
> 
> It is safe to use v0.15.0.1 in the meantime.

About the second issue, If we are running a normal node, is there such a scenario, that is, the Tor node established by the hacker itself is attacked to add the peer_id of the node to those normal nodes connected to the tor node.
The address of the nodal node is exposed. After the connection, the hacker node can respond to the false data for the request of the normal node. In this way, all the information which important to our node requested by our node is false and will be attacked.
So we are always trying to upgrade to the latest version quickly to avoid risks，from here: https://github.com/monero-project/monero/issues/6390, advised to update the latest version.

## GongSuiLi | 2020-03-22T10:20:59+00:00
> I should have checked for version increases, sorry everybody! I'll work on tooling to catch this in the future. It's probably easiest to revert the version, yes. It's not just the rpc client effected, it's the wallet as well. Alternatively we could see if we can do some clever patching with it, but this will require some time.

Will there be a new version about this issue, how to deploy monero v0.15.0.5？ 

## youngqqcn | 2020-03-23T01:41:51+00:00
Same issue !    How to resolve this problem ?   Waiting for  the answers.....

## youngqqcn | 2020-03-23T01:49:07+00:00
I had meet the similary problem  before in other project (Bitcoin SV ).    I resolved that problem by compiled the source  on my CentOS7. But, it was too much trouble to compile source.



## trasherdk | 2020-03-23T04:54:20+00:00
Until a new release, with a fix for this is released, the solution is to build from source.

## BKdilse | 2020-03-23T05:04:50+00:00
> Until a new release, with a fix for this is released, the solution is to build from source.

Have you tried build from source on Ubuntu 16.04?  It fails.

## BKdilse | 2020-03-23T05:06:39+00:00
I've reverted back to v0.15.0.1 for now.  My server instance froze yesterday, and can't be sure what caused it, but the only change made was v0.15.0.5.

## GongSuiLi | 2020-03-23T09:41:32+00:00
> Until a new release, with a fix for this is released, the solution is to build from source.

When will the new release be released? Compiling directly from the source code is slow and tedious.

## sumogr | 2020-03-23T13:00:36+00:00
@BKdilse got to this line https://github.com/monero-project/monero/blob/master/CMakeLists.txt#L647 and change it with this `if (NOT WIN32 AND NOT (CMAKE_C_COMPILER_ID STREQUAL "GNU" AND CMAKE_C_COMPILER_VERSION VERSION_LESS 9.1))` you will then be able to build on ubuntu 16 with `make release-static`. @GongSuiLi it is tedious indeed cause you have to find all respective dependencies. Update your centos to version 8 for the time being 15.05 should run i think @selsta just cross build on xenial and release ffs , that will solve all your problems and you wont have to be patching depends killing symbols not compatible with gblic latest

## selsta | 2020-03-23T13:07:03+00:00
@GongSuiLi 

We will release a new version but there is no ETA yet. It is safe to continue using v0.15.0.1 in the meantime like I explained previously.

@sumogr xiphon already PRed the fix.

## GongSuiLi | 2020-03-23T13:11:51+00:00
> @GongSuiLi
> 
> We will release a new version but there is no ETA yet. It is safe to continue using v0.15.0.1 in the meantime like I explained previously.
> 
> @sumogr xiphon already PRed the fix.

As @sumogr said, can I try to run v0.15.0.5 on centos8, of course, I have a libmonero.so compiled by Monero on another machine centos7, and synchronize data from the Monero node, will there be any problems? Or you do not recommend using v0.15.0.5 immediately

## sumogr | 2020-03-23T13:16:55+00:00
> > @GongSuiLi
> > We will release a new version but there is no ETA yet. It is safe to continue using v0.15.0.1 in the meantime like I explained previously.
> > @sumogr xiphon already PRed the fix.
> 
> As @sumogr said, can I try to run v0.15.0.5 on centos8, of course, I have a libmonero.so compiled by Monero on another machine centos7, and synchronize data from the Monero node, will there be any problems?

If you desperately need to use 15.0.5 then its safe to use it on Centos8, it doesnt have any bugs (and then replace it with the new version when released). Its just a glibc compatiblity issue on cross building. 

## GongSuiLi | 2020-03-23T13:31:42+00:00
> If you desperately need to use 15.0.5 then its safe to use it on Centos8, it doesnt have any bugs (and then replace it with the new version when released). Its just a glibc compatiblity issue on cross building.

It looks like a good solution. My libmonero.so is on a centos7 machine, the monero node will be deployed on another centos8 machine, libmonero.so synchronizes the data from the monero node, and I will call libmonero.so for some tests . Will there be problems with this, such as the difference in os, and incompatibility issues on both sides?



## sumogr | 2020-03-23T13:36:21+00:00
> > If you desperately need to use 15.0.5 then its safe to use it on Centos8, it doesnt have any bugs (and then replace it with the new version when released). Its just a glibc compatiblity issue on cross building.
> 
> It looks like a good solution. My libmonero.so is on a centos7 machine, the monero node will be deployed on another centos8 machine, libmonero.so synchronizes the data from the monero node, and I will call libmonero.so for some tests . Will there be problems with this, such as the difference in os, and incompatibility issues on both sides?

I cannot understand exactly what you mean but no its not a hardfork its a backwards compatible release it should be working. 

## GongSuiLi | 2020-03-23T13:39:30+00:00
> I cannot understand exactly what you mean but no its not a hardfork its a backwards compatible release it should be working.

I mean the OS system versions on both sides are different, will there be compatibility issues between the libmonero.so and monerod nodes?

## sumogr | 2020-03-23T13:41:58+00:00
> > I cannot understand exactly what you mean but no its not a hardfork its a backwards compatible release it should be working.
> 
> I mean the OS system versions on both sides are different, will there be compatibility issues between the libmonero.so and monerod nodes?

No

## GongSuiLi | 2020-03-23T13:45:46+00:00
> No

Thanks for your reply, I will try this solution


# Action History
- Created by: GongSuiLi | 2020-03-20T08:10:27+00:00
- Closed at: 2020-04-04T18:19:39+00:00
