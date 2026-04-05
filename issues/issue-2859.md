---
title: What algos are supported by xmrig?
source_url: https://github.com/xmrig/xmrig/issues/2859
author: PSLLSP
assignees: []
labels: []
created_at: '2022-01-11T00:10:21+00:00'
updated_at: '2022-01-18T18:32:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I cannot see `gr` algo (**ghostrider**) listed at page [https://xmrig.com/docs/algorithms](https://xmrig.com/docs/algorithms)

Is that page up to date? `xmrig -h` doesn't list algos those could be mined but it refers to page https://xmrig.com/docs/algorithms

# Discussion History
## Spudz76 | 2022-01-11T00:44:38+00:00
The current list is [within the source here](https://github.com/xmrig/xmrig/blob/master/src/base/crypto/Algorithm.h#L48)

Yes the web site is outdated.

There should be a way to list algorithms from command line, really.

## PSLLSP | 2022-01-12T23:35:04+00:00
I compared source code with web page and these algos are missing at web page [algorithms](https://xmrig.com/docs/algorithms):

* cn/dark
* cn/dark-lite
* cn/fast
* cn/lite
* cn/turtle
* cn/turtle-lite
* ghostrider
* rx/graft
* argon2/wrkz

On the other side, there is one more algorithm at web page that I failed to map to source code, `argon2/ninja`; it is different name for `argon2/wrkz` from the list above, it is documented here: [**Added argon2/ninja alias for argon2/wrkz algorithm.**](https://newreleases.io/project/github/xmrig/xmrig/release/v6.12.2)

## Spudz76 | 2022-01-13T01:29:55+00:00
Ghostrider uses several sub-algorithms which are the `*_GR_*` ones visible in the [initial Ghostrider commit](https://github.com/xmrig/xmrig/commit/ceaebfd87720d3079700cc243838c1c479b78276#diff-79e563220c3ffa21b1d35572d0d0245ecf13ade894590f18172d5cfadba5b1d6R68).  They are not otherwise separately accessible thus are not listed.  They only occur when using the encompassing algorithm, `ghostrider`.

Graft probably should be listed, it was added for the hardfork sep/2021, and has a coin entry.

The other couple argon2 variants, coins that used those have dwindled in popularity or hardforked since.  Something still uses `argon2/chukwav2` but I don't think the others are used anymore.

The accessible `cn-lite/1` is the only one of those available separately, although `cn-lite/0` might still operate there is nothing using it (and it's also nulled out of being configured in thread profiles).  The `cn/lite` is one of the ghostrider sub-algos which is different than the other two variants and not available separately (as an `--algo` or `--coin`).

The ones allowed as arguments and their names are in the companion to that header file, [src/base/crypto/Algorithm.cpp](https://github.com/xmrig/xmrig/blob/master/src/base/crypto/Algorithm.cpp).  Coin name mappings are over in [src/base/crypto/Coin.cpp](https://github.com/xmrig/xmrig/blob/master/src/base/crypto/Coin.cpp#L47) which simply apply the `Algorithm::` identifier from the left column for any of the strings listed (using `--coin` just sets the underlying `--algo`)

## dastardlyman12 | 2022-01-14T01:05:22+00:00
turtle uses argon2/chukwav2
yay turtle! you gotta love the little nibblers! i do and often mine them

## APT-ZERO | 2022-01-18T09:45:22+00:00
@Spudz76 
> The current list is [within the source here](https://github.com/xmrig/xmrig/blob/master/src/base/crypto/Algorithm.h#L48)
> 
> Yes the web site is outdated.
> 
> There should be a way to list algorithms from command line, really.

If you added list of algos supported as a parameter
it will be even better if you write L3 Cache and RAM needed for them in front of them

also a question, what is usage of --coin? what is benefits of specifying coin instead of algorithm

## Spudz76 | 2022-01-18T18:32:31+00:00
For lazy people who don't want to look up what algo their target coin uses.

# Action History
- Created by: PSLLSP | 2022-01-11T00:10:21+00:00
