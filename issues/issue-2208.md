---
title: '"Mode selection"-window: Wording overhaul'
source_url: https://github.com/monero-project/monero-gui/issues/2208
author: ghost
assignees: []
labels: []
created_at: '2019-06-10T16:29:32+00:00'
updated_at: '2019-09-04T09:38:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![monero3](https://user-images.githubusercontent.com/46682965/59207445-5eee8500-8ba7-11e9-8be7-ab2343bec5d0.jpg)

Issues:

1.) The term "bootstrap" is already used by many other projects for accelerated blockchain downloads over a 3rd-party bypassing the p2p-protocol. Contrary to that, in Monero-GUI the term is currently used to describe the concept of temporarily connecting to a remote node while the blockchain is downloaded in the background. This is unexpected, confusing wording.

2.) The actual difference between "Simple mode" and "Simple mode (bootstrap)" is not described at all. For example, a user has no chance to know, that "Simple mode (bootstrap)" will allow him to use his wallet instantly, or what that mode does at all.

3.) It is not indicated, what the EFFECTIVE consequences of the different modes are. But that's what's most important for (new!) users.

4.) In the description of Advanced mode it says "The blockchain is downloaded to your computer" - which is not correct, because the user has all options in Advanced mode.

![monero 3 vorschlag](https://user-images.githubusercontent.com/46682965/59210146-2a7dc780-8bad-11e9-97e3-c71a94276c33.jpg)


# Discussion History
## sanderfoobar | 2019-06-10T17:34:14+00:00
I like the proposed changes.

## notmike-5 | 2019-06-28T05:21:29+00:00
#2236 

## sanderfoobar | 2019-07-15T18:36:37+00:00
People on IRC (`#monero-gui`) do not seem to like this change. Specifically; dEBRYUNE/sgp/ErCiccione. In order for this to go in, you'll have to convince multiple people - I don't have the energy for it so I'm closing my PR over at #2280

## notmike-5 | 2019-07-15T18:57:30+00:00
I have also closed #2273 so as to satisfy the Monero Politboro and Central Committee. 

## sanderfoobar | 2019-07-15T19:03:49+00:00
That's kind of stretching it @notmike-5 ;-)

## ghost | 2019-07-15T20:41:44+00:00
That's why I gave 4 reasons why the changes are important, so that people can argue against it (instead of having to say "they don't like it" on IRC.)

Seriously: That bootstrap-mode is ANYTHING but self-explaining. And currently it is not explained at all! Sure, no problem for veterans. But for newcomers it's a slap in the face.

## dEBRUYNE-1 | 2019-07-18T12:36:06+00:00
@Realchacal - I was opposed to the changes mainly because it included the terms remote node and local node. New users are not acquainted with those terms and therefore they arguably should not be used. Do you have any suggestions on new wording without these terms? 

## ghost | 2019-07-18T13:03:28+00:00
@dEBRUYNE-1 fair point! We could make it this way:

- Simple mode (quick)
Basic functionality. You are connected to a third party, resulting in reduced privacy.

- Simple mode (quick + privacy)
Basic functionality. You are temporarily connected to a third party, while the blockchain is downloaded in the background. Once the download is complete, you will have maximum privacy.

- Advanced mode (maximum privacy)
Includes extra features like mining and message verification. By default, the blockchain is downloaded to your computer.





## ghost | 2019-07-21T09:45:05+00:00
Can one of the veterans say if we're going to do this now? And then someone put it into code? (I won't cause I can't.)

## notmike-5 | 2019-07-21T16:24:30+00:00
@Realchacal I think they already said no. PR #2273 has the code you're looking for.

## selsta | 2019-07-21T16:29:17+00:00
No we didn’t say no, else the issue would be closed.

## ghost | 2019-07-27T14:55:59+00:00
I consider this proposal just a quick & dirty improvement. #2321 is the real solution.

# Action History
- Created by: ghost | 2019-06-10T16:29:32+00:00
