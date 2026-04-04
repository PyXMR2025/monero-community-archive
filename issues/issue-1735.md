---
title: Issue with smart mining
source_url: https://github.com/monero-project/monero/issues/1735
author: ghost
assignees: []
labels: []
created_at: '2017-02-15T10:29:07+00:00'
updated_at: '2017-02-23T07:30:27+00:00'
type: issue
status: closed
closed_at: '2017-02-23T07:30:27+00:00'
---

# Original Description
Hi @revler1082 I've just gone into `monero-wallet-cli` and entered `start_mining 4` as I used to do. It used to get me 12H/s (amazing, I know)...but now it just says `smart mining at 0H/s`.

Two questions:

1.  Do you know why my setup thinks it's background mining, and then only at 0H/s?

2. Would you add a `background mining` option to monero-wallet-cli

Thanks!

# Discussion History
## revler1082 | 2017-02-15T11:33:09+00:00
@NanoAkron Hmm, I never tested through the wallet, just daemon (/sorry).

Thanks for testing. Can you tell me what happens if you start mining through the daemon with **start_mining address 4 true**?

Few other things
* Current idle threshold is 90%, so if you have background processes running that take up 15% CPU, background mining will never be triggered
* If you're not plugged in, background mining will never be triggered
* If background mining is enabled, but not started (ie because not plugged in), status will show **smart mining at 0H/s**

## revler1082 | 2017-02-15T11:45:01+00:00
Taking a quick glance, it looks like I'll have to add some argument handling when starting mining through the wallet. I'll try to submit a patch when I get home from work =)

## ghost | 2017-02-15T14:50:51+00:00
Thanks @revler1082.

Trying what you suggested still leaves things at 0H/s, whether 1,2,3, or 4 mining processes are started. This is a little Odroid C2 ARMv8 machine which is always plugged in. 

In `htop` I've got 15 `monerod --detach` processes consuming 0% each, with the occasional one blipping up to 11% without mining. After starting smart mining this jumps to 20 processes at 0% each, with the occasional blip up to 19%.

## revler1082 | 2017-02-15T16:36:03+00:00
Hmm, off the top of my head I'd say the power status querying is failing:

```
 #elif defined(__linux__)

      // i've only tested on UBUNTU, these paths might be different on other systems
      // need to figure out a way to make this more flexible
      const std::string POWER_SUPPLY_STATUS_PATH = "/sys/class/power_supply/ACAD/online";

```
Does that path exist on your system?

## vtnerd | 2017-02-15T17:51:28+00:00
It does not exist on my laptop. Vanilla 3.12 kernel. `/sys/class/power_supply/AC/online` seems to be the path instead.

## ghost | 2017-02-15T23:32:07+00:00
Will look myself once at home. 

Is it not possible to differentiate 'forced' mining from smart mining in some way - presumably we eventually want smart mining to be default on when we have a global p2pool, but I should still be able to force my system to mine ignoring power settings etc. 

## revler1082 | 2017-02-15T23:45:46+00:00
That's what that last parameter is, if you just leave it off or specify anything but "true", then you will mine normally i.e. full speed

## ghost | 2017-02-16T01:07:47+00:00
Ah ok. So putting true there should have made my little thing mine properly. 

## revler1082 | 2017-02-16T01:15:10+00:00
Apologies if my explanation is confusing. That last parameter is whether or not to smart mine. If you want to mine as before, either leave it out, or set it to anything but "true". 

This is for starting mining through the daemon. I'm going to have to submit a patch for the wallet.

# Action History
- Created by: ghost | 2017-02-15T10:29:07+00:00
- Closed at: 2017-02-23T07:30:27+00:00
