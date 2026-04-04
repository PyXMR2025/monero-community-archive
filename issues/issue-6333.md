---
title: Input error when confirming transaction
source_url: https://github.com/monero-project/monero/issues/6333
author: vdo
assignees: []
labels: []
created_at: '2020-02-11T18:20:10+00:00'
updated_at: '2022-09-06T19:16:57+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:01:16+00:00'
---

# Original Description
I'm experiencing a bug, it seems related with readline.
I can enter commands normally, but when I'm about to confirm the transaction, when I press Enter, it inputs "^M" instead, so I'm locked and I can only exit with Ctrl+C (and I get a segmentation fault):

```
Background refresh thread started
[wallet 4... ]: transfer 8....V 1
Wallet password: 

Transaction 1/1:
Spending from address index 0
Sending 1.000000000000.  The transaction fee is 0.000022220000
Is this okay?  (Y/Yes/N/No): Y^M^M^M^M^M^M^Czsh: segmentation fault (core dumped)  monero-wallet-cli --daemon-host node.xmr.to --wallet-file foobar

```
Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
Operating system is Manjaro (ArchLinux)
Terminal: Lilyterm

```
 stty -a
speed 38400 baud; rows 56; columns 190; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = <undef>; eol2 = <undef>; swtch = <undef>; start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V; discard = ^O;
min = 1; time = 0;
-parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
-ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl ixon -ixoff -iuclc -ixany -imaxbel iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke -flusho -extproc
```



# Discussion History
## vdo | 2020-02-11T18:25:40+00:00
I tried with another terminal (alacritty) and the bug is not reproducible anymore.

## moneromooo-monero | 2020-02-11T19:56:21+00:00
Do you have a strack trace for that crash ?

## moneromooo-monero | 2020-05-16T16:01:16+00:00
I don't get a a crash when ^C on that prompt. Reopen if you can supply a stack trace.

## vdo | 2022-09-06T18:52:57+00:00
I'm having this issue again, this time with alacritty.


This is the coredump I could get:

```
(gdb) bt
#0  0x00007ffff7d9de2c in read () from /usr/lib/libc.so.6
#1  0x00007ffff7d264e6 in _IO_file_underflow () from /usr/lib/libc.so.6
#2  0x00007ffff7d27516 in _IO_default_uflow () from /usr/lib/libc.so.6
#3  0x00007ffff7d21f30 in getc () from /usr/lib/libc.so.6
#4  0x000055555622bc7d in __gnu_cxx::stdio_sync_filebuf<char, std::char_traits<char> >::underflow() ()
#5  0x000055555619c379 in std::basic_istream<char, std::char_traits<char> >& std::getline<char, std::char_traits<char>, std::allocator<char> >(std::basic_istream<char, std::char_traits<char> >&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, char) ()
#6  0x00005555555af6c3 in (anonymous namespace)::input_line(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) ()
#7  0x000055555561705b in cryptonote::simple_wallet::transfer_main(int, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, bool) ()
#8  0x0000555555618b63 in cryptonote::simple_wallet::transfer(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) ()
#9  0x00005555555bbd03 in cryptonote::simple_wallet::on_command(bool (cryptonote::simple_wallet::*)(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&), std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) ()
#10 0x0000555555637ce3 in epee::command_handler::process_command_vec(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) ()
#11 0x00005555556589dd in epee::command_handler::process_command_str(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&) ()
#12 0x0000555555639501 in bool epee::async_console_handler::run<epee::async_console_handler::run<std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)> >(std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)>, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::async_console_handler::run<std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)> >(std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)>, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)#1} const&, std::function<void ()>) ()
#13 0x00005555555f3bf9 in cryptonote::simple_wallet::run() ()
#14 0x0000555555594756 in main ()
(gdb)
```

## selsta | 2022-09-06T18:55:09+00:00
What is the output of `echo $TERM` ?

## vdo | 2022-09-06T18:57:17+00:00
```
[vdo@spectre crypta]$ echo $TERM
xterm-256color
```

## selsta | 2022-09-06T18:57:57+00:00
which OS are you using? Also which alacritty version?

## vdo | 2022-09-06T18:59:53+00:00
I'm using Manjaro Linux.

I could workaround the issue using another terminal,  xfce4-terminal, and it has the same $TERM.

alacritty is version 0.10.1 

## selsta | 2022-09-06T19:06:30+00:00
Are these the binaries from getmonero.org?

alacritty 0.10.1 seems to work for me on macOS but I didn't test on Linux.

## vdo | 2022-09-06T19:16:57+00:00
Yes, I downloaded them from getmonero.org (and checked signatures).
This issue does not happen in another machine, running Void Linux, with alacritty 0.10.1 and zsh. Weird.

Related: https://github.com/monero-project/monero/issues/7211

# Action History
- Created by: vdo | 2020-02-11T18:20:10+00:00
- Closed at: 2020-05-16T16:01:16+00:00
