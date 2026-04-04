---
title: Store the deterministic wallet seed serialized in the '.keys' file
source_url: https://github.com/monero-project/monero/issues/59
author: Jojatekok
assignees: []
labels: []
created_at: '2014-07-12T08:28:03+00:00'
updated_at: '2014-08-05T07:44:27+00:00'
type: issue
status: closed
closed_at: '2014-08-05T07:44:27+00:00'
---

# Original Description
It would be great to have the opportunity of retrieving our _(newly-generated)_ wallets' seeds, as it is one of the most convenient ways of making a backup.

My idea is to store the seeds **permamently** _(encrypted in the '.keys' file),_ in order to let the users retrieve them anytime with an RPC command. The command should return an empty string _(or a **specific** error)_ whether the wallet's '.keys' file doesn't contain a seed.


# Discussion History
## Neozaru | 2014-07-12T08:39:20+00:00
Isn't the seed a representation of the private key (in deterministic mode) ? If so, it would be possible to get seed from private key directly.

I don't think we should be able to get it from RPC command, since it assumes the user network is safe.
It's a good practice to display the seed only once. You can ask the user to repeat/retype it at this time.


## Jojatekok | 2014-07-12T09:51:47+00:00
I was not sure about getting the seed from the key privately, but if it's possible, then it's even better.

I also understand why it should **not** be sent through the RPC, but then, it could still be displayed in the command prompt by a command.

**There may also be a separate console application _(or even better: class library)_ which outputs seeds from the input '.keys' files.** _By the way I want this to be implemented because of easier retrieval when creating backups from GUI wallets._


## fluffypony | 2014-07-18T08:35:22+00:00
@tewinget can comment on this, but I agree that the seed should be stored for future recall.


## fluffypony | 2014-08-01T08:42:29+00:00
@jakoblind may want to do this, as he's just been digging around in the wallet code

I think coupled with this would be:
- CLI/RPC methods to retrieve the mnemonic
- CLI/RPC methods to change the password (at a guess I'd think this involves nuking the .bin.keys and .bin files and recreating them, encrypted with the new password)


## jakoblind | 2014-08-01T09:33:03+00:00
will take a look at this one when I'm done with #36 


## Jojatekok | 2014-08-01T12:33:28+00:00
@fluffypony Nuking must happen safely:

1.) Rename the wallet files to '.bin.old' and '.bin.keys.old'
2.) Write the new wallet files
3.) Send a request to the network indicating that the password has been changed
4.) Remove the old wallet files

_(Step 2 and 3 may be merged or reversed if necessary)_

Also, there should be an ability to remove passphrase protection from wallets.


## fluffypony | 2014-08-01T12:35:44+00:00
@Jojatekok the network doesn't know about your password, so that isn't necessary:) Removing the .bin can be done unsafely, since it's just a cache. The .bin.keys file won't be removed, it'll just be overwritten by the new serialised data, so it's a safe action.


## jakoblind | 2014-08-01T13:51:45+00:00
I've added a seed command to the CLI (are we sure we want this in the RPC also?). Should I add extra password protection to that command?

https://github.com/jakoblind/bitmonero/commits/seed_command


## fluffypony | 2014-08-01T16:28:10+00:00
@jakoblind don't add password protection to that command, if the RPC API for the wallet is compromised the attacker can just transfer the funds out anyway. We do need HTTPS and Simple Auth for RPC, but rather than extend epee (which is over-templates and ill-suited to Monero in the long run) we're going to replace the RPC stuff either with our own code or with a library. Feel free to hop in on #monero-dev when you're around to discuss that, and you're welcome to run with that task once we've all decided on the best way to do it:)


## tewinget | 2014-08-01T17:20:43+00:00
@jakoblind unless I misread, your seed command treats the private send key as the seed and converts that to mnemonic words, but that key is not the seed.  You'll want to change the wallet keys generation part to store the seed, as it is not currently stored, just printed.


## jakoblind | 2014-08-01T17:53:51+00:00
@tewinget what is the seed then? The code works fine for me. I will continue the discussion over IRC :)


## fluffypony | 2014-08-01T22:19:15+00:00
@tewinget @jakoblind It's just occurred to me that we have a greater problem: changing the data structure of the .keys file will mean it can't open old wallets. I think we're going to need a version to the data structure, and if it encounters an old version (or the original unversioned data) it should automatically convert that .keys file to the latest version. After a year we can deprecate the old formats, with a note that old tagged releases can be used to convert them before opening them in a "current" wallet app.


## Jojatekok | 2014-08-02T14:21:06+00:00
@fluffypony Excatly, that's a great idea! I already have a proof of concept for this [implemented in Monero Client .NET](https://github.com/Jojatekok/monero-client-net/blob/0f047f9b430038e59dbfcffcc4b8425d8c87b0fd/MoneroGui/Objects/SettingsManager.cs#L121), which automatically converts the old setting values to new ones.


## fluffypony | 2014-08-02T14:23:15+00:00
@Jojatekok turns out to be a non-issue, as the seed is already stored in the .keys file, but in future this is the general idea for the workflow behind switching data formats:)


## fluffypony | 2014-08-02T14:25:59+00:00
@jakoblind please PR your change so I can merge it, then we can do the in-memory key encryption/mlock etc. stuff separately


## jakoblind | 2014-08-02T16:17:00+00:00
now the function fail and spit out a notice if the wallet is non-deterministic. @fluffypony could you test with an old wallet if it works? I dont have access to old wallets.


## tewinget | 2014-08-02T16:41:06+00:00
@jakoblind, you can create an "old" wallet with the --non-deterministic
flag during wallet creation.

On Sat, Aug 2, 2014 at 12:17 PM, Jakob Lind notifications@github.com
wrote:

> now the function fail and spit out a notice if the wallet is
> non-deterministic. @fluffypony https://github.com/fluffypony could you
> test with an old wallet if it works? I dont have access to old wallets.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/59#issuecomment-50967004
> .

## 

Thomas Winget
Computer Engineering
Purdue University '12


## jakoblind | 2014-08-02T16:49:07+00:00
@tewinget thanks for info. The code seems to work. Will implement the RPC calls before I do a PR.


## fluffypony | 2014-08-05T07:44:27+00:00
Merged and closed


# Action History
- Created by: Jojatekok | 2014-07-12T08:28:03+00:00
- Closed at: 2014-08-05T07:44:27+00:00
