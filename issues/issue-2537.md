---
title: Font Size on High DPI Devices
source_url: https://github.com/monero-project/monero-gui/issues/2537
author: jeffro256
assignees: []
labels: []
created_at: '2019-11-30T18:21:29+00:00'
updated_at: '2020-09-07T21:18:19+00:00'
type: issue
status: closed
closed_at: '2020-09-07T21:18:19+00:00'
---

# Original Description
Hello! Maybe this has been asked already, but I couldn't find it. I'm running Windows 10 with a 3840x2160 screen. The font size in the GUI wallet is tiny. I included a screenshot of what it looks like:
![Screenshot](https://user-images.githubusercontent.com/10839482/69904363-6d09ab00-136b-11ea-8d67-c44ec8933e53.png)
Keep in mind that this is a laptop screen so the text is itty bitty in physical size. I think it would be a good idea to detect what kind of screen the user is using and scale the text accordingly. 

# Discussion History
## selsta | 2019-11-30T18:33:16+00:00
As a temporary workaround: add a file called `start-high-dpi.bat` to the same folder as the `monero-wallet-gui.exe` with

```
@echo off

set QT_SCALE_FACTOR=2

start /b monero-wallet-gui.exe
```

## selsta | 2020-09-07T21:18:19+00:00
Windows releases now come with a `start-high-dpi.bat`

# Action History
- Created by: jeffro256 | 2019-11-30T18:21:29+00:00
- Closed at: 2020-09-07T21:18:19+00:00
