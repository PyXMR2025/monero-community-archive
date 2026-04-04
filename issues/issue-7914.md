---
title: monerod failing to run
source_url: https://github.com/monero-project/monero/issues/7914
author: S1700
assignees: []
labels: []
created_at: '2021-09-01T12:07:15+00:00'
updated_at: '2021-10-03T20:32:53+00:00'
type: issue
status: closed
closed_at: '2021-10-03T20:32:53+00:00'
---

# Original Description
It's me again. When I run monerod with the command `./monerod` i get the error:
`Illegal instruction (core dumped)`

Thanks!

# Discussion History
## S1700 | 2021-09-02T13:40:36+00:00
anyone

plz help

## selsta | 2021-09-02T18:07:17+00:00
Where did you get the monerod binay?

## S1700 | 2021-09-02T18:08:23+00:00
I ran the command make and after that the file in the bin dir 

## selsta | 2021-09-02T18:16:17+00:00
Did you do it on the same computer / VPS?

## S1700 | 2021-09-03T20:08:07+00:00
yes. sorry for the late reply


## selsta | 2021-09-03T22:07:43+00:00
This message usually shows up if you compile on one system and copy the binary to a different one.

## S1700 | 2021-09-04T13:02:03+00:00
Ah alr. Thanks for the reply ill try recompiling 

## S1700 | 2021-09-04T18:23:46+00:00
Ok so i reinstalled the entire repo and remaked it and I'm still getting the same error

## selsta | 2021-09-04T19:59:53+00:00
Does the binary from getmonero.org work?

## S1700 | 2021-09-05T11:20:46+00:00
how would I get that binary onto my VPS? and test if it works because I have only used the one from here

# Action History
- Created by: S1700 | 2021-09-01T12:07:15+00:00
- Closed at: 2021-10-03T20:32:53+00:00
