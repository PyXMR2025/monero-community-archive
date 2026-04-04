---
title: 'feature request: run monerod in foreground without tty'
source_url: https://github.com/monero-project/monero/issues/1763
author: dotnwat
assignees: []
labels: []
created_at: '2017-02-21T19:00:06+00:00'
updated_at: '2017-08-29T09:36:14+00:00'
type: issue
status: closed
closed_at: '2017-08-29T09:36:14+00:00'
---

# Original Description
Currently if monerod is run in the foreground without a tty allocated then it immediately exits after it blocks on standard input for user commands. It would be useful for containerization if this were not the case. A simple mode in which user inputs are not activated without a tty would be sufficient.

# Discussion History
## hyc | 2017-02-21T19:52:35+00:00
That's what the --detach option is for.

## dotnwat | 2017-02-21T20:05:00+00:00
Running in the background is inconvenient in a containerized environment because the canonical usage is that the container waits on the main process to exist. In this case that main process is monerod. Keeping the container alive with monerod in the background means making something tail -f monero.log the main process, which has drawbacks in terms of monitoring etc... running the foreground with tty is possible, but the no-tty mode i'm proposing is nice because I don't need to worry about rouge data slipping in through standard input.

## hyc | 2017-02-21T20:21:55+00:00
monerod is surely not the first daemon to ever be run in a container, and the monerod daemon behavior is standard behavior for all Unix daemons. There must already be a common solution for this use case.

## dotnwat | 2017-02-21T20:41:41+00:00
Yes, there are solutions which I'm currently using. This ticket is about an enhancement to monerod to make it work in more canonical behavior. If it changes backwards compat then its probably not worth the effort.

## gituser | 2017-02-21T23:47:43+00:00
@noahdesu you can use start-stop-daemon binary and [this shell script](https://github.com/monero-project/monero/issues/1768#issuecomment-281517002) .  Of course you'd need similar init script for monerod as well.

## Kukunin | 2017-03-04T12:27:04+00:00
👍 for this topic. 
1) It's not about daemon background execution, it's about foreground
2) Monero is first daemon that I've encountered such behaviour with docker
3) It's extremely confusing, if daemon initializes and deinitalizes immediately without no notification - there is no log or message.

At least, it's worth to give some focus on this issue because of third item: it's confusing.
a minimal solution is to print message about 'Can't find tty, going to shutdown' to log.
a better solution is to make Monero working in foreground without tty - I believe there is no significant reason but a coincidence.

## dotnwat | 2017-03-04T15:46:37+00:00
The foreground mode with standard input open really is a headache for integrating with tools. Here is a simple patch that adds a --non-interactive foreground mode. It works, but probably would need some work for upstream inclusions. https://github.com/noahdesu/monero/commit/44a5b03841e34154e824fcc7773c458326a3487f

## amiuhle | 2017-03-04T16:22:55+00:00
I wrote this https://github.com/monero-project/monero/issues/1598#issuecomment-282904374 because I was also confused by that behaviour.

## analogic | 2017-03-09T14:36:58+00:00
+1 hit same issue, there is no way to handle monerod with supervisor properly

## moneromooo-monero | 2017-03-18T10:37:16+00:00
noahdesu, I think your patch is fine, if you want to PR it.

## mortengh | 2017-03-18T11:12:17+00:00
Cool! So my workaround for this TTY issue  is to start the daemon in detached mode and make docker wait by having this in my Dockerfile:

CMD exec /bin/bash -c "./monerod --detach --p2p-bind-port=18080 --rpc-bind-port=18081 & trap : TERM INT; sleep infinity & wait"

## MoroccanMalinois | 2017-08-28T01:55:59+00:00
I confirm that #1897 answers this request

Can be closed ?

## moneromooo-monero | 2017-08-29T09:32:26+00:00
+resolved

# Action History
- Created by: dotnwat | 2017-02-21T19:00:06+00:00
- Closed at: 2017-08-29T09:36:14+00:00
