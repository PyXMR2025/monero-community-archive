---
title: 'Cannot choose hardware device: Creating new wallet'
source_url: https://github.com/monero-project/monero-gui/issues/3318
author: mr-optimate
assignees: []
labels: []
created_at: '2021-01-29T09:02:22+00:00'
updated_at: '2021-01-29T09:10:44+00:00'
type: issue
status: closed
closed_at: '2021-01-29T09:10:44+00:00'
---

# Original Description
See attached gif (the glitches around the sides of the program are from the screen capture software)
![no drop down](https://user-images.githubusercontent.com/78201439/106253527-99c28800-61e5-11eb-8bb3-b91a7ccb1bee.gif)
As you can see when I go to select what hardwear wallet i want to use from the drop down menu, no options drop down. The little arrow on the right is moving so it is registering as a click.

Specs:
monjaro - kernel 5.9.16-1 
Fresh install of monero-gui 0.17.1.9-1
ledger firmware is up to date as well as all the apps. (I dont think that maters in this case)

What I've tried to do:
restart the computer
reinstall monero-gui
restarting the program

I don't think this is a ledger problem since the drop down menu should appear even if I don't have a wallet plugged in, at least that's what the windows version of monero gui does. 

# Discussion History
## selsta | 2021-01-29T09:04:16+00:00
Is this installed using your package manager? If yes please try the getmonero.org version

## mr-optimate | 2021-01-29T09:09:36+00:00
Yes it was installed from the package manager. The getmonero.org version works as expected

## selsta | 2021-01-29T09:10:17+00:00
Ok, please reach out to the package maintainer. This is out of our control.

# Action History
- Created by: mr-optimate | 2021-01-29T09:02:22+00:00
- Closed at: 2021-01-29T09:10:44+00:00
