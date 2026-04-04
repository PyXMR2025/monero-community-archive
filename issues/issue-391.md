---
title: Migrating docs to Slate
source_url: https://github.com/monero-project/monero-site/issues/391
author: lessless
assignees: []
labels: []
created_at: '2017-09-09T12:26:44+00:00'
updated_at: '2017-10-23T11:45:08+00:00'
type: issue
status: closed
closed_at: '2017-10-23T11:45:08+00:00'
---

# Original Description
Hello team,

Last month I complete migrating current docs to slate https://github.com/lessless/lessless.github.io
The feedback was good and we started to discuss with @rehrar how we can integrate it in the Monero website. 

So far I see 2 options: 

- Dissect docs project and integrated in the current website. According to  my investigation that should be possible  because both of the projects are using very similar static site generators written in Ruby. Monero Website use Jekyll and Slate uses Middleman. Thee  obvious paint points here are  differences in template language (Liquid vs ERB) (particularly loops that outputs content - https://github.com/lessless/lessless.github.io/blob/ad3c55a793332177b2c9a793d71e7d3ddbaa1444/source/layouts/layout.erb#L55, that guy got me stuck) and in how project settings are set up (footer/header inclusion, layout, assets processing, etc). Most work & time intensive way and also will break compatibility with Slate, means no bug fixes and updates. 

- Generate static content and upload them either to the current location https://getmonero.org/resources/developer-guides/ or as https://docs.getmonero.org

I'm 100% for the later option since docs looks quite different from the main website.  Also ERB (template language that Slate is using) is much less secure and allows arbitrary code execution on the static content generation stage.  Because of that it can make sense to host them on the different host or carefully review PR's :) 

If needed we can sponsor Scaleaway host for 3-5 years, they're starting from 3 eur/month, lol.





# Discussion History
## serhack | 2017-09-09T20:20:30+00:00
I'd like to have a domain like docs.monero.org with slate! Keep Your good work @lessless

## lessless | 2017-09-11T11:56:57+00:00
thanks @serhack!  I'm also working on the updating docs with calls from the recent update by @cryptobadger https://github.com/monero-project/monero-site/pull/377


## rehrar | 2017-09-20T05:09:45+00:00
Alright. Finally getting around to take a look at this. Integrating these into the website proper would be a huge change of styling. It would indeed have to be something like docs.getmonero.org or something else. 

As well, I'm not sure if the effort that would be needed to put into integrating Slate into the website itself would be worth it, but that's just me. This endeavor is appreciated, and making the documentation for everything in a more accessible format is always a plus. I'll ask pigeons and @fluffypony what their thoughts on this would be.

## lessless | 2017-09-22T05:31:19+00:00
@rehrar after https://github.com/monero-project/monero-site/pull/399 docs are much more readable (or at least I don't have a problems with them anymore).

I'm not sure if this issue still holds. 

## anonimal | 2017-09-22T05:57:50+00:00
Slate requires browser enabled javascript? Monero-site is supposed to be functional without javascript.

## lessless | 2017-09-22T07:24:06+00:00
@anonimal exactly: search and menu expanding / collapsing requires JS

## anonimal | 2017-09-22T08:13:45+00:00
>I'm not sure if this issue still holds.

Considering the amount of API documentation in monero which is already covered by Doxygen, and the amount of non-C++ documentation which is very minimal by comparison, and since monero-site is *supposed* to be functional without javascript, then yes: this issue may no longer be applicable (nice idea though if there were a pressing need (maybe there is?)).

## QuickBASIC | 2017-10-23T11:11:07+00:00
@anonimal @lessless 

It seems like the consensus is that this issue can be closed, but I wanted to check before we closed the issue.

+improvement
+guide

## lessless | 2017-10-23T11:17:21+00:00
Confirming

On Oct 23, 2017 18:11, "Mike Justman" <notifications@github.com> wrote:

> @anonimal <https://github.com/anonimal> @lessless
> <https://github.com/lessless>
>
> It seems like the consensus is that this issue can be closed, but I wanted
> to check before we closed the issue.
>
> +improvement
> +guide
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-site/issues/391#issuecomment-338625722>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ABd9zIOE_gkGz07wNkj0urq44iQDUEcZks5svHRMgaJpZM4PR-vn>
> .
>


## QuickBASIC | 2017-10-23T11:34:37+00:00
Thank you.

+resolved

# Action History
- Created by: lessless | 2017-09-09T12:26:44+00:00
- Closed at: 2017-10-23T11:45:08+00:00
