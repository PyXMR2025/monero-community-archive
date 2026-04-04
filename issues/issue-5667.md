---
title: why transaction type failed
source_url: https://github.com/monero-project/monero/issues/5667
author: vae520283995
assignees: []
labels: []
created_at: '2019-06-18T11:30:18+00:00'
updated_at: '2019-06-19T01:36:53+00:00'
type: issue
status: closed
closed_at: '2019-06-19T01:36:53+00:00'
---

# Original Description
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "469yWRhGbihfSBX3WwciNgEc3e8gVhJkpGFFYerFnSBgc4LCbiStL453FqzBH1KdxpePqXcEfkwRF6Ju4sbp1bvRHCT6KMD",
      "amount": 1592000000000,
      "confirmations": 1854648,
      "double_spend_seen": false,
      "fee": 32200000,
      "height": 0,
      "note": "",
      "payment_id": "d4ae08d4a13053b4f098759603dbff3c5dbb16e367f748d61234567890abeefe",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1560565893,
      "txid": "24bf7964915b187c8e947b7cc02f634379125296549b502acedc0038a1846a1d",
      "type": "failed",
      "unlock_time": 0
    },
    "transfers": [{
      "address": "469yWRhGbihfSBX3WwciNgEc3e8gVhJkpGFFYerFnSBgc4LCbiStL453FqzBH1KdxpePqXcEfkwRF6Ju4sbp1bvRHCT6KMD",
      "amount": 1592000000000,
      "confirmations": 1854648,
      "double_spend_seen": false,
      "fee": 32200000,
      "height": 0,
      "note": "",
      "payment_id": "d4ae08d4a13053b4f098759603dbff3c5dbb16e367f748d61234567890abeefe",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1560565893,
      "txid": "24bf7964915b187c8e947b7cc02f634379125296549b502acedc0038a1846a1d",
      "type": "failed",
      "unlock_time": 0
    }]
  }
}

why type failed?

# Discussion History
## moneromooo-monero | 2019-06-18T11:50:13+00:00
It means it was not mined and got dropped from the txpool. This can be due to double spend, wrong ring size, too low fee and nobody mined it, etc.


## vae520283995 | 2019-06-19T01:36:49+00:00
> It means it was not mined and got dropped from the txpool. This can be due to double spend, wrong ring size, too low fee and nobody mined it, etc.

thank you very much

# Action History
- Created by: vae520283995 | 2019-06-18T11:30:18+00:00
- Closed at: 2019-06-19T01:36:53+00:00
