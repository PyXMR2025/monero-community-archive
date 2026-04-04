---
title: Encrypted backup in a format designed for long life
source_url: https://github.com/monero-project/monero/issues/5492
author: fresheneesz
assignees: []
labels: []
created_at: '2019-04-24T22:16:08+00:00'
updated_at: '2019-10-12T15:03:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
So for me, the wallet words is completely fine. I copy them to a file I encrypt with NotepadCrypt which does AES encryption. But for your average joe. They're gonna write in a napkin or post-it or just keep it in some file on their networked computer in plain text. The default backup method shouldn't be "copy they keys to your wallet to your clipboard and paste it somewhere" or even "write it down on a piece of flammable material". Sure wallet words are nice to have, but it should be behind a warning that warns about how to properly secure and back up your keys.

What I want to suggest is a more fool-proof (in the original meaning of the word) default method of backing up your wallet. The goal is to give users who opt for the defaults a very safe and secure backup method. It would be nice if its also recoverable long after the current versions of monero software is no longer available for some reason (by making it human readable without external documentation). 

The format should almost definitely be separate from the monero project, whether we use an existing format or create a new one. If there is a good candidate for a standard encrypted backup format I don't know one, but if there is an existing format that fits the criteria, we should use it over creating a new one. I'll describe what I'd like to see in this format.

Requirements:
* The default backup should be a format containing both plain text and encrypted data, where examining the plain text clearly shows:
  1. The specific algorithm being used to encrypt (so someone in 100 years can easily figure out how to encrypt if they somehow have the password). This could be as simple as "encrypted with AES vX.X.X with Y padding.." etc, or it could also describe the whole algorithm explicitly.
  2. How to determine the section of the format that has encrypted data
* Monero's wallet UI should also be better about giving users instructions for safe secure backup, which I already talked about in [monero-gui issue 741](https://github.com/monero-project/monero-gui/issues/741), so I won't repeat here.

I think its might also important to include a couple other types of backups:
* Multi-signature backups - a backup where multiple passwords are necessary to decrypt the backup. This way you can give back ups to multiple trusted people who can unlock your xmr if you die or something (and they then find a note in your will telling them who has the proper keys. 
* Unencrypted backup? This is what we currently have. Some people might want to put something like this in a safety deposit box or something like that. But instructions NEED to specify that this is probably less secure than other methods and that it needs to be locked in a way that someone couldn't steal it. 

For the primary backup, I suggest a 256 or 512 bit AES encrypted key that looks something like this:

```
âãÏÓ monero-backup-AES-512-CBC nonce-prepended-to-password: 53df00a8b0ec2c097235e495a447cbe95276 EncryptedBackup-OpenPGPBase64RFC4880: 1GbVUSW5WJmRCpaCJ4hanUny77oDaWW4to5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o5WJmRCpaCJ4hanUny77o
```

Where the file format is:
1. First 4 bytes are a "magic number" identifying the file type
2. 5th byte is a sub-type. This can be set to 0 until there are more files types.
3. Next set of bytes is the ascii string " monero-backup-AES-512-CBC nonce-prepended-to-password: "
4. Next set of bytes is a password nonce, a random ASCII string prepended to the password when decrypting
5. Next set of bytes is the ascii string " EncryptedBackup-OpenPGPBase64RFC4880: "
6. Last set of bytes is the actual encrypted backup (of the wallet words), represented as a Hex ascii string. This should be encrypted with the same password used to unlock the on-disk 

This format is inspired by [the info here](http://www.real-me.net/ddyer/notepad/NotepadCrypt-technotes.html). Even better would be to store the file in a way that is durable to data corruption. An easy way of doing this is to simply copy most of the file data say 3 times in the file, so that if corruption happens to one, other parts of the file can be used to fully recover. There are probably better ways to do it, but I'm not sure if there are ways that are also easily human readable. 

What we could also do is put detailed instructions about the technical details of the encryption directly into the file so no external source is needed for anything (ie you could still recover your monero in a bunker cut off from the internet). 

This file can (probably should) also replace the current `.keys` wallet file used to load your monero wallet in normal use. 

Thoughts?


# Discussion History
## moneromooo-monero | 2019-04-24T23:43:39+00:00
I kinda like the idea of an error correcting file which includes instructions.

You can't recover your monero without the internet (or whatever network we use in the future) since a blockchain is a consensus data structure, where a transaction needs to be processed by at least some large subset of the network in order to have any kind of close-to-finality. But I get your point :)

## binaryFate | 2019-10-12T15:03:14+00:00
In the meantime anyone interested in that sort of super long term thing should simply backup the Monero source code of the version used to generate the wallet. Obviously this is the best description of the algorithm used for wallet generation.

# Action History
- Created by: fresheneesz | 2019-04-24T22:16:08+00:00
