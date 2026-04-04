---
title: two problems with load_checkpoints_from_dns
source_url: https://github.com/monero-project/monero/issues/166
author: iamsmooth
assignees: []
labels: []
created_at: '2014-10-02T22:58:00+00:00'
updated_at: '2014-10-06T08:29:35+00:00'
type: issue
status: closed
closed_at: '2014-10-06T08:29:35+00:00'
---

# Original Description
1. It is reading entropy from the hardware device every time it is called, which I believe is currently every hour. Consuming entropy repeatedly is harmful, especially for this use case. Instead, create (and seed) a prng once and use it on each poll without reseeding.
2. *_index should be size_t. since they are indexing a vector. As-is they produce a (correct) signed-unsigned compiler warning.


# Discussion History
## fluffypony | 2014-10-03T06:44:41+00:00
@iamsmooth @tewinget why don't we use src/crypto/random.c's generate_system_random_bytes for a single byte, divide that by 64, and floor the result (should give us a result between 0 and 3)? That way we're not doing any significant entropy usage, and we're using the existing function that uses a non-blocking device.


## iamsmooth | 2014-10-03T07:07:00+00:00
There is no reason to pull system random at all. Just use crypto::rand. This isn't even security sensitive at all (it is just load balancing right?), and if crypto::rand is broken the whole system fails.


## fluffypony | 2014-10-03T08:40:21+00:00
@iamsmooth yeah, I think we're completely over-engineering this even using random in the first place - we should just grab the current hour from the system time and divide by 6 and floor the result.


## iamsmooth | 2014-10-03T10:14:08+00:00
That's not great because more or less everyone in the world would then be querying the same one. If that is the intent, then just declare one of them to be the primary and cycle through them only in the event of failure. I'm not sure load balancing is really needed on a DNS query at all (which DNS _server_ is being hit will be load balanced by the DNS implementation at some lower level).

I have another question though. Are these DNS queries blocking? This is in the path of block acceptance, so that would add significant latency I think (only once an hour, but still...). Ideally this should be done in an independent thread.


## fluffypony | 2014-10-03T10:20:10+00:00
@iamsmooth local system time would be different across the world, so it would provide a reasonable distribution. It's not load-balancing per-se, it's more to ensure that if anything goes wonky with one of the domains (eg. DNSSEC validation fails) the entire network isn't polling it, and those that are will get a valid record from a different domain within 6 hours max.

Edit: that was a crappy example, but you get the general idea

I agree with the block acceptance hook. Polling events should have their own thread so that we prevent the issue we've seen where multiple checks are fired off simultaneously (could be bad if more than one thread requests a rollback?) @tewinget thoughts?


## iamsmooth | 2014-10-03T10:39:00+00:00
"more than one thread requests a rollback"

There are some locks on things like the blockchain that should prevent that from being possible. I have no idea if the checkpoint polling code handles those correctly (but it should -- you don't even want to be _looking_ at the blockchain if another thread is in the process of reorging it for example)

Regarding one domain not working, that's why I say just cycle to the next if you don't get a valid response. No need to wait 6 hours. Try first->if error, try next->if at end of list report problem. I was mistaken earlier there is no load balancing issue here; the only reason to have more than one is fail over.


## fluffypony | 2014-10-03T10:45:42+00:00
Fail over is already in there, but it _doesn't_ solve the problem. As I mentioned, this isn't about load-balancing, it's about distributing the queries. The reason is that a worst-case scenario is we lose control of a domain, and the new owner can run their own (perfectly valid) DNSSEC. Thus, spreading the queries out over all 4 of the domains means that, even if we lose control of one of them, we're still hitting the other 3 most of the time. To make this more robust we can (later) make sure it finds the same records on at least 1 of the other domains when querying.


## iamsmooth | 2014-10-03T10:54:34+00:00
Okay if that is the intent then I would say query them all (or at least 3 of them) and reject any outliers.


## fluffypony | 2014-10-03T10:55:59+00:00
Agreed - @tewinget is going to have fun reading this when he wakes up:-P


## iamsmooth | 2014-10-03T10:56:37+00:00
Good thought btw, to consider loss of control of one of the domains. Getting at more than one of them across independent registrations would likely be much harder, so this should be quite robust. It only needs to survive long enough to deliver an update anyway.


## fluffypony | 2014-10-03T10:58:26+00:00
Yep, if we lose control of a domain everyone will definitely know about it:)


## tewinget | 2014-10-03T18:42:22+00:00
_sigh_
On Oct 3, 2014 6:58 AM, "Riccardo Spagni" notifications@github.com wrote:

> Yep, if we lose control of a domain everyone will definitely know about
> it:)
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/166#issuecomment-57780567
> .


# Action History
- Created by: iamsmooth | 2014-10-02T22:58:00+00:00
- Closed at: 2014-10-06T08:29:35+00:00
