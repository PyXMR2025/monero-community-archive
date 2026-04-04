---
title: m-of-n multisig wallets have to be finalized twice
source_url: https://github.com/monero-project/monero/issues/5000
author: jacoblyles
assignees: []
labels: []
created_at: '2018-12-20T01:15:44+00:00'
updated_at: '2019-01-16T20:49:22+00:00'
type: issue
status: closed
closed_at: '2019-01-16T20:49:22+00:00'
---

# Original Description
My testing on creating 3-of-5 multisig wallets from the `monero-wallet-cli` shows that the `finalize-multisig`  command must be run twice for it to work:

```
[wallet 41fJjQ]: finalize_multisig MultisigxV14VCYeTTq1pB5E1T9rKfQZZA6fUMrZDCNU8jTpSfDkAc4TKNak2DWaaN2naUEHNdUkNGyfuymTEc9s4czUi1BFpDGZnqmPKensZe1qYF4kgqf7G4LxfLkL3h72FvsippCdkbBNmMkZLHrTuaYdS8ijauuVKUrhbHkLotJY6dNS1pYMB3T5DMGVqfqupbbHTp1dJz8ZhHbAr4J7Tr8x5kxa3WqBpXScovQqESipdN9yWukQdnrgYTgaUML1dzPgdc7SSZiK2pW3nZ6msGduCXBjfW4ktSuqgQhtaFgu1Yjk5bnoGXd1xCJ MultisigxV18bgD2HpBVZHAoqUumo532pgVepseKJbZ31eCoQEt577NZnqmPKensZe1qYF4kgqf7G4LxfLkL3h72FvsippCdkbBNwPcL2D2Y166f8FHe2XqjU3UeePdx1Y8oUsS5XY2XECdexEPEUTK4QMYneJj3H36LF55nDuNmDgc3HHc9BssgRw1Bbey5Um52sfF38Qfs23WxjjF37CtoBWRae54JGH938MuPKKvj25cRLzZkt2FnHgw8AiZQ2SWqtVJ6AzfnXMhxNRBb7XdtsRzdUzMc2LdwWPF1PDr9u778NRyaL3TjWnnHiM6 MultisigxV1ae2v9g8JfskVGXegF5NBENe5ZhdSPHhdZXsmjGvRX2bBNmMkZLHrTuaYdS8ijauuVKUrhbHkLotJY6dNS1pYMB3TUk1dPQ3pNp9eNgZeVp673K6LoEPyvYNtPCqL8ZbzX2CNexEPEUTK4QMYneJj3H36LF55nDuNmDgc3HHc9BssgRw1iqNZhwBp9S81rQpGuNTxXibzF9dNExpA72A6oFwnjzUjDyk2NmwfhtdBdWcJKW9MM5MHLemscmN9mVZSvvErA5csgekHq7Tiy1i85vPs2Do6zt8VWkzthFuVed3TLKfxxtvH MultisigxV1JtWDHnVzaRa7BajfTrBXMg2hBeoaprQ54KVzTL8FbZbL5DMGVqfqupbbHTp1dJz8ZhHbAr4J7Tr8x5kxa3WqBpXS5r2eupAEvbSLJngBhFJKP1FU1qW34ZLuUaaLKoP4z7LcBbey5Um52sfF38Qfs23WxjjF37CtoBWRae54JGH938MuiqNZhwBp9S81rQpGuNTxXibzF9dNExpA72A6oFwnjzUjebhKvsXytgMUNUNtXwmVdRDG5dbmeBAD2j38kd8RQ6wZg3vvYeEGakSdpETuq14jRd8ENgeymk7WKQ4mavuTESoo
Wallet password:
[wallet 41fJjQ]: finalize_multisig MultisigxV14VCYeTTq1pB5E1T9rKfQZZA6fUMrZDCNU8jTpSfDkAc4TKNak2DWaaN2naUEHNdUkNGyfuymTEc9s4czUi1BFpDGZnqmPKensZe1qYF4kgqf7G4LxfLkL3h72FvsippCdkbBNmMkZLHrTuaYdS8ijauuVKUrhbHkLotJY6dNS1pYMB3T5DMGVqfqupbbHTp1dJz8ZhHbAr4J7Tr8x5kxa3WqBpXScovQqESipdN9yWukQdnrgYTgaUML1dzPgdc7SSZiK2pW3nZ6msGduCXBjfW4ktSuqgQhtaFgu1Yjk5bnoGXd1xCJ MultisigxV18bgD2HpBVZHAoqUumo532pgVepseKJbZ31eCoQEt577NZnqmPKensZe1qYF4kgqf7G4LxfLkL3h72FvsippCdkbBNwPcL2D2Y166f8FHe2XqjU3UeePdx1Y8oUsS5XY2XECdexEPEUTK4QMYneJj3H36LF55nDuNmDgc3HHc9BssgRw1Bbey5Um52sfF38Qfs23WxjjF37CtoBWRae54JGH938MuPKKvj25cRLzZkt2FnHgw8AiZQ2SWqtVJ6AzfnXMhxNRBb7XdtsRzdUzMc2LdwWPF1PDr9u778NRyaL3TjWnnHiM6 MultisigxV1ae2v9g8JfskVGXegF5NBENe5ZhdSPHhdZXsmjGvRX2bBNmMkZLHrTuaYdS8ijauuVKUrhbHkLotJY6dNS1pYMB3TUk1dPQ3pNp9eNgZeVp673K6LoEPyvYNtPCqL8ZbzX2CNexEPEUTK4QMYneJj3H36LF55nDuNmDgc3HHc9BssgRw1iqNZhwBp9S81rQpGuNTxXibzF9dNExpA72A6oFwnjzUjDyk2NmwfhtdBdWcJKW9MM5MHLemscmN9mVZSvvErA5csgekHq7Tiy1i85vPs2Do6zt8VWkzthFuVed3TLKfxxtvH MultisigxV1JtWDHnVzaRa7BajfTrBXMg2hBeoaprQ54KVzTL8FbZbL5DMGVqfqupbbHTp1dJz8ZhHbAr4J7Tr8x5kxa3WqBpXS5r2eupAEvbSLJngBhFJKP1FU1qW34ZLuUaaLKoP4z7LcBbey5Um52sfF38Qfs23WxjjF37CtoBWRae54JGH938MuiqNZhwBp9S81rQpGuNTxXibzF9dNExpA72A6oFwnjzUjebhKvsXytgMUNUNtXwmVdRDG5dbmeBAD2j38kd8RQ6wZg3vvYeEGakSdpETuq14jRd8ENgeymk7WKQ4mavuTESoo
Wallet password:
[wallet 4222hm]: finalize_multisig MultisigxV14VCYeTTq1pB5E1T9rKfQZZA6fUMrZDCNU8jTpSfDkAc4TKNak2DWaaN2naUEHNdUkNGyfuymTEc9s4czUi1BFpDGZnqmPKensZe1qYF4kgqf7G4LxfLkL3h72FvsippCdkbBNmMkZLHrTuaYdS8ijauuVKUrhbHkLotJY6dNS1pYMB3T5DMGVqfqupbbHTp1dJz8ZhHbAr4J7Tr8x5kxa3WqBpXScovQqESipdN9yWukQdnrgYTgaUML1dzPgdc7SSZiK2pW3nZ6msGduCXBjfW4ktSuqgQhtaFgu1Yjk5bnoGXd1xCJ MultisigxV18bgD2HpBVZHAoqUumo532pgVepseKJbZ31eCoQEt577NZnqmPKensZe1qYF4kgqf7G4LxfLkL3h72FvsippCdkbBNwPcL2D2Y166f8FHe2XqjU3UeePdx1Y8oUsS5XY2XECdexEPEUTK4QMYneJj3H36LF55nDuNmDgc3HHc9BssgRw1Bbey5Um52sfF38Qfs23WxjjF37CtoBWRae54JGH938MuPKKvj25cRLzZkt2FnHgw8AiZQ2SWqtVJ6AzfnXMhxNRBb7XdtsRzdUzMc2LdwWPF1PDr9u778NRyaL3TjWnnHiM6 MultisigxV1ae2v9g8JfskVGXegF5NBENe5ZhdSPHhdZXsmjGvRX2bBNmMkZLHrTuaYdS8ijauuVKUrhbHkLotJY6dNS1pYMB3TUk1dPQ3pNp9eNgZeVp673K6LoEPyvYNtPCqL8ZbzX2CNexEPEUTK4QMYneJj3H36LF55nDuNmDgc3HHc9BssgRw1iqNZhwBp9S81rQpGuNTxXibzF9dNExpA72A6oFwnjzUjDyk2NmwfhtdBdWcJKW9MM5MHLemscmN9mVZSvvErA5csgekHq7Tiy1i85vPs2Do6zt8VWkzthFuVed3TLKfxxtvH MultisigxV1JtWDHnVzaRa7BajfTrBXMg2hBeoaprQ54KVzTL8FbZbL5DMGVqfqupbbHTp1dJz8ZhHbAr4J7Tr8x5kxa3WqBpXS5r2eupAEvbSLJngBhFJKP1FU1qW34ZLuUaaLKoP4z7LcBbey5Um52sfF38Qfs23WxjjF37CtoBWRae54JGH938MuiqNZhwBp9S81rQpGuNTxXibzF9dNExpA72A6oFwnjzUjebhKvsXytgMUNUNtXwmVdRDG5dbmeBAD2j38kd8RQ6wZg3vvYeEGakSdpETuq14jRd8ENgeymk7WKQ4mavuTESoo
Wallet password:
Error: This wallet is already finalized
```
If I run it once and exit the program and re-enter, the wallet will say it is not yet finalized and trying to run `finalize-multisig` again will result in an error message. `Error: Failed to finalize multisig: Failed to generate signer public key`

