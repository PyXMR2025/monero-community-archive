---
title: XMRig binaries blocked by Chrome
source_url: https://github.com/xmrig/xmrig/issues/270
author: CharlesNadolski
assignees: []
labels:
- av
created_at: '2017-12-17T19:43:24+00:00'
updated_at: '2018-02-23T21:21:44+00:00'
type: issue
status: closed
closed_at: '2018-02-23T21:21:44+00:00'
---

# Original Description
Cannot download binaries from https://github.com/xmrig/xmrig/releases/tag/v2.4.3
They are all flagged as dangerous (containing viruses or malware) by Chrome (63.0.3239.108).  Unfortunately chrome doesn't say *why* it was blocked. I was hoping to switch from xmr-stak to xmrig because xmr-stak also gets flagged as malware (!#UACTrigger.A), hoping that xmrig was safer but no dice.

# Discussion History
## daiplusplus | 2017-12-18T01:41:30+00:00
Many virus-scanners classify mining software as "Unwanted applications" as miners are now often included in viral software (because if you manage to infect 10,000 machines you might as well earn some residual income from them!) - and it looks like Chrome has a single list of malware that makes no distinction between wanted and unwanted miners. I think Chrome (and other virus scanners) should make a distinction between a mining program that appears on disk (perhaps named "svchost.exe") and miners that users have downloaded directly from GitHub or built themselves.

Here's a screenshot from VirusTotal of the `xmrig.exe` inside `xmrig-2.4.3-msvc-win64.zip`:

![image](https://user-images.githubusercontent.com/1693078/34086534-58839c14-e351-11e7-8929-1a2ac29df4da.png)


## CharlesNadolski | 2017-12-19T14:50:41+00:00
Thanks for the explanation.  It's too bad that the virus scanners can't distinguish between a trojan/virus and a legitimate executable.  I found out that there is a way to disable the virus scanning in Chrome, but it's not something I would recommend for most people.  Is there any way to submit the exe to get it whitelisted in Chrome?

## Pseudothink | 2017-12-29T14:56:34+00:00
Ditto, thanks for this explanation!

## ZachE84 | 2018-01-02T15:03:40+00:00
There is no way to get Chrome to download XMRig - its permanantly blocked. ideas?

## xmrig | 2018-01-02T15:18:37+00:00
You can temporary disable option `Protect you and your device from dangerous sites`.
Next release maybe clean again for some time, maybe not, depends of how Chrome blocking work.
Thank you.

## Pseudothink | 2018-01-02T23:30:34+00:00
I used Chrome to download and install Firefox, which made it easy.

# Action History
- Created by: CharlesNadolski | 2017-12-17T19:43:24+00:00
- Closed at: 2018-02-23T21:21:44+00:00
