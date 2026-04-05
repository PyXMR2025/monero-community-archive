---
title: amd gpu mining not working
source_url: https://github.com/xmrig/xmrig/issues/2469
author: arya6345
assignees: []
labels: []
created_at: '2021-07-02T14:17:36+00:00'
updated_at: '2021-07-03T03:45:39+00:00'
type: issue
status: closed
closed_at: '2021-07-03T03:45:39+00:00'
---

# Original Description
CL_INVALID_HOST_PTR when calling clCreateBuffer with buffer size 2181038080

run the xmrig.exe to reproduce the behavior

just an error message like i said

![image](https://user-images.githubusercontent.com/86840789/124287572-5eecc380-db7a-11eb-87d7-b1745fb9ae5f.png)
OS is windows 7
![image](https://user-images.githubusercontent.com/86840789/124287791-a2dfc880-db7a-11eb-9103-b222537bbfb9.png)
![image](https://user-images.githubusercontent.com/86840789/124287847-b2f7a800-db7a-11eb-9291-fee61faefc9f.png)
![image](https://user-images.githubusercontent.com/86840789/124287916-c440b480-db7a-11eb-9e78-b4b40745dc7a.png)
![image](https://user-images.githubusercontent.com/86840789/124287981-d7ec1b00-db7a-11eb-822c-2593490a4db9.png)

The gpu is a Ati radeon hd 5570


# Discussion History
## SChernykh | 2021-07-02T14:22:42+00:00
RandomX dataset is 2 GB. Your GPU has 1 GB, system memory is 2 GB with only 0.5 GB free. Of course it can't allocate dataset anywhere.

## arya6345 | 2021-07-02T15:16:24+00:00
> RandomX dataset is 2 GB. Your GPU has 1 GB, system memory is 2 GB with only 0.5 GB free. Of course it can't allocate dataset anywhere.

can you tell me how to edit random dataset ?

## Spudz76 | 2021-07-02T17:35:26+00:00
You don't it's a requirement.  2080MB of dataset for RandomX.

Also Turks based GPUs don't work right with any driver newer than 15.x

## arya6345 | 2021-07-02T22:06:32+00:00
> You don't it's a requirement. 2080MB of dataset for RandomX.
> 
> Also Turks based GPUs don't work right with any driver newer than 15.x

ok but can you tell how to change the algo to cryptonight ? and after this message have been replied i'm gonna close the issue

## Spudz76 | 2021-07-02T22:29:32+00:00
Well you find a pool that serves your desired algorithm and configure it as your pool.  When it sends a job in a cryptonight algorithm, xmrig will follow along.

Currently you're mining on the donation pool because you've used the default/example config.json file. So even if you forced the algo it would just not work right (jobs being served by the pool are still `rx/0`).

## arya6345 | 2021-07-02T22:40:56+00:00
> Well you find a pool that serves your desired algorithm and configure it as your pool. When it sends a job in a cryptonight algorithm, xmrig will follow along.
> 
> Currently you're mining on the donation pool because you've used the default/example config.json file. So even if you forced the algo it would just not work right (jobs being served by the pool are still `rx/0`).

yeah but i'm gonna mine on hashvault so how to edit the algo of the miner ?

## arya6345 | 2021-07-02T23:46:56+00:00
or what pool should i use then sends the job in cryptonight ?

## arya6345 | 2021-07-03T03:45:33+00:00
Closing this issue..

# Action History
- Created by: arya6345 | 2021-07-02T14:17:36+00:00
- Closed at: 2021-07-03T03:45:39+00:00
