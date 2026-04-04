---
title: Switching between local/remote node is buggy sometimes.
source_url: https://github.com/monero-project/monero-gui/issues/2206
author: sanderfoobar
assignees: []
labels: []
created_at: '2019-06-08T21:51:34+00:00'
updated_at: '2020-02-13T14:38:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Switching between local/remote node or remote node to another remote node *can* be buggy. I say can because I don't know in what situation exactly it becomes buggy, but it is easy to reproduce by switching between remote nodes.

For example: 

1. go to Settings->Node
2. Enable Remote Node
3. Enter ip:port of node you find on `https://autonode.xmr.pm`
4. Press connect
5. It connects (hopefully)
6. Enter a different ip:port of a node
7. Press connect
8. It connects (hopefully)

Step 5 and 8 is where it can become problematic. Firstly, the user has no feedback of what the GUI is doing:

1. Is it busy connecting?
2. Was it able to do a TCP handshake (e.g: is the host reachable) ?
3. Is it a slow node? (perhaps it only started responding after 2000 msec
4. Did we connect?

Secondly, I believe libwalletqt (daemonManager) becomes quite confused if the remote node has certain kind of problems, at which point switching to another node and pressing 'Connect' will not do anything - as if the daemonManager is in limbo from the previous attempt(s). I could be wrong, then again there is no feedback to tell what is happening.

Would be nice if:

1. There is feedback, or a log to tell how the connection is progressing
2. A message when the connection failed
3. Verify that pressing 'Connect' will indeed destroy any previous attempt or state.
4. Maybe also introduce a 'Disconnect' button.

# Discussion History
## ghost | 2019-06-10T18:27:59+00:00
I can confirm I had the same issues. A main problem is that you never know what the GUI is doing because the status/messages are not good enough. 

## dEBRUYNE-1 | 2019-07-04T06:31:35+00:00
@Realchacal - Can you check again with GUI v0.14.1.0? 

## ghost | 2019-07-05T14:22:07+00:00
@dEBRUYNE-1 

Node switching unfortunately is still buggy. What I just did:

1. Launch the new GUI version. It automatically connected to the remote node that I was using the last time. Fine!
2. Enter another remote node address ("opennode.xmr-tw.org", same port)
3. Click connect. It disconnected! Nothing else.
4. Click connect again. Nothing.
5. Close wallet. It freezed for 10 seconds, then it actually closed.
6. Reopen the wallet. The remote node didn't connect automatically and pressing "connect" didn't help.
7. Switch to local node and instantly back to remote note. Didn't help.
7. Enter another remote node address ("node.moneroworld.com", same port), click connect. It connected!
9. Enter the remote node address from before again ("opennode.xmr-tw.org", same port), click connect. Now it works!

Apart from that: Status messages are not good enough. You just don't know, what the GUI is doing. When switching between remote node and local node the status isn't updated immediately, instead I sometimes have to wait up to 2-3 seconds until I see a status change. This drives people crazy, especially if they have to wait much longer than 2-3 seconds because of bad internet connection, and if they are new users. They just don't know "is it doing something? What is it doing? Do I have to press 'connect' or just wait?" There should be INSTANT status message changes when the user clicks something. Like "closing local node", "local node closed", "connecting to remote node (no response yet)", "connecting to remote node (is responding)" or something like that.

## MicahZoltu | 2019-07-18T07:57:38+00:00
I am trying to connect to a remote node of mine and there is no information in either the GUI, the GUI logs tab, or the remote node's logs.  Clicking the connect button doesn't appear to do anything at all, though maybe it is trying behind the scenes and just giving zero feedback?  I don't know if the host is unreachable, or if my remote node is on an incompatible version (it is running 0.13.x while GUI is 0.14.x), or if there is some other problem.

I'm at a total loss as to why I can't connect, but at the moment I cannot use Monero and it is quite frustrating.  Some simple status/logs would go a _long_ way to making this situation better!

## selsta | 2019-07-18T10:27:12+00:00
@MicahZoltu You can’t use v0.13 anymore.

Update both to v0.14.1.0 and it will work like expected.

## ghost | 2019-07-18T10:33:22+00:00
> @MicahZoltu You can’t use v0.13 anymore.
> 
> Update both to v0.14.1.0 and it will work like expected.

Nope. I was using v0.14.1.0. (I thought that was obvious, since dEBRUYNE-1 asked me to check with v0.14.1.0 and I replied to that.) Furthermore: Our other critique was the lack of meaningful status messages - and that hasn't changed, too.

## MicahZoltu | 2019-07-18T10:59:51+00:00
I updated both to 0.14.1.0 and was _eventually_ able to connect.  Even after updating, I ran into many of the symptoms people above described, where the UI would appear to be stuck, closing would lock up the app for 10 seconds, etc.

For the curious, my problem was related to the fact that Monero GUI doesn't support SSL for its connection to the daemon and my daemon was sitting behind an SSL terminating (and redirecting) load balancer.  With useful error messages in the GUI, I would have been able to track this down relatively quickly.  Instead, I was left poking around trying to figure out where the problem was and there were many variables involved.

For example, the response to the initial request was a 302 to https of the same address.  If the GUI doesn't support https and it gets instructed to folllow a redirect to HTTPS it should present the user with an error saying as much rather than silently doing nothing.

## selsta | 2019-07-18T11:15:16+00:00
@Realchacal I didn’t reply to you?

## ghost | 2019-07-18T12:41:19+00:00
> @Realchacal I didn’t reply to you?

You said "update BOTH" - I interpreted "BOTH" as "me and him". Misunderstanding :)

## ghost | 2019-07-24T11:59:25+00:00
I'd like to add:

I'm using the default wallet mode. Switching from local node to remote node
- sometimes leads to "Waiting for daemon to stop..." but after the daemon has stopped it then says "Waiting for daemon to start..." - although I haven't clicked anything.
- sometimes triggers no daemon stopping at all, it just says network status is "Remote node", while the daemon is still running.

## selsta | 2019-07-25T05:48:05+00:00
> sometimes triggers no daemon stopping at all, it just says network status is "Remote node", while the daemon is still running.

This is the correct behaviour.

> sometimes leads to "Waiting for daemon to stop..." but after the daemon has stopped it then says "Waiting for daemon to start..." - although I haven't clicked anything.

Sounds like a bug, I’ve never experienced this. Are you pressing “Stop local node” before switching from local to remote node? Any way to reproduce?

## ghost | 2019-07-25T06:19:19+00:00
> Sounds like a bug, I’ve never experienced this. Are you pressing “Stop local node” before switching from local to remote node? Any way to reproduce?

No, but I guess it may have something to do with changing modes too quickly, which may cause the node connections to be in some "half-established" state, similar to Schrödinger's cat.


## ghost | 2019-08-20T17:59:48+00:00
- Be in Advanced mode, remote node
- Prepare a transaction on the `Send` page
- Switch to local node on the `Settings` page
- QUICKLY go back to the `Send` page
--> The `Send` button SHOULD be gray (because the daemon hasn't started yet) but ACTUALLY it's orange and you can click it (if you have been fast enough). Results in various unexpected behavior afterwards.

This is just one of many examples that show that quick node mode switching is messy. But problems also occur when you switch node modes indirectly by switching the wallet mode. IMO we need #2320 as a first step, clearer network status messages #2304, and then some forced waiting times to prevent too quick switching.

## selsta | 2020-02-13T14:38:21+00:00
This has been greatly improved in #2747

# Action History
- Created by: sanderfoobar | 2019-06-08T21:51:34+00:00
