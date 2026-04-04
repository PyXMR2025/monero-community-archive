---
title: Remove benchmarks run from buildbot
source_url: https://github.com/monero-project/meta/issues/54
author: anonimal
assignees: []
labels: []
created_at: '2017-03-12T00:28:14+00:00'
updated_at: '2017-03-16T17:19:19+00:00'
type: issue
status: closed
closed_at: '2017-03-16T17:19:19+00:00'
---

# Original Description
We'll very soon have benchmarks running within the utility binary. This means no more `kovri-benchmarks`. I personally don't have a need to run benchmarks on every build either (but that's just me) so if we remove them all-together from the build then I'm fine with that. Otherwise we'll have to run them from `kovri-util`.

# Discussion History
## danrmiller | 2017-03-13T17:33:50+00:00
>  Otherwise we'll have to run them from kovri-util.

What is the syntax to run the benchmarks with kovri-util?

## anonimal | 2017-03-13T21:03:46+00:00
Currently `./kovri-util benchmark -t`

I'll ask @guzzijones to reconsider the switch or drop it completely because it currently isn't needed.

## guzzijones | 2017-03-14T00:18:05+00:00
syntax is 
`kovri-util benchmark -a`

## guzzijones | 2017-03-14T00:19:28+00:00
I can set -a as a default value and commit again.

## anonimal | 2017-03-16T17:19:19+00:00
Done. Thanks @danrmiller.

# Action History
- Created by: anonimal | 2017-03-12T00:28:14+00:00
- Closed at: 2017-03-16T17:19:19+00:00
