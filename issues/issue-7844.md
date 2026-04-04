---
title: sweep_all on a viewing wallet often embeds a wrong destination address.
source_url: https://github.com/monero-project/monero/issues/7844
author: crocket
assignees: []
labels: []
created_at: '2021-08-10T02:14:13+00:00'
updated_at: '2022-04-21T01:42:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If I executed `sweep_all` on a viewing wallet and tried to sign `unsigned_monero_tx` on an offline wallet, most of the time, the offline wallet would sign transfer to a wrong address which is always

> 46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU

I don't know where this address came from.

`sweep_all` sometimes embeds the correct destination address. `transfer` always embeds the correct destination address in `unsigned_monero_tx`.

# Discussion History
## moneromooo-monero | 2021-08-10T19:01:43+00:00
Does it send a non zero amount to it ? When there's no change (as in sweep_all), a dummy output is added, sending 0 to what is supposed to be a random address.

## crocket | 2021-08-10T22:27:31+00:00
It tried to send the full amount. I could have lost a lot of money.

## Tzadiko | 2021-10-16T00:53:46+00:00
I remember I ran a `sweep_all` several years back, it did indeed send dummy-change to a second address. Are you sure this is not what is going on? I doubt `sweep_all` is sending your founds to the wrong address. @crocket

## crocket | 2021-10-16T02:04:15+00:00
There is no address that starts with `46uz` in my monero wallet.

## Tzadiko | 2021-10-16T02:06:56+00:00
> There is no address that starts with `46uz` in my monero wallet.

That is correct. `46uz` is a random address unassociated with your wallet. When you sweep_all, you send all your funds to the destination address, and a dummy output with 0 XMR is sent to a random address (in this case `46uz`).

## crocket | 2021-10-16T02:07:53+00:00
Perhaps, I should update monero wallet on my offline machine.

## Tzadiko | 2021-10-16T02:10:45+00:00
> Perhaps, I should update monero wallet on my offline machine.

Can you check that the funds you sent with a sweep_all has actually arrived at the address specified?

## crocket | 2021-10-16T02:13:40+00:00
They arrived at the specified addresses in the past, but I didn't broadcast any transaction that tried to send everything to
> 46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU

because I didn't want to risk my money on a bug.

## Tzadiko | 2021-10-16T02:41:08+00:00
> They arrived at the specified addresses in the past, but I didn't broadcast any transaction that tried to send everything to
> 
> > 46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU
> 
> because I didn't want to risk my money on a bug.

Feel free to test with a cold wallet that has 0.001 XMR.

## crocket | 2022-01-01T08:04:46+00:00
This issue occurred when I ran sweep_all to check transaction fee and ran sweep_all again to create an unsigned transaction.
I have to run sweep_all twice because cryptocurrency swap service requires an exact amount to be sent.

## crocket | 2022-01-01T09:40:52+00:00
sign_transfer

> Loaded 1 transactions, for 0.010000000000, fee 0.000007240000, sending 0.009992760000 to 46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU, 1 dummy output(s), no change, with min ring size 11, dummy encrypted payment ID. 2 outputs to import. Is this okay?  (Y/Yes/N/No): y

submit_transfer

> Loaded 1 transactions, for 0.010000000000, fee 0.000007240000, sending 0.009992760000 to 46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU, 1 dummy output(s), no change, with min ring size 11, dummy encrypted payment ID. 52 key images to import. Is this okay?  (Y/Yes/N/No): y

## crocket | 2022-01-01T09:53:24+00:00
monero-wallet-cli pretended to send XMR to

> 46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU

But, it actually sent XMR to the correct destination XMR address.

How can it happen? Why does monero pretend that it is sending XMR to the following address?

> 46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU

I think monero-wallet-cli should not display random addresses as destinations because it doesn't actually send XMR to

> 46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU

## crocket | 2022-01-01T10:05:57+00:00
This is what submit_transfer looks like for `transfer`.

> Loaded 1 transactions, for 4.464275520000, fee 0.000009800000, sending xxxxxx to some XMR address (46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU with encrypted payment id xxxxxx), xxxxxx change to some XMR address, with min ring size 11, encrypted payment ID xxxxx. 52 key images to import. Is this okay?

## alt4weirdXMRaddress | 2022-04-21T01:13:50+00:00
Hello! I ran into this same mysterious Monero address (`46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU`) earlier in a different situation. Because this GitHub issue is the only search result online for the address, and since this issue is still open, I thought to share what I did in case that might help figure out whatever is going on. 

I had come across the address while authorizing a transaction using my Ledger Nano X on Monero Wallet GUI version 0.17.3.1-release. Here are the steps to reproduce:

1. Set up a Ledger Nano X with the Monero app installed, and create a new _wallet from hardware_ inside Monero Wallet GUI. Send some money to the Ledger address. 
2. Initiate a trade from Monero to another currency on the exchange FixedFloat (fixedfloat.com). For my specific example, my trade was 0.01 XMR to BTC, but anything should work as long your starting currency is XMR.
3. Use Monero Wallet GUI to start writing a transaction to send to the address FixedFloat provides. In the case of my test, the address they provided was `4GcfBn8eCbYfhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht4gt1c95mE9nGbmU62N`.
4. Proceed with signing the transaction as normal up until the Ledger device shows the destination address confirmation prompt. The address shown on the Ledger's screen will be the mysterious address in question `46uz ... 1QQU`.

My guess is that the address `46uz ... 1QQU` belongs to FixedFloat, who embeds certain payment IDs in the addresses to differentiate them internally. That's probably what the "encrypted payment id" is (from the last reply to this issue). If you look at the address that FixedFloat gave me and the strange Monero address in question, they are actually exactly the same except for the beginning and end:
`4GcfBn8eCbYfhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht4gt1c95mE9nGbmU62N
46uzAyK9bL2fhMz32Y5PW3diQR6CXNo2dVEgP8cvqUvjVqLCGabtEidMGCo7BWATJ2KSrykxQ5RnGKqUFJKoTsht3Z51QQU`.

Furthermore, I suppose that there's a bug in the Ledger hardware wallet application that causes the device to display the "base" address without the embedded payment ID. However, I haven't studied Monero's internals closely (and I don't think my terminology is even correct), so I can't say any of this for certain; it's just a guess.

I hope this helps!

## alt4weirdXMRaddress | 2022-04-21T01:42:01+00:00
I found this relevant issue on the GitHub page for Ledger's Monero app: LedgerHQ/app-monero#66 Unfortunately, it seems to be inactive.

# Action History
- Created by: crocket | 2021-08-10T02:14:13+00:00
