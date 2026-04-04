---
title: No AltiVec/VMX hash function provided
source_url: https://github.com/monero-project/monero/issues/2489
author: madscientist159
assignees: []
labels:
- proposal
created_at: '2017-09-20T05:18:46+00:00'
updated_at: '2024-07-31T23:22:57+00:00'
type: issue
status: closed
closed_at: '2024-07-31T23:22:57+00:00'
---

# Original Description
ppc64el machines have an analogue to SSE known as AltiVec or more specifically VMX.  This includes AES instructions.

A ppc64el-optimized hash function should be provided, considering there is an optimized ARM hash function already in the tree alongside the x86 hash functions.

# Discussion History
## hyc | 2017-09-20T10:08:52+00:00
Nothing just gets "provided" out of thin air. You're welcome to submit a patch to add this code though.

## madscientist159 | 2017-09-20T16:08:42+00:00
I'm aware :smile:  Lodged the issue as a wishlist item that either I or someone else may get around to doing at some point.  Not expecting anything to magically appear out of thin air here.

## dEBRUYNE-1 | 2018-01-08T12:38:14+00:00
+proposal

## selsta | 2024-07-31T23:22:57+00:00
I will close this issue as it doesn't seem anyone is interested in implementing this. PRs are still welcome even after this is closed.

# Action History
- Created by: madscientist159 | 2017-09-20T05:18:46+00:00
- Closed at: 2024-07-31T23:22:57+00:00
