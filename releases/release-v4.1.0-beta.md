---
title: v4.1.0-beta
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v4.1.0-beta
author: xmrig
tag_name: v4.1.0-beta
published_at: '2019-09-26T19:45:59+00:00'
---

# Version: v4.1.0-beta

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- http://workers.xmrig.info/

## v4.1.0-beta
- **OpenCL backend disabled by default.**
- [#1183](https://github.com/xmrig/xmrig/issues/1183) Fixed compatibility with systemd.
- [#1185](https://github.com/xmrig/xmrig/pull/1185) Added JIT compiler for RandomX on ARMv8.
- Improved API endpoint `GET /2/backends` and added support for this endpoint to [workers.xmrig.info](http://workers.xmrig.info).
- Added command line option `--no-cpu` to disable CPU backend.
- Added OpenCL specific command line options: `--opencl`, `--opencl-devices`, `--opencl-platform`, `--opencl-loader` and `--opencl-no-cache`.
- Removed command line option `--http-enabled`, HTTP API enabled automatically if any other `--http-*` option provided.