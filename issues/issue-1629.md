---
title: Torrents on downloads page
source_url: https://github.com/monero-project/monero-site/issues/1629
author: Masken8
assignees: []
labels:
- downloads
- enhancement
created_at: '2021-05-16T19:23:51+00:00'
updated_at: '2025-11-09T02:44:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
No description

# Discussion History
## erciccione | 2021-05-17T07:13:05+00:00
I guess you are suggesting to have the possibility to download the wallets as torrents. This has been discussed in past (#508 #515), but at the end we didn't add them. Mostly because it's something that need to be maintained.

Supporting torrent downloads is something i considered for some time. The problem is: who is going to host these torrent? Even if the hashes can be verified for autenticity, we need a trusted entity to publish the torrents if we want to list them on getmonero.

I don't know if the core team is willing to do that. Especially since a new torrent needs to be created for each release and then they need to be seeded.

## erciccione | 2021-05-17T07:42:13+00:00
There could be two solutions:

1. @binaryFate (or somebody else from the core team) could create and upload the torrent to a seedbox hosted by core. Then the process would be the same as it is for the normal binaries now. We don't need to add the hash of the torrent (but we could anyway) because people can unpack the torrent and verify the archive, so we would just need to add the links.
2.  Somebody else takes care of uploading the torrent files. This could be an easy CSS, but requires effort from the maintainers anyway, since the torrents will need to be verified to make sure they match the binaries released by core. We could also ask the uploader to post the hash of each torrent, so that people can easily verify the torrent is the same as the one of the uploader, but at the end, the important is to verify that the hash of the Monero binaries match.

## HardenedSteel | 2021-05-28T09:17:02+00:00
I think seeding is shouldn't be problem, everyone can seed and contribute + Monero has a community so we will have enough seeder i guees.

## HardenedSteel | 2022-01-15T19:06:56+00:00
Related bounty topic: https://bounties.monero.social/posts/52/add-alternative-download-methods-on-getmonero-org

## erciccione | 2022-01-16T12:16:19+00:00
I don't think a bounty will help here.

## MoneroArbo | 2022-01-18T21:09:45+00:00
I don't mind creating and seeding torrents, I already run a seedbox on a gigabit connection

The easiest thing (for me) would be create a single torrent containing all the downloads, then the user picks which one(s) they want in their torrent client, but separate torrent files would probably be easier for users.

Another question would be DHT vs public trackers vs running a tracker. I don't want to run a tracker. Public trackers are pretty unreliable. I think DHT works well enough and is decentralized, plus if I'm not mistaken someone could recreate the link with the same file and get the same result since it's a hash table, but maybe others have thoughts.

sample DHT only magnet link: magnet:?xt=urn:btih:9a884d0b352df58dbd49af49be0819f373b5b536&dn=monero-gui-linux-x64-v0.17.3.1.tar.bz2

seems to work for me but maybe someone else can test

I'm just not sure how much work me doing this would take from binaryFate since the links are easy to make and he'd have to verify stuff anyway. if the magnet links are indeed deterministic, maybe they could be generated during the build process or something.

I guess another question is how much this would help availability or censorship resistance. The files are small enough to be re-hosted easily, and however you get them you're going to need to verify authenticity somehow.

## HardenedSteel | 2022-01-18T23:33:23+00:00
@MoneroArbo I already made two separate torrent file which contains all the downloads at the pull request.

## MoneroArbo | 2022-01-18T23:36:46+00:00
I saw the pr

## plowsof | 2025-10-09T11:45:42+00:00
- A multi file torrent (not the blockchain file) has a reproducible file-info hash.
- a webseed acts as a bootstrap if there are no peers seeding.
- easy to create/update https://github.com/plowsof/monero-torrent ([see releases](https://github.com/plowsof/monero-torrent/releases/tag/v0.18.4.2))
- a placeholder PR is made, however, discussion is required and if approved - the torrent file can be updated as a final release step and added to dns via downloads.getmonero.org/torrent
- To support webseed **set and forget** redirects on getmonero are required: (getmonero will ~~only webseed the latest version~~ webseed whatever is available on the CDN still)

dlsrc.getmonero.org redirects:
--- 
redirect for hashes.txt
```
location ~ ^/monero-v[0-9.]+/hashes\.txt$ {
    return 302 https://www.getmonero.org/downloads/hashes.txt;
}
```
bfs gpg key: (DataHoarder noticed the redirect not working as i had a different order nginx side)
```
location ~ ^/monero-v[0-9.]+/binaryfate\.asc$ {
    return 302 https://raw.githubusercontent.com/monero-project/monero/master/utils/gpg_keys/binaryfate.asc;
}
```
and everything else
```
location ~ ^/(monero-v[0-9.]+)/(.+)$ {
    return 302 https://dlsrc.getmonero.org/$2;
}
```

## jermanuts | 2025-10-09T15:21:18+00:00
Bad idea, people will just pick the torrent with highest seed which will most likely be the first initial version, also less control if anything goes bad and people still download/seed that version. If anyone wants to create a torrent they can do themselves.

## plowsof | 2025-10-09T15:56:45+00:00
>people will just pick the torrent with highest seed

due to the set and forget redirects - getmonero will only webseed ~~the latest version~~ what is available on the CDN

>also less control if anything goes bad and people still download/seed that version.

these are release binaries: the torrent would e updated the same time as the DNS which prompts people to update if that was a concern, and see above reg getmonero ~~_only_ seeding the latest version~~ seeding whatever is available on the CDN

> If anyone wants to create a torrent they can do themselves.

yes, simply and deterministically via  this repo (i thought it was public but apparently not, fixed now) https://github.com/plowsof/monero-torrent

for reference, the same type of torrent is available for https://bitcoin.org/en/download 

## librootorg | 2025-11-09T02:44:38+00:00
> 
> ```
> location ~ ^/(monero-v[0-9.]+)/(.+)$ {
>     return 302 https://dlsrc.getmonero.org/$2;
> }
> ```

That redirect rule fails to match the Monero GUI paths. Maybe update it with something like this:

```
location ~ ^/(monero(-gui)?-v[0-9.]+)/(.+)$ {
    return 302 https://dlsrc.getmonero.org/$3;
}
```

Currently the webseed URLs for the GUI torrents do not work because of this.

# Action History
- Created by: Masken8 | 2021-05-16T19:23:51+00:00
