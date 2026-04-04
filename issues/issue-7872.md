---
title: check_tx_key not reporting proper data
source_url: https://github.com/monero-project/monero/issues/7872
author: maxkoda-cpu
assignees: []
labels: []
created_at: '2021-08-16T22:48:23+00:00'
updated_at: '2021-09-01T12:39:26+00:00'
type: issue
status: closed
closed_at: '2021-09-01T12:39:00+00:00'
---

# Original Description
We have an application that verifies payments have been received by our wallet using check_tx_key. This has worked reasonable well until just recently.  We have recently attempted to verify a number of payments using:

check_tx_key <txid> <txkey> <receiving_wallet_address>
and receive back:
Error: <receiving_wallet_address> received nothing in txid <txid>

However, inspection of our wallet transactions shows that the txid in the above check_tx_key error was actually received in our wallet.

Is this a known issue?


# Discussion History
## selsta | 2021-08-17T00:01:06+00:00
Did you restore from seed? Is this a different wallet cache?

## maxkoda-cpu | 2021-08-17T00:13:39+00:00
Yes, it turns out it was in fact a different wallet cache. Thanks.

## maxkoda-cpu | 2021-08-17T03:22:35+00:00
Spoke too soon.
I have a multi-sig wallet that received an incoming payment transaction (some tx data from monero-wallet-rpc "get_transfer_by_txid" call):
"amount": 12560270130000,
"confirmations": 1452,
"locked": false,
"suggested_confirmations_threshold": 14,
"type": "in",
 "unlock_time": 0

However, when I perform a check_tx_key on that monero-wallet-rpc  I receive back:
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "confirmations": 1456,
    "in_pool": false,
    "received": 0
  }
}
(1456 confirmations of a transfer in the amount of 0?)

I would expect the value in "received" in the check_tx_key call to give me the amount specified in the get_transfer_by_txid call. The "amount": 12560270130000 value.

This situation happens with several other incoming payment transactions as well. Whereas the majority of incoming payment transactions work as expected.

Is this a known issue?

I'm seeing several transactions coming into the wallet, where payers are providing the txkey to provide proof-of-payment, where the "check_tx_key" command is failing to verify such proof.

## selsta | 2021-08-18T22:45:11+00:00
Does this only happen in multi sig wallets?

## maxkoda-cpu | 2021-08-19T02:40:37+00:00
> Does this only happen in multi sig wallets?

I don't know. It is just where I'm seeing this issue. I've never seen this happen before in non multi-sig wallets.

## maxkoda-cpu | 2021-08-19T12:49:17+00:00
At this point it looks to be payments sent from the Monero GUI that present the issue described above. Payments sent via monero-wallet-cli have not yet been linked to this issue.

## selsta | 2021-08-19T12:50:10+00:00
Just for clarification, you use the same wallet cache?

If GUI and CLI have separate wallet caches it won't work.

## maxkoda-cpu | 2021-08-20T04:16:59+00:00
> Just for clarification, you use the same wallet cache?
> 
> If GUI and CLI have separate wallet caches it won't work.

Yes.
So I'm using the same monero-wallet-rpc interface to perform check_tx_key and get_transfer_by_txid.
Transactions are received by the multi-sig wallet (the same one the monero-wallet-rpc connects to), and payers provide the txid and txkey to prove they sent a payment to the multi-sig wallet.

Not all proofs provided by payers have issues, but several do show a number of confirmations for the txid and the amount of zero received with the check_tx_key call. On those transfers that have zero received, when I look at them with get_transfer_by_txid they show the correct (non-zero) amount.

Does that make sense?

## luigi1111 | 2021-08-20T19:41:34+00:00
The return for an incorrect txkey looks to be the same as "wrong address"; i.e., the function only checks whether the combination of inputs shows an address received something. It does not check whether the given txkey "belongs" to a transaction.

