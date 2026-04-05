---
title: Why is cpu only used 50%
source_url: https://github.com/xmrig/xmrig/issues/2307
author: echolinzi
assignees: []
labels:
- question
created_at: '2021-04-24T03:53:11+00:00'
updated_at: '2022-04-03T14:40:27+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:40:27+00:00'
---

# Original Description
I used this syntax
./xmrig -o pool.minexmr.com:4444 -u 89*****6 --rig-id xmr1 --randomx-1gb-pages --cpu-max-threads-hint=100 -t=24

Why the CPU usage rate is 50%

How can I make the cpu usage reach 100% to improve my hashing power

![image](https://user-images.githubusercontent.com/50605203/115946358-35b51480-a4f3-11eb-8162-eea8305ee731.png)


# Discussion History
## Spudz76 | 2021-04-24T06:51:05+00:00
Your CPU probably has not enough cache to use all cores (don't know what model CPU since you didn't bother to say).  How much cache is needed per thread depends on the algo (which you also didn't bother to mention).

## zkysimon | 2021-05-10T14:04:14+00:00
> Your CPU probably has not enough cache to use all cores (don't know what model CPU since you didn't bother to say). How much cache is needed per thread depends on the algo (which you also didn't bother to mention).

![image](https://user-images.githubusercontent.com/61656204/117671597-8c9d3800-b1db-11eb-969a-20fae0889abb.png)
![image](https://user-images.githubusercontent.com/61656204/117671605-8f982880-b1db-11eb-92d9-32115761de08.png)
I have the same problem as him, can you help me?

## Spudz76 | 2021-05-10T17:40:27+00:00
Cloud mining doesn't work very well, so that's probably why.  A real Platinum 8272CL has 26 cores not four.  And the Azure cloud is likely not giving you all the cache either, and even if it did it's not "your cache" or even "your cpu" so you'll get evicted all the time which kills hashrate.

Mining needs the most direct access to the CPU and cache and memory as possible, unshared, not inside any VM.

## noche-de-brujas | 2021-05-23T03:15:52+00:00
> > Your CPU probably has not enough cache to use all cores (don't know what model CPU since you didn't bother to say). How much cache is needed per thread depends on the algo (which you also didn't bother to mention).
> 
> ![image](https://user-images.githubusercontent.com/61656204/117671597-8c9d3800-b1db-11eb-969a-20fae0889abb.png)
> ![image](https://user-images.githubusercontent.com/61656204/117671605-8f982880-b1db-11eb-92d9-32115761de08.png)
> I have the same problem as him, can you help me?

You need to change the threads and apply the msr to optimize the Intel processing, since as it is vps it will not give you all the hashrate
--threads=$cpu


![Screenshot_20210522-221129](https://user-images.githubusercontent.com/64865173/119246903-f78b2f00-bb4a-11eb-8340-410a09235c4c.png)


![Screenshot_20210522-220812~2](https://user-images.githubusercontent.com/64865173/119246913-0ffb4980-bb4b-11eb-9075-b2731402b92a.png)



## zkysimon | 2021-05-23T11:05:39+00:00
> > > Your CPU probably has not enough cache to use all cores (don't know what model CPU since you didn't bother to say). How much cache is needed per thread depends on the algo (which you also didn't bother to mention).
> > 
> > 
> > ![image](https://user-images.githubusercontent.com/61656204/117671597-8c9d3800-b1db-11eb-969a-20fae0889abb.png)
> > ![image](https://user-images.githubusercontent.com/61656204/117671605-8f982880-b1db-11eb-92d9-32115761de08.png)
> > I have the same problem as him, can you help me?
> 
> You need to change the threads and apply the msr to optimize the Intel processing, since as it is vps it will not give you all the hashrate
> --threads=$cpu
> 
> ![Screenshot_20210522-221129](https://user-images.githubusercontent.com/64865173/119246903-f78b2f00-bb4a-11eb-8340-410a09235c4c.png)
> 
> ![Screenshot_20210522-220812~2](https://user-images.githubusercontent.com/64865173/119246913-0ffb4980-bb4b-11eb-9075-b2731402b92a.png)

Thank you,but how to change the threads?

## noche-de-brujas | 2021-05-27T15:03:49+00:00
You need to add  --threads=$cpu
only you change the number of proccesador you have, you can even create your script that makes all that configuration automatically, so you generate the best optimization either for Intel /AMD, Ram memory, the size of the huge page, so when you install your script it does everything automatically, optimizing and setting the best configuration according to the processor you have, threads, etc, 



# Action History
- Created by: echolinzi | 2021-04-24T03:53:11+00:00
- Closed at: 2022-04-03T14:40:27+00:00
