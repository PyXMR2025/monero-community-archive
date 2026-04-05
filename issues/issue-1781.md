---
title: 'Feature request: miner should stop in battery mode'
source_url: https://github.com/xmrig/xmrig/issues/1781
author: Lonnegan
assignees: []
labels:
- enhancement
created_at: '2020-07-16T22:08:35+00:00'
updated_at: '2020-08-11T22:49:06+00:00'
type: issue
status: closed
closed_at: '2020-07-31T07:09:11+00:00'
---

# Original Description
Hi,

there is a feature I've appreciated in the distributed computing scene (BOINC, F@H) for years: you can set up the software to stop if the system is in battery mode. So you can compute in the background with a notebook and don't have to care when you unplug it, because the software stops calculating then. Same on servers with UPS. If the power fails and the system runs on battery, the software pauses to not suck the UPS empty within seconds under full load.

That's a feature I'd like to have in xmrig, too; for the same reasons :)

# Discussion History
## ghost | 2020-07-20T02:08:12+00:00
This is something you can easily do yourself on linux, you can write a script to periodically check the content of /sys/class/power_supply/BAT0/status (or BAT1 if you have an internal battery) and stop xmrig if it says "Discharging"

## Lonnegan | 2020-07-20T10:17:21+00:00
Well, most of my systems are Windows systems, so it would be a nice feature to have :)

## xmrig | 2020-07-23T08:49:27+00:00
Next version will support boolean option `pause-on-battery`, code already in dev branch.
Thank you.

## Lonnegan | 2020-07-23T11:30:47+00:00
Great, THX! 👍 

## xmrig | 2020-07-31T07:09:11+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.3.1

## Lonnegan | 2020-08-11T22:49:06+00:00
Tested and works great on a UPS supported server system. 👍 

# Action History
- Created by: Lonnegan | 2020-07-16T22:08:35+00:00
- Closed at: 2020-07-31T07:09:11+00:00
