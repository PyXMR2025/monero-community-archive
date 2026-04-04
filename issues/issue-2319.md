---
title: Windows x64 v0.14.1.0
source_url: https://github.com/monero-project/monero-gui/issues/2319
author: Lollypops
assignees: []
labels:
- resolved
created_at: '2019-07-25T20:46:32+00:00'
updated_at: '2019-07-26T07:18:44+00:00'
type: issue
status: closed
closed_at: '2019-07-26T07:18:44+00:00'
---

# Original Description
The GUI walkthrough for Windows is missing key information. Possibly the text colours are the same as the background.

https://imgur.com/HKB6bsn

# Discussion History
## selsta | 2019-07-25T20:48:56+00:00
It should look like this:
<img width="1026" alt="Screenshot 2019-07-25 at 22 47 55" src="https://user-images.githubusercontent.com/7697454/61907686-3f7ca300-af2e-11e9-9837-68c417e78417.png">
Are you using a VM? Any special setup? Can you try to start the GUI using `start-low-graphics-mode.bat`?


## Lollypops | 2019-07-25T21:07:41+00:00
Nothing special, stock windows, brand new computer. I'm unfamiliar with how to open the GUI with start-low-graphics-mode.bat. 

## selsta | 2019-07-25T21:08:43+00:00
Simply double click on it.

## Lollypops | 2019-07-25T21:11:46+00:00
Thanks : )

It's working in low graphics mode.

## sanderfoobar | 2019-07-25T21:14:09+00:00
Which graphics card + drivers?

## Lollypops | 2019-07-25T21:27:09+00:00
Intel(R) UHD Graphics 620. The previous driver version did not work. Drivers updated to drivers version 26.20.100.6911, it appears to be working now. 

## dEBRUYNE-1 | 2019-07-26T07:13:25+00:00
+resolved

# Action History
- Created by: Lollypops | 2019-07-25T20:46:32+00:00
- Closed at: 2019-07-26T07:18:44+00:00
