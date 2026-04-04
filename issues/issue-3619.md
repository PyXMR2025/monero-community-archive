---
title: Running Monero GUI full/partial node on Android might be harmful to internal
  storage
source_url: https://github.com/monero-project/monero-gui/issues/3619
author: CryptoGrampy
assignees: []
labels: []
created_at: '2021-07-12T13:56:15+00:00'
updated_at: '2021-07-12T14:46:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It was just brought to my attention by Howard Chu that running a full Monero node off of Android internal storage is likely harmful to the device and will likely cause that device to brick after some time.  

It *is* actually possible to build the Monero GUI APK for Android today and run a full node (I've tried it myself), so I think it may be a good idea to either disable the option completely for Android or ensure that it can only work in conjunction with an external microSD card on the device (which also will likely be shorter lived from Monero node usage).  

Bringing this up now because I don't want to see a bunch of people have phones burn out if Monero GUI ever gets fully released for Android.   

# Discussion History
## hyc | 2021-07-12T14:02:27+00:00
If anyone has an old phone they don't care about destroying, would be interesting to actually measure how long it takes for the internal storage to die. I've had two microSD cards die at around the 3 year mark so far from running a full node.

## CryptoGrampy | 2021-07-12T14:46:41+00:00
> If anyone has an old phone they don't care about destroying, would be interesting to actually measure how long it takes for the internal storage to die. I've had two microSD cards die at around the 3 year mark so far from running a full node.

I'll pick up a used device this week and start the experiment :+1: 

# Action History
- Created by: CryptoGrampy | 2021-07-12T13:56:15+00:00
