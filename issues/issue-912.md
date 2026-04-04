---
title: Signup for Coverity Scan
source_url: https://github.com/monero-project/monero/issues/912
author: anonimal
assignees: []
labels:
- proposal
created_at: '2016-07-13T22:00:49+00:00'
updated_at: '2018-02-14T08:41:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As discussed in IRC with @moneromooo-monero, if repo owner [signs up for Coverity via GitHub](https://scan.coverity.com/github/authorize), I (or anyone with permissions) can get a scan uploaded in no time. The process of scanning _can_ be automated with Travis-CI but [it doesn't quite work at the moment for Kovri](https://github.com/travis-ci/travis-ci/issues/6274) - though it may work for bitmonero without issue. Manually uploading works well and [Kovri's scan passes](https://scan.coverity.com/projects/7621/) (status-badge also available in [README.md](https://github.com/monero-project/kovri/blob/master/README.md)).

What I _can_ do now is start the process in my fork and also tinker with Travis-CI/Coverity integration. If either components works, then I'll PR.  I only ask for feedback to see if Coverity is something of interest and, if so, I'll spend the time needed to pursue this.


# Discussion History
## anonimal | 2016-07-26T18:32:14+00:00
I've taken the liberty to start this within my fork. Results can be viewed [here](https://scan.coverity.com/projects/anonimal-bitmonero?tab=overview). I've given @moneromooo-monero ownership permissions so they should be able to invite other developers to view defects. If not, then ping me with an email and I will send an invite **Edit:** or you can request an invite on the site.


## anonimal | 2016-12-14T00:26:27+00:00
Referencing monero-project/meta#19. I'd like to get the scan out of my fork and into `monero-project` once automation gets going.

## dEBRUYNE-1 | 2018-01-08T12:35:48+00:00
+proposal

## hyc | 2018-02-11T22:01:11+00:00
I've seen that we have patches resulting from Coverity scans now. Is this issue now resolved?

## anonimal | 2018-02-12T22:08:00+00:00
Nope. I'm still pushing the builds from my repo. I've given moo coverity privileges and he's invited others to review the results so I think that's what's happening here though I'm not sure.

In hindsight, this issue may no longer be and issues because:

- I don't have a problem keeping up with the coverity build
- this is still unresolved https://github.com/monero-project/meta/issues/19
- luigi and fluffy are usually too busy to keep up with things like this so it's better to have someone actively involved such as myself
- keeps up with the decentralization

I do like less work though but not if doing so will result in coverity cobwebs.

## moneromooo-monero | 2018-02-13T10:53:55+00:00
> I think that's what's happening here though I'm not sure

I've been using anonimal's coverity builds. I don't remember adding anyone though, I did not know I could.


## anonimal | 2018-02-14T06:52:45+00:00
>I don't remember adding anyone though, I did not know I could.

Oh my, this is odd then. There are 8 members of which I did not invite but they somehow have defect view privileges. The only other person with elevated privileges is @danrmiller, did he invite them? If not, how are they acquiring invite-only privs?...

## anonimal | 2018-02-14T06:55:22+00:00
@stoffu how did you acquire privs to anonimal/monero on coverity? I see that you joined on Feb 12th, 2018.

## stoffu | 2018-02-14T07:17:38+00:00
Actually I had no idea about Coverity until recently when @moneromooo-monero made a few patches regarding Coverity. I just got curious and clicked this link https://scan.coverity.com/projects/9657/ on README.md, and then clicked a button that said 'subscribe' or 'join' (I don't remember well), and then I chose a member status option as something like 'reading member'.

Sorry for carelessly clicking buttons :P

## anonimal | 2018-02-14T08:41:44+00:00
>and then I chose a member status option as something like 'reading member'.

Oh, then apparently coverity changed their guidelines / setup without sending any notification. Back in the day, to even view meant invite only.

# Action History
- Created by: anonimal | 2016-07-13T22:00:49+00:00
