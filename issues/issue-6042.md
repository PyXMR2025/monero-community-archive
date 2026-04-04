---
title: '"Double Check" - An extension to OpenAlias for improved security'
source_url: https://github.com/monero-project/monero/issues/6042
author: fullmetalScience
assignees: []
labels: []
created_at: '2019-10-27T16:55:02+00:00'
updated_at: '2019-12-15T20:21:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I would like to propose an extension to OpenAlias.


## Problem

The current concept is based on one domain, and thus virtually on one DNS resolver. This establishes a single point of failure: If the DNS gets compromised, users run the risk of having their OpenAlias provide incorrect data.

Self-hosted or not, one can never trust with sufficient certainty that their TXT record is returning the desired XMR address.


## Mitigation

One way this could be mitigated to an extent is by cross-checking the results with a copy of the record on another domain.

For maximum benefit, the second domain should be with a different registrar and be associated to independent DNS resolvers.

In the case of XMR.ID I configured it like that: The TXT record for `saberhagen.xmr.id` is exactly the same as `saberhagen.xmrid.com`:

    [ "`dig -t TXT +short saberhagen.xmr.id`" =  \
      "`dig -t TXT +short saberhagen.xmr.id`" ]  \
      && echo 'All good!'

If wallet software were to perform that check, the likelihood of somebody sending funds to an undesired recipient is significantly lowered.


## How

I envision this as a general approach that anyone can utilize.

For this to work, the wallet software would have to know which two domains serve the same results.

I consider a hard-coded solution the most secure. We could name the pairs in a simple file on GitHub that domain owners can request merges for.

To confirm that one actually owns the domains in question they'd have to add a record to their DNS that confirms this. For every release, CI could have the ownerships checked and changes would only get in with new releases.


## Additional ideas

The "double check" idea opens possibilities for further improvements that build upon it. The wallet could check if the IP addresses (or even subnets) of the DNS resolvers actually differ. Also, the secondary domain could be specified to use *hashed* OpenAliases. Instead of requesting `saberhagen`, we would request its SHA224 hash:

`dig -t TXT +short __7855df3fa59f954816a11079603e9321b7b4842c69796dd21574fe5d.xmr.id`

The above will return the same XMR address as `saberhagen.xmr.id` does. Benefit: The DNS provider cannot tell which username was requested.


## Conclusion

The "dual domain" setup probably bears the highest benefits-to-efforts ratio to actually make the OpenAlias commonly used and thus Monero in general more usable.

A usable Monero means a higher likelihood of adoption.


# Discussion History
## moneromooo-monero | 2019-10-27T17:47:12+00:00
You can't really point a record to another record if you're starting from the assumption a record can get pwned. Asking github for which records to check seems to be a step backward since it relies on some third party to give you the records (and apparently a second third party to merge something). If you go that way, this would have no place in the spec IMHO (but a "alternate" record to point to another record might, and this could be used like HSTS, so that you're protected against a TXT change *after* you've used it once, though OA usage is probably a fair bit less about recurring uses than website usage).

## fullmetalScience | 2019-10-27T18:29:12+00:00
To clarify:

The part about initially linking domains to each other is for proving to wallet devs that one actually controls the domains in question.

It's comparable to a record you use to show to GitLab Pages that you own a domain and is thus independent of the resolving that happens when the software is being used.

Essentially I could also put up a TXT record saying `"moo, I confirm that this is my domain. regards fullmetal"` and if there's only a handful of applicants that want to use this feature, it could actually just be done manually.

## fluffypony | 2019-10-29T17:23:17+00:00
I like the idea of 2FA of some sort, but I think that an implementation like this misses the point of OpenAlias. If you’re going to have an out-of-band delivery of metadata (eg. A file on GitHub) then you may as well just put your address on GitHub and link to the file, or just provide your Monero address;) OpenAlias wants you to convey as much information as possible from as little information as possible (a domain), so having to additionally provide a link to a file defeats that.

One simple form of 2FA that *would* work would be to include the first and last few digits of the address in the OpenAlias. As an example, instead of providing ```saberhagen.xmr.id```, you could provide ````874t6u+saberhagen.xmr.id````. That way an attacker would have to produce an address with the same first 3 and last 3 digits (which is so difficult that we can conclude that the risk is cryptographically negligible) **and** compromise the domain.

PS. Would need to check with the MRL to see just how difficult it is to generate a collision at 3+3 characters, may have to go 4+4 if it can conceivably be brute-forced in our lifetime.

## fullmetalScience | 2019-10-31T13:06:35+00:00
Please disregard the part about GitHub altogether. It added confusion as to what I am proposing.

Think of it this way: When a user enters *saberhagen.xmr.id* as recipient, the wallet internally also checks *saberhagen.xmrid.com* and compares the results.

