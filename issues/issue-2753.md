---
title: Submit each Monero build to VirusTotal as early as possible
source_url: https://github.com/monero-project/monero-gui/issues/2753
author: mcgroarty
assignees: []
labels: []
created_at: '2020-01-29T22:23:35+00:00'
updated_at: '2022-03-16T19:51:20+00:00'
type: issue
status: closed
closed_at: '2022-03-16T19:51:20+00:00'
---

# Original Description
There are numerous previous issues which talk about antivirus engine false positives.

Consider submitting each Monero build to VirusTotal as early as possible. This accomplishes a few things:

1. It tells you which antivirus engines produce false positives

2. It tells the antivirus producers when their engine is out of sync with others' engines (Google now owns VirusTotal, and they share findings with participating engines)

3. VirusTotal result pages give you something to point at when communicating with antivirus vendors and end users


In my own experience shipping a commercial software product, we get a lot more traction on av vendor tickets when we provide a link to a VirusTotal scan where that vendor is a clear outlier.

Early uploads also mean that the antivirus vendors have an earlier opportunity to begin analysis. Often they clear false positives inside of a few days.

# Discussion History
## selsta | 2020-01-31T14:18:24+00:00
Does VirusTotal handle archives or does every binary have to get uploaded separately?

## mcgroarty | 2020-01-31T20:16:56+00:00
It accepts archives in some formats. Most engines will not look at the tarred bz2 archive. But the major engines look at the contents of a zip file.

Here's an example of recompressing the macOS client as a .zip file and uploading:
https://www.virustotal.com/gui/file/10e7c80ee99be3e785d5d650c06bc995c435821e3afb2878df56d8b221f69d29/detection

Note that it doesn't tell you which files in the archive were tagged though.

They also have an API which can be used to submit individual files. It requires that a user obtain a free API key, although the user must accept some terms and conditions to do so. This could be incorporated into the build scripts as an extra build option or alternative target.

## selsta | 2022-03-16T19:51:20+00:00
I'll close this as this is more information and not a bug report :) Will try to think about uploading the archives to virustotal for the next release.

# Action History
- Created by: mcgroarty | 2020-01-29T22:23:35+00:00
- Closed at: 2022-03-16T19:51:20+00:00
