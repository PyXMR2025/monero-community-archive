---
title: Prevent windows defender from being found
source_url: https://github.com/xmrig/xmrig/issues/3265
author: Unbrecht
assignees: []
labels:
- av
created_at: '2023-05-07T20:50:33+00:00'
updated_at: '2024-02-14T18:22:00+00:00'
type: issue
status: closed
closed_at: '2023-06-07T14:54:45+00:00'
---

# Original Description
When i build xmrig from source and move it or copy to another Computer, Windows Defender will remove xmrig.exe.

I know the solution to make a exception for xmrig in Windows defender. 
What i want to know is why xmrig was detected or rather what can i do to prevent this. What lines of Code i must change or is this not possible?

In a older xmrig version i try to replace all "miner" keywords to a pseudoname. My feeling was that fewer Computers found xmrig but not all.. 

I work on Windows 10 Pro with the newest Updates and xmrig version.

Maybe someone know the reason and can help. Thanks! 

# Discussion History
## Spudz76 | 2023-05-07T23:41:29+00:00
Not possible.

## Unbrecht | 2023-05-08T14:02:11+00:00
how does nicehash do it? When i install the APP including Miners (Xmrig,...) i don´t have any Windows defender messages..

## Spudz76 | 2023-05-09T00:01:53+00:00
Must require admin privileges, and must add its own exceptions.

## geekwilliams | 2023-12-27T21:11:14+00:00
> When i build xmrig from source and move it or copy to another Computer, Windows Defender will remove xmrig.exe.
> 
> 
> 
> I know the solution to make a exception for xmrig in Windows defender. 
> 
> What i want to know is why xmrig was detected or rather what can i do to prevent this. What lines of Code i must change or is this not possible?
> 
> 
> 
> In a older xmrig version i try to replace all "miner" keywords to a pseudoname. My feeling was that fewer Computers found xmrig but not all.. 
> 
> 
> 
> I work on Windows 10 Pro with the newest Updates and xmrig version.
> 
> 
> 
> Maybe someone know the reason and can help. Thanks! 

I know it's a pain, but you can also add an exemption to a directory, or just the executable itself to windows defender. The powershell command is MP-Preference -ExclusionPath {path}, or you can do it through the Defender UI also


## Unbrecht | 2023-12-29T15:17:07+00:00
I know. I build an installer to bypass uac and many virus software. 
I running the app on many devices but I stopping wasting my time because the yields were too bad.


# Action History
- Created by: Unbrecht | 2023-05-07T20:50:33+00:00
- Closed at: 2023-06-07T14:54:45+00:00
