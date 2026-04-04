---
title: libjasper
source_url: https://github.com/monero-project/monero-gui/issues/900
author: danrmiller
assignees: []
labels:
- resolved
created_at: '2017-10-12T19:55:30+00:00'
updated_at: '2017-10-27T13:54:14+00:00'
type: issue
status: closed
closed_at: '2017-10-27T13:54:14+00:00'
---

# Original Description
See https://build.getmonero.org/builders/monero-core-win64/builds/946/steps/deploy/logs/stdio

```cp: cannot stat '/mingw64/bin/libjasper-1.dll': No such file or directory```

https://github.com/monero-project/monero-core/blob/master/windeploy_helper.sh

I am trying to do a static build, do we need to include libjasper?

If we include libjasper, do we need to include a copyright notice or license file?

# Discussion History
## danrmiller | 2017-10-17T16:05:35+00:00
And do we build libjasper or where does it come from?

## danrmiller | 2017-10-17T16:30:33+00:00
@mbg033 

## dEBRUYNE-1 | 2017-10-27T13:47:02+00:00
+resolved

# Action History
- Created by: danrmiller | 2017-10-12T19:55:30+00:00
- Closed at: 2017-10-27T13:54:14+00:00
