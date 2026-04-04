---
title: Improvements for page "Create a new wallet using a hardware device".
source_url: https://github.com/monero-project/monero-gui/issues/2328
author: ghost
assignees: []
labels: []
created_at: '2019-07-30T12:27:05+00:00'
updated_at: '2019-11-21T14:22:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently:
![image](https://user-images.githubusercontent.com/46682965/64472273-fbe79c80-d15b-11e9-8e53-f311bf121cba.png)

- The user panics, thinks: **"WTF, I need the wallet creation date to restore my wallet?!?"**
- Mandatory inputs should come first, optional inputs second.
- The labels `Wallet name` and `Wallet location` could be misinterpreted as "Specify the name and the location of the existing wallet that you are trying to restore." (Noobs...)
- One could wonder if the "restore height" is the `wallet creation block height` or the `current block height` minus `wallet creation block height`.
- `YYYY-MM-DD` does not need backticks for clarity.
- `YYYY-MM` is precise enough and explains without words that the exact date is not relevant.
- Text boxes should not be 10 times larger than the expected input.
- We create the (false) impression that `Create a new wallet` and `Restore a wallet` are 2 different things while they are actually the same thing and the difference is just that in the latter case the blockchain is also scanned for funds.
- `Wallet creation date` isn't correct - `First transaction` is. (This is not about being nit-picky, it's about giving the user a chance to understand the logic behind it!)

Proposal (updated with input from @GBKS and @selsta):
![image](https://user-images.githubusercontent.com/46682965/64533880-b4584080-d314-11e9-99d9-fec1bf6cb656.png)
This would be in accordance with #2324 ("Good proposal").

______________________

If adopted, the following (small) changes would be also needed:
- In `Settings` > `Wallet` > `Show seed` replace the term "Wallet restore height" by "Wallet creation block height".
- On the regular wallet creation page (without hardware wallet) replace the term "Wallet restore height" by "Current block height"
- On the regular restore page (without hardware wallet) change the wording accordingly to this proposal (to be consistent).



# Discussion History
## GBKS | 2019-07-31T13:45:27+00:00
I agree that this need so be simplified. "Restore height" made no sense to me initially, I didn't even realize it was about block numbers, and didn't know what the relevance of this option even was. "Wallet creation date" would work. The GUI can always start scanning the blockchain 1-2 days earlier than what the user entered, as a bit of a failsafe.

The "not" in "Wallet created not before" really throws me off. It's a bit like those "Don't uncheck this checkmark if you don't not want to unsubscribe".

How about simplifying to just month and year and get rid of the date? It's a bit less precise, but easier to remember.

## ghost | 2019-07-31T13:55:18+00:00
@GBKS These are some excellent points! Agreed on all and updated! Please let me know if the update does not match your vision or if you have further ideas! Thanks!

## dEBRUYNE-1 | 2019-07-31T15:58:24+00:00
>How about simplifying to just month and year and get rid of the date? It's a bit less precise, but easier to remember.

We can default to the height of the first day of the month, that should cover all cases and should not visibly affect user experience (scanning ~20k additional blocks more at most takes a few minutes).  

## ghost | 2019-07-31T16:12:49+00:00
> ...that should cover all cases

Yes, but potential time zone issues if you've created on the 1st of a month and travel a lot or algorithm is bad. So maybe generously add another 24 hours safety margin?



## ghost | 2019-08-01T09:46:21+00:00
Alternative proposal added. Looking for feedback.

## selsta | 2019-08-03T08:53:22+00:00
Why is it marked as optional?

## ghost | 2019-08-03T08:55:42+00:00
> Why is it marked as optional?

If the user does not remember when he created the wallet, he can leave this field blank. Then the whole blockchain will have to be scanned.

Also: "Optional" helps to explain and takes away all anxiety, which a user may have from this option. It prevents the user from panicking. He does not go: "WTF, I need the wallet creation date to restore my wallet!?! Nobody told me that when I created it!!!!"

## selsta | 2019-08-06T21:31:56+00:00
What do you think about moving “Choose your hardware device” above the radio buttons? It would make more sense as it is mandatory, changing the radio button selection isn’t.

## ghost | 2019-08-06T21:36:51+00:00
@selsta You are absolutely right that would make a lot of sense!!

Proposal updated!

## rating89us | 2019-11-16T11:14:17+00:00
The "select your hardware wallet" field could be removed if Monero GUI auto-detected in this page whether a Trezor or a Ledger is plugged in. 

Normally the Monero GUI tries to detect the device when you go to the next page, but it could be done in the current page.

Instead of "select your hardware wallet" field there could be a status text field:
- "Detecting..." (while trying to detect the device every 5-10 seconds)
- "No hardware wallet detected. Please connect your device." (in red)
- "Hardware wallet detected: Trezor" (in green)
- "Hardware wallet detected: Ledger" (in green)

The button to proceed to the next page should only be enabled when the device is detected.

## rating89us | 2019-11-16T11:22:30+00:00
"First transaction" field should be hidden by default, and should only be displayed if the box "My hardware wallet already holds Monero" is checked. AFAIK, a new wallet without previous transactions never syncs the whole chain, it starts at the end.

## ghost | 2019-11-17T21:36:20+00:00
> "First transaction" field should be hidden by default, and should only be displayed if the box "My hardware wallet already holds Monero" is checked.

100% agreed! Nice!



## rating89us | 2019-11-18T01:11:46+00:00
I'm against changing "Wallet creation date" to "First transaction", even though first transaction is a more precise term (it's what the wallet really detects when scanning the blockchain):
- Wallet creation will always be on the same date of first transaction or before. Yes, some users may do their first transaction 6-12 months before creating the wallet, but I guess they're the minority.
- The wallet asks users to write down date and block height when they are creating the wallet, and not when the first transaction is done.
- Many users already have paper backups with "wallet creation date" written down. Changing terms would bring confusion.

