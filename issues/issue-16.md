---
title: deprecate the use of global output index
source_url: https://github.com/Cuprate/cuprate/issues/16
author: SyntheticBird45
assignees: []
labels:
- A-storage
- C-discussion
created_at: '2023-04-11T19:46:38+00:00'
updated_at: '2024-05-27T00:59:07+00:00'
type: issue
status: closed
closed_at: '2023-04-13T19:27:48+00:00'
---

# Original Description
The global output index (or Output ID) isn't mandatory for cryptonote and is just a subkey used to keep track of the number of output. Here's the function used by monerod that requires output ID :
```cpp
uint64_t BlockchainLMDB::num_outputs() const
{
  LOG_PRINT_L3("BlockchainLMDB::" << __func__);
  check_open();
  TXN_PREFIX_RDONLY();
  int result;

  RCURSOR(output_txs)

  uint64_t num = 0;
  MDB_val k, v;
  result = mdb_cursor_get(m_cur_output_txs, &k, &v, MDB_LAST);
  if (result == MDB_NOTFOUND)
    num = 0;
  else if (result == 0)
    num = 1 + ((const outtx*)v.mv_data)->output_id;
  else
    throw0(DB_ERROR(lmdb_error("Failed to query m_output_txs: ", result).c_str()));

  return num;
}
```
Since pre-rct outputs are a constant, we can replace the use of output ID by the entries method of a table :
https://docs.rs/libmdbx/latest/libmdbx/struct.Stat.html#method.entries
we then substract with the number of pre-rct output to get the result.

Then two choices can be made either we stay with two outputs table with the same amount/Key index/SubKey or we merge these two tables together. 


# Discussion History
## SyntheticBird45 | 2023-04-13T19:27:48+00:00
pre-rct output and rct output have been splited. see : https://github.com/Cuprate/cuprate/commit/fd9c095d664779a89918b9f5d4687c226685fc42

# Action History
- Created by: SyntheticBird45 | 2023-04-11T19:46:38+00:00
- Closed at: 2023-04-13T19:27:48+00:00
