---
title: failed tx shows as PENDING
source_url: https://github.com/monero-project/monero-gui/issues/898
author: gsee
assignees: []
labels:
- bug
- resolved
created_at: '2017-10-07T13:18:10+00:00'
updated_at: '2017-12-13T11:36:16+00:00'
type: issue
status: closed
closed_at: '2017-12-13T11:36:16+00:00'
---

# Original Description
I sent a transaction a couple weeks ago that still shows as PENDING in the GUI, however in the monero-wallet-cli logs it shows as failed

```
2017-10-07 12:42:00.790	  0x7fffc261c3c0	INFO 	msgwriter	src/common/scoped_message_writer.h:102	  failed    out       2017-09-18       2.000000000000 6adf283c420088ca40f777e2c5da78fc221e9707b88f8715417eaa13c7ea8552 b7f600e43beecab950fb14e807948b2540ec7a145c24bc4b404b78c5c421ca7b 0.013293280000 https://forum.getmonero.org/contribute/88459
```

<img width="686" alt="screen shot 2017-10-06 at 6 44 45 pm" src="https://user-images.githubusercontent.com/1143691/31308178-8dc104ea-ab37-11e7-914d-9e029bdffc84.png">


# Discussion History
## dEBRUYNE-1 | 2017-10-16T19:07:00+00:00
+bug

## dEBRUYNE-1 | 2017-12-13T11:21:31+00:00
+resolved

# Action History
- Created by: gsee | 2017-10-07T13:18:10+00:00
- Closed at: 2017-12-13T11:36:16+00:00
