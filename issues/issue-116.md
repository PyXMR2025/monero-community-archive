---
title: refresh during TRX construction process causes perfomance issues
source_url: https://github.com/monero-project/monero-gui/issues/116
author: medusadigital
assignees: []
labels: []
created_at: '2016-11-06T09:34:50+00:00'
updated_at: '2016-11-08T20:57:12+00:00'
type: issue
status: closed
closed_at: '2016-11-08T20:57:12+00:00'
---

# Original Description
qml: Creating transaction: 
qml: 	address:  46MNnPFNzsKMgE4EiMuoQ5iqZMPW3xk7UPq9NhTVPPZ1NjFLyswgAAWQief2czqUMZNEbpc3fuuXUP91YBiz2qiAPgs5kXM , payment_id:  c2fe1f596290687a , amount:  1 , mixins:  4 , priority:  1
qml: integer amount:  1000000000000
qml: integer unlocked 3290000000000
2016-Nov-06 10:26:22.046489 827119 outputs of size 1.000000000000
2016-Nov-06 10:26:22.046534 Using 1 recent outputs
2016-Nov-06 10:26:22.046571 asking for output 455821 for 1.000000000000
2016-Nov-06 10:26:22.046584 asking for output 621627 for 1.000000000000
2016-Nov-06 10:26:22.046595 asking for output 644660 for 1.000000000000
2016-Nov-06 10:26:22.046607 asking for output 695206 for 1.000000000000
2016-Nov-06 10:26:22.046623 asking for output 734827 for 1.000000000000
2016-Nov-06 10:26:22.046635 asking for output 800341 for 1.000000000000
2016-Nov-06 10:26:22.046647 asking for output 825419 for 1.000000000000
2016-Nov-06 10:26:22.046659 asking for output 826766 for 1.000000000000
2016-Nov-06 10:26:22.447273 amount=1.000000000000, real_output=3, real_output_in_tx_index=3, indexes: 621627 644660 800341 825419 826766 
2016-Nov-06 10:26:22.447666 Encrypted payment ID: <49fa72d102a76f51>
2016-Nov-06 10:26:22.730495 Found new pool tx: <f8cbf32f3006b458c60226d1027b48baf6228669a9eb3150ef534df2d2faef11>
2016-Nov-06 **10:26:22.820071** Refresh done, blocks received: 0, balance: 3.290000000000, unlocked: 3.290000000000
refreshed
2016-Nov-06 **10:26:41.854404** 827119 outputs of size 1.000000000000
2016-Nov-06 10:26:41.854436 Using 1 recent outputs
2016-Nov-06 10:26:41.854467 275961 outputs of size 0.090000000000
2016-Nov-06 10:26:41.854478 Using 1 recent outputs
2016-Nov-06 10:26:41.854506 asking for output 189254 for 1.000000000000
2016-Nov-06 10:26:41.854517 asking for output 247567 for 1.000000000000
2016-Nov-06 10:26:41.854528 asking for output 538304 for 1.000000000000
2016-Nov-06 10:26:41.854538 asking for output 584337 for 1.000000000000
2016-Nov-06 10:26:41.854548 asking for output 650521 for 1.000000000000
2016-Nov-06 10:26:41.854558 asking for output 811540 for 1.000000000000
2016-Nov-06 10:26:41.854569 asking for output 825419 for 1.000000000000
2016-Nov-06 10:26:41.854579 asking for output 826470 for 1.000000000000
2016-Nov-06 10:26:41.854589 asking for output 91693 for 0.090000000000
2016-Nov-06 10:26:41.854600 asking for output 241857 for 0.090000000000
2016-Nov-06 10:26:41.854610 asking for output 249811 for 0.090000000000
2016-Nov-06 10:26:41.854620 asking for output 259596 for 0.090000000000
2016-Nov-06 10:26:41.854631 asking for output 266801 for 0.090000000000
2016-Nov-06 10:26:41.854641 asking for output 271913 for 0.090000000000
2016-Nov-06 10:26:41.854651 asking for output 274394 for 0.090000000000
2016-Nov-06 10:26:41.854661 asking for output 275314 for 0.090000000000

# Discussion History
# Action History
- Created by: medusadigital | 2016-11-06T09:34:50+00:00
- Closed at: 2016-11-08T20:57:12+00:00
