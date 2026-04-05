---
title: Cannot UPX compress anymore
source_url: https://github.com/xmrig/xmrig/issues/1427
author: liminalsoundscapes
assignees: []
labels: []
created_at: '2019-12-15T21:22:58+00:00'
updated_at: '2019-12-22T19:06:41+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:06:41+00:00'
---

# Original Description
I Like using UPX to compress my compiled xmrig. this worked very well until the 2.xx versions. but now I am having the following error:

upx: D:\Visual Studio\xmrig\build\Release\xmrig.exe: CantPackException: size of Load Configuration directory unexpected

is there anything I can do about this ?

this is the entire UPX log

C:\Users\stian>"D:\Visual Studio\xmrig\build\Release\upx.exe" "D:\Visual Studio\xmrig\build\Release\xmrig.exe"
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2018
UPX 3.95w       Markus Oberhumer, Laszlo Molnar & John Reiser   Aug 26th 2018

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
upx: D:\Visual Studio\xmrig\build\Release\xmrig.exe: CantPackException: size of Load Configuration directory unexpected

Packed 1 file: 0 ok, 1 error.

# Discussion History
## mukesh-610 | 2019-12-20T15:32:10+00:00
I was able to compress XMRig using UPX.

I compiled XMRig myself on a 64-bit Linux PC (gcc 8.3), and used UPX 3.95 with `--force` flag.

## xmrig | 2019-12-22T19:06:41+00:00
It UPX bug https://github.com/upx/upx/issues/245 nothing I can do with it.
Thank you.

# Action History
- Created by: liminalsoundscapes | 2019-12-15T21:22:58+00:00
- Closed at: 2019-12-22T19:06:41+00:00
