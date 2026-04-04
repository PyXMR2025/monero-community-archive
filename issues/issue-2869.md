---
title: '[Feature] hardware keylogger/screenshot resistant wallet restore entry method
  for cli'
source_url: https://github.com/monero-project/monero/issues/2869
author: nasaWelder
assignees: []
labels:
- proposal
created_at: '2017-11-27T19:15:11+00:00'
updated_at: '2026-02-18T21:51:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If one of [keyboard|monitor] is physically compromised for an airgapped/liveUSB/Tails cold wallet (or for warm wallet: a non-targeted keylogger only virus), current wallet restore methods expose seed to attacker.

I realize this is very hypothetical at this point, but if a South African does ever have to flee, restoring wallet at refugee camp could have compromised keyboard...

Idea:
randomly spaced keys are displayed to user and keyboard is used to step through wordlist. Once user arrives at next key in seed, user presses number key that corresponds with correct seed word, and it is added to list. Repeat for all 25 words. I made up/down stepping keys for +/-1 word, +/- random(10,20) words, and +/- random(100,200) words to make jumping around alphabet quick but a little random.

demo:
https://github.com/nasaWelder/sandbox/tree/master/monero

I only know python, so my prototype is just a demonstration at this point. It only relies on standard library for 2.7+,3.0+ so I hope that encourages testing for yourself. It also wipes screen at exit so terminal does not show the seed if someone scrolls up. If no one picks this up It could be a good opportunity for me to learn C++.

Missing from demo:
1) at exit, public address should be displayed for user to check that input was error free, with confirmation dialogue.

If this is too trivial, I apologize. I'm new to contributing/open-source in general.

# Discussion History
## moneromooo-monero | 2017-11-27T22:59:11+00:00
Sounds like something that'd be even more useful for the GUI.

## nasaWelder | 2017-11-27T23:02:58+00:00
I bet you could use cli version as back end for gui. I make guis in python IRL. Python is so good at error Handling, I wish the gui was in that, would be so easy to contribute.

## dEBRUYNE-1 | 2017-11-27T23:05:04+00:00
@nasaWelder It's not that difficult as you think probably. This might be of help:

https://blog.cedsys.nl/misc-monero-gui-development-intro.html

## dEBRUYNE-1 | 2018-01-08T12:39:15+00:00
+proposal

## fresheneesz | 2018-01-21T00:52:07+00:00
I don't think this would materially improve the security of your monero. If someone can keylog, they can also screen capture and find out what you saw on the screen when you were typing or mouse clicking. Monero just needs hardware wallets, that'll solve the problem.

## moneromooo-monero | 2018-10-09T11:47:50+00:00
+hacktoberfest

# Action History
- Created by: nasaWelder | 2017-11-27T19:15:11+00:00
