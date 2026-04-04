---
title: why not using GNU gettext instead pootle for i18n and l10n?
source_url: https://github.com/monero-project/monero-gui/issues/1973
author: nuriyevn
assignees: []
labels:
- invalid
created_at: '2019-02-26T14:39:08+00:00'
updated_at: '2019-03-01T13:30:39+00:00'
type: issue
status: closed
closed_at: '2019-03-01T13:27:40+00:00'
---

# Original Description
No description

# Discussion History
## selsta | 2019-02-26T23:57:33+00:00
@erciccione chose pootle for translations. Both seem to be free software. Why would you prefer GNU gettext?

## nuriyevn | 2019-03-01T12:56:20+00:00
I worked with gettext. I heard a lot about gettext, I used a lot gettext, but I've never heard about pootle. So that's why I am asking why not choose standard tool instead of some marginal one? Does pootle has more pros and fewer cons like gettext?
I mean this is not good for those who want to translate instead of spending time to translate someone has to spend time to study pootle, especially if those translators does it for free. I don't know which part of the body you usually use to make decisions :) but frankly this is a bad decision and simply because it's an open source doesn't make it automatically brilliant.



## nuriyevn | 2019-03-01T12:58:15+00:00
Sorry, maybe I am saying a bit harsh things :) but I am really worried about XMR and it's future.

## sanderfoobar | 2019-03-01T13:03:02+00:00
Please (technically) specify why one thing is better than the other. I understand that you are used to GNU gettext, this however is no argument.

Pinging @erciccione 

## selsta | 2019-03-01T13:19:42+00:00
I’ve looked into this. Pootle and gettext are different things. Pootle is an online translation interface/tool, gettext is a whole translation system that can be used in combination with Pootle.

Pootle directly works with Qt .ts files, if we’d use gettext we’d have to convert our .ts files to .po files, translate and then convert them back. This doesn’t make sense for us.

We had a lot of success getting new translators thanks to Pootle, the web interface allows that even people who have no experience with translations can get into it quickly.

## sanderfoobar | 2019-03-01T13:20:57+00:00
+invalid

## erciccione | 2019-03-01T13:25:50+00:00
Hi @nuriyevn thank you for your input, but i suggest to look more deeply into the tool you are suggesting related to Monero's codebase.

Gettext works with .po files, Monero with .ts, that means to use gettext we should use a .po -> .ts converter. The most used one is *po2ts*, which is developed by... Pootle. Why not use directly Pootle, which support natively .ts files?

> I mean this is not good for those who want to translate instead of spending time to translate someone has to spend time to study pootle

There isn't really much to study, but in any case, i'm creating a graphical guide to help translators, many resources can be found online and translators can ask for supprot to the localization workgoup.

> but frankly this is a bad decision and simply because it's an open source doesn't make it automatically brilliant.

We tested 3 different platforms and went for pootle, you don't seem like to really know the technical differences between these services, so i'm sorry, but the fact you think it's a bad idea it's not really backed up by solid reasons.

Basically, between all the localization tools i know, the last one i would suggest is gettext.

Edit: to be more clear: Pootle supports gettext (actually, it's the default option), we don't use it because it's just useless for us.

# Action History
- Created by: nuriyevn | 2019-02-26T14:39:08+00:00
- Closed at: 2019-03-01T13:27:40+00:00
