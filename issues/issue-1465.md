---
title: Error when compiling on Ubuntu 14.04
source_url: https://github.com/monero-project/monero/issues/1465
author: Onefox
assignees: []
labels: []
created_at: '2016-12-16T23:44:07+00:00'
updated_at: '2017-08-07T17:24:14+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:24:14+00:00'
---

# Original Description
I needed to build boost 1.58 from source first but after that i still get an error while building the source:

`Scanning dependencies of target epee
make[3]: Leaving directory `/home/bitmonerod/monero/build/release'
make[3]: Entering directory `/home/bitmonerod/monero/build/release'
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
/home/bitmonerod/monero/contrib/epee/src/http_auth.cpp: In constructor ‘epee::net_utils::http::http_auth::http_auth(epee::net_utils::http::http_auth::login)’:
/home/bitmonerod/monero/contrib/epee/src/http_auth.cpp:485:46: error: no matching function for call to ‘epee::net_utils::http::http_auth::session::session(<brace-enclosed initializer list>)’
         : user(session{std::move(credentials)}) {
`

Here is the full log:
http://pastebin.com/5iaHQnfm
Is there any dependence i missed?

# Discussion History
## moneroexamples | 2016-12-17T00:14:12+00:00
On Fedora 25 there are also compilation problems. From what I recall they are related to tests, assuming they are same problems. You can try building without the tests `make release`. It helps on F25.

## ghost | 2016-12-17T03:11:01+00:00
Also perhaps run a `make clean` beforehand

## Onefox | 2016-12-17T09:33:47+00:00
make clean and than make release results in the same error.

## moneroexamples | 2016-12-19T22:22:45+00:00
I chacked again on Fedora 25, and it compiles properly now. The ubuntu 16.04/10 and Fedora 25 dependencies that I use are listed here: 

https://github.com/moneroexamples/compile-monero-09-on-ubuntu-16-04

Maybe you are missing some dependencies? 

## ghost | 2016-12-19T23:09:21+00:00
@moneroexamples this is great - would you consider submitting your README as a PR to the main repo?

## moneroexamples | 2016-12-20T01:41:43+00:00
@NanoAkron 

I think its better to keep it separate. The reason is that I make this to match monero projects at https://github.com/moneroexamples?tab=repositories and this guide changes in response to them, and not only to monero itself. 

## ghost | 2016-12-21T17:53:57+00:00
@moneroexamples Would you consider maybe submitting that link to the README?

## moneromooo-monero | 2017-08-07T17:19:58+00:00
+resolved

# Action History
- Created by: Onefox | 2016-12-16T23:44:07+00:00
- Closed at: 2017-08-07T17:24:14+00:00
