---
title: Create and maintain apparmor profiles for Monero binaries
source_url: https://github.com/monero-project/monero/issues/6705
author: garlicgambit
assignees: []
labels: []
created_at: '2020-07-13T17:51:35+00:00'
updated_at: '2021-09-24T16:14:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Create and maintain apparmor profiles for the Monero binaries.  
  
Start with the most popular binaries: monerod, monero-wallet-cli and monero-wallet-gui.  
  
Suggest to start with a basic blacklist approach. Block access to locations like ~/.ssh/ and other obvious ones. Take a look at apparmor.d/abstractions/private-files and private-files-strict. Experiment a while to get a good idea about which locations and permissions to use and gradually increase the restrictions.  
  
Motivation: defense in depth.

# Discussion History
## garlicgambit | 2020-08-06T18:26:17+00:00
This is a [relevant post](https://np.reddit.com/r/Monero/comments/hvynq2/what_the_monero_community_could_do_to_improve_the/) by @adrelanos from Whonix. He recommends that the Monero project (upstream) creates and maintains the apparmor profiles.  
  
@00-matt you mentioned that you have an apparmor profile for monerod and would be willing to share it. Would you please be so kind to do that. In case you or others want to make a pull request, @moneromooo-monero mentioned on irc to put the apparmor profiles in the contrib directory.  
  
Would like to see support for other MACs like selinux as well, but those will need their own github issues.

## moneromooo-monero | 2020-08-07T00:22:19+00:00
Yes please, contrib/apparmor/ would be a good place. Being willing to maintain it if needed would be even better :)

## 00-matt | 2020-08-07T09:17:20+00:00
A problem that I have is not knowing if users have changed --data-dir or where they store their wallet files.

It's no issue for users installing the profiles themselves, they can just edit a variable at the top of the profile. It just might be very confusing for someone that has done `apt install monero` and then they don't know why their wallet closes as soon as they try to open it.

## adrelanos | 2020-08-07T10:32:25+00:00
Matt Smith:
> A problem that I have is not knowing if users have changed --data-dir or where they store their wallet files.


Custom data dir paths are unsupported for any application that ships
apparmor profiles that I know.

I'd suggest to whitelist ~/.bitmonero and perhaps another custom folder.
Then advice users to move their data dir as sub directories in any
apparmor white listed directory.

> It just might be very confusing for someone that has done `apt install monero` and then they don't know why their wallet closes as soon as they try to open it. 


Can a test be added to monero which checks if --data-dir is readable and
if not, point that out with an error popup? Posting some link to help,
perhaps mentioning could be an apparmor issue?


## 00-matt | 2020-08-07T11:50:17+00:00
> I'd suggest to whitelist ~/.bitmonero and perhaps another custom folder.

Yes I just went with ~/.bitmonero for the daemon, and ~/Documents/Monero for wallet cli at the moment.

> Can a test be added to monero which checks if --data-dir is readable and if not, point that out with an error popup? Posting some link to help, perhaps mentioning could be an apparmor issue?

I'll check what the error is now, it might be good enough already.

## 00-matt | 2020-08-08T16:24:57+00:00
Here's the error when the --data-dir is blocked by the apparmor profile:

```
2020-08-08 15:16:29.349	I Loading blockchain from folder /path/to/lmdb ...
2020-08-08 15:16:29.349	W Failed to check for mmap support: open failed: Permission denied
2020-08-08 15:16:29.355	E Error opening database: Failed to check for mmap support: open failed: Permission denied
```

Here's the error when the wallet file is blocked by the apparmor profile:

```
Error: failed to load wallet: internal error: "./walletname.keys" is opened by another wallet program
```

## moneromooo-monero | 2020-08-08T21:08:47+00:00
Check the wallet log, you sohuld get the errno that caused the failure. Compare to the errno whe nthe wallet is actually opened by another program.

## garlicgambit | 2020-08-10T19:14:20+00:00
@00-matt consider the apparmor profiles experimental for now. Recommend package maintainers/distros to not install them by default with the monero binaries. Recommend to create a separate package like 'monero-apparmor-profiles' or something like it to install the profiles. This can be broken down into individual apparmor packages for each binary (monerod, monero-wallet-cli) and one meta package to install all the apparmor profiles.  
  
Basic instructions to troubleshoot apparmor are likely needed. Some suggestions:  
  
- A link to a [source](https://ubuntu.com/server/docs/security-apparmor) that explains the basics of apparmor  
- How to disable/enable a specific apparmor profile for the monero binaries (sudo aa-complain /path/to/bin + sudo aa-enforce /path/to/bin).  
- How to check the status of a profile (aa-status).  
- How to add a rule when using a different data-dir. That should probably be in /etc/apparmor.d/local/profile.name. The main profile should link to it and the (empty?) local/profile.name should be created automatically upon install of the apparmor profiles.  
- How to reload a profile (sudo apparmor_parser -r /etc/apparmor.d/profile.name).  
  
How can you make modifications to /etc/apparmor.d/local/profile.name by users as simple and foolproof as possible?  
  
- Have some sample rules in there that are disabled by default?  
- Add a note to the file to reload the profile after making any changes?  
- Package managers should not update this file once it has been installed

## adrelanos | 2020-08-11T09:20:36+00:00
garlicgambit:
> Recommend to create a separate package like 'monero-apparmor-profiles' or something like it to install the profiles.


I see.

> This can be broken down into individual apparmor packages for each binary (monerod, monero-wallet-cli) and one meta package to install all the apparmor profiles.  


Many packages which all just ship one file are usually not sustainable.
I don't see any reason to not put all apparmor profiles into one package.

> How can you make modifications to /etc/apparmor.d/local/profile.name by users as simple and foolproof as possible?  


In Debian all files in folder /etc/apparmor.d/local are empty by
default. (Same as "sudo touch /etc/apparmor.d/local/profile.name".)

> - Have some sample rules in there that are disabled by default?


In Debian: no

> - Add a note to the file to reload the profile after making any changes?  


I don't think it's up to monero to create general apparmor documentation.

> - Package managers should not update this file once it has been installed


Indeed. This is the default in Debian.


## Dresden945 | 2021-09-24T16:14:23+00:00
This is a complex topic. I'd ask what do you think about this:
- i've changed the default location from CLI monerod due to disk space to an externat hdd
- run'd the monerod with the new path
- received this error (failed to check for mmap support open failed permission denied)

Since the hdd can't hold the whole blockchain, i am wondering how to fix tha mmap issue and successfully use the new external hdd path

# Action History
- Created by: garlicgambit | 2020-07-13T17:51:35+00:00
