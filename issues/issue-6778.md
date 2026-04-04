---
title: CLI wallet RPC SSL with passphrase hangs on "Enter PEM pass phrase"
source_url: https://github.com/monero-project/monero/issues/6778
author: garlicgambit
assignees: []
labels: []
created_at: '2020-08-24T17:59:34+00:00'
updated_at: '2020-08-30T17:51:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If you instruct the CLI wallet to use a SSL key with a passphrase for the RPC connection to the daemon it will hang on: `Enter PEM pass phrase`.  
  
To reproduce you need create a SSL private key and certificate with a passphrase:  
```./monero-gen-ssl-cert --private-key-filename privatekey.pem --certificate-filename certificate.pem --prompt-for-passphrase```
  
Open the monero wallet with the following command:  
```./monero-wallet-cli --daemon-ssl-private-key privatekey.pem --daemon-ssl-certificate certificate.pem```

# Discussion History
## skironDotNet | 2020-08-25T05:11:58+00:00
So far the only way it works is if you generate ssl cert without passphrase, so don't use `--prompt-for-passphrase` or `--passphrase`. There is no way to pass ssl priv key passphrase to neither monerod or monero-wallet-cli

## garlicgambit | 2020-08-30T17:51:39+00:00
@skironDotNet, the monerod daemon will work when a SSL key is configured with a passphrase.

# Action History
- Created by: garlicgambit | 2020-08-24T17:59:34+00:00
