---
title: '"-a=cryptonight" not work in 2.6.3'
source_url: https://github.com/xmrig/xmrig/issues/702
author: Quake4
assignees: []
labels: []
created_at: '2018-06-23T07:55:49+00:00'
updated_at: '2018-06-23T11:12:57+00:00'
type: issue
status: closed
closed_at: '2018-06-23T11:12:57+00:00'
---

# Original Description
from command line -a switch not work
if specify `--algo=cryptonight` - work fine

command not work:
xmrig.exe -o cryptonightv7.eu.nicehash.com:3363 -u xxx.Home -p x --api-port=4045 --variant 1 --donate-level=1 --cpu-priority 0 -R 5 -a=cryptonight

command work fine:
xmrig.exe -o cryptonightv7.eu.nicehash.com:3363 -u xxx.Home -p x --api-port=4045 --variant 1 --donate-level=1 --cpu-priority 0 -R 5 --algo=cryptonight


# Discussion History
## lisergey | 2018-06-23T09:42:56+00:00
And it should not work in format
`-a=cryptonight`

There are two different formats of command line string: 
short with single dash before param: `-<param> <space> <value>`
and long with double dash: `--<param>=<value>`

do not mix them up :)

## Quake4 | 2018-06-23T11:12:57+00:00
thanks. sorry.

# Action History
- Created by: Quake4 | 2018-06-23T07:55:49+00:00
- Closed at: 2018-06-23T11:12:57+00:00
