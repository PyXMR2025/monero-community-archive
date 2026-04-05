---
title: 'Windows: `pause-on-active` should take into account media playback'
source_url: https://github.com/xmrig/xmrig/issues/2919
author: Tonux599
assignees: []
labels: []
created_at: '2022-02-03T18:18:22+00:00'
updated_at: '2022-05-08T23:26:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
`pause-on-active` is great but when playing media such as a full screen YouTube video on Chrome or a video file on VLC XMRig will resume from pause during playback. It should not.

**To Reproduce**
Enable `pause-on-active`. Start XMRig. Move mouse to have XMRig paused then open your favourite video on YouTube and play it full screen. Don't touch anything but wait the either the default 60 seconds or your preferred timeout and XMRig will resume.

**Expected behavior**
It would be good if XMRig could identify this media playback as the user being active.

**Additional context**
Chrome and VLC have the ability to tell Windows not to activate the screensaver or turn of the monitor when media is being played. If XMRig could hook into this also then the same "thing" that tells Windows that the user is enjoying the consumption of some media could also allow XMRig to know that also.


# Discussion History
## Spudz76 | 2022-02-03T20:34:23+00:00
Sorry it uses the [standard function GetLastInputInfo](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getlastinputinfo) and if it doesn't pay attention to videos playing then that's Microsoft's fault.

[This seems to say](https://stackoverflow.com/questions/57281699/how-to-detect-media-playing-with-c) there isn't a way to get any global signal that media is playing.  So again, blame Microsoft.

## Spudz76 | 2022-02-03T20:39:27+00:00
There is a [dev-featurePauseOnProcess branch on my fork](https://github.com/Spudz76/xmrig/tree/dev-featurePauseOnProcess) that adds ability to sense other programs running but all that would do is pause any time Chrome is running (no sense of if it's playing video, or just lurking Github).  I use it to pause mine any time VLC is running, but then I end up launching VLC just so it pauses while I do browser videos.

Config line is an array of substrings to check for in the process list.  This example is from Linux.
```
    "pause-on-process": ["/usr/bin/vlc", "make "],
```

This will never be merged since maintainers don't like it doing constant polling of process list in the mainloop, but I have been running this patch for a long time with no problems, and every time a new upstream `dev` branch drops I update this branch.

## Tonux599 | 2022-02-04T08:55:00+00:00
Thanks @Spudz76 I'll checkout your branch.

I would be curious also to whether or not GetLastInputInfo takes into account RDP input, as this is another of my use cases (will test this myself anyway in a few days).

I'll leave this issue open if that's okay as I still think it would be good to implement if/when it is possible.

To be honest, I think I'm possible leaning towards something along the lines using the HTTP API to pause and resume the miner when the screensaver is activated such that "whenever the screen is on, the user is active". Although this probably won't work when using RDP.

Thanks again!

## koitsu | 2022-05-08T23:26:18+00:00
`pause-on-active` *does* work across RDP (client: Windows 7 SP1, remote system: Windows 10 Pro 21H2, network: LAN), however it's somewhat flaky. It tends to notice mouse movement pretty well, but keyboard input not as well. On several occasions I witnessed xmrig not pausing at all on either type of input, which may be a quirk with how the pause/resume aspect is implemented in xmrig *or* a quirk in Windows. My conclusion is that GetLastInputInfo() might not work "as reliably" on RDP, so YMMV.

# Action History
- Created by: Tonux599 | 2022-02-03T18:18:22+00:00
