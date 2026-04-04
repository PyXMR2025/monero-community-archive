---
title: 'Inconsistent GUI terminology: "generate" vs. "create"'
source_url: https://github.com/monero-project/monero-gui/issues/1062
author: ordtrogen
assignees: []
labels: []
created_at: '2018-01-06T16:54:57+00:00'
updated_at: '2018-01-06T21:58:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm referring to the file with localizable strings, translations/monero_core.ts, as I haven't been able to run the GUI too much. (my screen is too small)

The GUI strings use the words 'generate' and 'create' inconsistently.

The command-line monero program uses 'generate' for generating wallets and stuff, but the GUI uses 'create' for the same thing. 

1. GUI should use same verb as CLI, i.e. 'Generate'  (I guess you could argue this point but the CLI has several flags, such as '--generate-new-wallet', so 'Generate' it should be for consistency (let's not mess with the flags))

It does use 'generate' in some cases, but GUI mostly uses 'create':
"Click Generate to create a random payment id for a new customer"  (even this sentence is inconsistent)
"Generate"
"Generate payment ID for integrated address"

These should be 'generate':
"Your computer will create hashes looking for block solutions.
"Create view only wallet
"Create a new wallet
"Create wallet
"The view only wallet has been created.

I think it's fine to use 'create' for transactions. 
"Can't create transaction: Wrong daemon version:"
"Can't create transaction:"

These string should still use 'create' (entry in address book, files and folders)
"Can't create entry"
"A new folder will be created."
"Create tx file"


# Discussion History
## ordtrogen | 2018-01-06T21:58:40+00:00
related to https://github.com/monero-project/monero/issues/3074


# Action History
- Created by: ordtrogen | 2018-01-06T16:54:57+00:00
