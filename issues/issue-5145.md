---
title: Protecting Monero's untraceability when large numbers of private view keys
  are disclosed to light-wallet servers
source_url: https://github.com/monero-project/monero/issues/5145
author: knaccc
assignees: []
labels: []
created_at: '2019-02-14T17:35:39+00:00'
updated_at: '2022-04-27T20:53:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is a discussion thread to spark thoughts related to protecting privacy (of users disclosing their private view keys) and untraceability (of all Monero users generally) when large numbers of private view keys are disclosed to light-wallet servers.

If only the private view key `a` is known, a light-wallet server can do the following:

1. For each output on the blockchain, calculate a per-output shared secret `ss=Hs(8aR||i)G`
2. (a) Use `ss` to attempt to decrypt the output amount as `decrypted amount = 32 byte encrypted amount - Hs(Hs(ss))`; or
(b) Use `ss` to attempt to decrypt the output amount as `keccak("amount" || ss) XOR 8-byte encrypted amount`
3. If 2(a) or 2(b) result in decrypted amounts that are small enough to look like typical XMR amounts (e.g. amounts less than 100,000 XMR), guess that this output is almost certainly destined for the user's wallet.
4. (a). If the user had received the output to a standard or integrated wallet address, the user's full wallet address can be calculated as the `(public view key A, public spend key B)` pair `(aG, P-Hs(8aR||i)G)`. All wallet subaddresses can now be determined, since the private view key `a` and public spend key `B` are known.
(b). If the user had received the output to a subaddress, the user's main wallet spend key `B` can be recovered as `B = P-Hs(8aR||i)G-Hs("SubAddr" || a || account_index || subaddress_index_within_account)G`. Again, this means that all of the user's subaddresses can now be determined.

To sum up, disclosing only a private view key `a` will result in the disclosure of all wallet addresses and subaddresses, and the ability to determine all outputs and output amounts owned by the wallet.

This means that light-wallet servers will have knowledge of vast amounts of output ownership data, which through blockchain analysis is a threat to Monero's untraceability promise and to the privacy of the individual users of that service.

Partial Solution
----------------

Change the amount encryption scheme so that it is `encrypted amount = keccak("amount" || ss || address/subaddress spend key B/D respectively) XOR 8-byte encrypted amount`.

Now, a  light-wallet server with knowledge of the private view key cannot attempt to determine likely owned outputs by examining the output amounts, because this would require knowledge of the user's public spend key.

In order for the user's wallet to learn about outputs from a light-wallet server (where the light-wallet server did not know the user's public spend key), a scheme such as the following would need to be employed: the light-wallet server would calculate the first two bytes of `P-Hs(8aR||i)G` for each output on the blockchain, and send a list of these bytes to the user's browser or other light client. For a blockchain consisting of 25 million outputs, this would amount to 47MB of data that would need to be sent to the client during a full wallet refresh.

The client would then attempt to match each of these sets of two bytes with the first two bytes of each of the user's wallet's list of subaddress public spend keys. Only the user's wallet would know the list of subaddress public spend keys. This would inform the user's browser/light client which outputs to request further information about. The client could do this by asking for information about far more outputs than the specific outputs of interest. For a blockchain of 25 million outputs, matching only the first two bytes would result in approx 380 false positives.

