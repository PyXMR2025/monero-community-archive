---
title: 'monero_blockchain_import: "Block verification failed"'
source_url: https://github.com/monero-project/monero/issues/7458
author: xmrdog
assignees: []
labels: []
created_at: '2021-03-07T08:34:52+00:00'
updated_at: '2021-03-24T13:33:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am using `v0.17.1.9` on Linux. I did these steps:

1. Exit all Monero programs, including the daemon.
2. `./monero_blockchain_export --output-file=/somewhere/foo.raw`.
3. Remove the blockchain directory `.bitmonero` (over 100 GB of data).
4. `./monero_blockchain_import --input-file=/somewhere/foo.raw`
5. Wait for many hours.

I end up with this error:

    E Block verification failed, id = 03a426e085198057bf6bf267fb6cf14ee5dc2a402e47f4a135395bb78ce01d3d
    I Number of blocks imported: 2268158
    I Finished at block: 2268159  total blocks: 2268160

Since block `2268159` is from 2 months ago (2021-01-05), this made me think that the blockchain might be corrupted at this point, and therefore nothing more was imported.

So after the import shown above, I resynced the last 2 months using `./monerod`.

**Strangest thing:** If I now repeat the above steps again, I end up with **exactly the same error at exactly the same block**!

Can someone here reproduce this error? What could be the issue?

# Discussion History
## moneromooo-monero | 2021-03-07T09:25:10+00:00
Why is it strange it would not do the same ?
The issue seems to be the data is bad, as you said.

## xmrdog | 2021-03-07T11:26:01+00:00
@moneromooo-monero There appears to be some misunderstanding. I said it's strange that the error *does* occur at exactly the same block for these reasons:

1. Doesn't `./monero_blockchain_import` import only valid data into `~/.bitmonero`, discarding bad data?
2. So shouldn't syncing from there (i.e., syncing the last 2 months) "fix" those errors?

That's why I think it's strange that the same error reoccurred.

Am I missing something obvious?

## moneromooo-monero | 2021-03-07T21:41:43+00:00
Oh, it's data you exported yourself, I glossed over that. So it should be valid, as opposed to something you got from the internet. There's either a bug in the exporter, or your blockchain is corrupted. The block hash the error references does not exist on the chain. Does your daemon find it with:

> print_block 03a426e085198057bf6bf267fb6cf14ee5dc2a402e47f4a135395bb78ce01d3d

Also, post the output of:

> print_block 2268158 +hex
> print_block 2268159 +hex

## xmrdog | 2021-03-08T13:18:18+00:00
@moneromooo-monero Hi, here is all your desired output (encrypted with your pgp key):

```
-----BEGIN PGP MESSAGE-----

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
9nbPdw==
=QwUD
-----END PGP MESSAGE-----

```

## moneromooo-monero | 2021-03-08T17:35:17+00:00
This was public data btw :)

## moneromooo-monero | 2021-03-08T17:55:42+00:00
I think the message is wrong about the block hash. Please apply this patch:

https://paste.debian.net/hidden/6aca4cb8/

Then run:

> monero-blockchain-export --log-level 2 --block-start 2268155 --block-stop 2268160

We should see if there are any errors on export.

