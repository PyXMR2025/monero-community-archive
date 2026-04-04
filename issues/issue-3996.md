---
title: VERY WEIRD interface at computer wake up
source_url: https://github.com/monero-project/monero-gui/issues/3996
author: lpoirothattermann
assignees: []
labels: []
created_at: '2022-08-07T11:39:11+00:00'
updated_at: '2023-01-18T05:58:27+00:00'
type: issue
status: closed
closed_at: '2023-01-18T05:58:27+00:00'
---

# Original Description
Hello,

When woke up my computer I got this Monero GUI Interface.

![image](https://user-images.githubusercontent.com/68006124/183288557-00ebd8b2-2be7-4d29-b3b7-9cd4d5405644.png)

OS: Linux Mint 20.3

Ask me what informations you need :)

# Discussion History
## selsta | 2022-08-07T12:59:23+00:00
There isn't much we can do. This looks like either a buggy graphics card driver, or a buggy graphics card. Does this happen every time you open monero-gui?

## lpoirothattermann | 2022-08-07T13:03:50+00:00
Every time I woke up computer. Only happens with Monero GUI

## selsta | 2022-08-07T18:25:33+00:00
Are you able to update your graphics drivers? Otherwise you have to use monero-gui in software renderer mode by starting it with the `QMLSCENE_DEVICE=softwarecontext` env var. This doesn't appear as anything we can fix on our side.

## fugbixer | 2022-08-10T02:29:54+00:00
>Ask me what informations you need :)

Go to settings and than the info tab 
Graphics mode: ? Please give us what the GUI tell you.

>Every time I woke up computer. 

Maybe some sort of power saving mode causing a failure correctly addressing  / communicating with the GPU. 

NVIDIA / AMD / Intel build in GPU / no GPU / KVM? 

Are you sure your GPU works and the drivers are setup correctly? I assume its a NVIDIA problem. 
(Linux Mint had sometimes troubles to setup the kernel hooks in a right fashion - mainly due to NVIDIA driver changes and being crappy af , so no way to blame on linux mint ) 

## selsta | 2023-01-18T05:58:27+00:00
Closing due to inactivity and no reply from issue creator.

# Action History
- Created by: lpoirothattermann | 2022-08-07T11:39:11+00:00
- Closed at: 2023-01-18T05:58:27+00:00
