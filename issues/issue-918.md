---
title: 'Seraphis wallet workgroup meeting #44 - Monday, 2023-11-06, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/918
author: rbrunner7
assignees: []
labels: []
created_at: '2023-11-03T15:28:45+00:00'
updated_at: '2023-11-06T18:46:19+00:00'
type: issue
status: closed
closed_at: '2023-11-06T18:46:18+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/914

# Discussion History
## rbrunner7 | 2023-11-06T18:46:19+00:00
````
relay> <r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/918
<s​needlewoods_xmr> hallo there
<j​effro256> howdee
<j​berman> hello
<r​brunner7> So, reports from last week?
<r​brunner7> ghostway made 2 PR's here:
<r​brunner7> https://github.com/seraphis-migration/monero/pull/14
<r​brunner7> https://github.com/seraphis-migration/monero/pull/15
<v​alldrac> Hello
<g​hostway> Hello
<r​brunner7> All invited to have a look, because we are still early, and still deciding styles, how to structure things, terminology, naming etc.
<r​brunner7> Those early PRs may set "norms", if you know what I mean
<j​effro256> ghostway: what is the encrypted file to be used for mainly? The keys file ?
<r​brunner7> I think it would be suitable for that, yes. At the very least to test things like serializations
<g​hostway> It was first written for something else, but it can be used for anything technically
<j​berman> agreed with the comment that key names should be more descriptive including other places they're used. will take a deeper pass soon
<j​berman> nothing much to report on my end from last week, I presented a summary of stuff I've been working on the last months at a Cake Wallet meetup (background wallet sync, the async scanner, fcmp integration, monero-serai). Planning to complete the background wallet sync GUI implementation this week, then should have my focus mostly reserved for Seraphis (and PR review)
<j​effro256> I ask b/c I think that for the majority of the wallet cache / enote stores, we should'nt use the old pattern of 1) serializing entire thing into a string then 2) save that string to a file
<j​effro256> But for smaller files this pattern is fine
<r​brunner7> Er ... I know the history behind that: On Windows you more or less can't write directly. A very messy thing regarding filenames with non-ASCII characters
<j​effro256> Wdym you can't write directly? I'll admit, I don't know jack about systems programming on Windows
<r​brunner7> Because I solved that problem a few years ago. Took me 3 weeks of work to get to the bottom of that.
<r​brunner7> Yeah, the "C runtime" classes, the stream classes, that Monero uses on Windows, can't deal with those filenames.
<r​brunner7> Complicated story, but believe me, I tried to find a better, less memory straining solution, and failed.
<r​brunner7> We could of course just stop to support Windows, problem solved :)
<j​effro256> lol
<r​brunner7> Do those keys already all have definite and final names? jeffro256 's machinations nonwithstanding
<r​brunner7> Regarding the variable names in the key container PR
<r​brunner7> You will just add one more key, jeffro256 , right?
<r​brunner7> or does the meaning of other keys also slightly change?
<g​hostway> +1
<j​effro256> Removing unlock_amounts key, renaming find-received key -> assist-filter key, adding view-received key
<r​brunner7> Alright. But I don't think that this should hold us back. Won't be the last change I am sure. I think we can nevertheless go forward with the key container
<r​brunner7> and adjust it later, after the "dust" settled
<r​brunner7> Anything special to discuss today in this round?
<r​brunner7> I am glad we have no drama here ...
<j​effro256> I spent a lot of time wrapped up in the CCS debacle
<r​brunner7> You mean spending time by reading and stay on top of it? Or thinking about improvements?
<j​effro256> Both
<r​brunner7> I was recently learning that Seraphis will simplify multisig, no exchange of data after each and every tx sent and received. Very welcome.
<j​effro256> Oh yeah that part is super nice
<j​effro256> No partial key image syncing needed
<j​effro256> Once you're done with the ceremony, you only need to communicate to construct txs IIRC
<r​brunner7> Exactly. So if it looks like we might need multisig for safety reasons, we should hurry to implement that, so the pain with the "old" multisig won't be too long
<j​effro256> not really related to this project, but I'm working on designing a solution which would make multisig a "one click" process
<j​effro256> And shrink multisig info  exchange messages
<r​brunner7> Yeah, I heard rumors about that. Not sure what to think about that, you should go full steam ahead with Seraphis work, maybe ...
<j​effro256> well this thing would also help during Seraphis as well...
<r​brunner7> If you have time, can the two of us chat about what you plan there? I am Monero's biggest multisig fan, and I would love to learn
<j​effro256> I want to at least finish the Jamtis changes first b/c its a large dependency
<r​brunner7> Alright. Looks like we have nothing else on the agenda that is ready to discuss today. I think we can close, thanks everybody for attending!
````


# Action History
- Created by: rbrunner7 | 2023-11-03T15:28:45+00:00
- Closed at: 2023-11-06T18:46:18+00:00
