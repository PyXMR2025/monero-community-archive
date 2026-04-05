---
title: downloading zero byte files
source_url: https://github.com/xmrig/xmrig/issues/2703
author: dgangstee
assignees: []
labels: []
created_at: '2021-11-17T20:49:26+00:00'
updated_at: '2021-11-18T02:15:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have tried many times to download xmrig-6.15.3-msvc-win64.zip and xmrig-6.15.3-gcc-win64.zip but I am getting only zero byte files even though the files have sizes listed are 2.87gb and 1.94 respectively. Downloading any .tar.gz downloads properly. It's just the Windows Zip files that give me this problem.

Does anyone have a solution?
Thanks/

# Discussion History
## Spudz76 | 2021-11-17T23:45:32+00:00
Your antivirus or the built-in garbage in the browser is blocking it.  Add exceptions.

## toy1111 | 2021-11-18T00:51:49+00:00
Download using Firefox and then in Firefox click the ongoing Downloads and it will show it as blocked but clicking on it gives you the option to allow. Haven't seen this in Chrome, it just blocks without option to allow.

## dgangstee | 2021-11-18T02:15:27+00:00
Thank you, that did the job, plus deactivating antivirus.

# Action History
- Created by: dgangstee | 2021-11-17T20:49:26+00:00
