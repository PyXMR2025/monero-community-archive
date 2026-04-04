---
title: A better `start-gui.sh` script
source_url: https://github.com/monero-project/monero/issues/2088
author: oerdnj
assignees: []
labels: []
created_at: '2017-06-14T08:19:49+00:00'
updated_at: '2017-06-15T05:14:24+00:00'
type: issue
status: closed
closed_at: '2017-06-14T21:20:27+00:00'
---

# Original Description
The start-gui.sh script has to be run from the "installation" directory now as it runs `./monero-wallet-gui`. The improved version can be called from elsewhere including linking it to `~/bin/monero-gui` (as an example).

```
#!/bin/bash
MONERO_HOME=$(dirname $(realpath ${0}))
export LD_LIBRARY_PATH=${MONERO_HOME}/libs
export QT_PLUGIN_PATH=${MONERO_HOME}/plugins
export QML2_IMPORT_PATH=${MONERO_HOME}/qml
exec ${MONERO_HOME}/monero-wallet-gui
```

# Discussion History
## Jaqueeee | 2017-06-14T21:18:11+00:00
hi @oerdnj 
The GUI repo is here: https://github.com/monero-project/monero-core
Please submit the issue there instead, or even better a PR =)

## oerdnj | 2017-06-14T21:20:27+00:00
Will do, I just couldn't find the repository with the script. Thanks for the pointer. 

## oerdnj | 2017-06-15T05:14:24+00:00
Filled as https://github.com/monero-project/monero-core/issues/765

# Action History
- Created by: oerdnj | 2017-06-14T08:19:49+00:00
- Closed at: 2017-06-14T21:20:27+00:00
