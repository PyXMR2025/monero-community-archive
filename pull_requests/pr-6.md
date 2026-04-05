---
title: 'common: add Jamtis base32 encoding'
source_url: https://github.com/seraphis-migration/monero/pull/6
author: jeffro256
assignees: []
labels: []
created_at: '2023-09-10T23:01:47+00:00'
updated_at: '2023-09-26T19:59:07+00:00'
type: pull_request
status: merged
closed_at: '2023-09-26T19:51:31+00:00'
merged_at: '2023-09-26T19:51:31+00:00'
---

# Original Description
see encoding scheme spec here: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#35-base32-encoding

This PR is an alternative to https://github.com/seraphis-migration/monero/pull/2. The motivation for this alternative was less code for reviewers (only about 60 real lines of code) and additional built-in functionality of the existing library `cppcodec`. The unit tests here include a sanity check for allowing for Jamtis address prefixes "xmra{1..9}{t,s,m}..." and a test to make sure that the added dependency doesn't change underneath our feet: `base32.future_modification_protection`.  

# Discussion History
## vtnerd | 2023-09-10T23:20:52+00:00
This feels like cheating compared to the other implementation - the PR is just offloading tons of code/work to `cppcodec`. I guess we implicitly trust that implementation?

## jeffro256 | 2023-09-11T04:55:26+00:00
FWIW, the repo has >500 stars and >100 forks. You can call it "cheating", but it's using a well-established library for its intended purpose instead of reinventing the wheel.

## jeffro256 | 2023-09-11T04:57:30+00:00
Having the library change underneath us is also planned to be caught in the "future_modifications_protection" test suite. That's assuming we decide to resync against the upstream repo, which can't happen by accident since git modules links by commit id.

## rbrunner7 | 2023-09-17T10:49:52+00:00
I guess this method is a leftover that you can finally delete?

## rbrunner7 | 2023-09-17T10:55:43+00:00
Not sure why you call this *similar* - you test for equality, right?

## rbrunner7 | 2023-09-17T11:02:05+00:00
I propose to replace *TEVADOR* by *JAMTIS* in the naming here, to be in line with all other places where the name of the spec and not the name of the spec designer is used.

## rbrunner7 | 2023-09-17T11:05:26+00:00
Copied over from my review of @DangerousFreedom1984 's code, in the spirit of making generous use of comments like the Seraphis library does:

I see here a very good opportunity to explain why we use a different alphabet than almost anybody else for "our" Base32 variant, and mention which characters are missing or different.

## rbrunner7 | 2023-09-17T11:09:21+00:00
Typo: "sring", without "t"

## rbrunner7 | 2023-09-17T11:19:06+00:00
Little nitpick, but shouldn't this be `bit_offset`?

## rbrunner7 | 2023-09-17T11:21:25+00:00
Just curious - where and when do we have to deal with eventual hyphens?

## rbrunner7 | 2023-09-17T11:34:23+00:00
A short comment explaining what this asserts?

I had to look up the Jamtis spec to (hopefully correctly) understand that the address prefix is base32.

## rbrunner7 | 2023-09-17T11:36:07+00:00
I don't quite get what you test here, why it's relevant and what's the connection with Jamtis address headers. Can you please elaborate a bit? (Probably my problem regarding understanding, not any problem with the test itself).

## jeffro256 | 2023-09-18T03:34:04+00:00
Yes, I just called it similar since the whole string doesn't have to be equal

## jeffro256 | 2023-09-18T03:45:35+00:00
A lot of other base32 standards use hyphens as spacing, and it might come in handy to space out Jamtis addresses, especially seeing as they will be so long.

## jeffro256 | 2023-09-18T03:46:12+00:00
That the Jamtis address header characters can be decoded (given a correct length). 

## jeffro256 | 2023-09-18T03:48:39+00:00
It wasn't a hard requirement, but making sure that changes on the right side of the binary only affect the right side of the encoded string makes Jamtis address encoding harder to mess up because you can encode the header + body together and know that you'll get the correct prefix. 

## vtnerd | 2023-09-19T19:19:57+00:00
A couple of nitpicks: (1) we typically started to use `epee::span<const char>` as it cleans the interface up slightly, and (2) I would have the binary buff be `const std::uint8_t` to differentiate. So the signature would be : 

```c++
ssize_t encode(epee::span<const std::uint8_t> in, epee::span<char> out, const Mode mode);
```

And the same comment for the other function signatures.

