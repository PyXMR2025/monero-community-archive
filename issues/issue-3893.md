---
title: GUI sometimes starts with smaller window
source_url: https://github.com/monero-project/monero-gui/issues/3893
author: elibroftw
assignees: []
labels: []
created_at: '2022-04-24T21:14:11+00:00'
updated_at: '2022-04-30T08:07:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://user-images.githubusercontent.com/21298211/164996821-46122280-8974-4692-bf4a-56a55021669f.png)
The resize button at the bottom right does not work unless the wallet has been unlocked.

# Discussion History
## qqiumax | 2022-04-30T04:02:37+00:00
maybe the wallet GIF doesn't support enlarging

## qqiumax | 2022-04-30T04:02:57+00:00
I mean the language page GIF

## qqiumax | 2022-04-30T04:03:30+00:00
and the box for unlocking also doesn't support enlarging?


## selsta | 2022-04-30T07:45:47+00:00
> GUI sometimes starts with smaller window

Again one of these bugs that I have never seen. Might be Windows related.

> The resize button at the bottom right does not work unless the wallet has been unlocked.

I can reproduce that one. The proper solution here would be a native frameless window, which is complicated because they are not supported by Qt.

# Action History
- Created by: elibroftw | 2022-04-24T21:14:11+00:00
