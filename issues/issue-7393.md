---
title: Calling /out_peers or /in_peers with out of bounds integer triggers HTTP 404
  Error
source_url: https://github.com/monero-project/monero/issues/7393
author: jeffro256
assignees: []
labels: []
created_at: '2021-02-21T00:57:21+00:00'
updated_at: '2023-10-25T22:14:29+00:00'
type: issue
status: closed
closed_at: '2023-10-25T22:14:29+00:00'
---

# Original Description
## Steps to reproduce:
1) Execute the /out_peers RPC Command with POST data of `{"out_peers": n}` or
2) Execute the /in_peers RPC Command with POST data of `{"in_peers": n}`

Where n < 0 or n > 4294967295.

## Expected behavior:
I would expect JSON returned with a descriptive `status` element or some other RPC error.

## Actual behavior:
The node returns with HTTP 404 "Not Found" status.

## Notes:
I think a 404 status is the wrong action for the node to take in this instance, especially since this behavior also occurs when the node is in restricted RPC mode. Maybe JSON could be returned with `status` set to "bad params" or something similar. I know calling these commands with numbers that are not unsigned 32-bit integers is undefined behavior, but the node could do more to provide more descriptive feedback.

In my opinion, I also think it would be beneficial to add the option for the user to supply -1 as the peers argument to set the number to unlimited. It is much more concise and straight-forwardl than 4294967295.

# Discussion History
## moneromooo-monero | 2021-02-23T18:55:46+00:00
https://github.com/monero-project/monero/pull/7399

## jeffro256 | 2021-02-27T10:27:21+00:00
Would you mind helping me out? I'm trying to test the changes, but I can't seem to get a different result than from the old code. I cloned your bitmonero repo, checked out branch h400, ran make, and ran the newly built monerod, but I still get a HTTP 404 Error.

## moneromooo-monero | 2021-02-27T13:38:11+00:00
Are you sure you're running the right binary ? If you checked out branch h400, the binary is possibly in a different path than you're used to, something like build/Linux/h400/release.

## jeffro256 | 2021-02-28T02:28:22+00:00
I ran the commands:

    git clone https://github.com/moneromooo-monero/bitmonero.git h400
    cd h400
    git checkout h400
    git submodule update --init --force
    make -j8
    ./build/Linux/h400/release/bin/monerod --detach
    sleep 60
    curl http://127.0.0.1:18081/in_peers -d '{"in_peers": -1}' -H 'Content-Type: application/json' -d out.txt
    cat out.txt

And got the output:

    HTTP/1.1 404 Not found
    Server: Epee-based
    Content-Length: 0
    Content-Type: text/plain
    Last-Modified: Sat, 27 Feb 2021 20:43:56 GMT
    Accept-Ranges: bytes


## moneromooo-monero | 2021-02-28T15:14:01+00:00
Sure you don't have another already running ?

