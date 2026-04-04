---
title: '"wallet/wallet2_api.h: No such file or directory" when running make'
source_url: https://github.com/monero-project/monero-gui/issues/18
author: hackmyl1fe
assignees: []
labels: []
created_at: '2016-09-08T21:15:50+00:00'
updated_at: '2016-11-01T08:25:22+00:00'
type: issue
status: closed
closed_at: '2016-11-01T08:25:22+00:00'
---

# Original Description
I tried to install monero-core multiple times now and i keep running into the same error.

I run ./get_libwallet_api.sh and it finishes successfully. I run qmake, I does not give me any outputs.
Then I run make and it complains about a missing file. The file is actually there but under bitmonero/src/wallet and not src/wallet. Im not sure if im missing some steps but im following the install guide.

Im running ubuntu 16.04 in a VM in case this is an issue


# Discussion History
## radfish | 2016-09-10T05:50:40+00:00
You need to manually merge PR #14 in order to build, because monero daemon repo was updated to not build/install wallet lib/headers by default (need to pass `BUILD_GUI_DEPS=ON` option).


## medusadigital | 2016-09-28T20:09:53+00:00
solution got merged to master with https://github.com/monero-project/monero-core/commit/c87eed558fa564509c611625d75a2f8ae7357527

no more issues, can be closed


# Action History
- Created by: hackmyl1fe | 2016-09-08T21:15:50+00:00
- Closed at: 2016-11-01T08:25:22+00:00
