---
title: Daemon background mining with wallet-cli in v0.14.1.0
source_url: https://github.com/monero-project/monero/issues/5660
author: normoes
assignees: []
labels:
- invalid
created_at: '2019-06-17T07:14:44+00:00'
updated_at: '2019-08-28T11:09:46+00:00'
type: issue
status: closed
closed_at: '2019-08-28T11:09:46+00:00'
---

# Original Description
I built the new tag Monero 'Boron Butterfly' (v0.14.1.0-29a505d1c)`.
I did not test it with a previous version.

I opened a view-only wallet and the dameon timed-out. I am not sure, whether those are relevant settings for this to happen.

It showed the folloiwng log (see below).

The most important part is, that the wallet asked me to dis/enable background mining for the daemon.

Is this supposed to happen?

---

Log:

```
Monero 'Boron Butterfly' (v0.14.1.0-29a505d1c)
Logging to monero-wallet-cli.log
Opened watch-only wallet: xxx
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
The daemon is not set up to background mine.
With background mining enabled, the daemon will mine when idle and not on batttery.
Enabling this supports the network you are using, and makes you eligible for receiving new monero
Do you want to do it now? (Y/Yes/N/No): : ^C^C^C^CBackground mining not enabled. Set setup-background-mining to 1 to change.
```

# Discussion History
## normoes | 2019-06-17T07:25:18+00:00
When creating a new wallet, the same question is asked.

Is this a new setting? And is `setup-background-mining = yes` the default setting for existing wallets? 

I was only asked for 2 wallets in the case described above, there have been other wallets where the value was just set to `yes`.

With `setup-background-mining = no`, `Background mining not enabled. Run "set setup-background-mining 1" to change.` is displayed in red everythime I start the cli.

Furthermore, why is this a setting in the first place? What does it do exactly?

## moneromooo-monero | 2019-06-17T09:23:23+00:00
Yes, it's supposed to. The default setting is to ask. If you have a default to yes, can you list the steps you do to get there ? There's a setting because it's be impolite to do it without asking I think.

## normoes | 2019-06-17T10:25:07+00:00
Ok, to be honest, I didn't really understand that setting.

After checking again, I found, that the wallet that was configured with `setup-background-mining = yes` actually was connected to a daemon that already mined to that wallet. So nothing wrong here.

I think, I was just confused by the question in general and by the red error/warning in particular.

I am going to close this issue. Sorry for the mess ;)

## josef-v | 2019-06-21T12:56:48+00:00
I am not sure if it wouldn't be best to open a new issue for this, but my question is still highly related.
Is it possible to generate a new wallet from `json` without any user interaction?
The thing is that in `v0.14.1.0` `monero-wallet-cli` always asks for a setup-background-mining.  I have been looking into the code and I don't think it is possible right now, so the correct question is probably: should it be?

Our use case:
We have a docker image for our testing environment. It contains `monero-wallet-cli` and `monero-wallet-rpc`. First, a wallet is generated from given `json` by `monero-wallet-cli`. Then a `monero-wallet-rpc` is started for the wallet. Reasons for this is that we want the same predetermined wallet each time we run the testing environment but we don't want a binary wallet file in git.
One option would be to pipe a `yes` into the command, but i found it to be a really dirty solution.

## normoes | 2019-06-21T13:01:04+00:00
I use this to automate wallet creation:
```
for i in {1..5}; do echo -e "test$i\nY\nwallet\nwallet\n1" | monero-wallet-cli; done && ls -l'
```
(Creates 5 wallets, called test1, test2, ..., password is wallet, seed is created in English)


The above does not take into account the action of confirming/declining the backgrond mining, but that's an easy fix.

The main part is `echo -e "test$i\nY\nwallet\nwallet\n1"` which _does_ the input.

By the way, I use the docker images provided by XMR.to - They are great.
https://hub.docker.com/r/xmrto/monero

## josef-v | 2019-06-21T13:14:16+00:00
That's the same as using `yes`. Don't take me wrong, it will work and I will use this if there's no other way. But I would expect that `--generate-from-json` would do all the work automatically in much cleaner way. Question is if someone just omitted this use case (and it shall be fixed) or if the `--generate-from-json` was never meant to be used this way.

Thanks for the dockerfiles, I'll take a look at them for inspiration. We do however prefer to use our own as they are much leaner (written just for our specific use cases).

## normoes | 2019-06-21T13:16:54+00:00
I reopened the issue as I can relate with your question.

What's your special use case? I like those Dockerfiles, because they are lean and easy to configure ;)
Do you prefer images only  for the CLI or the RPC e.g.?

## moneromooo-monero | 2019-06-21T13:46:18+00:00
It should be possible. I'll fix it.

## moneromooo-monero | 2019-06-21T13:48:53+00:00
Actually, on second thought, monero-wallet-cli should not really be used that way, as there is no guarantee input/output will not change. I'll still fix it, assuming it's not too hairy.

## moneromooo-monero | 2019-06-21T13:58:58+00:00
Does https://github.com/moneromooo-monero/bitmonero/commit/7ee4c123f02b32f5bee8908dbf81079a8f293e78 trigger in your case ? I assume you're using a command (eg, exit).

You can also generate new wallets via monero-wallet-rpc, and that'd be better.


## josef-v | 2019-06-21T14:55:59+00:00
> I assume you're using a command (eg, exit).

wallet-info :) It seems it should work, I am running the build right now and will let you know. I am just not sure if it's necessary because:

> You can also generate new wallets via monero-wallet-rpc, and that'd be better.

Sorry, I have totally missed this option. It works, I'll use this one.

## normoes | 2019-06-21T14:59:32+00:00
I missed it, too.
Good point!

## josef-v | 2019-06-21T15:00:32+00:00
@normoes 
> What's your special use case?

We usually do configuration by config files that are either on a mounted volume (outside of the docker container) or "baked" inside the image. The "baked-in" config files are usually used for testing configuration as it's really easy to just start a single docker-compose service with reasonably set defaults.
So no special use case, just little bit different one :)


## josef-v | 2019-06-21T15:25:40+00:00
> Does [moneromooo-monero@7ee4c12](https://github.com/moneromooo-monero/bitmonero/commit/7ee4c123f02b32f5bee8908dbf81079a8f293e78) trigger in your case ? I assume you're using a command (eg, exit).

It works. It's probably up to you to decide if this is the way to go. I can use monero-wallet-rpc with the same result.


## josef-v | 2019-06-21T15:31:41+00:00
Note: As I see, it is not possible to generate the wallet with monero-wallet-rpc without actually starting it with the newly generated wallet. 

## moneromooo-monero | 2019-06-21T15:39:28+00:00
I'm not sure exactly what you mean but the "normal" way is to start monero-wallet-rpc with -d, then use RPC like restore_deterministic_wallet or generate_from_keys.

## moneromooo-monero | 2019-06-22T10:51:29+00:00
https://github.com/monero-project/monero/pull/5685

## dmitry537 | 2019-07-10T12:58:43+00:00
> I'm not sure exactly what you mean but the "normal" way is to start monero-wallet-rpc with -d, then use RPC like restore_deterministic_wallet or generate_from_keys.

How i can use "restore_deterministic_wallet"? When i send 
```
{
	"jsonrpc": "2.0",
	"id": "0",
	"method": "restore_deterministic_wallet",
	"params": {
		"restore_height": 0,
		"filename": filename,
		"seed": seed,
		"seed_offset": offset,
		"password": password,
		"language": "English",
		"autosave_current": true
	}
}
```
I recieve 
```

