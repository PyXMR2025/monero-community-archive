---
title: WinInstaller 0.18.3.1 being downloaded and not 0.18.3.2
source_url: https://github.com/monero-project/monero-gui/issues/4295
author: 0hne
assignees: []
labels: []
created_at: '2024-03-20T12:46:04+00:00'
updated_at: '2024-03-21T03:30:27+00:00'
type: issue
status: closed
closed_at: '2024-03-21T03:30:26+00:00'
---

# Original Description
Hello, in the [download](https://www.getmonero.org/downloads/#gui:~:text=30%2B%20languages%20available-,Downloads,-Current%20Version%3A) section, clicking on the [Windows 64-bit (Installer)](https://downloads.getmonero.org/gui/win64install), downloads the old version 0.18.3.1 for me, instead of the current version 0.18.3.2.
On GitHub it's not a problem, just on the download website.

# Discussion History
## selsta | 2024-03-20T15:05:57+00:00
I think this is a CDN issue, depending on the location it correctly links to v0.18.3.2. Maybe some cache has to be purged, I will forward it.

## 0hne | 2024-03-20T15:15:39+00:00
It might be something locally as well though? I just tried inPrivate mode in Edge, and then it downloads the correct 0.18.3.2.

## plowsof | 2024-03-20T16:41:04+00:00
clear your browser cache or use a different* link to download the file. for example: https://downloads.getmonero.org/gui/win64install_some_text_here

## 0hne | 2024-03-20T16:59:46+00:00
Yes that's what I thought, but wanted to make sure. I guess we can close it then. Sorry.

## plowsof | 2024-03-20T17:01:53+00:00
if this is a big enough problem, perhaps the version number could be tagged into the url and then nobody would run into this issue. tagged on superficially inside the downloads page html.. dont have to mess with DNS

## selsta | 2024-03-21T03:30:26+00:00
Closing as this doesn't appear to be a GUI bug. monero-site repo would be better suited to further discuss the website and download link.

# Action History
- Created by: 0hne | 2024-03-20T12:46:04+00:00
- Closed at: 2024-03-21T03:30:26+00:00
