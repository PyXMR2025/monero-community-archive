---
title: Standardize ARM architecture naming convention
source_url: https://github.com/monero-project/monero/issues/1257
author: peronero
assignees: []
labels: []
created_at: '2016-10-24T21:17:27+00:00'
updated_at: '2016-11-22T00:44:07+00:00'
type: issue
status: closed
closed_at: '2016-11-22T00:44:07+00:00'
---

# Original Description
Successor to  #1227:

Currently, README build instructions for ARMv8 static build are 'make release-static-arm8' but there is no make rule for 'arm8' - the rule is for 'armv8'.

This is inconsistent with the other ARM build rules and corresponding references in the README ('arm6' and 'arm7'), but these are incorrectly named since ARM6, ARM7, and ARM8 are distinctly different architectures from the Cortex product line comprised of architectures named ARMv6, ARMv7 and ARMv8 for which Monero is intended.

References to ARM architectures should follow their actual naming convention as designated by ARM, in this case 'armv6', 'armv7', and 'armv8'.


# Discussion History
## ghost | 2016-10-24T21:34:36+00:00
Hi @peronero, why did you abandon your previous PR? Please make sure that you change the names in the readme, makefile and CmakeLists.txt


## peronero | 2016-10-25T01:04:02+00:00
@NanoAkron The PR was intended to be a quick fix to align the README with the code so that the text on the frontpage of the repo contains working instructions, as well as to provide a recommendation for improving the overall quality of repo.

It wasn't merged because 2 lines in the text displayed 'arm#' and 1 line displayed 'armv#', despite that being the state of code. Implementing a standardized nomenclature project-wide was outside the scope of the original PR.

Since you seem to already know what needs to be changed where, feel free to make the changes yourself. 


## ghost | 2016-10-25T07:13:26+00:00
But I don't want to because I'm not having any problems with the existing naming convention. Sorry, but meh. I won't resist someone else doing it though. 


## ghost | 2016-10-27T22:24:41+00:00
#1268 ;)


## peronero | 2016-11-22T00:44:07+00:00
Fixed.

# Action History
- Created by: peronero | 2016-10-24T21:17:27+00:00
- Closed at: 2016-11-22T00:44:07+00:00
