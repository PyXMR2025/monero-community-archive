---
title: 'using --add-exclusive-node foo:28080 errors with: Failed to parse or resolve
  address from string: foo:28080'
source_url: https://github.com/monero-project/monero/issues/8633
author: euri10
assignees: []
labels: []
created_at: '2022-11-09T17:12:06+00:00'
updated_at: '2023-01-11T16:39:55+00:00'
type: issue
status: closed
closed_at: '2023-01-11T16:39:55+00:00'
---

# Original Description
in order to perform e2e tests I have set up a Dockerfile that spawns a regtest monerod, creates a predictible wallet and spawns a wallet rpc, all that handled by the might s6-overlay.

you can find an example here and clone it : https://gitlab.com/euri10/monero_docker_regtest.git

to run it just do `docker compose up -d --build`

the issue I'm facing is the following:
in `monero_docker/root/etc/s6-overlay/s6-rc.d/monerod/run` which is the scrippt that launches monerod I uses the `--add-exclusive-node` flag.

Now if you look more closely at https://gitlab.com/euri10/monero_docker_regtest/-/blob/main/src/root/etc/s6-overlay/s6-rc.d/monerod/run#L12-13
I pass the ip of the container to the  `--add-exclusive-node` flag and it's working fine.

however, since the 2 containers are in the same network and are reachable I should not have to do the reverse lookup myself in the entry script,

if I uncomment line 12 and comment line 13, which I think is the right thing to do, then monerod complains with the following error:

```
monero_docker_regtest-foo-1  | 2022-11-09 17:06:24.696  I Initializing p2p server...
monero_docker_regtest-foo-1  | 2022-11-09 17:06:24.696  I Resolving node address: host=bar:29080, port=18080
monero_docker_regtest-foo-1  | 2022-11-09 17:06:24.697  E Failed to resolve host name 'bar:29080': Host not found (authoritative):1
monero_docker_regtest-foo-1  | 2022-11-09 17:06:24.697  E Failed to parse or resolve address from string: bar:29080
monero_docker_regtest-foo-1  | 2022-11-09 17:06:24.697  E Failed to handle command line
```

In essence, when I'm passing ` --add-exclusive-node bar:29080` monerod interprets it as if the host was `bar:29080` and the port `18080` which is not the case, hopefully it should understand that bar is the host and 29080 is the port



# Discussion History
## jeffro256 | 2022-11-15T22:50:25+00:00
Does it work if you replace `bar` with the resolved IP address? IIRC, `--add-exclusive-node` does *not* resolve the hostname w/ DNS

## euri10 | 2022-11-16T07:52:52+00:00
> Does it work if you replace `bar` with the resolved IP address

yes, it does work with the resolved ip address, in fact that's the hack I'm doing right now starting the container after doing a `dig +short bar` and passing the result ip to the --add-exclusive-node flag.

> ? IIRC, `--add-exclusive-node` does _not_ resolve the hostname w/ DNS

you cenrtainly know better the code, however the logs seems to indicate something different,  this line in particular `Resolving node address: host=bar:29080, port=18080`
I feel like the host/port parsing fails at detecting I'm passing the host bar on port 29080 and treats the whole string `bar:29080` as the entire host



## jeffro256 | 2022-11-16T22:10:57+00:00
Huh, yeah looks like you found a bug! Try compiling #8643, run `monerod` with the patch and see if it works.

## euri10 | 2022-11-17T08:52:23+00:00
amazing, I tested it and it's working great, can reach my containers with their host name now without having to dig for their ips !!
thanks a lot @jeffro256 
can't wait for it to be in :)

# Action History
- Created by: euri10 | 2022-11-09T17:12:06+00:00
- Closed at: 2023-01-11T16:39:55+00:00
