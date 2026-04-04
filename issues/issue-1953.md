---
title: Issue Getting The Daemon Started
source_url: https://github.com/monero-project/monero/issues/1953
author: Jayhorns
assignees: []
labels: []
created_at: '2017-04-02T16:58:18+00:00'
updated_at: '2017-09-25T21:06:20+00:00'
type: issue
status: closed
closed_at: '2017-04-15T07:01:10+00:00'
---

# Original Description
I am having a near identical issue as a user on another forum. I am trying to use the Windows 64bit version of the GUI. The application appears to have synchronized successfully after about 8 hours, but I cannot get the daemon to start. I receive this message: "Daemon failed to start. Please check your wallet and daemon log for errors. You can also try to start monerod.exe manually." However, the log does not show any message or text at all. And despite the message, the network status still says Connected and monerod is running as a background process in the task manager.

The solution that seemed to work for another user did not work for me (rename the folder that contains the monero-wallet-gui Application to "MoneroGui2").

If I run the monerod application manually, eventually I get a message that says: "You are now synchronized with the network. You may now start monero-wallet-cli."

With all that said, am I synced with the network and able to send Monero to this wallet despite the error message with the daemon?

[http://i.imgur.com/dPVB7l6.png](url)

# Discussion History
## dEBRUYNE-1 | 2017-04-03T09:42:48+00:00
Could you post your issue at [this](https://github.com/monero-project/monero-core/) repository?

## Jayhorns | 2017-04-04T21:08:04+00:00
I will do so now. Thanks.

## voidzero | 2017-04-14T20:18:46+00:00
Feel free to close this one.

## pspitalieri | 2017-06-06T09:11:45+00:00
Thanks guys, changing the path to MoneroGui2 helped. Thumbs up

## passabilities | 2017-09-25T21:05:08+00:00
I was getting the same error on Ubuntu 17.04. I needed to start the daemon manually using `sudo ./monerod`

# Action History
- Created by: Jayhorns | 2017-04-02T16:58:18+00:00
- Closed at: 2017-04-15T07:01:10+00:00
