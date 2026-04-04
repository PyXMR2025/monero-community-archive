---
title: can't run on opensuse 15.2
source_url: https://github.com/monero-project/monero-gui/issues/2980
author: micromatrix14
assignees: []
labels: []
created_at: '2020-07-02T17:20:52+00:00'
updated_at: '2020-09-07T21:14:36+00:00'
type: issue
status: closed
closed_at: '2020-09-07T21:14:36+00:00'
---

# Original Description
monero version for Linux can't run on OpenSUSE 15.1 and the newest one 15.2 because of the required glibc 2.27 version
there are a lot of users who use Opensuse distribution and with its released version few hours ago which will last for years, it means we OpenSUSE users can't run monero on it!!

# Discussion History
## xiphon | 2020-07-02T17:29:07+00:00
Are you sure you mentioned the correct glibc version? glibc 2.7 is pretty old version. Could you post the exact error message?

## micromatrix14 | 2020-07-02T17:47:21+00:00
sorry typing mistake actually it is v2.27
![Screenshot_20200702_173949](https://user-images.githubusercontent.com/22969054/86393065-841bcd00-bcad-11ea-88c2-bc238294f918.png)


## xiphon | 2020-07-02T17:59:37+00:00
> sorry typing mistake actually it is v2.27

Makes sense.

I just finished working on implementing Linux static builds with  Docker (https://github.com/monero-project/monero-gui/pull/2974). That's what we will be using for future releases.

The resulting Monero GUI binary requires glibc 2.23, it is available even on fairly old OSes.

## xiphon | 2020-07-02T18:14:16+00:00
Btw, you can try to build it yourself:

1. Install Docker [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
2. Clone the repository
   ```
   git clone --recursive https://github.com/monero-project/monero-gui.git
   cd monero-gui
   ```
3. Download and apply https://patch-diff.githubusercontent.com/raw/monero-project/monero-gui/pull/2974.patch patch
   ```
   git apply 2974.patch
   ```
4. Prepare build environment
   ```
   docker build --tag monero:build-env-gui --build-arg THREADS=4 .
   ```
   \* `4` - number of CPU threads to use

5. Build
   ```
   docker run --rm -it -v <MONERO_GUI_DIR_FULL_PATH>:/monero-gui -w /monero-gui monero:build-env-gui sh -c 'USE_SINGLE_BUILDDIR=ON DEV_MODE=ON make release-static -j4'
   ```
   \* `<MONERO_GUI_DIR_FULL_PATH>` - absolute path to `monero-gui` directory  
   \* `4` - number of CPU threads to use
5. Monero GUI Linux static binaries will be placed in  `monero-gui/build/release/bin` directory

## selsta | 2020-09-07T21:14:36+00:00
Resolved in v0.16.0.3

# Action History
- Created by: micromatrix14 | 2020-07-02T17:20:52+00:00
- Closed at: 2020-09-07T21:14:36+00:00
