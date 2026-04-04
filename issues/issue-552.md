---
title: '[Lightwallet API] ambiguous specification of timestamp format'
source_url: https://github.com/monero-project/meta/issues/552
author: dzonatan
assignees: []
labels: []
created_at: '2021-02-21T20:21:50+00:00'
updated_at: '2023-12-18T19:34:41+00:00'
type: issue
status: closed
closed_at: '2023-12-18T19:34:41+00:00'
---

# Original Description
I've noticed that there are differences in date formats used across lightwallet services which leads to incompatibilities (e.g. https://github.com/mymonero/mymonero-app-ios/issues/90).

To be precise:

- [monero-lws](https://github.com/vtnerd/monero-lws) uses `2021-02-20T19:10:45.0-00:00` (which seems to mimic the specification but not exactly)

- [mymonero-app-ios](https://github.com/mymonero/mymonero-app-ios) uses `2021-02-20T19:10:45.000Z` (which seems to be [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601))

- [openmonero](https://github.com/moneroexamples/openmonero) uses `1482567670` (**unix time**, although I haven't run this myself, just noticed in the examples)


And I can see why did that happen because the specification itself seems to be a bit too vague:

> A string in JSON. The string format is "YYYY-HH-MM-SS.0-00:00". Monero blockchain timestamps do not have sub-seconds.

At least for me it's hard to undestand what "SS" stands for, why dash is used as a separator between date and time, what this `.0-00:00` suffix means. This should have a better, more detailed, explanation. 

However, IMHO, ideally this requirement should be changed to ISO-8601 or unix time as these are the most commonly used between REST services and has pretty good support across the platforms/libraries/etc.

Without this it's a bit hard to decide which project I should be pinging about having an issue.

# Discussion History
## vtnerd | 2021-02-21T21:05:54+00:00
The timestamp spec written here was clearly a typo. `SS` was supposed to be seconds but I somehow botched specifying the entire thing.

The API was written to "whatever the golang backend was doing at the time." The backend was using golang `time.Time` which indicates its output is based on RFC 3339. Both `monero-lws` and `mymonero-app-ios` are valid according to this RFC. `monero-lws` is invalid according to ISO-8601 because timezone `-00:00` must be written as `Z`, but otherwise conforms. Its likely that `opemonero` was only tested against its own HTML based source and no other application.

Its fairly trivial for me to change `monero-lws` so I don't particularly care. @moneroexamples maintains `openmonero` and can comment on changing that backend. Using a 64-bit seconds integer based on unix epoch is fastest for the backends, but will require multi-stage rollouts for MyMonero to change.

## vtnerd | 2021-02-21T21:06:49+00:00
*will likely. I can't comment on this directly anymore, but they'd have to update clients before changing the backend, etc.

## dzonatan | 2021-02-22T16:06:10+00:00
Thanks for an explanation. 
Changing the `monero-lws` to use `ISO-8601` would help me to continue testing things.

But still, the specification could be improved to avoid misinterpretations in the future.
Does this needs some sort of consensus to update?

## ndorf | 2021-02-22T17:52:51+00:00
In my opinion, ISO-8601 would be the best choice. The performance cost vs. stringified Unixtime is negligible: a quick test on my machine shows 110 nanos vs 60. I would change the spec to require this, if @vtnerd and @moneroexamples both agree.

## vtnerd | 2021-02-24T07:41:42+00:00
@dzonatan latest `monero-lws` should conform to ISO-8601.

## ndorf | 2021-03-05T23:02:31+00:00
Ping @moneroexamples

## moneroexamples | 2021-03-07T01:29:07+00:00
I'm fine with that.

## nahuhh | 2023-12-18T13:56:58+00:00
> @dzonatan latest `monero-lws` should conform to ISO-8601.

@vtnerd, do you know status of the others? (If this can/should be closed)

## vtnerd | 2023-12-18T19:34:17+00:00
I think this can be closed.

# Action History
- Created by: dzonatan | 2021-02-21T20:21:50+00:00
- Closed at: 2023-12-18T19:34:41+00:00
