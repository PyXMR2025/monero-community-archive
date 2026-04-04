---
title: '[CLI] Can''t transfer from cli with payment_id on v0.14.0.2'
source_url: https://github.com/monero-project/monero/issues/5279
author: gituser
assignees: []
labels: []
created_at: '2019-03-13T12:43:25+00:00'
updated_at: '2019-11-25T20:11:44+00:00'
type: issue
status: closed
closed_at: '2019-11-25T20:11:44+00:00'
---

# Original Description
Hi. 

When trying to make a transfer on `v0.14.0.2` with payment_id (16 hex symbols) cli errors:

```
transfer xxx 0.5 1234567890abcdef
Wallet password:                                                                                                                                                                                           
Error: Invalid last argument: 1234567890abcdef
```

Same transfer via JSON-RPC perfectly works.

# Discussion History
## gituser | 2019-03-13T13:13:56+00:00
Ping @moneromooo-monero 

This is quite urgent because many users are using CLI instead of GUI to transfer monero.

## moneromooo-monero | 2019-03-13T13:18:29+00:00
This is not a valid payment id here. It was previously possible to send with a short payment id, but this was a bad idea. Short payment ids are embedded inside an integrated address, and are not meant to be used "free". I'll fix the RPC to disable those too.

## moneromooo-monero | 2019-03-13T13:19:11+00:00
And... is there an exchange actually asking for a freeform short payment id ? Which one ?

## gituser | 2019-03-13T13:22:46+00:00
What do you mean not valid payment_id?
Well I can provide you with a valid payment_id (which was generated via monero-wallet-rpc) but it doesn't work either.

Here is an example:
```
[wallet yyy] integrated_address
Random payment ID: <4f8dd5f06b0cb492>                                                                                                                                                                      
Matching integrated address: xxx
```

Now transfer:
```
[wallet yyy]: transfer xxx 0.5 4f8dd5f06b0cb492
Wallet password:                                                                                                                                                                                           
Error: Invalid last argument: 4f8dd5f06b0cb492
```

## gituser | 2019-03-13T13:24:05+00:00
>And... is there an exchange actually asking for a freeform short payment id ? Which one ?

Yes, there is, but not freeform, rather generated via wallet's integrated address.

And I'm sure there are still many exchanges relying on payment_ids instead of subaddresses as the transition is not that easy and well documented with examples in all programming languages.

## moneromooo-monero | 2019-03-13T13:35:43+00:00
It's not a valid free form payment id. They should be 32 byte (64 hexadecimal characters). The command you posted clearly gives you an integrated address for that random short payment id. If a recipient gives you just the short payment id, ask them for the actual integrated address.

## gituser | 2019-03-13T13:44:46+00:00
So, to re-iterate now:
1. 16 byte (32 hexadecimal characters) payment_id is only valid for integrated address
2. 32 byte (64 hexadecimal characters) payment_id is only a valid payment_id if used with the regular address combination
3. Default GUI and CLI only accept integrated address as of `v0.14.0.2`
4. If you tick in the GUI an option `use OBSOLETE payment_id` it will work again and display a field for sending transactions with payment_id
5. Is there any option for CLI to make the same behavior of transfer command?

Regarding integrated address instead of regular address + payment_id yes we're working on this.

## moneromooo-monero | 2019-03-13T13:51:42+00:00
8 byte (16 hex) are only valid when inside an integrated address. Those still work fine.
32 byte ones are obsolete, and can be used freeform.
32 byte ones can only be used to send if --long-payment-id-support in the CLI, and I think the GUI has a check box for this.
--long-payment-id-support


## gituser | 2019-03-13T13:53:48+00:00
Thank you!

## gituser | 2019-08-04T17:22:59+00:00
There are multiple issues with the new monerod `v0.14.1.2`:

* i can't send anymore transactions with payment_id 8 byte (16 hex) - and there is no option to make it possible to send such even if I send correct standard address and specific payment_id which both combine into integrated address. i have app logic which always sends via address and payment_id, so if user submits integrated address it gets split into standard address + payment_id and i no longer can send to such address.
* there is no option for `monero-wallet-rpc` `--long-payment-id-support` to send 32 byte (64 hex) payment_id transactions, the only option i can see there is for `monero-wallet-cli`, however 64 hex payment_ids work just fine with` v0.14.1.2`

## moneromooo-monero | 2019-08-19T17:00:42+00:00
As I said above, standalone payment IDs are 256 bit (32 bytes), not 8/16. Fixed size. Or do you mean you can't send to an integrated address ? I *assume* that when you saud monerod you mean the monero wallet, not monerod. If you really meant monerod, please confirm.

As for monero-wallet-rpc, AFAICT it does not need a --long-payment-id-support flag currently, as those are enabled by default. If something is not working there, please be specific.


## gituser | 2019-08-19T20:22:40+00:00
@moneromooo-monero every integrated address have a usual address + payment_id (16 hex).

