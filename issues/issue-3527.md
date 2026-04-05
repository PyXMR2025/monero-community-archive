---
title: Latest release API for mac-arm64 is missing `os` field
source_url: https://github.com/xmrig/xmrig/issues/3527
author: stringhandler
assignees: []
labels:
- bug
created_at: '2024-08-06T16:04:31+00:00'
updated_at: '2025-06-16T19:38:25+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:38:25+00:00'
---

# Original Description
When calling the API for latest version, all of the assets have `os` tags, except for the mac-arm64, which only has an `id` field.

```
https://api.xmrig.com/1/latest_release
```

``` 
 
    {
      "id": "macos-arm64",
      "name": "xmrig-6.21.3-macos-arm64.tar.gz",
      "url": "https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-macos-arm64.tar.gz",
      "size": 3227203,
      "ts": 1713865780000,
      "hash": "d7badde96309772bd219503bce91a239ed83dae042d426ef7aa663fce007dccf"
    },
    {
      "os": "macos-x64",
      "id": "macos-x64",
      "name": "xmrig-6.21.3-macos-x64.tar.gz",
      "url": "https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-macos-x64.tar.gz",
      "size": 3196075,
      "ts": 1713865783000,
      "hash": "4f6c7aa6d5d8ffa1429021db6d6104f42c2691abbab2e01d123356192bcf06fa"
    },
    {
      "os": "windows-x64",
      "id": "msvc-win64",
      "name": "xmrig-6.21.3-msvc-win64.zip",
      "url": "https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-msvc-win64.zip",
      "size": 2652511,
      "ts": 1713865793000,
      "hash": "713263085499ae626a6148fab67932c9a69611b21ac3d04cf52a5e23495f902e"
    },
```

# Discussion History
## xmrig | 2024-08-07T17:36:20+00:00
Fixed. Thank you.

# Action History
- Created by: stringhandler | 2024-08-06T16:04:31+00:00
- Closed at: 2025-06-16T19:38:25+00:00
