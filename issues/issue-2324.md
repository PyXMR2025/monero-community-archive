---
title: Wallet options not clear anymore since hardware wallets were introduced
source_url: https://github.com/monero-project/monero-gui/issues/2324
author: ghost
assignees: []
labels: []
created_at: '2019-07-27T06:25:16+00:00'
updated_at: '2020-01-06T16:49:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[Updated!]

Quick & dirty proposal:
![image](https://user-images.githubusercontent.com/46682965/64247906-1f1e0c00-cf10-11e9-8701-c6781031438d.png)

Good proposal:
![image](https://user-images.githubusercontent.com/46682965/65371900-db920480-dc68-11e9-8e19-6fef42415a6c.png)
This would be in accordance to #2328, which doesn't create the impression that there's a difference between _creating_ and _restoring_ a wallet from hardware.





# Discussion History
## selsta | 2019-07-27T16:12:31+00:00
4 times “Choose this option”, is this an improvement?

## ghost | 2019-07-27T16:41:18+00:00
Thank's for your feedback!! Updated!

## selsta | 2019-07-27T16:46:54+00:00
I’m not happy with the 3rd one.

“Choose this option if you have used Monero before”, can be confusing. You can have used Monero on a different computer before.

What about: “Choose this option to open an existing Monero wallet from your computer.” ?


## ghost | 2019-07-27T16:55:44+00:00
Your argument is good! What about leaving "from your computer", though? (Could be from USB-stick as well)
--> "Choose this option to open an existing Monero wallet." ?

## selsta | 2019-07-27T16:56:43+00:00
Ok. I’ll wait on other opinions before I implement it though.

## ghost | 2019-07-27T17:00:08+00:00
Sure! Updated.

## rating89us | 2019-07-28T14:24:06+00:00
Some considerations:
- "Create a new wallet" is intended only for users that don't want to use a hardware wallet.
- "Open a wallet from file" can be used both for users that have and don't have hardware wallets
- "Restore wallet from keys or mnemonic seed" can only be used for Monero wallets that don't support hardware. Ledger/Trezor users can't type device seed in this page. Also, hardware wallets don't inform their private keys to users.

So, I believe there should be a clear separation: do you want to use a Monero wallet with a hardware wallet or not?

**Use a Monero wallet without a hardware wallet:**
- **Create a new wallet** (_for users that just want to create a new Monero wallet that doesn't support hardware wallet. Hardware wallets can't import wallet files that were created in this page_)
- **Open a wallet from file** (_for users that have a wallet file that doesn't support hardware wallet_)
- **Restore wallet from keys or mnemonic seed** (_for users that want to restore from their keys/mnemonic seed_)

**Use a Monero wallet with a hardware wallet:**
- **Create/restore a wallet from hardware wallet** (_for users that have never created a Monero wallet from device OR lost their wallet file and want to restore it from device_)
- **Open a wallet from file** (_for users that already created their wallet file from hardware wallet_)

Some users might want to recover using Trezor/Ledger mnemonic seed, but this is not possible in Monero GUI. So **Create/restore a wallet from hardware wallet** page should inform that first they have to recover their Trezor/Ledger with mnemonic seed, and then use this page to restore their wallet from device.

@cslashm and @ph4r05 : 
Imagine I lost my device (Ledger/Trezor) after creating a Monero wallet file (.keys) from it. I then buy a new device and recover my device with my previous mnemonic seed. Will the old Monero wallet file (.keys file) work with this new hardware wallet device (recovered from previous mnemonic seed)? Or user must create a new wallet file for each new device?

## ghost | 2019-07-28T15:38:08+00:00
I like your clear distinction between with/without hardware wallet! Very logical. But as always, it's a **trade-off** how much text we're willing to accept. So I guess the optimal solution depends on how popular hardware wallets are. Any estimates? 10% of our users? 90% of our users?

## rating89us | 2019-07-28T15:50:08+00:00
We could either put everything on current page, or we could break all these options into two pages (with and without hardware wallet) and add an extra page to select if you want to use a hardware wallet or not.

![image](https://user-images.githubusercontent.com/45968869/62009490-19d6e000-b160-11e9-81fc-de8f24aefb08.png)



## ghost | 2019-07-28T17:00:19+00:00
Your proposal to make it 2 different pages (plus a 3rd page before) is **very logical** but not necessary with regard to the reasons you gave. I will go through them:

> "Create a new wallet" is intended only for users that don't want to use a hardware wallet.

True, but the option for hardware wallets is **directly** below. That's super clear.

> "Open a wallet from file" can be used both for users that have and don't have hardware wallets

True! I just added that info (see update) Thanks.

> "Restore wallet from keys or mnemonic seed" can only be used for Monero wallets that don't support hardware. Ledger/Trezor users can't type device seed in this page. Also, hardware wallets don't inform their private keys to users.

True, I just added "or restore" to row 2 (see update) Thanks. (And by the way: The GUI never intended to directly support seeds from hardware wallets. That would break the point of hardware wallets if you entered the seed directly into your computer.)

## ghost | 2019-07-30T06:56:29+00:00
Alternative proposal added. Thanks @rating89us for input.

## rating89us | 2019-07-30T08:41:38+00:00
Hardware wallet icon should include both Ledger and Trezor (Model T).
![image](https://user-images.githubusercontent.com/45968869/62114250-8bc13d80-b2b6-11e9-88cd-f3cfbd5f358a.png)


## ghost | 2019-07-30T09:23:16+00:00
That would look like this:
![image](https://user-images.githubusercontent.com/46682965/62116859-350a3280-b2bb-11e9-9005-091d7c297720.png)

- I don't like the added visual complexity.
- I don't like that we would have to add icons whenever new hardware wallets are supported.
- The icons don't tell which model exactly is supported (Nano S or Nano X? Trezor 1 or Trezor T?) So the user would have to check that anyways somewhere else.

## ph4r05 | 2019-08-06T16:13:44+00:00
> @cslashm and @ph4r05 :
> Imagine I lost my device (Ledger/Trezor) + my Monero wallet file (.keys) that was created from my device. I then buy a new device and recover my device with my previous mnemonic seed. Will the old Monero wallet file (.keys file) work with this new hardware wallet device (recovered from previous mnemonic seed)? Or user must create a new wallet file for each new device?

When you recover device from the mnemonic seed, the existing wallet files will keep working. Trezor holds no state related to the Monero wallet (besides the seed) thus different devices with the same seed can be used interchangeably.  

## cslashm | 2019-08-07T17:01:58+00:00
> @cslashm and @ph4r05 :
> Imagine I lost my device (Ledger/Trezor) after creating a Monero wallet file (.keys) from it. I then buy a new device and recover my device with my previous mnemonic seed. Will the old Monero wallet file (.keys file) work with this new hardware wallet device (recovered from previous mnemonic seed)? Or user must create a new wallet file for each new device?

Yes it will. 
Also note that Ledger provide tools to convert your *24 words of your NanoS/X* into *ELectrum 25 words* usable to restore your wallet as a full software wallet (without HW)


## rating89us | 2019-11-12T10:03:17+00:00
> I don't like the added visual complexity.

So let's remove all hardware wallet icons. There is no reason to only have Ledger icon.

Supported hardware wallet models have been added in #2694.

# Action History
- Created by: ghost | 2019-07-27T06:25:16+00:00
