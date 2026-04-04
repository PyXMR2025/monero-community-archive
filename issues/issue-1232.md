---
title: 'Monero Tech Meeting #127 - Monday, 2025-07-07, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1232
author: rbrunner7
assignees: []
labels: []
created_at: '2025-07-04T15:25:43+00:00'
updated_at: '2025-07-07T18:21:28+00:00'
type: issue
status: closed
closed_at: '2025-07-07T18:21:27+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1227).


# Discussion History
## rbrunner7 | 2025-07-07T18:21:28+00:00
````
<r​brunner7:monero.social> Meeting time. Hello! https://github.com/monero-project/meta/issues/1232
<s​needlewoods> hey
<j​berman:monero.social> *waves*
<r​brunner7:monero.social> Alright, let's start with the reports from last week
<s​needlewoods> mainly worked on multisig, will need to spend some time testing when everything is ready
<s​needlewoods> `grep "\<m_wallet\>" src/simplewallet/simplewallet.cpp -c` now gives 326 results on my branch, 668 on master
<s​needlewoods> Also noticed there is a problem with the methods that take `char *password` as argument (from my [remove cached password PR](https://github.com/monero-project/monero/pull/9915/commits/214bbf59092337987830dbfe66c574c7fe708566)). AFAICT after debugging, it is no issue if the pointer comes from a `string` (as it is the case in the GUI), but `wipeable_string` is not zero-terminated, s<clipped 
<s​needlewoods> o if you just pass `wipeable_str.data()` it will read the password + random amount of random bytes until next zero-byte.
<s​needlewoods> To solve this I added function overloads with `size_t pw_length` ([commit](https://github.com/monero-project/monero/commit/a5fc39da427fff8fdbd593713169f47343f0a7a2)).
<s​needlewoods> Haven't changed #9915 yet, but I'd say that we should not allow the potentially dangerous functions like `setPassword(const char *old_password, const char *new_password)` without `size_t pw_length`. So instead of overloads I would just replace the functions, do you agree?
<r​brunner7:monero.social> Sounds good
<r​brunner7:monero.social> You mean your *own* new methods that take a password in the form of `char *password`?
<s​needlewoods> yes, not merged into monero-project yet
<r​brunner7:monero.social> Then yes, I would make them safe
<sneedlewoods> +1
<r​brunner7:monero.social> But where would the caller get the length from?
<j​berman:monero.social> me: contest review/handling, PR wrangling, nothing significant to share since last week
<s​needlewoods> `wipeable_string.size()`
<r​brunner7:monero.social> I see
<r​brunner7:monero.social> jberman: Say again, when is the new, extended contest deadline?
<j​berman:monero.social> helioselene deadline extended to July 10th, 17:00 UTC
<j​berman:monero.social> https://github.com/j-berman/fcmp-plus-plus-optimization-competition?tab=readme-ov-file#update-helioselene-submission-deadline-extended
<r​brunner7:monero.social> Hopefully the updated rules do not allow any more loopholes or still offer room for misunderstandings ...
<s​needlewoods> sorry brb
<r​brunner7:monero.social> Who would have thought that the contest would get into such rough waters :)
<r​brunner7:monero.social> There is a second submitter for Helioselene beside dimalinux, right? You did not hear much from them?
<j​berman:monero.social> We're in contact via DM, they are aware of the latest
<r​brunner7:monero.social> Ok, so just less public drama :)
<j​berman:monero.social> pw_length makes sense to me here (unfortunately)
<j​berman:monero.social> Yep
<r​brunner7:monero.social> Alright, do we have something to discuss beyond these reports?
<r​brunner7:monero.social> Does not look like it. Thanks everybody for attending, read you again next week!
<j​berman> Doesn't need an answer right now, but was curious if you may have any thoughts on deprecating Boost serialization for MMS messages here: https://github.com/monero-project/monero/pull/9940
<r​brunner7> Don't see any problem with that. MMS does not work properly anymore anyway, and with tobtoht hopefully sooner or later bringing some successor to the table I don't think Boost support matters in any way here.
````


# Action History
- Created by: rbrunner7 | 2025-07-04T15:25:43+00:00
- Closed at: 2025-07-07T18:21:27+00:00
