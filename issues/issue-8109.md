---
title: The daemon ran without enough storage available
source_url: https://github.com/monero-project/monero/issues/8109
author: RJ-Frosty
assignees: []
labels: []
created_at: '2021-12-08T02:46:49+00:00'
updated_at: '2022-05-29T15:36:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
./monerod` ran with less that 75Gs of space available. on the cli. In the gui repository
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
## serhack | 2021-12-19T10:27:15+00:00
IIRC Daemon warns you about the insufficient disk space, but does not prevent you from synchronizing.

# Action History
- Created by: RJ-Frosty | 2021-12-08T02:46:49+00:00
