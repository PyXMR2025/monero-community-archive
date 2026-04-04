---
title: Undefined symbols for architecture x86_64
source_url: https://github.com/monero-project/monero/issues/3215
author: cryptobender69
assignees: []
labels: []
created_at: '2018-01-31T03:14:34+00:00'
updated_at: '2018-02-01T18:51:05+00:00'
type: issue
status: closed
closed_at: '2018-02-01T18:51:05+00:00'
---

# Original Description
Hello, I am trying to build monero-gui v0.11.1.0 branch and I get this error on Mac OSX 10.12.6.

I get this error after bunch of these warnings:
**ld: warning: object file (/Users/Username/Downloads/Project/monero-gui/monero/lib/libunbound.a(view.c.o)) was built for newer OSX version (10.12) than being linked (10.10**

``
Undefined symbols for architecture x86_64:
  "_rl_replace_line", referenced from:
      rdln::suspend_readline::suspend_readline() in libepee.a(readline_buffer.cpp.o)
      rdln::readline_buffer::stop() in libepee.a(readline_buffer.cpp.o)
      rdln::suspend_readline::suspend_readline() in libepee.a(readline_buffer.cpp.o)
  "_rl_restore_prompt", referenced from:
      rdln::readline_buffer::sync() in libepee.a(readline_buffer.cpp.o)
  "_rl_save_prompt", referenced from:
      rdln::readline_buffer::sync() in libepee.a(readline_buffer.cpp.o)
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [release/bin/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui] Error 1
``



# Discussion History
## moneromooo-monero | 2018-01-31T08:34:46+00:00
Looks like you need a make clean ?

## cryptobender69 | 2018-02-01T16:01:22+00:00
Thanks. Well I guess the issue was mac's readline library which the build found in /opt/local. 

rm -Rf'ed the F out of all the libreadline dylib and it compiled without any issue. 

Don't know if there is a better way to deal with this issue. But this worked and that matters.  If ther is a better way, please put it in this ticket. Otherwise this is good to be closed.

Thanks!

# Action History
- Created by: cryptobender69 | 2018-01-31T03:14:34+00:00
- Closed at: 2018-02-01T18:51:05+00:00
