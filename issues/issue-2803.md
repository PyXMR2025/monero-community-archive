---
title: v6.16.2 fails to mine Randomx with RX580 (Windows 11)
source_url: https://github.com/xmrig/xmrig/issues/2803
author: UselessGuru
assignees: []
labels: []
created_at: '2021-12-08T08:58:04+00:00'
updated_at: '2021-12-25T04:50:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://user-images.githubusercontent.com/30080938/145178789-5dbba894-d1ef-46d2-a9d0-79ef61c11e9a.png)

RX5700 with same driver works fine

# Discussion History
## Titaniumtown | 2021-12-08T14:28:05+00:00
why are you trying to mine monero on your gpus lol

## Spudz76 | 2021-12-08T16:03:58+00:00
Probably mixed Ellesmere and Navi needs driver no newer than 21.6.1 or 21.7.2

## dastardlyman12 | 2021-12-08T21:44:17+00:00
uselessguru we respect you. what im doing is mining eth on my rx580 and converting it into the durrty

## Lonnegan | 2021-12-08T22:14:19+00:00
ETH or ERGO or XHV. But mining RandomX via GPU is a waste of energy or profits given away.

## UselessGuru | 2021-12-09T11:19:09+00:00
> why are you trying to mine monero on your gpus lol

I am the co-developer of www.nemosminer.com. Our aim is to support all POSSIBLE algos. The program will choose the best algorithm (and this will never be Monero on GPU's). But If don't include it then there will be questions like 'Why don't you support xyz...'.


## SChernykh | 2021-12-09T14:50:48+00:00
Try to set `"gcn_asm":false,` in config.json for that GPU. Maybe new AMD drivers and Windows 11 are not compatible with ASM implementations.

## UselessGuru | 2021-12-10T16:37:36+00:00
@SChernykh

Is there also a command line parameter for "gcn_asm":false, ?

## Titaniumtown | 2021-12-10T18:35:59+00:00
> > why are you trying to mine monero on your gpus lol
> 
> I am the co-developer of [www.nemosminer.com](http://www.nemosminer.com). Our aim is to support all POSSIBLE algos. The program will choose the best algorithm (and this will never be Monero on GPU's). But If don't include it then there will be questions like 'Why don't you support xyz...'.

MoneroOcean already exists lol....

## ghost | 2021-12-24T15:19:38+00:00
> @SChernykh
> 
> Is there also a command line parameter for "gcn_asm":false, ?

Yes, it can be specified in the config file, in the "profile" object.
Example:

`"opencl":
{
"enabled":true,
"loader":"Path_To_amdocl64.dll",
"adl":true,
"cache":false,
"platform":"AMD",
"rx":
[{
"intensity":<<See what is best for you>>,
"worksize":<<See what is best for you>>,
"gcn_asm":false,
"index":0},
{
"intensity":<<See what is best for you>>,
"worksize":<<See what is best for you>>,
"gcn_asm":false,
"index":1}
]}`

## Spudz76 | 2021-12-25T04:50:05+00:00
> Yes, it can be specified in the config file

That's not a command line parameter then, is it?

# Action History
- Created by: UselessGuru | 2021-12-08T08:58:04+00:00
