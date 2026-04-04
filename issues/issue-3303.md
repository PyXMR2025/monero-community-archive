---
title: GUI won't load on Ubuntu 18.04
source_url: https://github.com/monero-project/monero-gui/issues/3303
author: XMR2020
assignees: []
labels: []
created_at: '2021-01-13T12:36:04+00:00'
updated_at: '2021-01-13T13:05:35+00:00'
type: issue
status: closed
closed_at: '2021-01-13T13:05:35+00:00'
---

# Original Description
Previous releases have worked on my machine. With the latest monero-gui-v0.17.1.9 I get:

2021-01-13 12:21:22.219	E Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags<QSurfaceFormat::FormatOption>(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior QSurfaceFormat::DoubleBuffer, swapInterval 1, colorSpace QSurfaceFormat::DefaultColorSpace, profile  QSurfaceFormat::NoProfile) 
Aborted (core dumped)

# Discussion History
## XMR2020 | 2021-01-13T12:37:09+00:00
NVIDIA 980Ti Driver version 440.100

## selsta | 2021-01-13T12:37:51+00:00
Is this the getmonero.org version?

Can you confirm that v0.17.1.8 is still working? We did not change anything between these two versions so that is weird.

## selsta | 2021-01-13T12:39:13+00:00
This sounds like you have issues with your graphic drivers.

## XMR2020 | 2021-01-13T12:53:17+00:00
Yeah, some kind of graphics card issue. Rebooted the system and now working fine. 

## selsta | 2021-01-13T13:05:35+00:00
Closing this here as it does not seem like a monero bug. Maybe would try to update / reinstall your graphic drivers.

# Action History
- Created by: XMR2020 | 2021-01-13T12:36:04+00:00
- Closed at: 2021-01-13T13:05:35+00:00
