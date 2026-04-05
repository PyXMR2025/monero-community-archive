---
title: How do I chose RandomX algorithim in the config?
source_url: https://github.com/xmrig/xmrig/issues/2459
author: Joe23232
assignees: []
labels:
- question
created_at: '2021-06-27T08:25:17+00:00'
updated_at: '2021-06-28T12:23:04+00:00'
type: issue
status: closed
closed_at: '2021-06-28T12:23:04+00:00'
---

# Original Description
So I am using [QRL](https://www.theqrl.org/) which supports RandomX.

![image](https://user-images.githubusercontent.com/34926497/123537794-aa673200-d774-11eb-9258-5fcbf624afb0.png)

In the config file configuration, how do I set it for RandomX?

# Discussion History
## ghost | 2021-06-27T12:13:06+00:00
if not available in preset mode pools mean you can retry at custom pool configuration

## Joe23232 | 2021-06-27T12:14:56+00:00
@cmxhost Where would I go to create a custom pool configuration?

## ghost | 2021-06-27T12:18:02+00:00
just start from begining wizard
you will see at pool selection

## Joe23232 | 2021-06-27T12:24:12+00:00
@cmxhost 

![image](https://user-images.githubusercontent.com/34926497/123544355-3c336700-d796-11eb-8f2d-085393b9b0f6.png)


Ok so I can't seem to find RandomX in the Algorithm section and also I thought it would work with QRL as under the coin section I can't find QRL support.

## ghost | 2021-06-27T12:26:16+00:00
just select rx/0

## Joe23232 | 2021-06-27T12:27:01+00:00
@cmxhost  And what about the Coin support, should I keep it at unspecified?

## ghost | 2021-06-27T12:27:32+00:00
just leave it blank


## Joe23232 | 2021-06-27T12:33:04+00:00
@cmxhost THanks mate :)

ANother thing, 

[https://www.theqrl.org/](https://www.theqrl.org/) I am going here now and how do I find out the host and port number as it asks over here:

![image](https://user-images.githubusercontent.com/34926497/123544638-93860700-d797-11eb-963b-a82753073cae.png)


Also you see the three options `NiceHash` etc, which one should I pick?

## ghost | 2021-06-27T12:34:43+00:00
if pool provider support nicehash then you can tick nicehash and as per pool address and port

## Joe23232 | 2021-06-27T12:39:27+00:00
@cmxhost Since I don't really understand how this stuff works,

I ALWAYS need a host and port number, am I correct?

## ghost | 2021-06-27T12:39:59+00:00
yeah both are must

## Joe23232 | 2021-06-27T12:41:45+00:00
I see, thanks mate @cmxhost  :)

## Joe23232 | 2021-06-27T12:43:21+00:00
@cmxhost Sorry another thing.

From QRL wallet, I was provided a `json` file which gives me the `address` and `addressB32`, I would assume I would be putting the `address` (from the `*.json` file) into the `User` field, am I correct?

## ghost | 2021-06-27T12:44:36+00:00
just fill in and try first

user field is wallet address

## Joe23232 | 2021-06-27T12:58:32+00:00
@cmxhost Thanks man,

Another question, I noticed that on this website that allows you to create the config file: http://pool.qrlmining.com/#getting_started

It asks for the hardware specification as shown in the image:

![image](https://user-images.githubusercontent.com/34926497/123545383-0f358300-d79b-11eb-9f43-2c85a68a8e8d.png)

but with xmrig's version it does not. So what is the hardware specification set to by default?

## Joe23232 | 2021-06-27T13:02:04+00:00
@cmxhost Sorry I meant like becase xmrig does not ask you the hardware specification, what is the default hardware specification set to?

## ghost | 2021-06-27T13:04:50+00:00
> @cmxhost Sorry I meant like becase xmrig does not ask you the hardware specification, what is the default hardware specification set to?
check on your system 


## Joe23232 | 2021-06-27T13:15:15+00:00
@cmxhost I mean like inside the `json` file, what is the hardware specificaiton set to since xmrig's own wizard does not give such options?

## ghost | 2021-06-27T13:27:04+00:00
will autodetect by xmrig just start sudo ./xmrig

## Joe23232 | 2021-06-28T11:39:57+00:00
@cmxhost Thanks mate :)

In regards to [this](https://github.com/xmrig/xmrig/issues/2462#issuecomment-869611773) post that I made, what default `config.json` (that I got from forking the source code) elements do I need to change?

# Action History
- Created by: Joe23232 | 2021-06-27T08:25:17+00:00
- Closed at: 2021-06-28T12:23:04+00:00
