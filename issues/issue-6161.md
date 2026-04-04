---
title: Security Recommendations
source_url: https://github.com/monero-project/monero/issues/6161
author: re42
assignees: []
labels: []
created_at: '2019-11-20T07:08:31+00:00'
updated_at: '2022-02-19T04:46:23+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:46:23+00:00'
---

# Original Description
Although i appreciate everything the team has done, i want to mention a few things. Whenever i downloaded Monero binaries from the website, deep down inside i always knew this was wrong (Even though i always checked the hashes from Github). As most software binaries such as bisq for example is downloaded straight from and hosted on Github only and their site linked to Github.  So i dont know why the binaries were hosted on the site.  What was the purpose of that exactly?  They couldve at least linked from the Github repo binaries(which are not all there currently).

Going further i propose 2 very important security requests for the survival of Monero.

1. Move over to Gitlab/Gitea or something other than Github ASAP. (Nothing Microsoft-owned is safe)
2. Host **_ALL_** binaries on Gitlab/Gitea and **_LINK_** from them on the site

If you shrug this off because you deem it unnecessary, it will bite most of us if not all in the ass in future. I guarantee you that.
Security comes first.

Edit:  I also recommend Radicle, but due to it being still new and buggy, i first say Gitlab/Gitea until Radicle is more stable.  Opinions?

# Discussion History
## dEBRUYNE-1 | 2019-11-20T07:28:01+00:00
Fluffypony's response regarding hosting the binaries on Github:

>GitHub is problematic in some countries, yes, but there’s also the issue of multiple people having access to GitHub so the attack surface is larger. We’ve discussed this many times and ultimately the decision has been to have GitHub as a backup.

https://www.reddit.com/r/Monero/comments/dyou81/psa_weve_posted_an_announcement_regarding_the/f847e1a/?context=3

## fluffypony | 2019-11-20T07:47:32+00:00
I don’t see how this would change anything. We would self-host GitLab, which would then host the binaries, which means the server hosting GitLab could be compromised. On the other hand, we could use GitLab’s hosted instance, but then we’re not only giving them the ability to censor downloads, but we’re massive broadening the attack surface.

## re42 | 2019-11-20T08:33:58+00:00
hmm true..
Ok so what about the following:

- When new releases come out, you automate upload the binaries both on Github, Gitlab and on the site.  3 different places.  All 3 places have the same information of hashes and signatures for the user.

- When the user clicks on the binary on the site to download, before downloading, a script would run in the background cross-checking the hashes and sigs from Github and Gitlab that they all match, if they do, the file gets downloaded.  If not, devs get sent an emergency notification.

- The Monero code should be primarily hosted on Gitlab and have Github update only the binaries for cross-checking purposes.

Could this work?

## fluffypony | 2019-11-20T08:42:31+00:00
We already have binaries on GitHub and the downloads server, and hashes on self-hosted GitLab and the website server. This isn’t a distribution problem. Automating the check is complicated - would such a script run on the user’s computer? How do we securely deliver the script to the user’s computer, wouldn’t an attacker just compromise that script? It’s not a trivially solvable problem - people have to be educated to check hashes after they download.

## re42 | 2019-11-20T08:47:04+00:00
My bad, the script could be compromised together with the site binaries.  So rather not have any binaries on the site, but a choice of download locations - Github / Gitlab / Gitea  and have the script cross-check hashes on all Github & Gitlab & Gitea.  So the attacker would have to attack both Github/Gitlab/Gitea AND your site to actually compromise anything.

This script should run in the background of https://web.getmonero.org/downloads/ before the choice of download locations is shown to the user.  Its just a check-script.  No binaries on the site.

Thoughts?

## fluffypony | 2019-11-20T09:18:07+00:00
We already have multiple locations, and the other locations weren’t compromised.

So a user opens the download page, and then a script downloads binaries for 10 operating systems to the user’s computer and compares them before allowing them to download? So about 700mb is loaded client-side before they can download? Because that’s untenable.

Or does the script live on some other server that downloads 700mb every time a user access the site? Because then an attacker can just serve untampered downloads to the server running that script, and serve bad downloads to the user.

## re42 | 2019-11-20T10:25:04+00:00
> We already have multiple locations, and the other locations weren’t compromised.

Thats the thing, thats why im suggesting the following:

