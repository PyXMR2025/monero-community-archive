---
title: Rare crash when loading password protected wallet
source_url: https://github.com/monero-project/monero-gui/issues/230
author: mochaccinuh
assignees: []
labels: []
created_at: '2016-11-30T22:55:30+00:00'
updated_at: '2016-12-14T21:27:38+00:00'
type: issue
status: closed
closed_at: '2016-12-14T21:27:38+00:00'
---

# Original Description
This can happen 1 in 20ish runs on my macbook running osx.

I don't know what is causing this but my best guess is that it has something to do with the async wallet close design. The application will first try to open the wallet with blank password. This fails, async wallet cleanup is initiated (can this be blocked by modal password dialog?), and password dialog gets generated. When correct password is entered the wallet gets loaded, and here the rare crash might occur. If the wallet has no password it will just open it straight away, minimizing risk with far less back and forth logic going on.

# Discussion History
## Jaqueeee | 2016-12-04T12:19:44+00:00
It takes a couple of seconds to close a wallet so this error can occur when trying to close a wallet multiple times. Please try #237

## Jaqueeee | 2016-12-08T15:03:16+00:00
Please test #249

# Action History
- Created by: mochaccinuh | 2016-11-30T22:55:30+00:00
- Closed at: 2016-12-14T21:27:38+00:00
