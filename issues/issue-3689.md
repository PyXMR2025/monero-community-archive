---
title: Command line options should override config
source_url: https://github.com/xmrig/xmrig/issues/3689
author: Agarmal
assignees: []
labels:
- wontfix
created_at: '2025-07-28T10:09:42+00:00'
updated_at: '2025-07-28T12:51:24+00:00'
type: issue
status: closed
closed_at: '2025-07-28T12:51:24+00:00'
---

# Original Description
I've been trying to make a wrapper for XMRig that sets the pass value dynamically based on the machine-id in Arch Linux. I tried using the -p flag (or --pass), but it will instead use the one defined in config.json.

This doesn't make any sense, because if I explicitly pass an option to the command, I'd expect it to override the default configuration instead of just ignoring it.

# Discussion History
## SChernykh | 2025-07-28T10:27:31+00:00
XMRig's config.json takes priority. It is how it is.

## Agarmal | 2025-07-28T10:28:51+00:00
> XMRig's config.json takes priority. It is how it is.

That doesn't make any sense, as I already said.

## SChernykh | 2025-07-28T10:40:30+00:00
I'm left-handed and everything around me made for right-handed people doesn't make sense too, but it is how it is. XMRig takes config.json as a priority.

## SChernykh | 2025-07-28T10:41:22+00:00
Either don't use config.json at all, or modify the password inside it for your machines.

## Agarmal | 2025-07-28T10:47:11+00:00
> I'm left-handed and everything around me made for right-handed people doesn't make sense too, but it is how it is. XMRig takes config.json as a priority.

Everything is made for right-handed people because that's the majority of population. It has nothing to do with XMRig's command line options actually being useful or not.

## Agarmal | 2025-07-28T10:48:13+00:00
Anyway, I'm just going to make a script to modify the password automatically. I still think command line options should take priority.

## xmrig | 2025-07-28T12:43:57+00:00
Yes, the most common and intuitive approach is that the command line takes priority; however, this is not how it is implemented. Mixing command-line with complex configuration is error-prone, even with the correct priority.
So you should use the command line or a config file, not both, unless you know exactly what you are doing. For example, what exactly `--pass` should override if multiple pools are specified? Or the config file is reloaded from disk or from the API when the override should stop.

If you prefer to stay with the config file, you can use https://xmrig.com/docs/miner/environment-variables in the config file.
Thank you.

## Agarmal | 2025-07-28T12:51:24+00:00
> Yes, the most common and intuitive approach is that the command line takes priority; however, this is not how it is implemented. Mixing command-line with complex configuration is error-prone, even with the correct priority. So you should use the command line or a config file, not both, unless you know exactly what you are doing. For example, what exactly `--pass` should override if multiple pools are specified? Or the config file is reloaded from disk or from the API when the override should stop.
>
> If you prefer to stay with the config file, you can use https://xmrig.com/docs/miner/environment-variables in the config file. Thank you.

Alright, thanks.

# Action History
- Created by: Agarmal | 2025-07-28T10:09:42+00:00
- Closed at: 2025-07-28T12:51:24+00:00
