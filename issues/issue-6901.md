---
title: Unsigned transactions generated on macOS cannot be signed on Linux
source_url: https://github.com/monero-project/monero/issues/6901
author: leevlad
assignees: []
labels: []
created_at: '2020-10-16T15:08:37+00:00'
updated_at: '2021-10-06T02:38:20+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:38:20+00:00'
---

# Original Description
- `macOS` version: `10.15.7`
- `Linux` version: `Ubuntu 18.04`
- `monerod` version: `0.17.1.0` obtained from the official downloads page
- `monero-wallet-rpc` version: `0.17.1.0` obtained from the official downloads page
- `network`: `mainnet`

### Steps to reproduce:

1. Generate a transaction on macOS using `monero-wallet-rpc` by calling the `transfer` JSON-RPC method.
2. Pass the `unsigned_txset` string to a `monero-wallet-rpc` instance running on Linux using the `sign_transfer` JSON-RPC method.

### Error:
```
{
  "error": {
    "code": -39,
    "message": "cannot load unsigned_txset"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

### Additional notes:
I did verify that the `unsigned_txset` in my test case is indeed of the `version == '\005'` format.

Passing the `unsigned_txset` string to a `monero-wallet-rpc` instance running on macOS does not produce an error and creates a signed transaction correctly.

Looking through the source code it appears to be a problem with the new serialization format introduced in the following PR: 
https://github.com/monero-project/monero/pull/6690

Specifically, the following `serialize` call fails: 
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L6710

# Discussion History
## moneromooo-monero | 2020-10-16T15:27:31+00:00
Can you repro this on testnet for a wallet you could give me both the seed for and the file generated on mac ?

## leevlad | 2020-10-16T15:46:34+00:00
I'm not currently running any nodes or wallets on the testnet, but can look into it when I have time. Alternatively I can share my mainnet wallet's `view_secret_key` and the `unsigned_txset` hex string that's failing, so you might be able to write a test harness with those values that would just replicate the code here:

https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L6710

## moneromooo-monero | 2020-10-16T16:02:38+00:00
I think that'd be sufficient, yes.

## moneromooo-monero | 2020-10-16T16:03:06+00:00
My GPG key's in the monero tree if you don't want that secret view key public.

## leevlad | 2020-10-16T18:52:15+00:00
No worries, this is a transient wallet that I created for testing this issue, of no monetary/privacy consequence whatsoever. Plus it will allow other people to work on it. You can find both in the gist below:
https://gist.github.com/leevlad/2f569e971646cdfc1108c0ffd919221e


## moneromooo-monero | 2020-10-17T21:38:51+00:00
If it has no privacy consequence... is the change supposed to be  0.048983820000 to 42wqzvHUsEv9aX9PTXy2UM6vbaABdra7sHcGvpaL3nxPBDitduMxYgLWxiXv3ph3SN2hBCx8DuK4T4Rs3JdcpjZHUbzJN6H ? I'm trying to find out where it starts going wonky.

## leevlad | 2020-10-17T21:46:29+00:00
That address is where I'd expect the change to go. The wallet balance before the transfer should be 0.05 XMR, sent amount was for 0.001 XMR + network fees. So that looks about right to me.

Another thing that might help narrow it down is that I found that when I exported outputs from a macOS machine using the `export_outputs` call, and then imported them on a Linux machine using the `import_outputs` call of `monero-wallet-rpc` - I did not run into any issues.

## moneromooo-monero | 2020-10-17T23:17:56+00:00
Does this fix it (apply on the mac version) ?

```
diff --git a/src/cryptonote_core/cryptonote_tx_utils.h b/src/cryptonote_core/cryptonote_tx_utils.h
index dbdf409b5..a6c71d3b1 100644
--- a/src/cryptonote_core/cryptonote_tx_utils.h
+++ b/src/cryptonote_core/cryptonote_tx_utils.h
@@ -102,8 +102,8 @@ namespace cryptonote
       FIELD(original)
       VARINT_FIELD(amount)
       FIELD(addr)
-      FIELD(is_subaddress)
-      FIELD(is_integrated)
+      VARINT_FIELD(is_subaddress)
+      VARINT_FIELD(is_integrated)
     END_SERIALIZE()
   };
 
