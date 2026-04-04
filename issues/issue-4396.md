---
title: Dockerfile build problem
source_url: https://github.com/monero-project/monero/issues/4396
author: opsxcq
assignees: []
labels: []
created_at: '2018-09-17T14:35:30+00:00'
updated_at: '2018-09-21T19:00:57+00:00'
type: issue
status: closed
closed_at: '2018-09-21T19:00:57+00:00'
---

# Original Description
While trying to build the current `Dockerfile` I get the following error

```
Removing intermediate container 36e7352bd87c
 ---> f4bc1ff22822
Step 35/40 : COPY --from=builder /src/build/release/bin/* /usr/local/bin/
COPY failed: no source files were specified
```

Since there isn't any file to be copied (Build files are stored on `/src/build/Linux/master/release`) the build fails.

# Discussion History
## moneromooo-monero | 2018-09-21T18:53:04+00:00
+resolved

# Action History
- Created by: opsxcq | 2018-09-17T14:35:30+00:00
- Closed at: 2018-09-21T19:00:57+00:00
