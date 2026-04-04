---
title: 'relay_tx error via monero_wallet_rpc: ''Failed to parse tx metadata.'''
source_url: https://github.com/monero-project/monero/issues/4283
author: sneurlax
assignees: []
labels: []
created_at: '2018-08-20T01:28:33+00:00'
updated_at: '2018-08-20T05:51:13+00:00'
type: issue
status: closed
closed_at: '2018-08-20T05:51:13+00:00'
---

# Original Description
When using `relay_tx` via JSON-RPC (`monero-wallet-rpc,`) error code `-27` (`"Failed to parse tx metadata"`) is thrown.  There doesn't appear to be any way to provide `tx_metadata` to `relay_tx`.

To reproduce, generate a transaction with `do_not_relay`, `get_tx_hex`, and `get_tx_metadata` all set to true.  Use `relay_tx` with param `{ hex: tx_blob }`.  There is not a clear way to pass `tx_metadata` as a param from looking at `wallet_rpc_server.cpp`.

# Discussion History
## stoffu | 2018-08-20T05:04:42+00:00
The `hex` parameter of `relay_tx` expects the value of `tx_metadata` in the response of the `transfer` command. It works for me.

## sneurlax | 2018-08-20T05:48:20+00:00
I don't understand your reply.  I tried passing `{ hex: tx_metadata }` with no success.

```js
          let tx_blob = '';
          let tx_metadata = '';

          describe('transfer()', () => {
            it('should generate transaction', done => {
              walletRPC.transfer({
                address: address,
                amount: 0.1,
                mixin: 6,
                get_tx_key: true,
                account_index: 0,
                subaddr_indices: 0,
                priority: 1,
                do_not_relay: true,
                get_tx_hex: true,
                get_tx_metadata: true
              })
              .then(result => {
                result.should.be.a.Object();
                result.amount.should.be.a.Number();
                result.amount.should.be.equal(100000000000);
                result.fee.should.be.a.Number();
                result.tx_hash.should.be.a.String();
                result.tx_key.should.be.a.String();
                result.tx_blob.should.be.a.String();
                tx_blob = result.tx_blob;
                result.tx_metadata.should.be.a.String();
                tx_metadata = result.tx_metadata;
              })
              .then(done, done);
            })
            .timeout(3000);
          });

          describe('relay_tx()', () => {
            it('should relay transaction', done => {
              walletRPC.relay_tx(tx_metadata)
              .then(result => {
                console.log(result);
              })
              .then(done, done);
            });
          });
```

Same error code as when passing `tx_blob`

## sneurlax | 2018-08-20T05:49:19+00:00
and for reference,

```
  /**
   * Relay a transaction
   *
   * @function relay_tx
   * @param {string} hex - Transaction metadata in hex as string  (optional)
   */
  relay_tx(hex) {
    let params = {
      hex: hex
    };
    let method = this._run('relay_tx', params);

    let save = this.store(); // Save wallet state after transaction relay

    return this._run('relay_tx');
  }
```

## sneurlax | 2018-08-20T05:51:13+00:00
Got it.  I had to `return method` in my last comment.  Thanks @stoffu 

# Action History
- Created by: sneurlax | 2018-08-20T01:28:33+00:00
- Closed at: 2018-08-20T05:51:13+00:00
