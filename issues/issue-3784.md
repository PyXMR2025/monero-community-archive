---
title: The daemon ran without enough storage available
source_url: https://github.com/monero-project/monero-gui/issues/3784
author: RJ-Frosty
assignees: []
labels: []
created_at: '2021-12-08T02:40:04+00:00'
updated_at: '2021-12-08T02:44:53+00:00'
type: issue
status: closed
closed_at: '2021-12-08T02:44:53+00:00'
---

# Original Description
./monerod` ran with less that 75Gs of space available. on the cli.  In the gui repository 
Don't know if cli version checks but if it does it didn't work.

Canonical-Ubuntu-20.04-aarch64-2021.10.15-0
Shape: VM.Standard.A1.Flex
OCPU count: 2
Network bandwidth (Gbps): 2
Memory (GB): 12 - I think, I deleted the instance when the disk filled up.
47 GB PARAVIRTUALIZED boot volume

Following from: monero-gui/src/daemon/DaemonManager.cpp

QStorageInfo storage(dataDir);
    if (storage.isValid() && storage.isReady()) {
        if (storage.isReadOnly()) {
            readOnly = true;
            valid = false;
        }

        // Make sure there is 75GB storage available
        storageAvailable = storage.bytesAvailable()/1000/1000/1000;
        if (storageAvailable < 75) {
            valid = false;
        }
    } else {
        valid = false;
    } 

# Discussion History
## RJ-Frosty | 2021-12-08T02:42:51+00:00
Don't know why the code looks like that.

## selsta | 2021-12-08T02:44:42+00:00
Can you be a bit more precise what you did? Did you run the GUI or the CLI?

The CLI does not have a space check.

## RJ-Frosty | 2021-12-08T02:44:53+00:00
Wrong project.

# Action History
- Created by: RJ-Frosty | 2021-12-08T02:40:04+00:00
- Closed at: 2021-12-08T02:44:53+00:00
