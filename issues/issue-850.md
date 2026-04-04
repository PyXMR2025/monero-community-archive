---
title: 'Seraphis wallet workgroup meeting #27 - Monday, 2023-06-19, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/850
author: rbrunner7
assignees: []
labels: []
created_at: '2023-06-16T19:08:44+00:00'
updated_at: '2023-06-19T18:34:16+00:00'
type: issue
status: closed
closed_at: '2023-06-19T18:34:16+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #847

# Discussion History
## rbrunner7 | 2023-06-19T18:34:16+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/850
<dangerousfreedom> Hello
<rbrunner7[m]> Everybody already at the beach for summer holiday :)
<rbrunner7[m]> In any case, nothing to report from me since the last meeting. About you, dangerousfreedom[m] ?
<jberman[m]> hello
<dangerousfreedom> Looks like mostly are living on the north hemisphere :p
<dangerousfreedom> rbrunner7[m]: This week I implemented the generation function of some knowledge proofs and I'm almost done with the generation of the spend_proof for legacy. Though I'm pretty sure I will have to modify it when we fix the format of the key_container. But mostly this week I focused on the MKon presentation.
<dangerousfreedom> I will update my changes to that PR draft next week
<rbrunner7[m]> +1
<rbrunner7[m]> Is the key container waiting for ghostway publishing what they have so far?
<jberman[m]> I spent a bit of time this past week working with kayabanerve on full chain membership proofs which was exciting. Nothing specific to share on it yet and would like to hold off on discussing it at this time, they'll be presenting on it at Monerokon. I'll be working on my presentation on the light wallet tier this week and will be back to working on wallet work hopefully within the next 2 weeks
<rbrunner7[m]> Ah, a cliffhanger.
<jberman[m]> sorry :)
<rbrunner7[m]> It's ok, makes Monerokon all the more exciting I hope.
<rbrunner7[m]> Maybe a bit silly, but still: Today I learned from jeffro256 that in 1.8 years the total number of emitted piconeros will go over the range of uint64. Is that a problem if we have to support that with the "old" codebase still in case Seraphis won't be ready for hardfork in those 1.8 years?
<rbrunner7[m]> Maybe there are not too many places in the code where this total plays any role?
<dangerousfreedom> I believe it would only be a problem if you make a transaction with more than 2**64 piconeros
<dangerousfreedom> So I dont see how practical it would be
<dangerousfreedom> Definetly not in the next 100 years
<dangerousfreedom> Unless someone really accumulates all the chain for himself
<dangerousfreedom> Because rangeproofs are bound by 64 bits
<dangerousfreedom> I think
<dangerousfreedom> I asked myself this question too some months ago :p
<dangerousfreedom> Another answer?
<jberman[m]> Also looks like get_coinbase_tx_sum already supports 128 bit integers when tallying supply, so that should be fine
<dangerousfreedom> But the bottleneck is still the rangeproofs with 64 bits
<rbrunner7[m]> Ok, good to know.
<rbrunner7[m]> Yeah, but as you said, nobody will gobble up all XMR anytime soon :)
<rbrunner7[m]> Regarding next Monday: Probably I will be back from Monerokon early enough to be at my computer at the hour of the meeting. I can chat a bit with whomever will be around.
<dangerousfreedom> Ok. I will probably not make it for next meeting.
<ghostway[m]> some good news and some bad news: I finished it yesterday, and now I am greeted to whatever this is[?1049h[22;0;0t[22;0t[?1h=[H[2J]11;? [?2004h[?u[c[?25h[?25l[m[H[2J[?1004h[?25h[?25l[38;2;243;141;112m[48;2;44;37;37m1   [m[38;2;255;241;243m[48;2;64;56;56m... (full message at <https://libera.ems.host/_matrix/media/v3/download/libera.chat/a2607b28c819c5776a8fd0774ac6ac1a159070a3>)
<ghostway[m]> so, seems like I have some work to do. again.
<dangerousfreedom> I see that you use neovim, nice. But what was that? :p
<rbrunner7[m]> Anybody else got a lot of gibberish on their screen together with ghostway 's message?
<rbrunner7[m]> Can you please post again, ghostway , I am deleting your last message
<ghostway[m]> no no, that's the thing, it is gibbrish. it just deleted my file
<rbrunner7[m]> Ah, you mean, you accidentally lost your work so far?
<ghostway[m]> only the cpp file, but yes..
<valldrac[m]> ghostway: That was the welcome message of VIM, with all control characters to put colored output on the console... just you to know 
<rbrunner7[m]> My, that's bad. Condolences.
<valldrac[m]> Might you run `vim > your-code.cpp` or something similar
<ghostway[m]> I don't even know how that could happen though, I don't do vim > stuff
<ghostway[m]> heh
<ghostway[m]> ohh, shit. I just remember, does bash interpret nvim >file the same as nvim > file?
<dangerousfreedom> do you have the .swp file?
<ghostway[m]> I don't think so, swaps are deleted when the session is finished
<dangerousfreedom> Oh if you use sessions there may be a way to recover
<ghostway[m]> I don't, that's how nvim works
<rbrunner7[m]> Alright. Maybe somebody has another idea how to salvage. Anything still for this meeting?
<rbrunner7[m]> If not, thanks for attending, and maybe see some of you at Monerokon.
<dangerousfreedom> Thank you :)
<ghostway[m]> thanks. let's hope next time I just commit my stuff and not leave it be
````


# Action History
- Created by: rbrunner7 | 2023-06-16T19:08:44+00:00
- Closed at: 2023-06-19T18:34:16+00:00
