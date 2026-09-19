---
title: corrupted text everywhere
source_url: https://github.com/monero-project/monero-gui/issues/3338
author: fatmalama
assignees: []
labels: []
created_at: '2021-02-15T21:38:54+00:00'
updated_at: '2022-04-26T18:39:21+00:00'
type: issue
status: closed
closed_at: '2022-04-26T18:39:21+00:00'
---

# Original Description
with the monero-gui-v0.17.1.9 linux binary and compiling from git, many texts are corrupted throughout the GUI
[screenshot](https://i.imgur.com/oJUF4hn.png)
[better screenshot](https://i.imgur.com/GKP8UjM.png)

on monero-gui-v0.16.0.3 this does not happen

# Discussion History
## dEBRUYNE-1 | 2021-02-16T17:02:37+00:00
Can you try launching the GUI as follows?

`QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui`

## fatmalama | 2021-02-16T17:06:15+00:00
> Can you try launching the GUI as follows?
> 
> `QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui`

yeah, that works

## selsta | 2021-02-17T14:37:00+00:00
@mikelpr This seems to be an issue with your graphics drivers. Can you try (re)installing / updating your graphics drivers and make sure they properly support opengl?

## fatmalama | 2021-02-18T03:10:13+00:00
@selsta I'm using amdgpu and radionsi. not thinking about moving to amdgpu pro. should I file a bug over at radionsi? also it could be a Qt bug

## selsta | 2022-04-26T18:39:21+00:00
I'll close this as this is a single report and it sounds like a graphics driver issue. There isn't much we can do here.

# Action History
- Created by: fatmalama | 2021-02-15T21:38:54+00:00
- Closed at: 2022-04-26T18:39:21+00:00