Now *how* the wallet knows that *xmrid.com* is confirming contents for the *xmr.id* OpenAliases is secondary. It's important *that* it knows. The highest certainty is guaranteed if hard coded, so that changes can only happen for new releases.

## fluffypony | 2019-10-31T16:37:56+00:00
What if the person has a .com, what is the pairwise domain? Also, what if I don't configure that and just use normal OpenAlias on *fluffypony.waffle.id*, and then an attacker registers *waffleid.com* just to mess with me?

## fullmetalScience | 2019-10-31T19:57:32+00:00
Well, domain naming wouldn't be deterministic like that :)

Any combination of domains is possible. Let's say it's *waffle.id* + *getmonero.org*.

You'd have to set up a TXT record **on waffle.id** saying `linktothisdomainplz: getmonero.org` and another **on getmonero.org** saying `linktothisdomainplz: waffle.id`.

Those two records would **only be looked up in the very moment of merging the corresponding change into master**. From then on, the link would be hard-coded.

Worst case such a link gets outdated which then leads to the OpenAlias becoming invalid.

Meanwhile safety of funds and usability receive a tremendous boost.

## fluffypony | 2019-10-31T21:08:35+00:00
So when someone adds their two URIs to the list they may have to wait 6 months before a hard fork to ensure everyone is on the latest version (with their URIs in it) before using their OpenAlias address? Also instead of just configuring a TXT record, and maybe figuring out DNSSEC, they have to do all that and also figure out how to get a pull request merged into Monero’s codebase?

## fullmetalScience | 2019-10-31T23:55:29+00:00
Not at all.

All OpenAliases will work as usual right from the moment they're configured.

This double check is optional, but strict for those who decided to opt their domains into it.

So anybody can use the current single-domain scheme right from the moment they set it up - and, if opted in, after a couple of months be glad that their OA became even more secure.

## fullmetalScience | 2019-12-15T16:08:14+00:00
[Community feedback on this idea is positive.](https://www.reddit.com/r/Monero/comments/e8dadt/want_monero_to_be_simpler_to_use_lets_start_with/?utm_source=share&utm_medium=web2x)

How can we best advance the topic from here?

## fluffypony | 2019-12-15T18:21:58+00:00
That thread isn't positive, there's lots of criticism in there and the general sense is that we just leave things as-is. Additionally, this idea adds a ton of complexity, and is just fraught with centralisation risk. For example, how do you revert something hardcoded into the Monero codebase if you lose access to your GitHub account? Now we have to trust that someone else has successfully identified that you want to change your URI and they've submitted a PR in your behalf? Who will manage the process of validating these?

I respect you wanting to improve OpenAlias, but this isn't an improvement.

## moneromooo-monero | 2019-12-15T18:30:28+00:00
A list of third party services does not belong in monero.
What we *could* do is an extension to Openalias where a record may have a "mirror:a.b.c:d.e.f" in a record which means "a mirror of the record for a.b.c is also available a d.e.f". The wallet could remember those, and next time it needs to lookup a a.b.c record, it'll also look it up at d.e.f and compare. This will not detect any compromise of a.b.c before the first lookup. It also DoSes you if you lose any one domain.
Whether the pros outweigh the cons, I don't know.

## moneromooo-monero | 2019-12-15T18:45:33+00:00
If we had plugins, we could have a plugin that'd list those.

If we had plugins, we could do a lot of nice stuff, like automatic xmr.to use, fiat balance, etc. These would not have to be in monero, and anyone could make their own plugins.


## fullmetalScience | 2019-12-15T19:23:42+00:00
> there's lots of criticism in there and the general sense is that we just leave things as-is.

There's not a single criticism on the "double check" idea in the entire thread.
(Note that the one user's sarcastic comment doesn't refer to this idea, but to the entire concept of OpenAlias which is not the topic of discussion.)

> how do you revert something hardcoded into the Monero codebase if you lose access to your GitHub account?

I can answer this truthfully, but remember that this isn't about Github access. So I realize you are likely not bringing it up in order to advance the development of the feature. I understand and I'm well aware that not getting your approval puts me in a hopeless position.

(If you're absolutely serious I am happy to clarify, but then I need you to set aside some time to actually consider what I am proposing.)

## fullmetalScience | 2019-12-15T19:27:53+00:00
Thanks mooo ... has the concept of plugins be discussed before?

My first impression is that a plugin system would be very risky for the end user.

## moneromooo-monero | 2019-12-15T20:21:22+00:00
I mentioned it a few times before, and I looked around a bit in the Qt docs, but there was no easy and obvious way. I don't remember anyone else discussing it offhand.

# Action History
- Created by: fullmetalScience | 2019-10-27T16:55:02+00:00
