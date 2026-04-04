---
title: View only wallet unknown key
source_url: https://github.com/monero-project/monero-gui/issues/2882
author: ogil109
assignees: []
labels: []
created_at: '2020-05-03T13:11:11+00:00'
updated_at: '2020-05-06T09:10:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

I'm trying to integrate Monero in my eCommerce. After creating the view only wallet from the Monero GUI I have been told that the pass to access this wallet is the same as the one that it comes from. Well, it isn't. I can't access the view only wallet. Do you know that kind of problem? I could use Monero CLI but I'd rather solve it with GUI as long as I don't have any experience with terminal or code. Thanks

# Discussion History
## selsta | 2020-05-03T13:36:38+00:00
I can’t reproduce the issue. Can you delete the view only wallet and try again?

## ogil109 | 2020-05-03T15:52:42+00:00
I've done it several times.

<img width="651" alt="Captura de pantalla 2020-05-03 a las 17 40 30" src="https://user-images.githubusercontent.com/64007529/80918691-95f0fa80-8d66-11ea-98ad-d8fccfa19b07.png">
<img width="952" alt="Captura de pantalla 2020-05-03 a las 17 40 57" src="https://user-images.githubusercontent.com/64007529/80918701-9ee1cc00-8d66-11ea-9b54-11819f2151d1.png">
<img width="431" alt="Captura de pantalla 2020-05-03 a las 17 49 28" src="https://user-images.githubusercontent.com/64007529/80918706-a4d7ad00-8d66-11ea-9ddf-1d80044a49cc.png">

I'm using the Mac version of GUI and a Ledger Nano S. I honestly don't know what is happening...

## selsta | 2020-05-03T15:54:05+00:00
Can you try without Ledger Nano S?

## ogil109 | 2020-05-03T15:55:47+00:00
I tried both ways, it seems like it has nothing to do with the Ledger, but I cannot understand what password was set by default.

Edit: Also, the daemon doesn't stop working. When I try to log in, just after that, a message displaying "Waiting for daemon to stop" keeps appearing every 2 seconds.

## ogil109 | 2020-05-03T16:05:24+00:00

![ezgif com-video-to-gif](https://user-images.githubusercontent.com/64007529/80919120-a3a77f80-8d68-11ea-820d-9db443ac32ef.gif)


## selsta | 2020-05-06T09:10:13+00:00
@ogil109 Regarding your second issue: #2888

# Action History
- Created by: ogil109 | 2020-05-03T13:11:11+00:00
