---
title: GUI issues 0.17.1.4
source_url: https://github.com/monero-project/monero-gui/issues/3238
author: throoweway387
assignees: []
labels: []
created_at: '2020-11-15T18:22:43+00:00'
updated_at: '2021-01-15T10:25:53+00:00'
type: issue
status: closed
closed_at: '2021-01-15T10:25:53+00:00'
---

# Original Description
Some GUI issues I noticed after I started using monero, I'm using Linux with KDE desktop

1. In Settings - Log tab, there is "log level" menu, it doesn't have any option except 0. 

2. Settings - Log tab, "Daemon log" box has texts in invisible font when you use Dark theme. you must select the text  to see it. If you use Light theme then all new text in the box will be visible.

3. Send tab on left side, if you type something in the "Address" box, it's also invisible if you use dark theme, with light theme it's ok.

4. Settings - Node tab, Blockchain location and Daemon startup flags are invisible with dark theme, light theme OK again. Unless it is a bug in my desktop configs...

5. When creating new wallet, the seed and height were written in invisible font (dark theme was used). 


# Discussion History
## selsta | 2020-11-15T19:11:12+00:00
Did you install using your package manager or from getmonero.org?

## selsta | 2020-11-16T17:45:36+00:00
Please try the getmonero.org version

## jonathancross | 2020-12-14T14:42:48+00:00
Friendly ping @throoweway387 

## xiphon | 2021-01-15T10:25:53+00:00
Looks like invalid build env configuration.

Either [build reproducible Monero GUI from source (Linux, Windows)](https://github.com/monero-project/monero-gui#compiling-the-monero-gui-from-source) or use official Monero GUI binaries from https://getmonero.org.

# Action History
- Created by: throoweway387 | 2020-11-15T18:22:43+00:00
- Closed at: 2021-01-15T10:25:53+00:00
