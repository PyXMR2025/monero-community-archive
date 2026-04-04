---
title: Consider switching from Jekyll to Hugo
source_url: https://github.com/monero-project/monero-site/issues/2140
author: erciccione
assignees: []
labels:
- 💬 discussion
created_at: '2023-03-14T10:46:28+00:00'
updated_at: '2024-09-26T19:58:21+00:00'
type: issue
status: closed
closed_at: '2024-09-26T19:58:21+00:00'
---

# Original Description
Recently i updated the dependencies of getmonero (#2116) and as noted in the PR, there is a problem that we have to deal with: [jekyll-multiple-languages-plugin](https://github.com/kurtsson/jekyll-multiple-languages-plugin) which we are using to make the website multilingual has been in maintainance mode for years. It was always a bit of a problem, but now things are getting worse, as incompatibilities are starting to pop up which force us to lock some specific versions in the dependencies.

This is a problem that will only get worse and that could only be solved by somebody taking over the plugin and maintain it again. This hasn't happened yet and i feel it won't ever happen. The result could be that we will find ourselves unable to update to newer Jekyll versions or we could find ourselves stuck in a dependency hell.

I see only two solutions:

1. We keep things as they are and we hope that the plugin will be kept in an usable state in the future
2. We move away from Jekyll entirely

The second point would require a massive amount of work, but will also allow us to have some stability, increased performances and better and much less painful multilingual support from that moment on. In case we decide to go for two, here are some things to keep in consideration (assuming [Hugo](https://gohugo.io/) as the substitute):

**PROS**

- Hugo is exponentially faster than jekyll. A website builds in milliseconds, even with multiple languages. Building with jekyll takes minutes and requires local tweaks to make local testing not painful.
- Much better internationalization. The way our user guides and moneropedia were made multilingual is suboptimal and requires a huge amount of work to maintain, where multiple files need to be edited. We automated this as much as possible by using tools like weblate and po4a, but it's still a very clunky system that could be much easier. Hugo will make internationalization of the whole website as easy as it currently is with a normal getmonero page (YAML key-value pairs)
- internationalization is built-in in Hugo and doesn't require reliance on an external plugin (which is what is generating our issue)
- We can take advantage of this big structural change, to implement some major UX improvements, like a better menu structure.

**CONS**

- Hugo is much newer and less tested than jekyll, even if the community is getting bigger
- Hugo hasn't release version 1 yet, even if it's generally considered stable
- The conversion to jekyll would require a massive amount of work. The biggest parts being the conversion of the localised pages to fit Hugo's structure and replacing jekyll's own scripting language (Liquid), which we use extensively. The entire conversion will require 2/3 people dedicated to the effort.
- Hugo is based on Go, Jekyll is based on Ruby. Not really a negative, but worth noting, because it would be a different environment.

So, what is people's opinion about this? I've been trying Hugo lately and was positively surprised. Beside that, switching from the Jekyll plugin is something that needs to be done sooner or later. We could look for another plugin and adapt our structure to that, but beside the pros and cons listed above, there is no assurance that we won't find ourselves in this situation again. Also, last time i checked (long ago) converting to another plugin would require a big amount of work anyway, so at that point...

Personally i think would be wise to switch, but this is a huge change that needs to be carefully considered. Would be great to gather as much feedback as possible.

# Discussion History
## plowsof | 2023-03-23T14:44:30+00:00
Having had some light experience with translations on -site - if what you say is true with regards to Hugos advantages in this area then i consider the switch vital to the future of the Monero project. (e,g, If existing guides can be edited easier)

There was also a push to move to a https://monerodocs.org/ style of guides (and others which i can't remember right now).

My domain expertise in this area is lacking but i'm available to provide effort where possible. Thank you for raising this issue. 

## MajesticBank | 2023-04-07T13:30:20+00:00
I have no previous experience with Jekyll or Hugo.

However Hugo does seem too new for site of scale as getmonero.org at this point.

https://github.com/kurtsson/jekyll-multiple-languages-plugin - Plugin we are currently using seems to be out of a date for year

But I see there is successor of that plugin - https://github.com/untra/polyglot on github says "Jekyll doesn't provide native support for multi-language blogs. This plugin was modeled after the jekyll-multiple-languages-plugin, whose implementation I liked, but execution I didn't." 

It seems that above plugin is up to date and well maintained, I am not sure how much cross compatible and easy to apply in our scenario.

I would make sure we exhaust all options on current setup before switching to someone new because there might not be guarantee that will be alive in next year or two.

Maybe better to invite some of these people to open CCS funding to keep language plugin up to date if only language plugin is causing issues.


## erciccione | 2023-04-11T07:36:11+00:00
> because there might not be guarantee that will be alive in next year or two

I see this as much more probable with the fork of the jekyll plugin than with Hugo, a project with a team behind that has already been around for years, while the fork is a personal project that is currently not listed as raccomended from Jekyll. I wouldn't switch to the polyglot plugin.

## plowsof | 2024-07-09T10:02:14+00:00
After noting some upcoming EOL ruby versions / issues with updating site in this comment here:
https://github.com/monero-project/monero-site/pull/2237#issuecomment-2216812332 

>Starting in Ruby 3.2.0 the exists? (pluralized) alias for exist? seems to has been removed.

`jekyll-multiple-languages-plugin` contains one instance of exists? https://github.com/kurtsson/jekyll-multiple-languages-plugin

## plowsof | 2024-07-09T16:16:38+00:00
we also can not use version 1.8.0 (stuck at 1.7.0) of jekyll-multiple-languages-plugin due to this error:

https://github.com/kurtsson/jekyll-multiple-languages-plugin/issues/201

## plowsof | 2024-07-09T21:35:11+00:00
Another option is possibly moving to polygot like this project has done:

https://github.com/george-gca/multi-language-al-folio/pull/18 

## rehrar | 2024-09-26T17:22:37+00:00
There have been several meetings in the Monero Website channels (IRC #monero-site, and the bridged Matrix room). In one of the meetings, and several discussion thereafter, the pros and cons of a new backend were discussed. I summarize them below:

Pros:
1. The current stack is fragile, with comments from people who work on it such as "held together by duct tape" and "glued together cluster fuk".
2. Building off of the above, Jekyll (in which the current site is coded) is ageing and not receiving many updates. It is written in Ruby, a language that is also declining from its heyday. This means fewer contributors in the case of custom code needed.
3. Doing anything seemingly simple for a modern Static Site Generator (such as adding dark mode) requires custom plugins and work. Most modern SSGs have built-in functionality for things like this.
4. None of the current maintainers enjoy working with Jekyll very much, or at the least are neutral to a backend change.

Cons:
1. Current site works. May not be pretty (design and/or backend), but it works.
2. We don't really plan to add a ton of features anyways, besides maybe dark mode, so all of this newfangled stuff may not be necessary.
3. Money and time will be needed to make the change. These resources could potentially be used better elsewhere?

This said, the framework that was decided upon in these meetings was Astro rather than Hugo, but that can be a different discussion. I am merely summarizing the arguments for and against a new backend at all.

## HardenedSteel | 2024-09-26T18:08:28+00:00
All the cons are pointing to same thing. It seems we eventually have to change the backend which means our choices are postpone or fix now.

## plowsof | 2024-09-26T19:58:21+00:00
please continue in #2374 where everyone can participate, thank you. 

# Action History
- Created by: erciccione | 2023-03-14T10:46:28+00:00
- Closed at: 2024-09-26T19:58:21+00:00
