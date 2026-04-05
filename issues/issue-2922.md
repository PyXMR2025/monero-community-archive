---
title: Discrepancy in the number of Accepted Shares vs number of Valid Shares
source_url: https://github.com/xmrig/xmrig/issues/2922
author: sunbearc22
assignees: []
labels: []
created_at: '2022-02-04T14:08:51+00:00'
updated_at: '2022-02-07T09:36:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
I noticed that the number of Accepted shares that is reported by XMRIg is greater than the number of Valid Shares that is reported by the XMRFAST webpage. Why is this the case? 

For example, XMRig states 
![xmrig](https://user-images.githubusercontent.com/23432142/152541462-d613fd8d-30a4-4f67-a918-538cfadfefa9.png)
But XMRFAST  webpage reported `16,513 / 0  Valid/Invalid Shares`, which is 5853 Valid Shares short. 

May I know why is there such a big difference?


XMrig-6.16.3 linux Ubuntu 20.04 version


# Discussion History
## SChernykh | 2022-02-04T15:40:26+00:00
XMRig counts accepted shares using responses from the pool:
- XMRig sends a share
- Pool responds "accepted"
- XMRig increases the counter

So I would ask pool admins first.

## sunbearc22 | 2022-02-04T15:55:34+00:00
XMRFAST just replied saying that this discrepancy is due to the 1% donation-level of XMRIG. 

I have difficulty understanding this discrepancy given that 5853÷22366*100=26.169% and this is 25% more than the default 1% donation of XMRIG.

## SChernykh | 2022-02-04T15:57:18+00:00
When XMRig is running a donation round, any found shares don't get added to the total counter, so this 1% is already accounted for.

## sunbearc22 | 2022-02-04T16:11:07+00:00
Am I correct to understand that the found shares in a donation round do not even appear on my terminal? 

Is there a way to have XMRIG output on my terminal the accepted shares from a donation round? A means for a user to verify the donation level? Is this commonly practised by XMRIG users? What is the SOP to verify donation level?

I hope you don't mind my question. I am trying to understand the significant discrepancy in Valid Shares that I am experiencing.

## SChernykh | 2022-02-04T16:13:00+00:00
They appear in the terminal, but they don't increase the counter. Maybe you have two pools in config.json and xmrig switched to the second pool for a while?

## sunbearc22 | 2022-02-04T16:17:13+00:00
I had only used the command line to mine (see command below) and not used a `config.json` file to submit the job. 

`$ sudo ./xmrig -o pool.xmrfast.com:9000 -u <mywallet> -k --tls --rig-id white -a rx/0 --huge-pages-jit --randomx-1gb-pages --randomx-mode=fast --astrobwt-avx2 --astrobwt-max-size=600`

## Spudz76 | 2022-02-04T20:22:01+00:00
Almost every pool has a lag time between reality and the dashboard.  Could the difference just be how many are in this lag zone?

Similar to when you stop mining for an hour then start up again, or add a new miner, and it takes an hour to show anything.

Then again 5853 at ~30s each would be 48+ hours, and I'm sure the lag isn't that long.  Is the result time ~30s (2 results per minute average)?

## sunbearc22 | 2022-02-05T18:05:13+00:00
I have about 3 to 4 accepted shares per minute.  
![numberofacceptedsharesperminute](https://user-images.githubusercontent.com/23432142/152653093-2918c3a5-02ab-432d-9015-54bec8e2fcb6.png) 
@Spudz76  Can this info help you figure out the cause of the discrepancy?

Does this mean the lag zone is a loop-hole for miners to lose share w/o a trace?

To minimise this discrepancy, I had tried to record the shares at the 5 minutes mark used by the dashboard.


## Spudz76 | 2022-02-05T18:53:34+00:00
No, you don't lose anything, it just doesn't show what happened in real-time since it has to collate and average the data so the latest data may not show up "now" but after it's been processed.  And the frontend (dashboard) is not attached directly to the backend mining or else the less important web site never can break the backend where mining happens.

But this is all a guess because I don't run the pool, ask them if there is lag time between reality and the dashboard.

## sunbearc22 | 2022-02-06T07:28:19+00:00
@Spudz76 I can understand the concept of having a lag between the dashboard vs the backend mining. But does a shortfall/discrepancy of 26% not seem quite large or abnormal? I am new to mining. I wonder if everyone else is also experiencing such a large discrepancy between the Valid Shares reported on their dashboard vs the backend mining program reported Accepted Share?

I investigated the effects of setting the donation level to 0. I had recompiled the XMRig source code and set the `--donate-level` to 0 to allow this study. Below is my result:
![image](https://user-images.githubusercontent.com/23432142/152671393-f5099165-71f1-4fb8-9133-747abc9aed40.png)
Findings:

1. W/o donation, the Valid Shares reported on XMRFAST dashboard is still always lesser than the backend XMRIG reported Accepted Shares. This observation reaffirms that the `donation-level` is not a contributing factor to the observed discrepancy. 
2. The level of discrepancy did not grow with time but appears to be in the 21% to 30% range.

In my earlier correspondence with XMRFAST, its admin said the discrepancy is my donation to XMRig.
![image](https://user-images.githubusercontent.com/23432142/152671917-80ceea3a-9e34-403b-b513-f5c1a887d9a7.png)







## Spudz76 | 2022-02-06T22:21:34+00:00
Yeah it was just a theory, I didn't think it really lined up.

I am out of ideas other than xmrfast sucks.

## toy1111 | 2022-02-07T01:52:28+00:00
Hi - Just because I was interested and I'd not seen a pool where your shares/hashes are actually provided. Often its just a hashrate graph or similar. I pointed one of my miners to xmrfast for a few hours and see the same discrepancy with what are the accepted shares and total hashes vs what is reported for both at xmrfast. Not sure what it means but they should provide a better explanation.

## Spudz76 | 2022-02-07T02:35:26+00:00
Thanks for the second data point.  I just try to hesitate with blaming pools since that's the easiest answer, someone is stealing, but jumping to that immediately is probably wrong too.  And I don't know much about xmrfast.

I do rip on Nanopool constantly but only because they refuse to support sane difficulties or autodiff or custom diff.

## sunbearc22 | 2022-02-07T06:05:16+00:00
@toynn Thanks for letting me know that you also experienced the same issue as me on XMRFAST.

## sunbearc22 | 2022-02-07T06:28:33+00:00
@Spudz76  I have written to XMRFAST, updating them that XMRIG Accepted Shares do not include donated Accepted Shares, my findings and I am awaiting a reply. 

I notice that you regard the cause of this discrepancy as stealing.  May I know what is the SOP to validate proper accounting of Valid Shares and Payments from a pool using the PPLNS reward system?

Does XMRIG have an option to log all the mining outputs that appear in the terminal to a file? I think this feature is useful for accounting purposes and dispute handling.

## SChernykh | 2022-02-07T08:32:56+00:00
> Does XMRIG have an option to log all the mining outputs that appear in the terminal to a file?

`"log-file":"xmrig.log",` in config.json right before `pools` section.

## sunbearc22 | 2022-02-07T09:36:51+00:00
@SChernykh Thanks 

I modified my terminal command to:
 
`$ sudo ./xmrig -o pool.xmrfast.com:9000 -u <mywallet> -k --tls --rig-id white -a rx/0 --huge-pages-jit --randomx-1gb-pages --randomx-mode=fast --log-file=xmrig_$(date +"%F_%H-%M-%S").log`

In this way, the logfile will be named with date and time, e.g. `xmrig_2022-02-07_10-40-31.log`

# Action History
- Created by: sunbearc22 | 2022-02-04T14:08:51+00:00
