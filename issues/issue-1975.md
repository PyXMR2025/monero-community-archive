---
title: OpenCL does not load when library is installed as libOpenCL.so.1
source_url: https://github.com/xmrig/xmrig/issues/1975
author: nopeinomicon
assignees: []
labels: []
created_at: '2020-12-11T20:18:06+00:00'
updated_at: '2020-12-15T08:26:35+00:00'
type: issue
status: closed
closed_at: '2020-12-15T08:23:57+00:00'
---

# Original Description
**Describe the bug**
When running xmrig on openSUSE (or potentially any other distro where libOpenCL is installed as libOpenCL.so.1) the OpenCL backend will fail to load.

**To Reproduce**
Run on a system with libOpenCL installed as libOpenCL.so.1 and attempt to enable OpenCL

**Expected behavior**
OpenCL backend loads, and miner is able to use OpenCL

**Required data**
 - Config file or command line (without wallets)
[xmrig.txt](https://github.com/xmrig/xmrig/files/5681386/xmrig.txt)
 - Miner log as text or screenshot
![Screenshot_20201211_130759](https://user-images.githubusercontent.com/11370809/101950096-ef998d00-3bb1-11eb-8c6a-693e1fa99356.png)
 - OS: openSUSE Tumbleweed
 - For GPU related issues: information about GPUs and driver version.
N/A, this is a library issue, not a GPU issue.

**Additional context**
This is using the packaged version of the app on openSUSE. I created the package and am one of package maintainers. https://build.opensuse.org/package/show/network:cryptocurrencies/xmrig


# Discussion History
## SChernykh | 2020-12-11T20:58:25+00:00
libOpenCL.so is the default name for Linux based OS, but you can override it with `--opencl-loader=PATH` command line or `loader` parameter in `opencl` section of config.json

## Saikatsaha1996 | 2020-12-15T04:14:28+00:00
![Screenshot_20201214-195733](https://user-images.githubusercontent.com/72664192/102170201-d21e3900-3eb9-11eb-9e4a-b7205965be2f.png)
![Screenshot_20201214-184632](https://user-images.githubusercontent.com/72664192/102170206-d3e7fc80-3eb9-11eb-8bcc-9d23fe5b0769.png)
![Screenshot_20201214-184518](https://user-images.githubusercontent.com/72664192/102170207-d4809300-3eb9-11eb-85e6-f70142676793.png)
![Screenshot_20201214-182224](https://user-images.githubusercontent.com/72664192/102170209-d5b1c000-3eb9-11eb-96f4-64f6ea62a8e2.png)
I am using xmrig android for some testing reason
I want help in my device already available OpenCL 2.0
But i got error failed to load OpenCL runtime
Please help me 🙏

## nopeinomicon | 2020-12-15T08:23:57+00:00
@Saikatsaha1996 I'd highly recommend opening a new issue with that. My issue was entirely specific to the way openSUSE installs the OpenCL library as far as I know.

## nopeinomicon | 2020-12-15T08:26:06+00:00
@SChernykh oh, and I though I had replied before but I guess not. openSUSE's OpenCL lib installs only to libOpenCL.so.1, not libOpenCL.so . That was my issue and I created a patch on the distribution side to resolve it. Thanks for your help though!

# Action History
- Created by: nopeinomicon | 2020-12-11T20:18:06+00:00
- Closed at: 2020-12-15T08:23:57+00:00
