---
title: 'Monero-wallet-rpc not work as backend for nginx (curl: (47) Maximum (50) redirects
  followed)'
source_url: https://github.com/monero-project/monero/issues/4084
author: minzak
assignees: []
labels: []
created_at: '2018-06-29T19:26:43+00:00'
updated_at: '2018-08-21T10:52:13+00:00'
type: issue
status: closed
closed_at: '2018-07-27T16:07:47+00:00'
---

# Original Description
I have worked monerod + monero-wallet-cli and nginx as proxy.

When i run curl directly to **monero-wallet-cli** daemon - all is work.
When i use my mobile wallet via **nginx->monerod** - all is work.

But when i use curl for **nginx->monero-wallet-cli** - i got curl/nginx error:
**curl: (47) Maximum (50) redirects followed**

```
root@monero:/mnt/monero/logs# curl -u monerowalletrpc:pass --digest -X POST https://monero.domain:8500/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_languages"}' -H 'Content-Type: application/json'
curl: (47) Maximum (50) redirects followed
```

```
root@monero:/mnt/monero/logs# curl -u monerowalletrpc:pass --digest -X POST http://127.0.0.1:18083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_languages"}' -H 'Content-Type: application/json' 
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "languages": ["Deutsch","English","Español","Français","Italiano","Nederlands","Português","русский язык","日本語","简体中文 (中国)","Esperanto","Lojban"]
  }
}
```

**monero.conf**
```
server {
        listen 8500 default_server;
        ssl on;
        ssl_certificate /etc/ssl/private/letsencrypt-domain.pem;
        ssl_certificate_key /etc/ssl/private/letsencrypt-domain.key;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        server_name monero.domain;
        error_log   /var/log/nginx/monero.error.log  warn;
        access_log  /var/log/nginx/monero.access.log ;
        proxy_http_version         1.1;
        proxy_connect_timeout      360;
        proxy_read_timeout         360;
        proxy_pass_header          Date;
        proxy_pass_header          Server;
        proxy_pass_header          Authorization;
        proxy_set_header           Accept-Encoding "";
        proxy_set_header           Host $host;
        proxy_set_header           X-Real-IP $remote_addr;
        proxy_set_header           X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass_request_headers on;
        proxy_buffering            off;
        proxy_set_header           Connection "Keep-Alive";
        location / {
              proxy_pass http://127.0.0.1:18083;
        }
}
```

same config for mobile wallet with **proxy_pass http://127.0.0.1:18081;** fine work!

**nginx.mobile-wallet.conf**
```
server {
        listen 18088;
        server_name monero.domain;
        error_log   /var/log/nginx/monero-wallet.error.log  warn;
        access_log  /var/log/nginx/monero-wallet.access.log ;
        proxy_http_version         1.1;
        proxy_connect_timeout      360;
        proxy_read_timeout         360;
        proxy_pass_header          Date;
        proxy_pass_header          Server;
        proxy_pass_header          Authorization;
        proxy_set_header           Accept-Encoding "";
        proxy_set_header           Host $host;
        proxy_set_header           X-Real-IP $remote_addr;
        proxy_set_header           X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass_request_headers on;
        proxy_buffering            off;
        proxy_set_header           Connection "Keep-Alive";
        location / {
              proxy_pass http://127.0.0.1:18081;
        }
}
```

**monero.access.log**
```
178.128.XX.XX - - [29/Jun/2018:19:35:13 +0000] "POST /json_rpc HTTP/1.1" 400 264 "-" "curl/7.38.0"
178.128.XX.XX - - [29/Jun/2018:19:35:23 +0000] "POST /json_rpc HTTP/1.1" 401 98 "-" "curl/7.38.0"
178.128.XX.XX - - [29/Jun/2018:19:35:23 +0000] "POST /json_rpc HTTP/1.1" 401 98 "-" "curl/7.38.0"
... many same rows here ..
178.128.XX.XX - - [29/Jun/2018:19:35:23 +0000] "POST /json_rpc HTTP/1.1" 401 98 "-" "curl/7.38.0"
178.128.XX.XX - - [29/Jun/2018:19:35:23 +0000] "POST /json_rpc HTTP/1.1" 401 98 "-" "curl/7.38.0"
```