Note that subaddress public spend keys are currently calculated as `D = B + M` where `M = Hs(a || i)G`. This means that the light-wallet server could, with knowledge only of `a`, calculate `M_1` and `M_2` (the first two `M` values in the first two subaddresses in a user's wallet), and then see if the difference between the calculation `P-Hs(8aR||i)G` for any two outputs on the blockchain is equal to `(M_2 - M_1)`. If so, the light-wallet server now knows that both outputs are owned by the user, and can recover the user's public spend key `B` as `B = P-Hs(8aR||i)G-M_1` for one of the outputs. This then allows the light-wallet server to determine all of the user's subaddresses and then all outputs for the wallet on the blockchain. It also allows the light-wallet server to discover the amounts of all of those outputs.

To fix this, `M` would need to be calculated as `M = Hs(a || B || i)G` instead. Now the light-wallet server cannot calculate `M_1` and `M_2`, and so the user's public spend key `B` is protected and the amounts of all user outputs are protected, even in the situations where the light-wallet server could guess that the user owns those outputs.

Result
------

It is now no longer possible for the light-wallet server to discover the amounts of any outputs received.

Output ownership would not be disclosed in cases where only a single output has been received to each address (unless either the user's main wallet address was known or the specific subaddress for those outputs was known). If multiple outputs had been received to any particular address or subaddress, the light-wallet server would notice the results of `P-Hs(8aR||i)G` being the same in each case, and can thus deduce that the user must own both of those outputs.

If a large list of wallet addresses was leaked from e.g. a merchant, then the light-wallet server could easily take each known private view key `a` and check if it matches any of the leaked wallet main addresses (by matching `aG` against the public view key of each address) and can see if the private view key matches any subaddress (check if `C == aD` for each subaddress).

This solution therefore could still result in the leak of the ownership of large numbers of outputs, but now only if a list of compromised private view keys were to be combined with a list of compromised wallet addresses.

This partial solution is therefore an improvement on the existing situation, but is still far from being a perfect solution. It is much more effective if users use subaddresses frequently, rather than having all of their outputs all arrive to the same address.

# Discussion History
## JustFranz | 2019-02-15T00:03:41+00:00
 (sorry, not dealing with the main issue, but it came to mind when reading this)

Regarding use of subaddresses can this be improved by changing the GUI somehow? Because Monero is a work in progress and imperfect and it seems to have an ethos of sorts (privacy) AND people can reduce their and everybody elses privacy through uninformed use, should the wallet be a source of education or is it acceptable if the wallet forces or guides people to use best practices? Even at the expense of jank?

_What follows is a stream of consciousness consisting of flawed to very flawed and incredibly raw ideas._

Do we need to have the main address be as prominent as it is? What should your Monero wallet or address be to you? Your wallet should be your 24 word phrase + passphrase. Do you need a main address? Can't your "address" or money receiving function be the functionality of the GUI?

The GUI is getting a merchant window, should it also get a Charity/Donation window? The donation window would reveal subaddresses, that window/subaddresses would behave like they do now. You reveal one and name it, then give it out and its just there.

The real addition and change would be a "personal money window". That window will deprioritize the main address (hide it?) and prioritize subaddresses. You'll be given some subadresses, when you get a transaction to one of them then the wallet will somehow mark it so that it is signified as spent for receiving or giving out again. If the subaddress had funds once and is now empty, it gets hidden.

If you need to receive a salary or some other recurring payment then you give it out once, receive payments and never copy+paste it anywhere else (this should be signified somehow).

Addresses will be listed in order of 

1. unnamed subaddress with no transactions (constantly 3 available)
2. named subaddressed with no transactions
3. subadresses with balances in order of last transaction received
4. subadresses with transactions but no balances, in order of balance last spent (hidden by default)

You'll also have advanced filtering and search functions for keeping track of finances. Search by name, address, amounts shown and dates.


When restoring from seed, subadresses 0-throughout-50 should be considered donation subaddresses (if restore height is after height of the respective change), before that idk. If you need to then you can allocate more addresses to donations, on each wallet restore you need to do it again.

For older wallets, donation addresses will be last used subaddress (by index, transaction received = used) + 20 (for buffer) -throughout-next 50.  (this is so bad, its making me dizzy)


Is there anything we can do in the GUI to educate people and encourage + favor the use of best practices regarding privacy?

## knaccc | 2019-02-15T06:48:39+00:00
@JustFranz I agree that someone with no prior cryptocurrency/Monero knowledge will struggle to understand how/why they need to issue subaddresses rather than just having one "bank account number". If you do decide to produce any wireframe/mockups that do a significantly better job of explaining this, I think people would be very interested. That UX discussion would definitely belong on another thread though, I'd like to keep this thread to the discussion of the private view key disclosure problem.

## knaccc | 2019-02-15T13:43:01+00:00
FYI I just made an edit to the main post above, adding in a rationale for altering the subaddress creation to include the public spend key. It's the last two paragraphs of the "Partial Solution" section that have been added.

## moneroexamples | 2019-02-16T01:24:23+00:00
> This means that light-wallet servers will have knowledge of vast amounts of output ownership data, which through blockchain analysis is a threat to Monero's untraceability promise and to the privacy of the individual users of that service.

The knowledge of the viewkey also allows to make good guesses about key images and spend outputs. That's how light wallets based on mymonero api work. Thus the more viewkeys is in control of a single party, good chunk of spendings can be "guessed" and cross-correlated with each other to even further improve the guesses.

## UkoeHB | 2022-04-27T20:53:43+00:00
Another possible solution is [Jamtis](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024), where remote scanning gets the 'find-received key' that can only filter outputs with view tags (1 byte = 1/256 filter) and match nominal spend keys (no decrypting amounts). The client uses their 'view-balance key' to finish the work started by the remote scanner, starting with a cheap decipher of an 'address tag' (which is an encrypted version of the address index that owns the output, with a 1 or 2 byte MAC that further filters the candidate set).

# Action History
- Created by: knaccc | 2019-02-14T17:35:39+00:00
