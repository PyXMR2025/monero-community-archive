---
title: '[v3.0.0 or v2.99.6-beta] xmrig creating file ''null'' and logging to file'
source_url: https://github.com/xmrig/xmrig/issues/1114
author: seanwhe
assignees: []
labels: []
created_at: '2019-08-13T16:11:13+00:00'
updated_at: '2019-08-13T17:24:33+00:00'
type: issue
status: closed
closed_at: '2019-08-13T17:24:33+00:00'
---

# Original Description
xmrig creating file 'null' and logging to file.

Is there a new logging feature in XMRig 2.99.6-beta?
If yes, then what json must be added?
If no, then what am I missing?

==========================================
xmrig v2.99.6-beta shows changes for v3.0.0
https://github.com/xmrig/xmrig/blob/beta/CHANGELOG.md 

==========================================
But HEAD of origin/beta checkout builds :

$ xmrig -V
XMRig 2.99.6-beta
 built on Aug 13 2019 with GCC 7.4.0
 features: 64-bit AES

libuv/1.18.0
OpenSSL/1.1.1
hwloc/1

=========
https://github.com/xmrig/xmrig/blob/beta/CHANGELOG.md 

talks about
- [#257](https://github.com/xmrig/xmrig-nvidia/pull/257) New logging subsystem, file and syslog now always without colors.
for xmrig-nvidia and I know there is a logging subsystem on the xmrig-proxy.

===================================
Testing
Directory before starting xmrig

$ ls -lash
total 164K
4.0K drwxrwxr-x  4 sean sean 4.0K Aug 13 17:52 .
4.0K drwxr-xr-x 33 sean sean 4.0K Aug 13 17:52 ..
4.0K -rwxrwxr-x  1 sean sean 1004 Aug 12 15:40 build.sh
4.0K -rw-rw-r--  1 sean sean 1.3K Aug 13 17:45 config.json
4.0K -rwxrwxr-x  1 sean sean  134 Aug 12 15:40 config.sh
4.0K -rw-r--r--  1 sean sean 3.6K Jul 30 19:09 CONTRIBUTING.md
   0 -rw-rw-r--  1 sean sean    0 Jul 27 12:12 CONTRIBUTORS
4.0K -rw-rw-r--  1 sean sean  177 Aug 13 17:41 crontab
4.0K -rwxrwxr-x  1 sean sean  416 Aug 12 15:40 crontab-off.sh
4.0K -rwxrwxr-x  1 sean sean  433 Aug 12 15:40 crontab-on.sh
4.0K -rwxrwxr-x  1 sean sean  574 Aug 12 15:40 crontab.sh
4.0K -rwxrwxr-x  1 sean sean  435 Aug 12 19:49 depends.sh
4.0K -rwxrwxr-x  1 sean sean 4.0K Aug 13 17:33 functions.sh
4.0K drwxrwxr-x  8 sean sean 4.0K Aug 13 17:51 .git
4.0K -rw-rw-r--  1 sean sean   70 Aug 13 17:48 .gitignore
4.0K -rwxr-xr-x  1 sean sean 1.5K Aug 13 17:27 input.sh
 12K -rw-r--r--  1 sean sean  12K Aug 13 17:27 .input.sh.swp
4.0K -rwxrwxr-x  1 sean sean 1.2K Aug 12 20:07 install.sh
 36K -rw-rw-r--  1 sean sean  35K Jul 27 12:12 LICENSE
4.0K -rwxrwxr-x  1 sean sean  238 Aug 12 20:08 maintenance.sh
4.0K -rwxrwxr-x  1 sean sean  213 Aug 13 17:35 mysettings.sh
4.0K -rw-r--r--  1 sean sean 1.7K Aug 13 17:51 null
8.0K -rw-rw-r--  1 sean sean 5.7K Aug 12 15:40 README.md
4.0K -rwxrwxr-x  1 sean sean 2.7K Aug 13 17:12 settings.sh
 12K -rw-r--r--  1 sean sean  12K Aug 13 17:14 .settings.sh.swp
4.0K -rwxrwxr-x  1 sean sean  746 Aug 12 15:40 start.sh
4.0K -rwxrwxr-x  1 sean sean  381 Aug 12 15:40 stop.sh
4.0K -rwxr-xr-x  1 sean sean  136 Aug 12 15:40 update.sh
4.0K drwxrwxr-x  8 sean sean 4.0K Aug 13 17:39 xmrig-cpu

Directory after starting xmrig

$ ls -lash
total 164K
4.0K drwxrwxr-x  4 sean sean 4.0K Aug 13 17:57 .
4.0K drwxr-xr-x 33 sean sean 4.0K Aug 13 17:52 ..
4.0K -rwxrwxr-x  1 sean sean 1004 Aug 12 15:40 build.sh
4.0K -rw-rw-r--  1 sean sean 1.3K Aug 13 17:57 config.json
4.0K -rwxrwxr-x  1 sean sean  134 Aug 12 15:40 config.sh
4.0K -rw-r--r--  1 sean sean 3.6K Jul 30 19:09 CONTRIBUTING.md
   0 -rw-rw-r--  1 sean sean    0 Jul 27 12:12 CONTRIBUTORS
   0 -rw-rw-r--  1 sean sean    0 Aug 13 17:57 crontab
4.0K -rwxrwxr-x  1 sean sean  416 Aug 12 15:40 crontab-off.sh
4.0K -rwxrwxr-x  1 sean sean  433 Aug 12 15:40 crontab-on.sh
4.0K -rwxrwxr-x  1 sean sean  574 Aug 12 15:40 crontab.sh
4.0K -rwxrwxr-x  1 sean sean  435 Aug 12 19:49 depends.sh
4.0K -rwxrwxr-x  1 sean sean 4.0K Aug 13 17:33 functions.sh
4.0K drwxrwxr-x  8 sean sean 4.0K Aug 13 18:02 .git
4.0K -rw-rw-r--  1 sean sean   70 Aug 13 17:48 .gitignore
4.0K -rwxr-xr-x  1 sean sean 1.5K Aug 13 17:27 input.sh
 12K -rw-r--r--  1 sean sean  12K Aug 13 17:27 .input.sh.swp
4.0K -rwxrwxr-x  1 sean sean 1.2K Aug 12 20:07 install.sh
 36K -rw-rw-r--  1 sean sean  35K Jul 27 12:12 LICENSE
4.0K -rwxrwxr-x  1 sean sean  238 Aug 12 20:08 maintenance.sh
4.0K -rwxrwxr-x  1 sean sean  213 Aug 13 17:35 mysettings.sh
**8.0K -rw-r--r--  1 sean sean 4.7K Aug 13 18:03 null**
8.0K -rw-rw-r--  1 sean sean 5.7K Aug 12 15:40 README.md
4.0K -rwxrwxr-x  1 sean sean 2.7K Aug 13 17:12 settings.sh
 12K -rw-r--r--  1 sean sean  12K Aug 13 17:14 .settings.sh.swp
4.0K -rwxrwxr-x  1 sean sean  746 Aug 12 15:40 start.sh
4.0K -rwxrwxr-x  1 sean sean  381 Aug 12 15:40 stop.sh
4.0K -rwxr-xr-x  1 sean sean  136 Aug 12 15:40 update.sh
4.0K drwxrwxr-x  8 sean sean 4.0K Aug 13 17:56 xmrig-cpu

Check file content and find logging. Tail confirms file is actively written to.

$ tail -f null 
[2019-08-13 18:02:29.071] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1900022
[2019-08-13 18:02:54.059] speed 10s/60s/15m 240.7 258.6 n/a H/s max 267.6 H/s
[2019-08-13 18:02:55.159] accepted (8/0) diff 10000 (201 ms)
[2019-08-13 18:03:07.346] accepted (9/0) diff 10000 (195 ms)
[2019-08-13 18:03:12.384] accepted (10/0) diff 10000 (194 ms)
[2019-08-13 18:03:24.081] speed 10s/60s/15m 251.7 253.5 n/a H/s max 267.6 H/s
[2019-08-13 18:03:24.935] accepted (11/0) diff 10000 (194 ms)
[2019-08-13 18:03:29.116] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1900022
[2019-08-13 18:03:52.286] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1900023
[2019-08-13 18:03:54.107] speed 10s/60s/15m 256.5 254.4 n/a H/s max 267.6 H/s

config.json
=============

{
    "api": {
        "id": null,
        "worker-id": "wks"
    },
    "http": {
        "enabled": true,
        "host": "192.168.1.47",
        "port": 8080,
        "access-token": null,
        "restricted": false
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": true,
        "priority": null,
        "asm": true,
        "cn": [0, 1, 2, 3],
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": "null",
    "pools": [
        {
            "algo": "cn/r",
            "url": "pool.supportxmr.com:3333",
            "user": "MFC9PTjaFscR2UU6ZwFCqJzGMUiZVbTM",
            "pass": "wks:person@example.com",
            "rig-id": "wks",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 30,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": "null",
    "watch": true
}

# Discussion History
## seanwhe | 2019-08-13T16:22:47+00:00
I should have added that on previous build of same version the behaviour described above does not exist

$ xmrig -V
XMRig 2.99.6-beta
 built on Aug 12 2019 with GCC 7.4.0
 features: 64-bit AES

libuv/1.18.0
OpenSSL/1.1.1
hwloc/1

========
$ ls -lash
total 140K
4.0K drwxrwxr-x 4 sean sean 4.0K Aug 12 12:38 .
4.0K drwxr-xr-x 7 sean sean 4.0K Aug 12 12:34 ..
4.0K -rwxrwxr-x 1 sean sean 1004 Aug 12 12:34 build.sh
4.0K -rw-rw-r-- 1 sean sean 1.3K Aug 12 12:38 config.json
4.0K -rwxrwxr-x 1 sean sean  134 Aug 12 12:34 config.sh
4.0K -rw-rw-r-- 1 sean sean 3.6K Jul 31 10:04 CONTRIBUTING.md
   0 -rw-rw-r-- 1 sean sean    0 Jul 29 13:36 CONTRIBUTORS
4.0K -rw-rw-r-- 1 sean sean  179 Aug 12 12:37 crontab
4.0K -rwxrwxr-x 1 sean sean  416 Aug 12 12:34 crontab-off.sh
4.0K -rwxrwxr-x 1 sean sean  433 Aug 12 12:34 crontab-on.sh
4.0K -rwxrwxr-x 1 sean sean  574 Aug 12 12:34 crontab.sh
4.0K -rwxrwxr-x 1 sean sean  429 Aug 12 12:34 depends.sh
8.0K -rwxrwxr-x 1 sean sean 4.4K Aug 12 12:34 functions.sh
4.0K drwxrwxr-x 8 sean sean 4.0K Aug 12 12:34 .git
4.0K -rw-rw-r-- 1 sean sean   65 Aug 12 12:34 .gitignore
4.0K -rwxrwxr-x 1 sean sean 2.0K Aug 12 12:34 input.sh
4.0K -rwxrwxr-x 1 sean sean 1.2K Aug 12 12:34 install.sh
 36K -rw-rw-r-- 1 sean sean  35K Jul 29 13:36 LICENSE
4.0K -rwxrwxr-x 1 sean sean  232 Aug 12 12:34 maintenance.sh
4.0K -rwxrwxr-x 1 sean sean  288 Aug 12 12:34 mysettings.sh
8.0K -rw-rw-r-- 1 sean sean 5.7K Aug 12 12:34 README.md
4.0K -rwxrwxr-x 1 sean sean 2.7K Aug 12 12:34 settings.sh
4.0K -rwxrwxr-x 1 sean sean  746 Aug 12 12:34 start.sh
4.0K -rwxrwxr-x 1 sean sean  381 Aug 12 12:34 stop.sh
4.0K -rwxrwxr-x 1 sean sean   96 Aug 12 12:34 update.sh
4.0K drwxrwxr-x 8 sean sean 4.0K Aug 12 12:36 xmrig-cpu

## xmrig | 2019-08-13T17:17:00+00:00
`"log-file": "null",` tell miner create file with name `null` because `"null"` is a string value, `"log-file": null,` disable log file, because it real `null`, filename not specified.
Thank you.

## seanwhe | 2019-08-13T17:24:30+00:00
Thanks

# Action History
- Created by: seanwhe | 2019-08-13T16:11:13+00:00
- Closed at: 2019-08-13T17:24:33+00:00
