---
title: '[Proposal] - optionally reduce user impact of locked XMR'
source_url: https://github.com/monero-project/monero-gui/issues/2059
author: ronohara
assignees: []
labels:
- invalid
created_at: '2019-04-08T11:26:23+00:00'
updated_at: '2019-04-08T12:45:49+00:00'
type: issue
status: closed
closed_at: '2019-04-08T12:45:49+00:00'
---

# Original Description
And idea to improve the usability of Monero wallets


6th April 2019 - Ron OHara


This proposal comes from a Reddit discussion on r/Monero. 

=========================================================================

It was prompted by a comment by some Dash supporter (on Zerohedge) who correctly points out that the outputs from Monero transactions are 'locked' for 10 blocks about 20 minutes. This can create the perception that Monero is slower than BTC or Dash and is often used as a negative aregument against Monero.

I have encountered this myself - and chose to simply wait ...   However, searching through r/Monero I found the reason behind this constraint, and a well known work around for it.
That prompted this idea.


The workaround is to simply split your 'balance' in the wallet into two values... just by sending half of the value to yourself. After doing this and waiting 20 minutes, your wallet now holds two unspent outputs.
You now make two consecutive transactions in the future in rapid succession... as long as the values of those transactions are less than half your balance.

Effectively you have created as small pool of available fund denominations and although you 'lock' one them when you use it, the other(s) are still immediately available for spending. The change from the locked first transaction becomes part of the pool again after 20 minutes..

One issue with using multiple inputs that were simple parts of a split up, is that it can potentially leak information.



To quote  u/dEBRUYNE_1:

/quote

A split transaction may be vulnerable yes if the outputs are subsequently combined. For instance, if you have split transaction 1 with outputs A B C D E (all to yourself) and you subsequently combine A B C for a new transaction, some information will be revealed / leaked that can be detrimental to your privacy. The wallet will provide a clear warning if you attempt to do this though.

I asked: What information gets revealed in that scenario ?


[–]dEBRUYNE_1
It increases the possibility of the input being the real one.


/end quote

Note that the vulnerability is to analysis, not loss of funds.

=========================================================================

Proposal.

I propose that we enhance the reference wallet(s) to support an easy (optional) automatic way to hold a pool of unspent values to implement the workaround in a simple manner for users. This would avoid possible user errors who are trying to set up the scenario.

The proposal is to allow this, but **not** make it the default approach. That ensures that the default approach the wallet takes is exactly the same as the current approach.

At present, by default, a wallet tends to hold a single unspent output from the value sent to it. If you then spend some of that output, the change amount returns to the wallet, so there is still only one available output and that is locked for the next 10 blocks.  If you send extra funds to the wallet, then there will be two unspent outputs. As you spend against those values, you will often be able to just use one of them as input, so you may not need to wait for the change amount to unlock before your next transaction. However, if you spend an amount that needs both available inputs, you end up encountering the 'locked' funds interval again.   IE. Normal usage tends to consolidate the funds into a single unspent output, and whenever you reach that situation the 'locked' time becomes relevant to the usability of your funds.

If we introduce a parameter to tell the wallet to maintain a minimum of 'x' unspent outputs, then the number of times the user will encounter the 'locked funds' issue will be substantially reduced. Clearly, the wallet should avoid creating dust outputs, so there should also be a minimum value for whatever the wallet does when it chooses to create extra outputs to achieve that continuous pool of available outputs.


Real world usage of 'wallets' ....

There are probably lots of wallets being used for only small total values. And if market uptake increases a lot, then the average wallet balance will mirror the sort of balance profile that banks have for their accounts ... mostly low balances ... and low balance accounts have the highest number of transactions.... Eg. My cheque account does lots of small purchases, but only has a small balance. My savings account has a higher balance, and does very few transactions.

so in the cheque account style sort of wallet profile, there would more often be a need to combine inputs - at least 2 rather than just selecting a single input. This might have some better setup possible... Eg. 5 possible inputs with nowhere near equal amounts. A wallet structure suitable for frequent small purchases, where the number inputs is greater than 1 on a bigger percentage of occasions, but almost never with the same number of real inputs.


This points to use cases where I can envisage a multiple wallet setup  ... with different profiles.


Wallet style one - ultra private.. the current approach. Does have locked funds, but no vulnerability along the lines identified.

Wallet style two - savings style wallet... any size balance. 3 inputs available - allows 3 transactions in a 20 minute window... very little vulnerability.

Wallet style three - normal spending style wallet, 5 inputs available, suitable for smaller balances... rarely gets the locked funds issue, but is mildly more likely to be vulnerable to analysis

That would leave the risk selection up to the user - and hence market forces... with the default being the same purist option that we have right now.



So the XMR wallet could be better by offering a range (or set) of utility choices versus privacy risk choices.

This proposal makes some suggestion for three different profiles - not mutually exclusive. I would probably set up three wallets. One of each style and use them accordingly.





One problem all crypto currencies have right now is that many design decisions are centralised - normally unavoidable. But where possible it is helpful to allow the market decide what is useful ... centralised decision making is unfortunately vulnerable to co-option or coercion, and vitriolic politics.



