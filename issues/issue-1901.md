---
title: Binaries mixed up?
source_url: https://github.com/monero-project/monero-site/issues/1901
author: TimGalloo
assignees: []
labels: []
created_at: '2021-12-08T22:15:12+00:00'
updated_at: '2021-12-09T20:15:59+00:00'
type: issue
status: closed
closed_at: '2021-12-09T20:15:59+00:00'
---

# Original Description
 shasum -a 256 monero-gui-linux-x64-v0.17.3.0.tar.bz2
ac18ce3d1189410a5c175984827d5d601974733303411f6142296d647f6582ce  monero-gui-linux-x64-v0.17.3.0.tar.bz2

 shasum -a 256 monero-linux-x64-v0.17.3.0.tar.bz2
ac18ce3d1189410a5c175984827d5d601974733303411f6142296d647f6582ce  monero-linux-x64-v0.17.3.0.tar.bz2

same hash = same files ?


# Discussion History
## selsta | 2021-12-09T17:08:23+00:00
Can't reproduce. Where did you download this file?

## TimGalloo | 2021-12-09T19:25:39+00:00
Getmonero.org but now ok
Issue can close

# Action History
- Created by: TimGalloo | 2021-12-08T22:15:12+00:00
- Closed at: 2021-12-09T20:15:59+00:00
