---
title: '`cuprated` peer list write is not atomic, prevents startup'
source_url: https://github.com/Cuprate/cuprate/issues/399
author: hinto-janai
assignees: []
labels:
- A-p2p
- C-bug
- A-binaries
created_at: '2025-03-12T13:05:21+00:00'
updated_at: '2025-04-10T13:25:47+00:00'
type: issue
status: closed
closed_at: '2025-04-10T13:25:47+00:00'
---

# Original Description
## Bug
Peer list writes are not atomic:

https://github.com/Cuprate/cuprate/blob/21ad35d44a465efbb5414a902cb6c370b8358303/p2p/address-book/src/store.rs#L47

Peer list reads do not have a recovery method so if a un-readable file exists, it will prevent `cuprated` from starting due to:

https://github.com/Cuprate/cuprate/blob/21ad35d44a465efbb5414a902cb6c370b8358303/p2p/address-book/src/lib.rs#L70-L71

## Expected behavior
- Recovery method on the (de)serialization (e.g. skip + warn on read fail)
- Atomic writes (`write(tmp_file)` -> `rename(tmp_file, actual_file)` or database instead of binary file)

## Steps to reproduce
1. Start `cuprated`
2. Run out of disk space (and maybe have an unlucky peer list write at the same time?)
3. See error `ERROR Could not save peer list to disk, got error: No space left on device (os error 28)`
4. Cannot launch `cuprated`, blocked by: `ERROR Failed to open peer list, Unexpected length of input`

# Discussion History
## NorrinRadd | 2025-04-06T22:42:14+00:00
Options
======
- The atomic write is a bit difficult. Can embed a light db, but does everyone want that? 
- Can make it more safe but not completely safe by writing to temp first, delete old file, rename new_file -> old_file. 

Preference? I can push what I have now that performs the latter. I think the latter is fine actually, because with the safe recovery that's added, it's an edge case that the delete would succeed and the rename fail, and it recovers safely regardless. 

# Action History
- Created by: hinto-janai | 2025-03-12T13:05:21+00:00
- Closed at: 2025-04-10T13:25:47+00:00
