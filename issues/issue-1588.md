---
title: Where is get_set_log_detalisation_level() defined?
source_url: https://github.com/monero-project/monero/issues/1588
author: moneroexamples
assignees: []
labels: []
created_at: '2017-01-16T21:38:44+00:00'
updated_at: '2017-02-05T01:52:03+00:00'
type: issue
status: closed
closed_at: '2017-02-05T01:52:03+00:00'
---

# Original Description
I see it used in many places, but cant find a file with its declaration or definition.  Similarly, where are `log_space::log_singletone::add_logger(LOGGER_CONSOLE, NULL, NULL);` and `LOGGER_CONSOLE` defiled? 

Searching the source code shows their use only. Is it boost or some other external library that monero is using that has these functions and constants?

# Discussion History
## ghost | 2017-01-16T22:12:23+00:00
Have a look at PR #1522 where @moneromooo-monero has changed the entire logging system to easylogging++

Reading through the code should hopefully provide the answers you're after

## moneromooo-monero | 2017-01-16T22:29:23+00:00
Not sure where they're defiled, but that sounds kinky.

contrib/epee/include/misc_log_ex.h (before the logging change - after it, they don't exist anymore)

## moneroexamples | 2017-01-16T22:46:49+00:00
@moneromooo-monero 

Yes, cant find them anywhere, but monero compiles without issues. There must be defined somewhere. I need to find where, as none of the moneroexamples compiles now because there are undefined. Including `easylogging++.h` does not help, so they are not there.

## ghost | 2017-01-16T23:10:13+00:00
I think you'll need to look at the changes in that PR to see how the new macros function etc rather than just a simple #include

## moneroexamples | 2017-01-16T23:23:45+00:00
@NanoAkron @moneromooo-monero 

I see what happened now. The loggin system was changed, but some files remianed in monero codebase that use the old logging system:

https://github.com/monero-project/monero/search?utf8=%E2%9C%93&q=get_set_log_detalisation_level

Seems those files are not used anywhere, as monero compiles even though they used undefined methods and variables?

## moneromooo-monero | 2017-01-17T09:14:33+00:00
You want to replace it with: mlog_configure("name_of_your_program.log", true_to_output_console_as_well);

## ghost | 2017-01-17T16:21:32+00:00
@moneroexamples that's an interesting find. Would you care to strip out the components you've found which are now redundant and submit that change as a PR?

## moneroexamples | 2017-01-17T21:27:06+00:00
@moneromooo-monero 

Thanks.

@NanoAkron 

Yes, I can remove the files, and make PR to romove those files later today.

Thanks for help.

# Action History
- Created by: moneroexamples | 2017-01-16T21:38:44+00:00
- Closed at: 2017-02-05T01:52:03+00:00
