---
title: Send page
source_url: https://github.com/monero-project/monero-gui/issues/2405
author: ghost
assignees: []
labels: []
created_at: '2019-10-01T16:09:23+00:00'
updated_at: '2019-11-14T10:19:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`[Updated]` ...aiming to be simple and intuitive ([because it can't be simple enough](https://www.reddit.com/r/Monero/comments/dbnid3/help_with_sending_monero_from_gui_wallet_and_fees/)):

![image](https://user-images.githubusercontent.com/46682965/68848190-3297e100-06d0-11ea-85ad-6bbba1788348.png)
(Transaction time: 95% probability of execution within shown time.)
- Right click shows: 
![image](https://user-images.githubusercontent.com/46682965/68847565-2eb78f00-06cf-11ea-9576-d76410160a52.png)
This is where everybody intuitively is looking for this!

Expanding `More options`:
![image](https://user-images.githubusercontent.com/46682965/68848319-696df700-06d0-11ea-9687-b2777ebfbe51.png)



# Discussion History
## selsta | 2019-10-01T16:54:59+00:00
@Realchacal what do you think of https://github.com/monero-project/monero-gui/issues/740#issuecomment-492886836

Your design doesn’t support sending to multiple recipients.

## ghost | 2019-10-01T20:17:59+00:00
> Your design doesn’t support sending to multiple recipients.

Thx man! I had no clue this is a thing. Fixed.

> what do you think of [#740 (comment)](https://github.com/monero-project/monero-gui/issues/740#issuecomment-492886836)?

That's some excellent ideas! I copied all I like (see updated proposal) but couldn't justify adding any complexity to the default page because we should make it as easy as possible for average users.


## ghost | 2019-10-03T08:06:04+00:00
Updated

## selsta | 2019-10-03T13:41:11+00:00
What do you think about hiding fee settings under advanced? The average user should not change the fee settings.

## ghost | 2019-10-05T06:40:47+00:00
I'd love the simplification but IMO the concept of fees is an integral part of transactions, and users are familiar to it from almost all other coins and wallets.

IMO our problem is that our fee options are not really useful because they don't tell anything about the time or the fee (example: `Fast x5 fee`). Hiding the fee options doesn't solve this. This would solve it:
![image](https://user-images.githubusercontent.com/46682965/66268774-0a030880-e841-11e9-9673-aab1d09a37e9.png)

## rating89us | 2019-11-12T06:14:30+00:00
- Address field could have a placeholder _Send to Monero address... (4.../8.../OpenAlias)_, similar to Exodus wallet (see below), since some users could inadvertently enter a Bitcoin address.
- A CHURN or MY WALLET button could be added in Address field, which would insert the current wallet's main address.
- User should be able to enter the amount in XMR and Fiat (USD/EUR/...)
- If the wallet saves the transaction amount in fiat when the transaction is completed, it could display in Transactions tab the respective amount in fiat (current amount and amount at the time of the transaction).
- Payment ID is being deprecated.
- Description should not be hidden in More options and should have an _(optional)_ mark.
- Multiple recipients should not be hidden in More options. Although it is not widely used in crypto today, we actually want to incentivize users to pay multiple recipients in a single transaction, because its cheaper and decreases blockchain bloat.
- Instead of using a single Max. button in amount, we could use HALF and ALL buttons. Exodus wallet has this option (see below) and its really useful in my opinion.
- When paying for multiple recipients, we could have a SPLIT button, where user type a single amount in first field, clicks the button and the amount is then equally divided for each recipient.
- Regarding displaying available (unlocked) balance (#2298), I believe we should always display it (even in Simple mode), since it is a thing that is really Monero specific, and we're developing an official Monero wallet. If always visible (like Exodus wallet), it could be displayed in small letters at the bottom. When there is a locked balance, we could increase font size and change color to red, to warn user that not all balance is available at the moment.

![image](https://user-images.githubusercontent.com/45968869/68647188-8a421b00-051d-11ea-8084-0db9fb05dcd6.png)


## ghost | 2019-11-12T09:48:39+00:00
> * Address field could have a placeholder _Send to Monero address..._, like Exodus wallet has (see below), since some users could inadvertently enter a Bitcoin address.

Not a problem since the address is checked anyway. But a disadvantage, since it adds visual complexity.

> * A CHURN or MY WALLET button could be added in Address field, which would insert the current wallet's main address.

Please not. This is such a random feature. Don't sacrifice simplicity for that. And if somebody needs it he can still do it without that feature. It's just 2 more clicks then.

> * User should be able to enter the amount in XMR and Fiat (USD/EUR/...)

I guess this is something that certainly many users want. However, I don't see it happening any time soon. Main problem is that the fiat feature is optional and will stay optional for privacy reasons. And I wouldn't want to add complexity to the `Send` page for everybody just to get a small comfort feature for a few users.

> * If the wallet saves the transaction amount in fiat when the transaction is completed, it could display in Transactions tab the respective amount in fiat (current amount and amount at the time of the transaction).

Fiat is just an optional feature. It sucks to add complexity to other pages only for those who use the fiat feature.

> * Payment ID is being deprecated.

k

> * Description should not be hidden in More options and should have an _(optional)_ mark.

The idea is to be simple for new users. If you click "More options" it will remember this for the next time - so you can easily add your description without extra click.

> * Multiple recipients should not be hidden in More options. Although it is not widely used in crypto today, we actually want to incentivize users to pay multiple recipients in a single transaction, because its cheaper and decreases blockchain bloat.

This is such a rare feature. It DEFINITELY must be hidden! The thinking that software should be made in such a way that the user gets forced/ nagged to do something is so wrong. There's millions examples where Microsoft or Apple does such a shitty design only to push their own agenda in some way. This makes users so angry. Rightfully, though. 

> * Instead of using a single Max. button in amount, we could use HALF and ALL buttons. Exodus wallet has this option (see below) and its really useful in my opinion.

Please not! Why would anybody need this anyway!? Even if like 2% of people need this: Why add complexity for the other 98% !?!?!?

> * When paying for multiple recipients, we could have a SPLIT button, where user type a single amount in first field, clicks the button and the amount is then equally divided for each recipient.

Yes, nice. But not nice enough to justify added complexity. Since this is something that also can be done WITHOUT your proposed feature.

> * When there is a locked balance, we could increase font size and change color to red, to warn user that not all balance is available at the moment.

Why bother the user with something that's not relevant for him? It's enough to warn the user that the balance is not available at the moment when he's on the `Send` page.


## rating89us | 2019-11-12T10:38:25+00:00
In my opinion Monero GUI should be designed for all types of users, and our discussions should be based whether we are talking about Simple or Advanced mode. Some features are best suited for Advanced mode, and some are not. I guess your ideas are only focusing on "common" users that would use Simple mode.

"Common" users should use it in Simple mode, which has less visual complexity. I believe _Description_ field, _Send to Monero address..._ placeholder and MAX button should be displayed in this mode. Multiple recipients would also be a nice feature in this mode, since common bank transfers and common bitcoin wallets don't allow this. Fiat conversion should be optional, and should be available in Simple mode.

"Advanced" users should use it in Advanced mode, which could include churn and amount buttons (half and split buttons).

## ghost | 2019-11-12T10:43:00+00:00
Agreed that the best solution would be a **specialized** `Simple mode` and a **specialized** `Advanced mode` - but that's not gonna happen because development effort. In reality our `Simple mode` will just be the `Advanced mode` with some features dropped. And that's why most of your proposed ideas can't be done without adding complexity to the `Simple mode`.

# Action History
- Created by: ghost | 2019-10-01T16:09:23+00:00
