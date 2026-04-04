---
title: Change banner on GetMonero.Org website
source_url: https://github.com/monero-project/monero-site/issues/752
author: One-horse-wagon
assignees: []
labels: []
created_at: '2018-05-31T17:28:58+00:00'
updated_at: '2018-07-11T12:14:29+00:00'
type: issue
status: closed
closed_at: '2018-07-11T12:14:29+00:00'
---

# Original Description
Present banner is very confusing.  My suggestion is--

"To all Monero holders.  Please upgrade your Monero software to the current April 6th network version"   

 MORE INFO (radio button to follow)

# Discussion History
## rehrar | 2018-05-31T17:32:43+00:00
I like the idea, and think this needs to change, but I would take out "To all Monero holders." Move away from the 'holder' verbiage. It denotes trading as the primary usecase, imo.

Perhaps "There was a network upgrade on April 6th, please make sure your software is upgraded to continue using the Monero chain."

Or something?

## One-horse-wagon | 2018-05-31T17:43:42+00:00
How about the following--

"There was a network upgrade on April 6th.  If you haven't already, please update your software now to continue using the Monero block chain"

## One-horse-wagon | 2018-05-31T18:06:26+00:00
Sorry, closed issue by mistake.  It's still open.

## Re-Diculous | 2018-06-01T05:16:05+00:00
"Make sure to be up-to-date with the network upgrade that occurred on April 6th"

## el00ruobuob | 2018-06-01T06:29:06+00:00
The sentence should be relevant before and after any network upgrade. So i suggest "To continue using the Monero chain, make sure your software is up-to-date with the April 6th network upgrade."

## One-horse-wagon | 2018-06-01T13:20:38+00:00
I like it.

## erciccione | 2018-06-01T15:36:23+00:00
>  "To continue using the Monero chain, make sure your software is up-to-date with the April 6th network upgrade."

I like this, i would just remove the word 'chain', to keep it as less techy as possible, something like: 

_To continue using Monero correctly (maybe better: with no issues?), make sure your software is up-to-date with the April 6th network upgrade_

## el00ruobuob | 2018-06-01T17:22:38+00:00
I don't think "correctly" or "with no issue" is even needed. If you don't upgrade, you're not using Monero anymore, but an old monero chain.

## erciccione | 2018-06-02T11:53:39+00:00
True, if nobody have any other suggestioni think we should go for:

 _To continue using Monero, make sure your software is up-to-date with the April 6th network upgrade_

+discussion

## One-horse-wagon | 2018-06-02T15:50:34+00:00
It's a zinger.  I like it very much.

## uncagedpotential | 2018-06-02T23:06:09+00:00
@el00ruobuob and @erciccione nailed the wording, nice work! Two questions about which key points of information we want to bring to visitors' attention.

Question 1) Is it valuable to state that this occurred on the sixth of April, specifically? This was pertinent precision before the update, seems like an unnecessary use of user attention now.

Question 2) Would it be helpful to specify "version 7" and/or "GUI 0.12.X.0" ... 

I'm trying to put myself in the shoes of somebody that is learning about the upgrade for the first time from the getmonero.org banner. Version numbers might be more helpful for checking whether I'm up to date.

## el00ruobuob | 2018-06-03T05:39:10+00:00
1) the idea is to keep an accurate message before and after network upgrade. We agree that it is not needed after, it's just that the same thing will stay here for weeks.

2) I believe the link is here for such details.

## el00ruobuob | 2018-07-08T17:31:16+00:00
this has not been updated in a month. Obviously the banner is not part of the monero-site code (or i'm blind), and i think it's added on the hosting server itself. @rehrar could you tell? Who could then change the actual banner with the one we agreed upon? Is it @luigi1111 or @fluffypony ?
> To continue using Monero, make sure your software is up-to-date with the April 6th network upgrade

## fluffypony | 2018-07-08T17:33:51+00:00
@el00ruobuob is there broad consensus on that wording?

## el00ruobuob | 2018-07-08T17:51:29+00:00
@fluffypony i think @SamsungGalaxyPlayer @erciccione @uncagedpotential @One-horse-wagon and me seemed to agree on this. At least, it's still better than the actual one.

## uncagedpotential | 2018-07-10T15:57:22+00:00
Sure, I would be okay with the proposed: "To continue using Monero, make sure your software is up-to-date with the April ~~6th~~~ **2018** network upgrade"

^ I removed the date, "6th" which is irrelevant now, and added the year instead.

-------------

Smaller commentary: Reading the above comments, there appear to be two considerations.
Consideration 1) Making sure that the before banner and after banner both cleanly convey the crucial information, without extraneous details or awkward tense wording
Consideration 2) Making the message be the same before and after the fork.

Given consideration 1 (highest priority for me) and the presumed triviality of changing the banner text, I do not see the impetus to use a single one-size-fits-all message for before and after the fork. 

A counterexample for why a single before/after message is difficult - the before message should contain future tense, the height, and the precise date. For the after message, the tense changes, and the exact date/height become extraneous information that wastes user attention.

Regarding homepage banners, we should never sacrifice informativeness or linguistic precision for convenience. :- )

For the September fork, perhaps we could just approve both (before & after) banners in one step, so that this doesn't balloon out into multiple conversations. Or maybe there is a clean single solution that is works both ways (I just haven't seen it yet).

Anyways, this meta conversation can happen for the next fork; I'm fine with the message above to clean up our current banner.

Edit: We could also just open a  separate issue to discuss a general template for all future network upgrade messages.

Cheers,
UncagedPotential

## el00ruobuob | 2018-07-11T07:19:45+00:00
@uncagedpotential, as the network upgrade occurs on a specific block height, it would be very complicated to have a core member behind the website to change the banner at this exact moment.

I think `To continue using Monero, make sure your software is up-to-date with the April 6th network upgrade` is valid before and after, as it is infinitive.

The point is the core team member has bigger things to do than changing a banner on the fly. They are busy enough merging all those Pull Request, dealing with FFS, and so on.
Once the new major release is published and the block height for the new version is defined, then the banner could be updated to reflect the new date, keeping it until next network upgrade block height definition and release publication.

## fluffypony | 2018-07-11T12:14:29+00:00
Changed, closing this issue.

# Action History
- Created by: One-horse-wagon | 2018-05-31T17:28:58+00:00
- Closed at: 2018-07-11T12:14:29+00:00
