---
title: 'CLI Wallet v0.16.0.0-Error: failed to generate new wallet: failed to save
  file "test.keys"'
source_url: https://github.com/monero-project/monero/issues/6654
author: downystreet
assignees: []
labels: []
created_at: '2020-06-14T04:52:23+00:00'
updated_at: '2021-08-15T03:55:24+00:00'
type: issue
status: closed
closed_at: '2021-08-15T03:55:24+00:00'
---

# Original Description
OS: CentOS 8, CLI-wallet verion: v0.16.0.0 
After downloading the Monero CLI from getmonero.org and starting up the wallet I go through the various steps of name and password, once it gets to the point where it asks you what language you you want and you enter a number and hit enter, the wallet exits with error code: Error: failed to generate new wallet: failed to save file "test.keys". I just downloaded this same file on my main computer without any problems and yet when I download it to the server it fails with error. Both computers are CentOS 8 with the only difference being that the server has no GUI.

# Discussion History
## moneromooo-monero | 2020-06-14T11:22:31+00:00
Are you sure you have write permissions on that directory for the user you're running as ?

## downystreet | 2020-06-14T15:27:33+00:00
Ok, you are correct, for some reason the directory didn't have write permissions. The wallet appears to be working normally as well.

# Action History
- Created by: downystreet | 2020-06-14T04:52:23+00:00
- Closed at: 2021-08-15T03:55:24+00:00
