---
title: Why are there 4 numbers in the versioning scheme?
source_url: https://github.com/monero-project/monero/issues/9133
author: comminutus
assignees: []
labels:
- question
- low priority
created_at: '2024-01-23T13:33:24+00:00'
updated_at: '2024-11-21T22:51:28+00:00'
type: issue
status: closed
closed_at: '2024-01-24T23:49:09+00:00'
---

# Original Description
It seems the first number is always `0`, which suggests that Monero is in some kind of pre-release state.  I doubt this is the case.  Shouldn't the leading `0` be dropped?  If not, does that mean the second and third numbers are minor and patch numbers, and the fourth a build number? 

Perhaps the idea was to follow some kind of similarity with the [Bitcoin version history](https://bitcoin.org/en/version-history)? 🤔

# Discussion History
## Swapnilchavan13 | 2024-01-24T07:49:25+00:00
Monero's versioning system follows the format MAJOR.MINOR.PATCH, with a leading zero in the major version. The leading zero doesn't imply a pre-release state but is a part of Monero's versioning convention. It is not directly influenced by Bitcoin's versioning scheme. To understand the current versioning details, it's best to check the official Monero documentation or the project's GitHub repository. Versioning conventions may evolve over time in software projects.

## comminutus | 2024-01-24T10:47:14+00:00
> Monero's versioning system follows the format MAJOR.MINOR.PATCH, with a leading zero in the major version. The leading zero doesn't imply a pre-release state but is a part of Monero's versioning convention.

This is evident, the question is why is there a leading "0?"

> To understand the current versioning details, it's best to check the official Monero documentation or the project's GitHub repository. Versioning conventions may evolve over time in software projects.

I did this, hence the reason for the post here. This looks like a ChatGPT response?


## comminutus | 2024-01-24T20:34:32+00:00
Forgive me if I thought @Swapnilchavan13's response was a generated answer, it seemed like it since the very reason I posted the question was because this information can't be found in the documentation nor the source, otherwise someone would've linked to it by now.

@Fjodor42 I think you're projecting my "tone" and making a lot of assumptions.  I'm not trying to be hostile.  I'm genuinely just curious why there are 4 numbers which make up the version, which are not compatible with SemVer.  Because SemVer is fairly standard these days, most understand an X.Y.Z versioning format to mean major, minor, and release.  Usually, a versioning scheme with 4 numbers adds a "build" component to the set.

Presumably, each component of the version has a meaning, I'm simply after the meaning of each component.  What is the meaning of each component in the Monero versioning scheme?  If the first component (the "0") is arbitrary, why is it so?


## iamamyth | 2024-01-24T22:42:13+00:00
@comminutus See https://github.com/monero-project/meta/issues/721.

## comminutus | 2024-01-24T23:49:09+00:00
@iamamyth that is helpful; I didn't see that (I wasn't looking in the meta repo) - thanks!

Based on that discussion, it seems like the leading 0 in the versioning was to convey the idea that major changes still may come.  While this is understandable, it looks as if the idea was conflated with the ideas of SemVer, making the 2nd component major, 3rd minor, and 4th revision.  This defeats the purpose of the "major" version number change, since major versions typically indicate incompatibility between versions and drastic changes.

Nonetheless, I'll close this because the topic linked by @iamamyth is probably a more relevant place to continue the discussion.

# Action History
- Created by: comminutus | 2024-01-23T13:33:24+00:00
- Closed at: 2024-01-24T23:49:09+00:00
