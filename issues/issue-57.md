---
title: 'Build Fails: undefined reference to `boost::re_detail_106100'
source_url: https://github.com/monero-project/monero-gui/issues/57
author: hamiltino
assignees: []
labels: []
created_at: '2016-10-12T10:25:11+00:00'
updated_at: '2016-11-13T17:59:45+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:59:45+00:00'
---

# Original Description
Hi,
I can't get monero core built on my system (debian sid) i get the following error on make:

```
` undefined reference to `boost::re_detail_106100::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
<artificial>:(.text+0x368d): undefined reference to `boost::re_detail_106100::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
collect2: error: ld returned 1 exit status
Makefile:187: recipe for target 'release/bin/monero-core' failed
make: *** [release/bin/monero-core] Error 1
```

`

What needs to be done to get it working? I'm using libboost-all-dev (1.61.0.2) libboost-regex-dev (1.61.0.2)


# Discussion History
## medusadigital | 2016-11-01T08:17:03+00:00
is this still an issue? did you try libboost1.58 ? 


## ghost | 2016-11-03T06:54:26+00:00
On OSX, I had a similar error with `boost` 1.62. I downgraded to 1.59, and now it works. See #101. I don't know if this is the same problem.


## fluffypony | 2016-11-13T17:59:45+00:00
Closing as fixed


# Action History
- Created by: hamiltino | 2016-10-12T10:25:11+00:00
- Closed at: 2016-11-13T17:59:45+00:00
