---
title: Wallet unresponsive when trying to make a transaction after unlocking the inactivity
  lock
source_url: https://github.com/monero-project/monero/issues/6113
author: erciccione
assignees: []
labels: []
created_at: '2019-11-10T10:34:03+00:00'
updated_at: '2024-03-24T08:22:46+00:00'
type: issue
status: closed
closed_at: '2024-03-24T08:22:46+00:00'
---

# Original Description
Right after unlocking with my password, i get a series of `[wallet XXXX]: [wallet XXXX]: [wallet XXXX]: [wallet XXXX]: [wallet XXXX]: [wallet XXXX]: [wallet XXXX]: [wallet XXXX]: [wallet XXXX]: [wallet XXXX]:`

if now i try to use the `transfer` command the wallet become unresponsive.

**Steps to reproduce:**

1. Open the wallet and wait until the safety lock activates
2. Unlock with wallet password (and notice the series of `[wallet XXXX]:` appearing)
3. Use `transfer` command (eg `transfer 43b7TPk6yRxaeau3zeVsKW4tyMaztEJ1Ag9x79eQDcw71Qe4kXAywgxdeW6UzaQS8kLAMjGRLW9vUYhGfibd4Hc97QqLQYH 1`)
4. Insert password
5. Wallet is now unresponsive. The 'enter' button has no effect and if i press it again i get `Error: invalid password` and right after `Error: Unknown command 'MYPASSWORD', try 'help'` (note that MYPASSWORD is actually my password but without the first and last character)

**System:**
Self compiled v0.15.0 on Debian Buster

# Discussion History
## selsta | 2019-11-10T11:24:04+00:00
Can you test if you get the same behaviour with the getmonero.org release binary?

## erciccione | 2019-11-10T12:00:49+00:00
@selsta. Sure, but I'm going out now. I will be able to test in some hours.

## moneromooo-monero | 2019-11-10T13:05:36+00:00
Sounds like buggy readline.

## erciccione | 2019-11-10T16:52:58+00:00
Just tested with the official binaries and everything went fine (no bug).

@moneromooo-monero i built static binaries using https://github.com/erciccione/monero-static-docker, which is an edited version of the Dockerfile in this repo. If readline is the problem i think would be better to suggest a newer version (now the Dockerfile [uses version 8.0](https://github.com/monero-project/monero/blob/master/Dockerfile#L94)). If that's the issue i could make some tests and suggest a newer version of readline that doesn't create problems.

## hyc | 2019-11-11T00:13:36+00:00
The version of readline isn't the problem. It's how it got built, and which terminfo/termcap library it got linked against, and whether that library includes correct terminal descriptions for the terminal you're currently running on.

# Action History
- Created by: erciccione | 2019-11-10T10:34:03+00:00
- Closed at: 2024-03-24T08:22:46+00:00
