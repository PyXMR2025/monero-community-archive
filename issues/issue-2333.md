---
title: monero-wallet-rpc missing user-agent option
source_url: https://github.com/monero-project/monero/issues/2333
author: galindro
assignees: []
labels:
- invalid
created_at: '2017-08-23T17:56:29+00:00'
updated_at: '2017-09-02T12:36:19+00:00'
type: issue
status: closed
closed_at: '2017-09-02T12:36:19+00:00'
---

# Original Description
I'm trying to use [Monero Wallet for Google Chrome](https://github.com/Monero-Monitor/monero-wallet-chrome) and I could not use it with monero-wallet-rpc because --user-agent option was dropped.

```bash
./monero-wallet-rpc --wallet-file monero.wall --password-file monero.wall.password --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18082 --daemon-address node.moneroclub.com:8880 --user-agent f42c371a
2017-08-23 14:55:08,152 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:119] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,152 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:120] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-08-23 14:55:08,162 DEBUG [default] [galindro@unknown-host] [void tools::log_stack_trace(const char*)] [/DISTRIBUTION-BUILD/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
Failed to parse arguments: unrecognised option '--user-agent'

General options:
  --help                          Produce help message
  --version                       Output version information

Wallet options:
  --daemon-address arg            Use daemon instance at <host>:<port>
  --daemon-host arg               Use daemon instance at host <arg> instead of 
                                  localhost
  --password arg                  Wallet password
  --password-file arg             Wallet password file
  --daemon-port arg (=0)          Use daemon instance at port <arg> instead of 
                                  18081
  --daemon-login arg              Specify username[:password] for daemon RPC 
                                  client
  --testnet                       For testnet. Daemon must also be launched 
                                  with --testnet flag
  --restricted-rpc                Restricts to view-only commands
  --rpc-bind-port arg             Sets bind port for server
  --disable-rpc-login             Disable HTTP authentication for RPC 
                                  connections served by this process
  --trusted-daemon                Enable commands which rely on a trusted 
                                  daemon
  --rpc-bind-ip arg (=127.0.0.1)  Specify ip to bind rpc server
  --rpc-login arg                 Specify username[:password] required for RPC 
                                  server
  --confirm-external-bind         Confirm rpc-bind-ip value is NOT a loopback 
                                  (local) IP
  --wallet-file arg               Use wallet <arg>
  --generate-from-json arg        Generate wallet from JSON format file
  --log-file arg                  Specify log file
  --log-level arg                 0-4 or categories
  --max-concurrency arg (=0)      Max number of threads to use for a parallel 
                                  job
  --config-file arg               Config file
```

# Discussion History
## moneromooo-monero | 2017-08-23T19:24:43+00:00
The user agent thing was a stopgap hack. You now run monerod using --rpc-login xxxxx.

## moneromooo-monero | 2017-09-02T12:30:48+00:00
You'll have to ask the author for this plugin to update, or send a PR for it.

+invalid


# Action History
- Created by: galindro | 2017-08-23T17:56:29+00:00
- Closed at: 2017-09-02T12:36:19+00:00
