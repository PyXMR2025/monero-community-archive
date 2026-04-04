---
title: Why are you suggest to sign message/file on only-view wallet?
source_url: https://github.com/monero-project/monero/issues/9095
author: developergames2d
assignees: []
labels:
- question
- low priority
- more info needed
created_at: '2023-12-21T07:40:27+00:00'
updated_at: '2023-12-22T13:55:49+00:00'
type: issue
status: closed
closed_at: '2023-12-22T13:55:48+00:00'
---

# Original Description
Why are you suggest to sign message/file on only-view wallet?
![image](https://github.com/monero-project/monero/assets/106807841/0caa09b3-7217-45a9-a5ed-2f6468e10477)



# Discussion History
## selsta | 2023-12-21T13:29:50+00:00
Can you rephrase your question? I don't understand what you are asking.

## developergames2d | 2023-12-21T14:02:22+00:00
> Can you rephrase your question? I don't understand what you are asking.

I use ONLY-VIEW wallet. Without SEED/Private Spend Key I can't to SIGN message/file. But monero-gui suggests (~give an opportunity) this!

## developergames2d | 2023-12-22T05:51:30+00:00
> Can you rephrase your question? I don't understand what you are asking.

Did you understand?

## plowsof | 2023-12-22T12:11:27+00:00
Messages can be signed with the public view key but its not yet implemented in the GUI (for which an open issue exists)

## developergames2d | 2023-12-22T12:58:43+00:00
> Messages can be signed with the public view key but its not yet implemented in the GUI (for which an open issue exists)

No, only with private view key. But only-view wallets can't to access to private view key. And if you check your signed message, the program writes about wrong sign.

## selsta | 2023-12-22T13:55:48+00:00
See https://github.com/monero-project/monero-gui/issues/4212

# Action History
- Created by: developergames2d | 2023-12-21T07:40:27+00:00
- Closed at: 2023-12-22T13:55:48+00:00
