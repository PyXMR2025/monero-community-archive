---
title: compile xmrig in linux with shared libs ... anyone ?!?!
source_url: https://github.com/xmrig/xmrig/issues/1564
author: ras2xm
assignees: []
labels:
- question
created_at: '2020-02-22T11:54:17+00:00'
updated_at: '2020-08-28T16:32:06+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:32:06+00:00'
---

# Original Description
Hi to y'all 
I want to compile xmrig with shared libs, why ? easy ... after compiling with shared libs you can take the 'exe' and run it over distributions without having to install again and again resources and compiling it on each individual machine again and again and again ... how can we do that ?

# Discussion History
## trasherdk | 2020-02-22T13:09:08+00:00
I think you got it backwards. If compiled with shared libraries, you need to have those libraries, with matching version, installed on every target machine. With static compile, you don't.

## ras2xm | 2020-02-22T15:44:24+00:00
> I think you got it backwards. If compiled with shared libraries, you need to have those libraries, with matching version, installed on every target machine. With static compile, you don't.

so what u're telling me is to compile with static ? let me tell you this : I want to make an "exe" ( xmrig ) including all libs and everything that xmr needs in order to use that "exe" on debian/ubuntu/centos without installing packets libs etc.... or to compile it on every distro everytime from scratch ... I have different machines... one is debian one is ubuntu ... centos ... one is from 2017 , another from 2018 / 2015 ....  I know it can be done but like you... there are others saying one thing and others another thing  ... not sure what to believe anymore!!!

## BlankerL | 2020-02-23T08:25:00+00:00
> > I think you got it backwards. If compiled with shared libraries, you need to have those libraries, with matching version, installed on every target machine. With static compile, you don't.
> 
> so what u're telling me is to compile with static ? let me tell you this : I want to make an "exe" ( xmrig ) including all libs and everything that xmr needs in order to use that "exe" on debian/ubuntu/centos without installing packets libs etc.... or to compile it on every distro everytime from scratch ... I have different machines... one is debian one is ubuntu ... centos ... one is from 2017 , another from 2018 / 2015 .... I know it can be done but like you... there are others saying one thing and others another thing ... not sure what to believe anymore!!!

Actually, I think what you are talking about is static compiling, so I can hardly understand why you do not accept static compiling and asking for a so-called "compiling with shared libs". Your description and explanation are just "static compiling"...

## xmrig | 2020-02-23T23:19:43+00:00
@ras2xm do advanced build on oldest system https://xmrig.com/docs/miner/ubuntu-build eg 16.04 it will likely work almost elsewhere.
Than you.

## ras2xm | 2020-03-28T12:13:27+00:00
./xmrigexe
./xmrigexe: /lib64/libc.so.6: version `GLIBC_2.14' not found (required by ./xmrigexe)
./xmrigexe: /lib64/libc.so.6: version `GLIBC_2.17' not found (required by ./xmrigexe)
so I think you did not understand what I want and that link you provided is no good , yeah it is compiling but when I change the distro from debian to centos it doesn't work it doesn't have everything in order to run it on whatever distro with the same x64 arch , and I know you can do this but ..... nevermind , if you guys DO NOT KNOW then ....

## xmrig | 2020-08-28T16:32:06+00:00
https://xmrig.com/docs/miner/build/alpine

# Action History
- Created by: ras2xm | 2020-02-22T11:54:17+00:00
- Closed at: 2020-08-28T16:32:06+00:00
