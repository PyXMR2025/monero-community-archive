---
title: Back after 3 years ! Very frustrating! Please help!
source_url: https://github.com/monero-project/monero/issues/2050
author: pbx001
assignees: []
labels: []
created_at: '2017-05-26T06:13:39+00:00'
updated_at: '2018-11-01T18:21:11+00:00'
type: issue
status: closed
closed_at: '2017-08-09T10:12:14+00:00'
---

# Original Description
Hi folks, i'm having major problems trying to transfer my 26 monero over to poloniex.. Just cant get it to work, and been spending hours and hours reading & trying different syntax.  I gathered my coins mining them about 3 years ago, if that makes any difference.

_Balance: 26.172142172202, unlocked balance: 26.172142172202_
sync is up to date

trying - 
> `transfer 4 <address> <amount> <paymentID>`
Error: not enough outputs for specified mixin_count = 4:
output amount = 0.003561077853, found outputs to mix = 1
output amount = 0.002990241943, found outputs to mix = 1
output amount = 0.000064521083, found outputs to mix = 3
output amount = 0.000999936999, found outputs to mix = 1
output amount = 0.001629974443, found outputs to mix = 1

etc..etc.. for about 25 more lines. 

Ive also tried different mixin's

`sweep_unmixable` gives me the following:
Sweeping 2.730303258823 in 3 transactions for a total fee of 0.251282244772.  Is this okay?  (Y/Yes/N/No): y
Error: transaction <713c6e880a777c0ebca99be6d033722d732d51a336e8787556127c500ab34fbc> was rejected by daemon with status: Failed
Error: Reason: fee too low

`sweep_all <my current wallet address>` is giving me the following;
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
Error: not enough outputs for specified mixin_count = 4:
output amount = 0.001070977178, found outputs to mix = 1
output amount = 0.000669376409, found outputs to mix = 1
output amount = 0.002207226320, found outputs to mix = 1
output amount = 0.002425004042, found outputs to mix = 1
output amount = 0.000324117462, found outputs to mix = 1
output amount = 0.003024624761, found outputs to mix = 1
output amount = 0.000889203213, found outputs to mix = 1
output amount = 0.000388440536, found outputs to mix = 1
output amount = 0.000388156938, found outputs to mix = 1
output amount = 0.000472452184, found outputs to mix = 1
etc...etc..


Any help would be greatly appreciated!  having this problem with latest monero-wallet-cli.exe and also the latest GUI wallet... i'm using windows.


# Discussion History
## moneromooo-monero | 2017-05-26T08:32:59+00:00
This is not a support channel, but bug tracker.
That said...
"fee too low" hints you're using an old wallet and/or daemon. Use 0.10.3.1 only now.
Then run sweep_unmixable
Then run sweep_all 2 POLOADDRESS POLOPAYMENDTID

The sweep_unmixable might fail, there's a known bug atm. You'll have to wait till next release if you hit it.
You will also have large fees, as you seem to have lots of tiny inputs. Try "set priority 1" first. When all done, back to "set priority 0".

## moneromooo-monero | 2017-08-09T10:09:44+00:00
The only bug here was sweep_unmixable using the wrong mixin, and that got fixed already.

+resolved

## lacksfish | 2018-11-01T18:21:11+00:00
Mining on a private testnet, I came across this error when trying to sweep a couple thousand blocks of block rewards:

```
[wallet 9wviCe]: sweep_all BZg53n1EgLJhYDZNCi3VvxXFMdmmgk6HhhFCvvw9sMf1RQFp7LyjGvrNuF7TzukfaGh7Gsin2bEDpUNRv9oc8qSGMKCnktw
Wallet password:
Error: not enough outputs for specified ring size = 11:
output amount = 0.100000000000, found outputs to use = 1
output amount = 80.000000000000, found outputs to use = 3
output amount = 500.000000000000, found outputs to use = 8
output amount = 70.000000000000, found outputs to use = 1
output amount = 0.300000000000, found outputs to use = 4
output amount = 400.000000000000, found outputs to use = 2
output amount = 9.000000000000, found outputs to use = 5
output amount = 90.000000000000, found outputs to use = 3Please use sweep_unmixable.
Password needed (output received) - use the refresh command
[wallet 9wviCe]: sweep_unmixable BZg53n1EgLJhYDZNCi3VvxXFMdmmgk6HhhFCvvw9sMf1RQFp7LyjGvrNuF7TzukfaGh7Gsin2bEDpUNRv9oc8qSGMKCnktw
Wallet password:
Sweeping 951.339515923395 in 11 transactions for a total fee of 1.034000000000.  Is this okay?  (Y/Yes/N/No): Y
Error: transaction <3fa55c130ae9b4963be27a5ce7062fa9cb8fa3f97350e4aff314b39688028728> was rejected by daemon with status: Failed
Error: Reason: fee too low
```

Then I used    
> set priority 1

Which then resulted in:
```
[wallet 9wviCe]: sweep_unmixable BZg53n1EgLJhYDZNCi3VvxXFMdmmgk6HhhFCvvw9sMf1RQFp7LyjGvrNuF7TzukfaGh7Gsin2bEDpUNRv9oc8qSGMKCnktw
Wallet password:
Sweeping 951.339515923395 in 3 transactions for a total fee of 0.7
11230240000.  Is this okay?  (Y/Yes/N/No): Y

Transaction successfully submitted, transaction <2626e039e9b6dedf7
af0cf8dc7fdf40e899c84eb3a765b0f0d17440e829bb72b>
You can check its status by using the `show_transfers` command.
Transaction successfully submitted, transaction <4f462f11885235c92
be74522d31791c380912448433db8b09605a8005c398f5a>
You can check its status by using the `show_transfers` command.
Transaction successfully submitted, transaction <9e6537be4ea1b0d72
4135ba81a872d240fdfcc055597069d45afbdf7f02bcc0c>
You can check its status by using the `show_transfers` command.
```

I'm also mining as I'm doing this, so a later hardfork might have resolved this? Odd that the fees are suddenly lower...

# Action History
- Created by: pbx001 | 2017-05-26T06:13:39+00:00
- Closed at: 2017-08-09T10:12:14+00:00
