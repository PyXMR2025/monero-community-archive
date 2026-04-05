---
title: Malware "Authors" using XMRig
source_url: https://github.com/xmrig/xmrig/issues/707
author: woah1337
assignees: []
labels: []
created_at: '2018-06-24T14:13:09+00:00'
updated_at: '2018-06-24T22:10:43+00:00'
type: issue
status: closed
closed_at: '2018-06-24T20:24:18+00:00'
---

# Original Description
Hi,
I have recently seen a lot of silent miners based on XMRig. This is being abused for malware, and unskilled "coders" are using command line arguments, I tried this myself and it took less than 5 minutes for me to make a silent miner. 
I read through your licence and saw nothing that forbid anyone from doing this, I do respect your licence however please consider stating that this isn't allowed for malware, people are selling this on forums such as HackForums and since it is a completely legal forum, I'm sure they will not allow people to sell malware based on your miner since it's against your rules (if you decide to change it)
Please consider this.
Thanks

# Discussion History
## kpcyrd | 2018-06-24T15:37:49+00:00
Since xmrig is GPLv3, isn't that already a copyright violation in itself? Unless the malware is GPLv3 as well? Note that such a clause might be incompatible with GPL.

## woah1337 | 2018-06-24T15:42:56+00:00
The malware is GPL as well, however when I show the licence and ask for the source code, people put unreasonable prices so no one can buy it (unreasonable compared to a compiled version)
I know that selling the source for something like a million dollars isn't allowed, but if for example a build is $8 then the source is $500 which is allowed, however no one will buy it since it takes 5 minutes to make.
I don't see anything that is stopping malware from being sold under GPL, however I am not sure.

## kpcyrd | 2018-06-24T15:48:02+00:00
The GPL requires that anybody who obtains a binary MUST be provided access to the source code for free. If you bought the binary (or it was provided for free), you could sue for the source code.

Regarding license conflicts, you might want to look into the [json license controversy][1].

[1]: https://www.gnu.org/licenses/license-list.html#JSON

## woah1337 | 2018-06-24T16:06:29+00:00
Oh I didn't know that
I read this http://prntscr.com/jyqyw5
I thought that you could price the source differently
Source - https://www.gnu.org/philosophy/selling.en.html


## Mila432 | 2018-06-24T19:51:52+00:00
wow what a great advice and then? all the bad guys will stop using this code for bad stuff , oh ya sure! go change the world

## kpcyrd | 2018-06-24T20:16:49+00:00
The selling part is referring to "compile a (modified or unmodified) version of xmrig and sell it". You're allowed to sell the binary for any price you want, but if you sell it (or distribute it for free), you need to comply with the conditions listed in [section 6].

[section 6]: https://www.gnu.org/licenses/gpl.html#section6

Basically, you need to provide the source for free as a digital copy, or as a physical copy "for a price no more than your reasonable cost of physically performing this conveying of source".

If you have the binary, it's your right to get the source code with no addition fee. This condition is the major reason why the GPL was written in the first place.

Basically, if you can expect a platform to care about a "not for use in malware" clause (which is very weakly defined), you could also expect that platform to care about basic copyright laws, since they are distributing pirated software if the author is including source code that is only allowed to be used if all conditions of the license are fulfilled.

## woah1337 | 2018-06-24T20:18:16+00:00
@Mila432 It certainly won't stop anyone from using this for malware, however it will definitely stop people from selling modified XMrig based miners on public forums, and the script kiddies won't have anything to mine with.
Therefore, there will be lesser skids that make botnets and buy XMrig to mine.
Thank you @kpcyrd I think I am going to close this issue now as it doesn't seem possible.
I only opened this because XMrig was becoming a selling point in many silent miners, instead of "coded from scratch".


## kpcyrd | 2018-06-24T21:04:50+00:00
@woah1337 if this is an issue you care about, you could inform the administrators about those copyright violations which would result in either:

- a takedown of the offer
- a change to the offer so the full source code is included in the $8 price, as required by the GPL
- legal issues for the administrators for knowingly tolerating pirated software on their platform

## woah1337 | 2018-06-24T22:01:29+00:00
@kpcyrd that's what I am going to do right now.
I will buy a couple of reputed miners and ask for the source code (and publish it on Github with the GPL).
It might temporarily spike XMrig malware activity but eventually people will stop selling it.
It's not like I am trying to stop malware, there are people that take 5 minutes "coding" something like this, sign up on a public forum and try to sell it. 

# Action History
- Created by: woah1337 | 2018-06-24T14:13:09+00:00
- Closed at: 2018-06-24T20:24:18+00:00