## xmrdog | 2021-03-08T20:30:43+00:00
@moneromooo-monero I see no errors at all:
```
2021-03-08 20:26:21.203	W Source blockchain storage initialized OK
2021-03-08 20:26:21.203	W Exporting blockchain raw data...
2021-03-08 20:26:21.203	I Storing blocks raw data...
2021-03-08 20:26:21.203	I source blockchain height: 2312520
2021-03-08 20:26:21.204	I Using requested block height: 2268160
2021-03-08 20:26:21.204	D creating file
2021-03-08 20:26:21.210	D bootstrap::file_info size: 4
2021-03-08 20:26:21.210	D bootstrap::blocks_info size: 9
2021-03-08 20:26:21.210	I Starting block height: 2268155
2021-03-08 20:26:21.210	I block hash at 2268155: <e6577bcf7ea0237aaf9b3140d074dab464b91bb04b76526432305cd3b4af8e45>
2021-03-08 20:26:21.219	I Calculated block hash <e6577bcf7ea0237aaf9b3140d074dab464b91bb04b76526432305cd3b4af8e45>
2021-03-08 20:26:21.243	D flushed chunk:  chunk_size: 9127
2021-03-08 20:26:21.243	I block hash at 2268156: <7f93bb7df58857e91f4501788d5e0eb72d31a4a792657d1b51b3655796c946a3>
2021-03-08 20:26:21.246	I Calculated block hash <7f93bb7df58857e91f4501788d5e0eb72d31a4a792657d1b51b3655796c946a3>
2021-03-08 20:26:21.332	D flushed chunk:  chunk_size: 51528
2021-03-08 20:26:21.332	I block hash at 2268157: <015e77bf0ff807420cdbca04d110cbc6de1a07068a14a5b3619f57678153335d>
2021-03-08 20:26:21.333	I Calculated block hash <015e77bf0ff807420cdbca04d110cbc6de1a07068a14a5b3619f57678153335d>
2021-03-08 20:26:21.375	D flushed chunk:  chunk_size: 24005
2021-03-08 20:26:21.375	I block hash at 2268158: <0f5363222750acc5e09b4cc8edbe2fd8b7da3f46725ffd11d3cab69f0b6a3451>
2021-03-08 20:26:21.378	I Calculated block hash <0f5363222750acc5e09b4cc8edbe2fd8b7da3f46725ffd11d3cab69f0b6a3451>
2021-03-08 20:26:21.596	D flushed chunk:  chunk_size: 149789
2021-03-08 20:26:21.596	I block hash at 2268159: <1d23d62d8c474c70bf2de03546a05ea2826ac5ffff9a5f9c2f55af37e3ab78b9>
2021-03-08 20:26:21.598	I Calculated block hash <1d23d62d8c474c70bf2de03546a05ea2826ac5ffff9a5f9c2f55af37e3ab78b9>
2021-03-08 20:26:21.788	D flushed chunk:  chunk_size: 190418
2021-03-08 20:26:21.788	I block hash at 2268160: <53e95e40886b5203a1b1cc25513af6d64b0716ebe25c690688fd1cc92a37d11a>
2021-03-08 20:26:21.790	I Calculated block hash <53e95e40886b5203a1b1cc25513af6d64b0716ebe25c690688fd1cc92a37d11a>
2021-03-08 20:26:21.832	D flushed chunk:  chunk_size: 29739
block 2268160/2268160               
2021-03-08 20:26:21.832	I Number of blocks exported: 6
2021-03-08 20:26:21.832	I Largest chunk: 190418 bytes
2021-03-08 20:26:21.832	W Blockchain raw data exported OK
```

## xmrdog | 2021-03-08T20:32:53+00:00
@moneromooo-monero Even ending a bit later, at `--block-stop 2268165`, gives no error either:

