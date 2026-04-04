---
title: Inconsistent balance of xmr
source_url: https://github.com/monero-project/monero-gui/issues/4449
author: PyXMR2025
assignees: []
labels: []
created_at: '2025-05-17T16:28:36+00:00'
updated_at: '2025-05-17T17:20:47+00:00'
type: issue
status: closed
closed_at: '2025-05-17T17:20:47+00:00'
---

# Original Description
Inconsistent balance of xmr
Write

![Image](https://github.com/user-attachments/assets/77458049-e014-467a-b3cc-7eaf97d9c820)

only read

![Image](https://github.com/user-attachments/assets/fb29a8e9-760b-452b-9d46-cb23fb02a522)

# Discussion History
## PyXMR2025 | 2025-05-17T16:29:24+00:00
@luigi1111 @plowsof @selsta emergency

## selsta | 2025-05-17T16:32:14+00:00
Can you explain how you got these two states? What do you mean with write / only read?

## PyXMR2025 | 2025-05-17T16:34:04+00:00
I opened both the read-only wallet and the writable wallet at the same time，Towards 44 spvcQDRui8vamGFjSvLhcjC3CFVcdsa2zHA2yApRcBWicSYKJJgLoHyXrC7aK7rBYEc6RyG3TsS7RS9dXkVupMR2fEfB1 Transferred

## PyXMR2025 | 2025-05-17T16:36:43+00:00
![Image](https://github.com/user-attachments/assets/0c246ebe-e4a9-43be-8e82-cb8b0029ef92)

![Image](https://github.com/user-attachments/assets/bff39b1b-688a-4ece-8533-7079192272e4)

## PyXMR2025 | 2025-05-17T16:38:26+00:00
![Image](https://github.com/user-attachments/assets/47982e57-b813-4e22-9531-04da760d7d2c)


## nahuhh | 2025-05-17T16:38:45+00:00
The "read" (view) wallet has no knowledge of outgoing transactions, and counts "change" outputs towards the total balance. As a result, the view wallet will show a higher balance than the "write" (spend) wallet

## PyXMR2025 | 2025-05-17T16:39:36+00:00
Yes

## PyXMR2025 | 2025-05-17T16:41:09+00:00
The main issue is that when I resynchronized the writable wallet, the result was like this

![Image](https://github.com/user-attachments/assets/51a78eb3-315b-43b6-878a-e0485c5d3d32)

![Image](https://github.com/user-attachments/assets/82f0fc38-40d0-48eb-bca4-987ada0f285e)

![Image](https://github.com/user-attachments/assets/5d092e10-23f1-46ea-88f4-1970df39afce)

## nahuhh | 2025-05-17T16:46:07+00:00
You have to set the "restore height" to before 2025-05-11

## PyXMR2025 | 2025-05-17T16:47:18+00:00
I try it

## PyXMR2025 | 2025-05-17T16:50:24+00:00
But the height of the read-only wallet is correct

## PyXMR2025 | 2025-05-17T16:53:03+00:00
![Image](https://github.com/user-attachments/assets/9dcf9072-a970-4e24-a65a-0b3561d9c8eb)

## PyXMR2025 | 2025-05-17T16:53:52+00:00
More and more

## PyXMR2025 | 2025-05-17T17:17:45+00:00
Good news: there are no more issues.
Thank you!

## PyXMR2025 | 2025-05-17T17:18:53+00:00
However, it seems that MoneroWall has not received it

![Image](https://github.com/user-attachments/assets/1dc9003d-b3e9-4f78-a362-95e3cf0aec8b)

![Image](https://github.com/user-attachments/assets/ac61e723-abff-4589-ab6d-dcc01efd4eb0)

# Action History
- Created by: PyXMR2025 | 2025-05-17T16:28:36+00:00
- Closed at: 2025-05-17T17:20:47+00:00
