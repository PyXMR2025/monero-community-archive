---
title: monero wallet v18 unusable in xwindows
source_url: https://github.com/monero-project/monero-gui/issues/4028
author: oppianmatt
assignees: []
labels: []
created_at: '2022-09-13T08:34:48+00:00'
updated_at: '2023-01-17T04:59:27+00:00'
type: issue
status: closed
closed_at: '2023-01-17T04:59:27+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/48596/189852677-f4a6551a-068d-49d7-b713-df087753e072.png)


Text is unreadable, overlays are transparent. Have tried changing themes but it doesn't want to use any theme settings I've changed.

v17 I can see clearly. 

Some messages from startup

```
2022-09-13 08:32:02.122	W Qt:5.15.5 GUI:- | screen: 1080x1857 - available: QSize(1080, 1826) - dpi: 90 - ratio:1.49832
2022-09-13 08:32:02.583	W QXcbConnection: Failed to initialize GLX
2022-09-13 08:32:04.280	W QXcbIntegration: Cannot create platform OpenGL context, neither GLX nor EGL are enabled
2022-09-13 08:32:06.371	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-09-13 08:32:06.371	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-09-13 08:32:06.372	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
...
```


# Discussion History
## selsta | 2022-09-13T12:30:57+00:00
How did you install monero-gui? We didn't anything between v0.17 and v0.18 that should cause this.

Try to start with the env var `QMLSCENE_DEVICE=softwarecontext` to use software rendering.

## selsta | 2023-01-17T04:59:27+00:00
Closing due to inactivity and no reply.

# Action History
- Created by: oppianmatt | 2022-09-13T08:34:48+00:00
- Closed at: 2023-01-17T04:59:27+00:00
