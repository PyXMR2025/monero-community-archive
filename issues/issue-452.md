---
title: Qt doesn't like &nbsp; in translations
source_url: https://github.com/monero-project/monero-gui/issues/452
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-02-04T16:27:42+00:00'
updated_at: '2017-02-04T17:33:47+00:00'
type: issue
status: closed
closed_at: '2017-02-04T17:33:47+00:00'
---

# Original Description
/home/user/bin/lrelease -compress -nounfinished -removeidentical translations/monero-core_fr.ts -qm /home/user/src/monero-core/release/bin/translations/monero-core_fr.qm
lrelease error: Parse error at translations/monero-core_fr.ts:68:50: Entity 'nbsp' not declared.


# Discussion History
# Action History
- Created by: moneromooo-monero | 2017-02-04T16:27:42+00:00
- Closed at: 2017-02-04T17:33:47+00:00