## ghost | 2019-11-18T06:28:05+00:00
> I'm against changing "Wallet creation date" to "First transaction", even though first transaction is a more precise term (it's what the wallet really detects when scanning the blockchain):
> 
> * Wallet creation will always be on the same date of first transaction or before.

Not really. Just think if you are restoring your wallet your 2nd, 3rd time...  Users will have no clue which date to enter. And they have no chance to figure it out themselves by logical thinking because "wallet creation date" is just wrong. Or think of compatibility to other software: In the future seeds hopefully will be widely compatible between different wallets. One wallet tells users to enter "first date of transaction", the other wallet to enter "wallet creation date". WE will be blamed because WE'RE doing it wrong.

> * The wallet asks users to write down date and block height when they are creating the wallet, and not when the first transaction is done.

So if there's a mistake in 2 places this is like saying: "let's not correct the mistake in one place because then it would be inconsistent to the other place". - We don't need to tell users anything during the installation process since this feature is optional after all. Or we could tell the user just how it is! "If you need to restore your wallet in the feature, it may be helpful to know the approximate date of your first transaction to speed up the restore process. If you remember the approximate date of your wallet creation, you'll be fine, too." or something like that. 

> * Many users already have paper backups with "wallet creation date" written down. Changing terms would bring confusion.

So we'll be carrying mistakes around forever in order to not confuse early adopters?



## GBKS | 2019-11-18T08:39:54+00:00
I'd move this to "Advanced" and call it "Date of first transaction (optional)". To avoid confusion, we can some short explanatory text, either below the label or accessible via a "?" or "Help". We can 

Most of these options cannot be clearly explained to newcomers with 1-3 word labels, so we need a mechanism to get more details inline.

Does "My wallet already holds Monero" make sense if you have to choose to create a new one or import an existing one earlier? New wallets can't hold any yet, and I'd assume the default for existing ones would be that they already have a balance.

## ghost | 2019-11-18T09:45:47+00:00
> I'd move this to "Advanced" and call it "Date of first transaction (optional)". To avoid confusion, we can some short explanatory text, either below the label or accessible via a "?" or "Help". We can

100% agreed

> Most of these options cannot be clearly explained to newcomers with 1-3 word labels, so we need a mechanism to get more details inline.

Yes.

> Does "My wallet already holds Monero" make sense if you have to choose to create a new one or import an existing one earlier? New wallets can't hold any yet, and I'd assume the default for existing ones would be that they already have a balance.

Very right. That's why this proposal does not talk about "Create NEW wallet" but instead it says "Create wallet", which is in accordance with #2324. By the way: The term wallet is wrong in general. "Keychain" (or "Keysfile") would be correct. A real (physical) wallet can't be copied and if you lose it your funds are gone. A real keychain can be copied and if you lose it your funds in the volt are not gone as long as you still have a copy of the keychain (or the data to create a new keychain). That's why it should be called "Keychain" (or "Keysfile") instead of "Wallet".

## GBKS | 2019-11-18T14:38:44+00:00
Yeah, wallet is just a nice metaphor people can make sense of (like a trash can for deleting files). It's always been weird to "download a wallet" and then "create a wallet", with wallet referring to totally different things. I think wallet should be the software you download and set up (or configure), and the keys are what you use to configure it. And either you have keys, or you generate them. But there are lots of opinions on these things...



## rating89us | 2019-11-21T13:27:35+00:00
"_Save wallet to_" should be moved to Advanced options in this page.

Common users probably will not want to move/backup/save this file in a directory different from the default.

Advanced users may want to move/copy the file to use it in CLI wallet.

When using a hardware wallet with Monero GUI, having the device physically is mandatory, but having the wallet file is not.

And, if lost or deleted, the wallet file can always be recovered later from the device. So the common hardware wallet user shouldn't worry about the location of this file.

# Action History
- Created by: ghost | 2019-07-30T12:27:05+00:00
