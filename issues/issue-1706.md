---
title: Add build instuctions for CentOS 8
source_url: https://github.com/xmrig/xmrig/issues/1706
author: downystreet
assignees: []
labels: []
created_at: '2020-06-01T13:28:21+00:00'
updated_at: '2021-11-26T08:34:52+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:31:11+00:00'
---

# Original Description
I noticed there were no build instructions for CentOS 8 and I happen to have them. Several repositories have to be added to get a few of the packages as they are not included in the main repositories.
1. sudo dnf install epel-release
2. sudo dnf config-manager --set-enabled PowerTools
3. sudo rpm -ivh http://repo.okay.com.mx/centos/8/x86_64/release/okay-release-1-3.el8.noarch.rpm?
4. sudo dnf install git make gcc gcc-c++ libstdc++-static hwloc-devel openssl-devel libuv-devel
5. git clone https://github.com/xmrig/xmrig.git
6. mkdir xmrig/build && cd xmrig/build
7. cmake ..
8. make -j$(nproc)

# Discussion History
## xmrig | 2020-08-28T16:31:11+00:00
https://xmrig.com/docs/miner/build/centos8

## fadsel | 2021-11-26T08:34:52+00:00
Now these Build Instructions are not working any more
Please change **PowerTools** to `powertools`

Thankfully, the CentOS.org organization has [posted ](https://wiki.centos.org/Manuals/ReleaseNotes/CentOS8.2011#Yum_repo_file_and_repoid_changes) confirming and detailing the naming change.

Now the command should be 
`sudo dnf config-manager --set-enabled powertools`

Thanks


# Action History
- Created by: downystreet | 2020-06-01T13:28:21+00:00
- Closed at: 2020-08-28T16:31:11+00:00
