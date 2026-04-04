---
title: tutorial for the commandline tools ?
source_url: https://github.com/monero-project/monero/issues/985
author: eriksank
assignees: []
labels:
- invalid
created_at: '2016-08-24T07:40:28+00:00'
updated_at: '2017-09-20T21:30:27+00:00'
type: issue
status: closed
closed_at: '2017-09-20T21:30:27+00:00'
---

# Original Description
I have downloaded the binaries, and now I am staring at this:

```
$ ls
bitmonerod  blockchain_converter  blockchain_dump
blockchain_export  blockchain_import
cn_deserialize  simpleminer  simplewallet
```

The help seems to function. So, something like this certainly works:

```
$ ./simplewallet --help | more
Creating the logger system
Monero 'Hydrogen Helix' (v0.9.4.0-release)
Usage: simplewallet [--wallet-file=<file>|--generate-new-wallet=<file>]
[--daemon-address=<host>:<port>] [<COMMAND>]

General options:
  --help                                Produce help message
  --version                             Output version information

Wallet options:
  --wallet-file arg                     Use wallet <arg>
...
```

Is there anybody who has published a few simple use-case scenarios? _Do this, do that, and then you see that as a result._

I saw this:

[simplewallet-commands](https://github.com/monero-project/bitmonero/wiki/simplewallet-commands)

but it is relatively poor and not much elaborated. I was looking for something that looks more like this:

[https://github.com/libbitcoin/libbitcoin-explorer/wiki](https://github.com/libbitcoin/libbitcoin-explorer/wiki)

Is there anything around like that?


# Discussion History
## moneromooo-monero | 2016-08-25T07:32:29+00:00
https://getmonero.org/knowledge-base/user-guides/simplewallet


## eriksank | 2016-08-26T05:04:00+00:00
Thanks for the link. First problem I ran into. I started both the `simplewallet` and the `bitmonerod` daemon in testnet:

```
terminal 1:
$ ./bitmonerod --testnet --offline

terminal 2:
$ echo balance | ./simplewallet --wallet-file test2 --testnet --password ""
Creating the logger system
Monero 'Hydrogen Helix' (v0.9.4.0-release)
Logging at log level 0 to /home/ontop/Desktop/monero/./simplewallet.log
Opened wallet: 9vS9V6UFwmvWCbBKFZ4LShUXxTAF96M7cKh2mQu4gpvCB1
UmzerijC43LkDgCYu8CchTzHcjhZRLQeHYjHVHPtLTQVmgjPA
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
[wallet 9vS9V6]: Balance: 0.000000000000, unlocked balance: 0.000000000000
[wallet 9vS9V6]: $ 
```

What I would obviously need now, is a way to generate test coins in the daemon (just like you can do with `bitcoin-cli`). I could not find the command to do that.

Second problem. `simplewallet` is a bit of a strange tool:

```
$ echo "integrated_address AAAAAAA" | ./simplewallet --wallet-file test2 --testnet --password ""
Creating the logger system
Monero 'Hydrogen Helix' (v0.9.4.0-release)
Logging at log level 0 to /home/ontop/Desktop/monero/./simplewallet.log
Opened wallet: 9vS9V6UFwmvWCbBKFZ4LShUXxTAF96M7cKh2m
Qu4gpvCB1UmzerijC43LkDgCYu8CchTzHcjhZRLQeHYjHVHPtLTQVmgjPA
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
[wallet 9vS9V6]: Error: failed to parse payment ID or address
```

You cannot really use it as real `cli` tool like `bitcoin-cli` and call it from other scripts. There is no other way to make it execute commands than by supplying them on `stdin`, but it will also not correctly parse commands supplied on `stdin`. 

It also produces lots of useless output on `stdout` which any other `cli` program would just output on `stderr`. 

At the same time, as a `cli` terminal program is also not meant to be an end user tool. However, in order to create a front-end GUI, `simplewallet` would need to be programmable by external scripts, but it isn't. Hence, it also actively prevents creating a GUI.

In other words, unlike `bitcoin-cli`, `simplewallet` really has no particular fitness for purpose and utterly misses the point.

Interactive `cli` programs that arbitrarily wait for user input, defeat the object. We cannot use them for scripting. We can also not use them as a backend for constructing a GUI. They are fundamentally useless. It is not particularly hard to avoid this problem -- since it is even easier not to add interactivity to a cli program -- but unfortunately, it is a widespread and very common mistake.

In my impression, the current incarnation of `simplewallet` is unusable. Building your own `cli` client, however, would require figuring out the communications protocol between `simplewallet` and `bitmonerod`. That is even more of an effort, especially, because that protocol does not seem to be that much documented anywhere. There is also no client library available with a documented API for it.

I am not sure about this, but in my impression, monero was more or less lifted from the `CryptoNote` reference implementation, which is the original source for these issues. There may be no point in raising any of these issues there either. In my experience, developers who create that kind of issues generally also refuse to listen to anybody complaining about them. I somehow suspect that the `simplewallet` developer is most likely also completely convinced that `simplewallet` should be built in that way, and will probably never listen to anybody saying otherwise. Hence, the problem could easily linger for years in a row before getting addressed, if it gets addressed ever.

But then again, if they do not make their project usable for other developers to integrate into their own projects as a supported payment method, their project will never take off either. My personal take on the issue is that Monero could perfectly-well be condemned to failure.

With `bitcoin` being imperfect in terms of privacy but still eminently usable in terms of building it in as a standard payment method,  and with monero's `simplewallet` being useless for any practical purpose, and with alternative ways to support monero as a payment method being too elaborate, I will recommend to my client not to support it at this point, but rather to wait and see if anything ever improves, which I doubt, but you'd never know. ;-)


## moneromooo-monero | 2016-08-26T08:31:34+00:00
To mine: start_mining 1

And simplewallet isn't unusable, you're just using it wrong and jumping to conclusions :D 

Anyway, please don't use github for requests for help. Use either Freenode IRC (#monero) or reddit.


## moneromooo-monero | 2016-08-28T09:56:34+00:00
That said, having a simple layer that outputs unadorned data to help with scripting could be a good thing to have. simplewallet just doesn't try to be that. It is unclear whether a simplewallet change or a new simpler tool that proxies RPC would be better suited for this.


## eriksank | 2016-08-29T03:26:42+00:00
> simplewallet just doesn't try to be that

Yes, agreed. I have to remark, however, that there is no valid use case for what `simplewallet` tries to be instead. Of course, everybody is entirely allowed to make programs that are essentially useless. There is in-and-of-itself nothing wrong with that. It could indeed be someone's legitimate hobby.

> It is unclear whether a simplewallet change or a new simpler tool that proxies RPC would be better suited for this.

Well, there is still a real need -- for real-world use cases -- for a simplewallet-style program that is actually scriptable. Someone else will now painstakingly have to produce a program that is essentially the same as `simplewallet` with a few differences in the details, that would make it usable. An actually usable alternative is not that much different from the existing `simplewallet` program. It would just have to obey a few simple rules:
- No Turing-style halting problem. The program accepts all arguments at the very start, always terminates, and never (unexpectedly) waits for user input. 
- The program limits its outputs to `stdout` to only desired results. All remarks, warnings, and error messages must be produced on `stderr` only.
- The program returns with result code 0, if the request was processed successfully, and with a non-zero result code if it failed, it being clearly understood that the associated error message will be available on `stderr`.

The rules to obey, are not particularly hard. The vast majority of cli programs can be, and are, written like that. A `simplewallet` for monero can certainly be written like that. 

The question is now: Would the original CryptoNote programmer agree to fix these issues in his program or should someone else just produce a replacement at the monero level? It is obvious, however, that every CryptoNote-derived currency will end up sitting on the same issue ...

So, do we solve the problem by software engineering or by social engineering? ;-)


