---
title: XMRig 4 unified CPU and OpenCL miner
source_url: https://github.com/xmrig/xmrig/issues/1172
author: xmrig
assignees: []
labels:
- META
- opencl
created_at: '2019-09-15T11:29:33+00:00'
updated_at: '2019-11-14T08:18:56+00:00'
type: issue
status: closed
closed_at: '2019-11-14T08:18:56+00:00'
---

# Original Description
XMRig 4 (beta) is unified CPU and OpenCL miner it includes all features from v3.1.2 and support OpenCL as second mining backend.

* OpenCL backend can be complete disabled on compile time (`-DWITH_OPENCL=OFF`) or via config (`enabled` field in `opencl` object.
* Config file backward compatible with v3.
* This version support RandomX mining.
* Dedicated xmrig-amd miner becomes obsolete and will not updated to support RandomX and future enhancements.
* OpenCL don't add any additional external dependency on compile time and runtime.
* Config format changed to support multiple profiles, same as v3.

#### Known issues
* [ ] No documentation about new options yet.
* [ ] Command line options not implemented.

Code available in evo branch.
v4.0.0-beta release will be created soon.

# Discussion History
# Action History
- Created by: xmrig | 2019-09-15T11:29:33+00:00
- Closed at: 2019-11-14T08:18:56+00:00
