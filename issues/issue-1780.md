---
title: Introduce i18n system for the Moneropedia
source_url: https://github.com/monero-project/monero-site/issues/1780
author: erciccione
assignees:
- erciccione
labels:
- 💬 discussion
- i18n
- 📖 moneropedia
created_at: '2021-08-15T10:52:44+00:00'
updated_at: '2022-01-15T09:26:27+00:00'
type: issue
status: closed
closed_at: '2022-01-15T09:26:26+00:00'
---

# Original Description
The Moneropedia is currently in the same situation the user guides were before the refactor (see #1270). All Moneropedia entries should be easy to update and translate. Also, new entries should be added painlessly. This is not the case at the moment.

The basic idea is to use po4a as we do for the user guides to translate the content of each Moneropedia entry.

The problem is that the Moneropedia is more challenging to refactor than the user guides, because we also have to consider the ruby plugin that parses tooltip descriptions (which shows up when hovering on a word preceeded with `@` ) and an array of terms.

We could keep most of the original structure and use a combination of po4a + a script parsing only what's necessary to translate (so leaving out the front matter of each Moneropedia entry), but that would increase complexity quite a lot, since we would need to add an additional script to strip entries from their front matter, and then a "bridge" file containing the stripped entries to translate. Then po4a would work on this bridge file, feeding Weblate with strings to translate.

That's not idea, IMO the best solution is to do basically what we did in #1270 and get rid of the `moneropedia.rb` plugin. The hyperlinks to the Moneropedia entries that we have spreead across the website are useful. I would keep them but instead of triggering them with `@` we can add them manually with html + CSS. This will result in slightly more complexity for translators, but if they are correctly instructed to leave those strings alone, shouldn't be an issue.

If there are no better suggestions, i'll work on this. Note that because of the ruby script, it might be not feasible to make multiple PRs with the changes like i did with the user guides, but i might have to do a single big PR with most of the needed changes.

# Discussion History
## devuana | 2021-08-21T11:25:23+00:00
Seems a good idea to me. This way it will be much easier to 'track the status of a translated file and to reliably update the entries', as you mentioned in #1270. Plus Weblate seems an easier solution for onboarding new translators. 

## erciccione | 2021-08-22T09:19:20+00:00
After some testing, i realized that refactoring `@` links to work with only css + html is not really feasible. yaml files don't support liquid formatting, so we would need to split a paragraph every time a word needs to be linked to a Moneropedia. Not really convenient.

What we can do is to keep the structure mostly as it is. The content of the front matter would be parsed by po4a, which will display it like this (will be then parsed by Weblate):

```
"terms: [\"account\", \"accounts\", \"wallet\", \"wallets\"]\n"
"summary: \"similar in function to a bank account, contains all of your sent "
"and received transactions\"\n"
```

There is some complexity added by the `\` before `"`. People not familiar with escaping characters will be confused at first, but i think won't be a problem if we add clear instructions on these strings on Weblate (we already add instructions to multiple strings).

Translators would be instructed to add translated `terms` after the last English one (in this case `"wallets"`) and to translate the content of `summary:`.

## erciccione | 2021-08-27T10:59:18+00:00
Some updates:

While the gettextizer tool will create the rough structure mentioned above for the front matter, `po4a` is actually much smarter and able to recognize the structure front matter! This drastically decreases complexity for translators, which will be prompted with something much simpler to understand:

```
#. type: YAML Front Matter: summary
#: ../_i18n/en/resources/moneropedia/account.md:1
#, no-wrap
msgid "similar in function to a bank account, contains all of your sent and received transactions"
msgstr ""

#. type: YAML Front Matter: terms
#: ../_i18n/en/resources/moneropedia/account.md:1
#, no-wrap
msgid "[\"account\", \"accounts\", \"wallet\", \"wallets\"]"
msgstr ""
```

On Weblate only the content of `msgid:` will be shown to the user. 


I started the process of converting the guides. Now that i have familiarity with the tool (after converting all user guides), I aim to have every moneropedia entry ready to be added on weblate with one single PR for each entry. The process i'm following is:

1. Gettextize translated and untranslated documents. This will generate `.po` and `.pot` files for all languages
2. Add .config file to be parsed by `po4a` for each moneropedia entry in `po/moneropedia/ENTRY.config`
3. When the structure of all entries matches the original English file, run `po4a` against the config file added above. This will change the structure of all .po/.pot files in a smarter way, which recognizes the different markdown structures.
4. Manually tweak the template .pot file and fix any weirdness found (remove `fuzzy` for each block or po4a will ignore it when it's time to transfer it back to the .md file, the actual guide)
5. Manually fix all incongruences and inconsistencies in each `.po` file
6. Run po4a again against the config file (as in point 3)
7. Visually check the resulting markdown file to make sure everything went fine

This is a long and very time consuming process. From an early estimation i would expect each guide to take at least ~2 hours or so (depending by the complexity and amount of issues found).

## erciccione | 2021-10-16T09:05:11+00:00
Just PRd #1876, which makes the last Moneropedia entry (wallet.md) trnaslatable on Weblate. I also PRd the adjustements to the README with #1877.

After all the PRs listed above will be merged, we will only need to add all the guides on Weblate, then this issue will be considered resolved.

## erciccione | 2021-11-10T08:48:12+00:00
Almost all PRs have been merged (only one missing). We can start the process of adding the moneropedia entries on weblate. Now that there is a structure for internationalization, Moneropedia entries can be edited safely.

## netrik182 | 2021-11-17T07:56:46+00:00
> Almost all PRs have been merged (only one missing). We can start the process of adding the moneropedia entries on weblate. Now that there is a structure for internationalization, Moneropedia entries can be edited safely.

I'd like to collaborate on adding them to Weblate ErCiccione. Please let me know when you have time. We can coordinate on matrix as always.

## netrik182 | 2022-01-11T10:40:05+00:00
Moneropedia added to Weblate: https://translate.getmonero.org/projects/getmonero-moneropedia/

## erciccione | 2022-01-15T09:26:26+00:00
This is completed.

# Action History
- Created by: erciccione | 2021-08-15T10:52:44+00:00
- Closed at: 2022-01-15T09:26:26+00:00
