---
title: Missing xmrig execution file in xmrig-6.12.1-macos-x64.tar.gz release
source_url: https://github.com/xmrig/xmrig/issues/2342
author: Sammed98
assignees: []
labels: []
created_at: '2021-05-03T18:12:27+00:00'
updated_at: '2021-05-06T23:52:20+00:00'
type: issue
status: closed
closed_at: '2021-05-05T02:30:09+00:00'
---

# Original Description
**Describe the bug**
The download the xmrig-6.12.1-macos-x64.tar.gz file, unzip it and open the folder but cannot find the xmrig execution file or something with a Terminal image or application. It just has a config.json and a SHA256 file. 

**To Reproduce**
Download xmrig-6.12.1-macos-x64.tar.gz and unzip

**Expected behavior**
It should have the terminal app

**Required data**
 - OS: [Mac Intel processor]



# Discussion History
## SChernykh | 2021-05-03T18:29:17+00:00
Add the folder where you unpack it to antivirus exceptions.

## RS102839 | 2021-05-03T21:04:09+00:00
FYI:  It installed for me a few days ago.

## reddy-hari | 2021-05-04T18:45:18+00:00
I've listed the folder as an exclusion where i'm downloading the source (https://github.com/fireice-uk/xmr-stak/archive/refs/tags/1.0.5-rx.zip). Still missing the exe file. am i missing anything?

## Sammed98 | 2021-05-05T02:30:01+00:00
Ok. I understood the issue here. The execution file or the application with the terminal image is not present in the "x64" in the latest version. Download from the release 6.12.0. You will get the application. 

## reddy-hari | 2021-05-06T23:52:20+00:00
I got it to work using this link here - https://xmrig.com/download
Also checked the 6.12.0 version. Works too.

# Action History
- Created by: Sammed98 | 2021-05-03T18:12:27+00:00
- Closed at: 2021-05-05T02:30:09+00:00
