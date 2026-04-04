---
title: Monero over java I2P
source_url: https://github.com/monero-project/monero/issues/3689
author: life-coder
assignees: []
labels: []
created_at: '2018-04-23T13:57:29+00:00'
updated_at: '2018-04-24T06:49:40+00:00'
type: issue
status: closed
closed_at: '2018-04-24T06:49:40+00:00'
---

# Original Description
Since the kovri project is heavily in development I was wondering if it would be possible to allow users of java-I2P to use monero over I2P already?

After reading this https://www.reddit.com/r/Monero/comments/2ti53m/why_is_monero_aiming_to_integrate_i2p/ it appears that you aim to use SAM for communication with the router which is working in java-I2P.

So my question is, why not already implement everything needed to run monero over I2P? So people can use it over java-I2P and when kovri is stable they could switch to that implementation.

Best regards

# Discussion History
## anonimal | 2018-04-23T22:37:24+00:00
>it appears that you aim to use SAM for communication with the router which is working in java-I2P.

Hi @life-coder. That's a very out-of-date 3 year old comment that is no longer applicable.

>So my question is, why not already implement everything needed to run monero over I2P?

Ping @fluffypony. I don't feel like answering this for the Nth time. The answers should be stickied somewhere or put in a FAQ.

## SamsungGalaxyPlayer | 2018-04-24T03:46:59+00:00
@life-coder Monero will be much better off with a light I2P router implementation. See more background [here](https://btcmanager.com/what-is-kovri-why-is-it-important-for-monero/) and [here](https://forum.getmonero.org/9/work-in-progress/86967/anonimal-s-kovri-full-time-development-funding-thread).

There's no reason Monero *couldn't* work with the Java implementation, but it's not something the community has desired to spend resources on, figuring Kovri is a much more comprehensive solution for most people.

Zcash has shown interest in taking your approach, but the [related ticket](https://github.com/zcash/zcash/issues/1111) hasn't seen any progress in the past year.

## life-coder | 2018-04-24T06:49:40+00:00
@anonimal oh I see,
@SamsungGalaxyPlayer thanks
Found this https://github.com/monero-project/monero/issues/1178 and read the dev meeting log.

Also read that Zcash issue, like @SamsungGalaxyPlayer says, monero is probably better off with a light I2P implementation. But I dont think every I2P user that wants to run a monero node will give up java I2P, with it's web interface and plugin support.
That said, I'll just wait and see and maybe contribute whatever I can. Thanks for taking time to respond

# Action History
- Created by: life-coder | 2018-04-23T13:57:29+00:00
- Closed at: 2018-04-24T06:49:40+00:00
