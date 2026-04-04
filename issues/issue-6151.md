---
title: Wrong hashes (from getmonero.org)
source_url: https://github.com/monero-project/monero/issues/6151
author: nikitasius
assignees: []
labels: []
created_at: '2019-11-18T16:21:07+00:00'
updated_at: '2019-12-04T19:09:34+00:00'
type: issue
status: closed
closed_at: '2019-12-04T19:09:34+00:00'
---

# Original Description
I downloaded: 
* https://dlsrc.getmonero.org/cli/monero-linux-x64-v0.15.0.0.tar.bz2  (https://web.getmonero.org/downloads/#linux)
* https://downloads.getmonero.org/cli/monero-linux-x64-v0.15.0.0.tar.bz2 (https://github.com/monero-project/monero/releases)

website say:
![image](https://user-images.githubusercontent.com/3670331/69068260-be897000-0a24-11ea-91d3-ecb14e2406c7.png)

Check sha256 and see this (only github's matches hashsum):

- 53d9da55137f83b1e7571aef090b0784d9f04a980115b5c391455374729393f3  monero-linux-x64-v0.15.0.0-github.tar.bz2
- b99009d2e47989262c23f7277808f7bb0115075e7467061d54fd80c51a22e63d  monero-linux-x64-v0.15.0.0-site.tar.bz2


I look inside:

### monero-linux-x64-v0.15.0.0-github
- 0d8e612321fac7acef02fc5024029663bd7831de8cd24ae980c59e6e6e77b2b8  LICENSE
- 2b05482894fae937a13f8b84209c6006cd1144db0205fa7ea6da0b82023e1b39  monero-blockchain-ancestry
- 2eb0087115b2d125987334158f7946b18c6c6a2abe33662164c6a95fe564fde1  monero-blockchain-depth
- ee7577d8f53485df902d8f706e3a1837a8a9e1add12f468bdfce52b93d74fc21  monero-blockchain-export
- f863333d2e6e7d283380a0a2bc9b128485020da63776317347144ecbabd5e9d5  monero-blockchain-import
- 2db50fc7cbaa15f8322ac2d5a27ac3e75dadd23cb32cacc9f2bd2097d741db39  monero-blockchain-mark-spent-outputs
- 14565c45fc6bd169ec1d94cb1a5b81bbac6ced59acabc264d360a34941a502ae  monero-blockchain-prune
- 06177f7cd37a4878e5af2d79a75b48ec5c0492cc66e911ee416bfd8962a865df  monero-blockchain-prune-known-spent-data
- a252531b84668e354ca36e1f12375ce3bdcb7061d81e76f0df736807c4ed77f0  monero-blockchain-stats
- 9fb26f5587f69cf85c9d548041b81e98590ec8c42ac5ff79b5421fcf02c0fcb4  monero-blockchain-usage
- b3f9ea5f196a9a67ae137b6c1f6916ff0c0cc836c1a225c96fe73d5ce50d1fed  monerod
- a9de252a6f5409aa33fddb557071fb3a17ab7fc4c9e23e0e10494761f1aa2c6a  monero-gen-ssl-cert
- bd1053ba7a1ecfece1676b294433a6b161049730c1ed9a566e762f6b3812a086  monero-gen-trusted-multisig
- **5decc690a63aab004bae261630980e631b9d37a0271bbe0c5b477feffcd3f8c2  monero-wallet-cli**
- 7fb80cec9b4a33051d47e228eeedf001faa376b93c9c7f1ecc9280dc9dab9225  monero-wallet-rpc

### monero-linux-x64-v0.15.0.0-site
- 0d8e612321fac7acef02fc5024029663bd7831de8cd24ae980c59e6e6e77b2b8  LICENSE
- 2b05482894fae937a13f8b84209c6006cd1144db0205fa7ea6da0b82023e1b39  monero-blockchain-ancestry
- 2eb0087115b2d125987334158f7946b18c6c6a2abe33662164c6a95fe564fde1  monero-blockchain-depth
- ee7577d8f53485df902d8f706e3a1837a8a9e1add12f468bdfce52b93d74fc21  monero-blockchain-export
- f863333d2e6e7d283380a0a2bc9b128485020da63776317347144ecbabd5e9d5  monero-blockchain-import
- 2db50fc7cbaa15f8322ac2d5a27ac3e75dadd23cb32cacc9f2bd2097d741db39  monero-blockchain-mark-spent-outputs
- 14565c45fc6bd169ec1d94cb1a5b81bbac6ced59acabc264d360a34941a502ae  monero-blockchain-prune
- 06177f7cd37a4878e5af2d79a75b48ec5c0492cc66e911ee416bfd8962a865df  monero-blockchain-prune-known-spent-data
- a252531b84668e354ca36e1f12375ce3bdcb7061d81e76f0df736807c4ed77f0  monero-blockchain-stats
- 9fb26f5587f69cf85c9d548041b81e98590ec8c42ac5ff79b5421fcf02c0fcb4  monero-blockchain-usage
- b3f9ea5f196a9a67ae137b6c1f6916ff0c0cc836c1a225c96fe73d5ce50d1fed  monerod
- a9de252a6f5409aa33fddb557071fb3a17ab7fc4c9e23e0e10494761f1aa2c6a  monero-gen-ssl-cert
- bd1053ba7a1ecfece1676b294433a6b161049730c1ed9a566e762f6b3812a086  monero-gen-trusted-multisig
- **7ab9afbc5f9a1df687558d570192fbfe9e085712657d2cfa5524f2c8caccca31  monero-wallet-cli**
- 7fb80cec9b4a33051d47e228eeedf001faa376b93c9c7f1ecc9280dc9dab9225  monero-wallet-rpc


### Why `monero-wallet-cli` are different in those 2 releases?

# Discussion History
## selsta | 2019-11-18T16:26:55+00:00
I can confirm, hash doesn’t match.

## sedited | 2019-11-18T16:31:34+00:00
The 53d9d... hash was verified independently in the gitian sigs repo and seems to be the correct one: https://github.com/monero-project/gitian.sigs/blob/master/v0.15.0.0-linux/hyc/monero-linux-0.15-build.assert#L6 .

## selsta | 2019-11-18T16:44:41+00:00
Issue should be fixed now, hyc is looking at the bad binary.

## nikitasius | 2019-11-18T18:14:36+00:00
yep it's correct now.

## trasherdk | 2019-11-18T19:00:20+00:00
So. Do I need to do a recompile/redeploy while waiting for 15.0.1 ?
My version is Monero `Carbon Chamaeleon' (v0.15.0.0-69c488a47)`

## selsta | 2019-11-18T19:04:48+00:00
> My version is Monero Carbon Chamaeleon' (v0.15.0.0-69c488a47)

Looks good, no need to recompile.

## trasherdk | 2019-11-18T19:21:43+00:00
Well. Compared, something changed:

***A few minutes ago***
```
$ sha1sum monero-v0.15.0.0/monerod 
e32220114d0c57886d16e50ac858edf9b1b22872  monero-v0.15.0.0/monerod
```
Compared to:
***2-3 days ago***
```
$ sha1sum ../build-monero-pool/usr/bin/monerod 
801706e2396d1a88475b5535247155ec147ae25c  ../build-monero-pool/usr/bin/monerod
```
Both are off clean `git clone`. Why are they not the same?

## selsta | 2019-11-18T19:30:58+00:00
Normal builds are not guaranteed to be deterministic. This issue here is about the getmonero.org download, not self compiled binaries.

## nikitasius | 2019-11-18T19:34:29+00:00
@trasherdk @selsta so.. still an issue (for old users), i keep it open? 

## trasherdk | 2019-11-18T19:50:34+00:00
I do realize that, your deterministic build environment, is very different from mine.
Doing a new clone/build of the `pool` version, tells me that I have to take another look at the build scripts.
Rebuilding both still yields different (same as before) results.
At least they match the previous results :)
```
$ sha1sum monero-v0.15.0.0/monerod             
e32220114d0c57886d16e50ac858edf9b1b22872  monero-v0.15.0.0/monerod
$ sha1sum ../build-monero-pool/usr/bin/monerod 
801706e2396d1a88475b5535247155ec147ae25c  ../build-monero-pool/usr/bin/monerod
```


## selsta | 2019-11-18T20:01:12+00:00
@trasherdk monero does support reproducible builds, see https://github.com/monero-project/monero/tree/master/contrib/gitian

## trasherdk | 2019-11-18T20:09:12+00:00
@selsta Yes, I know. But I'm not about to change my servers to Debian, just to build a Monero.
All my servers are running `Slackware x64 14.2`. I know. Old school, but that's what I like.

## scottAnselmo | 2019-11-19T05:41:07+00:00
Is there a copy of the bad binary somewhere for anyone else to investigate by downloading onto a VM and decompiling?

## selsta | 2019-11-19T05:53:39+00:00
https://reddit.com/r/Monero/comments/dyfozs/security_warning_cli_binaries_available_on/

## scottAnselmo | 2019-11-19T06:37:34+00:00
Per u/gingeropolous's [Reddit comment ](https://www.reddit.com/r/Monero/comments/dyfozs/security_warning_cli_binaries_available_on/f8107ji/) which is basically a pastebin of a userpost not going through on Reddit from u/moneromanz, old binary is indeed malicious and not just a fluke of the build process or some bad copy/paste of the checksum onto the website. serhack, a professional investigator, is looking into it. [Paste bin](https://paste.fedoraproject.org/paste/5sNieWLBYFzvMG-LKtp0lg/raw):

```
I can confirm that the malicious binary is stealing coins. Roughly 9 hours after I ran the binary a single transaction drained the wallet. I downloaded the build yesterday around 6pm Pacific time.

$ sha256sum 'monero_wallet_cli' produces:

7ab9afbc5f9a1df687558d570192fbfe9e085712657d2cfa5524f2c8caccca31

$ monero_wallet_cli --version produces:

Monero 'Carbon Chamaeleon' (v0.15.0.0-f07c326f1)

DO NOT RUN THE BINARY TO CHECK THE VERSION

It seems the attacker forked from commit f07c326f1 in the public repo.

I cross checked the individual binaries in the malicious tar file to a newly downloaded tar file (linux x64), and only the binary monero_wallet_cli has a different hash. I've uploaded the binary here.

https://anonfile.com/bbq8h9Bdn7/monero-wallet-cli

I have not completed any malware analysis as of yet, but I'd like to get to the bottom of whether the binary is limited to stealing xmr, or also tries to compromise the machine as a whole or any of its files. Any assistance analyzing he binary above would be appreciated!
```

## jindouyunz | 2019-11-19T07:56:41+00:00
There is a Monero community member from China suggests that networks cause this problem.
He tried downloading CLI with 2 computers yesterday, but all found that the hashes don't match.
Then he relay the file with a Hongkong server host, the hash matches. So he think it's about network, and not only monero, some other softwares have the similar problem. 
He suggests uploading the file directly to Github, instead of linking Github download address to getmonero.org.
update: there is an attack causing $7000 loss, so I think this is not a network problem. 

## fluffypony | 2019-11-19T08:52:06+00:00
@jindouyunz a network problem wouldn’t have caused a malicious binary to be placed on the download server. We’ve discussed using GitHub as the primary download location, but that just shifts the boundaries as if someone’s GitHub account is compromised they can be replaced.

## jindouyunz | 2019-11-19T08:57:50+00:00
@fluffypony agree, it's not a network problem. What you said makes sense, things would turned worse if we do so and the Github account is compromised. 
Thank you.

## im23pds | 2019-11-19T09:49:25+00:00
It may be because the official Monero official account on Github has been stolen or a security hole has been replaced on Monero's official website...

## nikitasius | 2019-11-19T13:39:28+00:00
@sanecito @1522402210 @iphelix

Here they are (compare sha256 with hashes i shared in 1st message):
* WRONG ONE `7ab9afbc5f9a1df687558d570192fbfe9e085712657d2cfa5524f2c8caccca31`/`monero-wallet-cli--site`
  * [link](https://drive.google.com/file/d/1A3Uu3fN27OYDHR6evJ-4poP4hPLV89OW/view) `https://drive.google.com/file/d/1A3Uu3fN27OYDHR6evJ-4poP4hPLV89OW/view`
* GOOD ONE `5decc690a63aab004bae261630980e631b9d37a0271bbe0c5b477feffcd3f8c2`/`monero-wallet-cli--github`
  * [link](https://drive.google.com/file/d/14Wrw7WTRsrd6KoqunqVCvNooWUiU-LcX/view) `https://drive.google.com/file/d/14Wrw7WTRsrd6KoqunqVCvNooWUiU-LcX/view`

## MaxXor | 2019-11-19T20:20:18+00:00
I'm analyzing the malicious binaries. Luckily debug symbols are included which makes it easier. Here's my progress so far:

- two new functions are added named `cryptonote::simple_wallet::send_to_cc` at address 0x0000000000689AE0 and `cryptonote::simple::wallet:send_seed` at address 0x000000000068B590
- these malicious functions are called inside `cryptonote::simple_wallet::print_seed`
- `print_seed` is called at `cryptonote::simple_wallet::open_wallet` and `cryptonote::simple_wallet::new_wallet` - that means **anyone who created or opened a wallet with this binary has his seed stolen**
- the seed is then sent to 45.9.148.65 (node.xmrsupport.co with SSL certificate for node.hashmonero.com) port 18081 as simple HTTP POST request

## nikitasius | 2019-11-19T20:23:48+00:00
@MaxXor 
fresh domain:
```
Domain Name: xmrsupport.co
Registry Domain ID: D9E3AC179ACA44FE4B81F274517F8F47E-NSR
Registrar WHOIS Server: whois.opensrs.net
Registrar URL: www.opensrs.com
Updated Date: 2019-11-14T16:02:52Z
Creation Date: 2019-11-14T16:02:51Z
```
mean, all those was planned before and they got access much before.

So, XMR team need to check unusual access logs for 60 days.

## serhack | 2019-11-19T20:28:22+00:00
I've found another IP (hxxs://91.210.104.245:18081 that redirects to web page https://monerohash.com/?r=from_node [not involved] - as specified earlier the SSL is self-signed node.hashmonero.com) doing dynamical analysis (e.g. identifying packets via ngrep and tcpdump). Interesting. I'm writing a blog post collecting all the possible analysis. 

The domain xmrsupport.co was bought using Njalla , a privacy-aware domain and VPS service.


## MaxXor | 2019-11-19T20:39:03+00:00
@serhack Both IPs redirect on port 18081 to https://monerohash.com/?r=from_node and have a certificate with CN=node.hashmonero.com which is self-signed.

## serhack | 2019-11-19T20:40:03+00:00
I specified that "redirects" :) that does not mean they're involved.

## nikitasius | 2019-11-19T20:40:04+00:00
@serhack 
```
% This is the RIPE Database query service.
% The objects are in RPSL format.
%
% The RIPE Database is subject to Terms and Conditions.
% See http://www.ripe.net/db/support/db-terms-conditions.pdf

% Note: this output has been filtered.
%       To receive output for a database update, use the "-B" flag.

% Information related to '91.210.104.0 - 91.210.107.255'

% Abuse contact for '91.210.104.0 - 91.210.107.255' is 'abuse@hostkey.ru'

inetnum:        91.210.104.0 - 91.210.107.255
netname:        RU-SERVER-V-ARENDY
country:        RU
org:            ORG-LVA15-RIPE
admin-c:        AS36383-RIPE
tech-c:         AS36383-RIPE
status:         ASSIGNED PI
mnt-by:     
```

Russians. Well, i will call this hoster tomorrow :+1: 
By russian law they must keep logs 6 months minimum. Payment papers much longer.
* https://www.ripe.net/membership/indices/data/ru.server-v-arendy.html

They offer servers in russia and netherlands. xmrsupport ip's from netherlands.

## serhack | 2019-11-19T20:41:06+00:00

> % Abuse contact for '91.210.104.0 - 91.210.107.255' is 'abuse@hostkey.ru'
> 
> inetnum:        91.210.104.0 - 91.210.107.255
> netname:        RU-SERVER-V-ARENDY
> country:        RU
> org:            ORG-LVA15-RIPE
> admin-c:        AS36383-RIPE
> tech-c:         AS36383-RIPE
> status:         ASSIGNED PI
> mnt-by:     
> ```
> 
> Russians. Well, i will call this hoster tomorrow 👍
> By russian law they must keep logs 6 months minimum. Payment papers much longer.
> 
> * https://www.ripe.net/membership/indices/data/ru.server-v-arendy.html
> 
> They offer servers in russia and netherlands. xmrsupport ip's from netherlands.

I've already filled the ABUSE report for hostkey.

## serhack | 2019-11-19T20:47:17+00:00
> IP HISTORY for hashmonero.com
> * 45.9.148.65 from 2019-11-15 to 2019-11-17
> * 91.210.104.245 from 2019-11-19 to 2019-11-19


## Shinoa-Fores | 2019-11-19T21:05:21+00:00
> @selsta Yes, I know. But I'm not about to change my servers to Debian, just to build a Monero.
> All my servers are running `Slackware x64 14.2`. I know. Old school, but that's what I like.

Is using sha1 for checksums part of your "old school" approach? Because it's really kind of useless.


## bartblaze | 2019-11-19T22:24:27+00:00
I was having a look at this earlier as well. Adding onto @MaxXor's analysis, I wrote a brief blog post including how to detect the malicious files:
https://bartblaze.blogspot.com/2019/11/monero-project-compromised.html
Hope this can help someone.

## AbdelhamidGamal | 2019-11-19T23:21:38+00:00
Oh my Lord , Thats nasty , anybody lost his funds???

## krtschmr | 2019-11-20T02:48:33+00:00
Funds are #safu

## arch-btw | 2019-11-20T03:03:58+00:00
What about the other ip?

IP Address 	45.9.148.65 

% Abuse contact for '45.9.148.0 - 45.9.148.255' is abuse@as49447.net ''

inetnum:        45.9.148.0 - 45.9.148.255
netname:        NiceIT-NL
descr:          Nice IT Customers Network
country:        NL
admin-c:        KS10518-RIPE
tech-c:         KS10518-RIPE
status:         LIR-PARTITIONED PA
mnt-by:         niceit-mnt
created:        2019-04-22T16:41:37Z
last-modified:  2019-09-30T15:47:30Z
source:         RIPE

person:         Kimon S.
address:        28 Cork Street
phone:          +17672677496
nic-hdl:        KS10518-RIPE
mnt-by:         niceit-mnt
created:        2019-04-20T21:28:19Z
last-modified:  2019-04-20T21:28:19Z
source:         RIPE

route:          45.9.148.0/24
origin:         AS49447
mnt-by:         niceit-mnt
created:        2019-07-04T10:42:15Z
last-modified:  2019-07-04T10:42:15Z
source:         RIPE

## nikitasius | 2019-11-20T08:53:22+00:00
@arch-btw i advice to send an abuse to 
* `abuse@as49447.net`
* `abuse@hostkey.com`

Due datacencer in Moscow offers some servers in netherlands too. So probably they are belong to same contracter.

## fluffypony | 2019-11-20T12:18:21+00:00
Deleted a post that linked to mobile apps that claim to be “offline wallets”, but clearly cannot be so. Don’t install random bits of software linked on GitHub, folks.

## fluffypony | 2019-11-20T13:13:04+00:00
> You can undelete my post :)

This is the wrong place to shill your product. You’re welcome to go post about it elsewhere, like Reddit.

## krtschmr | 2019-11-20T13:18:46+00:00
@bogdan4o yes, there are wrong places indeed. this is a serious security issue and it's not necessarily about monero but about the bigger picture. electrum had similar attacks iirc, myetherwallet had dns attacks. 
in the money business, where we are all our own bank, you need to learn how to verify that what you're doing is correct.

clicking on links in a discussion about a security breach isn't helpful. feel free to shill your stuff any day of the year, everywhere, but here and today is not the right place. if it's so good, we would have read on reddit about it, prior this incident. no disrespect against you, but somebody with a blank github profile gets not even zero trust but -1.

thanks.



## serhack | 2019-11-20T13:36:24+00:00
91.210.104.245 has been blocked by the hosting provider. Good work guys!

## nikitasius | 2019-11-20T14:04:25+00:00
@bogdan4o 
i do not PR startups where i'm working btw

I agree with @fluffypony , this issue related to technical problem. It does not related to "tell us in 60 seconds about your product".

Same time about apple store or android store: you can simply have online backup feature. Nobody knows till your code isn't opensource.

## arch-btw | 2019-11-20T15:25:23+00:00
@bogdan4o 

>I represent my company CRYPall Ltd.

Nobody cares, stop shilling CryBawl Ltd...., you've been warned by @fluffypony already.

@nikitasius 

Thank you friend, I will email them.


## arch-btw | 2019-11-20T15:37:50+00:00
Ok I have sent the email.

If anyone wants to copy mine, that's totally fine:

To: 
abuse@hostkey.com
abuse@as49447.net

```
Hello,

This abuse report is in regards to ip address: 45.9.148.65
Recently (November 18, 2019), we have found this ip address to be embedded in malware.

To be more specific, it was found in a maliciously modified version of the open source project: Monero.

One of our community members (MaxXor) did analysis on the malicious binaries and found that the modified version steals cryptocurrency seeds and sends them off to 45.9.148.65.

This specific event has been documented in this github comment:
https://github.com/monero-project/monero/issues/6151#issuecomment-555694443

We would like to ask you to terminate the current server and account associated with the above mentioned ip address.

Further reading regarding this event can be found here:

https://github.com/monero-project/monero/issues/6151
https://web.getmonero.org/2019/11/19/warning-compromised-binaries.html
https://old.reddit.com/r/Monero/comments/dyfozs/security_warning_cli_binaries_available_on/
https://thehackernews.com/2019/11/hacking-monero-cryptocurrency.html

Thank you for your time.

```

## skironDotNet | 2019-11-23T23:47:25+00:00
The signatures still don't match. I just downloaded linux cli from the website with header 

> Current Version: **0.15.0.1** Carbon Chamaeleon

The actual download is monero-linux-x64-v**0.15.0.0**.tar.bz2

So you have wrong version to start, and SHA256 is
53d9da55137f83b1e7571aef090b0784d9f04a980115b5c391455374729393f3

While in downloaded and verified signature hashed.txt
monero-linux-x64-v0.15.0.1.tar.bz2, 8d61f992a7e2dbc3d753470b4928b5bb9134ea14cf6f2973ba11d1600c0ce9ad

So the binary on the getmonero website haven't been updated :(

**UPDATE:**
Seems like all the binaries has been updated to 0.15.0.1 except linux 64 cli
but if you take the download link and change version you can actually download latest
`wget https://dlsrc.getmonero.org/cli/monero-linux-x64-v0.15.0.1.tar.bz2`
so it seems like the link has not been updated.

Signature match: 8d61f992a7e2dbc3d753470b4928b5bb9134ea14cf6f2973ba11d1600c0ce9ad

The question is if this clean binary :)


## selsta | 2019-11-24T00:19:53+00:00
@skironDotNet Try a different browser / private window. The old file is still cached.

## skironDotNet | 2019-11-25T06:44:35+00:00
Cached or not, it's good link now, all that matters

## nikitasius | 2019-11-25T07:56:24+00:00
yep, looks fine and legit :heart: 

```
# sha256sum monero-linux-x64-v0.15.0.1.tar.bz2
8d61f992a7e2dbc3d753470b4928b5bb9134ea14cf6f2973ba11d1600c0ce9ad  monero-linux-x64-v0.15.0.1.tar.bz2
# gpg --verify v.15.0.1.txt
gpg: Signature made Sat 23 Nov 2019 01:34:14 PM UTC
gpg:                using RSA key 94B738DD350132F5ACBEEA1D55432DF31CCD4FCD
gpg: Good signature from "Riccardo Spagni <ric@spagni.net>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: BDA6 BD70 42B7 21C4 67A9  759D 7455 C5E3 C0CD CEB9
     Subkey fingerprint: 94B7 38DD 3501 32F5 ACBE  EA1D 5543 2DF3 1CCD 4FCD
```

* `0d8e612321fac7acef02fc5024029663bd7831de8cd24ae980c59e6e6e77b2b8`  LICENSE
* `41d258029a1c1125da24bca36037faf35fa50a9663e37c5a0dfca8ba23d38863`  monero-blockchain-ancestry
* `b512552f847f100e7bd4239a59c26d0a7e6c09e9263101b3d579f080c011f87b`  monero-blockchain-depth
* `a8d52a7a38fcae1cc71d1347270cec1c798caca0570d8ea7a8abbc6ca2245ea2`  monero-blockchain-export
* `ee96ddff82d5c3e53310878016e1acaa0b59195eb86dfd7f315eb891df0192ea`  monero-blockchain-import
* `0daafba019c8398dfe98e297b533912f4af489e68e74a44e8b68737c5946e4c3`  monero-blockchain-mark-spent-outputs
* `f1f82a441d8a8bd290d029e727a9595ebc5842c1580ec67a3318f17e02cb3482`  monero-blockchain-prune
* `95b53044efc30f0b973c8bd34d97046215dcc3b2e5c662cfbc35a8944a7fd963`  monero-blockchain-prune-known-spent-data
* `13aab9c7e2ceb56247a37af1801a98fd6d9e874779e25121d157100dcbc0a4d4`  monero-blockchain-stats
* `980ff8a4192c8e1163fe477750aab951fba11aef0ff7c4e09aec26e9f77c3a06`  monero-blockchain-usage
* `4bd7253253543f43528c54af81b9e4f414f0339c4ac824bb963cfecb2c6b9a06`  monerod
* `efcf257de59d35db0d492ef722f08af67d1c53edc265fe8bf8970c7a400c7823`  monero-gen-ssl-cert
* `70edd9ec6ea8aa90d5e6826fd9863603226f2c90b529ca2ab44dd824b39e0c32`  monero-gen-trusted-multisig
* `bc880fdd41197cdd4e24ff66cfa3e9cfafad3d1e9c347e3c18fef302837d1637`  monero-wallet-cli
* `76f700188adb42ae698c6fa2eaca53801216fc07e63f85f816a6f6780be7c3e0`  monero-wallet-rpc


## lmiranda | 2019-11-26T12:45:35+00:00
monero-gui-v0.14.1.0 points to a new version with the following msg, when i start it:

> https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.15.0.1.tar.bz2
> SHA256 Hash:
> 260edb14b1614e5b862b761eccd6259c1f0914d978016b227a9f4558059e4866
> 

But when i check the hash, it's the same from the site "c8994781510e234985e24f465761355e4ae7bd58ef686bd8b0ce4401c2314d51".
Is version 0.14.1.0 compromissed at any point, or the site still compromised, or just a bug in v0.14.1.0?

## selsta | 2019-11-26T12:47:34+00:00
It’s a bug that got fixed here: https://github.com/monero-project/monero-gui/pull/2485

v0.14 is not compromised and was never compromised.

## moneromooo-monero | 2019-12-04T18:50:30+00:00
+resolved

# Action History
- Created by: nikitasius | 2019-11-18T16:21:07+00:00
- Closed at: 2019-12-04T19:09:34+00:00
