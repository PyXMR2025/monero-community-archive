---
title: osx 10.13 compile fail - was built for newer OSX version (10.13) than being
  linked (10.11)
source_url: https://github.com/monero-project/monero-gui/issues/1558
author: BigslimVdub
assignees: []
labels: []
created_at: '2018-09-13T02:55:44+00:00'
updated_at: '2018-09-18T03:41:11+00:00'
type: issue
status: closed
closed_at: '2018-09-18T03:41:11+00:00'
---

# Original Description
```
-framework QtWidgets -framework OpenGL -framework AGL 
clang: warning: argument unused during compilation: '-pie' [-Wunused-command-line-argument]
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(wallet_manager.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(wallet.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(utils.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(version.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libepee.a(mlog.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(cryptonote_format_utils.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(cryptonote_basic_impl.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libeasylogging.a(easylogging++.cc.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(device.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libepee.a(wipeable_string.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libepee.a(hex.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libepee.a(http_auth.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(util.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(updates.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(wallet2.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(dns_utils.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(subaddress.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(address_book.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(subaddress_account.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(pending_transaction.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(transaction_history.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(unsigned_transaction.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(crypto.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(electrum-words.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(account.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(random.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libepee.a(memwipe.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(i18n.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(checkpoints.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(multisig.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(cryptonote_tx_utils.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(device_default.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(rctOps.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(rctSigs.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(rctTypes.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libepee.a(string_tools.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(threadpool.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(node_rpc_proxy.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(password.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(base58.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(ringdb.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(transaction_info.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(chacha.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(hash.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(slow-hash.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(crypto-ops.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(keccak.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(tree-hash.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(libunbound.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(miner.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(log.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(bulletproofs.cc.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(perf_timer.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(aesb.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(alloc.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(authzone.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(config_file.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(context.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(module.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(net_help.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(crypto-ops-data.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(hash-extra-blake.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(hash-extra-groestl.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(hash-extra-jh.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(hash-extra-skein.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(infra.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(libworker.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(localzone.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(log.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/liblmdb.a(mdb.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(modstack.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(oaes_lib.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(rbtree.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(regional.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(rrset.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(rctCryptoOps.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(slabhash.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(sbuffer.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(tube.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(ub_event.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(random.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(msgreply.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(rtt.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(difficulty.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(dnstree.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(as112.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(blake256.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(netevent.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(dname.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(dns64.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(msgencode.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(iter_fwd.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(fptr_wlist.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(msgparse.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(groestl.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(lookup3.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(iter_hints.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(configlexer.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(iterator.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(jh.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(lruhash.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/liblmdb.a(midl.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(mesh.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(mini_event.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(val_secalgo.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(outside_network.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(packed_rrset.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(reallocarray.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(respip.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(skein.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(parseutil.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(keyraw.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(str2wire.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(rrdef.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(wire2str.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(configparser.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(validator.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(val_anchor.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(autotrust.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(dns.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(val_sigcrypt.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(iter_utils.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(listen_dnsport.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(iter_delegpt.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(iter_donotq.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(val_kcache.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(val_kentry.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(val_neg.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(val_nsec3.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(val_nsec.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(outbound_list.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(iter_priv.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(iter_resptype.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(iter_scrub.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(parse.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(timehist.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(val_utils.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libunbound.a(view.c.o)) was built for newer OSX version (10.13) than being linked (10.11)
```
Only Daemon and Wallet RPC are built. 

QT 5.11.1
High Sierra 10.13.6

# Discussion History
## stoffu | 2018-09-13T03:00:39+00:00
```
clang: warning: argument unused during compilation: '-pie' [-Wunused-command-line-argument]
ld: warning: object file (/Users/admin/Downloads/monero-gui/monero/lib/libwallet_merged.a(wallet_manager.cpp.o)) was built for newer OSX version (10.13) than being linked (10.11)
```
These are all warning messages, not errors, and shouldn't prevent the build from completing. If your build fails, there must be some other error.


## BigslimVdub | 2018-09-13T03:06:39+00:00
![gui build fail](https://user-images.githubusercontent.com/30030687/45464856-1a958d80-b6d8-11e8-8e62-509e8deb6485.png)


## stoffu | 2018-09-13T03:09:53+00:00
Please post logs in text format, not images.

## BigslimVdub | 2018-09-13T03:40:55+00:00
So no clue what went on here but I ran get_libwallet_api.sh and it fully built the gui no issues so far but its only 28.4mb (this says v0.12.3.0-4-gc7bca47b) not the 283.1mb from 0.12.3.0. 

Seems to be working fine syncing with my remote daemon.

## BigslimVdub | 2018-09-18T03:41:05+00:00
Gui build successful on osx 10.13.6 with additions made [here](https://github.com/monero-project/monero-gui/pull/1563) to wallet-gui.pro file. Confirm on Monero and also Aeon gui builds. 

# Action History
- Created by: BigslimVdub | 2018-09-13T02:55:44+00:00
- Closed at: 2018-09-18T03:41:11+00:00
