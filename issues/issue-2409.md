---
title: 'Why ability to add custom remote node not working !!! '
source_url: https://github.com/monero-project/monero-gui/issues/2409
author: yakitorifoodie
assignees: []
labels: []
created_at: '2019-10-05T09:33:36+00:00'
updated_at: '2019-10-06T15:02:31+00:00'
type: issue
status: closed
closed_at: '2019-10-05T09:40:42+00:00'
---

# Original Description
While using remote node feature it automatically selects a remote node. Unable to provide my custome node.

after editing that remote node to my node it automatically switches to unknown remote node. not cool.

![imageedit_1_5754906903](https://user-images.githubusercontent.com/46250897/66252991-b381c580-e77f-11e9-8d0c-4305f90c6144.gif)

# Discussion History
## dEBRUYNE-1 | 2019-10-05T09:36:14+00:00
See the answer here:

https://monero.stackexchange.com/questions/11647/remote-node-ip-is-always-changing-in-monero-gui-wallet

## yakitorifoodie | 2019-10-05T09:40:42+00:00
Thanks. Enough. Its time to fire UX guy.

## erciccione | 2019-10-05T09:42:20+00:00
maybe it worth putting a warning on the remote node page about this. Or maybe make impossible to edit the details of the node in simple mode? not an optimal UX if people are able to change the settings, but these settings don't go live.

## yakitorifoodie | 2019-10-05T09:44:02+00:00
> make impossible to edit the details of the node

That would work.

## xiphon | 2019-10-05T10:30:02+00:00
Fixed via https://github.com/monero-project/monero-gui/pull/2373. No more Node settings tab in Simple Mode.

## selsta | 2019-10-06T14:59:15+00:00
> Thanks. Enough. Its time to fire UX guy.

It was a bug, not intentional UX design.

## yakitorifoodie | 2019-10-06T15:02:31+00:00
> It was a bug, not intentional UX design.

I'm sorry. Frustrated that time.

# Action History
- Created by: yakitorifoodie | 2019-10-05T09:33:36+00:00
- Closed at: 2019-10-05T09:40:42+00:00
