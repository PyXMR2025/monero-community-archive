---
title: H/s higher on CLI than mining pool stats
source_url: https://github.com/xmrig/xmrig/issues/2145
author: noatte
assignees: []
labels: []
created_at: '2021-03-01T14:18:42+00:00'
updated_at: '2021-03-01T16:49:15+00:00'
type: issue
status: closed
closed_at: '2021-03-01T16:49:15+00:00'
---

# Original Description
Hi everyone,

I have started to mine Haven protocol using [hashvault](https://haven.hashvault.pro/en/dashboard) mining pool using both cpu and gpu on a Mac Mini M1.

On the terminal window I have the following hashrates :

![Capture d’écran 2021-03-01 à 15 10 07](https://user-images.githubusercontent.com/49617162/109508661-6010c580-7aa0-11eb-85ed-96020a502e7a.png)

but on hashvault dashboard I have only 130H/s.

I think it's a bug as 208447 H/s would gives me 8483.72 USD/month

I don't think something can be done to makes me have my 8000$ but maybe for the next version of xmrig that bug could be solved ¨̮ 

Enjoy mining !


# Discussion History
## SChernykh | 2021-03-01T14:56:06+00:00
This is a bug in OpenCL on Mac. Disable OpenCL in your XMRig config.

## noatte | 2021-03-01T15:03:37+00:00
> This is a bug in OpenCL on Mac. Disable OpenCL in your XMRig config.

if I disable it, it won't mine with gpu am I wrong ?

## SChernykh | 2021-03-01T15:05:39+00:00
GPU doesn't mine correctly anyway because OpenCL is broken in MacOS.

# Action History
- Created by: noatte | 2021-03-01T14:18:42+00:00
- Closed at: 2021-03-01T16:49:15+00:00
