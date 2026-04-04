---
title: Create seperate QML application specifically for mobile
source_url: https://github.com/monero-project/monero-gui/issues/2026
author: sanderfoobar
assignees: []
labels: []
created_at: '2019-03-19T02:41:05+00:00'
updated_at: '2019-03-19T02:47:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
We make an effort in trying to ensure the QML we code runs on desktop, mobile, and tablet via stuff like `isMobile()` and `* scaleRatio`. This is not particularly pretty and more importantly, I don't think it would be wise to pursue [true responsiveness](https://www.w3schools.com/html/html_responsive.asp) within a single application,  at least not in QML.

I propose we create a second QML application specifically for mobile that's totally separate from our existing codebase. We should spawn a QML engine in `main.cpp` based on `isMobile`.

This way, the mobile application is not at the mercy of the 'flow' of the GUI, in terms of existing logic and views. GUI is made desktop-first, so it would be silly to try and 'make everything smaller' and hope this approach is good UX on mobile

To sum up;

- Don't have to create crazy logic to support all kinds of screen sizes
- More performance, as we can optimize our QML specifically for mobile.

We'll need something custom to give mobile support the proper attention. Doesn't have to be a complicated QML application.

# Discussion History
# Action History
- Created by: sanderfoobar | 2019-03-19T02:41:05+00:00
