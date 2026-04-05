---
title: Windows 11 Huge Pages...how to enable?
source_url: https://github.com/xmrig/xmrig/issues/2643
author: alanhasgari
assignees: []
labels: []
created_at: '2021-10-23T22:16:56+00:00'
updated_at: '2021-10-24T08:29:20+00:00'
type: issue
status: closed
closed_at: '2021-10-24T00:46:45+00:00'
---

# Original Description
tried the rktools.exe method, and it says the permissions are granted, but xmrig still shows huge pages as unavailable...

# Discussion History
## alanhasgari | 2021-10-24T00:46:45+00:00
disregard. seems it was my windows install that was broken. issue fixed itself after windows updated to latest build.

## Spudz76 | 2021-10-24T08:23:53+00:00
Can also be "Memory integrity" setting buried somewhere in security.  Then your xmrig will show "VM" mode and not allow MSRs or Hugepages (even if otherwise enabled, "granted")

## SChernykh | 2021-10-24T08:29:20+00:00
> Can also be "Memory integrity" setting buried somewhere in security

Here: https://youtu.be/Z1iO7N22Um8?t=196

# Action History
- Created by: alanhasgari | 2021-10-23T22:16:56+00:00
- Closed at: 2021-10-24T00:46:45+00:00
