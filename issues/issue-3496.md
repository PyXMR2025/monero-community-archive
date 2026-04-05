---
title: Is there a way to apply msr mod on a .cmd file?
source_url: https://github.com/xmrig/xmrig/issues/3496
author: Fgr-35
assignees: []
labels: []
created_at: '2024-06-08T22:47:40+00:00'
updated_at: '2024-06-12T20:01:44+00:00'
type: issue
status: closed
closed_at: '2024-06-12T20:01:44+00:00'
---

# Original Description
Is there a way to apply msr mod on a .cmd file? I couldn't get xmrig to connect with the pool so i made a .cmd file provided by the pool to start but i cannot run it in admin mode so i won't get msr. How can i fix that?

# Discussion History
## geekwilliams | 2024-06-08T23:07:38+00:00
Run it in admin mode with right-click-> run as admin

## Fgr-35 | 2024-06-08T23:09:45+00:00
I get an error that xmrig.exe is not a command, this is why i asked here

## Fgr-35 | 2024-06-08T23:10:11+00:00
It doesn't make sense and i couldn't find anything on the internet 

## geekwilliams | 2024-06-08T23:17:39+00:00
Can you post the contents of your .cmd file minus any private info? 

## Fgr-35 | 2024-06-08T23:22:31+00:00
@echo off
xmrig.exe --donate-level 1 -o de.monero.herominers.com:1111 -u YOUR_MONERO_WALLET_ADDRESS -p YOUR_WORKER_NAME -a rx/0 -k 
pause

This is what is provided by the pool. I only had to configure the wallet address amd the worker name

## geekwilliams | 2024-06-08T23:35:03+00:00
You need to make sure the cmd is in the same folder as xmrig.exe for that to work. Also use .\xmrig.exe at the beginning 

## Fgr-35 | 2024-06-08T23:50:15+00:00
It is on the same folder and it works, the only issue im encountering is that i cannot run it in admin mode to enable msr mod

## SChernykh | 2024-06-08T23:59:16+00:00
https://github.com/xmrig/xmrig/blob/master/scripts/pool_mine_example.cmd
When you run .cmd as admin, it runs in C:\Windows\system32 by default, so some special commands are needed.

## Fgr-35 | 2024-06-09T00:02:32+00:00
Should i run cmd as admin and then use the cd command to locate the folder where xmrig is and from there run the .cmd file, something like that?

## geekwilliams | 2024-06-09T00:05:54+00:00
Sure, that's one way to do it 

## Fgr-35 | 2024-06-09T12:50:17+00:00
It worked and i get 4,5kH/s. Thank you for the help

# Action History
- Created by: Fgr-35 | 2024-06-08T22:47:40+00:00
- Closed at: 2024-06-12T20:01:44+00:00
