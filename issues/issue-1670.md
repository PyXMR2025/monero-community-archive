---
title: Why cpu only uses 50%??????????
source_url: https://github.com/xmrig/xmrig/issues/1670
author: vvring
assignees: []
labels: []
created_at: '2020-05-05T13:39:21+00:00'
updated_at: '2020-08-19T01:21:36+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:21:36+00:00'
---

# Original Description
Why cpu only uses 50%
Large memory support has been turned on
4pcs E7-4850 v3 how to set CPU
4 E7-4850 v3 112 cores only have 55 cores?
How should I set it up?

- 
![1](https://user-images.githubusercontent.com/47848167/81072480-c8425980-8f18-11ea-80d4-d9ee5cc16c66.PNG)
![2](https://user-images.githubusercontent.com/47848167/81072490-cb3d4a00-8f18-11ea-91a0-07797d97e902.PNG)
![3](https://user-images.githubusercontent.com/47848167/81072494-cc6e7700-8f18-11ea-888d-b3ffa04e2051.PNG)




# Discussion History
## Masterbob79 | 2020-05-05T17:15:11+00:00
"Yield": false might help

## Miner9009 | 2020-05-06T18:20:32+00:00
Cache requirements dude, 2MB per thread.

## divinity76 | 2020-06-15T23:02:46+00:00
***if you turn off hyperthreading in the BIOS, you will see that it's actually using ~100%***

wrong, you don't have 112 cores, you have 56 cores. 
thanks to hyperthreading, they look like 112 cores to the OS, but 50% of those cores are hyperthreaded virtual cores, and if you actually try to mine on the real core, and the hyperthreaded core simultaneously, your overall hashrate will actually go SLOWER than just mining on the real cores.

hence, xmrig actively avoids mining on the hyperthreaded cores, which seems, to the OS, like it's only mining on 50% of your cores (because the hyperthreaded cores are useless for mining)


# Action History
- Created by: vvring | 2020-05-05T13:39:21+00:00
- Closed at: 2020-08-19T01:21:36+00:00
