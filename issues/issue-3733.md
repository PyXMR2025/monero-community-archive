---
title: monero-wallet-cli at boot/crontab
source_url: https://github.com/monero-project/monero/issues/3733
author: cryptify
assignees: []
labels: []
created_at: '2018-04-30T07:20:17+00:00'
updated_at: '2018-05-01T10:44:40+00:00'
type: issue
status: closed
closed_at: '2018-05-01T10:44:40+00:00'
---

# Original Description
I managed to get monerod to run at boot by making a script like:

--------------------
#!/bin/sh

kill -9 | grep ./monero/monero-v0.12.0.0/monerod

./monero/monero-v0.12.0.0/monerod --detach

---------------------------------

chmod +x the file and then add it to crontab. it works, monerod opens and begins syncing at boot.

however, i want to run monero-wallet-cli from boot as well.

the same script, however, does not work. I have tried everything, that script, running it directly from crontab, everything. but the monero-wallet-cli simply will not open at boot. even if i pass the --wallet-file and --password options, and even if i pass the --detach option (although i would rather it open in a screen so i can watch the wallet)

how can i get monero-wallet-cli to run from boot in crontab??

# Discussion History
## moneromooo-monero | 2018-04-30T08:09:15+00:00
You want monero-wallet-rpc for this.

## cryptify | 2018-04-30T08:59:41+00:00
doh! i feel dumb. ok I'm testing the monero-wallet-rpc. I think like monerod it's gonna need a little refinement - took me forever to figure out the --detach flag and that screen will not work with it on crontab.

## cryptify | 2018-04-30T09:18:02+00:00
okay the script doesn't work, monero-wallet-rpc doesn't take --detach, the & flag isn't working, nohup isn't working, crontab won't do it, what am i doing wrong here? 

## cryptify | 2018-04-30T09:19:06+00:00
i'm trying to pass in ./monero/monero-v0.12.0.0/monero-wallet-rpc --rpc-bind-port 8082 --wallet-file file --password passx

just for reference

it works on its own, but not when i try to make it reboot

## gene-telligent | 2018-04-30T17:38:03+00:00
What OS are you running on? If you're on a Linux system that uses systemd or init.d, there are better options of starting an always-on service than a cron script.

Also, don't pass your password to monero-wallet-rpc in cleartext on the command line. That's a huge security vulnerability. Put it in a file and chmod 600 it, and use the flag --password-file instead.

## cryptify | 2018-05-01T09:54:40+00:00
ubuntu 14.04


yeah I figured I would change the password file after I got it to actually boot, just testing it for now

I like cron because it's so easy lol, and I use it with my eth machines. I will look into trying upstart and let you guys know how it goes, thank you so much for the help

## cryptify | 2018-05-01T10:38:07+00:00
ok so I tried upstart but no dice, it would say "service stop/waiting" even when I tried to manually run it.

however that led me down a rabbit hole and i sorted the problem out (i believe - it's working now, anyways, we'll see over the next few days)

what I ended up doing was writing a script similar to the one in OP for the cli, and then I added it to reboot as:

@reboot sleep 45 && ./script.sh

and it worked. it seems crontab performs actions before login so the sleep parameter was needed to make the CLI start up after. 

sometimes it's the simplest things... lol

# Action History
- Created by: cryptify | 2018-04-30T07:20:17+00:00
- Closed at: 2018-05-01T10:44:40+00:00
