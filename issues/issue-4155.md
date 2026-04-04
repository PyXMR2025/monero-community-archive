---
title: 'Unable to connect monero rpc wallet to a daemon - N5tools5error21wallet_int
  ernal_errorE: Index out of bounds of hashcha'
source_url: https://github.com/monero-project/monero/issues/4155
author: vijayr2410
assignees: []
labels:
- duplicate
created_at: '2018-07-19T20:27:47+00:00'
updated_at: '2018-07-19T21:40:56+00:00'
type: issue
status: closed
closed_at: '2018-07-19T21:40:56+00:00'
---

# Original Description
PS C:\CoinClients\Monero> .\monero-wallet-rpc.exe --daemon-login xyzuser:1234332222 --rpc-bind-port 18082 --daemon-address 127.0.0.1:18085 --rpc-login rxyzuser:1234332222 --wallet-file C:\CoinData\Monero\Wallet1 --password 1234533 --rpc-bind-ip 127.0.0.1 --confirm-external-bind --trusted-daemon --max-concurrency 10 --log-level 4
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.2.0-release)
2018-07-19 19:28:59.554 2652    INFO    wallet.wallet2  src/wallet/wallet_args.cpp:192  Setting log level = 4
2018-07-19 19:28:59.554 2652    INFO    wallet.wallet2  src/wallet/wallet_args.cpp:195  Logging to: C:\CoinClients\Monero\monero-wallet-rpc.log
Logging to C:\CoinClients\Monero\monero-wallet-rpc.log
2018-07-19 19:28:59.554 2652    WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:2948   Loading wallet...
2018-07-19 19:28:59.554 2652    DEBUG   device.ledger   src/device/device_ledger.cpp:223        Device 0 Created
2018-07-19 19:28:59.695 2652    INFO    wallet.wallet2  src/wallet/wallet2.cpp:5531     ringdb path set to C:\ProgramData\.shared-ringdb
2018-07-19 19:28:59.757 2652    WARN    wallet.wallet2  src/wallet/wallet2.cpp:3762     Loaded wallet keys file, with public address: 49zYanoMEvXDJeX1vjs7ELHpgSDvufB5sN84
SwrmndRWQQAGK9HT8QRHkHYvd5pW5S1eqjSLmAZaV8xG9TXZyP6XRE1K4cV
2018-07-19 19:28:59.757 2652    INFO    wallet.wallet2  src/wallet/wallet2.cpp:3781     Trying to decrypt cache data
2018-07-19 19:28:59.867 2652    DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3906     trimming to 1578999, offset 1578999
2018-07-19 19:28:59.867 2652    DEBUG   net.http        contrib/epee/include/net/http_client.h:365      Reconnecting...
2018-07-19 19:28:59.867 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 395
2018-07-19 19:28:59.867 2652    TRACE   net.http        contrib/epee/include/net/http_client.h:758      http_stream_filter::parse_cached_header(*)
2018-07-19 19:28:59.867 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 98
2018-07-19 19:28:59.867 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 160
2018-07-19 19:28:59.867 2652    TRACE   net.http        contrib/epee/include/net/http_client.h:758      http_stream_filter::parse_cached_header(*)
2018-07-19 19:28:59.867 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 127
2018-07-19 19:28:59.867 2652    DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:1670     Daemon is recent enough, asking for pruned blocks
2018-07-19 19:28:59.898 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 172
2018-07-19 19:28:59.898 2652    TRACE   net.http        contrib/epee/include/net/http_client.h:758      http_stream_filter::parse_cached_header(*)
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.914 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.929 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.945 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.960 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.960 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:28:59.960 2652    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 6014
2018-07-19 19:28:59.976 2652    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1721     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal
_error
2018-07-19 19:28:59.976 7760    DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:1670     Daemon is recent enough, asking for pruned blocks
2018-07-19 19:28:59.976 2652    WARN    net.http        src/wallet/wallet_errors.h:794  C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1721:N5tools5error21wallet_int
ernal_errorE: Index out of bounds of hashchain
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 172
2018-07-19 19:29:00.007 7760    TRACE   net.http        contrib/epee/include/net/http_client.h:758      http_stream_filter::parse_cached_header(*)
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.007 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.023 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.039 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.054 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.054 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.054 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.054 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.054 7760    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 425
2018-07-19 19:29:00.070 2652    INFO    wallet.wallet2  src/wallet/wallet2.cpp:2309     Another try pull_blocks (try_count=0)...
2018-07-19 19:29:00.070 2652    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1721     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal
_error
2018-07-19 19:29:00.070 2652    WARN    net.http        src/wallet/wallet_errors.h:794  C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1721:N5tools5error21wallet_int
ernal_errorE: Index out of bounds of hashchain
2018-07-19 19:29:00.070 6696    DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:1670     Daemon is recent enough, asking for pruned blocks
2018-07-19 19:29:00.148 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 172
2018-07-19 19:29:00.148 6696    TRACE   net.http        contrib/epee/include/net/http_client.h:758      http_stream_filter::parse_cached_header(*)
2018-07-19 19:29:00.148 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.164 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.179 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.195 6696    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 425
2018-07-19 19:29:00.210 2652    INFO    wallet.wallet2  src/wallet/wallet2.cpp:2309     Another try pull_blocks (try_count=1)...
2018-07-19 19:29:00.210 2652    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1721     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal
_error
2018-07-19 19:29:00.210 2652    WARN    net.http        src/wallet/wallet_errors.h:794  C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1721:N5tools5error21wallet_int
ernal_errorE: Index out of bounds of hashchain
2018-07-19 19:29:00.210 6568    DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:1670     Daemon is recent enough, asking for pruned blocks
2018-07-19 19:29:00.242 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 172
2018-07-19 19:29:00.242 6568    TRACE   net.http        contrib/epee/include/net/http_client.h:758      http_stream_filter::parse_cached_header(*)
2018-07-19 19:29:00.242 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.242 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.257 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.273 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.289 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 425
2018-07-19 19:29:00.304 2652    INFO    wallet.wallet2  src/wallet/wallet2.cpp:2309     Another try pull_blocks (try_count=2)...
2018-07-19 19:29:00.304 6568    DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:1670     Daemon is recent enough, asking for pruned blocks
2018-07-19 19:29:00.304 2652    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1721     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal
_error
2018-07-19 19:29:00.304 2652    WARN    net.http        src/wallet/wallet_errors.h:794  C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1721:N5tools5error21wallet_int
ernal_errorE: Index out of bounds of hashchain
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 172
2018-07-19 19:29:00.351 6568    TRACE   net.http        contrib/epee/include/net/http_client.h:758      http_stream_filter::parse_cached_header(*)
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.351 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.367 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.382 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.398 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 10000
2018-07-19 19:29:00.398 6568    TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 425
2018-07-19 19:29:00.414 2652    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2314     pull_blocks failed, try_count=3
2018-07-19 19:29:00.414 2652    ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:2990   Wallet initialization failed: Index out of bounds of hashchain
2018-07-19 19:29:00.414 2652    DEBUG   device.ledger   src/device/device_ledger.cpp:228        Device 0 Destroyed

# Discussion History
## moneromooo-monero | 2018-07-19T21:38:36+00:00
See https://github.com/monero-project/monero/issues/3848, with a fix now merged.

+duplicate

# Action History
- Created by: vijayr2410 | 2018-07-19T20:27:47+00:00
- Closed at: 2018-07-19T21:40:56+00:00
