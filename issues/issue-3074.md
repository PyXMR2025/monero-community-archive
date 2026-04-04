---
title: 'Inconsistent terminology: "generate" vs. "create"'
source_url: https://github.com/monero-project/monero/issues/3074
author: ordtrogen
assignees: []
labels: []
created_at: '2018-01-06T21:58:15+00:00'
updated_at: '2018-01-26T00:50:11+00:00'
type: issue
status: closed
closed_at: '2018-01-26T00:50:11+00:00'
---

# Original Description
Referring to the file of localizable strings, translations/monero.ts

The words 'generate' and 'create' are used inconsistently. 'Generate' is more frequent than 'Create'. Should be consistent. There are flags such as --generate-new-wallet which, unless we want to change the flags, suggest 'generate' should be preferred.

I think for things like wallets and other cryptographic things, 'generate' is correct, whereas files (and transactions) are 'created'.

Examples which are correct:
"failed to generate new wallet:"
"failed to generate key derivation from supplied parameters"
"Attempting to generate or restore wallet, but specified file(s) exist."
"Generated new wallet:"
"Generate wallet from private keys"

Should change to 'generate':
"Create non-deterministic view and spend keys"
"Cannot create deprecated wallets from JSON"

Ok:
"Failed to find a way to create transactions."
"Failed to create file"



# Discussion History
## ordtrogen | 2018-01-06T21:58:28+00:00
related to https://github.com/monero-project/monero-gui/issues/1062


# Action History
- Created by: ordtrogen | 2018-01-06T21:58:15+00:00
- Closed at: 2018-01-26T00:50:11+00:00
