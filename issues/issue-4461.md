---
title: Make monero gui aware of user locale in all aspects and all platforms
source_url: https://github.com/monero-project/monero-gui/issues/4461
author: godfuture
assignees: []
labels: []
created_at: '2025-06-17T10:58:55+00:00'
updated_at: '2025-08-26T01:05:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi guys,
I am using monero gui for windows and sitting in west europe. I noticed that using the clipboard or export does consider my current locale setting in windows. This means that the decimal separator is not correctly interpreted by my installed tools.

Please consider locale settings in different platforms consider the users locale (clipboard, export....what else?)

Best regards

# Discussion History
## SuperCryptoNoob | 2025-08-06T10:50:23+00:00
Could you explain in detail? What is your tool?

## godfuture | 2025-08-26T01:05:47+00:00
If you click the amount of XMR in a transaction, it is copied to clipboard. Pasting the number into other tools of your choice, it shows that decimal separator in number format is not according your current locale setting, but always a dot which is not compatible with my calculator app in win10.

And it seems other areas are also not user locale aware.

# Action History
- Created by: godfuture | 2025-06-17T10:58:55+00:00
