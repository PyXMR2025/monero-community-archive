---
title: Raw blockchain + autodownload/autoload
source_url: https://github.com/monero-project/monero/issues/87
author: fluffypony
assignees: []
labels: []
created_at: '2014-08-05T18:39:53+00:00'
updated_at: '2015-03-26T14:59:53+00:00'
type: issue
status: closed
closed_at: '2015-03-26T14:59:53+00:00'
---

# Original Description
Two things are needed:
1. A CLI flag for the daemon that will allow a 'blockchain.raw' file to be created and used in parallel with the normal blockchain. This raw blockchain should just be a flat, serialised copy of every block in existence. If the daemon is started with this flag and this file does not exist, it should be created based on the existing blockchain (using the standard blockchain functions so that it still works when we move to an embedded db). It should be kept in-sync - when the blockchain is periodically written to disk, this file should be added to too.
2. Once that is complete, a new function is that when the daemon is started for the first time in interactive mode (see: @mikezackles daemonize branch for when this won't happen) it should prompt to bootstrap the blockchain from downloads.monero.cc. The daemon can also be started with a --bootstrap-blockchain flag that will do this if no local blockchain is found. The daemon can also check for the existence of blockchain.raw in its working folder, which is an indicator to auto-import it. In all three cases, if the user wants to download the bootstrap, it should download it from a set URL (to be confirmed) over HTTP, with resume if the download stalls or the daemon crashes and is restarted with this option enabled / prompt shown and user answers yes, and download progress should be shown as it proceeds. VERY NB: as it downloads (OR as it is read off disk, if it exists locally) it should be read/downloaded in chunks that are deserialised, with each block being verified and added to the regular blockchain storage. It should not be read/downloaded into RAM whole and then worked with, as the regular blockchain already does that, so it will exhaust RAM on most boxes. In order to keep this consistent between sessions (eg. if the daemon is killed halfway through) a state file should temporarily be stored in the working folder that indicates the byte position and block height of the last chunk successfully imported. I think it should chunk -> import -> chunk -> import rather than trying to get clever and do it multi-threaded. We'll get clever later:)


# Discussion History
## fluffypony | 2015-02-03T18:08:06+00:00
@warptangent picked up to finish what konmanto had nearly completed


## fluffypony | 2015-03-26T14:59:53+00:00
Completed and merged into blockchainDB


# Action History
- Created by: fluffypony | 2014-08-05T18:39:53+00:00
- Closed at: 2015-03-26T14:59:53+00:00
