---
title: 'Fiat balance: Suggestions for further enhancements'
source_url: https://github.com/monero-project/monero-gui/issues/2368
author: kayront
assignees: []
labels: []
created_at: '2019-09-01T08:14:18+00:00'
updated_at: '2019-09-06T13:14:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Since #2322 has already been closed (a bit late to the party), here are my thoughts on the matter.

1. It seems to me that it is a very good idea to have the option to display the fiat balance: this is something that, whether we like it or not, people *need*. If not on-wallet, then from some external source: it would be unwise to transfer any amount of volatile cryptocurrency without knowing the present exchange rate with traditional fiat.

2. The fact that the wallet clearly warns that the user's IP will be exposed is well thought out, and a (simple) step above mostly any other wallet that I have seen.
**However**, it can be even better: there is somewhere in the wallet an option to toggle proxy support, yes? That being the case, just make the price check connection go through the proxy; And inform the user clearly that this is the case and that their privacy has been thought about. Related to this, I don't know when the first price check is triggered (on enabling the option?), but care should be taken not to expose the user's IP before he's had a chance to configure a proxy (or not).

3. Regarding displaying the fiat balance, first of all in my opinion this is the best version (but see below):

![img](https://user-images.githubusercontent.com/46682965/61965606-e0bc3580-afd0-11e9-9ca1-781363cf630f.png)

My main contribution to point 3 would be the following. Get rid of both the yen/euro sign *and* the little expandable menu shown above.

In my opinion, for your consideration, it would look a lot better if:

  - The "main" balance display (the bigger letters, presumably above the "secondary", "XMR" in the case above) can be XMR, but it could also be swapped for a configured fiat currency -- or in other words, if the user so chooses, the fiat currency display could become the "main" one displayed on the wallet.

  - Under the "main" balance display, and rather than using the little toggle menu shown in the image above, the "secondary" currency is shown, in smaller letters. The advantage of this method is that the user no longer needs t constantly hit a toggle or a button to compare XMR value with desired currency.

  - In order to enable the functionality described in the two points above, there has to be a way to select which fiat currency the user is interested in displaying. Since the idea is eliminating toggle menus and extra buttons, the first thing that comes to mind is relegating that preference to the settings window, but then it can get cumbersome to swap currencies (out of curiosity, for practical purposes that don't come to mind right away, etc). **So how about this**: Create a new section in settings where the user *can* choose which altcurrencies will be available, and then when the user clicks the "XMR" (image above), the "main" currency gets swapped for altcurrency1, one more click and altcurrency2, one more and back to XMR: meanwhile XMR, for as long as the "main" currency is an altcurrency, gets displayed below as "secondary", with smaller letters. Once back to/when XMR is set as "main" currency, the "secondary" becomes clickable, and the GUI will cycle between the chosen (from settings) altcurrencies.

  - Another suggestion is to not just stop at fiat currency! Allow the user to choose Gold, Silver, and even Bitcoin as altcurrencies.

Thoughts?

# Discussion History
## ghost | 2019-09-01T09:27:59+00:00
**Could we please agree** that we discuss **balance card-related UI stuff** in #2298, while this issue here is used to discuss the **backend changes** you're proposing?

## ghost | 2019-09-06T09:33:06+00:00
The first concrete step in this direction would be adding more currencies:
![image](https://user-images.githubusercontent.com/46682965/64417033-a1393c80-d098-11e9-8cbc-b821a2688d77.png)
We support 30+ languages, but 2 fiat currencies.

@kayront Could you maybe delete the balance card-related parts in your 1st comment for better clarity?

# Action History
- Created by: kayront | 2019-09-01T08:14:18+00:00
