---
title: 'Trezor: rephrase "Device wallet does not match wallet adress" error message'
source_url: https://github.com/monero-project/monero/issues/7783
author: ph4r05
assignees: []
labels: []
created_at: '2021-07-11T14:02:23+00:00'
updated_at: '2022-02-19T00:16:14+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:16:14+00:00'
---

# Original Description
Recently, few users reported problems with opening their Trezor-based Monero wallets:

- https://www.reddit.com/r/monerosupport/comments/ohfegp/help_cant_access_my_gui_wallet_trezor_model_t/h4q4z2b/
- more: https://github.com/trezor/trezor-firmware/issues/1686

Often happens that the culprit is usage of a different Trezor passphrase (or typo in the passphrase, capitalization, ...). Some users are not quite aware that different passphrase yields a different Monero address, which causes confusion (and support tickets). 

So it might be beneficial to rephrase error from [wallet2.cpp](https://github.com/monero-project/monero/blob/de3456e1275836725291ba71036b7ef0e2cda91f/src/wallet/wallet2.cpp) so it indicates there might be problem with a passphrase. https://github.com/monero-project/monero/blob/de3456e1275836725291ba71036b7ef0e2cda91f/src/wallet/wallet2.cpp#L4425-L4427

I am not sure what a rephrased error message should be and if it is the right place to address the passphrase problem, thus I am starting this issue to discuss. 

What do you think about:
```cpp
THROW_WALLET_EXCEPTION_IF(device_account_public_address != m_account.get_keys().m_account_address, error::wallet_internal_error, 
  "Device wallet address does not match wallet address. " 
  "Device address: " + cryptonote::get_account_address_as_str(m_nettype, false, device_account_public_address) + 
  ", wallet address: " + m_account.get_public_address_str(m_nettype) + 
  ". If device uses passphrase, please check it is correctly entered (case-sensitive, it might be misspelled, different passphrase generates different address)"); 
```

Feel free to suggest something better. 

What do you think @dEBRUYNE-1, @selsta ? Thanks!

# Discussion History
## dEBRUYNE-1 | 2021-07-13T21:08:58+00:00
Agree with the proposal in principle. With respect to the text, perhaps we can rename as follows:

> If the device uses the passphrase feature, please check whether the passphrase was entered correctly (it may have been misspelled - different passphrases generate different wallets)

# Action History
- Created by: ph4r05 | 2021-07-11T14:02:23+00:00
- Closed at: 2022-02-19T00:16:14+00:00
