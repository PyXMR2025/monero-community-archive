---
title: Various UX issues
source_url: https://github.com/monero-project/monero-gui/issues/1568
author: Gingeropolous
assignees: []
labels:
- Hacktoberfest
created_at: '2018-09-22T05:27:05+00:00'
updated_at: '2018-11-27T16:06:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
copied from some dude on reddit

Yup, without providing solutions then critique is useless. Here's a few issues.

Onboarding: There's a fundamental lack of onboarding and the wallet literally requires a manual to understand how to use it. Don't even get me started on the Ledger integration, but that's not Moneros fault IMO. Moving forward, it's easy to forget how confusing this space was when you first started but keeping this first time user POV is the key to simplifying products. There should be a mix of onboarding, tooltips, explanations and potentially links to video tutorials (for visual learners)

Information Hierarchy: The navigational components can (and should) be consolidated because they don't (IMO) justify their own nav items because there's simply not enough content, "Receive" being the main culprit here. As an example, Send and Receive can be consolidated into "Transfers" and address book can be a selector in the Send tab. Here, we went from 3 tabs to one. This type of consolidation is important because it lessens the cognitive load on users and provides the perception of simplicity which can be as important as simplicity itself.

Semantics: This is the lowest hanging fruit IMO. Protocol semantics should not be presented at the application layer. A few examples of current semantics that should be abstracted into simpler phrases: node, daemon, ring signatures (even though this is awesome) etc.

Graphics: This is a minor one but none of the images in the wallet are hi-res (svgs) they're all flat 1x pngs, so on retina devices all the assets are pixelated. This is such a small issue, but it's the small things that make an application feel safe, secure and trustworthy.

Payment ID's: Probably the most confusing things for new users. What is this and why is it important? What happens if I don't add one? How do I add one? Can I type in random chars? Is their char limitations? What do you suggest as an ID structure? Admittedly, these are really asinine questions, but trust me, these are the questions the average user asks themselves.

Addresses: When I create a new address what happens? Do I need a separate account for these wallets? Do all my balances show in this wallet? How many can I create? Again, such stupid questions but reflective of average user mental models.

Layout: There's a lot of layout issues and there's UI conflicts where things overlap, have inconsistent paddings, margins etc. We're not using grids at all so things look very inconsistent. This isn't the worst thing in the world because thinking about interfaces spatially and responsively is kinda hard. It's a little easier for me by virtue of the systems I've built but it's these kinda of things that contribute to the overall trustworthiness of the product because everything looks like it was intentionally placed where it is and thought about.

Error Handling: Errors aren't really handled very well in the system right now. There's two types of errors -- global and local. Local errors are for things like inputs. Right now the inputs are triggering a red input border but there's no assistive prompts that help a user remediate the issue. Each input should have a/some custom error message for example: The Address Book input error should say something like "That address couldn't be found, check your address book" as a shitty example. Global errors are for things like conflicts that prevent all actions from being performed. Something like "No internet connection" is a global error that should persist across all views no assigned to a local component.


# Discussion History
## dEBRUYNE-1 | 2018-09-22T07:53:30+00:00
+ui/ux

## GBKS | 2018-09-24T07:45:39+00:00
I'll try to add my perspective here, since this is a pretty long laundry list of things.

**Onboarding**
AFAIK, some work is currently being done on this, but it's mostly a restyling with some usability improvements. I think there can be a lot more work done in the future, but some of this feedback goes beyond the wallet itself. Creating videos and guides, etc is probably better handled community-wide?

**Information hierarchy**
AFAIK, the nav critique comes up frequently and should be addresses. Seems like some people feel strongly about combining send, receive and transactions and others feel strongly about having them exposed because they are they key actions in the wallet. Personally, I agree with the latter. Generally though, I'd like to move to a navigation system that can more easily be ported to mobile. [Here's a mock-up](https://raw.githubusercontent.com/GBKS/monero-wallet-design/master/screens/future/responsive%20layout.png) of what it could look like.

**Semantics**
Agreed. Probably should also start with a wider effort to explain things simply on the website, tutorials, etc, and then trickle to the wallet (and also other wallets?).

**Graphics**
Yes, please.

**Payment IDs**
I'm also confused about this feature :)

**Addresses**
Agree, this could be explained better as part of onboarding the first-time experiences of sending and creating an address.

**Layout**
Looks more like a QA issue? Maybe this could be turned into a separate issue to report layout bugs, so the community can gather them and the dev team can focus on fixing them? It can be tricky as a dev to both do the work and QA at the same time.

**Error handling**
Agreed. I like to think of error messages as tips. The point is not just to say what's wrong, but to let users know how to do it right.

Cool to see this feedback. Would love to help address the parts that require design work.

Just my 2 cents. I'm not fully aware of all the work that's happening though, so might be totally wrong here.






## erciccione | 2018-10-06T15:49:54+00:00
Maybe not for all of them, but definitely for some of the easier ones:

+hacktoberfest

## stoffu | 2018-10-15T11:43:14+00:00
Regarding the payment ID, AFAIK the classical long (64 characters) payment ID format specified separately is discouraged and will be deprecated in the near future. The integrated address format (with a short payment ID integrated) and the newer subaddress format both will not cause this confusion.

## ITwrx | 2018-11-27T16:06:30+00:00
My main FRs for the gui related to usability would be (in no particular order):

1) highlight, copy and paste should work (with the mouse too) for any text the gui shows on the screen. not being able to copy and paste basic stuff like the wallet balance makes things seem amateurish or buggy (even if that's not the case).
2) inline help text for all field names/labels. hovering over the field label should show help text (or be a link to built in docs or remote docs). you shouldn't have to go searching to find out how a field works.
3) stop asking users what they want to do about a daemon. just manage it silently. if some users really need to be able to micromanage the daemon(when using the gui), a advanced config option could be added. 
4) you shouldn't have to close the wallet (and the daemon currently) to be able to switch to a new wallet. the gui should facilitate this, imo.
    4a) choosing a language and regional format every time shouldn't be necessary either. this should be a config item per wallet. only required to be set on first run and then only available in the advanced config. (or only just in the config from the beginning_
5) built-in, configurable cpulimit support. maybe set to 50%(or less) by default?
6) the layout/organization and labels might could be improved, but the things i've listed above are the main things that make things unintuitive to me. Also, i would try to be careful not to "Windows things up" where people can't even figure out what the gui is actually doing, while trying to make things easier for people. there's a difference between "easy to use" and "stripped of all usefulness or user control". 

thanks



# Action History
- Created by: Gingeropolous | 2018-09-22T05:27:05+00:00
