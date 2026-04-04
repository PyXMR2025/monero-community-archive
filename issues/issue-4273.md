---
title: 'Couldn''t open wallet: device not found: Trezor'
source_url: https://github.com/monero-project/monero-gui/issues/4273
author: StevenRispoli
assignees: []
labels: []
created_at: '2024-02-03T18:05:46+00:00'
updated_at: '2024-03-11T01:49:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I can no longer connect to the Monero-gui wallet with my Trezor Model T.

Issue title is the exact error message: "Couldn't open wallet: device not found: Trezor"

Monero-gui v0.18.3.1 - flatpak

Trezor Bridge v2.0.27

Pop_OS 22.04

I don't see trezord in system monitor or htop, but it does otherwise appear to be running since I could verify the bridge status and that it could see my Model T connected here: http://127.0.0.1:21325/status/

I've reinstalled the bridge and restarted my PC to no avail.

Monero-gui is the only third-party wallet I use so I have not confirmed if I can connect to other third-party wallets, but I can connect to the desktop and web versions of trezor suite with no issues (though that might not tell us much since trezor suite supposedly has it's own bridge it falls back to).

Is this an issue anyone else has encountered? I'm not sure if it's a Monero-gui issue or a Trezor bridge issue.

Thanks


# Discussion History
## selsta | 2024-02-03T18:08:12+00:00
Can you try the GUI binary from getmonero.org? It's possible that the flatpak version was compiled without Trezor support.

## StevenRispoli | 2024-02-03T18:38:22+00:00
That was indeed the problem, thank you. Any reason the flatpak version wouldn't be compiled with Trezor support? Should we refrain from using the flatpak version?

## selsta | 2024-02-03T18:40:54+00:00
@BigmenPixel0 any idea if this changed recently or did flatpak always miss Trezor support?

## StevenRispoli | 2024-02-03T18:42:40+00:00
I've been using the flatpak version with the same Model T for at least a couple of years.

## andreashuber69 | 2024-02-10T11:36:43+00:00
> I've been using the flatpak version with the same Model T for at least a couple of years.

Same here, Trezor has been working flawlessly with the flatpak version. Only the latest version fails to detect it.

@ Monero Team: Please restore Trezor support in the flatpak version.

(When I try to add a new wallet with hardware support, then Trezor is still offered as an option in the UI.)

## selsta | 2024-02-10T12:05:33+00:00
Some dependencies got updated and it seems that caused issues with the Trezor subsystem, I will try to get it reverted.

https://github.com/flathub/org.getmonero.Monero/commit/9811de679ef12e60f3644197a7b429724689d7f3

## q7nm | 2024-02-10T12:17:09+00:00
@selsta, sorry, I didn't see past messages in time. Should I revert the update?

## q7nm | 2024-02-10T12:18:28+00:00
And which module can be a problem, if you know?

## selsta | 2024-02-10T12:20:06+00:00
@BigmenPixel0 I would need to see build logs, easiest for now is to revert everything. I'd guess it's related to the protobuf update.

## q7nm | 2024-02-10T12:21:27+00:00
@selsta you can see them here
https://buildbot.flathub.org/#/builders/6/builds/97527


## selsta | 2024-02-10T12:25:28+00:00
> -- Trezor support disabled

Try reverting the protobuf change. I think the version is too new and would require changes in monero that we currently only have in the master branch.

## q7nm | 2024-02-10T12:56:39+00:00
@andreashuber69 @StevenRispoli 
Can you try it and tell me if it works?
https://github.com/flathub/org.getmonero.Monero/pull/104#issuecomment-1937001039

## andreashuber69 | 2024-02-10T13:08:34+00:00
> @andreashuber69 @StevenRispoli Can you try it and tell me if it works? [flathub/org.getmonero.Monero#104 (comment)](https://github.com/flathub/org.getmonero.Monero/pull/104#issuecomment-1937001039)

Ran the command line in the linked post and now everything is back to where it was, thank you!

## q7nm | 2024-02-10T13:12:35+00:00
@andreashuber69 
Great. Now you should remove this version and wait for an update (because that's a test package which won't get updates)

## q7nm | 2024-03-11T01:47:03+00:00
@selsta does the new release support the newest version of protobuf?

## selsta | 2024-03-11T01:49:12+00:00
@BigmenPixel0 no, the newest version of protobuf requires C++17 which we currently don't use on the release branch.

# Action History
- Created by: StevenRispoli | 2024-02-03T18:05:46+00:00
