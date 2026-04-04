---
title: '[seeking feedback] wallet selection on GUI startup'
source_url: https://github.com/monero-project/monero-gui/issues/2678
author: tobtoht
assignees: []
labels: []
created_at: '2019-12-22T20:21:22+00:00'
updated_at: '2022-02-05T17:20:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![gui_wallet_selection](https://user-images.githubusercontent.com/41021257/71326364-8678bf80-24f1-11ea-83ec-a7759481c697.gif)

Alternative simplified design with solid background color:

![gui_wallet_selection_alt](https://user-images.githubusercontent.com/41021257/71326757-7ebc1980-24f7-11ea-82ce-d30761d79d82.gif)

It will currently only show up on wallet startup and only display the menu if there is more than one wallet.

Which design do you like better? How can it be improved?
What should the limit on the number of displayed wallets be? 4 or 6?
Should it show up when the wallet is locked due to inactivity?
Only display mainnet/testnet/stagenet information if the user has at least one testnet / stagenet wallet?

# Discussion History
## selsta | 2019-12-23T08:29:51+00:00
Cool idea

> Which design do you like better? How can it be improved?

Maybe it’s the GIF compression but the first design makes it hard to see what is selected, but it also looks slightly better. Not sure yet which version I prefer.

> What should the limit on the number of displayed wallets be? 4 or 6?

4 looks good

> Should it show up when the wallet is locked due to inactivity?

No

> Only display mainnet/testnet/stagenet information if the user has at least one testnet / stagenet wallet?

I guess yes

## rating89us | 2019-12-24T06:19:08+00:00
I don't like it:
- It's not necessary to display many wallets at the same time to choose from, because most users use a single wallet
- Password field is being displayed before the wallet selection
- Ok and Cancel buttons don't cover other problems: I forgot my password. I bought a hardware wallet. I want to create a new wallet. I want to recover my old wallet. etc.
- I wouldn't blur the background, because it seems that the wallet is already open, but locked. I would use an opaque background

Regarding GUI startup, I would do a screen with a UI that is familiar to the common user (similar to a login page of an email service or a traditional bank).

Users usually see the following UI elements:
- `Username` or `Account` field
- `Password` field
- `Forgot your password?` link
- `Sign up` link

Therefore, I would do the following:
Variant 1 (gray links)
![image](https://user-images.githubusercontent.com/45968869/71420951-bbeaed80-2656-11ea-823d-74b57ef2a3ae.png)
Variant 2 (white links at the bottom)
![image](https://user-images.githubusercontent.com/45968869/71419888-bf7b7600-2650-11ea-8deb-d3f0fd59f89b.png)

- `Wallet` dropdown list -> display a maximum of 4 wallet files. Last used wallet selected by default. In case of a testnet or stagenet wallet, display "(testnet)" or "(stagenet)" at the end
- `Password` field
- `Next` or `Open Wallet` button
- `Forgot your password?` link -> open Main Menu. In the future, we could redirect users directly to restore wallet page (from seed or keys), we just need to know if the user is trying to restore a common wallet or a hardware wallet
- `Use another wallet?` link -> open Main Menu, so that user can create a new wallet, open a different wallet file or restore a wallet.

Regarding wallet lockup due to inactivity, I would do a simple unlock wallet screen:
![image](https://user-images.githubusercontent.com/45968869/71421423-754ac280-2659-11ea-8a46-d6a2b1e4789e.png)
- `Password` field
- `Close wallet` button (+ icon) -> Open Main Menu or GUI startup (see above)
- `Unlock` button (+icon)

## SamsungGalaxyPlayer | 2019-12-28T14:54:04+00:00
Maybe some compromise here is best. I think it's worth adding the wallet type, forgot password option, and create a new wallet option to the list of requirements.

To this, I suggest the following:

1. Move the wallet cards to the top above the password. Change the fourth card (bottom right) to a + logo and the text "open or create another wallet", "use another wallet", or similar. This will only show 3 wallets instead of 4 but will keep the grid.

2. Drop the separate variant for timeout lock. Why do we need two separate screens?

3. In all cases, change "ok" and "next" to "unlock" wording.

4. Have the most recent wallet clearly auto-selected.

5. Change "cancel" to "close wallet" or similar.

## rating89us | 2019-12-28T17:31:59+00:00
> Drop the separate variant for timeout lock. Why do we need two separate screens?

Unlocking has a different meaning from opening a wallet. When you have a locked wallet, the wallet is still open in the background. When the user sees the unlock wallet screen (that is different from the wallet selection in startup), he knows that his wallet was locked because of inactivity (and not because someone closed his wallet when he was away).

> In all cases, change "ok" and "next" to "unlock" wording.

We could change "Next" to "Open wallet", or just use a button with a right arrow (->) and no text.

## GBKS | 2020-01-16T17:49:40+00:00
<img width="2348" alt="monero-log-in-gbks-200116" src="https://user-images.githubusercontent.com/695901/72549139-735ad480-3890-11ea-85cd-72bf8641d778.png">

How about something like this? It's consistent with the layout and UI elements in the onboarding screens. Here's the [Figma link](https://www.figma.com/file/DplJ2DDQfIKiuRvolHX2hN/Monero-GUI?node-id=24%3A5416).

I do like the feel of the initial design, but also agree with some of the feedback.

## ITwrx | 2022-02-05T17:20:26+00:00
A select/dropdown for wallets above the password field as @rating89us  has proposed is what i was going to propose and is better UX, IMO. No need for fancy selection boxes. Just more mouse movement for little/no benefit, except it is subjectively nicer looking, which i de-prioritize compared to unneeded mouse movements/clicks.

I would change the wording of the "use another wallet?" link, as it is confusing because that's what the drop down allows. Maybe something like "other wallet options" or "more wallet options" or similar.

All that said, i would rather not be asked for the password just to open the GUI as mentioned in #3834

thanks


# Action History
- Created by: tobtoht | 2019-12-22T20:21:22+00:00
