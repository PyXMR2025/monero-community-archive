---
title: use our own custom Jekyll-Multiple-Languages-Plugin
source_url: https://github.com/monero-project/monero-site/issues/2317
author: plowsof
assignees: []
labels:
- 🧰 back end
created_at: '2024-07-09T17:13:27+00:00'
updated_at: '2024-07-18T07:29:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
prefacing this by saying i don't know what ruby or gems are.

please read 2140 for more context: 
- #2140 

we are currently forced to use ruby < 3.2.0 which is not good for long term as [Ruby EOL's versions frequently](https://endoflife.date/ruby)
>Starting in Ruby 3.2.0 the exists? (pluralized) alias for exist? seems to has been removed.

- Jekyll multiple language (JML) plugin has an "`exists?`" which can be simply fixed, just like in this [upstream PR](https://github.com/kurtsson/jekyll-multiple-languages-plugin/pull/210/files) but its not maintained anymore.

- we also have an "`exists?`" to be replaced with "`exist?`" here https://github.com/monero-project/monero-site/blob/99fd539bea6b819ce1a3a02722d3062cf6f18fc6/_plugins/sitemap_generator.rb#L129 

- we're using JML version 1.7.0 but there is a 1.8.0 version that has an error reg parsing a nul string, which is either another dependency issue (paginate) or fixable if we can modify JML ourselves:  [no implicit conversion of nil into String since 1.8.0](https://github.com/kurtsson/jekyll-multiple-languages-plugin/issues/201)

Now to my request. So before i can even attempt to fix the lowest hanging fruit "exists?" -> "exist?" issue, i need to use/import a custom version of JML.

Jekyll multiple languages plugin describes how to import/use the plugin manually (or as a submodule):
https://github.com/kurtsson/jekyll-multiple-languages-plugin?tab=readme-ov-file#32-manually 

I couldn't get it to work.. infinite recursion.. dependency still attempted to be grabbed from an external resource instead of locally. I am hoping its just my lack of ruby/gem/plugin knowledge and someone can help/advise. 

# Discussion History
## plowsof | 2024-07-09T18:45:07+00:00
i seem to have got it working, just the .rb file in _plugins will auto load. combined with cleaning any mention of JML plugin from config files https://jekyllrb.com/docs/plugins/installation/ 

## plowsof | 2024-07-09T20:57:55+00:00
ruby 3.2.4 now builds with a custom JML script. the "nil into string" error was fixed by adding some extra parsing logic. this was a speedrun just to make myself feel confident about getmonero having a none EOL ruby version in ~8 months. I need to put the changes into an acceptable/re-viewable PR. 

https://github.com/plowsof/monero-site/pull/29

# Action History
- Created by: plowsof | 2024-07-09T17:13:27+00:00
