---
title: 'Monero Tech Meeting #151 - Monday, 2025-12-22, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1315
author: rbrunner7
assignees: []
labels: []
created_at: '2025-12-19T19:48:19+00:00'
updated_at: '2025-12-22T18:53:03+00:00'
type: issue
status: closed
closed_at: '2025-12-22T18:53:03+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1311).


# Discussion History
## rbrunner7 | 2025-12-22T18:53:03+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1315
<j​berman> *waves*
<v​tnerd> Hi
<s​needlewoods> hey
<r​brunner7> Before I forget to mention it: I propose that we skip the "between the years" meeting in 1 week, on December 29, and meet again in the new year in 2 weeks, on January 5. I will probably be around nevertheless should there be something interesting and/or urgent.
<j​berman> good with me
<s​needlewoods> sounds good to me
<r​brunner7> Good. So, what is there to report from last week?
<j​effro256> Howdy
<s​needlewoods> GUI restore height on wallet creation: https://github.com/monero-project/monero-gui/compare/master...SNeedlewoods:monero-gui:x_restore_height_on_wallet_creation
<s​needlewoods> I think most important cases are covered now, but IMO what's missing is information about the nettype for saved remote nodes in `remoteNodesSerialized` (the comment in [this WIP commit](https://github.com/monero-project/monero-gui/commit/b565f4e34fa5df2d52baac0def19654bd80f2d8e) goes into more details) so will probably continue to spend a little more time on this
<j​berman> interesting strategy there to use a mock temp wallet
<j​effro256> Me: Finishing up knowledge proofs crypto and will be moving to migrate carrot code to using the unbiased hash-to-point where applicable. Interesting note: reserve proofs now have full-chain sender anonymity and don't reveal amounts per enote
<j​berman> me: implemented unbiased hash to point for tree building, made some changes to tx relay v2 and currently testing those changes locally
<v​tnerd> Me: some work in monerod+lws+lwsf for fcmp++ proofs client side. Got a bit more work in lwsf before I know whether the protocol is sufficient, etc, so it'll be a while before prs
<r​brunner7> Say again, what is *lwsf*?
<v​tnerd> Lws frontend. Skylight uses it to do all the heavy work
<r​brunner7> Something like a library to build clients?
<v​tnerd> There also lwcli wallet which uses lwsf, but only only ofrn and myself have really used thT
<v​tnerd> Yes. It reimplements wallet2api virtual functions so technically lwcli is both a wallet2 wallet and light wallet with little code needed to swap them. You can't swap metadata files though
<j​effro256> Nice
<j​effro256> That'll hopedully become pretty powerful with SNeedlewoods's work
<j​effro256> Maybe allowing a wallet-RPC and/or wallet-CLI type interface with light wallets
<v​tnerd> We could nearly make the main wallet GUI an optional light wallet too but it might confuse people
<j​effro256> Is that possible?
<v​tnerd> yes if the primary wallets use the vtable API it's basically one call to create a different factory class and the remaining is seamless because of the vtavlbles
<jeffro256> +1
<r​brunner7> Well, whether something like that would be confusing or not would probably depend a lot on UX/UI design. With quality there it should be possible to make things clear IMHO
<jeffro256> +1
<v​tnerd> The file types differ so you must select at creation time
<jeffro256> +1
<v​tnerd> But otherwise lwcli demonstrates a basic wallet can use both implementations easily
<r​brunner7> Interesting. A requirement to use different apps only to use LWS could develop into quite a drag regarding making it popular
<r​brunner7> And finally that complicated Wallet API structure with virtual functions for everything would be put to good use
<v​tnerd> Yup. And This was loads easier than shoving light wallet cod into wallet2 etc, as it wasn't trying to do tow things at once
<v​tnerd> *two
<r​brunner7> Well, long term we want to get rid of wallet2 anyway, so that's definitely a plus
<r​brunner7> If the Rust people do not steamroll us earlier than we get the chance to do that :)
<r​brunner7> Different question: SNeedlewoods 's ready-to-review PR currently has 4 commits. Does that matter in any way regarding reviewing it, does it make that more complicated? https://github.com/monero-project/monero/pull/10233/commits
<r​brunner7> Would it be a good idea to review the commits individually?
<r​brunner7> Is that even possible with GitHub?
<s​needlewoods> only commit that matters for that PR is the last one, the others are still open PRs
<r​brunner7> You mean everything worthy of review is all in the last commit? Not sure I understand.
<s​needlewoods> first commit is just this PR https://github.com/monero-project/monero/pull/9464
<s​needlewoods> second commit is another PR
<s​needlewoods> the simplewallet changes are based on those PRs, I thought this way it's easier to review, because you just have to pull one PR
<s​needlewoods> instead of pulling 3 and then rebasing them in the correct order youself
<r​brunner7> Ok, will try to have a look and hope I will see better once I check the details
<s​needlewoods> hit me up if you have more questions
<rbrunner7> +1
<j​berman> SNeedlewoods: rather than use a temp wallet (which I think might have some tricky things to manage / make sure is done correctly / adds overhead of a new wallet), another idea could be to use QT's http request lib to communicate directly with the daemon that way: https://www.qt.io/product/qt6/qml-book/ch13-networking-http-requests
<s​needlewoods> interesting, I'm also afraid the tmp_wallet could have unseen drawbacks, will look into it, thanks
<j​berman> I guess then you may have to deal with tor too, and the wallet out of the box I think should have that covered
<r​brunner7> So you may swap some potential problems with a different set of potential problems ...
<j​berman> yep true, I think a temp wallet is a solid strategy, feel free to continue with that
<s​needlewoods> looked into many things already, because 1. I'm a GUI noob, and 2. it's definitely more complicated then the CLI lol
<r​brunner7> Might also be more "future-proof", if yet more stuff gets added to daemon communication
<j​berman> I think when I first looked at the issue, I thought there might be a solid way to reorganize some of the logic internally in the wallet API functions to establish the daemon connection sooner, but maybe this will be simpler
<r​brunner7> Does Featherwallet have to deal with the same problem somehow, and maybe already have sort of a solution? tobtoht is usually quite methodical with such things IMHO.
<j​berman> ya that is a good question, tobtoht would be good to check with on this too
<jeffro256> +1
<j​berman> and/or take a look at the feather code
<s​needlewoods> will do
<r​brunner7> I guess that might be even more complicated, or at least larger, than the GUI code :)
<r​brunner7> Ok, anything else to discuss today beyond these?
<s​needlewoods> wish you all happy holidays
<jeffro256> +1
<j​effro256> Perhaps the wallet API could have an endpoint added which lets you make HTTP requests on the same internet client as the wallet ?
<r​brunner7> Thanks, likewise! Has been an interesting year, in any case. Next year sure will be even better, with added FCMP++ pixie dust
<sneedlewoods> +1
<r​brunner7> So thanks for attending, read you again in **two** weeks in 2026!
<s​needlewoods> thanks everyone, see you
<j​effro256> Thanks everyone!!
<j​berman> thanks all :)
````


# Action History
- Created by: rbrunner7 | 2025-12-19T19:48:19+00:00
- Closed at: 2025-12-22T18:53:03+00:00
