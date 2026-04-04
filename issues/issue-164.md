---
title: Translations not working - selected language not used
source_url: https://github.com/monero-project/monero-gui/issues/164
author: ghost
assignees: []
labels:
- resolved
created_at: '2016-11-14T06:29:30+00:00'
updated_at: '2017-08-07T17:40:07+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:40:07+00:00'
---

# Original Description
I have tried to activate german and italian translations in `lang/languages.xml`. The languages are available in the welcome screen, and once selected activated for the first wizard page. But the application itself does not use the selected language. The language selection is also not persisted in the property store of Qt (tested on MacOS):

```
# defaults read org.getmonero.monero-core
{
    "account_name" = foo;
    "allow_background_mining" = 0;
    "auto_donations_amount" = 0;
    "auto_donations_enabled" = 0;
    "daemon_address" = "localhost:18081";
    "is_recovering" = 0;
    language = "US English";
    locale = "en_US";
    ...
}

```

There has already some work done for translations (TranslationManager.cpp, WizardWelcome.qml), but I have basically no idea how the translation stuff should work.

Perhaps someone can have a look at it, so that we can add some more languages.

# Discussion History
## Jaqueeee | 2016-11-14T14:49:30+00:00
@mbg033 can you confirm if translations are working or if they aren't fully implemented yet?


## mbg033 | 2016-11-15T23:29:40+00:00
@Jaqueeee yes translations are working but there should be actual translated strings. Also, I can confirm "language" and "locale" settings persists. At least on Ubuntu. 
This issue could be with Debug build - long time ago I disabled translations update/generation for debug build as it forced re-link everytime, which took about 30 seconds. Recently I figure out if we link debug monero-core with debug libwallet_api - it processed quite fast, so I will enable "translations update for debug build" in next PR

![image](https://cloud.githubusercontent.com/assets/411612/20328581/90d6b032-aba4-11e6-845d-96175ebde22f.png)


## ghost | 2016-11-17T21:06:51+00:00
**Update**: My build works now, but the language selection is still not reliable on MacOS. I can select one of the languages, and the language is active until I select the wallet which should be opened:

![image](https://cloud.githubusercontent.com/assets/2729275/20673579/ee0e9d88-b585-11e6-8dd3-a256297c96a0.png)

After the wallet file has been selected, the language switches back to English:

![image](https://cloud.githubusercontent.com/assets/2729275/20673599/01679fb0-b586-11e6-9605-7a29ab0f67b7.png)

Is this only a MacOS issue?


## ghost | 2016-12-05T08:38:26+00:00
**Update**: After I changed the MacOS `defaults` with the following command, the language is used for the UI: ``defaults write org.getmonero.monero-core locale de``. So it seams the selected language is not persisted under MacOS.

## dEBRUYNE-1 | 2017-08-07T17:34:14+00:00
+resolved

# Action History
- Created by: ghost | 2016-11-14T06:29:30+00:00
- Closed at: 2017-08-07T17:40:07+00:00
