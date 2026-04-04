---
title: Failed to store wallet
source_url: https://github.com/monero-project/monero-gui/issues/4403
author: mhoude1966
assignees: []
labels: []
created_at: '2025-01-24T17:59:06+00:00'
updated_at: '2025-01-26T11:31:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
New installation on Windows 11 LTSC and Server 2025, when I setup a new wallet, simple and/or advanced mode, I am getting the above error message.

Starting the app as administrator nor changing the paths and wallet name doesn't change anything.

I don't have any log files.

I really don't know what to do next...

Any ideas ?

Thanks

# Discussion History
## selsta | 2025-01-24T18:01:34+00:00
New installation meaning nothing else is installed yet? Anything else that would be out of the ordinary with your setup?

## mhoude1966 | 2025-01-24T18:28:28+00:00
Two brand new installations, right after the OS install.

## selsta | 2025-01-24T18:33:38+00:00
Did you setup with Onedrive?

## mhoude1966 | 2025-01-24T18:50:53+00:00
> Did you setup with Onedrive?

Nope

I even checked the permissions on the folders giving full control to everyone, nada.

## tobtoht | 2025-01-25T06:10:08+00:00
Go to Settings -> Info and check the wallet path.

Does it contain any:

- spaces 
- non-English characters
- characters with diacritics (e.g. é)

Edit: if you're unable to open the wallet, try creating a new wallet and check the 'Wallet location'.

## mhoude1966 | 2025-01-25T14:43:39+00:00
No spaces
Only English characters
No accented characters
Changed the location and wallet name
Happens with both Windows 11 LTSC and Server 2025, did not try Windows 10.

## mhoude1966 | 2025-01-25T22:47:00+00:00
How about a log to see why the wallet was not created instead of a generic error ?

## selsta | 2025-01-26T11:31:02+00:00
What happens if you enable "portable mode", does it allow you to store a wallet? You can enable it by clicking on "Change wallet mode" and selecting it under optional features.

# Action History
- Created by: mhoude1966 | 2025-01-24T17:59:06+00:00
