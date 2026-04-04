---
title: Clicking homepage video to pause will not pause
source_url: https://github.com/monero-project/monero-site/issues/1007
author: Samuel-Pedraza
assignees: []
labels:
- bug
created_at: '2020-05-25T01:37:55+00:00'
updated_at: '2020-06-02T04:23:07+00:00'
type: issue
status: closed
closed_at: '2020-06-02T04:23:07+00:00'
---

# Original Description
When I click "Play" on the video on the homepage, it will play.

However, if I click the body of the video in order to pause it, it will not pause. It only pauses when I click the pause button.

I could see how this could be determined as "expected behavior", but I thought I would bring it someone's attention as it surprised me.

I am using Chrome Version 81 on Windows 10.

I reproduced using Chrome, Version 81 on Windows 10 on browserstack.

Would this project be open to using an open source media player for videos? I've found the HTML5 video element to be quite buggy in it's implementation throughout browsers and that might be a more simplistic solution in the long run.

# Discussion History
## erciccione | 2020-05-25T08:51:23+00:00
I could reproduce this on the live version using chromium, but not locally. Actually, the video doesn't really work locally on chromium. I tried with #994 but i didn't notice any difference.

## Samuel-Pedraza | 2020-06-02T04:23:07+00:00
I think this bug can be closed, as I just tested this after the most recent Chrome update (version 83), and it seems to be working fine now.

# Action History
- Created by: Samuel-Pedraza | 2020-05-25T01:37:55+00:00
- Closed at: 2020-06-02T04:23:07+00:00
