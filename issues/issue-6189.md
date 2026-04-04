---
title: Can't build release v0.15
source_url: https://github.com/monero-project/monero/issues/6189
author: 4NobleTruths
assignees: []
labels: []
created_at: '2019-11-27T04:38:54+00:00'
updated_at: '2019-11-28T08:01:11+00:00'
type: issue
status: closed
closed_at: '2019-11-28T08:01:11+00:00'
---

# Original Description
Using instructions:
https://github.com/monero-project/monero/tree/release-v0.15#compiling-monero-from-source

On Debian 9 Qubes 4

Error log attached.
[CMakeError.log](https://github.com/monero-project/monero/files/3895125/CMakeError.log)
[CMakeOutput.log](https://github.com/monero-project/monero/files/3895130/CMakeOutput.log)



# Discussion History
## vtnerd | 2019-11-27T04:55:09+00:00
pthreads does not appear to be installed.

## 4NobleTruths | 2019-11-27T05:21:23+00:00
Installing libevent-core for pthreads doesn't fix it.
To me, seems like it's all those lines that say "c++: error: unrecognized command line option"

## vtnerd | 2019-11-27T05:27:05+00:00
The first error was to a missing link on `pthread_create`. The output from the standard console would be useful too because I think it differs from this.

## 4NobleTruths | 2019-11-27T05:40:32+00:00
Then I guess something is missing from the list of dependencies on that  page.

This is what it wrote from console redirect:
[make.log](https://github.com/monero-project/monero/files/3895288/make.log)

The only failures are regarding the fcf unrecognized commands.

## moneromooo-monero | 2019-11-27T13:57:50+00:00
Works for me from a fresh vm.

## 4NobleTruths | 2019-11-28T05:45:35+00:00
I'm building in a Debian-9-minimal VM template, with just the minimal networking and the Monero dependencies listed on above release page.

If a VM is created from it, has the same errors.

## 4NobleTruths | 2019-11-28T08:00:58+00:00
It builds from the git clone, but not from the zip archive of that release branch.

# Action History
- Created by: 4NobleTruths | 2019-11-27T04:38:54+00:00
- Closed at: 2019-11-28T08:01:11+00:00
