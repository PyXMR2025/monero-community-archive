---
title: Various small UI bugs / possible improvements
source_url: https://github.com/monero-project/monero-gui/issues/1806
author: selsta
assignees: []
labels: []
created_at: '2018-12-12T17:41:02+00:00'
updated_at: '2018-12-21T22:26:27+00:00'
type: issue
status: closed
closed_at: '2018-12-21T22:26:26+00:00'
---

# Original Description
- ~~The “Stop daemon” button has the wrong size.~~ (#1809)
- ~~*Settings -> Log:* Looks wrong the first time the GUI is opened. Lot’s of bugs on the whole page. Qt 5.12 related.~~ (#1813)
- ~~*Settings -> Node:* “Stop local node” button has no mouseover hover effect.~~ (#1815)
- ~~*Settings:* Grey buttons have no mouseover hover effect.~~ (#1817, #1818)
- ~~The height of most of the pages is weird, e.g. why can scroll this far on the Transfer page?~~ (#1834)

# Discussion History
## mmbyday | 2018-12-13T19:03:45+00:00
Great attention to detail. ;)

## mmbyday | 2018-12-13T19:09:25+00:00
As for "The height of most of the pages is weird, e.g. why can scroll this far on the Transfer page?"

That's because flickable needs a contentHeight value. Currently this is hard-coded.  Might need a way to dynamically add up all the component's heights, or maybe there's a better way...
```
 State {
                name: "Transfer"
                PropertyChanges { target: root; currentView: transferView }
                PropertyChanges { target: mainFlickable; contentHeight: 1000 * scaleRatio }
```

# Action History
- Created by: selsta | 2018-12-12T17:41:02+00:00
- Closed at: 2018-12-21T22:26:26+00:00
