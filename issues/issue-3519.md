---
title: How to debug json's set to mining pool
source_url: https://github.com/xmrig/xmrig/issues/3519
author: Redhawk18
assignees: []
labels: []
created_at: '2024-07-29T17:47:27+00:00'
updated_at: '2025-06-18T22:08:41+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:08:41+00:00'
---

# Original Description
**Describe the bug**
I wanted to debug print out the json's sent to the mining pool.

**To Reproduce**
I added this code to `EthStratumClient::subscribe`
```cpp
  JsonRequest::create(doc, m_sequence, "mining.subscribe", params);

  StringBuffer buffer;
  Writer<StringBuffer> writer(buffer);
  doc.Accept(writer);
  LOG_INFO(buffer.GetString());
  ```

**Expected behavior**
To see the json printed out by the logger.

**Required data**
 - XMRig version
    - master


# Discussion History
## SChernykh | 2024-07-29T18:07:21+00:00
There is `WITH_DEBUG_LOG` for cmake: add `-DWITH_DEBUG_LOG=ON` to cmake command line when building. XMRig will print all pool communication.

## Redhawk18 | 2024-07-29T18:20:41+00:00
> There is `WITH_DEBUG_LOG` for cmake: add `-DWITH_DEBUG_LOG=ON` to cmake command line when building. XMRig will print all pool communication.

I'll try that, I thought that maybe the method above was dead code that wasn't used anymore.

## SChernykh | 2024-07-29T18:24:28+00:00
`EthStratumClient::subscribe` is used when mining Ravencoin or Raptoreum.

## Redhawk18 | 2024-07-29T18:50:41+00:00
Thanks! Is there a table or a resource for which protocol is used for which coin?

## SChernykh | 2024-07-29T18:55:20+00:00
You can find some data in `Algorithm.cpp` and `Coin.cpp` in src/base/crypto folder.

## Redhawk18 | 2024-07-29T19:25:55+00:00
> You can find some data in `Algorithm.cpp` and `Coin.cpp` in src/base/crypto folder.

I see where the coins are defined with their short and long names, but not which coins map to which protocols.

## SChernykh | 2024-07-29T19:32:10+00:00
src/base/net/stratum/AutoClient.cpp

Only KawPow and GhostRider algorithms use EthStratumClient

## Redhawk18 | 2024-07-29T19:44:17+00:00
> src/base/net/stratum/AutoClient.cpp
> 
> Only KawPow and GhostRider algorithms use EthStratumClient

What does monero use then?

# Action History
- Created by: Redhawk18 | 2024-07-29T17:47:27+00:00
- Closed at: 2025-06-18T22:08:41+00:00
