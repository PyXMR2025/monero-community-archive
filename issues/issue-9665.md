---
title: '[Bug] monerod on win does not load bitmonero.conf from default data dir without
  setting --config-file'
source_url: https://github.com/monero-project/monero/issues/9665
author: 5andr0
assignees: []
labels:
- reproduction needed
created_at: '2024-12-30T22:41:57+00:00'
updated_at: '2025-03-18T03:51:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
monerod v0.18.3.4 won't load bitmonero.conf from default dir C:\ProgramData\bitmonero without setting any cli arguments. 
I had to set --config-file=C:\ProgramData\bitmonero\bitmonero.conf
I tested it multiple times on win 11 latest by setting a unique log-file in the conf
That broke my last sync with alternating prune settings that I had in the bitmonero.conf

# Discussion History
## selsta | 2025-02-19T17:54:02+00:00
Can you explain what you mean with prune settings? You only have to set `--prune-blockchain` once for it to be pruned.

## 5andr0 | 2025-02-22T08:35:18+00:00
> Can you explain what you mean with prune settings? You only have to set `--prune-blockchain` once for it to be pruned.

Oh, thanks for the clarification. I thought it bricked my chain data when it loaded for a while without prune blockchain enabled, so I resynced from scratch again.

Anyways, the bug still persists about not loading the default bitmonero.conf

## 0xFFFC0000 | 2025-02-25T07:07:32+00:00
![Image](https://github.com/user-attachments/assets/bcfc3bb8-6f0b-4736-b4ab-119e8dc68e06)

It is not a bug; it is expected behavior. 

IF you are running on admin it will load from `CSIDL_APPDATA` ( `C:\ProgramData` ). If you are not admin, it will load from `CSIDL_APPDATA` (`C:\Users\<Username>\AppData\Roaming`) 

## nahuhh | 2025-03-18T03:51:28+00:00
@5andr0 if you run with no args, is the blockchain synced to `C:\ProgramData\bitmonero`?

# Action History
- Created by: 5andr0 | 2024-12-30T22:41:57+00:00