So if we split the integrated address into the standard address + payment_id we are not able to send a transaction - getting an error.

If we use integrated address instead - it works.

It's just that sometimes users specify standard address + payment_id instead of the integrated address.

And yes I meant `monero-wallet-rpc`.

## moneromooo-monero | 2019-08-20T10:56:21+00:00
Yes, that is all correct, except that for "sometimes users specify standard address + payment_id instead of the integrated address" those users are doing it wrong.

## moneromooo-monero | 2019-08-27T15:17:09+00:00
Everything is as expected AFAICT. Using 8 byte payment ids manually was an unfortunate misfeature which was corrected. I'll close this soon unless you can point to something that's actually a bug.

## gituser | 2019-08-27T19:13:21+00:00
@moneromooo-monero ok, closing this one, thanks for the clarification once again.

## gituser | 2019-11-24T23:03:56+00:00
Hi @moneromooo-monero 

I have the issue with v0.15.0.0:

When I try to transfer to regular Monero address + 32 byte (64 hex or 256 bit) payment_id I get this error:

```
'result' => 
  array (
    'code' => -5,
    'message' => 'Standalone payment IDs are obsolete. Use subaddresses or integrated addresses instead',
  ),
```

I do not see `--long-payment-id-support` in `monero-wallet-rpc` binary and before the upgrade it did work just fine. 

Can you fix this or add this option as many of our users still send to exchanges which require regular monero address + 32 byte (256 bit) payment_id (64 hex)

## moneromooo-monero | 2019-11-25T01:24:22+00:00
There's no command line support option anymore. This will not be added again. It would defeat the purpose of tiered obsoletion. People should migrate when it *starts* being deprecated, not after it is eventually removed. Those users can send to themselves or somewhere which does not require plaintext payment ids,

## dEBRUYNE-1 | 2019-11-25T08:49:49+00:00
@gituser - It has been known for quite some time that long payment IDs would be phased out this year (basically with the upcoming scheduled network upgrade of November 30). See:

https://web.getmonero.org/2019/06/04/Long-Payment-ID-Deprecation.html

## gituser | 2019-11-25T09:50:10+00:00
@moneromooo-monero it seems to me that it's too early that you closed this function.

Many exchanges are still relying on payment_id, why not make additional option until everyone migrates to the integrated address / subaddress? 

It's not a default option just an optional for those who still rely on payment_id's.

@dEBRUYNE-1 I know about that I'm just saying that right now it's too early to cut this ability off completely as top players didn't migrate yet.

## hyc | 2019-11-25T11:40:25+00:00
> it seems to me that it's too early that you closed this function.

Exchanges have literally had over 5 months to migrate. You should be complaining to your exchanges that they've waited so long to migrate, this is all their responsibility to fix.

## gituser | 2019-11-25T11:54:45+00:00
@hyx I understand your position, but the reality is: exchanges are very slow to implement such changes, e.g. Binance still requires payment_id for the address. 

And many users won't be able to transfer with this new monero version.

For those who are having this issue and want to quickly fix it here is a patch I made (based on the other commit by @moneromooo-monero):

https://gist.github.com/gituser/28610a676df7bf7a8a2c2610f94da0c4


## selsta | 2019-11-25T12:07:08+00:00
Binance confirmed that they will upgrade before November 30.

## gituser | 2019-11-25T12:11:16+00:00
@selsta the reason that we've updated earlier in order to test the new monero version and not to miss the network upgrade and got this issue.

Thanks for the info regarding Binance.

## xiphon | 2019-11-25T12:17:46+00:00
> Exchanges have literally had over 5 months to migrate

Even more, they actually have had 9 months to migrate.
Long payment ids are marked obsolete since [Boron Butterfly v0.14.0.0 release 25 Feb 2019](https://github.com/monero-project/monero/releases/tag/v0.14.0.0).

## moneromooo-monero | 2019-11-25T13:25:10+00:00
What exchange are you running, so we know which one is actively trying to prevent privacy improvements from being adopted in monero by making patches meant to counter them ?

## gituser | 2019-11-25T20:02:56+00:00
@moneromooo-monero  you probably misunderstood me.

We're runnning not exchange but instant exchange service. And from the start we've integrated monero without payment_ids (when nobody knew about this feature). The issue is only for users who are exchanging through us to withdraw to 3rd party exchanges which are not supporting yet integrated addresses but requiring payment_id.

It's not my call to stall the upgrade, it's our users demand. Hopefully after November 30 everyone will upgrade and we will remove payment_id support on our exchange form as we don't like it either.

We're happy to get rid completely of payment_id's when everyone will stop supporting them, but for now we have to maintain this functionality because there are still other services requiring payment_id's unfortunately :(

Thank you.

## gituser | 2019-11-25T20:11:44+00:00
I'll close the issue as there is a workaround for now for some time until everyone will be supporting payment_id's.

# Action History
- Created by: gituser | 2019-03-13T12:43:25+00:00
- Closed at: 2019-11-25T20:11:44+00:00
