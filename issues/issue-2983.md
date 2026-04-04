---
title: 'Error opening wallet: internal error: failed to deserialize keys buffer'
source_url: https://github.com/monero-project/monero-gui/issues/2983
author: deathmorlock
assignees: []
labels: []
created_at: '2020-07-03T09:38:39+00:00'
updated_at: '2020-07-03T10:06:51+00:00'
type: issue
status: closed
closed_at: '2020-07-03T09:59:55+00:00'
---

# Original Description
Hello,  tried to restore monero gui wallet from keys and have such bug while import .key file
Error opening wallet: internal error: failed to deserialize keys buffer

# Discussion History
## selsta | 2020-07-03T09:41:58+00:00
What OS are you using? Can you try to restore from seed?

## deathmorlock | 2020-07-03T09:46:02+00:00
OS win 7 and tried on win 10.  Will test on ubuntu now.
No i  only have backups of keys file. What info i can collect for you for diagnost?
Also can send .key file (but only in private message)

## selsta | 2020-07-03T09:47:11+00:00
> failed to deserialize keys buffer

Usually means corrupted file. Where did you store it? How big is the file?

## deathmorlock | 2020-07-03T09:53:38+00:00
on external hdd.
7,73 KB.  
But yes,i think  you right. it's damaged. No other reasons as i see

## selsta | 2020-07-03T10:06:51+00:00
Did you manage to resolve the issue? Maybe try to directly copy it from HDD to Ubuntu.

Also my .keys file are 1.5KB, 7.73KB sounds weird.

# Action History
- Created by: deathmorlock | 2020-07-03T09:38:39+00:00
- Closed at: 2020-07-03T09:59:55+00:00
