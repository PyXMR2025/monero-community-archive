---
title: Consider putting downloads in a separate submodule?
source_url: https://github.com/monero-project/monero-site/issues/393
author: hyc
assignees: []
labels: []
created_at: '2017-09-10T12:39:42+00:00'
updated_at: '2020-04-07T09:31:27+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:31:27+00:00'
---

# Original Description
This repo is particularly huge and slow to clone. Is it because the downloads/binaries are part of the repo?

# Discussion History
## fluffypony | 2017-09-10T12:59:40+00:00
@hyc Huh? They're not at all; total size is 95.7mb including full git history, actual data size is 47.4mb. The offending folder is the ```media``` folder, which has the 4 Monero videos in.

## mattcode55 | 2017-09-10T13:07:51+00:00
Would it be worth looking at [git-lfs](https://git-lfs.github.com/) for storing the videos?

## hyc | 2017-09-10T13:08:14+00:00
OK. Didn't actually look to see where the space was going, but it was a lot longer to download than I expected.

## fluffypony | 2017-09-10T13:23:40+00:00
@mattcode55 if the videos get larger, sure, but seeing as how the site is well under half the size of the CLI project I don't think we need to worry about it.

## rehrar | 2017-09-20T05:12:14+00:00
I have compressed the videos. I experiment with compressing further while testing to see when there is great loss of quality. The choice to keep the media files on the site itself is for Tor-friendliness.

## QuickBASIC | 2017-10-23T11:41:08+00:00
+discussion

## rehrar | 2017-10-25T17:21:17+00:00
This may still be something worthwhile to do. This would allow all of the sensitive links to be controlled by the Core Team, while it may allow additional collaborators on the site repo if it was ever called for in the future.

## QuickBASIC | 2017-10-25T17:58:17+00:00
While I agree with you, @rehrar, I don't know if it's worth the added complexity at the moment. As long as maintainers don't merge things willy-nilly, collaborators do a fine job of reviewing changes to the site. (I for one check the diffs religiously if it's the Downloads page with hashes or the one with the dev donation address.)

## rehrar | 2017-10-25T18:03:21+00:00
Indeed. Key wording there being "in the future". Don't see it as being needed right now, as Luigi gets into the swing of things. 

## erciccione | 2018-06-25T10:06:00+00:00
What is the feeling about this at the moment? Is a submodule needed at this state of things?
If not i would close this issue, a new one can be opened if necessary

## fluffypony | 2018-06-25T10:09:06+00:00
@erciccione see my comment on the podcasts issue - I'd vote for moving the videos on to downloads.getmonero.org and having a repo for that.

## erciccione | 2018-06-25T10:47:30+00:00
> I'd vote for moving the videos on to downloads.getmonero.org and having a repo for that.

+1
see [my comment in #249](https://github.com/monero-project/monero-site/issues/249#issuecomment-399910088)

## erciccione | 2020-04-07T09:31:27+00:00
This issue was discussed and closed on gitlab.

# Action History
- Created by: hyc | 2017-09-10T12:39:42+00:00
- Closed at: 2020-04-07T09:31:27+00:00
