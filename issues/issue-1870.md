---
title: 'docs: Update .profile'
source_url: https://github.com/monero-project/monero/issues/1870
author: grummerd
assignees: []
labels: []
created_at: '2017-03-16T06:02:49+00:00'
updated_at: '2017-03-17T18:16:12+00:00'
type: issue
status: closed
closed_at: '2017-03-17T18:16:12+00:00'
---

# Original Description
In section, "Build instructions"->"On Linux and OS X"

Monero binaries are added to the current user's PATH. I'm assuming most people are total noobs. Myself included. Just editing ~/.profile doesn't update the current session. Would be nice to skip login/logout or reboot

# The Original

- Add PATH="$PATH:$HOME/monero/build/release/bin" to .profile

# The requested change

- Add PATH="$PATH:$HOME/monero/build/release/bin" to .profile
Refresh PATH, `source ~/.profile`
`env` shows current session's environment including the value of PATH

# Discussion History
## grummerd | 2017-03-16T06:06:40+00:00
"Build instructions"->"On the Raspberry Pi"

same deal, but worse. After changing .profile, the next line says, "Run Monero with monerod --detach". Without `source ~/.profile` the monero deamon would be run without the monero bin in the current sessions's PATH

## grummerd | 2017-03-16T07:24:42+00:00
systemd.service is expecting to find monerod at `/usr/bin/monerod`. According to the manual, the monerod binary doesn't live there.

Why not make a symbolic link, so a PATH search can be avoided and editing the ~/.profile can also be avoided.

sudo ln -s ~/monero-master/build/release/bin/monerod /usr/bin/monerod

## grummerd | 2017-03-17T18:16:12+00:00
Found the root cause of my confusion

`git clone [the monero repository]`
will make the root folder `monero`

downloading and unzip'ing
with make the root folder `monero-master`

This is confusing from an UX perspective...But world+dog probably already know this. So lets retire this one. Use git clone and MINIMUM ubuntu 16.04 LTS. ubuntu 14.04 LTS libboost-all-dev is < v1.58. Installing it from source is a disaster

# Action History
- Created by: grummerd | 2017-03-16T06:02:49+00:00
- Closed at: 2017-03-17T18:16:12+00:00
