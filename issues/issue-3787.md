---
title: Compile time option to disable "Would you like to register Monero GUI Desktop
  entry?"
source_url: https://github.com/monero-project/monero-gui/issues/3787
author: kpcyrd
assignees: []
labels: []
created_at: '2021-12-09T11:53:50+00:00'
updated_at: '2022-04-30T17:43:09+00:00'
type: issue
status: closed
closed_at: '2022-01-24T20:23:08+00:00'
---

# Original Description
hi!

Arch Linux is distributing a monero-gui package that already includes a desktop entry.

Is there a way to disable this question with a compile time option?

![image](https://user-images.githubusercontent.com/7763184/145391346-21da313e-e82a-40c5-8c19-88f826ada741.png)

Thanks!

# Discussion History
## selsta | 2021-12-17T15:45:13+00:00
#3808

Once this is merged you can add `-D WITH_DESKTOP_ENTRY=OFF` to your CMake arguments.

## selsta | 2022-04-29T03:24:59+00:00
reminder that this release (v0.17.3.2) supports `-D WITH_DESKTOP_ENTRY=OFF`

## kpcyrd | 2022-04-30T17:43:09+00:00
Thanks, we're now using this option in Arch Linux :heart: 

# Action History
- Created by: kpcyrd | 2021-12-09T11:53:50+00:00
- Closed at: 2022-01-24T20:23:08+00:00
