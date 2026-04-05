---
title: 'is it possible to mine BEAM with xmrig? '
source_url: https://github.com/xmrig/xmrig/issues/2189
author: AlberoPazzo
assignees: []
labels: []
created_at: '2021-03-17T11:16:33+00:00'
updated_at: '2021-03-18T11:44:56+00:00'
type: issue
status: closed
closed_at: '2021-03-18T11:44:32+00:00'
---

# Original Description
hi, I've been using this miner for a while mining monero with cpu tried on both linux and windows and damn, i love it, but i was wondering if it is possible to make xmrig mine BEAM, is this crypto available for mining on the coin parameter? also i dont see the algorithm used for the mining of this crypto called Beam Hash III so i think there is no way to mine it with xmrig i guess, im not an expert so i might be wrong.
if it is possible could you explain how do i do that? i just have to place "beam" on the coin parameter or i have to put an algo parameter and i am done?
if there isn't a way because it is not available yet, could you add it please? it would be really great!
this is the site of the team of beam beam.mw

# Discussion History
## Lonnegan | 2021-03-17T11:47:20+00:00
Beam uses an algo that is related to the Equihash family used in ZCache or Bitcoin Gold. So you for sure will find Beam support in miners which are at home in this corner.

## AlberoPazzo | 2021-03-17T11:55:04+00:00
> Beam uses an algo that is related to the Equihash family used in ZCache or Bitcoin Gold. So you for sure will find Beam support in miners which are at home in this corner.

but the miners that beam suggest for mining only uses GPU and if you don't have one the miners will not start, or you are saying to search for a cpu miner used to mine zcash and bitcoin gold, since they use the algo related to the new used my beam, so a miner that uses equilash could mine BEAM? or im totally wrong and i dont understand because im stupid, if i didn't understand please be patient and could you explain better? 

## Lonnegan | 2021-03-17T12:18:21+00:00
Not each miner which supports Equihash also supports Beam. But since Beam is a variant of Equihash, the developers, who already have a miner with Equihash support, can easily adopt it to support Beam, as well. xmrig doesn't support Equihash since it has its heritage in Cryptonote. The xmrig developers would have to write everything from scratch to support Beam.

Equihash is an algo for GPUs. It doesn't make much sense to mine Equihash via CPU. But go to the "Start" section of the pool beam.herominers.com , there you'll find a list of miners which support Beam, a few even support CPU mining.

## AlberoPazzo | 2021-03-17T12:33:11+00:00
ok im gonna try searching there i will be back in a couple of hours, btw nice explanation of everything, thanks! 

## AlberoPazzo | 2021-03-18T11:15:34+00:00
ok is been a day and i didn't find a cpu miner for mining beams i installed every single one and the miners won't even start, btw then i decided to mine DERO instead, but i figured out that it lowers the hashrate like a lot, with the randomX algo used by default from xmrig i get something like 400/300 h/s but now with astrobwt for mining dero i only get 50.. for the beam mining i gave up, but what about mining dero? is there anyway to still get those 400/300 h/s with that different algo? 

## Lonnegan | 2021-03-18T11:29:38+00:00
You can't compare the hashrate values of different algos! The same CPU here does e.g. 6300 H/s with RandomX (Monero), but only 220 on CN-Heavy (Haven) or  170 H/s with AstroBWT (Dero). To compare how profitable or not an algo is for your Hardware, you have to take these values and type them into the calculator of each coin. Then you'll learn how much $ per day you'll get. Most pools have a calculator, just use them :)

## AlberoPazzo | 2021-03-18T11:44:32+00:00
Thanks Lonnegan, you helped me A LOT! Have a nice day man thanks again for your patience and time! i really appreciate that. 

# Action History
- Created by: AlberoPazzo | 2021-03-17T11:16:33+00:00
- Closed at: 2021-03-18T11:44:32+00:00
