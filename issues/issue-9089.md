---
title: 'Bug: it''s theoretically possible (seems *very* unlikely) to be unable to
  restore a valid seed'
source_url: https://github.com/monero-project/monero/issues/9089
author: j-berman
assignees: []
labels:
- bug
- wallet
created_at: '2023-12-17T10:50:22+00:00'
updated_at: '2024-03-20T02:05:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### How to see the bug

Take the following valid Spanish seed as an example:

```
seed
pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma pluma

spend key
b4050000b4050000b4050000b4050000b4050000b4050000b4050000b4050000
```

It's theoretically possible (obviously extremely unlikely) for a wallet to generate the above seed.

When restoring this seed, it restores to the English seed:

```
seed
plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus plus

spend key
3b0400003b0400003b0400003b0400003b0400003b0400003b0400003b040000
```

### Why it happens

The wallet tries to infer what language the seed is in. It does this by checking the first X letters of each seed word against each language mnemonic dictionary. For English, only the first 3 letters of each seed word are checked. For Spanish, only the first 4 letters of each seed word are checked.

The first 3 letters of `pluma` -> `plu` is the same as `plus` -> `plu`.

The wallet checks if a seed is English before it checks if the seed is Spanish. When checking if the seed is English, the wallet trims each word to the first 3 letters `plu`, sees `plu` is in the trimmed English mnemonic dictionary, then calculates the seed's checksum using the trimmed words and sees the checksum is valid. The wallet then infers the seed's language is the first valid checksum. Thus, in this case, the checksum passes for English **before the wallet can even check if the checksum is valid in Spanish**, and so the wallet incorrectly thinks the seed is the English seed `plus plus ... plus`.

### Proposed solutions

#### Potentially disruptive but optimal solution

On restore, require the user specify the seed language along with the seed.

EDIT: I had previously proposed requiring the complete full seed (rather than trimmed), but as @iamamyth pointed out [below](https://github.com/monero-project/monero/issues/9089#issuecomment-1863266831), this would not solve the issue because there are duplicate full words across languages (e.g. `audio` in English and Spanish).

#### Less disruptive solution

Only require the language specification in the event a given seed has multiple valid checksums across different languages.

This means the edge case is applied to some already likely very niche users in exceptionally rare circumstances.

### Misc.

Related: 
#1579
https://github.com/serai-dex/serai/pull/490


# Discussion History
## iamamyth | 2023-12-17T18:10:23+00:00
You could also just score the language options based on similarity (exact match counts may suffice, though of course edit distances also work). So, for this example, even if a user typos pluma a few times, you'd compare ~20 "pluma" exact matches (score of 20) to ~0 "plus" exact matches and Spanish would win.

## iamamyth | 2023-12-17T18:15:55+00:00
To clarify: While I think the probability of a wrong inference can (probably should) be easily reduced without altering the existing UX (see prior suggestion), it also seems appropriate to let users select the language. Requiring an exact seed match seems unnecessary to fix the scenario outlined here, though would also mitigate other unlikely typo situations.

## kayabaNerve | 2023-12-18T04:13:42+00:00
I do not support fuzzy matching. Seeds should either have a valid result or be invalid. Probablistically selecting results, or yielding multiple results, will lead to unexpected/undesirable behavior.

The known solutions are:
1) Banning trimmed seeds (trimmed referring to partial words, not the whitespace cleanup)
2) Requiring the users select the language
3) Re-selecting the word lists

I most prefer 1. It doesn't complicate the UX. The migration path for anyone with a trimmed seed would simply be to manually re-expand it before typing it in.

## j-berman | 2023-12-18T18:57:34+00:00
> Probablistically selecting results, or yielding multiple results, will lead to unexpected/undesirable behavior.

I think this is a fair argument.

> 1. Banning trimmed seeds (trimmed referring to partial words, not the whitespace cleanup)
> 2. Requiring the users select the language

I figure requiring a user select a language when inputting a seed is a more significant UX change than requiring full words, since most people I'm guessing probably already use full words. As @iamamyth mentioned, supporting partial seed words also helps in the event someone misspells some words, though personally I think this can be smoothly and reasonably handled with error detection / word suggestion UX similar to Feather's.

