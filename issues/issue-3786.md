---
title: Someone Breach my Computer and planted xmrig miner trojan, it slows down my
  computer or maybe stealing personal data
source_url: https://github.com/xmrig/xmrig/issues/3786
author: WENDELL509
assignees: []
labels: []
created_at: '2026-02-28T18:57:38+00:00'
updated_at: '2026-03-17T17:23:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
<img width="892" height="687" alt="Image" src="https://github.com/user-attachments/assets/f3ffe3b9-5593-47f8-9be9-51b06ad27068" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/84671c67-3980-4b24-b8a7-66527f586146" />

it automatically blocks my windows defender 

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/a1af258f-5c53-415c-b032-27f7d02e8065" />

heres the scan report of windows defender 

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/30abc84b-7cfa-4ec1-880b-35e2c18a47b1" />

how to find the root cause of this ill do everything like using cmd and system to my advantage to track down who planted this

# Discussion History
## muhammedalibilgin | 2026-03-01T07:45:46+00:00
I'm in the same situation as you.
I'm looking for a solution.
I want to find something that will catch the culprit and render all their efforts futile.

## SChernykh | 2026-03-01T08:55:47+00:00
XMRig is a miner software, not a "trojan". The real trojan is just using it. Read #3754 and #3741

## geekwilliams | 2026-03-01T19:15:57+00:00
> I want to find something that will catch the culprit and render all their efforts futile.

Unfortunately, the culprit is probably you.  Bad actors use many different ways to get onto your system, but most of them are through phishing attacks. Meaning, you probably clicked on something bad to cause malware to be installed.    

Xmrig is just mining software packaged inside the malware, and cannot "install itself".  You can try removing the executable with the xmrig icon, but it's likely that the malware will re-install it.  

The most straightforward course of action you can take is to backup necessary files, wipe the computer, and reinstall Windows. Run only trusted software, and do not download content from untrusted sources

## WENDELL509 | 2026-03-02T10:42:15+00:00
Alright guys thanks, ive read all of the comments imma nuke my pc out for now, i think its a bad idea to play whack a mole on this 


## PPPDUD | 2026-03-17T13:15:05+00:00
Hold on. You should submit whatever you got to VirusTotal before wiping your PC. It would be helpful for researchers hoping to find a solution for your issue.

## PPPDUD | 2026-03-17T13:17:25+00:00
@muhammedalibilgin Hold on. Can you check and make sure that the executable is on the same path as it is on @WENDELL509's PC?

## PPPDUD | 2026-03-17T13:23:55+00:00
It looks like this malware is related to a piece of software called hone[.]gg, which is said to behave almost exactly the same as what @WENDELL509 reports. Source: https://cheatglobal.com/konu/hone-gg-virus-suphesi.111469/

## PPPDUD | 2026-03-17T17:23:47+00:00
@WENDELL509 @muhammedalibilgin Does the description that I wrote at https://github.com/PPPDUD/malware-taxonomy/blob/main/Trojan:WinNT/wsvcz/A.md match your observations?

# Action History
- Created by: WENDELL509 | 2026-02-28T18:57:38+00:00
