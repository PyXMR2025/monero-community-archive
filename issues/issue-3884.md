---
title: Operation not permitted while trying to run monerod (v0.17.3.1) (Linux)
source_url: https://github.com/monero-project/monero-gui/issues/3884
author: manuel-arguelles
assignees: []
labels: []
created_at: '2022-04-10T03:16:07+00:00'
updated_at: '2022-04-11T22:47:33+00:00'
type: issue
status: closed
closed_at: '2022-04-11T22:47:33+00:00'
---

# Original Description
Hi, I just downloaded monero gui version 0.17.3.1, the gui itself opens ok, asks for my wallet's password, opens the wallet and then says the daemon failed to start. So I tried to start the daemon manually and got:
`
bash: ./monerod: Operation not permitted`

The permissions looks fine: 
`
-rwxr-xr-x 1 user user  22M Nov 30 17:07 monerod`

architecture is amd64 as expected:

```
monero-gui-v0.17.3.1 file ./monerod
./monerod: ELF 64-bit LSB shared object, x86-64, version 1 (GNU/Linux), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=5d280d59a6080601a0a2486acf256418218dfd0b, with debug_info, not stripped
```

my system:
```
uname -r -p
5.4.0-105-generic x86_64
```

Version 0.17.1.9 works fine. (On a side node, why is it shipped with debug symbols?)


# Discussion History
## selsta | 2022-04-11T22:21:53+00:00
Where did you download the GUI from?

## manuel-arguelles | 2022-04-11T22:23:45+00:00
@selsta from getmonero.com, the sha256 matched...

## selsta | 2022-04-11T22:24:44+00:00
Do you mean getmonero.org? getmonero.com is not the official site.

## manuel-arguelles | 2022-04-11T22:26:48+00:00
yes sorry:
02e8e32455383cf32030e33511656492a352788a619a0c9220ec360c2e863ef9  monero-gui-linux-x64-v0.17.3.1.tar.bz2


## selsta | 2022-04-11T22:29:50+00:00
Can you download v0.17.3.0 CLI from getmonero.org and check if the monerod binary works? It should be the same binary as in v0.17.3.1 GUI.

## manuel-arguelles | 2022-04-11T22:36:51+00:00
Similar:
2627571a3350b91173e7a4d1cf0d404825188d6fceae9caa4e1e1a6ea05ef062  monerod

```
$ file ./monerod
./monerod: ELF 64-bit LSB shared object, x86-64, version 1 (GNU/Linux), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=5d280d59a6080601a0a2486acf256418218dfd0b, with debug_info, not stripped
```

```
$ ./monerod
bash: ./monerod: Operation not permitted
```



## selsta | 2022-04-11T22:38:31+00:00
This is the first report we are getting about this. Anything specific with your local setup?

## manuel-arguelles | 2022-04-11T22:47:33+00:00
Sorry I just realized the problem, Carbon Black Cloud Sensor was getting in the way :-1: 

# Action History
- Created by: manuel-arguelles | 2022-04-10T03:16:07+00:00
- Closed at: 2022-04-11T22:47:33+00:00
