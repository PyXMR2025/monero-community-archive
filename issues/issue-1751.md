---
title: 'Developer Guides: globe icon not being displayed on Chrome and Internet Explorer'
source_url: https://github.com/monero-project/monero-site/issues/1751
author: rating89us
assignees: []
labels:
- bug
created_at: '2021-08-01T16:21:27+00:00'
updated_at: '2021-08-07T14:58:24+00:00'
type: issue
status: closed
closed_at: '2021-08-07T14:58:24+00:00'
---

# Original Description
It is being displayed correctly on Firefox.

![image](https://user-images.githubusercontent.com/45968869/127778085-05df5646-dd42-4b33-8924-37f2607ab3ac.png)


# Discussion History
## erciccione | 2021-08-02T07:25:37+00:00
What operating system are you using?

I just tried Chromium and Chrome and all seems to be working well.

## erciccione | 2021-08-04T07:51:03+00:00
This seems to happen only on windows. I fixed by replacing the unicode images with SVGs. This will also make the page more uniform and less prone to this kind of problems: #1755

## rating89us | 2021-08-04T16:33:45+00:00
> This seems to happen only on windows. 

Yes, I'm using windows. Your PR fixes this issue.

# Action History
- Created by: rating89us | 2021-08-01T16:21:27+00:00
- Closed at: 2021-08-07T14:58:24+00:00
