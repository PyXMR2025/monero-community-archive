---
title: Discuss the possibility of migrating to a documentation platform
source_url: https://github.com/monero-project/monero-site/issues/1754
author: erciccione
assignees: []
labels:
- 💬 discussion
- 📚 docs
created_at: '2021-08-03T09:37:12+00:00'
updated_at: '2024-03-24T08:24:18+00:00'
type: issue
status: closed
closed_at: '2024-03-24T08:24:18+00:00'
---

# Original Description
I've been thinking again about the possibility of moving the present documentation (developer guides and user guides) to a dedicated documentation platform (like [Readthedocs](https://readthedocs.org/)). This possibility came up from time to time during the years, but nothing ever came out of it. I think it worth having the discussion to see what community and devs think about it.

Keep in mind that such migration would take a significant effort. I cannot provide more details about that because i would have to look into the details of the platforms, but i want to see what people think about it first.

Pros:

- Developers are used to docs platforms. That would make easier for them to browse and contribute to the docs
- Possibility to have docs specific for each version
- Many documentation platforms have built-in multi-language support (managing translations would be easier)

Cons:

- The migration would take **a lot** of work (but depends by what we would want to include)
- Ideally we would need to register a subdomain like `docs.getmonero.org` where the docs would be hosted.

# Discussion History
## apertamono | 2021-09-30T10:25:52+00:00
For context, here's an example of a developer-focused Read the Docs site: [Solidity](https://docs.soliditylang.org/en/v0.8.7/#), and a user-focused Read the Docs site: [Finance Vote](https://financevote.readthedocs.io/en/latest/index.html). This particular platform is well-structured. On the other hand, the layout on the desktop is extremely vertical, on the left instead of the usual middle. It only takes up 40% of my screen, a third of which is used for the navigation pane.

I'm skeptical about this plan, because most of the documentation on this website is targeting users rather than developers. It could be useful to compile all developer documentation in one place, without removing the user guides. But that would be a big effort, and then it would have to be updated regularly for new versions. The examples I linked to were funded indirectly by token sales. There's a danger that outdated documentation would be copied blindly when there's no time to check everything. Also, keeping documentation for older versions available is not as relevant for Monero as it is for programming languages or for software that doesn't need to be updated.

In the past, the user guides had inconsistent formatting, but they look fine to me now.

## apertamono | 2021-09-30T10:26:35+00:00
Side note: Is there a reason why there's no link to Mastering Monero on the Developer Guides page?

## erciccione | 2021-09-30T12:12:35+00:00
> I'm skeptical about this plan, because most of the documentation on this website is targeting users rather than developers

The dev guides are much more extensive than the user guides and are meant to be expanded.

> Also, keeping documentation for older versions available is not as relevant for Monero

This is not the case. For example, older versions might have missing RPC calls, or same calls but slightly different responses.

> Side note: Is there a reason why there's no link to Mastering Monero on the Developer Guides page?

I don't think Mastering Monero fits in the dev guides. We list it on the "Library" section.

## elibroftw | 2021-11-22T21:10:29+00:00
@erciccione You've already contributed to https://github.com/monerodocs/md, so why not recommend it instead of yet another docs website? Instead of migrating the docs page, getmonero should just redirect to the monero docs page, but still keep the old doc pages for safe keeping.

## erciccione | 2021-11-23T09:32:14+00:00
@elibroftw that was my suggestion long time ago, but for reasons that i don't remember, we ended up not doing it. There might be a discussion somewhere in this repo. My idea was to implement monerodocs in docs.getmonero.org and then improve it and assure its maintainance. I still think would be a great option, but we need to know what people and @qertoip think about it.

## qertoip | 2021-11-23T11:30:55+00:00
Thanks for considering MoneroDocs! Here are my thoughts:

1) All MoneroDocs content is MIT which means **anyone is free to do anything with the content**. I am perfectly fine with any or all content being copied, modified, repurposed, etc. I can further put the content into public domain if that helps.

2) MoneroDocs intentionally targets technical power users and ecosystem developers. There are no beginner guides, no user guides, etc. I believe single documentation shouldn't mix the two distinct user groups. So the "user guides" should be a separate project.

3) I like MoneroDocs being **unofficial** because it takes the pressure away from me, gives me room for errors, etc. It was supposed to be my fun side-project :-)

4) I like MoneroDocs being **independent** project, domain, and hosting. I believe it's good for ecosystem decentralization. BTW, the site is literally served by my ancient ThinkPad T520 sitting by my desk.


## elibroftw | 2021-11-23T13:30:50+00:00
It's simply too much work for contributors to make pull requests for two repos!

The priorities of the get monero website are vast but the priority of monero docs is simple; to document how to use the various binaries and to look good doing it.

Not to mention that when I made a pull request for monero docs, it was reviewed the next day and subsequently merged after I responded to the review.

With the monero website, there are pull requests 12 months old! This is for a website where an incorrect update won't harm end users and can be fixed pretty fast. 

The core team needs to add more maintainers (reviewers) to the website. A simple request for applicants on Matrix, even an issue on Github, or reddit can yield even one person.

Contributors shouldn't look at the number of open pull requests and then be discouraged from making a contribution. 

## HardenedSteel | 2023-06-01T21:53:35+00:00
I think we should merge/migrate to MoneroDocs because the reasons @elibroftw said.

> 3. I like MoneroDocs being unofficial because it takes the pressure away from me, gives me room for errors, etc. It was supposed to be my fun side-project :-)
> 4. I like MoneroDocs being independent project, domain, and hosting. I believe it's good for ecosystem decentralization. BTW, the site is literally served by my ancient ThinkPad T520 sitting by my desk.

I believe it can still stay independent project except the domain while monero-site maintainers focusing and helping to MoneroDocs instead separately working. Thus would put less pressure to @qertoip.

## johnr365 | 2023-06-02T07:08:24+00:00
> I think we should merge/migrate to MoneroDocs because the reasons @elibroftw said.

Replying to @HardenedSteel - earlier in the conversation @elibroftw said:

> Instead of migrating the docs page, getmonero should just redirect to the monero docs page

One reservation I have with this is that monerodocs is only maintained by one person; @qertoip 

The last time he merged pull requests was June 16 2022; almost 1 year ago. There are [7 open PRs](https://github.com/monerodocs/md/pulls).

It is @qertoip's project to do as he wishes - but the only way I can see it making sense as a replacement for something on getmonero is if it had multiple maintainers, such that if one is busy, they don't bottleneck the whole project.

## HardenedSteel | 2023-06-02T11:36:26+00:00
> It is @qertoip's project to do as he wishes - but the only way I can see it making sense as a replacement for something on getmonero is if it had multiple maintainers, such that if one is busy, they don't bottleneck the whole project.

As I said monero-site maintainers can move to monerodocs instead separately working.

## qertoip | 2023-06-18T09:36:13+00:00
1. I merged the PR-s.
2. I am willing to add co-maintainers with with full commit rights.

# Action History
- Created by: erciccione | 2021-08-03T09:37:12+00:00
- Closed at: 2024-03-24T08:24:18+00:00
