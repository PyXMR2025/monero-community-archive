---
title: 'Monero Tech Meeting #117 - Monday, 2025-04-21, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1190
author: rbrunner7
assignees: []
labels: []
created_at: '2025-04-20T05:56:43+00:00'
updated_at: '2025-04-21T18:25:09+00:00'
type: issue
status: closed
closed_at: '2025-04-21T18:25:08+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1187).

# Discussion History
## rbrunner7 | 2025-04-21T18:25:08+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1190
<r​brunner7> Thankfully the Monero matrix server is fast again ...
<s​needlewoods> hey
<r​brunner7> But maybe some people still searching for their hidden Easter eggs :)
<r​brunner7> Anyway, something to report from you, SNeedlewoods ?
<j​berman> *waves*
<j​berman> me: completed the FCMP++ blinds cache (implemented serialization to save pre-calculated blinds to the wallet cache), implemented composition changes prior discussed (hash y coords in the leaf layer in addition to x coords), implemented comments on latest PR's for bannig torsion at consensus and modifying the PoW hash for FCMP++, and did some debugging in the torsion checking crypto code. Continuing this week reviewing jeffro's PR on FCMP++ / Carrot transaction weight and taking a look at FCMP++ fees (will likely discuss with @articmine once I'm further along in my looking into)
<r​brunner7> I saw tobtoht reporting new tx creating times middle last week, with release build instead of debug build, which look very promising: 1-in: 1.2s, 2-in: 1.5s, 4-in: 2.4s, 8-in: 4.4s
<j​berman> Yep and with the blinds cache + elimination of multiple rounds of blinds calculations during tx construction, it should be instant
<r​brunner7> Because the fetching of decoys falls away?
<s​needlewoods> been trying to remove all the secret material from memory that appears after you open the seed page
<s​needlewoods> I figured out displaying the QR code creates a bunch of copies of secrets, but even if I disable the QR thing there are still one copy for each svk, ssk and seed that I can't get rid off.
<j​berman> I believe fetching decoys can take some time especially pointing to a cold node (it's also 2 round trips to the node), so eliminating that definitely helps yes. I was mostly referring to the client-side execution time to construct the tx
<r​brunner7> SNeedlewoods: What would probably be my strategy as a hacker to find those secrets in memory? I think all kinds of strings are in memory, how would I target the secrets in particular?
<r​brunner7> Needle, meet haystack?
<j​berman> I think it's oook to make an attempt to tighten secret material in ram in this case, but not really worth any sort of significant time. If the user requests the seed be displayed in the app (a relatively rare action), it's reasonable to assume the seed is going to be sprayed all over
<s​needlewoods> for the QR code they were conveniently prefixed by "spend_key=" lol
<s​needlewoods> otherwise it just looks like random bytes for the keys
<s​needlewoods> "looks like random bytes" I have to correct, that's not the case since they are stored as a `QString` which has 16 byte characters, so each single byte of the key is followed by a `0x00` so there is a pattern
<r​brunner7> I was just thinking back to some earlier thought of mine: If you can't eliminate each and every copy, fill memory with similar stuff, to obfuscate basically. If you do that basically at exactly the same time, not even comparing memory snapshots before and after should give many clues
<r​brunner7> But I agree with jberman : Maybe at this point you should call it a day, PR what you have which is an improvement, and march on to greener fields
<sneedlewoods> +1
<r​brunner7> So, anything to discuss today beyond these reports?
<r​brunner7> The most prevalent attack scenario isn't probably genius hacker scanning process memory, but spammer sending people to the "verifysourseed.com" website ...
<s​needlewoods> If an attacker can dump your memory, you probably have other things to be concerned about like e.g. keylogger, clipboard logger etc.
<r​brunner7> Right :)
<r​brunner7> Alright, seems like we can close the meeting. Thanks for attending, read you again next week!
<s​needlewoods> thanks, cu
````


# Action History
- Created by: rbrunner7 | 2025-04-20T05:56:43+00:00
- Closed at: 2025-04-21T18:25:08+00:00
