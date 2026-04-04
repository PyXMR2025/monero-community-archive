---
title: The installed GUI wallet cannot find wallets in C:\Users\%USER%\Documents\Monero\wallets
source_url: https://github.com/monero-project/monero-gui/issues/3891
author: elibroftw
assignees: []
labels: []
created_at: '2022-04-23T16:17:43+00:00'
updated_at: '2023-01-21T09:36:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue has been happening for over a month now, I'm not sure what I did, but the installed GUI cannot detect my wallets:
![image](https://user-images.githubusercontent.com/21298211/164914364-6e7a938f-7b84-44d0-9307-0c03e31185e2.png)
This is how it should look at shown by a portable GUI (downloaded from https://github.com/monero-project/monero-gui/issues/3840#issuecomment-1105961410)
![image](https://user-images.githubusercontent.com/21298211/164914406-f6f67d30-ab27-41cc-83ef-1f42167cf8c1.png)


# Discussion History
## qqiumax | 2022-04-26T01:05:14+00:00
I see your directory is from %USER% file, which is a wildcard file, you could switch to another identified user or Administrator in your computer.

## elibroftw | 2022-04-26T04:00:47+00:00
You misunderstand. That's just the title to help others find the issue. My wallet files are located in the user folder I'm logged in as. 

## selsta | 2023-01-18T06:04:34+00:00
@elibroftw Do you still have this issue?

## elibroftw | 2023-01-18T12:02:35+00:00
Away from home until Friday so can't check till then. 

## elibroftw | 2023-01-20T23:08:38+00:00
Yeah I reinstalled the Monero GUI from the latest release and the issue is still present.

## selsta | 2023-01-21T09:36:50+00:00
Thank you, what I don't understand is why there are no other reports about this issue, it must be something related to the local Windows setup.

# Action History
- Created by: elibroftw | 2022-04-23T16:17:43+00:00
