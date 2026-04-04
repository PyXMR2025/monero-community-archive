---
title: '[UX] Move seed into a separate screen of the onboarding flow'
source_url: https://github.com/monero-project/monero-gui/issues/2043
author: GBKS
assignees: []
labels: []
created_at: '2019-03-29T10:06:57+00:00'
updated_at: '2024-03-27T15:04:25+00:00'
type: issue
status: closed
closed_at: '2023-02-21T01:13:48+00:00'
---

# Original Description
During [user testing](https://paper.dropbox.com/doc/Monero-GUI-user-testing--AaPItIR28uMAAkEXUdQZnYARAg-YAWmy01OJa5vkmdQvt6wg), testers seemed to miss the seed section or not understand it. It just seems to get a bit lost because it is below the wallet name and location, and because the term "Mnemonic seed" isn't clear. Writing down the seed and storing it securely is probably the most important thing a user needs to do during wallet creation, so I suggest moving it into a separate screen.

Here's a suggestion for what this screen could look like, all feedback is welcome. The title is very direct about what users should be doing, and there's a checkbox to confirm that they wrote it down.

![monero-seed-gbks-190329](https://user-images.githubusercontent.com/695901/55224924-c4baaa00-5211-11e9-8757-9ab277e67c31.png)

And here's the print template referenced in the screen. Without this, users may just use a post-it or a scrap of paper they happen to have on their desks (or just copy/paste the seed into a file). A proper template should hopefully make it easier for users to "do the right thing".

[Monero recovery phrase template.pdf](https://github.com/monero-project/monero-gui/files/3022055/Monero.recovery.phrase.template.pdf)

# Discussion History
## rating89us | 2019-03-29T11:19:37+00:00
There should be some warnings also. Use pen and paper. Don't copy and paste. Don't save in a text file. This is a backup: if you lose these words and your wallet has a problem, you will lose all your XMR.

## GBKS | 2019-03-29T16:15:49+00:00
If we're worried about users copy/pasting, we can choose a different format in which the seed is not in a text field, but instead shown in a list. The attached template matches the same 3-column layout, so should be pretty easy to write things down. Let me know what you think...

![monero-seed-gbks-2-190329](https://user-images.githubusercontent.com/695901/55245754-0fedb080-5244-11e9-8cea-96c5838877a6.png)

[Monero recovery phrase template 2.pdf](https://github.com/monero-project/monero-gui/files/3023446/Monero.recovery.phrase.template.2.pdf)

How about a different approach instead of a warning? We could have a multiple choice quiz - "What happens if you lose your recovery phrase?" with three different options. That would be a more playful way to ensure people understand what their responsibilities are. Some other wallets require users to retype their seed to verify, that's another approach we could take.

![monero-seed-quiz-gbks-190329](https://user-images.githubusercontent.com/695901/55246583-caca7e00-5245-11e9-9c6f-f7b7457eac1c.png)



## rating89us | 2019-03-29T16:56:19+00:00
I like this list with 3 columns, but this would still incentivate users to do a PrintScreen. If you display words one by one, users will not have the idea of doing 25 PrintScreens.

Ideally the wallet should monitor for any Ctrl+C or PrintScreen events.

Instead of a quiz, I prefer making the user retype 5 random words of the 25. Retyping the whole seed should be avoided since you are leaking your recently generated seed.





## sanderfoobar | 2019-03-29T17:05:56+00:00
@rating89us Disagreed, I believe the point is to make sure the user is aware of how important this seed is. With this in mind, @GBKS dedicated 2 new screens - which communicates to the user 'this is important, you should write it down'. As for CTRL-C/PRINTSCRN, if the user wants to do that - fine by me. We just need to make sure the user knows he's shooting himself in the foot. 

Should not make it too hard for (power)users who know what the dangers are but choose to divert from our guidelines.

## selsta | 2019-03-29T17:08:14+00:00
I’m against no clipboard functionality.

## rating89us | 2019-03-29T17:12:35+00:00
Quoting Monero GUI user testing:
> ​​No tester wrote things down on paper (which was readily available), everybody just copy/pasted. One user was planning to store the seed in the cloud.

GUI wallet users are "normal" users.

Power users can use CLI or they can write down the words on a text editor and then copy.

## sanderfoobar | 2019-03-30T00:56:18+00:00
If a program (malware) has the ability to hijack the clipboard, it also has the ability to read the seed straight from process memory. Or take screenshots. Or steal the .keys file and monitor keystrokes for wallet passphrases. I don't see added value in blocking clipboard or printscreen, other than forcing users to write down their seed - which imo is better as a choice rather than a decision that was made for them, as long as we communicate clearly the former would be the sane course of action.

## GBKS | 2019-03-30T07:01:20+00:00
I found that some mobile wallets disable screenshot functionality during wallet creation, or show a warning when they detect that the user takes a screenshot (![example](https://www.cryptouxhandbook.com/images/user-onboarding/copay-onboarding-7-privacy-hint-screenshot-warning.png)). Not sure which of these are doable on desktop operating systems with the tech stack we use. I don't have a strong opinion on whether we should to do this or not. 

A "Copy" button could easily be added next to the "Download print template" button. 



## rating89us | 2019-03-30T10:13:58+00:00
I'm against blocking clipboard or printscreen, but I believe the wallet could monitor these events, and, when detected, warn the user that it is a dangerous action.

## ghost | 2019-04-19T11:47:06+00:00
Completely agree with this. Make sure the user can’t click next until they check the box also. 

<sub>Sent with <a href="http://githawk.com">GitHawk</a></sub>

## rating89us | 2020-06-11T19:59:12+00:00
@GBKS 
![image](https://user-images.githubusercontent.com/45968869/84433431-8fd81e80-ac2e-11ea-844e-10a00e05eb51.png)
I'm coding this page now. Do you have this icon with transparent background in .png and the @2x version of it?

Thanks

## GBKS | 2020-07-03T09:22:04+00:00
@rating89us sorry, just seeing it now. I assume it's too late to send you that icon now?

## rating89us | 2020-07-03T10:08:23+00:00
It's not late, I only need this icon to finish it. The code is ready :)

## GBKS | 2020-07-07T08:24:00+00:00
Here you go then, in 1x and 2x resolutions, for white and black backgrounds. Let me know if those work for you.
 
![write-seed-white](https://user-images.githubusercontent.com/695901/86747196-dfe2af00-c03b-11ea-9afa-db9937874000.png)
<img width="50" alt="write-seed-white@2x" src="https://user-images.githubusercontent.com/695901/86747199-e07b4580-c03b-11ea-9be1-5e1edb86f862.png">

![write-seed](https://user-images.githubusercontent.com/695901/86746703-88444380-c03b-11ea-939c-ee204195579a.png)
<img width="50" alt="write-seed@2x" src="https://user-images.githubusercontent.com/695901/86746709-89757080-c03b-11ea-97fe-d9f6bdb1f36e.png">


## rating89us | 2020-07-07T21:08:46+00:00
Since our default window size is not tall enough, I decided to use 5 columns to display the seed:
![image](https://user-images.githubusercontent.com/45968869/86843283-a4c99580-c0a6-11ea-91e3-61f65b8d4a4b.png)

Should we add an explanation for the restore height?
Should we add a "I understand" check box below the restore height?

## GBKS | 2020-07-08T11:03:37+00:00
The 5 columns look good.

Are you also planning to add the downloadable template?

I like having the checkbox as an extra friction point to make people think about what they are doing.

Wallet restore height is super confusing. I think there have been conversations around whether for it to be a block height or a date. "What month and year did you first use this wallet?" also does the job of narrowing down on the point of where blocks need to be inspected. I don't think it belongs on this page though. Is there another page where we can ask for this?

## rating89us | 2020-07-10T09:51:34+00:00
> Are you also planning to add the downloadable template?

Yes. Can you create a pdf template with a single page in landscape orientation, with the seed space disposed as in the monero GUI wizard (5 columns x 5 lines) and with two spaces to write down the "blockheight" and "wallet creation date"?

> Wallet restore height is super confusing. Is there another page where we can ask for this?

This page is not asking the wallet restore height, it is informing the user what is the current restore height while the wallet is being created. 

I agree that it is really confusing having to explain the user what it is and ask the user to write it down, but fortunately the wallet restore height will be included in the seed words of the next version of Monero seed, so the users will not have to write it down in the future.

## GBKS | 2020-08-06T12:14:02+00:00
Something like this?

<img width="1900" alt="Onboarding recovery phrase GBKS 200806" src="https://user-images.githubusercontent.com/695901/89530567-03da1180-d7ef-11ea-9635-c5f24689d44e.png">


## rating89us | 2020-09-06T13:31:32+00:00
Looks good to me. Could you share this pdf template?

## garlicgambit | 2020-09-15T17:52:02+00:00
In favor of putting the mnemonic seed on a separate page.  
  
Propose to switch the wallet password section with the mnemonic seed section on the "Create a new wallet" page. This will put the mnemonic seed on a separate page without introducing a new one.  
  
Would it make sense to put the mnemonic seed page before the "Create a new wallet" page? Or as early in the wizard as possible? Put the most important information at the beginning or end of the wizard? What is more important: the mnemonic seed or the wallet name/password? What UI/UX will make the user more likely to properly backup the mnemonic seed? Add a note on the first page that recommends users to grab a pen and paper?  
  
Recommendations for the text on the mnemonic seed page:  
  
- Mention the number of mnemonic words: 25  
- Mention that the order of words matters  
- Mention an alternative term for 'mnemonic seed'. Example: "recovery phrase aka mnemonic seed"  
- Mention to store the seed on a non-digital and persistent backup medium. Example: paper  
- Mention to store the backup at a safe place.  
  
Modified text of @rating89us:  
"IMPORTANT: The 25 words below are your recovery phrase or mnemonic seed for this wallet. You can use it to backup and restore this wallet. It is important that you write these words on a piece of paper in the correct order. Store this backup at a safe place. It's not recommend to store these words digitally (email, online cloud service or a computer file). Many have lost access to their wallet because they failed to make a proper backup. Don't be like them."  
  
Or spit the text in an instruction and explanation:  
"INSTRUCTIONS: write the 25 words listed below in the correct order on a piece of paper and verify that you've written them down correctly.  
  
IMPORTANT: The 25 words below are your recovery phrase or mnemonic seed for this wallet..."  
  
The note from the monero CLI wallet is also pretty good and to the point.  
  
Like the 5 columns mnemonic seed design. UI/UX question: order the words horizontally or vertically? Example with horizontal ordering:  
  
![seed-horizontal](https://user-images.githubusercontent.com/11670003/93245021-2a8a5100-f77a-11ea-8b28-e6f66cdeea1a.png)  
  
Like the print template. Suggest to add it as a separate file to the GUI archive. Make sure that it is possible to make the template deterministically reproducible. Is there enough space to write the words within the text fields? You can put the template in landscape mode to provide more space.  
  
Users also need a simple way to verify the backup of their mnemonic seed as mentioned in [this issue](https://github.com/monero-project/monero-gui/issues/910). One of the first rules of making backups is to verify that they work. This verification step could be on a separate page, but it is possible to add a 'Mnemonic seed verification' option to the mnemonic seed page. The verification page will remove some or all mnemonic words and allows the user to enter or select them.  
  
Example with the "Verify recovery phrase" button in the middle to make stand out from the other buttons:  
  
![verify-seed-button](https://user-images.githubusercontent.com/11670003/93245198-789f5480-f77a-11ea-9f9b-26f8748887ea.png)  
  
The empty recovery phrase verification page. User has to enter in 25 words. The right side has red X's to highlight that action is required:  
  
![verify-seed-empty-compare](https://user-images.githubusercontent.com/11670003/93245445-ddf34580-f77a-11ea-8478-82869f15cc59.png)  
  
Provide positive or negative feedback for each word:  
  
![verify-seed-feedback](https://user-images.githubusercontent.com/11670003/93245495-f1061580-f77a-11ea-920b-b40348744df8.png)
    
Seed verification page that requires the user to only verify a couple of mnemonic words. In this example one word per column:  
  
![verify-seed-partial-complete](https://user-images.githubusercontent.com/11670003/93245612-12670180-f77b-11ea-8c3f-e24f0955c43b.png)  
  
UI/UX design question: have the user type each mnemonic word or have a way to select the correct word or both? Selecting the correct word could speed up the verification process. The selection menu could limit the options to 2-25 words.  
  
Aside from a dedicated page, an alternative location for the mnemonic seed verification button/option would be the last page of the wizard. The summary table could add a row with: "Recovery seed verified" with a happy or sad face. Or something that will motivate people to verify their mnemonic seed, like an achievement.  
  
Idea: display a warning sign if the user has skipped mnemonic seed verification step in the wizard. This could be in the top bar next to the light/dark mode icon or somewhere else. This would be a reminder to verify the seed. It will disappear once the seed is verified. A large percentage of people will probably skip the mnemonic backup procedure in the wizard. This is human nature. UI/UX design has to take this into account and give people the option and reminder to fix this at a later stage.   
  
Example with some sample icons. The red warning sign is taken from [this design](https://github.com/monero-project/monero-gui/issues/2024) by @ghost.  
  
![verify-seed-icons](https://user-images.githubusercontent.com/11670003/93245663-227ee100-f77b-11ea-9f25-514160fc684b.png)  
  
The post-wizard seed verification option can be located at: Settings > Wallet.

## GBKS | 2020-09-16T09:09:48+00:00
@rating89us here's the template. Not sure if the PDF has the font embedded, so I also uploaded a PNG version of what it's supposed to look like. I assume there's not easy way to localize a PDF, right?

![monero-onboarding-recovery-phrase-template-gbks-200916](https://user-images.githubusercontent.com/695901/93316224-3a527580-f80c-11ea-94a5-723c37b6ca78.png)
[monero-onboarding-recovery-phrase-template-gbks-200916.pdf](https://github.com/monero-project/monero-gui/files/5231047/monero-onboarding-recovery-phrase-template-gbks-200916.pdf)

@garlicgambit one approach I like for verifying the seed is to show the words in a scrambled order and ask the user to click them in the correct order. I mocked this up [here](https://www.figma.com/file/tiU8sOzEZQq2kmsE89Vj21/Monero-Mobile-Concept?node-id=22%3A2422) for mobile.


## rating89us | 2020-09-16T18:03:01+00:00
- Added wallet name (so user can copy it in the PDF template)
- Added wallet creation date
- Added print PDF template button (not working yet)

I think we should verify the seed (ask user some words) in the next page.

![image](https://user-images.githubusercontent.com/45968869/93374605-3a2b9780-f857-11ea-8d35-78d6c9325868.png)




## garlicgambit | 2020-09-20T18:23:09+00:00
@GBKS does the template provide enough space to write the words in the text fields?  
  
Is it possible to print a GUI page instead of a pdf file? That would solve the localization issue.  
  
@rating89us prefer to minimize the options/info on the mnemonic seed page and have the most essential information at the top. Not in favor of adding the wallet name. Or at least put it below the mnemonic seed. In favor of adding the wallet creation date, because it makes sense to beginners.  
  
In favor of putting the seed verification step on the next page.  
  
What will the mnemonic restore page/option look like?

## selsta | 2020-09-20T18:55:26+00:00
> Is it possible to print a GUI page instead of a pdf file? 

No, this is not possible, unless I misunderstand what you want to do. Also the PDF looks way cleaner.

## rating89us | 2020-09-20T21:19:37+00:00
> Not in favor of adding the wallet name. Or at least put it below the mnemonic seed.

My intention is to display in a single page everything that the user must write down on the paper. But I see that it looks like a lot of information in a single page.

## GBKS | 2020-09-21T06:26:11+00:00
That does get pretty cluttered. But if the wallet name, recovery height and creation date not editable, then you don't need to show them as input fields. Simple text is enough.

<img width="1024" alt="onboarding - recovery phrase 200921" src="https://user-images.githubusercontent.com/695901/93737390-60e52780-fbe3-11ea-8f4a-9fd8a188e176.png">

@garlicgambit I printed the template, filled in some of the longer words and found it a comfortable amount of space (on an A4-size sheet).

## garlicgambit | 2020-09-22T18:21:02+00:00
@selsta ok, no printing. What about copy/pasting a text template from the GUI instead of printing a PDF. People would have to manually paste it into a word processor and print it, but it would be with the correct localization.  
  
@rating89us understood.  
  
@GBKS thanks for checking the print template.  
  
Suggestions for the the print template:  
Suggest to change: "Wallet name" to something like "Wallet name/description"  
  
Could add a (short) motivation why you would want to save the wallet creation date and block height. Perhaps add a short note like: "Wallet creation date (speedup sync)" or "Wallet creation date for faster sync".  
  
Text at the bottom of the print template:  
Change "specific oder" to "specific order".  
  
Remove "randomly chosen". This may confuse people.  
  
Could remove the second sentence.  
  
Suggest to add the getmonero.org domain somewhere on the template. This could be at the top and/or in the description at the bottom. This is in case someone wants to restore a wallet and has forgotten the domain. Or maybe someone other then the creator wants to restore the wallet. This can prevent people from going to scam sites.  
  
Prefer the GUI design by GBKS where the wallet name is below the seed, but wouldn't mind if it was removed from the page. Less is more idea.  
  
Is there a reason why the creation date and block height are currently editable?  
  
A couple of remixes of the latest designs by rating89us and GBKS:  
  
![seed-page-center](https://user-images.githubusercontent.com/11670003/93921100-9c751400-fcff-11ea-9a64-e975f45d9e58.png)  
  
This design includes the wallet name and has switched the 'Print PDF template' and 'Copy to Clipboard' buttons:  
  
![seed-page-wallet-name](https://user-images.githubusercontent.com/11670003/93921180-badb0f80-fcff-11ea-9318-e03c58927997.png)  
  
Same design without the wallet name:  
  
![seed-page-wallet-name-removed](https://user-images.githubusercontent.com/11670003/93921221-cc241c00-fcff-11ea-82a4-04a75d63e5a6.png)  
  
We prefer to switch the positions of the copy to clipboard and print to pdf template buttons.

## garlicgambit | 2020-10-30T19:45:22+00:00
This [issue](https://github.com/monero-ecosystem/monero-GUI-guide/issues/194) contains information on how to create a deterministically reproducible pdf with markdown. This may be relevant for the recovery phrase template.

## selsta | 2023-02-21T01:13:48+00:00
Resolved in #3878, thank you @rating89us

## thewhitegrizzli | 2024-03-27T15:04:23+00:00
how about do your own damn research and that's it?

# Action History
- Created by: GBKS | 2019-03-29T10:06:57+00:00
- Closed at: 2023-02-21T01:13:48+00:00