=========================================================================

Worked example. The savings style wallet.


This uses the A,B,C,D,E sort of notation that u/dEBRUYNE_1 uses in the referenced Reddit discussion...

For the suggested savings style wallet, it is 'always hold 3 outputs in a wallet' ... and this sort of depends on the total available funds versus the normal usage profile of the user.



So - assume I accept 100 XMR into my wallet... single unspent output. Then buy a Google Home speaker .... about 2 XMR at the time of writing. My wallet spends the 2 XMR and splits up the 98 XMR change into 3 outputs.

For arguments sake. A=33 B=33 C=32


I decide to buy another 30 minutes later - A,B and C are all possible choices, the wallet just uses 'A' ... and decides that it only needs the change in one output to ensure there are 3 outputs in the wallet.

now A=31 (waiting to unlock) B=33 C=32


I immediately buy another speaker. Only B and C are available, so the wallet picks B ... and still only needs to have one change output to have three to choose from for the next transaction.

now A=31 (waiting to unlock) B=31 (waiting to unlock) C=32

etc.


Obviously you can run out of unlocked funds, but this allows multiple transactions quickly ... depending on your usage patterns.

This example allows up to 3 rapid transactions of up to 30(ish) XMR for any given transaction.... without encountering the risk mentioned at the start.

Obviously if you just consolidated everything in your wallet (A,B,C) in a transaction, that risk applies. But this is not a new risk - it has always been there if you have multiple available outputs in a wallet.

What it does do is increase the frequency that this occurs - because instead of only some users who set up their wallet manually generating multiple inputs of their own funds... now many users will occasionally generate this type of transaction. But you still can not isolate these sorts of transactions... and for normal usage, most transactions are likely to be 1 input and 10 decoys. But without the 20 minute delay.

The wallet should also probaby try to use unspent outputs that are unlocked, but were created as a by product of a split, whenever it is generating a transaction with only single change output. That way, these 'split' outputs tend to be removed from the wallet quickly, and the risk disappears entirely once all (bar one) of the 'split' outputs have been used.

If need, the GUI wallet could emulate the Coin Control facility that the Bitcoin-Qt wallet has.... offering advanced users precise control of inputs.



=========================================================================

Thoughts on the analysis vulnerability that was highlighted by u/dEBRUYNE_1


The original advice was from a time when the ring size was small and variable ... and correctly put the self input consolidation as a risk at de-cloaking the real inputs to a transaction. The risk was fairly big at that time.

But - with many more decoys, this risk has become negligible ... 1 of 11 ..... and that means that even 2 of 11 is nowhere near what used to be an accepted level of risk. My guess 3 inputs is ok too - and only used when you empty your wallet or need to take more value than can be satisfied by 1 or 2 inputs immediately after a 'split' - so probably very rare.

So ... a little more often than currently, take a risk that is almost certainly less than was normal Monero practice in the recent past.

And this remains optional... the default should be to have a wallet profile exactly as it currently is.

So for those who want it, they have an automated way to work past the 'locked funds' issue - and only if they deliberately choose it. The wallet can provide educational warnings about the risk.


Automating this also removes much of the possible errors that people probably make when attempting this manually.



In the simplistic worked example of buying Google home speakers.... there is actually never multiple (connected ?) inputs .... A,B,C were all created as a split, but never joined again. And even when the change from the second transaction gets spent at a later date, it is not the original split ... it is a new output ...

This pattern would go on, and on, and on ...if your spending pattern is below the values that would force combining inputs.

And if you have spent in single input transactions the original 'split' A, B, C values .... then you end up with a wallet holding 3 unrelated outputs ... the change amounts from your early transactions. Adding a new transfer of value into the wallet further extends the pool of available outputs...

So this sort of pattern would quickly eliminates the privacy issue entirely for a particular wallet - yet still provides relief from the 'locked funds' user issue on an ongoing basis for that wallet.

Remember that you can not generate a transaction graph to connect the change values to the original 'split' transaction.

The risk of having a set of outputs (say 3) that reveal anything, is obviated as soon as you do small transactions to use the pool members once (or more)... so it remains that the risk the u/deBRUYNE_1 identifies exists, but only for the first one or two transactions after an automated 'split' occurs .... and that becomes a very rare event for a wallet.

Statistical review of real usage patterns is need to determine the real risk level.

I suspect that the trade offs here are valuable - with no compromise on the core of Monero

=========================================================================


References.

You can read the original discussion at: https://np.reddit.com/r/Monero/comments/b8gbqu/usability_issue_with_wallets/



# Discussion History
## sanderfoobar | 2019-04-08T12:38:37+00:00
This issue tracker is for the GUI though, not Monero internals. We (GUI) generally follow CLI in terms of wallet functionality. You'll have more luck posting at https://github.com/monero-project/monero. In addition, I think `#monero-research-lab` or `#monero` is the right place to discuss such ideas first. 

Please note Github supports [the markdown format](https://daringfireball.net/projects/markdown/syntax), which would make your proposal more readable.

+invalid

# Action History
- Created by: ronohara | 2019-04-08T11:26:23+00:00
- Closed at: 2019-04-08T12:45:49+00:00
