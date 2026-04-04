---
title: Fix insane number of duplicated png files used for user guides
source_url: https://github.com/monero-project/monero-site/issues/1082
author: erciccione
assignees:
- erciccione
labels:
- performance
created_at: '2020-07-15T18:33:46+00:00'
updated_at: '2020-11-16T19:10:04+00:00'
type: issue
status: closed
closed_at: '2020-11-16T19:10:04+00:00'
---

# Original Description
While upgrading a user guide I realized that the files contained in /resources/user-guides/png are useless. All screenshots used by the guides are in _i18n/$LANG/resources/user-guides/png. The thing is that every language has its own png folder, but most of the screenshots are in english. This means we have a total of **1430**  (110 * 13 languages) pictures used for the user guides in the repository, when we could have only **110**. All screenshots (or at least the vast majority of them) are duplicates.

This is a huge waste of space. I believe that by fixing this issue we could save at least 120 MB. The current size of the entire repository is about 450 MB.

Jekyll doesn't handle I/O very well, but anything would be better thant the current system. I will investigate this issue further, but resolving it will require a deep check all user guides for each language one by one, so it could require some time.

# Discussion History
## erciccione | 2020-07-15T19:19:48+00:00
Removing the "priority" label after a discussion in #monero-site:

```
18:41:18 <ErCiccione[m]> So, today i found out that 1/4 of the repository is made by duplicate screenshots -_-. I'm not gonna lie, i screamed a lot: https://github.com/monero-project/monero-site/issues/1082
18:44:00 <fluffypony> hmmmm
18:44:39 <fluffypony> ErCiccione[m]: removing it won't change the repo size
18:45:37 <fluffypony> it will remove it out of the working directory, but it'll remain in .git as it's historical
18:45:38 -xmr-pr- erciccione opened pull request #1083: Update screenshots of user guide 'verification-windows-beginner.html' ...
18:45:38 -xmr-pr- > https://github.com/monero-project/monero-site/pull/1083
18:45:38 -xmr-pr- erciccione opened issue #1082: Fix insane number of duplicated png files used for user guides
18:45:38 -xmr-pr- > https://github.com/monero-project/monero-site/issues/1082
18:46:07 <fluffypony> so you might as well not bother
18:46:39 <ErCiccione[m]> yes sure, the git repo is gone at this point. But would be 120MB less heavy on people's hard drive, no?
18:46:45 <moneromooo> It fixes runaway repo growth though.
18:47:04 <fluffypony> nope
18:48:01 <fluffypony> moneromooo: sure, but only if we're adding new languages or new user guides
18:48:26 <fluffypony> I don't disagree with finding a way to tell jekyll "if this png doesn't exist translated use the default one"
18:49:23 <fluffypony> also one nice thing ErCiccione[m] is that if these pngs have the same hash then it'll only store one blob for the history
18:49:27 <fluffypony> and not hundreds of them
18:49:33 <ErCiccione[m]> O yeah i got it now. The thing is that right now to change one user guide's PNGs we have to change all screenshots for all languages. That will make the history heavier with each PR and doesn't make any sense
18:49:42 <moneromooo> Oh, that's a good point. I forgot about this...
18:50:46 <fluffypony> you might be able to do it in Liquid, ErCiccione[m]
18:51:31 <ErCiccione[m]> yeah that make sense. But still, changing more than 100 pictures when changing one user guide is insane. I think i will put all png's in the resources folder and create a folder for the languages only if the screenshots get updated
18:51:50 <ErCiccione[m]> liquid doesn't handle files very well, needs some tweaks
18:52:44 <ErCiccione[m]> basically we have to tell it manually where to go get the files. The "if file exists" thing doesn't work with liquid afaik
18:53:43 <fluffypony> https://stackoverflow.com/questions/16528783/check-for-existence-of-file-using-jekyll
18:55:06 <fluffypony> looping through site.static_files is inefficient, but given that we jekyll build infrequently I don't think it's a problem
18:55:08 <fluffypony> else you have to do it in Ruby :-P
18:55:10 <ErCiccione[m]> Yeah i already read that for another PR i was working on (the video in the homepage. That's the only way to do it, but i remember being problematic for some reason
18:55:34 <asymptotically> are there any other changes to the _config/nginx.conf other than the version numbers?
18:56:51 <ErCiccione[m]> asymptotically: that config file is quite old, may be very different now. I think binaryfate said he will upload an updated one
18:59:21 <ErCiccione[m]> anyway. I feel better knowing that the size is either not affected or there is nothing to do about it anymore. Thanks fluffypony :P
18:59:42 <asymptotically> not sure why the `rewrite ^ /cli/montello.tar.bz2 redirect;` goes from https to http
19:00:07 <ErCiccione[m]> Will change it anyway, but i can remove the "priority" label
```

In any case would remain a problem if we want to add languages or guides (and we want to add both, possibly). Also, changing 10 screenshots will result in actually creating a PR which changes 130 screenshots (10*13) and that is just more noise and efforts. So i think we should change it, but it's not urgent anymore. Beside the fact that the screenshots of some languages are outdated and the /resources/user-guides/png folder is partially useless and some guides uses it and others don't.

# Action History
- Created by: erciccione | 2020-07-15T18:33:46+00:00
- Closed at: 2020-11-16T19:10:04+00:00
