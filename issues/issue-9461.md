---
title: wallet2_api + smart pointers
source_url: https://github.com/monero-project/monero/issues/9461
author: vtnerd
assignees: []
labels:
- important
- proposal
- discussion
- wallet
created_at: '2024-08-27T22:54:15+00:00'
updated_at: '2025-12-03T16:47:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The [wallet2_api](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/wallet/api/wallet2_api.h) uses raw pointers in most situations. In some places, [memory leaks exist if an exception is thrown](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/wallet/api/transaction_history.cpp#L183). In other places, the [memory management isn't specified in the documentation](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/wallet/api/wallet2_api.h#L212) (in this situation, `refresh()` will delete all memory returned by `getAll()`).

So I would like to update everything to `std::unique_ptr` and `std::shared_ptr` - but this will break existing code. So my questions are:

  * Is the effort worth the temporary compilation breakage pain?
  * What downstream systems use `wallet2_api.h` (outside of the official GUI)?

# Discussion History
## 0xFFFC0000 | 2024-09-05T20:56:24+00:00
> Is the effort worth the temporary compilation breakage pain?

My vote is yes. IMHO it worth it to modernize that part of the code-base.



## SNeedlewoods | 2024-09-17T11:36:41+00:00
>What downstream systems use wallet2_api.h (outside of the official GUI)?

If things work out as proposed [here](https://github.com/seraphis-migration/wallet3/issues/64) (in step 2), the `wallet2_api.h` will also be used by the wallet-CLI and wallet-RPC.

## rbrunner7 | 2024-09-17T17:27:51+00:00
@vtnerd, can you elaborate a bit for people like me that don't know the subtleties of C++ memory management, and make a good example of such a memory leakage, how and why it occurs, and how the use of special pointers will prevent it?

## jeffro256 | 2024-09-17T17:44:01+00:00
@rbrunner7 if you allocate an object on the heap, for example using the `new` operator, this will return a pointer to that object on the heap. Let's say we have a class called `CoolObject`. To instantiate an instance of this class on the heap, we would write `CoolObject *myobj = new CoolObject();`. This causes the operating system to allocate memory for that object. If we wanted to free that memory, we would write `delete myobj;`, which calls the destructor of `myobj` and then frees the used memory. However, if for some reason we lose the reference to `myobj`, then that memory can never be released (until we exit the program), which is called a "memory leak". Smart pointers are a form of defensive programming that prevents this. The simplest of which is `std::unique_ptr`, which is simply a struct that holds a single pointer to an object and calls `delete ptr;` when the `std::unique_ptr` goes out of scope. This means that either 1) the object is still in scope or 2) it is deleted, without explicitly having to call a delete expression. This is true even when a C++ exception is thrown, as the unwinding process calls all destructors of objects in stack scope until it hits a `catch` block or exits the thread. 

## rbrunner7 | 2024-09-17T20:23:58+00:00
Thanks for that detailed explanation, @jeffro256. Of course I know that memory leaks are one of the biggest problems of C++ programs, but wasn't aware how easy they can occur. I am still a bit confused now why `delete myobj` is not part of the standard "object goes out of scope* mechanism, couldn't C++ have been built that way? Anyway, now it's too late of course.

I saw that `std::unique_ptr` is quite prevalent in the Monero codebase.

In the light of all this I think we should extend them and similar mechanisms to the Wallet API.

## jeffro256 | 2024-09-17T21:09:36+00:00
> I am still a bit confused now why delete myobj is not part of the standard "object goes out of scope* mechanism, couldn't C++ have been built that way?

During it's design, C++ needed to be backwards compatible with C, which has raw pointers as well. Also, for object-oriented programming, there needs to be a way to pass references to objects without respect to how they're allocated/stored, or even which exact class that are instantiated from (AKA polymorphism), of which pointers serve that purpose well. Languages like Java do the same thing, where objects are passed by "reference-by-value". However, the Java runtime has a garbage collector which prevents memory leaks, at the cost of CPU overhead to manage that garbage collector. The C++ standards committee is pretty anal about making language features "zero-cost abstractions" when it is possible. Even C++ "references" are basically just syntactic sugar on top of pointers, without any real reference counting. 

## vtnerd | 2024-09-20T23:33:35+00:00
@rbrunner7 to follow up on what @jeffro256 wrote, search for C++ RAII. You should find examples of both pointers and mutexes/locks of the RAII concept in action. FWIW Rust took some of the design concepts, and rolled them into their std. Unfortunately C++ has to support "legacy" code, so raw pointers are still considered valid.

## binarybaron | 2025-10-26T15:38:23+00:00
> * What downstream systems use `wallet2_api.h` (outside of the official GUI)?

We use `wallet2_api.h` for our Rust FFI crate ([monero-sys](https://github.com/eigenwallet/core/tree/master/monero-sys))

## sneurlax | 2025-12-03T16:32:06+00:00
> * What downstream systems use `wallet2_api.h` (outside of the official GUI)?

Similarly, Cake Wallet and Stack Wallet use wallet2_api* via monero_c: https://github.com/MrCyjaneK/monero_c

## binarybaron | 2025-12-03T16:42:35+00:00
> > * What downstream systems use `wallet2_api.h` (outside of the official GUI)?
> 
> Similarly, Cake Wallet and Stack Wallet use wallet2 via monero_c: https://github.com/MrCyjaneK/monero_c

I think @vtnerd was specifically asking about `wallet2_api` which is different from `wallet2` (the naming is getting a bit confusing)

## sneurlax | 2025-12-03T16:45:05+00:00
> I think [@vtnerd](https://github.com/vtnerd) was specifically asking about `wallet2_api` which is different from `wallet2` (the naming is getting a bit confusing)

and I misspoke--it uses wallet2_api specifically: https://github.com/MrCyjaneK/monero_c/blob/develop/monero_libwallet2_api_c/src/main/cpp/wallet2_api_c.cpp#L6C18-L8C29

# Action History
- Created by: vtnerd | 2024-08-27T22:54:15+00:00
