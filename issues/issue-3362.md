---
title: VM Tag
source_url: https://github.com/xmrig/xmrig/issues/3362
author: Intybyte
assignees: []
labels: []
created_at: '2023-11-18T14:28:29+00:00'
updated_at: '2025-06-16T19:51:48+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:51:48+00:00'
---

# Original Description
At first i had some problems in making MSR work on win11, but after disabling core isolation it works and it was applied correctly, however xmrig still shows the red VM tag, does it lower my hashrate? If yes how do I fix it? Thank you

# Discussion History
## Intybyte | 2023-11-18T14:47:02+00:00
Disabling Virtualization on cpu fixed it but is there a work around? I need virtualization on if possible

## geekwilliams | 2023-11-18T16:12:16+00:00
Does having virtualization on actually effect your hashrate? I'm curious because I'm in the same position 

## Intybyte | 2023-11-18T19:30:35+00:00
Maybe a 50-100 H/s gain? Or maybe none, it is a small difference if there is some

## geekwilliams | 2023-11-18T19:38:28+00:00
Makes sense. I run vm's on my workstation, that also mines when I'm not using it. 50-100h/s doesn't matter that much to me.  I wouldn't think virtualization would effect even the msr mod but I don't know enough about it to say for sure

## SlavisaBakic | 2023-11-19T00:20:41+00:00
> At first i had some problems in making MSR work on win11, but after disabling core isolation it works and it was applied correctly, however xmrig still shows the red VM tag, does it lower my hashrate? If yes how do I fix it? Thank you

Is Hyper-V enabled?

## Intybyte | 2023-11-19T07:29:19+00:00
> > At first i had some problems in making MSR work on win11, but after disabling core isolation it works and it was applied correctly, however xmrig still shows the red VM tag, does it lower my hashrate? If yes how do I fix it? Thank you
> 
> Is Hyper-V enabled?

In order to disable virtualization you need to disable Hyper-V, so it isn't enabled

## SlavisaBakic | 2023-11-19T10:43:32+00:00
> > > At first i had some problems in making MSR work on win11, but after disabling core isolation it works and it was applied correctly, however xmrig still shows the red VM tag, does it lower my hashrate? If yes how do I fix it? Thank you
> > 
> > 
> > Is Hyper-V enabled?
> 
> In order to disable virtualization you need to disable Hyper-V, so it isn't enabled

Open System Information in Windows and check there if Virtualization Based Security is enabled.

## Intybyte | 2023-11-20T13:48:09+00:00
> > > > At first i had some problems in making MSR work on win11, but after disabling core isolation it works and it was applied correctly, however xmrig still shows the red VM tag, does it lower my hashrate? If yes how do I fix it? Thank you
> > > 
> > > 
> > > Is Hyper-V enabled?
> > 
> > In order to disable virtualization you need to disable Hyper-V, so it isn't enabled
> 
> Open System Information in Windows and check there if Virtualization Based Security is enabled.

It is disabled

## SlavisaBakic | 2023-11-20T14:31:23+00:00
> > > > > At first i had some problems in making MSR work on win11, but after disabling core isolation it works and it was applied correctly, however xmrig still shows the red VM tag, does it lower my hashrate? If yes how do I fix it? Thank you
> > > > 
> > > > 
> > > > Is Hyper-V enabled?
> > > 
> > > 
> > > In order to disable virtualization you need to disable Hyper-V, so it isn't enabled
> > 
> > 
> > Open System Information in Windows and check there if Virtualization Based Security is enabled.
> 
> It is disabled

In Windows Features Turn Off and On dialog make sure that those features are disabled:

- Hyper-V
- Microsoft Defender Application Guard
- Virtual Machine Platform
- Windows Hypervisor Platform
- Windows Sandbox
- Windows Subsystem for Linux

# Action History
- Created by: Intybyte | 2023-11-18T14:28:29+00:00
- Closed at: 2025-06-16T19:51:48+00:00
