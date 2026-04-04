---
title: macOS 12 (Monterey) unsupported
source_url: https://github.com/monero-project/monero-gui/issues/4250
author: lkraider
assignees: []
labels: []
created_at: '2023-12-06T19:54:20+00:00'
updated_at: '2023-12-15T05:55:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I just upgraded using homebrew and it broke my wallet installation because now it needs macOS 13 it seems:

<img width="251" alt="Screen Shot 2023-12-06 at 16 47 26" src="https://github.com/monero-project/monero-gui/assets/52256/3817e1f0-7ef2-46d1-ad2c-33ea464559b9">

What are the specific new feature requirements that necessitate an OS upgrade?

# Discussion History
## selsta | 2023-12-07T02:15:17+00:00
Do you have a M1 Mac? The Apple Silicon native version requires macOS 13 or newer. You can download the Intel version from here if that's not an option for you, it should still work with older macOS versions: https://www.getmonero.org/downloads/

> What are the specific new feature requirements that necessitate an OS upgrade?

The build machine that I have access to has macOS 13 installed, that's why it is the minimum required version.

## lkraider | 2023-12-07T12:33:22+00:00
Yes, I have a M1 Mac. For the moment I have downgraded to the previous release.

Any way we can help to support older macOS versions?

## selsta | 2023-12-08T02:19:34+00:00
Will try to make it compatible with macOS 12 for the next release.

## selsta | 2023-12-15T05:55:37+00:00
Unfortuntelay I wasn't able to get access to a macOS 12 machine, so I won't be able to solve this next release.

> For the moment I have downgraded to the previous release.

You can use the latest Intel version, it will use Rosetta.

# Action History
- Created by: lkraider | 2023-12-06T19:54:20+00:00
