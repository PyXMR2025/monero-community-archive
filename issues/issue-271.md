---
title: Mac binary problem illegal instruction 4
source_url: https://github.com/monero-project/monero/issues/271
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-04-25T03:45:24+00:00'
updated_at: '2015-04-25T07:05:07+00:00'
type: issue
status: closed
closed_at: '2015-04-25T07:05:07+00:00'
---

# Original Description
on the #monero channel. 

<Almo> hi! I get Illegal instruction: 4 when trying to run simplewallet on my OSX machine
<Gingeropolous> hrm
<Gingeropolous> is this the latest build or the stable binary?
<Almo> https://downloads.getmonero.org/mac64
<Almo> from there
<Almo> that should be the stable binary, I think
<Gingeropolous> yeah
<Almo> I'm running MAvericks on a 2013 trashcan model
<Gingeropolous> im not a mac user - i've seen some people mention there's some quirky things with macs
<Almo> StackOverflow says that Illegal Instruction 4 often means it was compiled for an OS more advanced than what you have
<Almo> which could mean it was made with Yosemite
<Gingeropolous> ah
<Gingeropolous> can you build from source?
<Almo> I have the tools, I could try


# Discussion History
## fluffypony | 2015-04-25T07:04:16+00:00
Known issue, will be fixed in the next tagged release


# Action History
- Created by: Gingeropolous | 2015-04-25T03:45:24+00:00
- Closed at: 2015-04-25T07:05:07+00:00
