---
title: Provide SHA3 hashes at getmonero.org instead of SHA256
source_url: https://github.com/monero-project/monero-site/issues/548
author: b-g-goodell
assignees: []
labels: []
created_at: '2018-01-11T14:08:16+00:00'
updated_at: '2018-01-19T01:39:13+00:00'
type: issue
status: closed
closed_at: '2018-01-18T21:52:48+00:00'
---

# Original Description
I opened an issue [here](https://github.com/monero-project/monero/issues/3041#issuecomment-354680744) about this. I got a response that hashing is to check integrity, not security, and folks should check signatures anyway.

But this misses the point, which is: don't make a modifiable hash the _face_ of download integrity checks. If you want to have a big list of hashes, _fine,_ but don't _only include_ the one that is vulnerable to length extension attacks _on the official, user-friendly website!_ If users want to check only _one_ hash, which one are they going to check? The one next to the download link!

Yes, the best practice is for users to check signatures, but almost no one ever does, in practice. If your version of security is to put up a modifiable hash on the most publicly available download page, but bury the actual authentication through a series of links, then you've put unnecessary barriers between users downloading a file and authenticating it, so a huge portion of users will simply not bother authenticating appropriately, even some of the savviest users we have get lazy, and almost _none_ of the newest users are savvy.

# Discussion History
## erciccione | 2018-01-15T13:38:22+00:00
+improvement

## luigi1111 | 2018-01-15T19:47:57+00:00
> but bury the actual authentication through a series of links, then you've put unnecessary barriers between users downloading a file and authenticating it

Are you promoting a more visible way of authenticating the downloads?
SHA256 vs SHA3 has no bearing on authentication, and one isn't notably better than the other on the integrity front. SHA256 is more widely supported at this point, but that's not likely a huge consideration either way.

## b-g-goodell | 2018-01-18T13:01:15+00:00
As the title says, I think the getmonero.org downloads sections should display the sha3 hash not the sha256. If the MD5 hash of the download was being displayed, the reason to change would be obvious. Fact of the matter is that SHA256 is notably worse than SHA3 because SHA256 is vulnerable to length extension attacks... so consider the following hypothetical scenario to see why *in this scenario.*

I am a new user, I don't know about unicode, and I'm moderately lazy. My plan is to google "get monero downloads page" because I forgot or never knew the name, download monerod, and check the SHA256 hash. Or perhaps a friend has sent me a link that I am blindly clicking on. Now that I have the URL in hand, I can manually type it in forevermore, but that first time, I downloaded something from a website I found through google or through a blind link. So later on, I will manually type in the URL and find the full list of hashes of my download by following the links on getmonero.org. But I only check the SHA256 hash because, I figure "why would they only list SHA256 on getmonero.org if that was insufficient?" 

Unfortunately, the first time I googled this, I clicked on a malicious advertisement for getmonerσ.org, I didn't notice the unicode character, and my mind registered this URL as getmonero.org (this has happened with mymonero many times to many new users). So my downloaded file has some malicious data appended to it in a length extension attack such that the SHA256 hasn't changed. When I manually type in the URL the second, third, and all future times, I find myself on the true Monero website, and the SHA256 hashes match! I stop here instead of checking all four or five or eleventy-billion different hashes, because I'm human and there are so many hours in the day. Voila, malicious information happily downloaded onto my computer and authenticated with the SHA256 hash. The worst part? The whole original download had to have been included in the download for the length extension attack, so *not only did all the above occur, I also successfully installed the current up to date version of monerod from this process!* I also, unfortunately, have invited an unknown amount of appended malicious data onto my local machine.

If the hash on the website had merely been SHA3 instead, or pretty much *any* of the SHA-3 finalists, really, this route of MITM is not possible. Including only the SHA256 on the website is not as bad as including only the MD5 hash, but... why? It takes three minutes to change and it prevents the above sort of malicious behavior.

If any of the above is a misunderstanding of the length extension attack or SHA256 or anything like that, I'd rather be corrected on the matter than continue humping a dead horse.

## leonklingele | 2018-01-18T14:43:05+00:00
Thinking about it, why is the statement only signed by @fluffypony? Doesn't Monero have reproducible builds which would allow others to sign it as well?

## luigi1111 | 2018-01-18T17:58:51+00:00
@b-g-goodell LEA isn't about collisions; it is mostly relevant to MAC uses where part of the data is secret.

All in all, the first order use of the hashes isn't terribly useful (that is, verifying integrity of a download from getmonero.org -- browsers are pretty good about corrupt downloads AFAIK), but they are useful for checking validity of a third party download site (basically your example).

## b-g-goodell | 2018-01-18T21:52:48+00:00
@luigi1111 Gosh darnit, you are 100% correct, and I am wrong. I thought length extension could be used to execute a collision attack, but that is incorrect. The length extension vulnerability of MD5 or SHA256 are not relevant to the situation I described above. 

I am closing this issue, because it's not an issue! Hup hup!

# Action History
- Created by: b-g-goodell | 2018-01-11T14:08:16+00:00
- Closed at: 2018-01-18T21:52:48+00:00
