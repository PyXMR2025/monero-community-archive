---
title: Migrate to Qt 6
source_url: https://github.com/monero-project/monero-gui/issues/4348
author: tobtoht
assignees: []
labels: []
created_at: '2024-09-01T10:54:29+00:00'
updated_at: '2024-09-02T07:17:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Qt 5.15 LTS commercial extended lifetime ends in [May 2025](https://www.qt.io/blog/qt-5.15-extended-support-for-subscription-license-holders). Due to an agreement with KDE, commercial releases become available under LGPL with a one year delay. However, we can't expect patches for critical issues or support for new platforms after official support ends.

Qt 6.8 is the latest LTS version, set for release in September 2024.

The required build system changes (CMake / Dockerfiles) are relatively straightforward. It's unclear to me at this time how much code needs to be modified to be compatible with Qt 6, and how much breakage there will be in the QML / graphical department.

Resources:

- https://doc.qt.io/qt-6/supported-platforms.html
- https://doc.qt.io/qt-6/portingguide.html

# Discussion History
## aperechnev | 2024-09-01T12:14:22+00:00
I had tried to compile Monero GUI with Qt6 and recognized that it depends on some libraries that aren't available in Qt6. `xmlpatterns` as an example, it's available in Qt5, but not in Qt6. So it looks like it'll be necessary to find a replacement for it. I noticed a couple of more libraries, but I don't remember their names.

## tobtoht | 2024-09-01T13:21:43+00:00
@aperechnev I think `find_package(Qt5XmlPatterns QUIET)` can simply be removed.

# Action History
- Created by: tobtoht | 2024-09-01T10:54:29+00:00