Therefore, if check_tx_key fails and get_transfer_by_txid succeeds for your address, a reasonable quick conclusion is that the given txkey is incorrect.

I'm not aware of any built-in function that checks whether the txkey is correct for a transaction. It could be checked manually to troubleshoot this particular issue you are having (if it's indeed something else), or the existing function could be improved to distinguish between txkey and address errors.

## defi-monero | 2021-08-20T20:32:34+00:00
I can probably offer some additional insight on this as it affected me as an end-user sending XMR. It seems like a (several?) Monero GUI/Core issue(s).

I confirmed this with another user who had similar problems and they were able to get spend proofs from the CLI, but not the GUI, however they extracted their keys from their Ledger hardware wallet. In both our cases we got garbage spend proofs when we click the 'P' in the GUI. These were not able to give a good signature and were different each time. I was using a Trezor Model T. In my case the GUI froze or was possibly taking too long to respond and I killed the process. Then:
- GUI + CLI: tx_key was missing (this makes sense given the freeze I suppose)
- GUI + CLI: 'Unknown recipient'. CLI will show '-' for the recipient address. See attached.
- GUI: spend proof is garbage and totally different each time. Gives bad signature obviously.
- GUI: Checking tx proof and spend proof with the Advanced tab, nothing happens when the buttons are pressed. In addition, a minor UX bug with spend proof when recipient is entered but not required leaves the button greyed out.
- CLI: get_spend_proof shows 'Error: command not supported by HW wallet'
- GUI: Sometimes won't print the garbage spend proof and shows this error: 'Call method failed.' (maybe due to Trezor being held by another application)

I can provide more images or clarification if needed.
![cli_recipient_xmr](https://user-images.githubusercontent.com/89277299/130290440-06b135ce-1f4e-40ec-be31-b55a823f813a.png)

## selsta | 2021-08-20T20:45:19+00:00
@defi-monero I think this issue is about transactions keys, not spend proofs.

Regarding your issues...

> GUI + CLI: 'Unknown recipient'. CLI will show '-' for the recipient address. See attached.

This is normal if you kill the application before it is able to save after sending / don't have the original wallet cache.

> GUI + CLI: tx_key was missing (this makes sense given the freeze I suppose)

Correct

> GUI: spend proof is garbage and totally different each time. Gives bad signature obviously.

It's possible that the spend proof simply isn't supported by the hardware wallet, as the CLI suggests. There isn't a correct error message in this case.

> GUI: Checking tx proof and spend proof with the Advanced tab, nothing happens when the buttons are pressed. In addition, a minor UX bug with spend proof when recipient is entered but not required leaves the button greyed out.

Correct, that seems to be a bug, will take a look.

## defi-monero | 2021-08-20T21:38:34+00:00
> 
> 
> @defi-monero I think this issue is about transactions keys, not spend proofs.
> 
> Regarding your issues...
> 
> > GUI + CLI: 'Unknown recipient'. CLI will show '-' for the recipient address. See attached.
> 
> This is normal if you kill the application before it is able to save after sending / don't have the original wallet cache.
> 
> > GUI + CLI: tx_key was missing (this makes sense given the freeze I suppose)
> 
> Correct
> 
> > GUI: spend proof is garbage and totally different each time. Gives bad signature obviously.
> 
> It's possible that the spend proof simply isn't supported by the hardware wallet, as the CLI suggests. There isn't a correct error message in this case.
> 
> > GUI: Checking tx proof and spend proof with the Advanced tab, nothing happens when the buttons are pressed. In addition, a minor UX bug with spend proof when recipient is entered but not required leaves the button greyed out.
> 
> Correct, that seems to be a bug, will take a look.

Thank you. Yes it seemed somewhat related and occurred using the application built by @maxkoda-cpu's team. If spend proofs aren't supported by the wallet, I suggest not printing any spend proof in that case, not the randomized data I got back.

Also, how would we confirm a transaction in this scenario when transferring large amounts of XMR for instance? I would have thought that using a hardware wallet was considered best for security and Trezor was one of the first to integrate with Monero. In such an instance as mine it may be possible to never be able to prove ownership of a transaction to a merchant unless you export the keys which compromises security.

## luigi1111 | 2021-08-21T02:29:51+00:00
Key security and proving a payment are different targets, but there's no technical reason I'm aware of that would prevent a HW wallet from proving a payment (given software support).

## maxkoda-cpu | 2021-08-21T03:40:59+00:00
> The return for an incorrect txkey looks to be the same as "wrong address"; i.e., the function only checks whether the combination of inputs shows an address received something. It does not check whether the given txkey "belongs" to a transaction.
> 
> Therefore, if check_tx_key fails and get_transfer_by_txid succeeds for your address, a reasonable quick conclusion is that the given txkey is incorrect.
> 
> I'm not aware of any built-in function that checks whether the txkey is correct for a transaction. It could be checked manually to troubleshoot this particular issue you are having (if it's indeed something else), or the existing function could be improved to distinguish between txkey and address errors.

