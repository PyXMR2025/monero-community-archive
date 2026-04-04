---
title: m_key_image_known in transfer_details is incorrect when exporting outputs in
  view only wallet
source_url: https://github.com/monero-project/monero/issues/1407
author: moneroexamples
assignees: []
labels: []
created_at: '2016-12-05T23:16:27+00:00'
updated_at: '2016-12-06T00:53:34+00:00'
type: issue
status: closed
closed_at: '2016-12-06T00:53:34+00:00'
---

# Original Description
As the title says. m_key_image_known in transfer_details is incorrect when exporting outputs in view only wallet. View only wallet does not have spend key, thus it can produce valid spend key when `export_outputs` is executed in view only wallet. 

Currently, when doing this, `m_key_image_known` is sent to `True`, subsequently, value of key_image in the outputs false, i.e.,  `m_key_image` is incorrect. This results in problem with processing key_images from output files, as its unclear how to differentiate between real key image (i.e., the one produced with normal wallet) and the one with incorrect one (i.e., the one produced with view only wallet).

# Discussion History
# Action History
- Created by: moneroexamples | 2016-12-05T23:16:27+00:00
- Closed at: 2016-12-06T00:53:34+00:00
