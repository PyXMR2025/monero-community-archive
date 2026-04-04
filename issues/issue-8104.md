---
title: Spinning drive warning with no spinning drive
source_url: https://github.com/monero-project/monero/issues/8104
author: lbennett-stacki
assignees: []
labels: []
created_at: '2021-12-05T16:16:52+00:00'
updated_at: '2022-02-18T23:13:15+00:00'
type: issue
status: closed
closed_at: '2022-02-18T23:13:15+00:00'
---

# Original Description
Hello,

I'm getting a warning about monerod syncing to a spinning drive. I don't have any spinning drives, I have a regular SSD and an M.2 SSD. monerod is currently running in an wsl2 debian instance which is on the M.2.

Any ideas?

# Discussion History
## Gingeropolous | 2021-12-05T16:50:26+00:00
i mean, i think it can be ignored. It just means that whatever mechanism monero uses to detect the type of drive isn't working properly on your system. I don't think that the detection of a spinny drive changes any parameters.

Oh, so you essentially have a debian virtual machine on top of windows? yeah, I doubt the monero software can detect the hardware abstraction going on in the vm if I had to guess. 

## lbennett-stacki | 2021-12-05T17:09:09+00:00
Sure, makes sense. Just checking, thanks

## moneromooo-monero | 2021-12-23T10:26:49+00:00
You can look for a "rotational" pseudo file somewhere in the /sys/dev/block tree and cat it. That's what monero looks for. There may be several if you have more than one disk. The VMM might be filling these settings with default values for a "fake" disk layer.

# Action History
- Created by: lbennett-stacki | 2021-12-05T16:16:52+00:00
- Closed at: 2022-02-18T23:13:15+00:00
