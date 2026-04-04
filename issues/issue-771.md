---
title: Library page
source_url: https://github.com/monero-project/monero-site/issues/771
author: el00ruobuob
assignees: []
labels: []
created_at: '2018-06-21T14:04:51+00:00'
updated_at: '2018-06-29T13:00:22+00:00'
type: issue
status: closed
closed_at: '2018-06-29T13:00:22+00:00'
---

# Original Description
As discussed on #769, i am begining the implementation of a new page for pubished books and other stuffs like this.
I open this issue to discuss it.
Several points:
- the page URL should be at root level: no problem, it's just as technical specs.
- page name:
  - "Library" was suggested
  - ~~I found "bookshop" more elegant~~ @MaxXor had a good point for library
- Content:
  - First content is obviously "books", with zero to monero & mastering monero
  - I was thinking to a second content for "revuo monero" if @rehrar is still planning on releasing new versions
- Look&feel:
  - I was thinking to a basic up to down list, like [merchants](https://getmonero.org/community/merchants/) with only one item per line, and a description on the right.

What else? Discussion's open.

# Discussion History
## UkoeHB | 2018-06-21T19:33:28+00:00
@el00ruobuob  it built fine on my computer. Since it's translated = "no", it seems  the other pages display in english. Maybe copy paste into the other  files? 

The index is simple because its purpose is simple: short description,  and a link. I dont think advanced UX will improve user experience here.  You can change yml if you want, I didn't think much about it.

More generally, it would be great to get this live asap. Tweaks and upgrades are pretty low priority imo.

## el00ruobuob | 2018-06-22T04:55:57+00:00
> The index is simple because its purpose is simple: short description, and a link. I dont think advanced UX will improve user experience here. You can change yml if you want, I didn't think much about it.

@UkoeHB I'm not talking about advance UX here, just saying the librry page should be ready to include any other kind of publications, like the revuo monero.
I'm also saying that having every link hard-coded in html is a bit ugly, i'm more satisfied with an automatic generation in liquid like for merchants or IRC page.
Regarding the "short description, and a link" i totally agree, i havn't code more than this so far.

> More generally, it would be great to get this live asap. Tweaks and upgrades are pretty low priority imo.

And more generally, no need to rush: ths PR are merged by luigi once a week or every two week, unless it's an emergency, and the site is rebuild once or twice a month, unless it's an emergency. And i don't think adding a library page will be consider as an emergency by @rehrar or @luigi1111, so let take a day to discuss it and implement it right.

Btw, if you want to have zero-to-monero hosted asap, you must clean your commits on #769. Beside of the library page itself, you did 3 commits to add the pdf file: this will never be merged by @luigi1111 and 5 commits for everything is too much for a merge. you can ask for help about it on IRC channel [monero-community](irc://monero-community).

Finally, i only have one or two enhancement to do on my side to PR a proposition that satisfies your concerns and my concerns. So if no one has anything to add, like @erciccione @MaxXor @mattcode55 or @rehrar, then it will be ready to merge asap. But as mention above, never live asap it will be.

## UkoeHB | 2018-06-22T07:56:00+00:00
@el00ruobuob thank you for clarifying. Unfortunately Github.com doesn't seem to offer any tools for cleaning up commits.. I could try deleting my fork and redoing the whole process, or will your PR take care of everything (in which case I can close my disaster of a PR)?

## el00ruobuob | 2018-06-22T08:01:38+00:00
If you want, i can publish your book in my commit.
I would not have suggest it myself, as i don't want to get any credit from your huge work.

Indeed, for handling PR and cleaning stuff, i believe you should use a git client.
Either git cli command, or ths smartgit gui.
Those let you do whatever you want, like squashing commits, and so on.

## UkoeHB | 2018-06-22T08:21:20+00:00
It's fine :) your help is making this a lot easier for me. Guess Ill have to start learning git.. maybe my next writing project should be a git tutorial that isn't headache inducing.

Would you mind adding the pdf from [here](https://github.com/UkoeHB/Monero-RCT-report). It's the most up-to-date version. Thank you! 

## el00ruobuob | 2018-06-22T13:11:50+00:00
Almost done. I'm adding the revuo monero in a magazines section.
It's all generated, like for merchants, but localized. maybe will it be a good POC to discuss #768?

## el00ruobuob | 2018-06-22T13:52:57+00:00
Change published. Was it fast enough @UkoeHB ? :wink:

## SamsungGalaxyPlayer | 2018-06-22T15:15:48+00:00
Having a library is a great idea.

## erciccione | 2018-06-25T09:22:19+00:00
~+enhancement~ (ehm ehm)
+in progress

## erciccione | 2018-06-25T09:55:11+00:00
+improvement

## el00ruobuob | 2018-06-28T19:25:49+00:00
this can be closed @erciccione 

## erciccione | 2018-06-29T12:55:34+00:00
+resolved

# Action History
- Created by: el00ruobuob | 2018-06-21T14:04:51+00:00
- Closed at: 2018-06-29T13:00:22+00:00
