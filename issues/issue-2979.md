---
title: '[CMake] Build type Debug broken'
source_url: https://github.com/monero-project/monero-gui/issues/2979
author: sanderfoobar
assignees: []
labels: []
created_at: '2020-07-02T13:47:01+00:00'
updated_at: '2020-07-06T21:46:21+00:00'
type: issue
status: closed
closed_at: '2020-07-06T21:46:21+00:00'
---

# Original Description
Running with `-DCMAKE_BUILD_TYPE=Debug` will yield the error:

```
make[2]: *** No rule to make target 'monero/external/easylogging++/libeasylogging.a', needed by 'bin/monero-wallet-gui'.  Stop.
```

# Discussion History
## sanderfoobar | 2020-07-02T13:47:55+00:00
In addition, would be nice if our build bots could build in debug mode when this is fixed.

## sanderfoobar | 2020-07-06T21:46:20+00:00
Fixed since #2982

# Action History
- Created by: sanderfoobar | 2020-07-02T13:47:01+00:00
- Closed at: 2020-07-06T21:46:21+00:00
