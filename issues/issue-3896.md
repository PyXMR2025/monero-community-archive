---
title: '[Performance BUG] Lag after GUI is open for a while'
source_url: https://github.com/monero-project/monero-gui/issues/3896
author: elibroftw
assignees: []
labels: []
created_at: '2022-04-27T15:23:04+00:00'
updated_at: '2023-01-21T09:35:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It takes 3s for the send transaction button in the address book to populate a row in the send page.


Demo: 

https://user-images.githubusercontent.com/21298211/165557394-1189dcca-e6e2-4986-977e-8d322b0ded0e.mp4

# Discussion History
## selsta | 2022-04-30T07:40:59+00:00
Some of these bugs a bizarre. It works instantly on my system. I wonder what can cause a 3 second difference.

## elibroftw | 2022-05-17T03:21:26+00:00
Selsta, this bug is similar to the async bug. If I open the GUI for more than a couple hours, the entire GUI is laggy. On a fresh start of the GUI, this address bug does not exist.

## elibroftw | 2022-05-17T17:34:02+00:00
Actually it might just be the first instance of monero-gui that has problems. I have monero-gui start on my Windows startup and everytime since the wallet close fix it behaves so low..

## selsta | 2022-05-17T17:35:14+00:00
What do you mean with first instance?

## elibroftw | 2022-05-17T17:35:29+00:00
nvm it's still laggy.

## selsta | 2022-05-17T17:36:13+00:00
Can you reproduce this on every computer you own?

## elibroftw | 2022-05-17T17:36:58+00:00
I'll try it on my laptop

## elibroftw | 2022-05-17T17:54:48+00:00
well well well, my laptop runs without lag. I'll try reinstalling the GUI on my PC.

## selsta | 2022-05-17T18:40:42+00:00
One thing you can test is if you start low-graphics-node on your PC and check if you also have this issue.

## elibroftw | 2022-05-17T20:50:49+00:00
It might have to do with the wallet itself since a reinstall didn't fix the performance issues.

## selsta | 2022-05-17T21:33:26+00:00
@elibroftw please try low graphics mode so we can check if it's an graphics issue.

## elibroftw | 2022-05-17T23:04:41+00:00
Bug still exists when running low graphics mode

## ahmafi | 2023-01-21T07:43:12+00:00
I have the same issue, it lags the entire system for me!

I'm using fedora 37, GNOME.

## selsta | 2023-01-21T09:17:55+00:00
@ahmafi can you post more information? how long does it take until you it causes slowdowns on your system? are you running a local node?

## ahmafi | 2023-01-21T09:33:04+00:00
> @ahmafi can you post more information? how long does it take until you it causes slowdowns on your system? are you running a local node?

I'm starting a local node, and it's syncing for the first time. It lags almost from the beginning, I can't say for sure, but I think it lags mostly when it's downloading at higher speed (on network spikes).
I'm also using a SSD and an Intel CPU.

```
[21/01/2023 12:55] 2023-01-21 09:25:52.335 I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Height: 2348584/2804361 (83.7%) on mainnet, not mining, net hash 2.08 GH/s, v14, 32(out)+0(in) connections, uptime 0d 3h 49m 44s
```
(I have increased the output connections to 32, but it also happened when it was the default 12 connections)

I will also check if it slows the system after the first sync completed and post the results here.
I can also provide more info if you say exactly what you need.

## selsta | 2023-01-21T09:34:59+00:00
I don't think your issue is related to this issue here, your slowdown is likely due to syncing a node, not the GUI itself. Please report back after syncing is finished.

# Action History
- Created by: elibroftw | 2022-04-27T15:23:04+00:00
