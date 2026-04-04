---
title: ' Failed to open lmdb environment: Invalid argument'
source_url: https://github.com/monero-project/monero/issues/6533
author: chrissound
assignees: []
labels: []
created_at: '2020-05-14T22:37:26+00:00'
updated_at: '2022-02-19T04:40:29+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:40:29+00:00'
---

# Original Description
Running this in a qemu vm.

```
[130] root@nixos> monerod --data-dir /mount/moneromount/mon-block                                                                        /mount
2020-05-14 22:36:05.954	I Monero 'Carbon Chamaeleon' (v0.15.0.0-unknown)
2020-05-14 22:36:05.954	I Initializing cryptonote protocol...
2020-05-14 22:36:05.954	I Cryptonote protocol initialized OK
2020-05-14 22:36:05.954	I Initializing core...
2020-05-14 22:36:05.955	I Loading blockchain from folder /mount/moneromount/mon-block/lmdb ...
2020-05-14 22:36:05.957	W Failed to open lmdb environment: Invalid argument
2020-05-14 22:36:05.961	E Error opening database: Failed to open lmdb environment: Invalid argument
2020-05-14 22:36:05.963	I Stopping cryptonote protocol...
2020-05-14 22:36:05.963	I Cryptonote protocol stopped successfully
2020-05-14 22:36:05.964	E Exception in main! Failed to initialize core
```

Version:
```
[1] root@nixos> monerod --version                                                                                                        /mount
Monero 'Carbon Chamaeleon' (v0.15.0.0-unknown)
```

# Discussion History
## chrissound | 2020-05-14T22:44:29+00:00
Works correctly if I don't mount the vm mount path.. 

```
[127] root@nixos> mount | grep mon                                                                                                       /mount
a457b9c00b7152b02ceea27e7fe1a07 on /mount/moneromount type 9p (rw,relatime,sync,dirsync,access=client,trans=virtio)
```

I suppose something to do with the 9p mount type? 

## hyc | 2020-05-14T23:03:35+00:00
Most likely that 9p filesystem doesn't support mmap.

## moneromooo-monero | 2020-05-15T23:24:07+00:00
https://github.com/monero-project/monero/pull/6536 will make it clear when a lmdb init failure is due to mmap. Assuming lmdb doens't need support for more fancy usage hyc ?

## hyc | 2020-05-16T00:04:13+00:00
Well.... it *should* be enough that mmap works. But there are things like WSL that may still fail.
https://github.com/microsoft/WSL/issues/3451#issuecomment-415251320


# Action History
- Created by: chrissound | 2020-05-14T22:37:26+00:00
- Closed at: 2022-02-19T04:40:29+00:00
