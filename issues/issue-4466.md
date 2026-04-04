---
title: Change the word 'background' in GUI mining to 'pause when active'
source_url: https://github.com/monero-project/monero-gui/issues/4466
author: PyXMR2025
assignees: []
labels: []
created_at: '2025-06-28T14:13:22+00:00'
updated_at: '2025-06-29T10:06:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Change the word 'background' in GUI mining to 'pause when active'

In GUI, the term 'background' does not intuitively imply that it refers to mining when the user is idle. Perhaps we need to change it.

After discussion in the Monero GUI channel.

# Discussion History
## PyXMR2025 | 2025-06-29T10:06:46+00:00
newbie20250619:newbie20250619
@day20250619:matrix.org
|
05:24 PM

Jackie

@day20250619:matrix.org If possible, register a Github account and open it https://github.com/monero-project/monero-gui/pull/4467/files Click on 'Approve' in the 'Review changes' section and then click on' Submit review '.

I have a Github account.
259 - text: qsTr("Background mining (experimental)") + translationManager.emptyString
259 + text: qsTr("Pause when active (experimental)") + translationManager.emptyString
At least twice I pointed that I don't like "pause when active" phrase. I'd rather prefer "Mine only when idle".
Maybe somebody else can approve "pause when active" instead of me.

# Action History
- Created by: PyXMR2025 | 2025-06-28T14:13:22+00:00
