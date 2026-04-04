---
title: Use password hashes for RPC login
source_url: https://github.com/monero-project/monero/issues/7659
author: moneromooo-monero
assignees: []
labels: []
created_at: '2021-04-11T10:25:52+00:00'
updated_at: '2022-05-25T10:02:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
From JaakkoLuttinen[m on IRC:

RPC login should support hashed passwords. It's bad practice to store passwords in plain text as --rpc-login` requires. For instance, Linux stores users' passwords hashed.


# Discussion History
## vtnerd | 2021-04-11T20:13:08+00:00
Bitcoin and other similar systems behave identically to Monero because this won't work with HTTP digest authentication easily. We'd have to provide a tool (bash script?) that correctly generates the two hashes necessary to be specified on the command line, or just force the user to know the correct scheme. And knowledge of these two hashes allows an attacker to "login" into the HTTP server, so the only benefit is the protection against password re-use with another service.

## artyomsol | 2021-05-21T09:13:46+00:00
@vtnerd bitcoin core and clones does not behave identically to Monero  at all. It uses **Basic access authentication** schema while Monero RPC API requires **Digest authentication**.
Plain text passwords is a final fallback authentication configuration for bitcoin core. 
There are two main use cases for RPC API: 
1. Server and Client started on a same user environment
2. Server runs continuously and configured to accept RPC requests from one or multiple statically configured (possibly remote) clients.  

For the first case, if no `rpcpassword` is set, rpc cookie auth is sought. Server generates random credentials on start up (`.cookie` file, readable for user who started the server). And client reads `.cookie` file and uses credentials obtained. 
The idea of this method is to simplify node daemon and wallet client configuration as far as they are started under the same user.

For the second use case - single or multiple authorization credentials required to be configured statically on a server side.
That is the case where plain text `rpcpassword` is used to configure `monerod` while the bitcoin core daemon prefers `rpcauth`
configuration containing `<rpc user>:<rpc password hash>` (could be generated with python script provided under `share/rpcauth` folder of binaries package [see](https://github.com/bitcoin/bitcoin/tree/master/share/rpcauth) ). 

If `monerod` will be designed to stick to a session digest authorization (i.e. "algorithm" directive's value is "MD5-sess", see [RFC 2617](https://datatracker.ietf.org/doc/html/rfc2617#section-3.2.2.2))
then it could be configured with `rpcauth = username:hash` where `hash = H(username:realm:password)` 
and use it to authenticate RPC calls without storing and transferring plain text passwords.  
This approach will not brake any existing integrations as long as they are stick to a RFC 2617.

## vtnerd | 2021-05-31T11:24:09+00:00
Are you asking me to provide a script that generates such a hash? See above:

> We'd have to provide a tool (bash script?) that correctly generates the two hashes necessary to be specified on the command line, or just force the user to know the correct scheme

This scheme was primarily designed to prevent sending the password to the server - the client always has the login details. If the   wrong, possibly malicious, server was contacted the password never leaked. This also has the benefit of never leaking the password in a cleartext context, but logins without encryption+authentication are perilous anyway.

I don't see a benefit because the A1 hash becomes the defacto password in your request. Unless the issue is password re-use?

## vtnerd | 2021-05-31T11:26:43+00:00
Oh sorry skimmed too quickly - yes the random cookie method with password file. That can be done.

## vtnerd | 2021-05-31T11:27:50+00:00
`[--http-auth-cookie=~/.bitmonero/http_cookie]` will be the new option I think. By default it just does that.

## artyomsol | 2021-05-31T17:20:50+00:00
> Are you asking me to provide a script that generates such a hash? 

No, I'm not. It's pretty simple as long as realm remains hardcoded ```monero-rpc``` (BTW, it's better to allow to configure custom realm value or infer it from host name).

> I don't see a benefit because the A1 hash becomes the defacto password in your request.

Yes, it does. And caution stated clearly in [RFC 2617](https://datatracker.ietf.org/doc/html/rfc2617#section-4.13) 

>Unless the issue is password re-use?

The issue is about the best practice - do not have a plain text passwords stored on a server side. Including re-used credentials  drawback.

## vtnerd | 2021-05-31T19:48:45+00:00
Are you suggesting the deprecation of HTTP auth entirely? SSL authentication should work already for those that need the security. I'm pushing back slightly because this will change existing behavior.

The wallet currently randomly generates a user/pass if none is provided, and writes the information to a specific file. This is identical to the user setting up manually, except each restart the value changes and the value is pseudo-randomly selected as opposed to human selected.

The daemon rpc can be modified in the same way, but it still has the same limitation. The login credentials are being stored on the harddisk. There isn't a way to get around this afaik. 




## artyomsol | 2021-05-31T20:45:15+00:00
As @moneromooo-monero quoted from IRC: do not store passwords in plain text on server side.
It is not a case when client and server started under the same user environment and randomly generated credentials could be fetched from locally accessible file.
Just adding ```rpcauth``` parameter with ```username:A1``` and  using ```A1``` for Digest Access Authentication will keep things running without any influence on existing integrations while plain text passwords will be hashed. 
This is not an ideal implementation. It is just a canonical RFC 2617 implementation familiar to bitcoin core users. 

# Action History
- Created by: moneromooo-monero | 2021-04-11T10:25:52+00:00
