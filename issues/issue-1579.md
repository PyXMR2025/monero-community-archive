---
title: '[Enhancement] Do not set MSR registers if the CPU backend is completely switched
  off'
source_url: https://github.com/xmrig/xmrig/issues/1579
author: YetAnotherRussian
assignees: []
labels:
- bug
- enhancement
created_at: '2020-03-05T07:27:34+00:00'
updated_at: '2020-08-19T01:27:54+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:27:54+00:00'
---

# Original Description
```
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
< CUT-OFF >
    "cpu": {
        "enabled": false,
< CUT-OFF >
    "opencl": {
        "enabled": true,
< CUT-OFF >
    "cuda": {
        "enabled": true,
```

So, this mode is intended to disable CPU mining at all, but we still set the registers and degrade third-party applications performance. I think msr option should take in charge both "randomx" section and "cpu" section (so we dont't have to modify several values instead of one).

Note: this is not a BUG.

# Discussion History
# Action History
- Created by: YetAnotherRussian | 2020-03-05T07:27:34+00:00
- Closed at: 2020-08-19T01:27:54+00:00
