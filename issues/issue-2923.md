---
title: subaddresses as the standard
source_url: https://github.com/monero-project/monero-gui/issues/2923
author: Sunray-Nucleon
assignees: []
labels: []
created_at: '2020-05-25T12:32:04+00:00'
updated_at: '2020-05-27T15:50:53+00:00'
type: issue
status: closed
closed_at: '2020-05-27T15:48:52+00:00'
---

# Original Description
Can we make subaddresses the standard? Let's hide the 4... address behind a "advanced" menu named 'show secret integrated address' and advice users to not give out this main address.

Maybe create a first subadress automatic at first wallet-start and display it, or just show a button 'create address' but not show 4... address in first place, instead hide it.

We would want to propagate the use of subaddresses, right? [_edit: removed naming thought_]

Integrated addresses would, of cause, still work. Its meant as change of display and treat addresses in a better way.

# Discussion History
## rating89us | 2020-05-27T06:56:39+00:00
I agree with your proposal.

Currently the wallet's primary/main address (4...) is being displayed in the Settings > Seed & Keys page, and I believe it should only be displayed there: 
![image](https://user-images.githubusercontent.com/45968869/82987161-647eee00-9ff7-11ea-89ba-f7524a4b4a8a.png)

Account page should not display main address or subaddresses anymore (see #2925)

In my opinion, receive page should only create and display subaddresses.

## Sunray-Nucleon | 2020-05-27T15:48:52+00:00
> remove first address of each account: displaying a single address for each account incentivizes address reuse, discourages use of subaddresses, and gives a false idea that each account has an "official" or "main" address

this point of #2925 hits it - hide initial 4... address and show 8... address! thank you

# Action History
- Created by: Sunray-Nucleon | 2020-05-25T12:32:04+00:00
- Closed at: 2020-05-27T15:48:52+00:00