## moneromooo-monero | 2016-09-01T19:07:48+00:00
I might be missing your point, but there is a use case for simplewallet as it is: using monero interactively.

Most of the wallet logic is in wallet2 fwiw, not simplewallet.


## eriksank | 2016-09-02T03:26:56+00:00
I think that monero is a good idea. The CryptoNote initiative is certainly very worthwhile. Unfortunately, _in the real world_ we also have do deal with all kinds of unexpected practicalities:

```
$ ls 
bitmonerod  blockchain_converter  blockchain_dump
blockchain_export  blockchain_import  cn_deserialize
simpleminer  simplewallet
```

I had only detected the `simplewallet` program in the monero package. Where can I find `wallet2`?

I am kind of interested in exploring what it would take to run a market that works with monero instead of bitcoin. Or what it would take to build an exchange platform that does XMR/USD. Then, there is also the issue of using monero as a payment method in e-commerce. There are lots of situations in which monero's privacy would be at a premium. Therefore, it should make sense for everybody involved. It's just that taking it from here, is a daunting task. With `simplewallet` a bit crippled, it is not a good starting point. So, I should indeed be looking for another starting point! ;-)


## moneromooo-monero | 2016-09-02T12:24:37+00:00
wallet2 is not a standalone program, but the main wallet logic code, which simplewallet uses. My intent was to elaborate on why I said it was not clear whether simplewallet or another program would be best as a scriptable output tool (and, to be even clearer, such a hypothetical new tool would be mostly a simple shell around the wallet2 library code).


