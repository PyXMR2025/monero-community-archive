---
title: 'Kovri: DragonBSD build failing'
source_url: https://github.com/monero-project/meta/issues/130
author: anonimal
assignees: []
labels: []
created_at: '2017-10-24T14:36:47+00:00'
updated_at: '2017-11-01T17:22:48+00:00'
type: issue
status: closed
closed_at: '2017-11-01T17:22:48+00:00'
---

# Original Description
@danrmiller how did you build boost? https://build.getmonero.org/builders/kovri-all-dragonflybsd-amd64

# Discussion History
## danrmiller | 2017-10-24T14:42:14+00:00
I didn't build it, its DragonflyBSD's port of boost-libs-1.63.0_1

## anonimal | 2017-10-24T15:20:59+00:00
Was clang needed for monero? I don't remember asking to switch to clang for dragonflybsd... The build started failing in-between the switch from gcc to clang:

- [Working gcc build](https://build.getmonero.org/builders/kovri-all-dragonflybsd-amd64/builds/218/steps/compile/logs/stdio)
- [Failing in-between switch](https://build.getmonero.org/builders/kovri-all-dragonflybsd-amd64/builds/219/steps/compile/logs/stdio)
- [Beginning of failing clang build](https://build.getmonero.org/builders/kovri-all-dragonflybsd-amd64/builds/229/steps/compile/logs/stdio)

## danrmiller | 2017-10-31T21:00:55+00:00
It switched to clang because I thought all of the platform specific build environment differences were gone so I combined the BSDs to use one build factory. But I missed the difference that dragonfly doesn't use clang, or maybe figured it wouldn't matter.

I've switched back to gcc for dragonfly and it builds:

https://build.getmonero.org/builders/kovri-all-dragonflybsd-amd64/builds/342

# Action History
- Created by: anonimal | 2017-10-24T14:36:47+00:00
- Closed at: 2017-11-01T17:22:48+00:00