Feather has both FWIW (both requires full words and also supports a language picker for the seed, though the bug is still present in Feather as well).

> 3. Re-selecting the word lists

We need a solution that would correctly restore existing seeds, like the `pluma` seed in the example above

## kayabaNerve | 2023-12-18T20:55:15+00:00
Agreed re-selection is infeasible.

## iamamyth | 2023-12-19T18:17:17+00:00
> supporting partial seed words also helps in the event someone misspells some words, though personally I think this can be smoothly and reasonably handled with error detection / word suggestion UX similar to Feather's

Seems like a question of separation of concerns. At the lowest layer, exact matching would be appropriate (though note that, if *any* two dictionaries overlap in a single word, that would imply you need to specify a language to disambiguate). At higher layers, word suggestion could rely on a very simple probabilitstic algorithm (e.g. on the 0th word, show suggestions ordered by a fixed language probability; on the Nth word, N > 0, order by `(exact match count, default language probability)`).


## kayabaNerve | 2023-12-19T19:26:09+00:00
If any two dictionaries share a word, then not allowing trimmed seeds means a seed may have multiple outcomes and forces language-based selection.

## j-berman | 2023-12-19T22:41:17+00:00
> (though note that, if any two dictionaries overlap in a single word, that would imply you need to specify a language to disambiguate)

Good spot here. I checked and there are a number of duplicate words across languages.

You are correct. This means users must specify a language, and requiring full words is not a solution. Trimmed words can still be allowed.

Looks like the optimal solution is therefore removing `find_seed_language` from the code which cannot yield a valid result in all cases, and requiring the seed language as an input parameter to the `words_to_bytes` functions (and to `WalletImpl::recover`).

I can submit a PR for the CLI, RPC, and GUI wallets. Unless I'm missing something above, this would be a breaking change for wallets using the wallet API in the ecosystem worth communicating as well.

## j-berman | 2023-12-20T00:49:41+00:00
Worth noting: there is an additional UX thorn with requiring specifying a language. There's both an English and EnglishOld, and there are duplicate words across both (e.g. `goodbye`). Users would therefore need to have the EnglishOld option available in addition to English, which is fairly confusing.

## iamamyth | 2023-12-20T01:53:01+00:00
> Users would therefore need to have the EnglishOld option available in addition to English, which is fairly confusing

Probably the easiest option would be to datestamp it (looks like that wordlist hasn't been available for many years, ~2014; someone could just figure out the exact year and the wallet could list it as, say, pre-2015, which most people would ignore).

## selsta | 2023-12-20T01:59:34+00:00
Is it worth it to make wallet restore more complicated to all users for a case that is more theoretical / extremely unlikely? Monero is already more complicated compared to other coins due to the restore height – adding another selection feels like going in the wrong direction :/

## kayabaNerve | 2023-12-20T02:31:36+00:00
English (pre-2015), English sound fine to me.

@selsta If this ever comes up IRL, users will be unable to restore their wallet and lose access to their funds. I don't believe specifying a language is a notable blocker. It's a single query which should have an obvious answer to any human.

Wallets can also try to abstract it, by decoding with all languages, and only asking the user if/when multiple valid options show up ("Is this seed Spanish or Italian?").

## j-berman | 2023-12-21T14:19:23+00:00
> Probably the easiest option would be to datestamp it

This is a good solution for EnglishOld.

> Wallets can also try to abstract it, by decoding with all languages, and only asking the user if/when multiple valid options show up ("Is this seed Spanish or Italian?").

I'll try this approach in GUI, CLI, RPC so it will only affect the UX for edge case seeds, unless there are objections/any more thoughts come along.

I generally agree there should be a solution in place in the rare event someone runs into the issue.

## BigslimVdub | 2024-03-20T02:05:36+00:00

> Wallets can also try to abstract it, by decoding with all languages, and only asking the user if/when multiple valid options show up ("Is this seed Spanish or Italian?").

this makes the most sense, if there are multiples then ask the user to clarify which language the seed is. If for some reason it doesn’t restore the correct wallet they can simply pick the next language asked

# Action History
- Created by: j-berman | 2023-12-17T10:50:22+00:00
