---
title: monero download with curl enforcing https broken
source_url: https://github.com/monero-project/monero-site/issues/1081
author: adrelanos
assignees: []
labels:
- 🧰 back end
- UX
created_at: '2020-07-15T09:34:00+00:00'
updated_at: '2020-07-16T16:08:04+00:00'
type: issue
status: closed
closed_at: '2020-07-16T16:06:50+00:00'
---

# Original Description
`https://downloads.getmonero.org/gui/linux64` is the download link provided at `https://web.getmonero.org/downloads/`.

    curl --tlsv1.2 --proto =https --location --remote-name-all --remote-header-name --output /tmp/test https://downloads.getmonero.org/gui/linux64

> curl: (1) Protocol "http" not supported or disabled in libcurl

Dropping `/gui/linux64` works.

    curl --tlsv1.2 --proto =https --location --remote-name-all --remote-header-name --output /tmp/test https://downloads.getmonero.org

No error. But then it is not clear to me what would be downloaded.

# Discussion History
## 00-matt | 2020-07-15T11:14:59+00:00
I think that this is because you get a long chain of redirects, some of which are plain HTTP.

## adrelanos | 2020-07-16T09:48:31+00:00
I guess so. Imo very worthwhile to fix since any intermediate redirect
to HTTP could be mitm'd.


## fluffypony | 2020-07-16T16:06:40+00:00
FIXED! We originally support HTTP for updates.getmonero.org (used by the auto-updater), but now that it can handle HTTPS (and everyone's mostly updated since that change) we no longer require it. We've also enabled HSTS, applied for it to get added to the HSTS pre-load list, and enforced HTTP->HTTPS for everything on getmonero.org including all subdomains.

## SarangNoether | 2020-07-16T16:08:04+00:00
I just tested the original HTTPS query, and it redirects properly now.

# Action History
- Created by: adrelanos | 2020-07-15T09:34:00+00:00
- Closed at: 2020-07-16T16:06:50+00:00
