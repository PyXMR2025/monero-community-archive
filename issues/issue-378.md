---
title: 'Question: How to run xmrig automatically at window start-up......???'
source_url: https://github.com/xmrig/xmrig/issues/378
author: Gill1000
assignees: []
labels: []
created_at: '2018-02-01T13:46:07+00:00'
updated_at: '2018-11-05T07:10:23+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:10:23+00:00'
---

# Original Description
I have gone through other issues but still i m out of luck..I want to run xmrig automatically on window start-up when i start my window I have tried other ways to run at start-up and now I want to run start-up by registry keys of current user!!!!!........I mean sort of like(it automatically install itself and run automatically even after shut-down by registry keys)hope you get my point.
Thanks.

# Discussion History
## Gill1000 | 2018-02-02T07:50:18+00:00
Thanks Dhruv420 ..but i have done this.i have gon through all the issues !!!.... But. Now i want to practice with registry keys!!!!!

## Gill1000 | 2018-02-02T11:44:21+00:00
Again thanks :)
Let me again clear my question!...How to edit or rewrite the source code only in such a way that it automatically install itself without help of additional apps as you mention before.!! And automatically start-up!!! As i log in! (By windows startup) @Dhruv420 
Thanks.

## Gill1000 | 2018-02-02T14:33:34+00:00
Where. Are you pal @Zelecktor you have got what exactly i m looking for..plz guide if you are reading this.

## Zelecktor | 2018-02-02T16:12:12+00:00
duplicated issue, related with #293
please close.

## Zelecktor | 2018-02-02T16:37:47+00:00
> How to edit or rewrite the source code only in such a way that it automatically install itself without help of additional apps as you mention before.

Are you thinking in make like a startup registry key persistance? for example, when you launch miner for first time, it will automatically put the register and If the user deletes the startup registry key, the miner will write a new startup key immediately?

I think you want to create a virus hahahaha but interesting, to do it you need to modify severals src to add a fragment of the source code of register injection. Also to bypass admin permision to modify register key if you run as user, thats not easy.

## sergneo | 2018-02-02T17:40:21+00:00
I use xmrig installed as a service using nssm ( http://nssm.cc/download ) . It is very easy to use program.

## Gill1000 | 2018-02-03T06:53:12+00:00
Hehehe virus hehaheha..noo way ..this option is not in my checklist.. maybe @xmrig you can help

## JuanMao1997 | 2018-05-01T09:01:09+00:00
@sergneo but how to make it startup on other computers? It's impossible to install nssm on every computer.

# Action History
- Created by: Gill1000 | 2018-02-01T13:46:07+00:00
- Closed at: 2018-11-05T07:10:23+00:00