If i use curl wit -v i get:

```
* Hostname was NOT found in DNS cache
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 178.128.XX.XX...
* Connected to monero.domain (178.128.XX.XX) port 8500 (#0)
* successfully set certificate verify locations:
*   CAfile: none
  CApath: /etc/ssl/certs
* SSLv3, TLS handshake, Client hello (1):
} [data not shown]
* SSLv3, TLS handshake, Server hello (2):
{ [data not shown]
* SSLv3, TLS handshake, CERT (11):
{ [data not shown]
* SSLv3, TLS handshake, Server key exchange (12):
{ [data not shown]
* SSLv3, TLS handshake, Server finished (14):
{ [data not shown]
* SSLv3, TLS handshake, Client key exchange (16):
} [data not shown]
* SSLv3, TLS change cipher, Client hello (1):
} [data not shown]
* SSLv3, TLS handshake, Finished (20):
} [data not shown]
* SSLv3, TLS change cipher, Client hello (1):
{ [data not shown]
* SSLv3, TLS handshake, Finished (20):
{ [data not shown]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* Server certificate:
* 	 subject: CN=monero.domain
* 	 start date: 2018-06-25 11:18:33 GMT
* 	 expire date: 2018-09-23 11:18:33 GMT
* 	 subjectAltName: monero.domain matched
* 	 issuer: C=US; O=Let's Encrypt; CN=Let's Encrypt Authority X3
* 	 SSL certificate verify ok.
* Server auth using Digest with user 'monerowalletrpc'
> POST /json_rpc HTTP/1.1
> User-Agent: curl/7.38.0
> Host: monero.domain:8500
> Accept: */*
> Content-Type: application/json
> Content-Length: 0
> 
< HTTP/1.1 401 Unauthorized
< Content-Type: text/html
< Content-Length: 98
< Connection: keep-alive
* Server Epee-based is not blacklisted
< Server: Epee-based
< Last-Modified: Fri, 29 Jun 2018 19:38:55 GMT
< Accept-Ranges: bytes
< WWW-authenticate: Digest qop="auth",algorithm=MD5,realm="monero-rpc",nonce="jC1y2/SEH0xo1P6yUGbdsA==",stale=false
* Ignoring duplicate digest auth header.
< WWW-authenticate: Digest qop="auth",algorithm=MD5-sess,realm="monero-rpc",nonce="jC1y2/SEH0xo1P6yUGbdsA==",stale=false
< 
* Ignoring the response-body
{ [data not shown]

100    98  100    98    0     0   7116      0 --:--:-- --:--:-- --:--:--  7538
* Connection #0 to host monero.domain left intact
* Issue another request to this URL: 'https://monero.domain:8500/json_rpc'
* Found bundle for host monero.domain: 0x55cd4c7f77d0
* Re-using existing connection! (#0) with host monero.domain
* Connected to monero.domain (178.128.XX.XX) port 8500 (#0)
* Server auth using Digest with user 'monerowalletrpc'
> POST /json_rpc HTTP/1.1
> Authorization: Digest username="monerowalletrpc", realm="monero-rpc", nonce="jC1y2/SEH0xo1P6yUGbdsA==", uri="/json_rpc", cnonce="M2M3NjVjMjZiMzUwYzM5YzIzZjgwOWY3OGE3NDFmMmE=", nc=00000001, qop=auth, response="0340a9b10b41d56e3a5568d9a48254c8", algorithm="MD5"
> User-Agent: curl/7.38.0
> Host: monero.domain:8500
> Accept: */*
> Content-Type: application/json
> Content-Length: 51
> 
} [data not shown]
* upload completely sent off: 51 out of 51 bytes
< HTTP/1.1 401 Unauthorized
< Content-Type: text/html
< Content-Length: 98
< Connection: keep-alive
* Server Epee-based is not blacklisted
< Server: Epee-based
< Last-Modified: Fri, 29 Jun 2018 19:38:55 GMT
< Accept-Ranges: bytes
< WWW-authenticate: Digest qop="auth",algorithm=MD5,realm="monero-rpc",nonce="P4lbGCQYPa9IkjAMvlgMHw==",stale=true
* Ignoring duplicate digest auth header.
< WWW-authenticate: Digest qop="auth",algorithm=MD5-sess,realm="monero-rpc",nonce="P4lbGCQYPa9IkjAMvlgMHw==",stale=true
< 
* Ignoring the response-body
{ [data not shown]

100   149  100    98  100    51   6578   3423 --:--:-- --:--:-- --:--:--  6578
* Connection #0 to host monero.domain left intact
* Issue another request to this URL: 'https://monero.domain:8500/json_rpc'
* Found bundle for host monero.domain: 0x55cd4c7f77d0

... repeat block many times ...

```

