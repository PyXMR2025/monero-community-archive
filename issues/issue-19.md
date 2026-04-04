---
title: Automated Coverity uploads
source_url: https://github.com/monero-project/meta/issues/19
author: anonimal
assignees: []
labels: []
created_at: '2016-11-27T23:29:45+00:00'
updated_at: '2018-09-28T00:35:45+00:00'
type: issue
status: closed
closed_at: '2018-09-28T00:35:45+00:00'
---

# Original Description
For kovri and monero, I'm currently managing both but we easily have this automated (maybe weekly or daily). monero-core can be thrown into the mix too.

@danrmiller we can talk details in private.

# Discussion History
## anonimal | 2017-02-09T20:09:36+00:00
@danrmiller the coverity tool is also upgraded semi-frequently (our last scan in early November was with release 8.5.0.5. Today, their release version is 8.7.0). We should see if there is a way to automate downloading/upgrading.

## anonimal | 2017-02-09T20:17:59+00:00
@danrmiller Download link is at the bottom https://scan.coverity.com/projects/monero-project-kovri/builds/new

Note: they say they update their tool "twice yearly" but I don't think that counts for their patch point releases. I've seen varying results between those releases too so, we should try to automate updating the tool maybe once a month (arbitrary value).

## anonimal | 2018-09-28T00:35:45+00:00
I've taken this issue completely into my hands per my work in `#monero-vrp`. Builds are now automated and scans will run at least once a week for both monero and kovri.

# Action History
- Created by: anonimal | 2016-11-27T23:29:45+00:00
- Closed at: 2018-09-28T00:35:45+00:00
