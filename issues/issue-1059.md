---
title: Cannot no longer build using brew on OS X
source_url: https://github.com/monero-project/monero/issues/1059
author: peanutsformonkeys
assignees: []
labels: []
created_at: '2016-09-07T19:24:49+00:00'
updated_at: '2016-09-18T11:41:54+00:00'
type: issue
status: closed
closed_at: '2016-09-18T11:41:54+00:00'
---

# Original Description
The instructions in README.md to build Monero using brew for OS X no longer seem to work:

```
brew tap sammy007/cryptonight
…
brew install bitmonero --build-from-source
Error: No available formula with the name "bitmonero" 
==> Searching for similarly named formulae...
Error: No similarly named formulae found.
==> Searching taps...
Error: No formulae found in taps.

```

Is this due to the recent GitHub repository name change? I am very new to all this, it's the only thing I can think of. This worked fine on another Mac about 1 or 2 weeks ago, same OS X version, same setup.


# Discussion History
## bigreddmachine | 2016-09-14T19:46:14+00:00
The homebrew formula was changed to reflect the name change of the repo from bitmonero to monero.

Fixed in PR #1072.


## ghost | 2016-09-15T15:04:04+00:00
Hi @peanutsformonkeys is this still an issue for you or can it be closed?


## peanutsformonkeys | 2016-09-16T19:26:53+00:00
I just did some tests here. I confirm I can do `brew install monero --build-from-source`. But with `brew install monero --HEAD -v` it fails at the end now:

> [ 98%] Built target simplewallet
> [100%] Linking CXX executable ../../bin/monerod
> [100%] Built target daemon
> Error: No such file or directory - ./build/release/bin/bitmonerod

No idea if that has another cause or not …


## ghost | 2016-09-17T21:21:00+00:00
Ah...see this http://apple.stackexchange.com/questions/78984/what-does-brew-head-mean

To quote:

> In git using the --HEAD will grab all of the latest commits from the source repo. The problem with this is sometimes the latest revision will be in an inconsistant or unbuildable state, so use at your own risk.
> 
> When you sync from other tags that are published as "known stable" releases then the developer is saying that the files as they existed at that point will build and has passed all if its tests.
> 
> Running from head can be risky.

So unless you have a strong reason for building from `--HEAD`, I wouldn't do it ;)


## peanutsformonkeys | 2016-09-18T11:41:54+00:00
Thanks for clarifying about `--HEAD`. Going to close the issue because `--build-from-source` works.


# Action History
- Created by: peanutsformonkeys | 2016-09-07T19:24:49+00:00
- Closed at: 2016-09-18T11:41:54+00:00