What is wrong?

# Discussion History
## moneromooo-monero | 2018-06-29T20:28:44+00:00
Are you sure it's monero-wallet-rpc that's replying on that port ?

## minzak | 2018-06-29T20:49:58+00:00
wallet listen and reply, but not any query via curl/nginx way.

My ways:
1 - curl -> wallet = **YES** present query in **wallet** logs,
2 - curl -> nginx -> wallet = **NO** present query in **wallet** logs,
BUT!
3 - curl -> nginx -> node = **YES** present query in **node** logs.
Where:
2 - nginx(**8500**)->wallet(**18083**)
3 - nginx(**18088**)->node(**18081**)

But you see both nginx gonfig, for node and for wallet - differens only in ports.

Where configs are:

**_ExecStart=/usr/local/bin/monero-wallet-rpc --config-file=/mnt/monero/monero-wallet-rpc.conf_**

**monero-wallet-rpc.conf**
```
daemon-address=127.0.0.1:18081
rpc-bind-ip=127.0.0.1
rpc-bind-port=18083
rpc-login=monerowalletrpc:pass
wallet-dir=/mnt/monero/wallets/
log-file=/mnt/monero/logs/monero-wallet-rpc.log
log-level=1
trusted-daemon=1
shared-ringdb-dir=/mnt/monero/shared-ringdb

```

**_ExecStart=/usr/local/bin/monerod --non-interactive --detach --no-igd --confirm-external-bind --restricted-rpc --fast-block-sync=0 --show-time-stats=1 --pidfile=/mnt/monero/monerod.pid --config-file=/mnt/monero/monerod.conf_**

**monerod.conf**
```
data-dir=/mnt/monero
log-file=/mnt/monero/logs/monerod.log
log-level=1
p2p-bind-ip=0.0.0.0
p2p-bind-port=18080
zmq-rpc-bind-ip=127.0.0.1
zmq-rpc-bind-port=18082

#for nginx
rpc-bind-ip=127.0.0.1
rpc-bind-port=18081

#if no nginx use next
#rpc-bind-ip=0.0.0.0
#rpc-bind-port=18089
```




## moneromooo-monero | 2018-06-30T10:02:16+00:00
If you just kill off monero-wallet-rpc, do you still get these redirects ? AFAIK, monero code does not use redirects. Maybe just run nc (nc -l PORT_WHERE_RPC_WAS_LISTENING) on that port instead, to see if you get anything at all.

## jtgrassie | 2018-07-01T11:32:33+00:00
There is no auth on the node which is why your "curl -> nginx -> node" works. 
Try adding:
```
proxy_set_header Authorization $http_authorization;
proxy_pass_header  Authorization;
```
to your nginx.mobile-wallet.conf

## jtgrassie | 2018-07-01T11:34:57+00:00
And `proxy_pass_request_headers on;`

## minzak | 2018-07-01T13:17:13+00:00
@moneromooo-monero  if wallet does not work - i get 502 error in nginx - Bad gateway, because here is no present listener on  18083 port.
after run **nc -l -p 18084**  (and reconfigure nginx to 18084 proxy port) and make this request:
`curl -v -u monerowalletrpc:pass --digest -X POST http://127.0.0.1:8500/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_languages"}' -H 'Content-Type: application/json'
`

i have:
```
root@monero:/mnt# nc -l -p 18084
POST /json_rpc HTTP/1.1
Connection: Keep-Alive
Cache-Control:: no-cache
X-Real-IP: 127.0.0.1
X-Forwarded-For: 127.0.0.1
Host: 127.0.0.1
X-Forwarded-Host: 127.0.0.1:8500
Origin: 127.0.0.1:8500
Referer: 127.0.0.1:8500
Content-Length: 0
User-Agent: curl/7.38.0
Accept: */*
Content-Type: application/json
```
It is a prove, that proxy pass works, but maybe it is not all needed header or else, or we have something wrong in monero-wallet-rpc, because monerod full works in proxy mode!!!

