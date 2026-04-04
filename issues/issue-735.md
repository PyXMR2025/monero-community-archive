---
title: Localized user-guides not using local png folders
source_url: https://github.com/monero-project/monero-site/issues/735
author: el00ruobuob
assignees: []
labels: []
created_at: '2018-05-13T17:53:58+00:00'
updated_at: '2018-08-25T05:19:26+00:00'
type: issue
status: closed
closed_at: '2018-08-25T05:19:25+00:00'
---

# Original Description
I was testing the #734 i made to partially close #729 and figured out the screenshots were not updated.
It was because i only updated the /_i18n/XX/ressources subfolder and not the /ressource subfolders.

So it means, our screenshots, localized or not, are not beeing used in the user guides.

That's too bad, because it make sense to have the screenshot in the right language.
I.e., i re-did most of the screenshots of #649 in #697 as the Windows UIs are displaying differently in french.

Is it a known issue @erciccione & @rehrar?

# Discussion History
## el00ruobuob | 2018-05-13T20:28:55+00:00
As a woraround, i believe you are copying the png folders each time you build the site? Couldn't it be automated by Jekyll, or any ruby script?
Edit: I added the following piece of code to by build script:
```bash
local=(`ls _i18n/ | grep -e ^..$ | grep -v en`)
for i in "${local[@]}"
do
        cp -R _i18n/$i/resources/user-guides/png _site/$i/resources/user-guides/
done
```

## el00ruobuob | 2018-06-08T05:57:07+00:00
@rehrar & @luigi1111 The current build of getmonero.org is not using the localized screenshot.
Jekyll is not using the _i18n/***/png folders by himself.
Could you apply the workaround above so that readers will have their localized version of screenshots?

## el00ruobuob | 2018-07-10T15:25:22+00:00
@erciccione its +improvement + in progress through #798 

## erciccione | 2018-07-12T15:15:09+00:00
+improvement
+in progress

## el00ruobuob | 2018-08-25T05:18:20+00:00
This could be closed

## el00ruobuob | 2018-08-25T05:19:25+00:00
Fixed

# Action History
- Created by: el00ruobuob | 2018-05-13T17:53:58+00:00
- Closed at: 2018-08-25T05:19:25+00:00
