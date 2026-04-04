---
title: A better `start-gui.sh` script
source_url: https://github.com/monero-project/monero-gui/issues/765
author: oerdnj
assignees: []
labels:
- resolved
created_at: '2017-06-15T05:14:03+00:00'
updated_at: '2017-08-07T18:55:11+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:55:11+00:00'
---

# Original Description
The start-gui.sh script has to be run from the "installation" directory now as it runs `./monero-wallet-gui`. The improved version can be called from elsewhere including linking it to `~/bin/monero-gui` (as an example).

I can find the script anywhere in the repository hence the issue and not PR.

```
#!/bin/bash
MONERO_HOME=$(dirname $(realpath ${0}))
export LD_LIBRARY_PATH=${MONERO_HOME}/libs
export QT_PLUGIN_PATH=${MONERO_HOME}/plugins
export QML2_IMPORT_PATH=${MONERO_HOME}/qml
exec ${MONERO_HOME}/monero-wallet-gui
```

# Discussion History
## jonathancross | 2017-06-16T20:43:40+00:00
Hi @oerdnj, the script is created here:
https://github.com/monero-project/monero-core/blob/master/linuxdeploy_helper.sh#L44

But this might have already been addressed in https://github.com/monero-project/monero-core/pull/723 ?

If not, you can make your change there and submit as a Pull Request.

## medusadigital | 2017-08-07T18:51:28+00:00
can this be considered as done?

looking good to me.

will close for now until further notice. please respond here or open a new ticket if there is still something that neeeds to be done.

+resolved

# Action History
- Created by: oerdnj | 2017-06-15T05:14:03+00:00
- Closed at: 2017-08-07T18:55:11+00:00
