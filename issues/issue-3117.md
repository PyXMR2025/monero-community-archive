---
title: prevent user from `export_key_images` to a filename that will overwrite .keys
  file
source_url: https://github.com/monero-project/monero/issues/3117
author: PsychicCat
assignees: []
labels: []
created_at: '2018-01-14T22:20:26+00:00'
updated_at: '2018-02-18T19:31:06+00:00'
type: issue
status: closed
closed_at: '2018-02-18T19:31:06+00:00'
---

# Original Description
I have seen a couple sorry users report on reddit with problems because they executed `export_key_images` overwriting their .keys file without knowing what it was doing. 

Perhaps the command could check if they are about to write to a filename that is the same as their wallet and error out beforehand.



# Discussion History
## stoffu | 2018-01-14T23:38:50+00:00
#3118 

## moneromooo-monero | 2018-02-18T19:23:37+00:00
+resolved

# Action History
- Created by: PsychicCat | 2018-01-14T22:20:26+00:00
- Closed at: 2018-02-18T19:31:06+00:00
