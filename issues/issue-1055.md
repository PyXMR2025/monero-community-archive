---
title: Sweep_all returns error "Duplicate indices though we did not ask for any"
source_url: https://github.com/monero-project/monero/issues/1055
author: iDunk5400
assignees: []
labels: []
created_at: '2016-09-05T22:31:28+00:00'
updated_at: '2018-08-20T20:24:53+00:00'
type: issue
status: closed
closed_at: '2016-10-04T22:33:51+00:00'
---

# Original Description
Running the command sweep_all in monero-wallet-cli afe3cce on Ubuntu 14.04 returns an error "Duplicate indices though we did not ask for any". Monero-wallet-cli does not crash from the error but keeps running normally.

Stack trace from the log:

```
2016-Sep-05 11:30:31.358702 ERROR /home/xxx/monero/src/wallet/wallet2.cpp:2826 std::get<0>(outs.back()[n]) == std::get<0>(outs.back()[n-1]). THROW EXCEPTION: error::wallet_internal_error
2016-Sep-05 11:30:31.358720 /home/xxx/monero/src/wallet/wallet2.cpp:2826:N5tools5error21wallet_internal_errorE: Duplicate indices though we did not ask for any
2016-Sep-05 11:30:31.358739 Exception: tools::error::wallet_internal_error
2016-Sep-05 11:30:31.358747 Unwinded call stack:
2016-Sep-05 11:30:31.392353      1                  0x6b15dc __cxa_throw + 0x7c
2016-Sep-05 11:30:31.453410      2                  0x58e10e void tools::wallet2::get_outs<std::tuple<unsigned long, crypto::public_key, rct::key> >(std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, std::list<__gnu_cxx::__normal_iterator<tools::wallet2::transfer_details*, std::vector<tools::wallet2::transfer_details, std::allocator<tools::wallet2::transfer_details> > >, std::allocator<__gnu_cxx::__normal_iterator<tools::wallet2::transfer_details*, std::vector<tools::wallet2::transfer_details, std::allocator<tools::wallet2::transfer_details> > > > > const&, unsigned long) [clone .lto_priv.1448] + 0x40b6
2016-Sep-05 11:30:31.454199      3                  0x6162b7 void tools::wallet2::transfer_selected<void (*)(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, cryptonote::tx_destination_entry const&, unsigned long, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >&, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >&)>(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, std::list<__gnu_cxx::__normal_iterator<tools::wallet2::transfer_details*, std::vector<tools::wallet2::transfer_details, std::allocator<tools::wallet2::transfer_details> > >, std::allocator<__gnu_cxx::__normal_iterator<tools::wallet2::transfer_details*, std::vector<tools::wallet2::transfer_details, std::allocator<tools::wallet2::transfer_details> > > > >, unsigned long, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> > const&, void (*)(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, cryptonote::tx_destination_entry const&, unsigned long, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >&, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >&), tools::tx_dust_policy const&, cryptonote::transaction&, tools::wallet2::pending_tx&) [clone .constprop.460] + 0x587
2016-Sep-05 11:30:31.454745      4                  0x56b0b9 tools::wallet2::create_transactions_all(cryptonote::account_public_address const&, unsigned long, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> >, bool) + 0x1969
2016-Sep-05 11:30:31.455474      5                  0x4ed832 cryptonote::simple_wallet::sweep_all(std::vector<std::string, std::allocator<std::string> > const&) + 0x292
2016-Sep-05 11:30:31.456067      6                  0x4cf4f5 epee::command_handler::process_command_str(std::string const&) + 0x3f5
2016-Sep-05 11:30:31.456623      7                  0x5251be cryptonote::simple_wallet::run() + 0xeee
2016-Sep-05 11:30:31.457168      8                  0x4a34b6 main + 0x2616
2016-Sep-05 11:30:31.457686      9                  0x7efc3f5ebf45 __libc_start_main + 0xf5
2016-Sep-05 11:30:31.458198     10                  0x4b53fc _start + 0x29
2016-Sep-05 11:30:31.458676     11                  0x0
2016-Sep-05 11:30:31.490852 ERROR /home/xxx/monero/src/simplewallet/simplewallet.cpp:2926 internal error: /home/xxx/monero/src/wallet/wallet2.cpp:2826:N5tools5error21wallet_internal_errorE: Duplicate indices though we did not ask for any
2016-Sep-05 11:30:31.490911 Error: internal error: Duplicate indices though we did not ask for any
```


# Discussion History
## moneromooo-monero | 2016-09-17T15:35:28+00:00
Fixed in latest git (though you'll now get "failed to find enough outs for that amount and mixin" instead, but there is sweep_unmixable for that).


## iDunk5400 | 2018-08-20T20:22:18+00:00
@moneromooo-monero 
Earth to moneromooo...
This seems to be the only way to contact you right now (possibly by anyone), so... yeah... regexps... take care of those, please :)
(unrelated to this closed issue, if that's not already obvious)

# Action History
- Created by: iDunk5400 | 2016-09-05T22:31:28+00:00
- Closed at: 2016-10-04T22:33:51+00:00