{
  "error": {
    "code": -32601,
    "message": "Method not found"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```


## moneromooo-monero | 2019-07-10T14:03:52+00:00
That one worked for me:

```
{"jsonrpc":"2.0","id":"0","method":"restore_deterministic_wallet","params":{"filename":"test-new-wallet","password":"   ","language":"Français", "restore_height":0, "seed":"velvet lymph giddy number token physics poetry unquoted nibs useful sabotage limits benches lifestyle eden nitrogen anvil fewest avoid batch vials washin
g fences goat unquoted", "password":"foo", "seed_offset":"foo", "autosave_current":true}}
```

I did not use yours since it's a placeholder, so untestable.


## dmitry537 | 2019-07-11T10:05:01+00:00
Your example doesn't work either. What am I doing wrong?
![image](https://user-images.githubusercontent.com/23293525/61042160-54105580-a3dc-11e9-951c-7a42d021e983.png)
Version of my monero-wallet-rpc is `Monero 'Boron Butterfly' (v0.14.0.2-release)`


## selsta | 2019-07-11T10:26:28+00:00
Update to `v0.14.1.0`.

## moneromooo-monero | 2019-07-11T11:12:29+00:00
Are you actually asking a wallet ?

## moneromooo-monero | 2019-08-27T15:09:49+00:00
Is there anything still open here ?

## normoes | 2019-08-28T07:55:44+00:00
Not from my side. Thanks for taking care of this.

## moneromooo-monero | 2019-08-28T10:58:28+00:00
Thanks for confirming.

+invalid

# Action History
- Created by: normoes | 2019-06-17T07:14:44+00:00
- Closed at: 2019-08-28T11:09:46+00:00
