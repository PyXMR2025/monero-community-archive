---
title: Alias ​​proposal
source_url: https://github.com/monero-project/monero/issues/1974
author: bart886
assignees: []
labels: []
created_at: '2017-04-14T13:38:53+00:00'
updated_at: '2017-09-22T05:22:16+00:00'
type: issue
status: closed
closed_at: '2017-09-21T09:00:31+00:00'
---

# Original Description
Proposes to put aliases into the command. The user manually sets the skin for the most commonly used functions. Of course in the cli version.

# Discussion History
## voidzero | 2017-04-14T20:23:58+00:00
Can you provide some examples?

## moneromooo-monero | 2017-04-16T09:52:01+00:00
Like "alias sendmommy=transfer 4 4xxxxxx", then using "sendmommy 10" ?

It sounds simple enough, though not something we'd spend much time on. Patches maybe welcome, depends on the intrusiveness/complexity of the patch, but I think it could be fairly simple (though how to do the persistence might make it a bit more annoying/intrusive).


## voidzero | 2017-04-21T01:52:12+00:00
Wouldn't some kind of `rlwrap`-like application be more suitable for this? `rlwrap` already maintains input history, so maybe some kind of `rlwrap` on steroids, where you could define a bunch of commands (that start with a certain prefix character) in a text file. Just a thought.

## tewinget | 2017-04-21T02:59:28+00:00
Sounds to me like a job for bash completion and aliasing.

On Thu, Apr 20, 2017 at 9:52 PM, Mark <notifications@github.com> wrote:

> Wouldn't some kind of rlwrap-like application be more suitable for this?
> rlwrap already maintains input history, so maybe some kind of rlwrap on
> steroids, where you could define a bunch of commands (that start with a
> certain prefix character) in a text file. Just a thought.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/1974#issuecomment-296010785>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AE3k5rwLOLcYf215goGnTEFCZQOtccWOks5ryAvNgaJpZM4M9wKa>
> .
>



-- 
Thomas Winget
Computer Engineering
Purdue University '12


## voidzero | 2017-04-23T22:33:53+00:00
Maybe I'm not getting it, but how would you send commands to monero's CLI from an external shell?

## hyc | 2017-09-20T20:52:19+00:00
readline is natively supported now, and you can define macros using `~/.inputrc`. Can this be closed?

## moneromooo-monero | 2017-09-21T08:55:55+00:00
How to add those (I've just verified this works with monerod):

http://www.thegeekstuff.com/2014/06/linux-custom-keybindings/

+resolved


## bart886 | 2017-09-22T05:22:15+00:00
Yes

2017-09-20 22:52 GMT+02:00 hyc <notifications@github.com>:

> readline is natively supported now, and you can define macros using
> ~/.inputrc. Can this be closed?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/1974#issuecomment-330977300>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AVzNowBKVS41BeoLUWnatFlW0FjC2ayUks5skXsLgaJpZM4M9wKa>
> .
>


# Action History
- Created by: bart886 | 2017-04-14T13:38:53+00:00
- Closed at: 2017-09-21T09:00:31+00:00
