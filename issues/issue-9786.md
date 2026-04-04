---
title: Does Simplewallet support QR codes?
source_url: https://github.com/monero-project/monero/issues/9786
author: dbee01
assignees: []
labels:
- question
created_at: '2025-02-08T17:57:42+00:00'
updated_at: '2025-02-08T21:38:44+00:00'
type: issue
status: closed
closed_at: '2025-02-08T21:38:25+00:00'
---

# Original Description
I found this function in the Monero src:

`bool simple_wallet::show_qr_code(const std::vector<std::string> &args)`

I was under the impression Monero Simplewallet didn't natively support QR codes? 

# Discussion History
## selsta | 2025-02-08T21:38:25+00:00
It allows you to print a QR code to the console with the `show_qr_code` command. It does not allow you to scan QR codes.

# Action History
- Created by: dbee01 | 2025-02-08T17:57:42+00:00
- Closed at: 2025-02-08T21:38:25+00:00