## jeffro256 | 2021-02-28T19:38:26+00:00
I'm 95% sure I didn't. Just be be clear, the repo is at [https://github.com/moneromooo-monero/bitmonero.git](https://github.com/moneromooo-monero/bitmonero.git) correct?

## moneromooo-monero | 2021-02-28T22:25:47+00:00
That's mine yes.


## moneromooo-monero | 2021-03-01T16:21:51+00:00
Just to make sure, do you still get 404 with this ?

curl -v http://127.0.0.1:18081/in_peers -d '{"in_peers": -1}' -H 'Content-Type: application/json'

The -d out.txt seems fishy to me, but I assume you have a different curl patchset.


## jeffro256 | 2021-03-01T20:23:50+00:00
The `-d` option for me dumps the response headers to a file. This is the output of the command you provided:

    *   Trying 127.0.0.1:18081...
    * TCP_NODELAY set
    * Connected to 127.0.0.1 (127.0.0.1) port 18081 (#0)
    > POST /in_peers HTTP/1.1
    > Host: 127.0.0.1:18081
    > User-Agent: curl/7.68.0
    > Accept: */*
    > Content-Type: application/json
    > Content-Length: 16
    > 
    * upload completely sent off: 16 out of 16 bytes
    * Mark bundle as not supporting multiuse
    < HTTP/1.1 404 Not found
    < Server: Epee-based
    < Content-Length: 0
    < Content-Type: text/plain
    < Last-Modified: Mon, 01 Mar 2021 20:21:47 GMT
    < Accept-Ranges: bytes
    < 
    * Connection #0 to host 127.0.0.1 left intact

Does that curl command give you a HTTP 400 Error for your build? I have double-checked that I was running the code from  #7399.

## moneromooo-monero | 2021-03-02T00:06:11+00:00
It does...

## moneromooo-monero | 2021-03-02T00:26:16+00:00
Can you set_log 3 in monerod before curl, and post the resulting logs ?

## jeffro256 | 2021-03-03T16:34:42+00:00

[bitmonero.log](https://github.com/monero-project/monero/files/6077535/bitmonero.log) Here it is


## moneromooo-monero | 2021-03-05T13:26:24+00:00
Can you apply this *on top* of the PR, and post logs again ? Might as well make it log level 4 this time, in case something jumps out there.

```
diff --git a/contrib/epee/include/net/http_server_handlers_map2.h b/contrib/epee/include/net/http_server_handlers_map2.h
index ffb3f3b7e..587582894 100644
--- a/contrib/epee/include/net/http_server_handlers_map2.h
+++ b/contrib/epee/include/net/http_server_handlers_map2.h
@@ -74,6 +74,7 @@
       uint64_t ticks = misc_utils::get_tick_count(); \
       boost::value_initialized<command_type::request> req; \
       bool parse_res = epee::serialization::load_t_from_json(static_cast<command_type::request&>(req), query_info.m_body); \
+MGINFO("load_t_from_json (1): " << parse_res); \
       if (!parse_res) \
       { \
          MERROR("Failed to parse json: \r\n" << query_info.m_body); \
@@ -110,6 +111,7 @@
       uint64_t ticks = misc_utils::get_tick_count(); \
       boost::value_initialized<command_type::request> req; \
       bool parse_res = epee::serialization::load_t_from_binary(static_cast<command_type::request&>(req), epee::strspan<uint8_t>(query_info.m_body)); \
+MGINFO("load_t_from_json (2): " << parse_res); \
       if (!parse_res) \
       { \
          MERROR("Failed to parse bin body data, body size=" << query_info.m_body.size()); \
```

## jeffro256 | 2021-03-06T21:50:20+00:00
I ran:

    diff -u contrib/epee/include/net/http_server_handlers_map2.h ../monero/contrib/epee/include/net/http_server_handlers_map2.h

I'm on Ubuntu and my diff command doesn't have a `--git` option but `-u` is the next best thing. From that command I got the output:

    +++ ../monero/contrib/epee/include/net/http_server_handlers_map2.h2021-02-26 01:29:54.785800045 -0600
    @@ -74,13 +74,7 @@
           uint64_t ticks = misc_utils::get_tick_count(); \
           boost::value_initialized<command_type::request> req; \
           bool parse_res = epee::serialization::load_t_from_json(static_cast<command_type::request&>(req), query_info.m_body); \
    -      if (!parse_res) \
    -      { \
    -         MERROR("Failed to parse json: \r\n" << query_info.m_body); \
    -         response_info.m_response_code = 400; \
    -         response_info.m_response_comment = "Bad request"; \
    -         return true; \
    -      } \
    +      CHECK_AND_ASSERT_MES(parse_res, false, "Failed to parse json: \r\n" << query_info.m_body); \
           uint64_t ticks1 = epee::misc_utils::get_tick_count(); \
           boost::value_initialized<command_type::response> resp;\
           MINFO(m_conn_context << "calling " << s_pattern); \
    @@ -110,13 +104,7 @@
           uint64_t ticks = misc_utils::get_tick_count(); \
           boost::value_initialized<command_type::request> req; \
           bool parse_res = epee::serialization::load_t_from_binary(static_cast<command_type::request&>(req), epee::strspan<uint8_t>(query_info.m_body)); \
    -      if (!parse_res) \
    -      { \
    -         MERROR("Failed to parse bin body data, body size=" << query_info.m_body.size()); \
    -         response_info.m_response_code = 400; \
    -         response_info.m_response_comment = "Bad request"; \
    -         return true; \
    -      } \
    +      CHECK_AND_ASSERT_MES(parse_res, false, "Failed to parse bin body data, body size=" << query_info.m_body.size()); \
           uint64_t ticks1 = misc_utils::get_tick_count(); \
           boost::value_initialized<command_type::response> resp;\
           MINFO(m_conn_context << "calling " << s_pattern); \

"../monero" is where I cloned the main working repository. I will post the logs for `set_log 4` later today.


## jeffro256 | 2021-03-06T22:25:09+00:00

[Here](https://github.com/monero-project/monero/files/6096211/bitmonero.log)
 is the level 4 log file 

## moneromooo-monero | 2021-03-07T09:34:24+00:00
This diff is the reverse of my patch in the h400 branch.
To apply the patch in the comment above, save it to, eg, /tmp/patch:
> patch -p1 < /tmp/patch

## moneromooo-monero | 2021-03-07T09:38:47+00:00
The log doesn't show anything more unfortunately. It's odd you're not getting serialization errors like I do. What platform is it ?

## jeffro256 | 2021-03-07T18:55:55+00:00
I think that's just how `-u` displays the output because I have triple-checked that the code in the working directory is your updated code, and the code in the `monero` directory is the old code. My system specs:

    Intel® Core™ i7-8750H CPU @ 2.20GHz
    Ubuntu 20.04.2 LTS (64-bit)
    gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
    g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
    

## moneromooo-monero | 2021-03-07T22:11:14+00:00
-u produces a unified diff (as opposed to old style format). You can check for sure the binary contains by code with:

strings -n 8 build/..../bin/monerod | grep 'Bad request'

If it shows a line, it's good.

## moneromooo-monero | 2021-03-07T22:11:53+00:00
In any case, both with and without the patch should trigger the parse error, which you don't have in your logs, so the issue is elsewhere.

## jeffro256 | 2021-03-08T05:03:32+00:00
Yeah that is weird... Do you think that it's not an EPEE parse error? I ran the strings command and it returned `Bad request`. I know you probably did, but did you try testing it on your end to make sure it returns a 400 status? I can't for the life of me get anything to return a 400 status. I might try manually debugging it soon...

## jeffro256 | 2021-03-08T06:07:33+00:00
Sorry if this is a n00b question, but how do you debug the `handle_http_request_map` function? I built with `make debug` but it doesn't come up in the list of functions with `info functions`. I'm using gdb btw. Is there a chance that's there's another part of the code that is handling deserialization?

## moneromooo-monero | 2021-03-08T18:05:36+00:00
Yes, I ran curl on it and got a 400 code, using:

> curl -v http://127.0.0.1:28081/in_peers -d '{"in_peers": -1}' -H 'Content-Type: application/json'

## jeffro256 | 2021-03-09T01:03:03+00:00
Setting a breakpoint in "contrib/epee/include/net/http_protocol_handler.inl" at line 618 caused the code to halt when I ran the command `curl -v http://127.0.0.1:28081/in_peers -d '{"in_peers": -1}' -H 'Content-Type: application/json'`. I think this is the part of the code that is returning a 404 status code for me. The function that your changes were inside of in the above PR doesn't even show up in the debugger. What do you think?

## jeffro256 | 2021-03-09T17:32:36+00:00
Do you think it makes a difference that yours was running on stagenet? (at least I presume from 28081 port)

## moneromooo-monero | 2021-03-11T00:38:42+00:00
I don't see "Not found (404)" in the log you posted, which is the line you're pointing to. Testnet should not matter.

## jeffro256 | 2021-03-12T15:59:46+00:00
The '404 Not Found' log message is on line 34114, from "contrib/epee/include/net/http_protocol_handler.inl:594"

## moneromooo-monero | 2021-03-14T09:50:23+00:00
That's a dump of the returned data, the log is different.

## jeffro256 | 2021-03-14T22:44:11+00:00
Well either way, doesn't that means that its returning a 404 error when it shouldn't? Would it be helpful for me to print my backtrace and local variables from where I got that message?

## moneromooo-monero | 2021-03-17T12:03:17+00:00
It would be helpful.

# Action History
- Created by: jeffro256 | 2021-02-21T00:57:21+00:00
- Closed at: 2023-10-25T22:14:29+00:00
