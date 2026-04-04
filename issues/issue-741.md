---
title: 'Feature Request: Encrypted backup in standard format'
source_url: https://github.com/monero-project/monero-gui/issues/741
author: fresheneesz
assignees: []
labels:
- invalid
created_at: '2017-05-24T06:32:49+00:00'
updated_at: '2019-04-24T13:18:48+00:00'
type: issue
status: closed
closed_at: '2019-04-24T13:18:48+00:00'
---

# Original Description
So for me, the wallet words is completely fine. I copy them to a file I encrypt with [NotepadCrypt](http://www.andromeda.com/people/ddyer/notepad/NotepadCrypt.html) which does AES encryption. But for your average joe. They're gonna write in a napkin or post-it or just keep it in some file on their networked computer in plain text. The default backup method shouldn't be "copy they keys to your wallet to your clipboard and paste it somewhere" or even "write it down on a piece of flammable material". 

Sure wallet words are nice to have, but it should be behind a warning that warns about how to properly secure and back up your keys. 



# Discussion History
## medusadigital | 2017-08-08T00:43:28+00:00
sorry i do not understand your feature request.

can you be more precise ?



## fresheneesz | 2017-08-08T01:46:51+00:00
What I'm suggesting is a more fool-proof (in the original meaning of the word) default method of backing up your wallet. The goal is to give users who opt for the defaults a very safe and secure backup method. It would be nice if its also recoverable long after the current versions of monero software is no longer available for some reason (by making it human readable without external documentation).

Requirements:
* The default backup should be encrypted in a format where examining the plain text clearly shows:
  1. The specific algorithm being used to encrypt (so someone in 100 years can easily figure out how to encrypt if they somehow have the password)
  2. The section of the format that has encrypted data
* Instructions should be given (or linked to) that clearly spell out:
  1. The reasons for backing up
  2. How to properly and safely store the backup (ie store it in multiple places, in multiple mediums, also give advice on the decay rate of common mediums like hard drives, ssds, optical formats, and paper)

I think its might also important to include a couple other types of backups:
* Multi-signature backups - a backup where multiple passwords are necessary to decrypt the backup. This way you can give back ups to multiple trusted people who can unlock your xmr if you die or something (and they then find a note in your will telling them who has the proper keys. 
* Unencrypted backup? This is what we currently have. Some people might want to put something like this in a safety deposit box or something like that. But instructions NEED to specify that this is probably less secure than other methods and that it needs to be locked in a way that someone couldn't steal it. 

For the primary backup, I suggest a 256 or 512 bit AES encrypted key that looks something like this:

```
âãÏÓ monero-backup-AES-512-CBC nonce-prepended-to-password: 53df00a8b0ec2c097235e495a447cbe95276 EncryptedBackup: 1GbVUSW5WJmRCpaCJ4hanUny77oDaWW4to5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o
```

Where the file format is:
1. First 4 bytes are a "magic number" identifying the file type
2. 5th byte is a sub-type. This can be set to 0 until there are more files types.
3. Next set of bytes is the ascii string " monero-backup-AES-512-CBC nonce-prepended-to-password: "
4. Next set of bytes is a password nonce, a random ASCII string prepended to the password when decrypting
5. Next set of bytes is the ascii string " EncryptedBackup-HexFormat: "
6. Last set of bytes is the actual encrypted backup (of the wallet words), represented as a Hex ascii string. This should be encrypted with the same password used to unlock the on-disk 

This format is based on info here: http://www.andromeda.com/people/ddyer/notepad/NotepadCrypt-technotes.html . Even better would be to store the file in a way that is durable to data corruption. An easy way of doing this is to simply copy most of the file data say 3 times in the file, so that if corruption happens to one, other parts of the file can be used to fully recover. There are probably better ways to do it, but I'm not sure if there are ways that are also easily human readable. 

What we could also do is put detailed instructions about the technical details of the encryption directly into the file so no external source is needed for anything. 

This file can (probably should) also replace the current `.keys` wallet file used to load your monero wallet in normal use. 

Some instructions I can think of for the default encrypted backup (not exhaustive):
* **DO NOT LOSE YOUR PASSWORD**. If you lose your password, you will not be able to recover from this backup.
* **DO NOT LOSE YOUR BACKUP FILE**.
* Copy your backup file to multiple separate storage mediums. Best practice is to store the backup on multiple different types of mediums as well (for example, store on a hard disk, a USB disk, and an optical disk).
  * Keep in mind that most hard disks and optical disks lose data after being 5-10 years old. Solid state drives may only last 1 or 2 years. Paper can last for centuries. Some disks, like the Blue Ray M-Disk is rated to last 1000 years. Choose your backup mediums wisely.
* Store the backups in multiple physical locations that are physically distant from each other (for example, in a relative's home, a safety deposit box at a bank, and in your own home)
* Store the backups in locations that are safe from disasters like fires and floods. 
* **TEST YOUR BACKUP**. Before you put any xmr into your wallet, delete your local wallet and make sure you can restore it from your backups. Do this again once you put a small amount of xmr in your wallet, so that you are sure the restore process really works.

I also thought about including information on securely storing significant wealth in cold-storage and hardware wallets (ie not on your local machine), but that's less about backing up and more about mitigating the risk of virus attempts to steal your XMR. 

Thoughts?


## selsta | 2019-04-24T13:02:16+00:00
We are currently improving the seed page to make it more clear what you should and shouldn’t do.

Regarding a different backup format, please open an issue here: https://github.com/monero-project/monero/issues

+invalid

# Action History
- Created by: fresheneesz | 2017-05-24T06:32:49+00:00
- Closed at: 2019-04-24T13:18:48+00:00
