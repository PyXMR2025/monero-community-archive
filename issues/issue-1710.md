---
title: Logger [net.cn] is not registered yet
source_url: https://github.com/monero-project/monero/issues/1710
author: ghost
assignees: []
labels: []
created_at: '2017-02-12T10:05:12+00:00'
updated_at: '2017-02-24T06:06:16+00:00'
type: issue
status: closed
closed_at: '2017-02-24T06:06:16+00:00'
---

# Original Description
Interesting duplicated message with latest master + some extra PRs. Ubuntu 16.04, ARMv8, GCC 5.4.1.

```
nodey@odroidc2:~$ monerod status
2017-02-12 09:59:29,480 DEBUG [default] [nodey@unknown-host] [void command_line::add_arg(boost::program_options::options_description&, const command_line::arg_descriptor<T, required>&, bool) [with T = std::__cxx11::basic_string<char>; bool required = false]] [/home/nodey/monero/src/common/command_line.h:120] Logger [net.cn] is not registered yet!
2017-02-12 09:59:29,480 DEBUG [default] [nodey@unknown-host] [void command_line::add_arg(boost::program_options::options_description&, const command_line::arg_descriptor<T, required>&, bool) [with T = std::__cxx11::basic_string<char>; bool required = false]] [/home/nodey/monero/src/common/command_line.h:120] Logger [net.cn] is not registered yet!
Height: 1244398/1244398 (100.0%) on mainnet, not mining, net hash 56.19 MH/s, v4, up to date, 65(out)+13(in) connections, uptime 0d 9h 20m 23s


```

# Discussion History
## ghost | 2017-02-12T13:03:51+00:00
Hold this thought - appears to be a result of merging either #1703  or #1709 on top of master (`cb54eea`). Investigating.

Edit: Not #1709

## ghost | 2017-02-12T16:41:58+00:00
Looks like it's #1703 

# Action History
- Created by: ghost | 2017-02-12T10:05:12+00:00
- Closed at: 2017-02-24T06:06:16+00:00
