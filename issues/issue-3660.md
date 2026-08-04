---
title: '"Use System Theme"'
source_url: https://github.com/monero-project/monero-gui/issues/3660
author: sirjamesgray
assignees: []
labels: []
created_at: '2021-08-06T23:59:14+00:00'
updated_at: '2026-08-03T06:35:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
currently we have a "Light theme" on/off toggle. 

I suggest we make "Theme" a drop-down or a segmented control with 3 options: 

1. Light theme 
2. Dark theme
3. System theme 

Thanks!

# Discussion History
## selsta | 2021-08-06T23:59:59+00:00
Which OS have an API for this?

## cirocosta | 2021-08-09T00:06:10+00:00
+1, defaulting to system theme

@selsta , macos does - https://developer.apple.com/documentation/appkit/nsapplication/2967171-effectiveappearance
 

## PPPDUD | 2024-03-31T14:16:33+00:00
+1 but the default theme should still be dark mode

## atraxsrc | 2026-08-03T01:57:53+00:00
Hi, just checking if there’s still interest in this.
I’m on Linux and would like better theme support (at least System / Light / Dark, and ideally the ability to have additional color schemes).
Would a clean PR that implements the three-option selector (and keeps the current light/dark behaviour) be welcome?
I’m also experimenting with a Catppuccin-style dark theme locally by editing Style.qml. If the system-theme change is accepted, I could later look at making the color sets more modular.
Thanks

## jpk68 | 2026-08-03T02:10:28+00:00
@atraxsrc Not sure about other themes like Catppuccin, but I'm sure there's still interest in this; yes, a PR would be welcome.

## atraxsrc | 2026-08-03T06:33:22+00:00
@jpk68 Thanks - I've opened #4670 implementing the System/Light/Dark selector.

Kept it deliberately narrow: no other themes, just the three-way choice from this issue. A couple of notes on the approach:

`Style.blackTheme` becomes a read-only derived property backed by a new `Style.theme` tri-state, so all 34 files that read it are untouched and only the four that wrote to it change.

For system detection I went with xdg-desktop-portal (`org.freedesktop.appearance color-scheme`) plus a Qt-palette fallback, and
made Qt5DBus an optional dependency so the depends/Guix setup doesn't need to change. I originally tried palette-only to avoid the dependency entirely, but it doesn't hold up: on COSMIC — and on any setup where the Qt palette comes
from a static qt5ct profile - the palette never reflects the user's actual choice, so "System" would silently do nothing.

Tested on Pop!_OS 24.04 / COSMIC / Wayland with live switching in both directions; screenshots are in the PR. Existing settings migrate and the old `blackTheme` key stays in sync so downgrades are safe. The default for new profiles is unchanged.

Happy to adjust anything - in particular whether "System" should become the default for new profiles, which I left out as a separate discussion.


# Action History
- Created by: sirjamesgray | 2021-08-06T23:59:14+00:00
