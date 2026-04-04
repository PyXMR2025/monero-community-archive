---
title: Taking too long to make a cold sign due to unsigned_monero_tx size is quite
  big if there are many history transfers
source_url: https://github.com/monero-project/monero/issues/3918
author: zhongqiuwood
assignees: []
labels: []
created_at: '2018-06-04T01:22:14+00:00'
updated_at: '2018-10-15T01:00:42+00:00'
type: issue
status: closed
closed_at: '2018-10-15T01:00:41+00:00'
---

# Original Description
The <wallet2::save_tx> method stores all history transfers into the unsigned_monero_tx file every time when run command [transfer] in a view-only wallet.
The way makes unsigned_monero_tx file too big to transfer in case of the account has  a tremendous amount of history transfers happend in past a couple of years.

The cli should provide user a way to specify a timestamps or a txid, before which the transfers will not be stored into unsigned_monero_tx file.

# Discussion History
## zhongqiuwood | 2018-09-11T08:49:18+00:00
Is there any plan to fix this issue?

## stoffu | 2018-10-14T10:05:22+00:00
> The wallet2::save_tx method stores all history transfers into the unsigned_monero_tx file every time when run command [transfer] in a view-only wallet.
The way makes unsigned_monero_tx file too big to transfer in case of the account has a tremendous amount of history transfers happend in past a couple of years.

This description is simply not true. As in wallet2.cpp,

```c++
bool wallet2::save_tx(const std::vector<pending_tx>& ptx_vector, const std::string &filename) const
{
  LOG_PRINT_L0("saving " << ptx_vector.size() << " transactions");
  std::string ciphertext = dump_tx_to_str(ptx_vector);
  if (ciphertext.empty())
    return false;
  return epee::file_io_utils::save_string_to_file(filename, ciphertext);
}
```

`save_tx` dumps the vector of `pending_tx` which is defined as

```c++
    struct pending_tx
    {
      cryptonote::transaction tx;
      uint64_t dust, fee;
      bool dust_added_to_fee;
      cryptonote::tx_destination_entry change_dts;
      std::vector<size_t> selected_transfers;
      std::string key_images;
      crypto::secret_key tx_key;
      std::vector<crypto::secret_key> additional_tx_keys;
      std::vector<cryptonote::tx_destination_entry> dests;
      std::vector<multisig_sig> multisig_sigs;
      tx_construction_data construction_data;
    };
```

I.e., the `unsigned_monero_tx` file stores information about only one transaction or multiple transactions in case of split txes each referring to only relevant data such as the global key indices for each ring signature and the destination addresses/amounts. The wallet's history of transactions in the past has nothing to do with it.


## zhongqiuwood | 2018-10-15T00:45:35+00:00
Thank you @stoffu!
You are correct. 
I revisited the code and found:
```
It was, before <wallet2::save_tx>, <wallet2::create_transactions_2> that goes through all m_transfers to find upspent. 
The unsigned_monero_tx file only stores relevant upspent transfers, not all history transfers.
```

Though traversing all m_transfers in wallet2::create_transactions_2 does not hurt performance that much, it would be better if upspent and spent transfers split from m_transfers.

# Action History
- Created by: zhongqiuwood | 2018-06-04T01:22:14+00:00
- Closed at: 2018-10-15T01:00:41+00:00
