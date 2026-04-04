---
title: The problem with monerod memory consumption on Windows 7 x64
source_url: https://github.com/monero-project/monero/issues/2732
author: Raicam
assignees: []
labels:
- bug
created_at: '2017-10-27T21:03:15+00:00'
updated_at: '2025-12-19T15:31:59+00:00'
type: issue
status: closed
closed_at: '2025-12-19T15:31:59+00:00'
---

# Original Description
Hello.

There is a problem with memory consumption of monerod x64 on Windows 7 SP1 x64 system (Core2Duo 2.6Ghz / 3Gb RAM / SSD 128Gb).

When I run monerod v0.11.1.0 x64 after full synchronization and connect to it via CLI wallet, during the synchronization of the wallet itself monerod.exe consumes all the memory and then starts to consume the swap file (which causes a complete inability to work with other applications in Windows) .
It looks like this:

https://imgur.com/GEagSml

But when I try to run monerod v0.11.1.0 version x86 then there is no such problem under the same conditions!
With the x86 version, it looks like this:

https://imgur.com/NhGkf3U

What could be the problem?

# Discussion History
## moneromooo-monero | 2017-10-28T10:00:56+00:00
What is "working set" here ? Is it like resident memory, virtual memory, other ?

## Raicam | 2017-10-28T12:41:06+00:00
These readings are taken from the Process Explorer utility since the standard task manager does not show the complete data where the memory is consumed.

The column "Working Set" in this program means something like a real consumption of physical memory at the moment.

But I myself do not really understand such meanings.
Here is more detailed write here from the manual to Process Explorer - https://msdn.microsoft.com/en-us/library/cc441804(VS.85).aspx

## moneromooo-monero | 2017-10-28T13:07:42+00:00
This page says it includes memory mapped files, so that's expected (assuming the bulk of it is indeed memory mapped files). It'd need something that can report with finer granularity to determine it. If the OS can't deal with that, it may be an OS bug, or at least an OS being mediocre at it. If it's not mostly memory mapped files, then it'd be a monerod bug.

## Raicam | 2017-10-28T14:16:03+00:00
A more detailed report.

monerod x64 process:

https://imgur.com/IZfzXpK

monerod x86 process:

https://imgur.com/uZ6RtWw


In both cases monerod.exe was launched first and after a few minutes monero-wallet-cli.exe

## moneromooo-monero | 2017-10-28T15:29:19+00:00
Thanks, I think the "shareable" amount is the memory mapped (and others). So that is as expected. Your OS ought to be able to reallocate that space if necessary, and it looks like it doesn't. I'll ping hyc to comment on the difference between x86 and x86_64.

## hyc | 2017-10-28T15:40:10+00:00
On 64bit we map the entire database file as a single shared memory region. So yes, with the current blockchain size, the virtual memory size should be around 39GB, as shown here. On 32bit the OS can't map more than 2GB of shared memory, so we have to break the map into chunks, typically 64KB each.

Regardless, none of these sizes matter. Since mapping is only using virtual address space and not physical RAM, and the virtual memory size limit on a current x86_64 OS is 128TB, the actual values are irrelevant and have no impact on system performance.

Note that shared memory that is used for a memory-mapped file *never* uses swap space. If you're seeing swap usage increase, something else is the culprit.

## Raicam | 2017-10-28T18:08:32+00:00
I also noticed this behavior:

That even if you close the CLI wallet and leave monerod.exe running, then "Working Set" remains at the maximum value (equal to all free RAM) and is not unloaded.
Because of this, even if you try to open at least a simple browser (firefox) it works so slowly because of a lack of memory that the tabs open for 2-5 minutes.

If it's up to Windows 7 x64 itself, then what's wrong with it?

## dEBRUYNE-1 | 2018-01-08T12:31:21+00:00
+bug

## mmortal03 | 2018-06-15T23:37:51+00:00
I'm also seeing this behavior in v0.12.2.0 doing a monero-blockchain-import from a blockchain.raw file. (I assume the "monero-blockchain-import" executable uses somewhat comparable logic to monerod such that the bug is the same.) This is on Windows 10 64-bit, and it just keeps using more and more RAM, to the point where the swap file gets filled up and all other apps grind to a halt.

## mmortal03 | 2018-06-17T04:51:02+00:00
This issue of excessive memory consumption seems *much more* pronounced when using -db-sync-mode fastest. I think it may also be present when using "fast", but to a *much* lesser extent, and only on machines with below average amounts of RAM.

If monero-blockchain-import could dynamically control how much RAM it uses based on the system's allocation, "fastest" would probably be an advantageous setting to use. At the moment, it seems like it's got some sort of bug in its memory management causing it to not fit its name, as swapping to hard disk completely defeats the purpose. Well, at least this is the case of how it operates on Windows 64-bit. I haven't tested it in Linux yet.

## mmortal03 | 2018-06-25T22:55:42+00:00
One thing I noticed while testing this bug was that if I preemptively stopped the sync process *just ahead* of the system RAM filling up, I could then use the resume feature to restart the syncing process right where it left off, and the occupied RAM would be cleared out each time I did this. 

The problem with doing this in practice is that each time you resume it, monero-blockchain-import has to re-scan the bootstrap file in its entirety.  A feature that could make resuming faster, regardless of this bug, would be to have monero-blockchain-import detect on resume if it's using the same bootstrap raw input file as it was before to avoid re-scanning it on each subsequent resume. 

I don't know what specific information it gets from the scan of the bootstrap file, but I could see possibly caching that information to a file and then doing a quick check for no file change on each resume to save time? Just a thought to save some time if you can't do the import all in one go. It'd also be interesting to be able to disable this bootstrap file scanning for testing purposes.

## moneromooo-monero | 2018-06-27T09:14:22+00:00
Does it also happen with small versions of --batch-size ?

## mmortal03 | 2018-06-27T17:05:31+00:00
Yes, I tested a batch-size of 100 with a block-sync-size of 10, and I think I even went down to 50 and 10 on batch-size. Lowering this caused *slightly* slower RAM use growth, but it still eventually filled up the entire system RAM and started to swap to disk.

## moneromooo-monero | 2018-06-28T10:10:20+00:00
AFAIK, this is an OS bug (since I don't see actual leaks).


## ghost | 2019-06-25T18:07:31+00:00
Win7 should possibly find it's way to the "not supported" list:

https://www.microsoft.com/en-us/microsoft-365/windows/end-of-windows-7-support

Additionally, it would help to have some basic `System Requiremets` for the monero software.

# Action History
- Created by: Raicam | 2017-10-27T21:03:15+00:00
- Closed at: 2025-12-19T15:31:59+00:00
