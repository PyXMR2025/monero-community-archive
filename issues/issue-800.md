---
title: Abide by the LGPL
source_url: https://github.com/monero-project/monero-gui/issues/800
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-07-23T23:44:22+00:00'
updated_at: '2018-04-13T19:01:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Including Qt copyright notices in the binary releases, and include prominent iinks to the source, including exact revisions used for this particular binary. Might also need to host Qt source ourselves.

# Discussion History
## Ashaman- | 2018-03-30T12:49:53+00:00
Since it is the act of distribution that triggers the relevant clauses of the LGPL, aside from possibly inclusion of a QT copyrigh notice, the fact that both on the github repo and at getmonero.org there are prominently displayed links to the source right next to the links to the binaries is sufficient to comply with the terms of the license.

## pazos | 2018-04-03T19:24:01+00:00
@moneromooo-monero:

> Including Qt copyright notices in the binary releases, and include prominent iinks to the source

You mean a text file or something in the GUI? Most qt based projects add an "about qt" page somewhere which includes the link to the official page and/or sources

> including exact revisions used for this particular binary

This is done in #1239, it uses runtime qt, but should match the build time qt in static builds.


>  Might also need to host Qt source ourselves.

Not needed unless we modify those sources ourselves

## pazos | 2018-04-13T19:01:10+00:00
A screen like this should be a good starting point (from bitcoin-core):

![qt](https://user-images.githubusercontent.com/975883/38753109-a9b57f22-3f5d-11e8-8caa-769c090d9547.png)


# Action History
- Created by: moneromooo-monero | 2017-07-23T23:44:22+00:00
