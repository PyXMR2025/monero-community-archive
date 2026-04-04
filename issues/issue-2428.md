---
title: Improve README
source_url: https://github.com/monero-project/monero-site/issues/2428
author: jermanuts
assignees: []
labels: []
created_at: '2024-11-23T08:40:06+00:00'
updated_at: '2024-11-25T15:12:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The current README is confusing, long and contains a lot of grammar issues. I found myself opening PRs which is not up to the standard/structure of this repository as @plowsof kept noting, but it is because _none_ of that is mentioned in the README.

Here are the few things that I found to be missing in the README (list is not exhaustive), please comment with other improvements you want to see:

* For each PR have a separate branch with a decent short description

* The commit message should have page name before it, for example: downloads: improve wallets description, User Guides: write a new guide about X...

Mention that Github [generated table of contents](https://github.blog/changelog/2021-04-13-table-of-contents-support-in-markdown-files/), so readers can navigate easily (I myself didn't know GitHub had this feature 🤣 and [found about it](https://github.com/monero-project/monero-site/pull/1975#pullrequestreview-1005766078) from selsta's comment)

>This website is completely open-source however and anything and everything is available for changing should the community deem it necessary.

change it to: This site is completely open source, and everything is open to change if the community deems it necessary.

Add hyperlinks to file paths in README like `_includes/onion.html` and `/onion.txt`, also why is the onion subdomain not in _includes/onion.html?

I think we stopped using GitHub Project board? should we not mention it in [PR workflow](https://github.com/monero-project/monero-site?tab=readme-ov-file#pr-workflow)?

Translation (rip) while we wait for someone to take for it, [Localization Workgroup](https://github.com/monero-ecosystem/monero-translations) should be removed as Erc stopped maintaining it.

# Discussion History
## HardenedSteel | 2024-11-24T23:39:48+00:00
relevant to CONTRIBUTING.md

## plowsof | 2024-11-25T08:56:43+00:00
HardenedSteel is correct, this is for contributing.md. there is a pull request (or something merged) regarding adding the filename being edited in the commit to monero-core repo somewhere. we can add it to contributing.md , but its not a priority.  Alot of the times this is subjective for the maintainer. they may just be asking for a helping hand to help organise the merge list and anticipate merge conflicts.

The first half of this issue is just an update on your journey of earning your "contributor" flair. and part of being a good git-izen. no more making pull requests using master... if a maintainer asks you to rename a commit or reviewers ask for changes you don't spend weeks avoiding it... or creating a new branch to make the PR with changes instead of learning... you can rebase... amend... we're all proud of your journey and looking on with pride.

There are actionable tasks mentioned in this issue. 

## plowsof | 2024-11-25T15:12:02+00:00
https://github.com/monero-project/monero/pull/9451 for commit title best practices.

This issue does not mention the pitfalls of updating wallets on the downloads page + mobile view (which can and should be generated progrsmatically anyway) but we're getting a new site soon(tm)


# Action History
- Created by: jermanuts | 2024-11-23T08:40:06+00:00
