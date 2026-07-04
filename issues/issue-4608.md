---
title: 'UI Bug: Update prompt incorrectly appears inside "Hardware wallet passphrase"
  dialog after unlocking Trezor'
source_url: https://github.com/monero-project/monero-gui/issues/4608
author: CupofJavad
assignees: []
labels: []
created_at: '2026-06-16T14:25:44+00:00'
updated_at: '2026-07-02T21:04:46+00:00'
type: issue
status: closed
closed_at: '2026-07-02T21:04:45+00:00'
---

# Original Description
Summary
When connecting a Trezor hardware wallet and unlocking the device, the "Hardware wallet passphrase" dialog incorrectly displays the standard Monero update notification ("New Monero version v0.18.5.0 is available") inside or overlaid on top of it.
This appears to be a dialog management / parenting issue in the GUI. The update prompt belongs to the normal Monero software updater, but it is being shown in the wrong context during the hardware wallet connection flow.
Steps to Reproduce

Open the latest Monero GUI (v0.18.5.0 or newer).
Connect a Trezor hardware wallet.
Unlock the Trezor device normally (enter PIN on the device).
The "Hardware wallet passphrase" dialog appears.
The update prompt ("New Monero version v0.18.5.0 is available. Do you want to download and verify new version?") is incorrectly shown inside this dialog.

This happens consistently after unlocking the device.
Expected Behavior
The "Hardware wallet passphrase" dialog should appear cleanly without any unrelated update prompts. The software update notification should only appear as a separate, top-level dialog when appropriate.
Actual Behavior
The update notification is nested or overlaid inside the passphrase dialog, creating a confusing user experience.
Screenshot
Attached (shows the update prompt appearing inside the hardware wallet passphrase dialog).
Environment

Monero GUI version: Latest (v0.18.5.0 / Fluorine Fermi)
Operating System: Windows 11
Trezor model:  Model T
Trezor firmware: Latest (verified in official Trezor Suite)

Additional Notes

Confirmed via official Trezor Suite that there is no pending firmware update for the device.
The prompt is the normal Monero GUI updater, not a Trezor-related message.
This occurs even though the GUI is fully up to date.

<img width="976" height="796" alt="Image" src="https://github.com/user-attachments/assets/c4492003-e7ea-4067-a3b0-098ae4c67fc2" />

# Discussion History
## CupofJavad | 2026-07-01T17:36:41+00:00
@r06293138-coder
@e93276151-gif
@kyliebryna45-prog

I just noticed each you responded to this but then delete/removed your comments later so I’m guessing you all figured this out or resolved it? In response, to your questions, no I never actually attempted to resolve this...I’m am merely a pleb-end-user and do not work with the dev team. The only reason I went through the (surprisingly difficult) process of submitting a bug was because I was worried this was some sort attack on my device, couldn’t find much online about it, and wanted to support the project. 

## selsta | 2026-07-01T17:37:40+00:00
@CupofJavad they were support scam bots, that's why the comments were deleted

## CupofJavad | 2026-07-01T17:44:05+00:00
> @CupofJavad they were support scam bots, that's why the comments were deleted

@selsta ahh that makes more sense now and appreciate you chiming in here... guess this means I'll just have to assume you're not a bot of some kind either 🤷🏽‍♂️

## selsta | 2026-07-01T18:09:43+00:00
You can see by the "collaborator" sign that I have elevated privilges in the repo. I did not have time to fix your report yet.

# Action History
- Created by: CupofJavad | 2026-06-16T14:25:44+00:00
- Closed at: 2026-07-02T21:04:45+00:00
