---
title: ' iOS sync blocks performance issues'
source_url: https://github.com/monero-project/monero/issues/6573
author: WooKeyWallet
assignees: []
labels: []
created_at: '2020-05-20T09:34:34+00:00'
updated_at: '2020-05-24T14:32:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
We found that in release-0.15 version, iOS performance is obviously not as good as Android. We compared Monroe wallets including self-developed and cakewallet.

I tracked the running status of the app, the screenshot is as follows:

![image](https://user-images.githubusercontent.com/46467247/82429788-087c0d00-9abf-11ea-93e9-f1ebd66b6b08.png)

![image](https://user-images.githubusercontent.com/46467247/82429803-0d40c100-9abf-11ea-985e-e281672ed8e0.png)

When 100% of the CPU occurs, I check the threads and find that there are two Monero wallet threads that are very time-consuming and occupy CPU when parsing the block. The call stack is displayed as follows:

```
#0	0x00000001016c3b84 in fe_sq at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/crypto/crypto-ops.c:675
#1	0x00000001016c3968 in fe_invert at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/crypto/crypto-ops.c:295
#2	0x00000001016c8d24 in ge_tobytes at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/crypto/crypto-ops.c:1659
#3	0x00000001016d61ac in crypto::crypto_ops::derive_subaddress_public_key(crypto::public_key const&, crypto::key_derivation const&, unsigned long, crypto::public_key&) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/crypto/crypto.cpp:254
#4	0x0000000100f75d64 in crypto::derive_subaddress_public_key(crypto::public_key const&, crypto::key_derivation const&, unsigned long, crypto::public_key&) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/crypto/crypto.h:232
#5	0x00000001016ff2dc in hw::core::device_default::derive_subaddress_public_key(crypto::public_key const&, crypto::key_derivation const&, unsigned long, crypto::public_key&) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/device/device_default.cpp:125
#6	0x000000010158b47c in cryptonote::is_out_to_acc_precomp(std::__1::unordered_map<crypto::public_key, cryptonote::subaddress_index, std::__1::hash<crypto::public_key>, std::__1::equal_to<crypto::public_key>, std::__1::allocator<std::__1::pair<crypto::public_key const, cryptonote::subaddress_index> > > const&, crypto::public_key const&, crypto::key_derivation const&, std::__1::vector<crypto::key_derivation, std::__1::allocator<crypto::key_derivation> > const&, unsigned long, hw::device&) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/cryptonote_basic/cryptonote_format_utils.cpp:904
#7	0x00000001010bfe50 in tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*)::$_40::operator()(cryptonote::transaction const&, unsigned long, unsigned long) const at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/wallet/wallet2.cpp:2658
#8	0x00000001010c239c in tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*)::$_6::operator()() const at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/wallet/wallet2.cpp:2684
#9	0x00000001010c22e8 in decltype(std::__1::forward<tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*)::$_6&>(fp)()) std::__1::__invoke<tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*)::$_6&>(tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*)::$_6&) at /Applications/Xcode10.3.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/type_traits:4339
#10	0x00000001010c229c in void std::__1::__invoke_void_return_wrapper<void>::__call<tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*)::$_6&>(tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*)::$_6&) at /Applications/Xcode10.3.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/__functional_base:349
#11	0x00000001010c0e7c in std::__1::__function::__func<tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*)::$_6, std::__1::allocator<tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*)::$_6>, void ()>::operator()() at /Applications/Xcode10.3.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/functional:1562
#12	0x00000001016af220 in std::__1::function<void ()>::operator()() const at /Applications/Xcode10.3.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/functional:1913
#13	0x00000001016ae6e4 in tools::threadpool::run(bool) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/common/threadpool.cpp:153
#14	0x00000001016af834 in tools::threadpool::waiter::wait(tools::threadpool*) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/common/threadpool.cpp:117
#15	0x0000000100ec30f8 in tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/wallet/wallet2.cpp:2689
#16	0x0000000100ec6264 in tools::wallet2::refresh(bool, unsigned long long, unsigned long long&, bool&, bool) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/wallet/wallet2.cpp:3311
#17	0x0000000100ec56fc in tools::wallet2::refresh(bool, unsigned long long, unsigned long long&) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/wallet/wallet2.cpp:2732
#18	0x0000000100ec566c in tools::wallet2::refresh(bool) at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/wallet/wallet2.cpp:2726
#19	0x0000000100cb58d0 in Monero::WalletImpl::doRefresh() at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/wallet/api/wallet.cpp:2137
#20	0x0000000100cc2378 in Monero::WalletImpl::refreshThreadFunc() at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/wallet/api/wallet.cpp:2119
#21	0x0000000100cf605c in Monero::WalletImpl::WalletImpl(Monero::NetworkType, unsigned long long)::$_0::operator()() const at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/monero/src/wallet/api/wallet.cpp:443
#22	0x0000000100cf5464 in boost::detail::thread_data<Monero::WalletImpl::WalletImpl(Monero::NetworkType, unsigned long long)::$_0>::run() at /Users/jowsing/Desktop/WooKey_GitHub/monero-ios-lib/SharedExternal/ofxiOSBoost/build/ios/prefix/include/boost/thread/detail/thread.hpp:116
#23	0x00000001017ecc58 in boost::(anonymous namespace)::thread_proxy(void*) at /Users/luzhentian/Desktop/CakeWallet/SharedExternal/ofxiOSBoost/build/src/boost_1_60_0/libs/thread/src/pthread/thread.cpp:167
#24	0x000000018432431c in _pthread_body ()
#26	0x0000000184322c28 in thread_start ()

```

# Discussion History
## SomaticFanatic | 2020-05-22T02:13:24+00:00
Not sure if this is related but my OSX laptop’s SSD took over two days to sync from scratch (using 0.16) which seemed unreasonably long to me

## selsta | 2020-05-22T02:25:43+00:00
@SomaticFanatic Did you self compile v0.16 from master branch? I tested v0.16 and was able to sync up in 2:40 on a 30€/month VPS.

## SomaticFanatic | 2020-05-22T15:21:46+00:00
@selsta was your VPS OSX? That’s more the issue I’m focused on. My Linux box synced fine

## selsta | 2020-05-22T15:23:20+00:00
Which is the exact commit you compiled?

I also own a 2014 MacBook and can test later.

## SomaticFanatic | 2020-05-22T15:53:23+00:00
Cloned master and compiled. Last master commit was 15 days ago. 

https://github.com/monero-project/monero/commit/70609d76814bfd1dcabb813d45bbd367597aaa95

## selsta | 2020-05-22T15:55:31+00:00
master does not contain the updated fast sync checkpoints yet. Try again with `release-v0.16` branch or `v0.16.0.0` tag.

## moneromooo-monero | 2020-05-22T22:14:06+00:00
Those don't impact wallet sync speed though.

## WooKeyWallet | 2020-05-24T14:32:13+00:00
> Those don't impact wallet sync speed though.

I have found that time-consuming method：
```
bool crypto_ops::derive_subaddress_public_key(const public_key &out_key, const key_derivation &derivation, std::size_t output_index, public_key &derived_key) {
    ec_scalar scalar;
    ge_p3 point1;
    ge_p3 point2;
    ge_cached point3;
    ge_p1p1 point4;
    ge_p2 point5;
    if (ge_frombytes_vartime(&point1, &out_key) != 0) {
      return false;
    }
    derivation_to_scalar(derivation, output_index, scalar);
    ge_scalarmult_base(&point2, &scalar);
    ge_p3_to_cached(&point3, &point2);
    ge_sub(&point4, &point1, &point3);
    ge_p1p1_to_p2(&point5, &point4);
    ge_tobytes(&derived_key, &point5);
    return true;
  }
```

# Action History
- Created by: WooKeyWallet | 2020-05-20T09:34:34+00:00