```

## moneromooo-monero | 2020-10-17T23:25:55+00:00
(if not, please send me the new unsigned tx data)

## leevlad | 2020-10-17T23:31:50+00:00
Thanks for looking into it so soon.

I'm not going to be able to get this tested on my Mac as I can't compile monero on the latest version Catalina on `clang v12.0.0`, but I do see that this issue has recently been solved (per https://github.com/monero-project/monero/issues/6799).

I'll give this a go later this week and report back.

## selsta | 2020-10-17T23:33:13+00:00
@leevlad normal `make release` should work fine on Mac. (I’m on Catalina too)

## leevlad | 2020-10-18T02:56:34+00:00
> Does this fix it (apply on the mac version) ?
> 
> ```
> diff --git a/src/cryptonote_core/cryptonote_tx_utils.h b/src/cryptonote_core/cryptonote_tx_utils.h
> index dbdf409b5..a6c71d3b1 100644
> --- a/src/cryptonote_core/cryptonote_tx_utils.h
> +++ b/src/cryptonote_core/cryptonote_tx_utils.h
> @@ -102,8 +102,8 @@ namespace cryptonote
>        FIELD(original)
>        VARINT_FIELD(amount)
>        FIELD(addr)
> -      FIELD(is_subaddress)
> -      FIELD(is_integrated)
> +      VARINT_FIELD(is_subaddress)
> +      VARINT_FIELD(is_integrated)
>      END_SERIALIZE()
>    };
>  
> ```

This doesn't seem to compile on Mac. Here's a relevant snippet:
```
[ 50%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
In file included from /Users/vladimirli/Developer/paradiso/xmr-golang-bindings/monero/src/wallet/wallet2.cpp:35:
In file included from /usr/local/include/boost/algorithm/string/classification.hpp:17:
In file included from /usr/local/include/boost/range/as_literal.hpp:22:
In file included from /usr/local/include/boost/range/iterator_range.hpp:13:
In file included from /usr/local/include/boost/range/iterator_range_core.hpp:38:
In file included from /usr/local/include/boost/range/functions.hpp:20:
In file included from /usr/local/include/boost/range/size.hpp:21:
In file included from /usr/local/include/boost/range/size_type.hpp:24:
/usr/local/include/boost/type_traits/make_unsigned.hpp:32:4: error: static_assert failed due to requirement '!::boost::is_same<bool, bool>::value' "The template argument to make_unsigned must not be the type bool"
   BOOST_STATIC_ASSERT_MSG((! ::boost::is_same<typename remove_cv<T>::type, bool>::value), "The template argument to make_unsigned must not be the type bool");
   ^                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/local/include/boost/static_assert.hpp:31:45: note: expanded from macro 'BOOST_STATIC_ASSERT_MSG'
#     define BOOST_STATIC_ASSERT_MSG( ... ) static_assert(__VA_ARGS__)
                                            ^             ~~~~~~~~~~~
monero/src/serialization/binary_archive.h:142:41: note: in instantiation of template class 'boost::make_unsigned<bool>' requested here
    serialize_uvarint(*(typename boost::make_unsigned<T>::type *)(&v));
                                        ^
monero/src/cryptonote_core/cryptonote_tx_utils.h:105:7: note: in instantiation of function template specialization 'binary_archive<false>::serialize_varint<bool>' requested here
      VARINT_FIELD(is_subaddress)
      ^
monero/src/serialization/serialization.h:267:8: note: expanded from macro 'VARINT_FIELD'
    ar.serialize_varint(f);                     \
       ^
monero/src/cryptonote_core/cryptonote_tx_utils.h:101:5: note: in instantiation of function template specialization 'cryptonote::tx_destination_entry::do_serialize_object<false, binary_archive>' requested here
    BEGIN_SERIALIZE_OBJECT()
/usr/local/include/boost/type_traits/make_unsigned.hpp:32:4: error: static_assert failed due to requirement '!::boost::is_same<bool, bool>::value' "The template argument to make_unsigned must not be the type bool"
   BOOST_STATIC_ASSERT_MSG((! ::boost::is_same<typename remove_cv<T>::type, bool>::value), "The template argument to make_unsigned must not be the type bool");
   ^                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/local/include/boost/static_assert.hpp:31:45: note: expanded from macro 'BOOST_STATIC_ASSERT_MSG'
#     define BOOST_STATIC_ASSERT_MSG( ... ) static_assert(__VA_ARGS__)
                                            ^             ~~~~~~~~~~~
monero/src/serialization/binary_archive.h:142:41: note: in instantiation of template class 'boost::make_unsigned<bool>' requested here
    serialize_uvarint(*(typename boost::make_unsigned<T>::type *)(&v));
                                        ^
monero/src/cryptonote_core/cryptonote_tx_utils.h:105:7: note: in instantiation of function template specialization 'binary_archive<false>::serialize_varint<bool>' requested here
      VARINT_FIELD(is_subaddress)
      ^
monero/src/serialization/serialization.h:267:8: note: expanded from macro 'VARINT_FIELD'
    ar.serialize_varint(f);                     \
       ^
monero/src/cryptonote_core/cryptonote_tx_utils.h:101:5: note: in instantiation of function template specialization 'cryptonote::tx_destination_entry::do_serialize_object<false, binary_archive>' requested here
    BEGIN_SERIALIZE_OBJECT()
```

## moneromooo-monero | 2020-10-18T14:14:24+00:00
Then this one:

```
diff --git a/src/cryptonote_core/cryptonote_tx_utils.h b/src/cryptonote_core/cryptonote_tx_utils.h
index dbdf409b5..d4cfb8262 100644
--- a/src/cryptonote_core/cryptonote_tx_utils.h
+++ b/src/cryptonote_core/cryptonote_tx_utils.h
@@ -76,8 +76,8 @@ namespace cryptonote
     std::string original;
     uint64_t amount;                    //money
     account_public_address addr;        //destination address
-    bool is_subaddress;
-    bool is_integrated;
+    uint8_t is_subaddress;
+    uint8_t is_integrated;
 
     tx_destination_entry() : amount(0), addr(AUTO_VAL_INIT(addr)), is_subaddress(false), is_integrated(false) { }
     tx_destination_entry(uint64_t a, const account_public_address &ad, bool is_subaddress) : amount(a), addr(ad), is_subaddress(is_subaddress), is_integrated(false) { }
```

## leevlad | 2020-10-19T15:08:15+00:00
Just tried this out. Unfortunately it's still producing the same error. Tried just the diff you posted above, which compiled fine, but failed to sign on Linux with the same error.

Then tried both your suggestions from above, which also compiled fine but produced the same error when signing on Linux:
```
 #pragma once
@@ -76,8 +76,8 @@ namespace cryptonote
     std::string original;
     uint64_t amount;                    //money
     account_public_address addr;        //destination address
-    bool is_subaddress;
-    bool is_integrated;
+    uint8_t is_subaddress;
+    uint8_t is_integrated;
 
     tx_destination_entry() : amount(0), addr(AUTO_VAL_INIT(addr)), is_subaddress(false), is_integrated(false) { }
     tx_destination_entry(uint64_t a, const account_public_address &ad, bool is_subaddress) : amount(a), addr(ad), is_subaddress(is_subaddress), is_integrated(false) { }
@@ -102,8 +102,8 @@ namespace cryptonote
       FIELD(original)
       VARINT_FIELD(amount)
       FIELD(addr)
-      FIELD(is_subaddress)
-      FIELD(is_integrated)
+      VARINT_FIELD(is_subaddress)
+      VARINT_FIELD(is_integrated)
     END_SERIALIZE()
   };
