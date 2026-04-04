---
title: Add release binaries for OpenBSD?
source_url: https://github.com/monero-project/monero/issues/3454
author: ston1th
assignees: []
labels: []
created_at: '2018-03-20T22:21:30+00:00'
updated_at: '2022-11-24T12:03:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
@fluffypony 

Would it be possible to add release binaries for OpenBSD like those for Free/DragonflyBSD?

# Discussion History
## ghost | 2018-05-01T21:01:06+00:00
I would love this as well

## offshoremonero | 2022-11-24T01:38:33+00:00
I would be willing to do this.

## selsta | 2022-11-24T02:51:55+00:00
@offshoremonero It would have to be added to the depends / gitian system: https://github.com/monero-project/monero/tree/master/contrib/depends https://github.com/monero-project/monero/tree/master/contrib/gitian

We cross compile all our release binaries and they have to be reproducible.

## offshoremonero | 2022-11-24T05:07:08+00:00
Hmm.. I think the compilers on OpenBSD are specifically designed to randomize code output? I could be wrong.

Maybe I should focus on having Monero added to OpenBSD's ports tree instead? Being able to "pkg_add monero-cli" would be handy for some users.

## selsta | 2022-11-24T12:03:43+00:00
> Maybe I should focus on having Monero added to OpenBSD's ports tree instead?

That will likely be easier.

# Action History
- Created by: ston1th | 2018-03-20T22:21:30+00:00
