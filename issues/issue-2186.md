---
title: 'EulerOS How to use it '
source_url: https://github.com/xmrig/xmrig/issues/2186
author: oneoy
assignees: []
labels: []
created_at: '2021-03-16T10:39:19+00:00'
updated_at: '2021-03-21T12:26:50+00:00'
type: issue
status: closed
closed_at: '2021-03-21T12:26:50+00:00'
---

# Original Description
user@r90yglzvzkh-machine:~$ cat /etc/os-release 
NAME="EulerOS"
VERSION="2.0 (SP8)"
ID="euleros"
ID_LIKE="rhel fedora centos"
VERSION_ID="2.0"
PRETTY_NAME="EulerOS 2.0 (SP8)"
ANSI_COLOR="0;31"

# Discussion History
## oneoy | 2021-03-16T10:40:46+00:00
bash: ./xmrig: cannot execute binary file: Exec format error

## Lonnegan | 2021-03-16T15:46:26+00:00
Type "uname -a" into your console to check which kernel you are running. Then type "file xmrig" into the console and double check if you downloaded the right version of xmrig for your system. EulerOS is just a variant of CentOS which is a variant of Red Hat Linux. So it should work if you've chosen the right binary :)

# Action History
- Created by: oneoy | 2021-03-16T10:39:19+00:00
- Closed at: 2021-03-21T12:26:50+00:00
