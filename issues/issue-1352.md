---
title: Moneropedia links (created by _plugins/moneropedia.rb) are always lower case
source_url: https://github.com/monero-project/monero-site/issues/1352
author: erciccione
assignees: []
labels:
- enhancement
created_at: '2020-12-04T10:04:15+00:00'
updated_at: '2021-02-26T19:01:54+00:00'
type: issue
status: closed
closed_at: '2021-02-26T19:01:54+00:00'
---

# Original Description
No description

# Discussion History
## ghost | 2021-02-22T14:40:37+00:00
What's the expected behavior? Should they all be capitalized? From what I can tell, the Moneropedia plugin just preserves the capitalization of the terms provided in each Moneropedia entry, and the majority of them are lowercase. Several of them (Locally-unique host, Canonically-unique host, and Kovri) are capitalized and are displayed as such.

## erciccione | 2021-02-23T08:48:29+00:00
> Should they all be capitalized?

They should be capital when at the beginning of a sentence or after a dot, lowercase if the word is in the middle of a sentence.

## ghost | 2021-02-23T18:25:32+00:00
What do you think about replacing the hyperlink text with the regex match instead of whatever term is stored in the entry? That way, the Moneropedia links simply reflect the way that they were written, and it wouldn't require any code to check for punctuation.
```
content = content.gsub(/(\@#{term})((?=-#{lookahead})|(?![\w-]))/i) { |match_term| '<a class="info-tooltip" data-tooltip="' + entry[:summary] + '" href="/resources/moneropedia/' + entry[:file] + '.html" >' + match_term.gsub(/[@-]/, '@' => '', '-' => ' ') + '</a>' }
```

For example, `@ring-ct` would display as `ring ct` and `@Ring-CT` as `Ring CT`. Any existing capitalization errors would need to be fixed manually, but that shouldn't be too difficult.


## erciccione | 2021-02-24T09:05:19+00:00
Good idea. I was slightly worried about how the other languages would have reacted (especially the ones not using latin characters), but i tested your patch quite extensively and there seem to be no problems.

Would you PR your patch? As you said, capitalization errors are not a big deal and we can fix them when we find them.

# Action History
- Created by: erciccione | 2020-12-04T10:04:15+00:00
- Closed at: 2021-02-26T19:01:54+00:00
