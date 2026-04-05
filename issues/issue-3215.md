---
title: XMRig randomly disconnects from unMineable on raspberrypi
source_url: https://github.com/xmrig/xmrig/issues/3215
author: SeaPickle754
assignees: []
labels: []
created_at: '2023-02-23T16:28:11+00:00'
updated_at: '2025-06-18T22:48:02+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:48:02+00:00'
---

# Original Description
**Problem**
Hello, I am trying to mine some Dogecoin with unmineable on my raspberry pi 3 B. I know that this will not make much money, but it is something I want to do before I buy an ASIC. I am just trying to get into mining. Anyways, my issue is that it will randomly go offline    when I check unmineable. Sometimes it will mine a small amount of Doge, but then it goes offline and disconnects. I have regenerated config.json, and tried to use the command line. I have even created a new wallet and address, which did not fix the problem. My raspberry pi is overclocked in /boot/config.txt by setting arm_freq to 900. I have a heatsink and fan setup, and as far as I know, it has not gone over 60C. I am also using ssh to configure everything, and screen to keep it alive after I close the window.

**To Reproduce**
I haven't been able to find any help online, which makes me hesitant to assume you can reproduce it. Anyways:
Raspberry pi is running 64-bit Raspbian.
Config.json is from ```wget https://raw.githubusercontent.com/xmrig/xmrig/master/src/config.json```
Change your Coin to Doge, and your wallet address. Also add a worker name, which I did. Also, I set the "url" field to rx.unmineable.com:3333. 

**Expected behavior**
I expected my raspberry pi to just be able to be left on and continue working. I want to be able to mine continuously, instead of trying to trouble shoot it because it is randomly going offline.

**Required data**
 - Startup:
![image](https://user-images.githubusercontent.com/62182495/220967631-f016f28f-3abf-428d-9795-684109cc09dd.png)
- Config.txt "pools" section
![image](https://user-images.githubusercontent.com/62182495/220968028-4893fa22-5668-4aa3-9766-8d234e100f88.png)
- Unmineable page (Confirmed wallet address)
![image](https://user-images.githubusercontent.com/62182495/220968535-724a6154-89e3-4e12-bb53-87749ea3ced1.png)

**Additional context**
Thank you in advance, I really have no idea if this is a problem with unmineable or xmrig. As I said earlier, I have googled the problem over and over again and I have found no working fixes. Good luck!


# Discussion History
## SeaPickle754 | 2023-02-23T18:11:11+00:00
More info:
Top 1 hour later:
![image](https://user-images.githubusercontent.com/62182495/220992914-cce0bb2d-ac45-4500-a5e6-b196bbf2bc21.png)

So, still running...
![image](https://user-images.githubusercontent.com/62182495/220993059-8cbd2d49-b2ca-4f0a-ae37-9b9891613f2c.png)
Still getting shares...

![image](https://user-images.githubusercontent.com/62182495/220993402-73a47a3a-4299-48f4-bcc9-5163eceee1d1.png)
Still not registered.

## Spudz76 | 2023-02-24T07:29:33+00:00
Diff of `100001` divided by 30 means your hashrate should be at least 3333.  Pi4 usually is something like 100 meaning you need a diff of 100*30=3000 to ever find results without timing out.  Not sure if unmineable offers a vardiff port or a way of requesting a smaller fixed diff but that's what you need.

## SeaPickle754 | 2023-02-24T22:37:14+00:00
Ok so I just figure out how to lover the diff to 3000?

## SeaPickle754 | 2023-02-24T22:38:47+00:00
*lower

## SChernykh | 2023-02-25T08:41:22+00:00
This is the question to the pool you're mining on.

## SeaPickle754 | 2023-03-06T02:06:35+00:00
Ok. So, after a quick google search, it looks like unmineable won't go lower that 50000 diff. Can anybody recommend an easy dogecoin pool with a vardiff port?

## aalfiann | 2023-03-25T10:19:04+00:00
worker not detected because you mining with slow mode.

Just increase your RAM up to 2Gb, then your problem will solved automatically.

# Action History
- Created by: SeaPickle754 | 2023-02-23T16:28:11+00:00
- Closed at: 2025-06-18T22:48:02+00:00
