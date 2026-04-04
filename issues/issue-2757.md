---
title: How to create checkpoint.dat self ?
source_url: https://github.com/monero-project/monero/issues/2757
author: ghost
assignees: []
labels:
- invalid
created_at: '2017-11-03T16:30:03+00:00'
updated_at: '2017-11-03T21:24:02+00:00'
type: issue
status: closed
closed_at: '2017-11-03T18:56:25+00:00'
---

# Original Description
How to create checkpoint.dat self ?

i meen this file https://github.com/monero-project/monero/blob/master/src/blocks/checkpoints.dat

I try to find at doc's how do this , but do not find any info.

# Discussion History
## moneromooo-monero | 2017-11-03T18:51:42+00:00
This is a bug tracker. Ask in #monero on Freenode, or reddit.

+invalid

## ghost | 2017-11-03T19:01:42+00:00
I understand :( I ask but no who not answer this , and i try find answer at here , sorry for my qustion. But if you can help please answer :( I try to find this 5 day's and no info.

## ghost | 2017-11-03T19:04:41+00:00
and if it not hard for you , how to calculate this value 
static const char expected_block_hashes_hash[] = "d3ca80d50661684cde0e715d46d7c19704d2e216b21ed088af9fd4ef37ed4d65";

## fluffypony | 2017-11-03T19:06:31+00:00
We don’t provide support for Monero forks.

## ghost | 2017-11-03T19:13:04+00:00
I ask about how do this , i not say anyting abou creating fork. Info how this templates value cannot find , and i ask about it , if it secret closed info ,say that and close sources. I whant undestand how it work for modify and add how to propose changes. But for do this i need first understand how it work. But info no exist. I am very sorry  for ask this , try somwhere  else ask. Again sorry

## fluffypony | 2017-11-03T19:14:17+00:00
It’s not a secret, it’s been discussed many times on IRC, and frankly it’s rather self-explanatory to any serious contributor.

## ghost | 2017-11-03T19:17:30+00:00
Ok i understand sorry for qustion at issure, i try ask it how say head dev at freenode. 
Tried to understand but did not understand, since before that he was digging in the source codes of classical coins, + This info not hv at classic cryptonote

## ghost | 2017-11-03T19:27:27+00:00
no who not answer at freenode , sorry for my qustion again . Try to find it self. At freenode i was ignored with this qustion.

## ghost | 2017-11-03T21:22:09+00:00
about  static const char expected_block_hashes_hash[] =  it's sha256 off checkpoint,dat ( siple can be findet with 7zip sha256 claculate

# Action History
- Created by: ghost | 2017-11-03T16:30:03+00:00
- Closed at: 2017-11-03T18:56:25+00:00
