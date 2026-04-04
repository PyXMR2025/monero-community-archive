---
title: Raising the ringsize in the v10 hardfork, April 2019
source_url: https://github.com/monero-project/monero/issues/4827
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-11-09T04:21:56+00:00'
updated_at: '2022-02-22T21:39:27+00:00'
type: issue
status: closed
closed_at: '2022-02-22T21:39:26+00:00'
---

# Original Description
Let. The Games. Begin!

So, we're currently at a fixed ringsize of 11, because of obvious reasons.... mostly involving Spinal Tap and some math, but mostly Spinal Tap. In an ideal world, the ringsize would be the entire chain. In the real world we have functionality to think of, so we're obviously way under that because of raspberry pies. 

Who would have ever known that a fruit based pastry could get in the way of revolutionary internet money!?!>!>!

Pending any revolutionary change in ring signatures verification optimizations, new ring signatures schemes, or a completely different means of obfuscating the inputs to a transaction, I think a modest increase in the ringsize is warranted. 

Why?

Mainly to match the theoretical increase in overall infrastructure speed. There are probably some graphs I can show that would say "internet gets faster" and "computers get faster", and then hyc would come along and say "Moores law is dead! Long live entropy!", and then luigi would scold me for my grammar, but where we're going we don't need graphs.

So elect Ringsize 15 for v10 Hardfork April 2019! This Ringsize will bring you all of the promises that ringsize 11 couldn't deliver, like freedom from people looking at the monero blockchain and going "See, thats the real input _i know it_"

# Discussion History
## selsta | 2018-11-11T18:06:19+00:00
We could also continue with the next best prime, e.g. 17 :) (13 would be too close to 11).

## ghost | 2018-12-07T21:34:30+00:00
the ''optimal'' with current tech without compromising performance is between 10-20 so 17.

## KimWonLee | 2019-01-31T20:51:09+00:00
@lethos3 Where did you get those numbers from? How often do you believe the ringsize will need to be updated?

## SamsungGalaxyPlayer | 2019-02-01T03:41:29+00:00
11 vs 15
![image](https://user-images.githubusercontent.com/12520755/52101272-6c17b980-25a0-11e9-8b1b-8be5788b2e6a.png)

11 vs 17
![image](https://user-images.githubusercontent.com/12520755/52101286-7fc32000-25a0-11e9-8580-23e855046a26.png)

I haven't performed a cost-benefit analysis for ringsizes larger than 11. We're still fighting against increased verification times and transaction sizes. We need MRL to finish their transaction graph paper to get a better idea how these larger ringsizes help.

## Gingeropolous | 2019-02-01T12:46:38+00:00
11 is blue, orange is the higher number @SamsungGalaxyPlayer ?

# Action History
- Created by: Gingeropolous | 2018-11-09T04:21:56+00:00
- Closed at: 2022-02-22T21:39:26+00:00
