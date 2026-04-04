---
title: macos aarch64 depends build missing from readme
source_url: https://github.com/monero-project/monero/issues/9987
author: nahuhh
assignees: []
labels: []
created_at: '2025-07-11T20:10:56+00:00'
updated_at: '2025-07-19T15:22:05+00:00'
type: issue
status: closed
closed_at: '2025-07-19T15:22:05+00:00'
---

# Original Description
```bash
make depends target=aarch64-apple-darwin11
```

iirc it requires some different dependencies 

something(s) from here (these are taken from the workflow)

- add mac specific dependencies: `cmake imagemagick libcap-dev librsvg2-bin libz-dev libbz2-dev libtiff-tools python-dev`
- potentially not listed aarch specific dependencies `autotools-dev automake python3 bsdmainutils curl ca-certificates unzip ccache python3-setuptools-git libtinfo5`

# Discussion History
# Action History
- Created by: nahuhh | 2025-07-11T20:10:56+00:00
- Closed at: 2025-07-19T15:22:05+00:00
