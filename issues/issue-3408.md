---
title: Miner not doing anything when run
source_url: https://github.com/xmrig/xmrig/issues/3408
author: Jinxsyns
assignees: []
labels: []
created_at: '2024-01-26T08:47:41+00:00'
updated_at: '2025-06-18T22:39:35+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:39:35+00:00'
---

# Original Description
So it's setup exactly the same as at a different location with a different windows pc. 

the batch file script is 
xmrig.exe -a ghostrider -o stratum+tcp://ghostrider.na.mine.zergpool.com:5354 -u 0xe2154301861355cd3E6203e19a068F03c10b2BAA -p  c=USDT-BEP20,mc=RTC,ID=laggys first rig
pause

also if clicking on the XMrig application in the file works fine and mines. but this is what happens when trying to open this reaction ghostrider batch file.


![poop2_rig](https://github.com/xmrig/xmrig/assets/130711085/71bcc8fc-0722-4e6a-972b-74cce1cb761e)



then nothing ever


# Discussion History
## geekwilliams | 2024-01-26T09:00:50+00:00


```
-p c=USDT-BEP20,mc=RTC,ID=laggys first rig
```

I think the spaces in ID=laggys first rig may be causing the problem. You could try putting quotes around the whole thing like: 

```
-p "c=USDT-BEP20,mc=RTC,ID=laggys first rig"
```

Edit: after checking out the pool page, I see what you're trying to do. Please replace spaces in "laggys first rig" with non-white space characters (like - or _) and try again.

## Jinxsyns | 2024-01-26T13:26:58+00:00
I apologize that's my fault I pasted the wrong thing we removed those already and it still isn't working i apologize for the wasted time.

## sergik7777 | 2024-02-10T19:37:30+00:00
у меня таже проблема что делать?

## sergik7777 | 2024-02-10T19:51:51+00:00
![Снимок экрана (2)](https://github.com/xmrig/xmrig/assets/159652031/73521ba9-44df-4371-9356-0973280014d2)


## koitsu | 2024-03-19T06:54:18+00:00
I have personally seen this problem many times, but only recall it happening on Windows (though my memory could be wrong).  MSVC and GCC builds both do this, so it's not a compiler issue.  Debugging/troubleshooting it is difficult without a custom-built Windows binary that includes debug support.  My line of thinking is that it could be a stalled DNS lookup, a TCP connection that is stalled (high backlog on server), or a TLS handshake that is not completing quickly.  I **have not** performed packet captures when this happens, since to figure out where the stall is happening I really need both things (debug binary and packet captures).

I tend to Ctrl-C XMRig, wait a few seconds and try again, and it usually works.  And yes, for what it's worth, I also use Zergpool.

@sergik7777 Your issue is something entirely different.

# Action History
- Created by: Jinxsyns | 2024-01-26T08:47:41+00:00
- Closed at: 2025-06-18T22:39:35+00:00