**I dont understand One Main Thing - Why on the same scheme (curl-nginx-daemon) monerod works, but monero-wallet-rpc does not work! What a differences between these 2 files in network stack?**
 
@jtgrassie  Thanks, but it does no work, i also tried to use other option in any variants - still no luck.
see my last config **nginx.monero.conf**
```
server {
        listen 8500;
        server_name 127.0.0.1;
        error_log   /var/log/nginx/monero.error.log  warn;
        access_log  /var/log/nginx/monero.access.log ;
        location / {
        proxy_set_header           Connection "Keep-Alive";
        proxy_set_header Cache-Control: no-cache;
        add_header Content-Type application/json;

        proxy_http_version         1.1;
        proxy_connect_timeout      360;
        proxy_read_timeout         360;
        proxy_pass_header          Date;
        proxy_pass_header          Server;
        proxy_pass_header          Authorization;
        proxy_set_header           Authorization $http_authorization;
        proxy_set_header           Accept-Encoding "";
        proxy_set_header           X-Real-IP $remote_addr;
        proxy_set_header           X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass_request_headers on;
        proxy_set_header           Host $host;
        proxy_set_header           X-Forwarded-Host $host:$server_port;

#    proxy_redirect off;
#    proxy_buffering off;

#proxy_hide_header   Referer;
#proxy_hide_header   Origin;

proxy_set_header    Origin        $host:$server_port;
proxy_set_header    Referer       $host:$server_port;

#proxy_set_header    Referer           '';
#proxy_set_header    Origin            '';

              proxy_pass http://127.0.0.1:18083;

        }
}
```

