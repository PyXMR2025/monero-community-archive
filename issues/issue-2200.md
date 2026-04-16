---
title: Add the Flathub verify token
source_url: https://github.com/monero-project/monero-site/issues/2200
author: q7nm
assignees: []
labels:
- 💬 discussion
created_at: '2023-10-17T03:31:49+00:00'
updated_at: '2025-12-30T11:49:08+00:00'
type: issue
status: closed
closed_at: '2025-12-30T11:49:08+00:00'
---

# Original Description
Add this token `0a1ae4b2-3a4b-4f2d-bcd7-c9ff261e0f05` into `/.well-known/org.flathub.VerifiedApps.txt` to verify the application on Flathub.

# Discussion History
## plowsof | 2023-10-17T06:57:06+00:00
Example: https://fedoraproject.org/.well-known/org.flathub.VerifiedApps.txt

This is for the [Monero GUI Flatpak](https://flathub.org/apps/org.getmonero.Monero). We need the verified status to (in part) obtain a stable API key for this workflow which is using a beta key: https://github.com/monero-project/monero-gui/blob/master/.github/workflows/flatpak.yml

context: https://github.com/flathub/flathub/issues/3905#issuecomment-1591048976

bigmenpixels in-progress CCS proposal  - [Maintaining Flatpak package](https://ccs.getmonero.org/proposals/maintaining-flatpak-package.html)

## erciccione | 2023-10-17T07:25:03+00:00
The best way to do this is probably through the web server. I'll ping pigeons.

## erciccione | 2023-10-17T07:29:08+00:00
Maybe this should be discussed first. Verifying the flatpak from getmonero will mean that an effort completely run by a volunteer is "guaranteed" by the core team as trusted. Not sure if this should be the case, as nothing in the community is "official". Might be better to leave the flatpak "unverified". Asking for an input from core.

## VictorVow | 2023-10-17T07:50:28+00:00
Agreed, only do this if you're given commit control over the repo and the current maintainer has to instead submit PRs for any changes so that core can review them for malicious changes first. 

## plowsof | 2023-10-17T07:56:37+00:00
Edit* the flatpak workflow is now being reviewed. i think we can re-discuss/hold off until thats complete

some discussion can be seen in this comment and others on the proposal: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/381#note_21079

originally i agreed that its never going to be verified (as its clearly ripe for supply chain attacks - we don't control the flathub servers), however, i now support this "checkmark" for these reasons:
- the flatpak workflow which pushes binaries to flathub displays hashes at the end of the build process which can be verified on your local machine. it resides on the monero-gui repo which we control.
- we've made best efforts to remove control from our 3rd party volunteer* (sponsored by the CCS) by moving the flatpak repo to our core repo and had the api key pgp encrypted for luigis eyes only* ('best effort')
- an actual third party desktop app which supports monero can be "verified" instead. while the Monero-GUI not and people may be inclined to switch to that instead. 
- it's open source for people to build at home (or verify the hashes from the workflow run on our core repo)


# Action History
- Created by: q7nm | 2023-10-17T03:31:49+00:00
- Closed at: 2025-12-30T11:49:08+00:00
