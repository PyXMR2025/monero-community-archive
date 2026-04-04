---
title: Update version with every tag
source_url: https://github.com/monero-project/monero/issues/4497
author: normoes
assignees: []
labels: []
created_at: '2018-10-04T10:42:47+00:00'
updated_at: '2022-03-16T15:42:13+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:42:13+00:00'
---

# Original Description
I tend to check the version of `monero` after building from source to verify/double check the result.
I build from `master` as well as from  the latest `tag`/`release`.

I noticed the version in `src/version.cpp.in` does not always relfect the current version.

As of around 7am CEST:
The tag `v0.13.0.2-RC2` shows: `Monero 'Beryllium Bullet' (v0.13.0.1-rc-release)`
The tag `v0.13.0.1-RC1` shows: `Monero 'Beryllium Bullet' (v0.13.0.1-rc-release)`
`master`shows: `Monero 'Beryllium Bullet' (v0.13.0.1-rc-215651c)`


# Discussion History
## moneromooo-monero | 2018-10-04T10:59:45+00:00
I'd much rather we keep to normal version numbers, rather than add strings which make things confusing (except the "-master" suffix. Moreover, normal version numbers always sort properly.

## normoes | 2018-10-04T11:46:42+00:00
What are the normal version numbers, names of tags, releases, etc.?

## moneromooo-monero | 2018-10-04T13:14:50+00:00
I mean. Numeric, not alphanumeric. Like 1.3,0,1 instead of 1.3.0.2-RC2.

## gituser | 2018-10-09T20:23:37+00:00
Hey guys, please tag latest release as `v0.12.4` on github as well automatically!
https://github.com/monero-project/monero/releases

It's not convenient to check your release page via API call to get the information that latest release is `v0.12.3` instead of `v0.12.4` at all.


## gituser | 2018-10-17T14:27:16+00:00
Once again, guys the latest release marked on github is: `v0.13.0.2` BUT there is already available `v0.13.0.3`! So what's the latest release? Can you make sure that there is always proper release marked on github?

Thank you.

## moneromooo-monero | 2018-10-17T16:54:24+00:00
The latest tag is v0.13.0.3. The latest binaries are for 0.13.0.2.

## gituser | 2018-10-17T17:04:51+00:00
It's confusing. 

Would be nice if you could keep actual release number there on releases page, because I'm regularly checking it via github's API to check if I need to update monero daemon or not.

## moneromooo-monero | 2018-10-17T17:15:34+00:00
If you want binaries, use monerod's update command.
If you want source, use git and check for a new tag.

## gituser | 2018-10-17T17:25:21+00:00
> If you want binaries, use monerod's update command.
> If you want source, use git and check for a new tag.

No, I don't need binaries. I need to know the correct latest release.
I do so via github's API it's the most quick method not requiring me to sync the repository every time.
And so to speak all other cryptocurrencies, e.g. bitcoin, litecoin, dash, etc.. are maintaining correct latest release versions on the page I've mentioned before.

## selsta | 2022-03-16T15:42:13+00:00
Github should be in sync with the latest version now.

# Action History
- Created by: normoes | 2018-10-04T10:42:47+00:00
- Closed at: 2022-03-16T15:42:13+00:00