1. User goes to https://web.getmonero.org/downloads/
2. When user clicks on a binary file, a popup window informs the user to please wait until all binaries have been verified from all hosted locations.
3. At that instant a cross-check script runs in the background on the site, validating the signature & the hashes of the binary file the user is about to download and compares the 3 location binaries to each other.
4. If all binaries match each other, user gets notified "Binaries validated" and gets the option to download from one of the 3 locations.

- No downloads should be hosted on getmonero.org
- All binaries should be hosted and hashes clearly shown on all 3 locations.
- Only the cross-check script should run to check signatures and hashes before download options occur.
- No need for user to download a script or anything like that.

If the attacker tries to get a hold of the script, so what? what are they going to change?  Its just a signature and hash checker.  They would have to attack one of the other 3 locations **as well as** your site to make changes believable.  They could however change the download links(Github/Gitlab/Gitea) to redirect the user to a copycat site, then i would suggest running a different script that runs from a selected number of dev's computers as a CRON which often checks that those links are not changed on the site.

Of course all users should learn how to validate their hashes and signatures, but its important for Monero to secure all deployed binaries first.

Personally, After all this, i will STILL validate all hashes and signatures from locations on my end anyway.

## fluffypony | 2019-11-20T10:39:57+00:00
So then the hacker just attacks the server the site is hosted on, and changes the download link to their own malicious GitHub / GitLab whatever, and modifies the script to validate those. This doesn’t solve anything, it just gives the user a false sense of security.

## re42 | 2019-11-20T10:45:43+00:00
> So then the hacker just attacks the server the site is hosted on, and changes the download link to their own malicious GitHub / GitLab whatever, and modifies the script to validate those. This doesn’t solve anything, it just gives the user a false sense of security.

Yea i know, i mentioned a workaround to that already:

> They could however change the download links(Github/Gitlab/Gitea) to redirect the user to a copycat site, then i would suggest running a different script that runs from a selected number of dev's computers as a CRON which often checks that those links are not changed on the site.

This cronjob can be a simple bash script that anyone of us can run on our computer's to check those links every hour or something, if those links are changed then all devs get notified.  Can't that work?

## fluffypony | 2019-11-20T12:16:14+00:00
It seems like a very convoluted measure that ultimately boils down to a bunch of people checking the downloads from around the planet to see that they’re still fine, either manually or scripted, which is exactly what happened and was how we picked this problem up.

## NacJidtyd6op | 2019-11-20T12:47:53+00:00
Zeronet site with hashes is enough.



## fluffypony | 2019-11-20T12:49:15+00:00
Again - the distribution is not the issue. People have to check the downloads after they’ve downloaded them.

## NacJidtyd6op | 2019-11-20T12:54:56+00:00
If github,gitlab etc are hacked hashes will change too.
Zeronet site is unbreakable so why not.
Hashes cant change.


## fluffypony | 2019-11-20T12:56:10+00:00
An attacker would then just hack the website and modify the link to the downloads. It doesn’t solve anything, it just moves the goalposts.

## NacJidtyd6op | 2019-11-20T13:00:36+00:00
ok but if anyone do hashing check is sure.
if someone dont is his/her problem.

is a positive reinforcement step for monero.

## fluffypony | 2019-11-20T13:11:54+00:00
I agree that it’s overall positive that is a big reminder to check hashes after downloading!

## NacJidtyd6op | 2019-11-20T13:17:39+00:00
zeronet download links are hashed too so zeronet site is must!

the only thing left for attacker is to put a gun on the head of zeronet site hash owner!

## iamamyth | 2019-11-20T22:18:11+00:00
Is there currently only one signature posted? It might be a good idea to have multiple parties provide signatures, that way people downloading the binaries can make a more informed web of trust determination.

## hyc | 2019-11-20T22:53:59+00:00
@iamamyth we've been encouraging more people to submit signatures to https://github.com/monero-project/gitian.sigs
At this point anyone can submit a PGP key and create a reproducible build, and attest to the hashes.

## fluffypony | 2019-11-21T03:51:34+00:00
> Is there currently only one signature posted? It might be a good idea to have multiple parties provide signatures, that way people downloading the binaries can make a more informed web of trust determination.

That one signature is just a convenient way to post the result of the Gitian sigs up in a digestible format. The source of that is MANY people posting their GPG sigs conforming they get the same hashes. I think it’s safe to consider the Gitian sigs an irrefutable source of truth, no need to over complicate hashes.txt as a communications mechanism for that.

# Action History
- Created by: re42 | 2019-11-20T07:08:31+00:00
- Closed at: 2022-02-19T04:46:23+00:00
