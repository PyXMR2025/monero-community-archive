---
title: xmrig application denied - Meraki blacklisted blocking app
source_url: https://github.com/xmrig/xmrig/issues/671
author: teshy
assignees: []
labels:
- av
created_at: '2018-06-02T16:18:07+00:00'
updated_at: '2018-06-17T17:56:45+00:00'
type: issue
status: closed
closed_at: '2018-06-17T17:56:45+00:00'
---

# Original Description
I can no longer run xmrig on my laptop after a Cisco Meraki update was applied. I get 
-bash: ./xmrig-amd: Permission denied
When trying to run the application.
What would I need to change in the source code to get around the issue, I imaging Meraki is looking for some kind of app ID or signature. I tried changing the values in version.h file with no success.

# Discussion History
# Action History
- Created by: teshy | 2018-06-02T16:18:07+00:00
- Closed at: 2018-06-17T17:56:45+00:00
