---
title: Xmrig virus
source_url: https://github.com/xmrig/xmrig/issues/460
author: robfpvgt
assignees: []
labels:
- av
created_at: '2018-03-17T18:24:33+00:00'
updated_at: '2018-11-05T13:00:16+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:00:16+00:00'
---

# Original Description
Sup fellas,
Recently got a infection of malware etc on my pc, got rid of it all exept xmrig , it's running in the background using all my CPU power.
Every time I end task it comes back , and if I try to locate the file it only shows up in my local/temp file
But annoying how it comes back every second I delete the process
Cheers rob 

# Discussion History
## 2010phenix | 2018-03-17T19:53:57+00:00
first  ... this is not virus but crypto miner.
second ... this is issue tracker
and for last if you have virus, ask google how to clean your PC.

## Zelecktor | 2018-03-17T20:52:11+00:00
Can you upload de file? maybe we can see the source code and try to find a way to delete it.

## Swardu | 2018-03-18T02:42:27+00:00
You can find the miner's location by going to task manager and open the process's path. If you can't figure out how to delete it, as a temporary solution, you can open config.json and remove the pool link, which should result the miner to stop.

If you can't find confg.json, then they're using params or their own version.

XMRig miner is a single .exe file, it doesn't re-open when you kill it. You're dealing with a malware that uses xmrig.

## robfpvgt | 2018-03-18T04:14:00+00:00
So the malware is making open again ?
I did follow the path and it's only location is in my local/temp file 
I delete from task manager then from the file location and 10'seconds later it's back 

## Zelecktor | 2018-03-18T04:20:12+00:00
How about registers? maybe there is a binary register. If the file is deleted it create a new one.
Do you use any antivirus? Norton have the function to block IPs related with cryptocurrency mining and block some "file intrussion".

## Swardu | 2018-03-18T12:31:39+00:00
Since you mentioned that you had malware injected, there might be a lot more than just XMRig left. I recommend you to back-up the important files to an external storage device or cloud, and re-install Windows from scratch.

## robfpvgt | 2018-03-18T14:35:26+00:00
I managed to get rid of 90% of it, I used hitman and ccleaner all thats left seems to be the xmrig
I tried to download xmrig to find and installer to (uninstall) but no luck 

Sent from my iPhone

> On 18 Mar 2018, at 8:31 pm, Swardu <notifications@github.com> wrote:
> 
> Since you mentioned that you had malware injected, there might be a lot more than just XMRig left. I recommend you to back-up the important files to an external storage device or cloud, and re-install Windows from scratch.
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub, or mute the thread.
> 


## Minipada | 2018-03-25T12:51:47+00:00
I was setting up a jenkins today on an AWS server. Not even 10 minutes after I was in, a job was added called 'Insecure jenkins' and it started downloading xmrig. We just need to protect

## danielhuang | 2018-03-30T13:42:14+00:00
Try using Process Hacker and locating the parent process, and deleting it

# Action History
- Created by: robfpvgt | 2018-03-17T18:24:33+00:00
- Closed at: 2018-11-05T13:00:16+00:00
