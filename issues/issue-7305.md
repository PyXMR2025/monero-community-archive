---
title: New Monero Wallet GUI update is too big for my screen and I can't resize it.
source_url: https://github.com/monero-project/monero/issues/7305
author: ImNotASheep
assignees: []
labels: []
created_at: '2021-01-10T13:42:40+00:00'
updated_at: '2022-02-19T00:45:50+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:45:50+00:00'
---

# Original Description
Just downloaded the latest version of GUI wallet and when I opened it for the first time, the whole interface (including text) is enlarged compared to older versions. I cannot access the top bar to close/minimise/maximise, nor can I access the resize tool in the bottom right corner. Any way to manually resize the wallet before starting the .exe? Link to screenshot of problem: https://imgur.com/a/POOtFov

# Discussion History
## selsta | 2021-01-10T14:13:35+00:00
We now have high dpi support, previously everything was too small on high dpi screens. Did you set scaling inside Windows? How large is your screen?

## selsta | 2021-01-10T14:15:26+00:00
Did you start using the "start-high-dpi.bat" file?

## ImNotASheep | 2021-01-10T16:09:19+00:00
> Did you start using the "start-high-dpi.bat" file?

No, I started using the usual monero-wallet-GUI.exe 

## jonathancross | 2021-01-28T17:02:43+00:00
Hi @ImNotASheep 
Did `start-high-dpi.bat` work?

## selsta | 2021-01-28T17:03:58+00:00
We don't ship start-high-dpi.bat anymore, Windows now supports high dpi scaling.

## jonathancross | 2021-01-28T17:05:45+00:00
This should be moved to the monero-gui repo if there is still problems.

# Action History
- Created by: ImNotASheep | 2021-01-10T13:42:40+00:00
- Closed at: 2022-02-19T00:45:50+00:00
