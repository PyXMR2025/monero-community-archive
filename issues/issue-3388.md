---
title: Import and export outputs
source_url: https://github.com/monero-project/monero-gui/issues/3388
author: jluttine
assignees: []
labels: []
created_at: '2021-04-11T16:48:36+00:00'
updated_at: '2021-04-21T02:27:38+00:00'
type: issue
status: closed
closed_at: '2021-04-21T02:27:38+00:00'
---

# Original Description
Monero GUI "Send" tab gives the following instructions:

> Offline transaction signing:
>
> 1. Using view-only wallet, export the outputs into a file
> 2. Using cold wallet, import the outputs file and export the key images
> 3. ...
> 4. ...
> 5. ...

However, the GUI doesn't provide buttons to export and import the outputs. It would be nice to have such buttons available so that offline transaction signing could be done with the GUI wallet without needing to use the CLI wallet. Especially, as the GUI wallet gives the instructions, it seems weird that it cannot be done.

Or is this already possible but I just cannot find it?

# Discussion History
## selsta | 2021-04-21T02:27:38+00:00
Closing as a duplicate of #2816.

Will try to add support for this in the next weeks.

# Action History
- Created by: jluttine | 2021-04-11T16:48:36+00:00
- Closed at: 2021-04-21T02:27:38+00:00
