---
title: Simplify multi-language support
source_url: https://github.com/monero-project/monero-site/issues/725
author: MaxXor
assignees: []
labels: []
created_at: '2018-05-07T09:27:36+00:00'
updated_at: '2018-06-02T12:49:42+00:00'
type: issue
status: closed
closed_at: '2018-06-02T12:45:14+00:00'
---

# Original Description
The current multi-language support is hard to maintain and gets out of sync very fast. A good example how easy it can be implemented in Jekyll can be seen in https://github.com/bitcoinxt/website/pull/51. I propose that we adapt this to make it less error-prone to update or add pages to the website.

They use `jekyll-multiple-languages-plugin` and have one layout for all languages which contain placeholders like `{% t page.title %}`. Beside that the language files are simple `.yml`-files which contain the translated strings.

This issue can be used to track progress on simplifying multi-language support.

# Discussion History
## el00ruobuob | 2018-05-07T09:51:43+00:00
I'm totally in it.
But hasn't @rehrar tried to go this way already? And found a lot of issues / complications?

## MaxXor | 2018-05-07T09:56:06+00:00
@el00ruobuob He mentioned it a while ago, I don't remember the exact details though... (maybe @rehrar could list the complications here for an overview) Well, I'm sure we can find solutions for it or at least live with trade-offs. It has to be simplified imho or no one wants to keep the website up-to-date sooner or later.

## rehrar | 2018-05-08T22:19:17+00:00
Yes, some things were broken at that time, but...some things are broken now. :P With jekyll there is no good way to do this, so if things will be broken no matter what, it's probably best to implement it the way you guys are suggesting.

Edit: The big issue is, not all languages are easy to work with. Heck, some read right to left. And with the ones we have there was already cases of things breaking. I'll have to do a full website audit and overhaul for resilience and to implement the new stuff. I'll get started on that this week.

## MaxXor | 2018-05-09T06:43:03+00:00
@rehrar Nonetheless I think this is the right decision to do. I think we can fix the languages which read right-to-left later, maybe even with the plugin authors. Thanks for your work, I'll try to help where I can.

## rehrar | 2018-05-09T17:38:38+00:00
After looking at the site, the portions of the site that are not broken up into snippets (such as Guides) should remain as they are, as this will ultimately be the easier translating experience. All the other sectioned portions can be changed over to the new way.

## rehrar | 2018-05-09T17:58:59+00:00
It occurs to me that with this method, it becomes much more difficult to put the untranslated snippet in the pages. The website is actually quite complex with all of the things it has, and I'll need to think about how to do all of the little teeny things.

## MaxXor | 2018-05-09T18:11:03+00:00
Untranslated snippets should have the value copied from the english translation. We can split up the work and everyone who wants to help does a few pages.

## rehrar | 2018-05-09T18:24:10+00:00
I meant the thing on the bottom of the untranslated pages that says 'This page is not yet translated blah blah blah'. 

## MaxXor | 2018-05-09T18:51:15+00:00
Maybe just remove it altogether and just display the page in english.

## rehrar | 2018-05-09T18:52:44+00:00
From a UX perspective it's pretty important. It can confuse a user who thinks they may have navigated to the wrong page by accident. I'll see if I can't make something work with the new way of doing things somehow.

## el00ruobuob | 2018-05-18T13:34:56+00:00
@rehrar why not keeping/adding a localized page with only the snippet and an included content then?
```markdown
{% include untranslated.html %}
{% include html-content.html %}
```
This md file will be just a bridge between html and localization to include the snippet.

## el00ruobuob | 2018-05-18T21:08:07+00:00
Great minds think alike @rehrar.
I wonder if we should add a 
```yml
translated: yes / no / partially
```
Statement in yml and use it with a `{% if ... elseif ... %}` to display (or not) the untranslated message, even a different message for partial translation, and moreover tell the world not to touch those md files, and only work on the yml.

## erciccione | 2018-06-02T12:05:04+00:00
This can be closed since #744 was merged

+resolved

## erciccione | 2018-06-02T12:49:41+00:00
I'm sorry @MaxXor i just noticed maybe you wanted to keep this open

# Action History
- Created by: MaxXor | 2018-05-07T09:27:36+00:00
- Closed at: 2018-06-02T12:45:14+00:00
