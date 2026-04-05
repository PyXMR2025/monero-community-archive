---
title: 'Question: pause/resume the miner remotely'
source_url: https://github.com/xmrig/xmrig/issues/3220
author: Lonnegan
assignees: []
labels: []
created_at: '2023-02-28T22:27:37+00:00'
updated_at: '2025-06-18T22:45:51+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:45:51+00:00'
---

# Original Description
Hello,

when I sit in front of the PC with xmrig running, I simple can pause and resume mining by pressing p and r. But that is not comfortable under any circumstances. Is there any possibility to remotely pause and resume mining e.g. per script without having to log on the machine and manually press p or r?

# Discussion History
## Spudz76 | 2023-03-01T18:54:45+00:00
I (re)documented it all in an [API update PR](https://github.com/xmrig/xmrig/pull/3030) that has never been merged, but can be [viewed here](https://github.com/xmrig/xmrig/blob/ddf304620575218bbb4b91cd205c99c486238f86/doc/API.md#json-rpc-interface)

You have to enable http+API and a secret to enable the writable control endpoints, and use the Bearer header with that secret.  Send `pause` or `resume` and it pokes the identical spot in the code where the P/R keys do.  Without the rest of my PR the `start` isn't there, only `stop` which will force you to login and relaunch to get it going again (or, GET and then PUT the same config as is running which will trigger a config-changed and soft restart).

## Lonnegan | 2023-03-01T21:29:10+00:00
Thank you for the links.

I tried it with this config

"http": {
        "enabled": true,
        "host": "127.0.0.1",
        "port": 44444,
        "access-token": "SECRET",
        "restricted": false
    },

Started xmrig and then tried to pause it with the following command in cmd:

curl -v --data '{"method":"pause","id":1}' -H "Content-Type: application/json" -H "Authorization: Bearer SECRET" http://127.0.0.1:44444/json_rpc

But it doesn't work:

C:\WINDOWS\system32>curl -v --data '{"method":"pause","id":1}' -H "Content-Type: application/json" -H "Authorization: Bearer SECRET" http://127.0.0.1:44444/json_rpc
*   Trying 127.0.0.1:44444...
* Connected to 127.0.0.1 (127.0.0.1) port 44444 (#0)
> POST /json_rpc HTTP/1.1
> Host: 127.0.0.1:44444
> User-Agent: curl/7.83.1
> Accept: */*
> Content-Type: application/json
> Authorization: Bearer SECRET
> Content-Length: 21
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Access-Control-Allow-Headers: Authorization, Content-Type
< Access-Control-Allow-Methods: GET, PUT, POST, DELETE
< Access-Control-Allow-Origin: *
< Connection: close
< Content-Length: 119
< Content-Type: application/json
<
* Excess found in a read: excess = 355, size = 119, maxdownload = 119, bytecount = 0
{
    "error": {
        "code": -32700,
        "message": "Parse error"
    },
    "jsonrpc": "2.0",
    "id": null
}* Closing connection 0

What's wrong?


## Spudz76 | 2023-03-01T23:24:48+00:00
Not sure.

```
$ curl -v --data '{"method":"pause","id":1}' -H "Content-Type: application/json" -H "Authorization: Bearer UuK3ajTsQKLzmdG" http://127.0.0.1:10083/json_rpc
*   Trying 127.0.0.1:10083...
* Connected to 127.0.0.1 (127.0.0.1) port 10083 (#0)
> POST /json_rpc HTTP/1.1
> Host: 127.0.0.1:10083
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Type: application/json
> Authorization: Bearer UuK3ajTsQKLzmdG
> Content-Length: 25
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Access-Control-Allow-Headers: Authorization, Content-Type
< Access-Control-Allow-Methods: GET, PUT, POST, DELETE
< Access-Control-Allow-Origin: *
< Connection: close
< Content-Length: 83
< Content-Type: application/json
<
* Excess found in a read: excess = 318, size = 83, maxdownload = 83, bytecount = 0
{
    "result": {
        "status": "OK"
    },
    "jsonrpc": "2.0",
    "id": 1
* Closing connection 0
```
And in the output/log:
```
[2023-03-01 16:20:19.716]  miner    paused, press  r  to resume
```

Then the opposite,
```
~$ curl -v --data '{"method":"resume","id":1}' -H "Content-Type: application/json" -H "Authorization: Bearer UuK3ajTsQKLzmdG" http://127.0.0.1:10083/json_rpc
*   Trying 127.0.0.1:10083...
* Connected to 127.0.0.1 (127.0.0.1) port 10083 (#0)
> POST /json_rpc HTTP/1.1
> Host: 127.0.0.1:10083
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Type: application/json
> Authorization: Bearer UuK3ajTsQKLzmdG
> Content-Length: 26
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Access-Control-Allow-Headers: Authorization, Content-Type
< Access-Control-Allow-Methods: GET, PUT, POST, DELETE
< Access-Control-Allow-Origin: *
< Connection: close
< Content-Length: 83
< Content-Type: application/json
<
{
    "result": {
        "status": "OK"
    },
    "jsonrpc": "2.0",
    "id": 1
* Closing connection 0
```
And the confirmation:
```
[2023-03-01 16:20:46.046]  miner    resumed
```

Maybe for some reason Windows commandline is different.  It might not like the single-quoted `--data` argument (could be sending the singlequotes literally, which would be invalid JSON).

## Spudz76 | 2023-03-01T23:29:11+00:00
Yep, windows cmd.exe hates the singlequotes.  Do it as such, then:
```
curl -v --data "{\"method\":\"pause\",\"id\":1}" -H "Content-Type: application/json" -H "Authorization: Bearer SECRET" http://127.0.0.1:44444/json_rpc
```

Under Linux I use the singlequote method to avoid all the escaping the other doublequotes.

Tested working from a windows machine.

## Spudz76 | 2023-03-01T23:36:44+00:00
And if you'd like to send the commands from a different PC on the LAN or such, use `http->host` as `0.0.0.0` instead of `127.0.0.1`, so it binds to externally accessible IP(s).

## Lonnegan | 2023-03-02T06:26:48+00:00
That's it! Thanks bro! :-)

## DavidReddecliffe | 2025-01-16T10:47:40+00:00
I currently have 5 added workers from 4 devices all on the same VLAN. I can see all device statistics and edit the config.json files through any device's browser when on the same VLAN.
But how do you POST the pause / resume instructions through the web interface [[http://workers.xmrig.info/worker/dev?]](http://workers.xmrig.info/worker/dev?)
_If this is not possible, any suggestions on £0 self hosted solutions would be very much appreciated._


## DavidReddecliffe | 2025-01-16T11:45:12+00:00
> I currently have 5 added workers from 4 devices all on the same VLAN. I can see all device statistics and edit the config.json files through any device's browser when on the same VLAN.
> But how do you POST the pause / resume instructions through the web interface [[http://workers.xmrig.info/worker/dev?]](http://workers.xmrig.info/worker/dev?)
> _If this is not possible, any suggestions on £0 self hosted solutions would be very much appreciated._
> 


![image](https://github.com/user-attachments/assets/1abf9c93-467c-4261-9451-2b065c86946e)

Answered my own noib question 😂

Just in case the answer is: 
1) open to the Dev option of the worker
2) drop down and change GET to POST
3) replace the contents of the last text box across the top with /json_rpc
4) add the pause or resume command to the larger text box
5) hit send 👏🏻

    Command to use for pause: ``{"method":"pause","id":1}``

    Command to use for resume: ``{"method":"resume","id":1}``

Now I'm going to self host http://workers.xmrig.info, so that I can open it in the browser of any device on my network and add buttons to pause and resume, rather than typing commands ✅

## divinity76 | 2025-06-14T11:43:17+00:00
cmd:
```
curl -X POST http://localhost:7681/json_rpc -H "Content-Type: application/json" -H "Authorization: Bearer token" --data-raw "{\"method\":\"pause\",\"id\":1}"

curl -X POST http://localhost:7681/json_rpc -H "Content-Type: application/json" -H "Authorization: Bearer token" --data-raw "{\"method\":\"resume\",\"id\":1}"
```
works for me with `xmrig.exe --http-port=7681 --http-access-token=token --http-no-restricted`

# Action History
- Created by: Lonnegan | 2023-02-28T22:27:37+00:00
- Closed at: 2025-06-18T22:45:51+00:00
