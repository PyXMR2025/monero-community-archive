---
title: Code Style - Line Width Limit
source_url: https://github.com/monero-project/monero/issues/2982
author: ilprincipe33
assignees: []
labels:
- invalid
created_at: '2017-12-21T04:03:38+00:00'
updated_at: '2017-12-25T22:52:45+00:00'
type: issue
status: closed
closed_at: '2017-12-25T18:00:26+00:00'
---

# Original Description
Please consider formatting all sources by placing a strict column limit to (say) 80 columns to improve readability and maintainability. 

Some source files are extremely difficult to read to the point where I had to use [Clang Format](https://clang.llvm.org/docs/ClangFormat.html) before I could actually start reading the code...

Here is an example of a function that that is currently displayed as a single statement spanning 176 columns:

```C++
bool construct_tx_with_tx_key(const account_keys& sender_account_keys, const std::unordered_map<crypto::public_key, subaddress_index>& subaddresses, std::vector<tx_source_entry>& sources, const std::vector<tx_destination_entry>& destinations, const boost::optional<cryptonote::account_public_address>& change_addr, std::vector<uint8_t> extra, transaction& tx, uint64_t unlock_time, const crypto::secret_key &tx_key, const std::vector<crypto::secret_key> &additional_tx_keys, bool rct, bool bulletproof, rct::multisig_out *msout)
```

[Source](https://github.com/monero-project/monero/blob/master/src/cryptonote_core/cryptonote_tx_utils.cpp#L191)

Here is an example of aforementioned function styled with clang-format using [Mozilla code style](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Coding_Style) conventions:

```C++
bool
construct_tx_with_tx_key(
  const account_keys& sender_account_keys,
  const std::unordered_map<crypto::public_key, subaddress_index>& subaddresses,
  std::vector<tx_source_entry>& sources,
  const std::vector<tx_destination_entry>& destinations,
  const boost::optional<cryptonote::account_public_address>& change_addr,
  std::vector<uint8_t> extra, transaction& tx, uint64_t unlock_time,
  const crypto::secret_key& tx_key,
  const std::vector<crypto::secret_key>& additional_tx_keys, bool rct,
  bool bulletproof, rct::multisig_out* msout)
```

Hope this helps. GLHF. 

# Discussion History
## ilprincipe33 | 2017-12-21T04:27:08+00:00
Another thing: in C++ source files function definitions are being preceded by a comment line composed of hyphens that look like this: 

```C++
//--------------------------------------------------------------------------------------
std::whatever_t core::my_method() const 
{
/* do whatever ... */
}
```
Presumably, these markers are being interpreted to facilitate code-folding specific to some editor(s). Whatever the case, this is just more cruft that makes code harder to read and should be removed. 

## jasjuang | 2017-12-21T06:55:59+00:00
+1 for clang-format, strict 80 column limit is needed

## moneromooo-monero | 2017-12-21T09:23:04+00:00
NAK, no reformatting. If you're adding new code, you're free to keep to 80 columns, though.

## moneromooo-monero | 2017-12-25T17:49:10+00:00
+invalid

## jasjuang | 2017-12-25T18:01:19+00:00
@moneromooo-monero That's unfortunate. I was thinking about contributing to monero on my free time (I am sure @ilprincipe33 is too, that's why we are here), but the current no-coding-style is making the friction to contribute unnecessarily high. 

## fluffypony | 2017-12-25T18:13:46+00:00
@jasjuang then create an issue about establishing a coding style, and submit a PR after discussion in that issue. @moneromooo-monero is *only* saying that refactor-as-you-go is acceptable, but necessary refactoring is not.

## stoffu | 2017-12-25T22:52:45+00:00
As someone who's been working on Monero for a little over a year, I'd say the codebase may look a bit overwhelming and intimidating at first sight, but it'll become quite manageable as you get used to it. Monero developers should have at least this level of patience and perseverance, IMO.


# Action History
- Created by: ilprincipe33 | 2017-12-21T04:03:38+00:00
- Closed at: 2017-12-25T18:00:26+00:00
