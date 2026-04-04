---
title: monero-wallet-cli
source_url: https://github.com/monero-project/monero/issues/7316
author: spitrip82
assignees: []
labels: []
created_at: '2021-01-13T06:10:29+00:00'
updated_at: '2022-02-19T00:45:36+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:45:36+00:00'
---

# Original Description
hello 
after accessing monero-wallet-cli  ./monero I started mining with the command: start_mining (my wallet adress) 1
after starting to mine I ran the command: mining_status 
and the result was this :

mining_status
Mining at 101 H/s with 1 threads
PoW algorithm: RandomX
Mining address: 44AQ4WuLq9UYVaSyQBDMgT5y7ETxZ1enBLbjaXu4B8jgGXTZVKFV4GBVuKEqQyD1baGAzUX8dcs3PhkEV4eHXkSESGKsFrn
Expected: 0.000045739943 monero daily, 0.001395068269 monero monthly, 0.016283419795 yearly
 
my question is, how will I be able to see how many moneros I've already made and when will I receive it in my wallet?

# Discussion History
## moneromooo-monero | 2021-01-16T18:02:30+00:00
You'll get an incoming tx in your wallet whenever you mine a block.
As this rate though, it'll be with an expected time to a block of about... 1.2/0.016283419795 == 73 years. It's a lottery, and you don't have many tickets. Good luck!

# Action History
- Created by: spitrip82 | 2021-01-13T06:10:29+00:00
- Closed at: 2022-02-19T00:45:36+00:00
