---
title: Introduce i18n system for user guides
source_url: https://github.com/monero-project/monero-site/issues/1270
author: erciccione
assignees:
- erciccione
labels:
- '📚 docs: user guides'
- enhancement
- i18n
created_at: '2020-10-24T14:13:35+00:00'
updated_at: '2021-04-28T12:47:39+00:00'
type: issue
status: closed
closed_at: '2021-04-28T12:47:39+00:00'
---

# Original Description
User guides and Moneropedia entries are currently translated manually one by one, which makes impossible to track the status of a translated file and to reliably update the entries. Furthermore, changing/adding an entry requires editing a huge amount of files. This was recently mitigated for the Moneropedia (#1198), but the system as a whole remains broken and unmaintanable.

About half website wasn't adapted correctly to the redesign, which was sloppyly implemented and, beside breaking important functionalities, was only partly adapted to the new i18n system: FAQ, footers, navigation menu, Roadmap, User guides, Moneropedia and Hangouts were left out for some reason or implemented uncorrectly. I've been fixing them all during this year and then i added them to Weblate. Now only user guides and Moneropedia are left. These two are much more complex to refactor, because during the years many translations were added. This hugely complicates things.

I've been thinking on ways to fix the system. The best option is to leave the markdown files as they are and use a converter to generate strings and serve them to weblate.

### Process
We will first introduce this for the user guides. After it will be well tested, we can adopt it for the Moneropedia as well.

The plan is to use `po4a`, a very versatile converter which we will use to extract the English text of a markdown document and put it into a tamplate file (`.pot`). Since we have documents already translated, we will have to extract the translated strings from these files, so that we don't need to retranslate them all. For this process to be successful, all files must have the same structure.

The extracted strings will be added to dedicated files in this repository and Weblate will pick them up. Translators will work on them on Weblate, which will commit the changes to these `.po` files. The translated strings will then be extracted from the .po files and transferred to the markdown documents, which will be picked up by Jekyll, as usual.

For a detailed overview of how po4a will work, see [this document](https://www.systutorials.com/docs/linux/man/7-po4a/).

Using this converter will allow us to have a system for translating markdown files, without making time consuming and invasive changes to the system we already use. In fact, jekyll will still work with the markdown files. The translation system will be separated entirely. Leaving the markdown files as they are will also make us ready for when Weblate will support markdown files (https://github.com/WeblateOrg/weblate/issues/3106) and using po4a won't be necessary anymore.

### What needs to be done

- [x] The open PR translating user guides (German: #1224 #1249 #1250 #1251 #1252 #1253 #1254 #1255. Norvegian: #1266 but more will come) must be merged/closed, so that it will be possible to work on the next point

- [x] All user guides in all languages must have their structure standardized and fit the English version.

- [x] Create the template file from the English user guides then extract the strings from each translated document. The resulting `.po` files will be feeded to Weblate

- [x] Add new 'user-guides' project in the [getmonero component](https://translate.getmonero.org/projects/getmonero/) on Weblate. This project will host the strings for the user guides and make them available to translators.

# Discussion History
## erciccione | 2021-01-04T09:48:58+00:00
> The open PR translating user guides (German: #1224 #1249 #1250 #1251 #1252 #1253 #1254 #1255. Norvegian: #1266 but more will come) must be merged/closed, so that it will be possible to work on the next point

Only  #1326 #1332 #1339 and #1396 missing to complete the first task.

## erciccione | 2021-01-23T13:14:13+00:00
Second task will be completed once all PRs which uniform the user guides will be merged. After that's done, i'll start step 3.

## erciccione | 2021-03-06T10:23:42+00:00
po4a seems to have problems with encoding. We have to wait for an input from the po4a developers for an idea of what's the problem. See https://github.com/mquinson/po4a/issues/201#issuecomment-788880446.

In the meantime i also set a bounty of 1 XMR for whomever will be able to add Markdown support to Weblate (https://github.com/WeblateOrg/weblate/issues/3106#issuecomment-785963224). When that happens, we will be able to translate markdown documents natively on Weblate, without passing through po4a.

One of these two situations need to unlock for us to be able to resolve this issue. Other ideas are welcome, but consider that i already researched and tested other solutions, like converting the docs to html (using pandoc), but the results were not really great.

## mquinson | 2021-03-08T08:18:27+00:00
If I may, it seems that only po4a-gettextize has such a problem. You may want to give po4a(1) a try to see if it fixes your problem.

## erciccione | 2021-03-17T09:49:51+00:00
@mquinson thanks for chiming in, it's appreciated :)

I've been banging my head on this for days, but i'm not finding a way to mimic the behaviour of po4a-gettextize (transfer existing translations from a .md to a .po file) using only po4a. I was able to configure everything else. Am i missing something? any hint?

## ghost | 2021-03-19T23:23:09+00:00
@erciccione I believe it works if you specify the localized charset:

```
po4a-gettextize -f text -L UTF-8 -m {markdown source file} -l {markdown localized file} -p {new po}
```

## erciccione | 2021-03-20T08:01:43+00:00
> @erciccione I believe it works if you specify the localized charset:

I already tried, no changes.

## erciccione | 2021-03-20T13:29:09+00:00
I could reproduce the problem on an Ubuntu VM, but i managed to resolve on my OS by tweaking the locale.

## erciccione | 2021-04-02T08:34:19+00:00
All user guides (except one[1]) have been gettextized. Next step is to have all the PRs listed above merged so that the work on Weblate can start: translators will need detailed instructions on Weblate to be able to translate properly and only the parts that should be translated.


[1] The user guide multisig-messaging-system.md is extrenely long and not really useful for the average user. Translating it take as much as translating all the other guides and i don't think it worth it. We are keeping the 2 translations we have (German and Norwegian), but i don't plan to add support for this guide on Weblate.

## erciccione | 2021-04-04T09:17:05+00:00
The first user guide is now translatable on Weblate: https://translate.getmonero.org/projects/getmonero-user-guides/cli_wallet_daemon_isolation_qubes_whonix/.

The Monero Localization Workgroup will test it soon. If everything goes fine i'll start adding the other guides.

## erciccione | 2021-04-28T12:47:39+00:00
All user guides are uploaded and organized on weblate: https://translate.getmonero.org/projects/getmonero-user-guides/

Translators are already working on the user guides. This is finally resolved :)

# Action History
- Created by: erciccione | 2020-10-24T14:13:35+00:00
- Closed at: 2021-04-28T12:47:39+00:00
