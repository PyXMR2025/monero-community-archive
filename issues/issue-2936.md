---
title: '"end of file" errors in the middle of mining v6.16.4'
source_url: https://github.com/xmrig/xmrig/issues/2936
author: Ralph416
assignees: []
labels:
- question
created_at: '2022-02-20T22:48:49+00:00'
updated_at: '2022-04-03T12:19:33+00:00'
type: issue
status: closed
closed_at: '2022-04-03T12:19:33+00:00'
---

# Original Description
![EndOfFile](https://user-images.githubusercontent.com/97701340/154867587-6c98609f-caba-4bd9-91a0-65a82910d747.jpg)

I'm getting this "end of file" error in the middle of mining RTM on minafacil. It seems to happen randomly when receiving a new job. It immediately resumes mining like nothing happened but I don't know if it's affecting the hashrate by doing this so often.

Also getting random "Invalid job id" messages..

![InvalidJobId](https://user-images.githubusercontent.com/97701340/154867723-a0c46fec-49f3-4b36-851b-71d03e8a1db1.jpg)

Don't know if the first error is causing the second error or if there's any correlation.


# Discussion History
## koitsu | 2022-02-23T01:00:32+00:00
First screenshot: "End of file" in this context means the remote server (pool) closed the TCP connection (either one that was already established that timed out due to inactivity or other anomalies, or a newly-attempted one got closed instead of a proper handshake).  When this happens, xmrig will stop mining briefly, re-look-up the DNS record for the pool (you can see the IP it shows) in the case that it changed, and essentially pick up where it left off.

This is actually a normal thing to have happen; the server/pool maintainers may be doing maintenance, cycling servers, etc..  I've seen it on every single pool I've participated in, varying across algos.  It's normal, as long as it's not "in excess" (i.e. constant, in which case there is probably an issue with your Internet connection, the Internet itself (likely), or with the pool provider).

In the case the TCP session is established and timing out, there is one thing you can use to minimise the issue (not solve, just minimise!): use `"keepalive": true` in the pool entry itself (in config.json).  Not all pools support this (if they say they do, great, but many which support it don't actually say so), but it allows for the TCP session to be kept up/alive through use of a ping-like communication method ("are you still there?" "yeah").

Second screenshot: This is not the same issue as in the first screenshot; totally separate/different.  This is the pool server telling you that the job ID you submitted is invalid.  This can happen for a multitude of reasons.  If you scour the Internet for information on this, a lot of people will blab about how it can be related to overclocking/etc..  In my case, since I do not OC and use stock everything, I know it's not that.  Instead, it's a rejected share that you've submitted to the pool when the rest of the pool has already solved it.  This is totally normal and expected, as long as you aren't seeing a ton of these (say, ~2% of all your submitted shares).  A better explanation comes from b-topmining.medium.com:

> Rejected shares represent work that will not be applied toward a round in a mining pool. It occurs when you find a share and submit it to the mining pool after the pool has already moved on to the next block. In that case, you will have some “invalid shares” which don’t count in terms of revenue share, in other words, you’ll not get paid by the mining pool. This happens not too often thus it is considered normal. If everything is working correct, the percentage of rejected shares should be around 1%.

A good pool provider will show you a dashboard with how many of your shares were invalid.  However, sadly, "rejected" shares in this scenario are often counted as "invalid" shares on pool dashboards, which makes differentiating them compared to overclocking issues/etc. very difficult.

In short: if this is just something you see "once in a while" (like, say, 1 per 1000 submitted shares), and the pool is particularly busy, then that's fine.  If you're seeing this happen constantly (say 100 per 1000 submitted shares), that's a problem and almost always an indicator of hardware problems on your side.

HTH, happy mining.

## Ralph416 | 2022-02-23T18:49:44+00:00
Wow, thank you such a detailed response. I suspect issue #1 was indeed something to do with the pool I was using, but the rejected shares are definitely not "stale" shares. Flockpool reports stales and rejects separately. I don't seem to get "invalid id" rejects using original RTM CPU miner. I'm not overclocking, in fact I'm locking my frequency at stock and disabled boost to minimize power consumption. It's just a small percentage of errors, less than 1%. I'm looking to maximize my efficiency, especially in this bear crypto market so I'm trying to eliminate all useless processing. I guess I'll just have to live with it.

## koitsu | 2022-02-23T21:08:48+00:00
No sweat!

I'm glad to hear that there's at least *one* pool out there which differentiates between "stale" (already-solved blocks) and rejected shares!  All the ones I've used lump everything into "invalid" (even when the pool reports back to the client "duplicate share"), which is extremely misleading.  I should look into Flockpool.  :)

In this case, yeah, I'm not sure what would be causing the pool to explicitly reject the job.  One thing you might try is launching xmrig with `--verbose` or add `"verbose": 999` to the `logging` section of your `config.json`.  [Docs on that option](https://xmrig.com/docs/miner/config/logging#verbose) (I'm not sure why the command-line flag doesn't accept a numeric value while the JSON parser does).  Maybe this will display the job ID which the pool claims is invalid -- I'm not sure.  @xmrig Do you have any ideas?

Otherwise it might be something you need to ask the pool maintainer/Support folks if they could assist in tracking it down.

## Ralph416 | 2022-02-23T23:15:19+00:00
Worst case, if I really want to follow that rabbit down its hole, any tips where I could put a breakpoint in the source to where this error is being generated? I'm using VS community 2022.

## rfiyoy | 2022-02-24T16:21:06+00:00
> ![EndOfFile](https://user-images.githubusercontent.com/97701340/154867587-6c98609f-caba-4bd9-91a0-65a82910d747.jpg)
> 
> I'm getting this "end of file" error in the middle of mining RTM on minafacil. It seems to happen randomly when receiving a new job. It immediately resumes mining like nothing happened but I don't know if it's affecting the hashrate by doing this so often.
> 
> Also getting random "Invalid job id" messages..
> 
> ![InvalidJobId](https://user-images.githubusercontent.com/97701340/154867723-a0c46fec-49f3-4b36-851b-71d03e8a1db1.jpg)
> 
> Don't know if the first error is causing the second error or if there's any correlation.



## toy1111 | 2022-02-26T04:31:21+00:00
Not sure why but I've experienced similar on other ghostrider pools. I'm thinking its common for RTM pools to get some rejected shares and times when the pool doesn't respond. I've got a 2nd pool set in xmrig and random times my miners switch to the 2nd pool but only for very short time. Ghostrider is algo switching every block and using 3 different algos per block so its not surprising to me it could lead to some issues on both the miner and pool. But it doesn't appear to be a bad problem - I only see about 0.1% rejected shares. Your screen shot shows 0.7% rejected but for only a short run and still not very bad. 

# Action History
- Created by: Ralph416 | 2022-02-20T22:48:49+00:00
- Closed at: 2022-04-03T12:19:33+00:00