```

Here's the resulting `unsigned_tx_set` string from the latest test I ran (with both you suggestions applied): https://gist.github.com/leevlad/efafb91c388430dd272996a1e6d8d2e1

## moneromooo-monero | 2020-10-19T19:05:18+00:00
Could you run with the patch at https://paste.debian.net/1167877/ on mac please ? It will log what it loads, and then I can compare with what I get here to see where it's going out of sync. You'll have to run the wallet with log level 0 or higher (the CLI wallet logs nothing by default).
I suspect it might be a list of size_t, and sizeof(size_t) might be different, we'll see.

## leevlad | 2020-10-19T21:44:32+00:00
Ok, I applied the patch from above to a clean state (at tag v0.17.1.0). Here's the log output:
https://gist.github.com/leevlad/b959b9c8b05b6dddaa6c6d616ffe3754

## moneromooo-monero | 2020-10-20T18:31:00+00:00
This is very odd, I can't see parts of the extra string in the decoded data you posted earlier. Are you sure you're loading the same data ?

## moneromooo-monero | 2020-10-25T02:08:20+00:00
What is the output of this exact command ?
```
echo -e '#include <stddef.h>\nint main(){return sizeof(size_t);}' | clang -x c - ; ./a.out ; echo $?
```

## leevlad | 2020-10-25T02:22:00+00:00
> This is very odd, I can't see parts of the extra string in the decoded data you posted earlier. Are you sure you're loading the same data ?

I'm not entirely sure what you're referring to. I just ran `monero-wallet-rpc` and tried to generate an unsigned transaction in the same way as before and gave you the trace output from `stdout`.



> What is the output of this exact command ?
> 
> ```
> echo -e '#include <stddef.h>\nint main(){return sizeof(size_t);}' | clang -x c - ; ./a.out ; echo $?
> ```

The output was:
```
8
```

## moneromooo-monero | 2020-10-25T02:26:58+00:00
If you generated another, it doesn't match anymore the one I have, so can't compare. Can you send me the new rx dump then, which matches the log data ?

## leevlad | 2020-10-25T02:44:37+00:00
This should be it: https://gist.github.com/leevlad/9c023225f807c0b762b8d1f53c59719f

## selsta | 2021-01-03T04:20:28+00:00
Someone on IRC reported the same issue.

## jonathancross | 2021-01-03T13:07:50+00:00
I've seen this issue as well going back several releases, but have not looked into it carfully to isolate the problem.

I also saw that outputs exported from macOS (watch-only wallet) via `export_outputs` would corrupt a (Linux) offline wallet when imported.  This seems to contradict what @leevlad says above in https://github.com/monero-project/monero/issues/6901#issuecomment-711084354 though, so I figured it might be something specific to my setup.  

Outputs exported from Linux watch-only version of the same wallet worked fine.

## moneromooo-monero | 2021-01-16T17:24:59+00:00
https://github.com/moneromooo-monero/bitmonero/commit/2910c84f4ba7c80f70e20c2746be6bf4189d1df0 should fix it. It should also convert your existing mac wallet cache to the new format, and be able to reload it. If it fails, it means the patch is not complete.

## moneromooo-monero | 2021-01-17T21:07:20+00:00
https://github.com/moneromooo-monero/bitmonero/commit/b744466e906b6c6233e996de07fa648624918a4c (slightly modified, thanks xmrdog for mac testing) fixes it.

## dethos | 2021-02-11T15:36:31+00:00
I'm experiencing the same problem using 2 `monero-wallet-rpc` instances on Linux. The view-only wallet creates the `unsigned_txset` hex but full-wallet does not recognize it.

----------------------
**RPC response**:
```
"code": -39,
"message": "cannot load unsigned_txset"
```
**RPC logs**:
```
2021-02-11 13:53:46.889 W Failed to decrypt unsigned tx: Failed to authenticate ciphertext
2021-02-11 14:14:40.492 E !crypto::check_signature(hash, pkey, signature). THROW EXCEPTION: error::wallet_internal_error
2021-02-11 14:14:40.492 W Failed to decrypt unsigned tx: Failed to authenticate ciphertext
```
**Network**: Stagenet
**Monero version:** Monero 'Oxygen Orion' (v0.17.1.9-release)

-------------------

**Steps to reproduce:**
1. call `transfer` from the view-only wallet
2. Store the  generated `unsigned_txset` hex
3. call `sign_transfer` (or even `describe_transfer`) using the stored `unsigned_txset` on the full-wallet
4. RPC returns the above error message.

## woodser | 2021-02-12T00:00:03+00:00
> What is the output of this exact command ?
> 
> ```
> echo -e '#include <stddef.h>\nint main(){return sizeof(size_t);}' | clang -x c - ; ./a.out ; echo $?
> ```

`sizeof(size_t);` returns 4 in WebAssembly (built on mac) which also has serialization compatibility issues:

- https://github.com/monero-ecosystem/monero-javascript/issues/50.
- The wallet cache fails to deserialize in WebAssembly.  moneromooo-monero@b744466 appears to have no effect unfortunately

## jonathancross | 2021-02-13T16:37:06+00:00
FYI: This should be fixed **when** ~~now that~~ #7321 is merged.

## selsta | 2021-02-13T16:38:18+00:00
It is not merged yet?

## jonathancross | 2021-02-13T16:50:27+00:00
Sorry, my mistake.  Updated my comment.

## jonathancross | 2021-04-07T16:15:45+00:00
#7321 is now merged  :-)

# Action History
- Created by: leevlad | 2020-10-16T15:08:37+00:00
- Closed at: 2021-10-06T02:38:20+00:00
