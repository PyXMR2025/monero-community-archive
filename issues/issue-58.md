---
title: get_libwallet_api.sh static build flags
source_url: https://github.com/monero-project/monero-gui/issues/58
author: peronero
assignees: []
labels: []
created_at: '2016-10-12T22:31:46+00:00'
updated_at: '2016-12-22T20:42:54+00:00'
type: issue
status: closed
closed_at: '2016-12-22T20:42:54+00:00'
---

# Original Description
openSUSE doesn't ship static versions of libraries causing this script to fail due to it requiring static versions of libboost components. This might be the case with Arch as well.

Stripping out 'STATIC=ON -D' from the script successfully compiles a working monero-core build in Tumbleweed - albeit not yet tested with monerod and the blockchain. 

Are the static build flags actually necessary?


# Discussion History
## dternyak | 2016-10-13T06:04:52+00:00
This happens on OSX as well based on some user reports (not mine).


## anonimal | 2016-10-13T16:12:43+00:00
On Arch (or with the [AUR package](https://aur.archlinux.org/packages/monero/)) I've never had this problem but I cannot confirm with a recent build because of #51.


## mbg033 | 2016-10-15T09:06:22+00:00
Static build is required for Windows at least (as it should work outside of msys2 environment and normally Windows PC doesn't have any boost and other dependencies installed).

I'll try without static on Linux, but normally it should be something like `libmonero-dev` (or `libwallet-dev`) package which installs libwallet_api, appropriate headers + all dependencies, so building GUI doesn't involve building libwallet (monero).

Actually at the beginning I wanted to have it as "one big package containing all dependencies and installing to the separate directory into filesystem, like /opt", but yes, makes sense to use packages infrastructure on Linux.


## fluffypony | 2016-11-13T17:59:36+00:00
Closing as fixed


## peronero | 2016-11-13T20:58:55+00:00
This doesn't look fixed to me but cannot confirm - I think I still see the offending flag in the bash script but now also get boost errors compiling monerod.

EDIT: This is not fixed.

## fluffypony | 2016-11-13T21:05:57+00:00
Reopened by request


# Action History
- Created by: peronero | 2016-10-12T22:31:46+00:00
- Closed at: 2016-12-22T20:42:54+00:00
