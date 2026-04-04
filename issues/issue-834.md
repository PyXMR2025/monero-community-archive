---
title: Use of "CLI" and its relation with translations
source_url: https://github.com/monero-project/monero-site/issues/834
author: BlackLotus64
assignees: []
labels: []
created_at: '2018-08-12T21:31:48+00:00'
updated_at: '2018-08-13T13:45:15+00:00'
type: issue
status: closed
closed_at: '2018-08-13T13:45:15+00:00'
---

# Original Description
We have had some discussion about the use of CLI in some pages of monero-site (getmonero), and we would like to open an issue about it so we can all be aware of its meaning and uses, and what should we do in translations to translate it, and make it clear if CLI is an acronym or it's a short name for ´monero-wallet-cli´.

# Discussion History
## BlackLotus64 | 2018-08-12T21:40:37+00:00
One of the issues is that lh1008 and ordtrogen say that it stands for the program ´monero-wallet-cli´, and it should be left that way in translations, or use the translated word for console/terminal followed by CLI to make it view that it in reference to ´monero-wallet-cli´.

I can understand that CLI can just be used as a short of ´monero-wallet-cli´, but those particular letters are an acronym for command-line interface, because, indeed, monero-wallet-cli is a command-line interface program, but CLI is not its own name, so I wasn't happy with using literally _the CLI_ in Spanish (which may be _la CLI_). I suggest that we just use the full name of what CLI stands for: command-line interface, and in Spanish it is _interfaz de línea de comandos_. And if it stands for ´monero-wallet-cli´, we should just use the same since it is indeed an own name.

I'm not sure what the other translations do for this cases, and I'm not able to just take a look and understand it because I only speak two languages for now, but it will be nice if we have participants who speak other languages rather than just English and Spanish, because this issue was born in a Spanish translation.

I'm looking forward to this so we all can be happy with the results and the result can also be the best one possible, @ordtrogen, @lh1008.

## lh1008 | 2018-08-12T21:57:22+00:00
I understand "CLI" stands for `monero-wallet-cli` without adding the complete `monero-wallet-cli` name. Saying "la CLI" is not a grammatical error, just as using "la internet" as "the internet". If it's confusing I suggest the following:

e.g. 
"Use the CLI to send and receive transactions."

Translation:
 - "Use la **interfaz de línea de comandos (CLI)** para enviar y recibir transacciones." **(These could be confusing for the user; specifying, "interfaz de línea de comandos", could indicate the use of the terminal in Mac/Linux or the cmd in Windows instead of the `monero-wallet-cli`)**
 - "Use el monedero `monero-wallet-cli` para enviar y recibir transacciones." 

to not be so redundant:
 - "Use `monero-wallet-cli` para enviar y recibir transacciones."



## BlackLotus64 | 2018-08-12T22:33:15+00:00
"Use monero-wallet-cli para enviar y recibir transacciones."

That's a lot better than the other sentences you wrote. Just a personal note, it's not the same as "the internet" because it's not an acronym, we must be aware that that part of the wallet program of Monero is also an acronym, because it can't be monero-wallet-command-line-interface obviously. Is not that CLI is for another reason. And like in the last example, we don't use just "net" or something like that for Internet, not in Spanish. Internet became a word even if its meaning can be also a type of acronym.

## erciccione | 2018-08-13T13:30:35+00:00
No need to open an issue about this on monero-site. This is a very minor discussion who can happen in the many channels we have available: `#monero-es` since its related to the Spanish language; `#monero-translations`, since it's a translations-related issue. Or, even better, opening an issue on one of the trackers we use for the localization workgroup - like [monero-ecosystem/monero-translations](https://github.com/monero-ecosystem/monero-translations), where all the glossaries are and where this kind of discussions can happen without clogging official moenero repositories - or Taiga. Closing this

+resolved

# Action History
- Created by: BlackLotus64 | 2018-08-12T21:31:48+00:00
- Closed at: 2018-08-13T13:45:15+00:00
