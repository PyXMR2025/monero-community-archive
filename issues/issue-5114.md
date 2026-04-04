---
title: simplewallet.cpp file is too big for spacemacs
source_url: https://github.com/monero-project/monero/issues/5114
author: ghost
assignees: []
labels: []
created_at: '2019-02-01T05:00:29+00:00'
updated_at: '2019-02-06T01:34:54+00:00'
type: issue
status: closed
closed_at: '2019-02-05T02:26:10+00:00'
---

# Original Description
I can barely move my cursor when editing this file with the default setup of spacemacs.

My PC is AMD Ryzen 2200G, which has 4 cores!

Please make it smaller so I can edit it.

# Discussion History
## moneromooo-monero | 2019-02-01T11:01:23+00:00
The problem is your editor :)

## ghost | 2019-02-01T13:54:35+00:00
spacemacs is a legitimate editor unless I can be shown that emacs lisp sucks.

## ghost | 2019-02-04T01:07:52+00:00
I just downloaded [atom](https://atom.io/) and it seems pretty fast when editing this file, so it seems to be an issue of my editor.

Should I close this now @moneromooo-monero ?

## moneromooo-monero | 2019-02-04T15:36:18+00:00
I think so. You may want to to check config for your original editor. Like if you have syntax highlighting and the context is huge for instance, so it parses loads of code for every keystroke.


## ghost | 2019-02-05T02:26:10+00:00
The problem does seem to be context dependent, worse in some sections of the code, and workable in others. Spacemacs isn't fast to begin with anyway. Thanks for the tip.

## Lederstrumpf | 2019-02-05T10:16:44+00:00
> My PC is AMD Ryzen 2200G, which has 4 cores!

Only single-threaded performance matters in this case, because spacemacs is single-threaded.

>spacemacs is a legitimate editor unless I can be shown that emacs lisp sucks

It does, especially compared with modern lisps.

>I can barely move my cursor when editing this file with the default setup of spacemacs.
wrt. C++, I believe my configuration is the default, and I do not experience a slowdown editing this file at all.

Try launching with `emacs -Q` to skip loading of your initialization file. Editing like this should by all means be snappy. 
Next, open up as normal again, and disable minor modes that are loaded next to the C/C++ major mode. My first suspects, presumably loaded, are flycheck-mode and company-mode.

Else, [profiling](https://www.gnu.org/software/emacs/manual/html_node/elisp/Profiling.html) is always an option.

## ghost | 2019-02-06T01:11:07+00:00
I'm using `emacsclient -c -a ''` as a startup command, and there's no `-Q` for me. I think both flycheck-mode and company-mode are disabled for me by default. I'm literally using the default setup here, there's not even a c++ layer in my `.spacemacs`, it has to come pre-loaded. Profiling seems cool, I'll check it when I have some time. Thanks @Lederstrumpf

## ghost | 2019-02-06T01:34:54+00:00
OK, I can run `emacs -Q`, but that's vanilla emacs not spacemacs anymore XD I'd be better off just using Atom.

# Action History
- Created by: ghost | 2019-02-01T05:00:29+00:00
- Closed at: 2019-02-05T02:26:10+00:00
