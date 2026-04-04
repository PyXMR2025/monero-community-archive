---
title: 'monerod: unrecognised option ''non-interactive'''
source_url: https://github.com/monero-project/monero/issues/8753
author: v-byte-cpu
assignees: []
labels: []
created_at: '2023-02-28T18:28:38+00:00'
updated_at: '2023-06-27T16:31:41+00:00'
type: issue
status: closed
closed_at: '2023-06-27T16:31:41+00:00'
---

# Original Description
Hi there! When I try to add `non-interactive=1` option to the monerod.conf file and start with `--config-file monerod.conf`, monerod crashes with the following error:
```
Exception in main! unrecognised option 'non-interactive'
```

However, when I run monerod with the `--non-interactive` command line flag directly, it starts successfully.

# Discussion History
## almalh | 2023-03-05T18:30:06+00:00
Will look into it, can you paste your .conf file here?

## almalh | 2023-03-05T19:13:36+00:00
Just had a look at the code and it is by design; only a subset of all possible options are allowed in the .conf file. In particular all daemonizer flags (incl. non-interactive) are designed to be kept in the command line. Someone else may chime in, but I don't think this should be changed.

## almalh | 2023-03-05T19:19:50+00:00
That being said, I can add something to better handle the error and make it clear that option belongs to the command line

## v-byte-cpu | 2023-03-06T13:33:41+00:00
Ok, the only question is why it was designed that way. I mean, what are the benefits of this restriction? 
Probably it was designed to set specific values at startup without changing config file, but in this case then it is better to make the cli flags have a higher priority than the flags in the configuration file

## almalh | 2023-03-06T14:26:28+00:00
I can only interpret the code that was written 8 years ago, but first, there are flags that do not belong in the config file by definition, like --help, --version, --os_version. Second, I can gather that this way the .conf files are ensured to be cross-platform, because the daemon has different flags on Windows and POSIX systems. This was implemented by very purposefully encapsulating the daemon process flags (incl. non-interactive) in posix_daemonizer.inl and windows_daemonizer.inl respectively with an anonymous namespace. Obviously the use case here is when people share their .conf files and have different OSs.

Now, non-interactive is encapsulated but also valid on both platforms. It could in theory be de-encapsulated, but I feel like that would violate the .conf file purpose as originally designed (i.e. a configuration for the Monero node core modules and not for how the process is executed by the OS), so I'm a bit wary. I'll leave this open for a little while see if others want to chime in.

## almalh | 2023-03-07T01:16:27+00:00
Honestly I took a careful look and there shouldn't be any issue allowing non-interactive in the config file, will get a PR going in the near term

## v-byte-cpu | 2023-03-07T18:07:10+00:00
This is great news, thanks!

# Action History
- Created by: v-byte-cpu | 2023-02-28T18:28:38+00:00
- Closed at: 2023-06-27T16:31:41+00:00
