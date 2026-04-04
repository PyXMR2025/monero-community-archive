---
title: Looking For Commit / Merge On Changes From v7 to v8
source_url: https://github.com/monero-project/monero/issues/5110
author: virtopiarvn
assignees: []
labels: []
created_at: '2019-01-30T20:03:08+00:00'
updated_at: '2019-01-31T15:03:33+00:00'
type: issue
status: closed
closed_at: '2019-01-31T15:03:33+00:00'
---

# Original Description
I am trying to figure out how to see a commit or merge that includes all changes from v7 to v8 (algorithm), similar to:
https://github.com/monero-project/monero/commit/608fd6f14a6b9c0eeba2843fb14cbb235be0034f#diff-47106096e4b0462d3324778bf55410e4

I cannot find it or see how to do it, using compare does not quite get me what I need. Any tips, pointer, gentle kick in the right direction appreciated.

# Discussion History
## moneromooo-monero | 2019-01-30T23:13:36+00:00
Each version has a tag: vX.Y.Z.W

Show all known tags: git tag

Show commits between two tags: git checkout TAG2; git cherry TAG1

Show diffs between two tags: git diff TAG1 TAG2


## virtopiarvn | 2019-01-31T00:22:15+00:00
Thanks for that. Yes I think this is = to what I did here:
https://github.com/monero-project/monero/compare

I am looking for changes only to the algorithm from v7 to v8, is there a way to pull that?

## fluffypony | 2019-01-31T00:28:41+00:00
@virtopiarvn what is “the algorithm”?

## virtopiarvn | 2019-01-31T00:29:12+00:00
Sorry, Cryptonight @fluffypony 

## Gingeropolous | 2019-01-31T03:51:28+00:00
@virtopiarvn , i don't know if it will help, but the "v7 to v8 " nomenclature for the PoW is wrong. It is technically CNv1 and CNv2, respectively. ...

though some among us think we are currently on CNv3 because there were 2 forks that happened within a day of each other ... but the PoW didn't change during those forks, so there is no variation between them, but .... yah know. Tomato tomato. 

but I think I found the commit 

https://github.com/monero-project/monero/commit/f3cd51a12b202875bd8191668aceb8a4f810ecd4

## virtopiarvn | 2019-01-31T15:03:33+00:00
@Gingeropolous Thanks for this, I saw it while browsing through things but was not sure it was what I was looking for. Also thanks for the clarification on naming, much appreciated!

# Action History
- Created by: virtopiarvn | 2019-01-30T20:03:08+00:00
- Closed at: 2019-01-31T15:03:33+00:00