## eriksank | 2016-09-02T12:55:25+00:00
In fact, simplewallet itself would be an excellent scriptable tool if it were not interactive.

Creating an interactive program on top of a non-interactive one is trivial. Creating a non-interactive program on top of an interactive one is insanely bug-prone. You can use a tool like `expect` to do that, but it is a nightmare. Utterly unreliable too.

To external scripters, the internal wallet2 code is not necessarily interesting in and of itself. If simplewallet just respected the functional model of scripting, it would be exactly what is needed:

```
f [stdin,env,args] = [resultcode,stdout,sderr]
```

From there on, it would be trivial for any scripter to create an interactive version of it. You would not even need to provide it, because anybody could create one in his favourite scripting language in no time. The same holds true for someone who wants a desktop GUI. It would be pretty much as easy to do. Just use something like nodewebkit or so. Or for someone who wants a web interface.

A non-interactive cli program is several orders of magnitude easier to integrate than a library. For a library, you first need to create bindings, test those bindings, fight with your binding tool, and so on. You would need to go to war with swig.org or similar, and hope that you will end up with usable bindings. That is why, for example, lots of scripters prefer integrating git to libgit.

Internally, the program could indeed still be a dependency hell, but then everybody still prefers the entire thing to be packed inside one binary file, instead of potentially dealing with files that need to go into lots of different places ...


## radfish | 2016-09-02T23:38:45+00:00
Adding a `-c <command>` to simplewallet to enable non-interactive usage might be useful and is harmless. Your PR of this feature is likely to be accepted.

PS. Writing interactive tools by wrapping non-interactive processes is an extremely inefficient, limited, brittle, and strange approach when a library is available.


## eriksank | 2016-09-03T02:12:54+00:00
> Adding a -c <command> to simplewallet to enable non-interactive usage might be useful and is harmless. Your PR of this feature is likely to be accepted.

Sounds good! Do we have any other steps to make for this?

> PS. Writing interactive tools by wrapping non-interactive processes is an extremely inefficient, limited, brittle, and strange approach when a library is available.

Well, the unix philosophy is is about small, little `programs` collaborating with each other, not about small, little `libraries` doing that. It is only brittle if you don't follow the rules. For example, it should also be possible to parse your program output correctly. If needed, provide a `-json` flag to transmit complex data.

Since you can transparently execute a program on a different machine, while you cannot do that with a library function, I really don't know if program chaining is more limited than function chaining. It also automatically enlists all available CPUs. Docker (linux process groups, aka microservices) is also about collaborating programs and not collaborating libraries.

A library is certainly ok for a memory-based data structure with associated functions, such as the implementation of a hashtable or arraylist or something like that. Otherwise, you are usually better off to output the results of your programs as soon as possible, and terminate the process, if only, because it will recover all process memory in that way.

Libraries are also much weaker at error handling than programs. If something went wrong, return a non-zero result code and dump the error message on stderr. Otherwise, produce the output desired on stdout. Libraries have much more trouble to do that.

How would you otherwise organize something like the communications between a web browser and a web server, since they usually run on two different machines? It will always be two programs and not two libraries ...


## jonathancross | 2017-09-19T22:15:15+00:00
Anyone else feel this issue should be closed?

## moneromooo-monero | 2017-09-20T10:07:01+00:00
It's kind of a mix of different things, but some of the things (like having a scriptable tool, or better HOWTOs, or even a man page) would be nice.

## jonathancross | 2017-09-20T14:10:06+00:00
I agree there is a lot we can do to make monero more usable and improve documentation, I just feel this particular issue has become a bit of a hodgepodge.

> You cannot really use it as real cli tool like bitcoin-cli and call it from other scripts.

We now have `monero-wallet-cli --command` which allows for passing commands from an external script.  Not sure if that is exactly what was requested, but it seems to work well for me.

I'd suggest we create a new feature request which is simply "Add monero 'man' (manual) pages".

HOWTOs might be better suited for websites, wikis, video tutorials, forum, etc.  We can try to consolidate better on getmonero.org , then add a link somewhere in the man page or in the GUI help, etc. man page could also have basic examples.  We can add a new feature request for this as well.

How does that sound?

## moneromooo-monero | 2017-09-20T21:15:39+00:00
Yeah, fair enough.

+invalid

# Action History
- Created by: eriksank | 2016-08-24T07:40:28+00:00
- Closed at: 2017-09-20T21:30:27+00:00
