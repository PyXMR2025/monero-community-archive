---
title: Share above target
source_url: https://github.com/xmrig/xmrig/issues/1523
author: hackerzade
assignees: []
labels: []
created_at: '2020-01-31T19:08:49+00:00'
updated_at: '2020-02-03T06:59:41+00:00'
type: issue
status: closed
closed_at: '2020-02-03T06:59:41+00:00'
---

# Original Description
Hello,i have a little idea about mining and i met this issue. I am mining XMR via nicehash.While i am mining i allways see red letters with 'Share above target' and i am adding photo too. I found a solution about it via forums but i could not understood what to do. it is here : https://github.com/xmrig/xmrig/issues/458 

I dont know how to set --variant 0. i need some help about it. i got no idea how to do it.
Thank you.
![help](https://user-images.githubusercontent.com/60521964/73566935-3c7ee400-4476-11ea-9c09-e956e1399d3e.jpg)



# Discussion History
## hackerzade | 2020-01-31T19:14:10+00:00
And i do not know why my ms is high like that. I am using GPU mining same time with CPU mining. is it causes that high ms? 

## ValoWaking | 2020-01-31T23:01:49+00:00
do you have any overclocked parts in your system?

## hackerzade | 2020-01-31T23:13:31+00:00
No,i did not.

## xmrig | 2020-02-01T09:02:02+00:00
I just check I works fine, is this issue still persists? if case if it nicehash.com related issue. Make sure you enable nicehash in config `"nicehash": true,`

You use GPU for mine another coin or for RandomX? Anyway you can disable it temporary and please note nicehash.com will not pay you in XMR.
Thank you.

## hackerzade | 2020-02-01T09:09:35+00:00
There was no config as "nicehash": true in general.json file . I am using my GPU for random highest rated coins but i am mining XMR with my CPU.

## xmrig | 2020-02-01T09:22:01+00:00
https://github.com/xmrig/xmrig/blob/master/src/config.json#L63

## hackerzade | 2020-02-01T09:42:37+00:00
There are too much difference between this json and mine. its interesting.

## hackerzade | 2020-02-01T09:44:56+00:00
I will copy old one to somewhere else and i will use new one with making changes for wallet adress.
Thank you.

## implodnik | 2020-02-02T22:29:53+00:00
There was a problem on the EU Nicehash servers on Jan. 31st, everyone got there 100% rejects with "share about target" reason, then just "internal server error"s . US servers worked fine.

# Action History
- Created by: hackerzade | 2020-01-31T19:08:49+00:00
- Closed at: 2020-02-03T06:59:41+00:00
