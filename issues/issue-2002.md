---
title: log file
source_url: https://github.com/xmrig/xmrig/issues/2002
author: Blisk
assignees: []
labels: []
created_at: '2020-12-24T09:40:54+00:00'
updated_at: '2021-04-12T14:26:44+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:26:44+00:00'
---

# Original Description
**Describe the bug**
How can I set logfile in this miner? And how can I set mining intension? 
Your readme have nothing about it.




# Discussion History
## Spudz76 | 2020-12-25T18:24:50+00:00
The readme clearly says go use the config generator wizard, so maybe [go use the generator](https://xmrig.com/wizard) to have a starting point

I'd bet the logfile location might be set with the `log-file` config option, but that's probably too obvious.  Better complain about not documenting it instead.  Nobody could ever figure that option out without docs for sure.  Oh wait `--help` has docs:
```
  -l, --log-file=FILE           log all output to a file
```
Protip: command line options roughly translate to the same config file entries, except when it's a backend option inside its own json sub-block and then you remove the backend name.  So the command line `--help` is actually also the docs for the config file, in a way.

Do you mean intensity?  Well once you've made a config.json with the wizard, and then run it once on your rig, it will autofill all the mining configurations, and then you quit and edit them if you don't like the automatic intensities.

## Blisk | 2020-12-25T18:52:26+00:00
thank you.
Intensity I don't want it to use max when I use my PC so I want to reduce it, when I use word or excell

# Action History
- Created by: Blisk | 2020-12-24T09:40:54+00:00
- Closed at: 2021-04-12T14:26:44+00:00
