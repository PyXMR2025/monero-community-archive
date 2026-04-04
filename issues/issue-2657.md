---
title: 'Windows: reduce flickering when resizing'
source_url: https://github.com/monero-project/monero-gui/issues/2657
author: tobtoht
assignees: []
labels: []
created_at: '2019-12-20T18:00:37+00:00'
updated_at: '2020-05-08T13:58:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
See: http://xmrguide42y34onq.onion/static/flickering.mp4 (Tor required)

# Discussion History
## selsta | 2019-12-21T04:38:06+00:00
Are you using a VM? I can reproduce on my system but it’s a VM. Might be solved once we move to newer Qt version.

## tobtoht | 2019-12-21T11:03:35+00:00
No, not a VM. Tested with v0.15.0.2 release binary running Windows 10 on real hardware.

>Might be solved once we move to newer Qt version.

Ok, I'll keep an eye out for this.

## selsta | 2020-05-08T13:58:16+00:00
As a workaround disabling custom decorations should solve the flickering issue.

We have our own resizing code when custom decorations are enabled which isn’t optimized.

To properly solve the issue we would have to write custom code for every OS to disable window decorations without disabling resizing.

# Action History
- Created by: tobtoht | 2019-12-20T18:00:37+00:00
