---
title: Revise send flow visuals
source_url: https://github.com/monero-project/monero-gui/issues/2148
author: GBKS
assignees: []
labels: []
created_at: '2019-05-02T08:59:32+00:00'
updated_at: '2021-04-24T20:15:27+00:00'
type: issue
status: closed
closed_at: '2021-04-24T20:15:27+00:00'
---

# Original Description
Making a transaction currently involves 5 steps. Step 1 is on the send page, and Steps 2-5 are modals, each one using a different visual style. I'd like to suggest streamlining those and making the final confirmation step a bit more useful with extra options to copy the transaction ID and a "View progress" option that takes you to the history screen to observe the confirmation progress. I find it pretty important to make users feel 100% confident that their transaction has been sent and is on the way.

There are also some minor tweaks here to standardize some of the button labels and visuals, etc.

Let me know what you think and if you have other ideas for improving this flow, I can update as needed and then push the designs to Zeplin.

![monero-transaction-flow-gbks-190429](https://user-images.githubusercontent.com/695901/57065103-a4768300-6cc8-11e9-83b4-6b32b746f7f9.png)

# Discussion History
## GBKS | 2019-05-02T10:30:15+00:00
The "Creating transaction" modal could also be merged into the approval modal, as shown in the image below. Might be a better experience if the loader is not so pronounced.

![monero-transaction-flow-tweak-gbks-190502](https://user-images.githubusercontent.com/695901/57069775-de01bb00-6cd5-11e9-887d-22271a84bedc.png)

## selsta | 2019-05-02T16:44:22+00:00
Looking awesome. +1

## ph4r05 | 2019-05-05T12:31:23+00:00
The visuals look awesome indeed!

How would "proceed to device" modal be solved? Is it going to be a splash screen or some indicator in the transaction signing window?

(We need to notify user that hardware device expects some user input in order to continue)

## rating89us | 2019-05-05T13:04:29+00:00
Regarding #2141, fiat value could also be displayed:
- Amount: 50 XMR (3,372.80 USD)
- Fee: 0.00097857 XMR (0.07 USD)

## GBKS | 2019-05-05T15:37:00+00:00
@ph4r05 good call. Is there an existing screen you could maybe send me a screenshot of? And can you think of any other interactive states that should be considered?

@rating89us that definitely should be addressed here, I'll revise.

## ph4r05 | 2019-05-05T15:51:34+00:00
@GBKS 

I had the following in mind:

<img width="1125" alt="Screenshot 2019-04-05 at 22 16 01" src="https://user-images.githubusercontent.com/1052761/57196499-ae64e400-6f5d-11e9-888a-ae88fa9bce95.png">

During the transaction creation process, the device requires user input to continue. It may prompt to confirm the destination addresses or amounts but also other processes, such as key image refresh. Without the prompt, the GUI won't progress.

Currently, it is made in such a way that if device signalizes required user input the splash screen with "Please proceed to the device" is shown and after the input is entered the device signalizes to hide the splash. Without the splash screen, user could have trouble to notice the device requires some input and wonder why GUI is not doing anything.

Similar logic is in the Wallet wizard:

<img width="1036" alt="Screenshot 2019-04-05 at 22 11 42" src="https://user-images.githubusercontent.com/1052761/57196514-ce94a300-6f5d-11e9-94be-bb56cb0d2489.png">

## GBKS | 2019-05-08T11:52:47+00:00
@ph4r05 how about this? If possible, it would be great to have more descriptive copy in this overlay as to what users should do on their hardware wallet.

![monero-finalize-transaction-gbks-190508](https://user-images.githubusercontent.com/695901/57373329-641b7700-7198-11e9-8ae0-2660d530276d.png)

## ph4r05 | 2019-05-09T16:12:40+00:00
@GBKS currently we don't have a more detailed device prompt notifications. The Trezor also prompts for other actions than transaction, such as confirmation of live refresh (key image sync) operation. Thus we decided to use more general "Please proceed to the device" phrase.

## GBKS | 2019-05-10T11:52:48+00:00
Here's an iteration that includes the fiat values and also takes a slightly different approach to the hardware wallet interaction. Let me know if this accurately reflects the user flow. The prompt to sign the transaction on the hardware wallet is less direct (= smaller text), but the modals are more consistent. Let me  know what you think.

![monero-transaction-flow-gbks-190510](https://user-images.githubusercontent.com/695901/57525290-94931a80-732a-11e9-9928-af69da552464.png)

# Action History
- Created by: GBKS | 2019-05-02T08:59:32+00:00
- Closed at: 2021-04-24T20:15:27+00:00