I am running commit https://github.com/monero-project/monero/commit/6bc0c7e6850d9b35ce48e3a7f494be95f5247604



# Discussion History
## moneromooo-monero | 2018-12-21T21:03:02+00:00
There needs to be n-m+1 data exchanges. However, it should have given you more data to send around for the new data exchange round AFAIK...


## jacoblyles | 2018-12-21T22:15:12+00:00
Is the process to create a m-of-n address documented somewhere? I am unaware of the need for n-m+1 data exchanges. Does a data exchange mean a `make_multisig` step followed by a `finalize_multisig` step? 

For a 3-of-5 wallet, should I be doing (5-3)+1 = 3 or 5-(3+1) = 1 data exchange? 

## moneromooo-monero | 2018-12-21T22:23:46+00:00
AFAIK, it's just extra comms steps, and except from that, identical to N/N and N-1/N, which is documented in the 4c313324b1c80148dff1a8099aa26c51ab6c7e3a commit message.

N/N: prepare_multisig/make_multisig (1 comms round)
N-1/N: prepare/make/finalize (2 rounds)
others: 1 extra round per difference between threshold and total

I did not code the extention to N-x/N with x>=2 so I'm not sure whether the "middle" step should use make or finalize. I'll ask.



## moneromooo-monero | 2018-12-21T22:24:10+00:00
In any case, the behaviour is a bug, just not sure what bug exactly :)

## moneromooo-monero | 2018-12-21T22:34:40+00:00
Going through the source, for N-x (>=2) / N, you have to use exchange_multisig_keys instead of finalize_multisig, which is kept as a proxy for exchange_multisig_keys for backward compat for N-1/N, but it doesn't output the needed data for the next comms round.

So, two things:

- it's a bug, finalize should complain if you use it for M/N with M<N-1

- you should use prepare/exchange and run exchange till it doesn't tell you there's more to exchange.

## moneromooo-monero | 2018-12-21T23:42:16+00:00
https://github.com/monero-project/monero/pull/5004 should fix it. Please confirm.

## jacoblyles | 2018-12-31T23:59:44+00:00
> #5004 should fix it. Please confirm.

Finalize multisig now fails with 3-of-5 wallets and still works with 2-of-3, so this looks good to me! 

## moneromooo-monero | 2019-01-16T20:28:55+00:00
+resolved

# Action History
- Created by: jacoblyles | 2018-12-20T01:15:44+00:00
- Closed at: 2019-01-16T20:49:22+00:00
