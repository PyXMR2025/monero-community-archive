---
title: The "Receive" tab format gives an address that doesn't fit the "Spend" tab
  format
source_url: https://github.com/monero-project/monero-gui/issues/2359
author: dginovker
assignees: []
labels: []
created_at: '2019-08-24T18:41:34+00:00'
updated_at: '2019-11-13T15:03:13+00:00'
type: issue
status: closed
closed_at: '2019-11-13T15:03:13+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/32943174/63641477-24ac6400-c67d-11e9-82ac-a1d4d1a1c3ea.png)

The button here gives an output that looks like this: `monero:49dpgSbHdA6auSv2gMPEsfj3uXVqqon4LEGWpuhdfXJsULVLKjFXkFQhpywAU8WddGbsN2ZDDpiVb8byZH6FfgL2R7ZwKZE`

If you paste this in the send tab, it looks like this:

![image](https://user-images.githubusercontent.com/32943174/63641482-3aba2480-c67d-11e9-81f0-69c0e5a826ab.png)

And it's not a valid address.

# Discussion History
## xiphon | 2019-08-25T13:37:01+00:00
> If you paste this in the send tab, it looks like this:
> 
> And it's not a valid address.

Yep, is a bug with address pasting using keyboard shortcuts. 
Use "paste" button, it will handle this correctly.



# Action History
- Created by: dginovker | 2019-08-24T18:41:34+00:00
- Closed at: 2019-11-13T15:03:13+00:00
