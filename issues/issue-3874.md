---
title: 'Couldn''t open wallet: invalid signature (i.e. Update error message for corrupted
  wallet files)'
source_url: https://github.com/monero-project/monero-gui/issues/3874
author: elibroftw
assignees: []
labels: []
created_at: '2022-03-30T03:13:49+00:00'
updated_at: '2025-08-04T18:23:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://user-images.githubusercontent.com/21298211/160743866-54e377ff-249c-4254-9861-c952c7051aec.png)

Trying to open a wallet and encountering this. Not sure if it's because I had to restart my computer via PC button today.

# Discussion History
## elibroftw | 2022-03-30T03:23:47+00:00
Already replaced the wallet files with a backup so can't do more testing.

## selsta | 2022-03-30T03:25:04+00:00
It means the wallet cache is corrupted, seems to be related to your force shutdown.

## elibroftw | 2022-03-30T03:26:11+00:00
Okay then can that error message be updated? 

## elibroftw | 2022-03-31T05:15:04+00:00
Or better yet, after every wallet save or auto save, a backup file should be generated. Then in these cases where the file is corrupted, just look for a backup file and overwrite the wallet file with it. 

## elibroftw | 2022-03-31T05:16:13+00:00
And I guess document what autosave actually does and why a user would want it enabled or disabled. What does the wallet do or not do if auto save is disabled?

## selsta | 2022-03-31T18:52:56+00:00
Autosave means it automatically saves the wallet every x minutes. Otherwise it only saves on exit and after a transaction if I remember correctly.

## elibroftw | 2022-03-31T19:14:46+00:00
What are the consequences though? Does it save the last scanned height or something? 

## selsta | 2022-04-02T01:39:43+00:00
Yes, scanned blocks get saved in the wallet cache. If you close without saving it has to rescan from the last saved height.

## MaxMusienko | 2022-08-23T20:17:02+00:00
Hi all! I have a similar situation today. **Couldn't open wallet: invalid signature**  Please tell me how to solve the problem? Thank you!

## elibroftw | 2022-08-23T20:51:14+00:00
You can either restore your wallet from seed, or use a backup file. Since I have two devices, I just replaced my local wallet files with the ones I had backed up on the cloud.

## MaxMusienko | 2022-08-23T21:28:25+00:00
I have solved this problem! Deleted the cache file and was able to log into the program! Here is the link with which I found the solution! Good luck to everyone! 
https://monero.stackexchange.com/questions/3122/how-do-i-delete-the-wallet-cache/3123

## selsta | 2022-08-23T21:30:01+00:00
@MaxMusienko make sure that you also have your seed backed up in case your whole hard drive fails

## sfsquires | 2022-08-24T01:49:37+00:00
@MaxMusienko made an account just to say thanks for the link, really good timing u saved me a lot of headache

## monirgh1365-del | 2025-08-04T16:16:15+00:00
> I have solved this problem! Deleted the cache file and was able to log into the program! Here is the link with which I found the solution! Good luck to everyone! https://monero.stackexchange.com/questions/3122/how-do-i-delete-the-wallet-cache/3123

Hello Thank you for your helpful guidance. I was getting an "invalid signature" error, which is why I followed your suggestion. However, now my wallet shows that my Monero balance is zero. How can I recover my Monero?

## nahuhh | 2025-08-04T18:23:56+00:00
> Hello Thank you for your helpful guidance. I was getting an "invalid signature" error, which is why I followed your suggestion. However, now my wallet shows that my Monero balance is zero. How can I recover my Monero?

wait for the wallet to finish syncing



# Action History
- Created by: elibroftw | 2022-03-30T03:13:49+00:00
