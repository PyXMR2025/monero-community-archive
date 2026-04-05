---
title: unable to open config file
source_url: https://github.com/xmrig/xmrig/issues/2722
author: ratsclub
assignees: []
labels: []
created_at: '2021-11-26T17:08:49+00:00'
updated_at: '2021-11-26T21:30:30+00:00'
type: issue
status: closed
closed_at: '2021-11-26T20:02:36+00:00'
---

# Original Description
**Describe the bug**
When running `xmrig --config=config.json` I receive the error that it was unable to open the config file. Currently I'm trying to run it as a systemd service.

**To Reproduce**
1. Create a `config.json` file with the following content `{ "url": "127.0.0.1:3333" }`
2. Run `xmrig --config=config.json`

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 ```
victor@t495:/tmp/xmrig$ ls
config.json
victor@t495:/tmp/xmrig$ cat config.json 
{
  "url": "127.0.0.1:3333"
}
victor@t495:/tmp/xmrig$ xmrig --config=config.json
[2021-11-26 14:03:02.529] unable to open "/nix/store/zayvp5khqxlhyfjdz0dwn47fi0v70cvc-xmrig-6.15.0/bin/config.json".
[2021-11-26 14:03:02.529] unable to open "/home/victor/.xmrig.json".
[2021-11-26 14:03:02.529] unable to open "/home/victor/.config/xmrig.json".
[2021-11-26 14:03:02.529] no valid configuration found, try https://xmrig.com/wizard
```
 - Config file or command line (without wallets)
```json
{
  "url": "127.0.0.1:3333"
}
```
 - OS: NixOS




# Discussion History
## Spudz76 | 2021-11-26T19:26:13+00:00
Well it's not lying, that's not valid at all.

Try the minimal:
```
{ "pools": [ { "url": "127.0.0.1:3333" } ] }
```

## ratsclub | 2021-11-26T20:02:36+00:00
Oh, I thought that the `--url` parameter would map to a `url` attribute. Thank you!

## Spudz76 | 2021-11-26T20:46:36+00:00
Well, it does, but within the scope of the first entry (`[0]`) in the pools array... :)

Most options end up in a sub-object of some kind (`--cpu-whatever=foo` would usually map to `"cpu": { "whatever": "foo" }`)

But some are assumed like `--url` instead of `--pool-0-url` which would be redundant-ish and longer

There is a [sample/default config.json in the source tree here](https://github.com/xmrig/xmrig/blob/master/src/config.json) which is sort of a reference.

After launch it will write a more filled-out config.json than the minimal.  Also config.json wins over commandline so once you have all the options you have to edit config.json to change things (commandline ignored).  This is opposite every other everything. :)

## ratsclub | 2021-11-26T21:30:30+00:00
Thank you for the detailed response. Nice to know this!

# Action History
- Created by: ratsclub | 2021-11-26T17:08:49+00:00
- Closed at: 2021-11-26T20:02:36+00:00
