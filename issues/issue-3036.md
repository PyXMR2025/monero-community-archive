---
title: enable_1gb_pages.sh doesn't set 1GB pages
source_url: https://github.com/xmrig/xmrig/issues/3036
author: ericrpatton
assignees: []
labels: []
created_at: '2022-04-27T19:57:31+00:00'
updated_at: '2022-04-27T21:20:53+00:00'
type: issue
status: closed
closed_at: '2022-04-27T21:20:53+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
I am running this script in Linux Mint 20.3, using kernel 5.14.0-1034. When executing enable_1gb_pages.sh, there are two problems: the first is that the command "sysctl" is not found on my system, and the second issue is that even if I susbstitute "systemctl" into the script instead of "sysctl" and rerun it, there is no '"-w" flag in the systemctl command, so the script terminates.

**Expected behavior**
1GB hugepagesize should be set without any errors from the script.

**Required data**
`>` enable_1gb_pages.sh 
systemctl: invalid option -- 'w'`

**Additional context**
Add any other context about the problem here.


# Discussion History
# Action History
- Created by: ericrpatton | 2022-04-27T19:57:31+00:00
- Closed at: 2022-04-27T21:20:53+00:00