```
2021-03-08 20:31:38.442	W Source blockchain storage initialized OK
2021-03-08 20:31:38.442	W Exporting blockchain raw data...
2021-03-08 20:31:38.442	I Storing blocks raw data...
2021-03-08 20:31:38.442	I source blockchain height: 2312520
2021-03-08 20:31:38.442	I Using requested block height: 2268165
2021-03-08 20:31:38.442	D creating file
2021-03-08 20:31:38.443	D bootstrap::file_info size: 4
2021-03-08 20:31:38.443	D bootstrap::blocks_info size: 9
2021-03-08 20:31:38.443	I Starting block height: 2268155
2021-03-08 20:31:38.443	I block hash at 2268155: <e6577bcf7ea0237aaf9b3140d074dab464b91bb04b76526432305cd3b4af8e45>
2021-03-08 20:31:38.443	I Calculated block hash <e6577bcf7ea0237aaf9b3140d074dab464b91bb04b76526432305cd3b4af8e45>
2021-03-08 20:31:38.445	D flushed chunk:  chunk_size: 9127
2021-03-08 20:31:38.445	I block hash at 2268156: <7f93bb7df58857e91f4501788d5e0eb72d31a4a792657d1b51b3655796c946a3>
2021-03-08 20:31:38.445	I Calculated block hash <7f93bb7df58857e91f4501788d5e0eb72d31a4a792657d1b51b3655796c946a3>
2021-03-08 20:31:38.457	D flushed chunk:  chunk_size: 51528
2021-03-08 20:31:38.457	I block hash at 2268157: <015e77bf0ff807420cdbca04d110cbc6de1a07068a14a5b3619f57678153335d>
2021-03-08 20:31:38.457	I Calculated block hash <015e77bf0ff807420cdbca04d110cbc6de1a07068a14a5b3619f57678153335d>
2021-03-08 20:31:38.463	D flushed chunk:  chunk_size: 24005
2021-03-08 20:31:38.463	I block hash at 2268158: <0f5363222750acc5e09b4cc8edbe2fd8b7da3f46725ffd11d3cab69f0b6a3451>
2021-03-08 20:31:38.463	I Calculated block hash <0f5363222750acc5e09b4cc8edbe2fd8b7da3f46725ffd11d3cab69f0b6a3451>
2021-03-08 20:31:38.496	D flushed chunk:  chunk_size: 149789
2021-03-08 20:31:38.496	I block hash at 2268159: <1d23d62d8c474c70bf2de03546a05ea2826ac5ffff9a5f9c2f55af37e3ab78b9>
2021-03-08 20:31:38.497	I Calculated block hash <1d23d62d8c474c70bf2de03546a05ea2826ac5ffff9a5f9c2f55af37e3ab78b9>
2021-03-08 20:31:38.531	D flushed chunk:  chunk_size: 190418
2021-03-08 20:31:38.531	I block hash at 2268160: <53e95e40886b5203a1b1cc25513af6d64b0716ebe25c690688fd1cc92a37d11a>
2021-03-08 20:31:38.531	I Calculated block hash <53e95e40886b5203a1b1cc25513af6d64b0716ebe25c690688fd1cc92a37d11a>
2021-03-08 20:31:38.538	D flushed chunk:  chunk_size: 29739
2021-03-08 20:31:38.538	I block hash at 2268161: <863275326f18668d44aeb74346481f91f2e670261c3dc5d10ccda2df650d5515>
2021-03-08 20:31:38.542	I Calculated block hash <863275326f18668d44aeb74346481f91f2e670261c3dc5d10ccda2df650d5515>
2021-03-08 20:31:38.542	D flushed chunk:  chunk_size: 162
2021-03-08 20:31:38.542	I block hash at 2268162: <ae6b38ea513dfb289c917ab0049f70bf18a0e52533f2c841d800e438eef5205d>
2021-03-08 20:31:38.543	I Calculated block hash <ae6b38ea513dfb289c917ab0049f70bf18a0e52533f2c841d800e438eef5205d>
2021-03-08 20:31:38.549	D flushed chunk:  chunk_size: 6168
2021-03-08 20:31:38.549	I block hash at 2268163: <b146fe44bc367de27b48eec65cf409ba15fbd84e66bcfebb974eaa5313d8720d>
2021-03-08 20:31:38.551	I Calculated block hash <b146fe44bc367de27b48eec65cf409ba15fbd84e66bcfebb974eaa5313d8720d>
2021-03-08 20:31:38.684	D flushed chunk:  chunk_size: 106363
2021-03-08 20:31:38.684	I block hash at 2268164: <fe1be5ed149f3ad4ef0ee6d3245df67ca02b3e6a132d1b03a2a251c4f3e7fae7>
2021-03-08 20:31:38.687	I Calculated block hash <fe1be5ed149f3ad4ef0ee6d3245df67ca02b3e6a132d1b03a2a251c4f3e7fae7>
2021-03-08 20:31:38.724	D flushed chunk:  chunk_size: 27797
2021-03-08 20:31:38.724	I block hash at 2268165: <3ac21fb7df6dce2dbaf1dd17c4e976882eea34c39082b5a81694fbb4ba051c94>
2021-03-08 20:31:38.727	I Calculated block hash <3ac21fb7df6dce2dbaf1dd17c4e976882eea34c39082b5a81694fbb4ba051c94>
2021-03-08 20:31:38.908	D flushed chunk:  chunk_size: 163911
block 2268165/2268165               
2021-03-08 20:31:38.908	I Number of blocks exported: 11
2021-03-08 20:31:38.908	I Largest chunk: 190418 bytes
2021-03-08 20:31:38.908	W Blockchain raw data exported OK
```

