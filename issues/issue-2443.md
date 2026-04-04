---
title: unable to connect to monero network
source_url: https://github.com/monero-project/monero-gui/issues/2443
author: jasonwee
assignees: []
labels:
- resolved
created_at: '2019-11-13T11:18:16+00:00'
updated_at: '2019-11-25T15:49:56+00:00'
type: issue
status: closed
closed_at: '2019-11-25T09:00:43+00:00'
---

# Original Description
When launch the app, this is shown

`Connected daemon is not compatible with GUI. Please upgrade or connect to another daemon`

using current version, 0.14.1.0, any fix for this?

# Discussion History
## selsta | 2019-11-13T11:19:17+00:00
Are you using simple mode? If no,  local/remote node?

## jasonwee | 2019-11-13T12:04:51+00:00
Not sure what you mean by your questions. But it only happen since today.

i start using the following command line,

`./start-gui.sh`

and then it show that error messages.

## SamsungGalaxyPlayer | 2019-11-13T20:36:13+00:00
What does it say under settings -> info? Make sure to remove any sensitive details if you send screenshots.

![image](https://user-images.githubusercontent.com/12520755/68802117-ec387880-0622-11ea-8d5f-44bc5ba375ba.png)

## jasonwee | 2019-11-14T05:12:51+00:00
Sure, thank you for looking and below are the screenshots.

![Screenshot from 2019-11-14 09-31-32](https://user-images.githubusercontent.com/3326279/68828376-67ac2f80-06e0-11ea-8b8e-6aee09602328.png)
![Screenshot from 2019-11-14 09-31-43](https://user-images.githubusercontent.com/3326279/68828377-67ac2f80-06e0-11ea-82de-61e8bd38adcf.png)


## jasonwee | 2019-11-14T05:13:51+00:00
I have been using this app for a while now and it rocks! But this problem only come yesterday and I'm puzzled as this is the current latest version. Not sure what should I do, can you tell me if I have to do anything manually?

## SamsungGalaxyPlayer | 2019-11-14T16:52:04+00:00
Is the reason because it's connected to a 0.15 node?

## jasonwee | 2019-11-14T16:57:18+00:00
I have no idea, there is no changes on configuration other than just launching the app. Do you mean I have to upgrade the app or use another configuration?

## selsta | 2019-11-14T20:13:15+00:00
I would suggest restarting a couple times until the error goes away. Not ideal but v0.15 GUI should be out soon.

## jasonwee | 2019-11-14T23:51:39+00:00
Restart? Tried many many times, when it does not work, it don't work.

What I did, start again the app by moving these directory and resetup the wallet.
```
user@localhost:$ mv Monero/ Monero-backup
user@localhost:$ mv .bitmonero/ .bitmonero-backup/
user@localhost:$ 
```

Resync everything and it seem to work again. Awesome!

## jasonwee | 2019-11-15T09:41:03+00:00
Unfortunately it happen again :'( guess I will have to wait for the new release. Do you know if the new release will fix current problem that I'm facing?

## selsta | 2019-11-15T09:44:31+00:00
Go to the wizard, select "Change wallet mode" and then select Advanced mode.

Open you wallet again, go to Settings -> Node -> Select remote node and enter the following:

Address: `uwillrunanodesoon.moneroworld.com`
Port: `18089`

Hit connect and it should work again.

## EmbeddedAndroid | 2019-11-19T18:11:04+00:00
I hit this today as well, when I updated my remote nodes to v0.15.0.0 fwiw. Seems that the new daemon code has broken compatibility with the older GUI.

## selsta | 2019-11-19T18:11:50+00:00
v0.15.0.1 is tagged, binaries should be out in the next 24-48 hours. This issue should be resolved then.

## EmbeddedAndroid | 2019-11-19T18:21:47+00:00
> v0.15.0.1 is tagged, binaries should be out in the next 24-48 hours. This issue should be resolved then.

Great, thank you!

## dEBRUYNE-1 | 2019-11-25T08:56:16+00:00
This should be fixed with the GUI v0.15.0.1 release.



## dEBRUYNE-1 | 2019-11-25T08:56:20+00:00
+resolved

## djp1701 | 2019-11-25T12:48:13+00:00
Unfortunately, the issue persists with 0.15.0.1 as I downloaded and installed yesterday and am experiencing the same behavior as jasonwee...been using the Monero wallet for years and this only started happening yesterday when I went to update the app in preparation for RandomX

## selsta | 2019-11-25T12:54:10+00:00
@djp1701 Which remote node are you connecting to? Try node.xmr.to:18081

## EmbeddedAndroid | 2019-11-25T15:49:56+00:00
I can confirm v0.15.0.1 gui works with my v0.15.0.1 local daemon now, thanks!

# Action History
- Created by: jasonwee | 2019-11-13T11:18:16+00:00
- Closed at: 2019-11-25T09:00:43+00:00
