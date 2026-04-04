---
title: 'Relying on `--data-dir` can be problematic. '
source_url: https://github.com/monero-project/monero/issues/9175
author: '0xFFFC0000'
assignees:
- '0xFFFC0000'
labels:
- bug
- low priority
- tests
created_at: '2024-02-16T09:07:26+00:00'
updated_at: '2024-02-16T11:10:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In `functional_tests` we define `--data-dir` for the daemon but, the daemon will read the default `--config-file` too. If you have anything in your default config file that would interfere with tests, that means tests are not going to run correctly. 


E.g. you can run the `mining` test in functional_tests with: 
```
/usr/bin/python3 /home/0xfffc/developments/monero/tests/functional_tests/functional_tests_rpc.py /usr/bin/python3 /home/0xfffc/developments/monero/tests/functional_tests /home/0xfffc/developments/monero/build mining
```

these are the commands we are running for the `mining`  test in `functional_tests`: 

```

/home/0xfffc/developments/monero/build/bin/monerod --regtest --fixed-difficulty 10 --no-igd --p2p-bind-port 18280 --rpc-bind-port 18180 --zmq-rpc-bind-port 18380 --zmq-pub tcp://127.0.0.1:18480 --non-interactive --disable-dns-checkpoints --check-updates disabled --rpc-ssl disabled --data-dir /home/0xfffc/developments/monero/build/functional-tests-directory/monerod0 --log-level 1 --offline


/home/0xfffc/developments/monero/build/bin/monerod --regtest --fixed-difficulty 10 --no-igd --p2p-bind-port 18281 --rpc-bind-port 18181 --zmq-rpc-bind-port 18381 --zmq-pub tcp://127.0.0.1:18481 --non-interactive --disable-dns-checkpoints --check-updates disabled --rpc-ssl disabled --data-dir /home/0xfffc/developments/monero/build/functional-tests-directory/monerod1 --log-level 1 --rpc-payment-address 44SKxxLQw929wRF6BA9paQ1EWFshNnKhXM3qz6Mo3JGDE2YG3xyzVutMStEicxbQGRfrYvAAYxH6Fe8rnD56EaNwUiqhcwR --rpc-payment-difficulty 10 --rpc-payment-credits 5000 --offline


/home/0xfffc/developments/monero/build/bin/monerod --regtest --fixed-difficulty 10 --no-igd --p2p-bind-port 18282 --rpc-bind-port 18182 --zmq-rpc-bind-port 18382 --zmq-pub tcp://127.0.0.1:18482 --non-interactive --disable-dns-checkpoints --check-updates disabled --rpc-ssl disabled --data-dir /home/0xfffc/developments/monero/build/functional-tests-directory/monerod2 --log-level 1 --add-exclusive-node 127.0.0.1:18283


/home/0xfffc/developments/monero/build/bin/monerod --regtest --fixed-difficulty 10 --no-igd --p2p-bind-port 18283 --rpc-bind-port 18183 --zmq-rpc-bind-port 18383 --zmq-pub tcp://127.0.0.1:18483 --non-interactive --disable-dns-checkpoints --check-updates disabled --rpc-ssl disabled --data-dir /home/0xfffc/developments/monero/build/functional-tests-directory/monerod3 --log-level 1 --add-exclusive-node 127.0.0.1:18282


/home/0xfffc/developments/monero/build/bin/monero-wallet-rpc --wallet-dir /home/0xfffc/developments/monero/build/functional-tests-directory --rpc-bind-port 18090 --disable-rpc-login --rpc-ssl disabled --daemon-ssl disabled --log-level 1 --allow-mismatched-daemon-version --daemon-port 18180


/home/0xfffc/developments/monero/build/bin/monero-wallet-rpc --wallet-dir /home/0xfffc/developments/monero/build/functional-tests-directory --rpc-bind-port 18091 --disable-rpc-login --rpc-ssl disabled --daemon-ssl disabled --log-level 1 --allow-mismatched-daemon-version --daemon-port 18180


/home/0xfffc/developments/monero/build/bin/monero-wallet-rpc --wallet-dir /home/0xfffc/developments/monero/build/functional-tests-directory --rpc-bind-port 18092 --disable-rpc-login --rpc-ssl disabled --daemon-ssl disabled --log-level 1 --allow-mismatched-daemon-version --daemon-port 18180


/home/0xfffc/developments/monero/build/bin/monero-wallet-rpc --wallet-dir /home/0xfffc/developments/monero/build/functional-tests-directory --rpc-bind-port 18093 --disable-rpc-login --rpc-ssl disabled --daemon-ssl disabled --log-level 1 --allow-mismatched-daemon-version --daemon-port 18180


/home/0xfffc/developments/monero/build/bin/monero-wallet-rpc --wallet-dir /home/0xfffc/developments/monero/build/functional-tests-directory --rpc-bind-port 18094 --disable-rpc-login --rpc-ssl disabled --daemon-ssl disabled --log-level 1 --allow-mismatched-daemon-version --daemon-port 18182


/home/0xfffc/developments/monero/build/bin/monero-wallet-rpc --wallet-dir /home/0xfffc/developments/monero/build/functional-tests-directory --rpc-bind-port 18095 --disable-rpc-login --rpc-ssl disabled --daemon-ssl disabled --log-level 1 --allow-mismatched-daemon-version --offline

```



# Discussion History
## hyc | 2024-02-16T11:10:01+00:00
Would be a good idea to have a `--no-config-file option` to prevent that from being read while running tests.
Or, have the test suite create its own config file and specify that.

# Action History
- Created by: 0xFFFC0000 | 2024-02-16T09:07:26+00:00
