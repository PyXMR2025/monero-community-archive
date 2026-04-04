---
title: 'i18n issue: languages are not flags'
source_url: https://github.com/monero-project/monero-gui/issues/1092
author: pazos
assignees: []
labels:
- proposal
created_at: '2018-01-23T17:05:34+00:00'
updated_at: '2018-04-02T15:40:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, first and foremost I would like to say thanks to everybody involved in monero. This seems like a great community to join 👍 So far I've installed monero on Ubuntu and I'm starting to read the documentation.

There is a "little" issue on the GUI that annoys me: [languages are not flags!](http://www.flagsarenotlanguages.com/blog/why-flags-do-not-represent-language/)

I know there are a lot of countries which are tied to a language unspoken in the rest of the world, but is not the case for a bunch of languages (spanish, english or portuguese come to my mind).

So the whole folder [flags](https://github.com/monero-project/monero-gui/tree/master/lang/flags) just doesn't make sense for me and I rather prefer to following these   [practices for representing languages](http://www.flagsarenotlanguages.com/blog/best-practice-for-presenting-languages/)

Please, share your opinion

# Discussion History
## danrmiller | 2018-01-24T05:01:49+00:00
These same thoughts come into my mind every time I see a PR about what flag to use for a translation.

## erciccione | 2018-01-24T14:30:20+00:00
I agree we could use a better way to show languages, but i think can be tricky. If we leave only the languages (with no flags) is going to be extremely ugly and confusing. We might use something as described at the end [of this article](http://daily.unitedlanguagegroup.com/stories/editorials/inside-design-language-selector-no-flags). "users are able to select from a variety of supported languages that are found in their chosen country."

## pazos | 2018-01-24T16:39:47+00:00
@erciccione: In the example you linked that makes senses because LandRover.com provides different services for different countries. The same form is used to lookup for localization and language. AFAIK monero-gui has no plans to provide such localization based services.

In the context of a web page this could work for services like "where to buy", but forcing users to choose their country to then be able to select their language doesn't seems a good point for me in a project like monero

## erciccione | 2018-01-25T12:33:43+00:00
Yes it's not optimal, but if we agree that a text only page would be ugly and confusing, i honestly don't see any other viable option for the GUI. Do you have any practical suggestion to improve the present way languages ar shown?

## pazos | 2018-01-25T18:41:34+00:00
Just a quick draft of my suggestion :)

Original:

![monero-welcome-current](https://user-images.githubusercontent.com/975883/35405600-f88cdc2e-0206-11e8-97c8-81cbfdd4698d.png)

New:

![monero-welcome-new](https://user-images.githubusercontent.com/975883/35405615-02676d04-0207-11e8-87fa-032838027a6e.png)


An optional "Please select your language"  between the globe icon and the language selector could be added.

## erciccione | 2018-01-25T19:44:40+00:00
I'm not sure about the "welcome" part, since somebody may rise the issue of why some languages are chosen for the welcome message and other are not, but i like it! 
In case, would you be able to implement it yourself?

## pazos | 2018-01-26T01:57:40+00:00
of course, the welcome part should have all languages supported :)

I'm new in QML, but I used pyqt a few times. I'll check the sources and ask for help if I need it.

Give me a few weeks

PD: "World Flags Globe" image is from [wiki-commons](https://commons.wikimedia.org/wiki/File:GDJ-World-Flags-Globe.svg). Are we ok with it?


## erciccione | 2018-01-26T12:39:37+00:00
Perfect, thank you! Yes sure, no problem for the image
If you need help you can find it here, on `#monero-gui` or `#monero-dev` on Freenode

## sanderfoobar | 2018-03-30T00:46:31+00:00
+proposal

## sanderfoobar | 2018-03-30T00:46:59+00:00
pinging @GBKS

## GBKS | 2018-03-30T20:16:35+00:00
Languages are definitely not flags, but they do add a nice visual elements to the page. If you'd like to avoid it, maybe go for a simple list so people can quickly click through and get to the wallet. This is a very straightforward screen, so my approach would be to keep it simple, like the attached image. Just my 2 cents.

![onboarding - choose language 2x](https://user-images.githubusercontent.com/695901/38152322-3bc4c4ec-3435-11e8-87de-430f7aeeccca.png)

## pazos | 2018-04-01T20:39:21+00:00
awesome KISS design @GBKS. I like it! @skftn, @erciccione  what do you think?  

## erciccione | 2018-04-02T15:40:36+00:00
I like it. Simple and clean. Let's just keep in mind the available languages will be 29 not 9, so the format should be a minimum flexible.

# Action History
- Created by: pazos | 2018-01-23T17:05:34+00:00