I know, that in this case only 3 possible errors in curl, or, nginx, or monero.
For curl - i have a lot other work examples, i do not think that point in curl.
For nginx - also have many different rpc services, nodes, wallets and everything is fine - this is my first strange case. (i also open case on nginx - https://trac.nginx.org/nginx/ticket/1586 )
For Monero - it is possible, but as i say - i do not understand why only one binaries have this strange.

P.S. i also made 2 log for compare, where 1.txt - direct curl, 2.txt - proxy curl, with nginx.monero.conf
```
curl -v -u monerowalletrpc:pass --digest -X POST http://127.0.0.1:18083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_languages"}' -H 'Content-Type: application/json' >1.txt 2>&1
curl -v -u monerowalletrpc:pass --digest -X POST http://127.0.0.1:8500/json_rpc  -d '{"jsonrpc":"2.0","id":"0","method":"get_languages"}' -H 'Content-Type: application/json' >2.txt 2>&1
```
[1.txt](https://github.com/monero-project/monero/files/2152812/1.txt)
[2.txt](https://github.com/monero-project/monero/files/2152813/2.txt)


## moneromooo-monero | 2018-07-01T13:46:09+00:00
Disable auth on monero-wallet-rpc. If it then works, jtgrassie's on to something.

## minzak | 2018-07-01T14:05:14+00:00
@moneromooo-monero  YES, if i disable auth, just add --disable-rpc-login to daemon all is work
In direct request and proxy request. 
And what is mean?
What is wrong?


## moneromooo-monero | 2018-07-01T14:44:58+00:00
What jtgrassie said. You need to get nginx to pass on auth properly.

## minzak | 2018-07-01T15:03:46+00:00
@moneromooo-monero  for monerod nginx to pass on auth is properly works!
And we add many options - and nothing (
And auth path corectly works with monerod, but no with monero-wallet-rpc.
What is wrong.

## jtgrassie | 2018-07-01T15:08:00+00:00
Try with --basic instead of --digest. Essentially this is an nginx proxy configuration issue not monero-wallet-rpc. I suggest trying to get help on nginx channels will get you better help than on this monero bug tracker.

## jtgrassie | 2018-07-01T15:09:39+00:00
Also, you do know you can get the nginx proxy to do the authorization and run the wallet without.

## minzak | 2018-07-01T15:15:50+00:00
@jtgrassie no, without nodigest in curl it is not work - no any request no work, no direct, no proxy.
`<html><head><title>Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html>`
I can't use rpc without pass - it is no secure for prod server (

Yes, i can use wallet with no password, but nginx with native auth.
**But it is not resolve bug in waller-rpc or nginx mismatch some proxy params, i'm right?**
P.S. why other nodes+wallet work. but no this one, and only wallet-rpc doesn't ? With monerod is all fine!

## jtgrassie | 2018-07-01T15:28:08+00:00
It's not a bug in wallet-rpc, it's misconfigured nginx. That's why I suggested you try and get help on nginx channels where there are people who know nginx far better than monero devs. 

## minzak | 2018-07-01T15:35:21+00:00
@jtgrassie  Why different auth behaviour in 2 files? It not must be work that.
And i understand that if i found some magic config for nginx - it is resolve my issue,
But also - it is not normal, because even monerod fine work!
I prove here that auth method  of monerod and monero-wallet-rpc is different!

**It is sadly (**
If we will use current nginx config and with password on rpc - what else can we do ?

## minzak | 2018-07-01T16:28:53+00:00
@moneromooo-monero  @jtgrassie 
Nginx answer - `For some reason your backend reject requests with the error 401 Unauthorized. You have to investigate your backend to find out why it does this. Either way, this doesn't looks like a bug in nginx, so closing this.`
As i  think - weird behaviour of monero-wallet-rpc!

In logs we can see 2 request, and wallet not correctly works with it.
I also see other nginx variants.

## moneromooo-monero | 2018-07-01T16:44:24+00:00
Run monero-wallet-rpc with --log-level 0,net:TRACE which will get you a dump of the received HTTP. Paste this received HTTP here.


## minzak | 2018-07-01T16:56:50+00:00
For this curl:
`curl -v -u monerowalletrpc:pass --digest -X POST http://127.0.0.1:8500/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_languages"}' -H 'Content-Type: application/json' >1.txt 2>&1
`
I got answer:[1.txt](https://github.com/monero-project/monero/files/2152967/1.txt)
with this configs with --log-level 0,net:TRACE:
[monero-wallet-rpc.conf.txt](https://github.com/monero-project/monero/files/2152968/monero-wallet-rpc.conf.txt)
[nginx.monero.conf.txt](https://github.com/monero-project/monero/files/2152969/nginx.monero.conf.txt)
i got this wallet-rpc log:
[wallet.log.txt](https://github.com/monero-project/monero/files/2152972/wallet.log.txt)


## moneromooo-monero | 2018-07-01T17:16:41+00:00
Sorry, should have been: --log-level 0,net\*:TRACE

## jtgrassie | 2018-07-01T17:20:03+00:00
> Why different auth behaviour in 2 files? It not must be work that.
And i understand that if i found some magic config for nginx - it is resolve my issue,
But also - it is not normal, because even monerod fine work!
I prove here that auth method of monerod and monero-wallet-rpc is different!

No. You aren't doing any actual auth on monerod, only wallet.

> Nginx answer - For some reason your backend reject requests with the error 401 Unauthorized. You have to investigate your backend to find out why it does this. Either way, this doesn't looks like a bug in nginx, so closing this.
As i think - weird behaviour of mo

It's not an nginx bug as far as I can tell, just your config is wrong.


## minzak | 2018-07-01T17:28:56+00:00
@jtgrassie Thanks, i understand that it it some missing in config, as one of way to resolve it, but we put in config almost all possible strings)
@moneromooo-monero Ok, restart with new config and new logs:
[wallet.log.txt](https://github.com/monero-project/monero/files/2152994/wallet.log.txt)


## moneromooo-monero | 2018-07-01T18:19:59+00:00
It seems it's only logging the outgoing data, not the incoming one, that's annoying as we don't get what I hoped to get.

## moneromooo-monero | 2018-07-01T18:21:22+00:00
Ah, you already posted a sample of this when using nc. It does not have any authentication header, so it looks like nginx is stripping it.

Try using nc again to see if it does include the auth header after you modified the nginx config.

## minzak | 2018-07-01T20:19:12+00:00
@moneromooo-monero  nc can use in many variants, not understand which one need for you?
And i see, i can't put nc betwen two services, only send or only receive. 
What command i must to use? 

## moneromooo-monero | 2018-07-01T20:28:58+00:00
I mean replace monero-wallet-rpc with nc as you did before, to see what nginx sends you.

## minzak | 2018-07-01T20:54:35+00:00
If i stop wallet, and run **nc -l -p 18083**
and run curl, i get:
```
root@monero:~# nc -l -p 18083
POST /json_rpc HTTP/1.1
Connection: Keep-Alive
X-Real-IP: 127.0.0.1
X-Forwarded-For: 127.0.0.1
X-Forwarded-Host: 127.0.0.1:8500
Host: 127.0.0.1:18083
Content-Length: 0
User-Agent: curl/7.38.0
Accept: */*
Content-Type: application/json
```
And it is all.

If i all stops and run direct query to nc (like to wallet) i get:

```
root@monero:~# nc -l -p 18083
POST /json_rpc HTTP/1.1
User-Agent: curl/7.38.0
Host: 127.0.0.1:18083
Accept: */*
Content-Type: application/json
Content-Length: 0
```

As i see - the same except additional header from nginx,

Also in typical proxy mode  (curl-nginx-wallet) i run this:
**tcpdump -i lo "port 8500 or port 18083" -A >dump.cap.txt**
 
and got
[dump.cap.txt](https://github.com/monero-project/monero/files/2153181/dump.cap.txt)


## moneromooo-monero | 2018-07-01T22:15:01+00:00
Then you need to find how to get nginx to not drop the auth headers.

## jtgrassie | 2018-07-01T23:32:29+00:00
@bizlevel 
> but we put in config almost all possible strings

Hardly. There are tons of other settings that have not been tried. 

I'll say it again, you'll get better help searching and asking the nginx community.

## moneromooo-monero | 2018-07-18T18:07:24+00:00
Did you find out what was being filtered out and why ?

## minzak | 2018-07-18T18:11:00+00:00
no, but i know what is point, it is like active and passive mode in ftp. Here is same. 
Just rewrite TCP stack like in **monero-wallet-cli**  and all will be fine.

## ChrisRut | 2018-07-27T13:35:53+00:00
I spent a ton of time banging my head against the wall on this, and I figured it out.
The issue is Digest authentication requires keepalive in your nginx config, so you can't simply use:
```
proxy_pass http://127.0.0.1:18083;
```

Your config must include an [`upstream` directive](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#upstream), a [`keepalive` setting](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#keepalive), and you must strip the `Connection` header from the request (otherwise nginx will send `close`), so here is a working config:
```
upstream monerowallet {
  server 127.0.0.1:18083;
  keepalive 64;
}

server {
    listen 0.0.0.0:18084 ssl;
    ssl_certificate     /etc/nginx/ssl/server.cert;
    ssl_certificate_key /etc/nginx/ssl/server.pem;
    ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers         HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers   on;

    location / {
  	# Remove the Connection header if the client sends it,
  	# it could be "close" to close a keepalive connection
  	proxy_set_header Connection "";
	proxy_pass http://monerowallet;
        proxy_http_version 1.1;
        proxy_read_timeout 600s;
    }
}
```

## minzak | 2018-07-27T15:17:34+00:00
yes, this works. But it is trick) Not like in other monero apps. 

## jtgrassie | 2018-07-27T15:58:24+00:00
It's not a "trick", it's clearly required for the authentication to work. 

## minzak | 2018-07-27T16:05:39+00:00
why this is not require for wallet? No one not hear me! 

## minzak | 2018-07-27T16:07:47+00:00
this is very minor, and not a bug, just is usual behavior, that not present in a lot other nodes and wallets. 

## ghost | 2018-08-21T10:52:13+00:00
I want to add monero to my exchange, how do i add the monero.conf file just like that of bitcoin.conf were the content of bitcoin.conf file is 
server=1
rpcport=18523
rpcallowip=29.99.99.30/0
rpcuser=bitcoin
rpcpassword=123455
walletnotify=/var/www/html/cron/receive.sh %s
thanks


# Action History
- Created by: minzak | 2018-06-29T19:26:43+00:00
- Closed at: 2018-07-27T16:07:47+00:00
