---
title: Your code is being used to attack github repositories.   Your repo is basically
  a virus.
source_url: https://github.com/xmrig/xmrig/issues/2236
author: Lothrazar
assignees: []
labels:
- av
created_at: '2021-04-05T16:11:24+00:00'
updated_at: '2021-04-12T13:34:05+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:34:05+00:00'
---

# Original Description
Example

https://github.com/Lothrazar/Cyclic/actions/runs/719171490

https://github.com/Lothrazar/Cyclic/actions/runs/719171490/workflow

# Discussion History
## SChernykh | 2021-04-05T16:17:46+00:00
xmrg is NOT a virus, read wikipedia for the definition of a virus.
Also read https://dev.to/thibaultduponchelle/the-github-action-mining-attack-through-pull-request-2lmc and https://www.bleepingcomputer.com/news/security/github-actions-being-actively-abused-to-mine-cryptocurrency-on-github-servers/

## naturallydisasterous | 2021-04-05T17:30:36+00:00
 I can use a screwdriver to drive a screw, or I can use a screwdriver to kill someone. The original purpose of the tool is to do good, but just like any other tool, the screwdriver can be used maliciously. This code is not a virus. Rather, the virus is the malicious individuals using this code unethically.
Also, just like @SChernykh stated, this software is inherently not a virus. A virus starts with malicious intent, and spreads itself. XMRig on the contrary, has a perfectly ethical purpose.

## mtfn | 2021-04-05T18:25:16+00:00
One of my repositories was recently targeted by one of these attacks. I promptly looked into the suspicious runs and reported the creator of the PR for abuse.

That being said, I do not believe that the issue stems from this software and I would agree with others that this repository, used primarily in a non-abusive manner, is not a virus.

I've reached out to GitHub support about my incident in particular and the articles I've found also mention being in touch with GitHub; we'll see how they go from there.

## snipeTR | 2021-04-05T18:41:53+00:00
Since you are using github, you understand programming languages.  In the code in xmrig, can you show us the part that makes the virus you are talking about?

## SChernykh | 2021-04-05T19:06:02+00:00
I think I found the suspect: https://www.reddit.com/r/MoneroMining/comments/mks43t/github_mining_guide/

## chron0 | 2021-04-05T19:24:41+00:00
How dare you question the master of math...

## mtfn | 2021-04-05T20:00:45+00:00

GitHub knows of these attacks and how they're being carried out, but I haven't seen them address it directly and publicly other than playing whack-a-mole by banning the offending accounts as they pop up.

As far as I can tell, any long-term solution would involve breaking changes to how GitHub Actions works with pull requests.

I have an idea on how these attacks can be prevented, **but I have no idea if this actually works**.

Public repositories can either disable Actions or [change the settings](https://docs.github.com/en/github/administering-a-repository/disabling-or-limiting-github-actions-for-a-repository) to establish a whitelist of Actions.

Hopefully this disables the creation and execution of new checks on pull requests, but again, I'm not sure if it will help in the slightest. I reached out to GitHub support on this, and they have yet to respond.

And to the opener of this issue: I understand your concern. Attacks like this on our own repositories are detrimental, and we're all looking for a solution. We just think that solution should allow this legitimate open source software to remain open.

## SChernykh | 2021-04-05T20:04:48+00:00
Honestly, the whole idea of executing random scripts and allowing things like curl and compilation there is a giant security hole waiting to be abused. So it is abused - if not with xmrig then it will use something else, but it WILL be abused.

## ThiefMaster | 2021-04-05T20:10:03+00:00
The whole point of GitHub actions is to let people run code - in an environment that's highly temporary and thus anything malicious you do there has no lasting impact. There's a reason why `pull_request` actions triggered from a fork get a `GITHUB_TOKEN` that has no write access whatsoever..

## ThiefMaster | 2021-04-05T20:11:22+00:00
> Public repositories can either disable Actions **or change the settings to establish a whitelist of Actions**.

That won't work. It's about whitelisting the sources of third-party actions. As long as the malicious code is in the local action itself, it won't help at all.

## mtfn | 2021-04-05T20:16:47+00:00
> > Public repositories can either disable Actions **or change the settings to establish a whitelist of Actions**.
> 
> That won't work. It's about whitelisting the sources of third-party actions. As long as the malicious code is in the local action itself, it won't help at all.

Got it. Guess what's left to do is cancel the workflows as they appear, lock the malicious PR, and then block and report the user.

Or do nothing.

EDIT: Maybe [limiting interactions](https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository) might help a _bit_, but I'm not too confident about this.

# Action History
- Created by: Lothrazar | 2021-04-05T16:11:24+00:00
- Closed at: 2021-04-12T13:34:05+00:00
