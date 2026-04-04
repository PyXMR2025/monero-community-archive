---
title: 'Inconsistent terminology: "key" (permutations of)'
source_url: https://github.com/monero-project/monero/issues/3067
author: ordtrogen
assignees: []
labels: []
created_at: '2018-01-04T21:19:14+00:00'
updated_at: '2018-01-07T01:23:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Looking at all occurrences of 'key' in translations/monero.ts, which I find confusing

"failed to parse secret spend key" - OK, I get that the key for spending should be kept secret
"No view key supplied, cancelled"  - Ok, maybe not 100% necessary to keep view key secret, depends on situation
"failed to parse secret view key"  - Wait, there is a "secret view key" as well? Is that the same as the above "view key" or different?
"wallet is watch-only and has no spend key" - I get it, but why sometimes use "secret spend key" and sometimes just "spend key"?
"Display private view key"         - Wait, now it's 'private' instead of 'secret'?
"Display private spend key"        -              idem.
"failed to parse view key secret key" - Say whaat? "view key secret key"?
"failed to parse spend key secret key"

My understanding is a wallet has a public address and two private (secret) keys, a spend key and a view key. The user should learn to protect these appropriately and the CLI needn't mention private/secret (or at least be consistent)


# Discussion History
## stoffu | 2018-01-04T23:21:17+00:00
The wallet address is a base58 encoding of a pair of spend public key and view public key. Spend secret key and view secret key are their secret counterparts. Terms like "view key" and "spend key" usually implicitly mean secret ones.

I agree that two terms "private" and "secret" being mixed can be confusing. I prefer the term "secret" since it matches the terminology in the implementation.

## hyc | 2018-01-06T06:10:24+00:00
But in cryptography these terms already have well defined meanings. The term "secret" key only applies to symmetric encryption mechanisms. For public key cryptography, "public" and "private" keypairs are the accepted terminology. We should be talking about public spend key and private spend key, public view key and private view key.

An example of "secret" key would apply to the passphrase which is used to encrypt the wallet cache file - this passphrase is used to derive a secret key.

We should definitely clean up and make our usage fully consistent, both internally consistent and with existing standard practice in cryptography.

## ordtrogen | 2018-01-06T21:33:57+00:00
I'd also prefer accepted terminology

Good you mentioned "spend public" and "spend secret" because I had just discovered those two terms being used in the GUI although I'm still confused by it. As a naïve user I thought you just used a spend key to spend money and a view key to let somebody view how much you have.

Nothing on getmonero.org on that topic (Ok,  now I found sth on Stackexchange). 

Still, monero src repo mentions neither "public spend key" nor "public view key"


## stoffu | 2018-01-07T01:14:48+00:00
Public spend and view keys are held by `account_public_address` struct: https://github.com/monero-project/monero/blob/master/src/cryptonote_basic/cryptonote_basic.h#L400

# Action History
- Created by: ordtrogen | 2018-01-04T21:19:14+00:00