## vtnerd | 2023-09-19T19:28:45+00:00
Do these tables really need to be exported? Can they be local to the cpp?

## vtnerd | 2023-09-19T19:29:01+00:00
Same with these constants, why export them?

## vtnerd | 2023-09-19T19:31:35+00:00
Perhaps a check to ensure we don't overflow `ssize_t` on the conversion? I realize that's practical impossible, but it would make this more portable.

## vtnerd | 2023-09-19T19:36:39+00:00
This should be a `runtime_error` too - the caller isn't necessarily expected to check for invalid characters before conversion (or at least that's my understanding).

## vtnerd | 2023-09-19T19:37:12+00:00
This would be a `logic_error`, this isn't expected to happen at all, ever.

## vtnerd | 2023-09-19T19:39:38+00:00
This should be a hard-check, and not an `assert`. Realistically it's impossible on most platforms, because it would require a massive buffer, but the check makes it portable if `size_t` et al are 32-bit.

Also, the assert could be in the above function, because its coerced there.

## vtnerd | 2023-09-19T19:41:19+00:00
Same thing about the coercing to `ssize_t` in the two decode functions.

## vtnerd | 2023-09-19T19:52:21+00:00
When is lossy useful? And how to select not lossy?

## vtnerd | 2023-09-19T21:44:45+00:00
I don't understand why the `<< 3` here. This should shift the first value by 3 (left), and I don't see how that could be accurate.

## jeffro256 | 2023-09-20T17:02:01+00:00
They are exported so they can be used by the base32 checksum PR #7 as default tables.

## jeffro256 | 2023-09-20T17:02:07+00:00
They are exported so they can be used by the base32 checksum PR #7 as default tables.

## jeffro256 | 2023-09-20T17:04:57+00:00
`Mode::binary_lossy` in useful for encoding exact blocks of 5 bits so that the encoded base32 string isn't as long. For example, Jamtis address body sizes will be an odd number of bits long, not divisible by 8. Thus, we can make the encoded string one byte shorter since there's leftover bits in the binary that we aren't using. 

## jeffro256 | 2023-09-20T17:05:24+00:00
You select `binary_lossy` by passing it as the `mode` parameter in each function. 

## jeffro256 | 2023-09-20T17:07:36+00:00
Since MSBs are encoded "before" LSBs, we shift the 5-bit alphabet index up 3 to align it with the first bit in the byte, the MSB, *then* we shift it according to the `bit_offset`.

## jeffro256 | 2023-09-20T17:10:09+00:00
This is a design choice where we could've encoded the LSBs before the MSBs, and not needed the `<< 3` but I like MSB->LSB type of encoding because it makes more sense for humans when you convert the raw data into a binary string.

## jeffro256 | 2023-09-20T17:10:39+00:00
That's also what most base32 libraries do anyways.

## vtnerd | 2023-09-20T17:11:52+00:00
I thought it was expected when divisible by 5-bits that no additional values would be appended. I guess not. But then how does someone select _lossless_ mode? There is no `enum` for it.

## jeffro256 | 2023-09-20T17:13:58+00:00
Although it isn't explicit, almost all base32 libraries take the "encoded lossy" approach which preserves every bit in the raw data and discards extraneous encoded string bits, since that's the expected behavior 90% of the time. That's the default behavior for this code too, but now you have the option. 

## jeffro256 | 2023-09-20T17:16:49+00:00
> But then how does someone select lossless mode? 

You could make a lossless mode if and only if you forced the user to only encode raw data for which the byte length is divisible by 5, and decode encoded strings of which the length is divisible by 8. 

## jeffro256 | 2023-09-20T17:17:15+00:00
It could be added, although I don't know when that would be useful. 

## vtnerd | 2023-09-20T17:37:21+00:00
Yup, looked at the encoding algorithm to see what you did. I suppose it doesn't matter, as long as its consistent behavior.

## jeffro256 | 2023-09-20T21:54:47+00:00
done

## jeffro256 | 2023-09-20T21:54:54+00:00
done

## jeffro256 | 2023-09-20T21:55:12+00:00
done

## jeffro256 | 2023-09-20T21:55:25+00:00
done

## jeffro256 | 2023-09-20T21:55:39+00:00
done

## jeffro256 | 2023-09-20T21:55:53+00:00
done

# Action History
- Created by: jeffro256 | 2023-09-10T23:01:47+00:00
- Merged at: 2023-09-26T19:51:31+00:00
