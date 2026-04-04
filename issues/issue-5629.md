---
title: cc1plus Error compiling monero master for ARM v8
source_url: https://github.com/monero-project/monero/issues/5629
author: JustHereToHelp
assignees: []
labels: []
created_at: '2019-06-12T00:03:08+00:00'
updated_at: '2022-02-19T04:54:11+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:54:11+00:00'
---

# Original Description
Complied master for arch 1 x86_64 and normal release just fine

when attempting to compile for ARM v8 :

cc1plus: error: bad value ('armv8-a') for  '-march=' switch
cc1plus: note: valid arugments to '-march=' switch are : nocona core2 hehlem corei7 westmere ....etc (rest of list is just every supported processor type)

# Discussion History
## moneromooo-monero | 2019-06-12T09:24:47+00:00
How are you trying to compile it ?

## JustHereToHelp | 2019-06-12T09:47:52+00:00
using this command
make release-static-linux-armv8

it gets to about 30% and gives error listed in op

I have been successfully been able to compile with "make" command for both master and current release just fine, but i get this error when trying for ARM v8.

I am doing all this on a VirtualBox machine of arch linux 5.1.8 arch1 x86_64 GNU/Linux




## moneromooo-monero | 2019-06-12T10:43:41+00:00
The host is x86_64, right ? And the VM is ARM ? What exact ARM platform on the VM ?

## JustHereToHelp | 2019-06-12T10:59:07+00:00
Host is windows 
VM is arch linux 5.1.8 arch1 x86_64 GNU/Linux

Compiled master and current release just fine 

Can i not use that command to make the ARM v8 version in my current VM?

Is raspi the only ARM emulation game in town to build monero on ? I could not get the dependency to all install to use make in these Qemu 

## moneromooo-monero | 2019-06-12T11:09:56+00:00
x86_64 is not an ARM architecture, it's an Intel/AMD one. If you want to build ARM, you need to either have an ARM VM, or use the depends cross compiler setup (see contrib/gitian/README.md).

## JustHereToHelp | 2019-06-12T19:09:56+00:00
makes sense, i tried running an ARM VM but the only one i could find was a raspi-wheezy and it could not download dependencies needed for building reliably for some reason (not found errors in repository).  Is there a better or standardized ARM emu that people prefer for building monero?

also when trying the cross compiler command  on my arch linux  VM, i am not able to download the dependency the README.md requires for cross compiling armv8 which is " g++-aarch-Linux-gnu" using the pacman command. Any suggestions on how to get that ?

i get this error when executing the cross compiler command for arm v8

make[1]: *** [funcs.mk:244: /root/monero/contrib/depends/work/build/aarch64-linux-gnu/boost/1_64_0-ad642601018/ ./ .stamp_built] Error 1
make[1]: Leaving directory '/root/monero/contrib/depends'
make: *** [Makefile:50:depends] Error 2

## hyc | 2019-06-12T19:25:23+00:00
I think the depends build is meant to run under Ubuntu 18.04. Other distros may not provide the right versions of the cross compilers.

## JustHereToHelp | 2019-06-12T19:27:37+00:00
Would that mean it would also work on Mint 19.1 ? or only specifically Ubuntu 18.04?

## moneromooo-monero | 2019-06-12T20:22:33+00:00
FWIW what you pasted does not include the actual error, just the "unwinding" of the build after the error.


## JustHereToHelp | 2019-06-12T20:29:40+00:00
Here is the error above what i pasted before.  I expected this error as i am not able to pacman the dependency g++-aarch64-linux-gnu,  Any idea how i can get that dependency  to install? 

error: toolset gcc initialization
error: provided command aarch64-linux-gnu-g++ not found
error: initialized from /root/monero/contrib/depends/work/build/aarch64-linux-gnu/boost/1_64_0-ad64261018/user-config.jam:1

## sedited | 2019-06-13T00:18:20+00:00
The depends build did work fine for me on arch linux a couple months ago, when I was still using arch. I do not remember the steps though to install the aarch64 toolchain. Using mint should work fine with the provided package names.

# Action History
- Created by: JustHereToHelp | 2019-06-12T00:03:08+00:00
- Closed at: 2022-02-19T04:54:11+00:00
