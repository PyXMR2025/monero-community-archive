---
title: rlwrap is not entirely safe as recommended in the readme
source_url: https://github.com/monero-project/monero/issues/1075
author: PsychicCat
assignees: []
labels: []
created_at: '2016-09-15T03:25:55+00:00'
updated_at: '2016-10-04T22:16:51+00:00'
type: issue
status: closed
closed_at: '2016-10-04T22:16:51+00:00'
---

# Original Description
rlwrap ignores password (e.g. '******') input automatically, so it won't store your password. 

but it does not know how to ignore input from prompts like `Specify Electrum seed:`, and probably some other prompts we don't want to have saved in history.

I'm curious how to add a filter to rlwrap if anyone is good with that. 

If filters cannot be added I suggest the README is edited to beware not to use rlwrap if you are going to be entering sensitive data like mnemonic seed, private keys, etc.


# Discussion History
## moneromooo-monero | 2016-09-16T19:54:43+00:00
from man rlwrap:

```
   -a, --always-readline [password_prompt]
          Always  remain  in "readline mode", regardless of command's terminal settings.  Use this option if you want to use rlwrap
          with commands that already use readline.  NB: With this option, rlwrap will echo (and save) passwords,  unless  you  give
          command's  password  prompt  as  an  argument.   The argument is optional; if given, it has to directly follow the option
          without an intervening space.
```

You might be able to pass several -A options...


## PsychicCat | 2016-09-16T20:00:47+00:00
Yeah, I tried -a but it doesn't seem to work with multiple spaces. I will do some more research on it this weekend and try to find a solution.

for example, this works:

```
rlwrap -apassword: ./simplewallet
```

these do not:

```
rlwrap -aSpecify Electrum seed: ./simplewallet
rlwrap -a="Specify Electrum seed:" ./simplewallet
rlwrap -a"Specify Electrum seed:" ./simplewallet
rlwrap -aSpecify\s+Electrum\s+seed: ./simplewallet
```


## moneromooo-monero | 2016-09-17T14:56:36+00:00
Too bad. I added a note in the README about this then. Thanks for the warning.


## voidzero | 2016-09-20T16:27:59+00:00
I tried this too, and when I specified the following command:

<pre>rlwrap -a'Specify Electrum Seed:' ~/.monero/monero-wallet-cli</pre>

the wallet did run, but the password input was no longer hidden with asterisks, it was shown in plain text.


## luigi1111 | 2016-10-04T22:16:51+00:00
Closed via #1083 


# Action History
- Created by: PsychicCat | 2016-09-15T03:25:55+00:00
- Closed at: 2016-10-04T22:16:51+00:00
