---
title: monerod on MacOS should automatically write output to ~/Library/Application
  Support/Monero
source_url: https://github.com/monero-project/monero/issues/3044
author: rex4539
assignees: []
labels: []
created_at: '2018-01-01T15:11:31+00:00'
updated_at: '2018-01-04T13:37:25+00:00'
type: issue
status: closed
closed_at: '2018-01-04T13:37:25+00:00'
---

# Original Description
Monero 'Helium Hydra' (v0.11.1.0-release)

Reproducibility: always

Steps:
Run monerod directly from Terminal.

What happened:
monerod writes output to ~/.bitmonero

Expected result:
monerod writes output to ~/Library/Application Support/Monero

# Discussion History
## moneromooo-monero | 2018-01-01T15:21:12+00:00
Can you post the output of "monerod --os-version" please ?

## rex4539 | 2018-01-01T15:22:48+00:00
`OS: Darwin Darwin Kernel Version 17.4.0: Mon Dec 11 21:15:27 PST 2017; root:xnu-4570.40.9~4/RELEASE_X86_64 17.4.0`

## moneromooo-monero | 2018-01-01T15:26:05+00:00
For whoever has a mac and looks at this, I think it might need replacing "#ifdef MAC_OSX" with "#ifdef \_\_APPLE\_\_" in src/common/util.cpp. Odd that it would not have been found before though.

## stoffu | 2018-01-02T14:52:22+00:00
I've used Mac for a while and never observed the `~/Library/Application Support/Monero` folder being created (at least with the last couple of OS versions). Has anyone else observed the reported behavior?

## ghost | 2018-01-04T08:26:07+00:00
@rex4539  Per #3052 it has been chosen to have as UNIX output folder `~/.bitmonero`.

## jtgrassie | 2018-01-04T13:29:06+00:00
This needs closing as it's misleading.

## ghost | 2018-01-04T13:31:28+00:00
And the `invalid` tag.

## jtgrassie | 2018-01-04T13:33:57+00:00
Personally, I prefer the OP to acknowledge and close. 

## rex4539 | 2018-01-04T13:37:25+00:00
ack

# Action History
- Created by: rex4539 | 2018-01-01T15:11:31+00:00
- Closed at: 2018-01-04T13:37:25+00:00
