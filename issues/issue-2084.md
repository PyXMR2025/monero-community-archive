---
title: Build fails with openssl version 1.1
source_url: https://github.com/monero-project/monero/issues/2084
author: erikd
assignees: []
labels: []
created_at: '2017-06-13T09:24:07+00:00'
updated_at: '2017-06-26T05:08:22+00:00'
type: issue
status: closed
closed_at: '2017-06-26T05:08:22+00:00'
---

# Original Description
Debian testing (which will become Debian stable RealSoonNow) only ships with a `libssl-dev-1.1.0f` and the in-tree unbound code doesn't build against OpenSSL 1.1. For example:
```
monero/external/unbound/validator/val_secalgo.c:256:8: error: dereferencing pointer to
 incomplete type ‘DSA_SIG {aka struct DSA_SIG_st}’
  dsasig->r = R;
        ^~
monero/external/unbound/validator/val_secalgo.c: In function ‘setup_ecdsa_sig’:
monero/external/unbound/validator/val_secalgo.c:291:11: error: dereferencing pointer to
 incomplete type ‘ECDSA_SIG {aka struct ECDSA_SIG_st}’
  ecdsa_sig->r = BN_bin2bn(*sig, bnsize, ecdsa_sig->r);
           ^~
monero/external/unbound/validator/val_secalgo.c: In function ‘verify_canonrrset’:
monero/external/unbound/validator/val_secalgo.c:513:13: error: storage size of ‘ctx’ isn’t
known
  EVP_MD_CTX ctx;
             ^~~
monero/external/unbound/validator/val_secalgo.c:564:5: warning: implicit declaration of 
function ‘EVP_MD_CTX_cleanup’ [-Wimplicit-function-declaration]
  if(EVP_MD_CTX_cleanup(&ctx) == 0) {
```


# Discussion History
## moneromooo-monero | 2017-06-13T22:43:47+00:00
https://github.com/monero-project/monero/pull/2086

## erikd | 2017-06-26T05:08:22+00:00
Fixed in #2089 .

# Action History
- Created by: erikd | 2017-06-13T09:24:07+00:00
- Closed at: 2017-06-26T05:08:22+00:00