After looking at our issue in detail, we have several payers providing their txid and txkey in order to prove they made the payment with the end result being the:

{
"id": "0",
"jsonrpc": "2.0",
"result": {
"confirmations": nnnn,
"in_pool": false,
"received": 0
}

as the output from the check_tx_key command. 

Somehow payers are consistently providing incorrect txkeys. We have confirmed through multiple tests, that providing an incorrect txkey paired with a valid txid,  produces the zero received output above.

If the use case is to have individuals send payments using the wallet of their choice, then send the txid and the txkey (to prove they made the payment), and this approach consistently fails because of an incorrect txkey (cause of which is still undetermined), then the result is unacceptable because the payer risks losing their funds.

If faulty software is responsible for providing the payer with an invalid txkey, then in this situation what are the alternatives available to a payer to prove that they made the payment?

That's where the spend proof came into play, as an alternative means of proof. (Mentioned because of incorrect txkeys being provided to payers.) It's a troubling situation when a payment is confirmed received by the wallet, but the payer can't prove they made the payment because they were provided an incorrect txkey - potential risk of loss. The service is put in a bad position, because the service runs the risk of delivering without proof of payment.

So given this repeatable pattern of payers claiming that they made payments which can't be proven because of incorrect txkeys. We are asking payers to provide a valid spend proof, as an alternative for the incorrect txkeys.

## maxkoda-cpu | 2021-08-21T22:28:03+00:00
> I can probably offer some additional insight on this as it affected me as an end-user sending XMR. It seems like a (several?) Monero GUI/Core issue(s).
> 
> I confirmed this with another user who had similar problems and they were able to get spend proofs from the CLI, but not the GUI, however they extracted their keys from their Ledger hardware wallet. In both our cases we got garbage spend proofs when we click the 'P' in the GUI. These were not able to give a good signature and were different each time. I was using a Trezor Model T. In my case the GUI froze or was possibly taking too long to respond and I killed the process. Then:
> 
> * GUI + CLI: tx_key was missing (this makes sense given the freeze I suppose)
> * GUI + CLI: 'Unknown recipient'. CLI will show '-' for the recipient address. See attached.
> * GUI: spend proof is garbage and totally different each time. Gives bad signature obviously.
> * GUI: Checking tx proof and spend proof with the Advanced tab, nothing happens when the buttons are pressed. In addition, a minor UX bug with spend proof when recipient is entered but not required leaves the button greyed out.
> * CLI: get_spend_proof shows 'Error: command not supported by HW wallet'
> * GUI: Sometimes won't print the garbage spend proof and shows this error: 'Call method failed.' (maybe due to Trezor being held by another application)
> 
> I can provide more images or clarification if needed.
> ![cli_recipient_xmr](https://user-images.githubusercontent.com/89277299/130290440-06b135ce-1f4e-40ec-be31-b55a823f813a.png)

To help others that are in a similar situation, could you provide a short description on the process you used to generate a valid spend proof? It appears that the Trezor hardware wallet is a common denominator in this support issue.

## luigi1111 | 2021-08-22T01:26:57+00:00
A potential backup verification method (with obvious caveats) could be the exact amount transferred, as only the payer should know that assuming the viewkey for the address hasn't been published anywhere of course.

A better UX and much reduced support and attack surface would be to provide a separate address (subaddresses) or payment code (integrated addresses, which are partially deprecated) for each payment. However, this does require some pre-payment instead of post-payment communication.

## downystreet | 2021-08-22T02:28:22+00:00
> > The return for an incorrect txkey looks to be the same as "wrong address"; i.e., the function only checks whether the combination of inputs shows an address received something. It does not check whether the given txkey "belongs" to a transaction.
> > Therefore, if check_tx_key fails and get_transfer_by_txid succeeds for your address, a reasonable quick conclusion is that the given txkey is incorrect.
> > I'm not aware of any built-in function that checks whether the txkey is correct for a transaction. It could be checked manually to troubleshoot this particular issue you are having (if it's indeed something else), or the existing function could be improved to distinguish between txkey and address errors.
> 
> After looking at our issue in detail, we have several payers providing their txid and txkey in order to prove they made the payment with the end result being the:
> 
> {
> "id": "0",
> "jsonrpc": "2.0",
> "result": {
> "confirmations": nnnn,
> "in_pool": false,
> "received": 0
> }
> 
> as the output from the check_tx_key command.
> 
> Somehow payers are consistently providing incorrect txkeys. We have confirmed through multiple tests, that providing an incorrect txkey paired with a valid txid, produces the zero received output above.
> 
> If the use case is to have individuals send payments using the wallet of their choice, then send the txid and the txkey (to prove they made the payment), and this approach consistently fails because of an incorrect txkey (cause of which is still undetermined), then the result is unacceptable because the payer risks losing their funds.
> 
> If faulty software is responsible for providing the payer with an invalid txkey, then in this situation what are the alternatives available to a payer to prove that they made the payment?
> 
> That's where the spend proof came into play, as an alternative means of proof. (Mentioned because of incorrect txkeys being provided to payers.) It's a troubling situation when a payment is confirmed received by the wallet, but the payer can't prove they made the payment because they were provided an incorrect txkey - potential risk of loss. The service is put in a bad position, because the service runs the risk of delivering without proof of payment.
> 
> So given this repeatable pattern of payers claiming that they made payments which can't be proven because of incorrect txkeys. We are asking payers to provide a valid spend proof, as an alternative for the incorrect txkeys.

Can you be sure that the incorrect tx keys provided are not just people trying to see if they can game the system?

On a side note I want to suggest adding a note or disclaimer on the bridge website to make people aware that the transaction times can take several hours. Most people don't understand how i2p works and start wondering where their money is if it's not immediate. The information in the facts section states: "Secret Monero Bridge deposits require 6 confirmations on the Monero blockchain before the sXMR will be minted." I've used the bridge a few times and this information has not been correct. It usually takes several hours.

## defi-monero | 2021-08-22T04:16:13+00:00
> To help others that are in a similar situation, could you provide a short description on the process you used to generate a valid spend proof? It appears that the Trezor hardware wallet is a common denominator in this support issue.

That's the thing. I didn't get a valid spend proof. It was garbage each time. See point 3. What I did was click the 'P' icon in the GUI after the GUI froze and the process was killed.

## maxkoda-cpu | 2021-09-01T12:39:00+00:00
After extensive investigation, we have concluded that this issue is attributed to payments made directly with hardware wallets.
The hardware wallets generate invalid txkeys and do not verify payments using the "check_tx_key" command.

# Action History
- Created by: maxkoda-cpu | 2021-08-16T22:48:23+00:00
- Closed at: 2021-09-01T12:39:00+00:00
