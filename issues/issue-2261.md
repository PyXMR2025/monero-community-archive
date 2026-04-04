---
title: Standardize and enforce the order of outputs
source_url: https://github.com/monero-project/monero/issues/2261
author: iamsmooth
assignees: []
labels:
- enhancement
created_at: '2017-08-07T19:47:35+00:00'
updated_at: '2018-01-04T11:18:40+00:00'
type: issue
status: closed
closed_at: '2017-09-25T18:42:23+00:00'
---

# Original Description
#2206 fixes an issue that outputs used to be sorted by amount, but this is either not possible or not desirable with ringct. The fix there randomizes the order, which solves the issue with the standard wallet, but similar bugs could still exist in other wallets. 

For example, MyMonero (which does not use much of the reference code base) at one time failed to sort the outputs by amount, which leaked information not only about the payments, but the wallet being used.

A better approach would be to sort by something public in the output, such as the output key, and enforce this in consensus (such enforcement would be efficient since it only requires comparing the outputs sequentially). This would prevent poorly-written wallets from leaking information.

# Discussion History
## moneromooo-monero | 2017-08-07T23:36:56+00:00
Good idea. I wanted to sort extra as well, as I think it might leak whether a tx was made with cold signing, etc.

## iamsmooth | 2017-08-08T00:21:22+00:00
While we are at it we can consider the order of the inputs as well. Same issue with poorly-written wallets doing something stupid, like putting the largest input first.

## dEBRUYNE-1 | 2017-08-25T15:54:00+00:00
+enhancement

## stoffu | 2017-08-29T11:14:22+00:00
How about lexicographically sorting 32-byte data of key images and destination pubkeys for inputs and outputs, respectively?

## moneromooo-monero | 2017-08-29T19:29:00+00:00
I think anything that is unambiguous and which can be checked without keys is fine.

## moneromooo-monero | 2017-09-12T20:44:09+00:00
https://github.com/monero-project/monero/pull/2440

## moneromooo-monero | 2017-09-25T18:41:17+00:00
+resolved

## stoffu | 2018-01-04T11:18:40+00:00
After #2440 and the subsequent revert of output sorting which was flawed, the original idea of output sorting proposed here is actually not implemented. So at least it seems inappropriate to me to mark this issue as "resolved" (since it's not solved).

A workable alternative I can think of is to sort the outputs according to the Pedersen Commitments. Do we still care to add it, or is this not really relevant?

# Action History
- Created by: iamsmooth | 2017-08-07T19:47:35+00:00
- Closed at: 2017-09-25T18:42:23+00:00
