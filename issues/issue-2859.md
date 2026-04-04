---
title: '[Feature] Add option to export multisig data to ASCII (e.g. text file)'
source_url: https://github.com/monero-project/monero/issues/2859
author: dEBRUYNE-1
assignees: []
labels:
- proposal
created_at: '2017-11-24T12:13:03+00:00'
updated_at: '2019-09-03T14:36:21+00:00'
type: issue
status: closed
closed_at: '2019-09-03T14:36:21+00:00'
---

# Original Description
Currently the following commands write to a file:

`export_multisig_info`
`sign_multisig` 

In addition, both `import_multisig_info` and `submit_multisig` will look for a file. Now imagine a 2/3 multisig case where buyer, seller, and arbitrator don't trust each other. It's highly unlikely that they would download files from each other. An elegant solution would be to export multisig data to ASCII (e.g. to a text file) such that the participants can simply paste their data and subsequently import it. More specifically, wallet A could post the output of `export_multisig_info` on https://paste.fedoraproject.org. Subsequently, wallet B could grab the data, save it to a text file, and lastly import it. 

For convenience, it might be easy to add intuitive multisig commands for this. For instance:

`export_multisig_info_txt`
`import_multisig_info_txt`
`sign_multisig_txt`
`submit_multisg_txt`

# Discussion History
## moneromooo-monero | 2017-11-24T12:18:54+00:00
I'm planning on adding a "set export-format raw hex" which will take care of this.
This will work also for other stuff like the cold signing info.
Loading will autodetect which format is used.

## stoffu | 2017-11-24T12:36:28+00:00
Just a minor comment: the file-less data exchange is already what it is for the RPC mode, and I experienced using the standard terminal on OSX that pasting the long hex string for the (partially signed or fully signed) tx takes quite long, at least a few minutes.

Also, I don't see the difference trustedness-wise between passing the data directly as text vs file download/attachment. If a participant gave some fake data, the end effect is simply that the resulting signature doesn't check.

## moneromooo-monero | 2017-11-24T14:37:32+00:00
It's just about ease of handling, not difference in trust. Sending raw data will end up with possible corruption as people copy/paste, if they don't use files. And we can't really tell people to use the RPC wallet for this.

## dEBRUYNE-1 | 2018-01-08T12:39:03+00:00
+proposal

## tmoravec | 2019-01-13T12:21:20+00:00
I'm going to try to implement this.

## saloppe73 | 2019-02-24T15:51:01+00:00
It would help if the output of wallet-cli export/import multisig-data are additional in hex like wallet-rpc. In case of 2/3 when alice and bob use wallet-cli and charly use wallet-rpc there is no way - or did I miss(understand) something?

## ajs-xmr | 2019-03-27T05:55:29+00:00
@moneromooo-monero being able to review the contents of `multisig_monero_tx` in raw hex/json would be very helpful, especially when dealing with multiple transactions to know which file is what by opening a text editor.

## vtnerd | 2019-04-12T20:48:01+00:00
 I commented in the PR too, but using the `base64` program will achieve the same thing - ?

## tmoravec | 2019-09-03T07:45:44+00:00
Implemented.

## dEBRUYNE-1 | 2019-09-03T14:36:21+00:00
Yes, thanks a lot. Will close this issue. 

# Action History
- Created by: dEBRUYNE-1 | 2017-11-24T12:13:03+00:00
- Closed at: 2019-09-03T14:36:21+00:00