## xmrdog | 2021-03-08T20:38:34+00:00
However, importing this small file runs without errors. So now I'm confused and wonder what was wrong with my larger file...

## moneromooo-monero | 2021-03-08T21:47:53+00:00
Well, we're left with "run it again, but import with log level 2". I originally thought the problem was the bad block hash (ie, bad data in the file), but I now think it's a red herring, so let's see what error happens in verification.

## xmrdog | 2021-03-10T06:59:50+00:00
@moneromooo-monero 

1. Sure, I can I run `monero-blockchain-import` as before. Should I do this with or without your earlier patch?
2. In any case, can you make me a separate patch that internally activates the log level 2 only after we have gotten closer to the failing block? For instance, activate it at block `2268000`. (At least with your earlier patch, log level 2 is increasing my import time from hours to days.)

## moneromooo-monero | 2021-03-11T00:35:14+00:00
This should do it:
```
diff --git a/src/cryptonote_core/blockchain.cpp b/src/cryptonote_core/blockchain.cpp
index 17c6801ed..bb6d756d5 100644
--- a/src/cryptonote_core/blockchain.cpp
+++ b/src/cryptonote_core/blockchain.cpp
@@ -4621,6 +4621,7 @@ leave:
         << t1 << "/" << t2 << "/" << t3 << "/" << t_exists << "/" << t_pool
         << "/" << t_checktx << "/" << t_dblspnd << "/" << vmt << "/" << addblock << ")ms");
   }
+if (new_height >= 2268000) mlog_set_log_level(2);
 
   bvc.m_added_to_main_chain = true;
   ++m_sync_counter;
```

Run with or without the patch, it doesn't matter now. 

## xmrdog | 2021-03-11T20:05:33+00:00
@moneromooo-monero 

Thanks for that last patch. It worked great. The original error is now fully reproduced, this time with the log-level 2 activating well before the error occurs. I've attached the LOG file (encrypted with your PGP key). Does this tell you anything?

[monero-blockchain-import.log.gpg.zip](https://github.com/monero-project/monero/files/6125690/monero-blockchain-import.log.gpg.zip)



## moneromooo-monero | 2021-03-12T16:20:47+00:00
That log does not include the error with log level 2, see:

> 2021-03-11 17:18:57.449     7fa27f6d0bc0        ERROR   bcutil  src/blockchain_utilities/blockchain_import.cpp:196      Block verification failed,

That's the error, but it's the previous run. Last run starts half an hour later:

> 2021-03-11 17:56:43.625     7fa27f6d0bc0        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:DEBUG

But this does not error out.

## xmrdog | 2021-03-22T19:52:53+00:00
@moneromooo-monero Hey, sorry for the delay. I have recreated the log now (encrypted with your PGP key), this time after first deleting any existing one. (Just to recap, it's using your custom patched import binary which only starts log-level 2 beyond a certain point.)

You will see the error reproduced. Does this help you identify the problem?

[monero-blockchain-import.log.asc.zip](https://github.com/monero-project/monero/files/6184943/monero-blockchain-import.log.asc.zip)


## moneromooo-monero | 2021-03-23T10:58:19+00:00
There's no level 2 logs in there, so I guess the block at which it switches is too late.

# Action History
- Created by: xmrdog | 2021-03-07T08:34:52+00:00
