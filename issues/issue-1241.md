---
title: Redundant if-statement in simplewallet.cpp?
source_url: https://github.com/monero-project/monero/issues/1241
author: RandomRun
assignees: []
labels: []
created_at: '2016-10-22T00:18:46+00:00'
updated_at: '2016-12-15T16:08:15+00:00'
type: issue
status: closed
closed_at: '2016-12-15T16:08:15+00:00'
---

# Original Description
I am just getting a hang of the basics of C++ and Monero's code, so that I don't really know what I am talking about, but:

Line 1489 seems to define a function `handle_command_line` that always returns `true`.

In line 1239, there is an if-statement that tests whether `handle_command_line(vm)` could be false, which, if I am reading this correctly, should never happen. If that is the case, couldn't lines 1239 and 1240 be eliminated?


# Discussion History
## moneromooo-monero | 2016-10-22T09:31:45+00:00
handle_command_line doens't seem like an obviously un-erroring function. It's a lot easier to add error return there than to re-add proper error checking in call sites later. Please keep as is.


## RandomRun | 2016-10-22T13:04:00+00:00
Just so I understand how the error could occur:

(i) When `handle_command_line(vm)` is called its boolean value is initialized to `false` by default? And so if something goes wrong inside of the function and the line `return true` is never reached it would just retain the `false` value? (I am just trying to guess how the code is executed.) Or

(ii) The if-statement is there in case in the future the code for `handle_command_line` gets changed to explicitly return `false` under some conditions?


## moneromooo-monero | 2016-10-22T14:03:55+00:00
There are no implicit error returns (there might be exception is called functions, but these would not return any boolean). You are right in your original description (that the boolean is effectively unused), I just think that removing it, while it reduces code slightly, is slightly worse than keeping it, though it is subjective, and you're free to disagree :)


## moneromooo-monero | 2016-10-22T14:05:59+00:00
 And, to elaborate, the reason I think it's better to keep, is that adding errors to a function tends to be error prone, as call sites must be updated to properly handle it, which the code already does now, so it's already prepared. But your suggestion also has a benefit of course.


## ghost | 2016-10-22T16:25:16+00:00
I think this is like @moneromooo-monero's comment on my PR #1225 where I tried to factor out an error checking function which always just returned true. 

I now see that it's sensible to keep error checking functions in-line even if they're just bare-bones right now because it makes it easier to expand them later.


## luigi1111 | 2016-12-15T16:08:15+00:00
Preponderance of the evidence suggests it is better to keep.

# Action History
- Created by: RandomRun | 2016-10-22T00:18:46+00:00
- Closed at: 2016-12-15T16:08:15+00:00
