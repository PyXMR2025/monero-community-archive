---
title: 'really bad color banding in dark theme '
source_url: https://github.com/monero-project/monero-gui/issues/3701
author: tleydxdy
assignees: []
labels: []
created_at: '2021-09-14T04:00:41+00:00'
updated_at: '2023-09-12T23:45:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The interface seems to have a very slight gradient which causes severe banding in the interface as shown.
![banding issue](https://user-images.githubusercontent.com/10610765/133192825-ddd261fe-917b-4ce4-af8c-ae76967e8721.png)


# Discussion History
## selsta | 2022-04-26T18:30:01+00:00
Are you using macOS?

## tleydxdy | 2022-04-28T01:39:56+00:00
No, it's GNU/Linux

## selsta | 2022-04-28T01:41:40+00:00
Did you download it from getmonero.org? Or custom compiled / package manager?

## tleydxdy | 2022-04-28T02:17:56+00:00
I got it from arch repo

## selsta | 2022-04-28T02:34:54+00:00
can you test the binary from getmonero.org just so that we know if it's generally an issue or an issue with the arch package

## tleydxdy | 2022-04-28T21:39:18+00:00
you can see the same banding on the screenshot on the website 
https://www.getmonero.org/img/downloads/gui.png

## kernkraft235 | 2023-09-12T23:45:46+00:00
Same issue on arch linux. Its not nearly as noticeable on qubes os, maybe just an artifact of how it presents windows

# Action History
- Created by: tleydxdy | 2021-09-14T04:00:41+00:00
