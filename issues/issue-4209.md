---
title: Please make the password entry field have focus
source_url: https://github.com/monero-project/monero-gui/issues/4209
author: MikeRich88
assignees: []
labels: []
created_at: '2023-08-12T23:49:33+00:00'
updated_at: '2026-01-17T03:48:35+00:00'
type: issue
status: closed
closed_at: '2026-01-17T03:48:35+00:00'
---

# Original Description
Attached is a video showing the problem. I think it only occurs when you use the keyboard to switch tasks.

macOS 13.5
monero-wallet-gui 0.18.2.2

https://github.com/monero-project/monero-gui/assets/7113073/85b156ed-b4fa-4897-bb1b-81d302a39ea2



# Discussion History
## selsta | 2023-08-13T23:10:46+00:00
Can you reproduce it without BBEdit? I don't have it installed but so far I wasn't able to reproduce on macOS 14, switching with keyboard works without issues.

## MikeRich88 | 2023-08-15T07:07:09+00:00
I have to switch from some app into Monero to show the issue. BBEdit just happened to be convenient because it could also demonstrate that I was typing, etc. (I had the Finder quit in the video because of all the junk on my desktop)

Try in this order exactly. I replicated it with TextEdit instead of BBEdit, no video though.
1. Launch Monero GUI, and then enter your password.
2. Make sure Monero is on the Send tab (this probably does not matter).
3. Launch TextEdit, or any other app, (which app probably shouldn't matter, as long as it's some other app)
4. Go away for 20 minutes, or however long it takes before Monero reintroduces the password prompt. Make sure the frontmost app is TextEdit for this time. (Maybe: Make sure the computer does not go to sleep? Probably doesn't matter)
5. Cmd-Tab from other app into Monero GUI.
6. Focus will not be in the password field.

It's a minor issue for sure, but I think at the same time it's an easy fix and therefore an easy win.

This is on my laptop so it's hard to leave it unused for periods of time like that, but I have an old Mac Pro with macOS 12 that I could try also.

## MikeRich88 | 2026-01-14T00:32:52+00:00
This is still a bug. It is still annoying. It is still an easy fix, probably.

## selsta | 2026-01-14T16:56:44+00:00
I was able to reproduce it, will try to fix it today.

# Action History
- Created by: MikeRich88 | 2023-08-12T23:49:33+00:00
- Closed at: 2026-01-17T03:48:35+00:00
