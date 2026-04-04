---
title: Re-introduce the "help <command>" variant of the CLI help command
source_url: https://github.com/monero-project/monero/issues/6494
author: rbrunner7
assignees: []
labels: []
created_at: '2020-05-02T12:59:09+00:00'
updated_at: '2022-02-19T04:34:22+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:34:22+00:00'
---

# Original Description
Up to PR #6127 the `help` command of the CLI wallet showed a long and somewhat unwieldy list of **all** available commands if issued without any parameters, and detailed help about a single command when using the name of the command as parameter.

PR #6127 basically renames the `help` command to `help_advanced`, and implements a new, simplified `help` command that only shows the most important commands, plus a pointer to `help_advanced` for getting more detailed info.

The new "noob-friendly" `help` command does not have any optional parameters; all it can do is print its short command list. The following does not work:

    help transfer

For help about the `transfer` command you must do now:

    help_advanced transfer

I see this state of affairs as 2 steps forward, 1 step back. While I acknowledge the short command list of `help` as an improvement, I don't like to type the long command name `help_advanced` for help about any command. I often already know the name of the command quite well, just don't remember all details about its arguments and then want to get a look at the usage as quickly as possible.

Proposal: Modify the new `help` command to **also** support a command name as parameter to print its usage.

I am aware that from a UX/UI point of view it's often a problem if there is more than one way to achieve the same thing, but I really can see no harm here in allowing both `help transfer` and `help_advanced transfer`.



# Discussion History
## sumogr | 2020-05-02T14:56:10+00:00
IMHO it needs some tiresome serious `cout`ing to create an organised commands "help" table (fixed widths, headers, the full monty) rather than a long list. there are many commands with many flags and options and many subcommands (e.g the accounts command). You will always face this problem using drop down lists due to the sheer number of commands. Anyhow i agree it needs reworking to become friendly but its a tedious work :D (EDIT: categorise the commands (accounts, mms and so on ... and add switches maybe i dont know)

## jtgrassie | 2020-05-13T03:21:16+00:00
I agree with @rbrunner7 here. #6127 in my view is a serious backwards step, not least because the previous help command worked _perfectly_. With this merged PR, a new user first has to type `help` to get a list of commands, and then `help_advanced command` to get the commands options! Also, this breaks tons of literature on StackExchange and reddit which often points to `help ...`. And why is the simplified help any better than before? Any CLI user is used to long man/info pages, so why do we need to dumb down the docs?

## iamamyth | 2020-05-13T08:04:03+00:00
> I am aware that from a UX/UI point of view it's often a problem if there is more than one way to achieve the same thing, but I really can see no harm here in allowing both help transfer and help_advanced transfer.

I would just add that, even if one accepts this design principle, that would imply that changing `help` in the first place was a mistake, and the correct choice would have been to introduce the simplified help as a new option of some sort (whether a command; a switch for the existing command, e.g. `help --simple`; or a prompt that appears after typing a bogus command). It's important to consider the *reasons* for these UX disciplines, not simply the rules resulting from those reasons: Providing multiple solutions to the same problem violates the principle of least surprise because users may see two guides with conflicting instructions, which also makes user assistance a challenge. With the `help_advanced` change, that violation is far worse, because the usage pattern has been broken for all existing users and direct user assistance is even more complex, as one much know which help command was run and on which wallet version.

What actual user knows to type `help` but then ends up overwhelmed by the amount of output? The likely scenario is that any user falling into that second camp would be typing random things in a vain attempt to get help, and they should be shown the simplified output. To me, the question isn't whether to re-introduce `help <command>` for all commands, but whether to completely revert the whole notion of burying help for all commands behind `help_advanced`, preferring, instead, to provide simplified help to users who seem to need it because either a) they asked for it explicitly; or b) they're flailing at the keyboard.

## selsta | 2022-02-19T04:34:22+00:00
I think this issue is resolved with https://github.com/monero-project/monero/pull/6614

# Action History
- Created by: rbrunner7 | 2020-05-02T12:59:09+00:00
- Closed at: 2022-02-19T04:34:22+00:00
