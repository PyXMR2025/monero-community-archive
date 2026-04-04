---
title: Docker Container uses a end of life version of Ubuntu
source_url: https://github.com/monero-project/monero/issues/7938
author: Skaronator
assignees: []
labels: []
created_at: '2021-09-12T16:47:57+00:00'
updated_at: '2021-09-24T03:21:35+00:00'
type: issue
status: closed
closed_at: '2021-09-24T03:21:35+00:00'
---

# Original Description
Hi,

just a small heads up: the Monero container uses Ubuntu 16.04 which is EOL for non enterprise customer since **April 2021**.

https://wiki.ubuntu.com/Releases

https://github.com/monero-project/monero/blob/a39b1d56c8835798e2f5e3cc43c33b5f2d8e13da/Dockerfile#L182

----

I don't know how the release workflow works exactly but I would recommend to not compile monero again within the Dockerfile since its already built by the CI for ubuntu. This would simplify the Dockerfile itself, reduces duplicated environment configuration (Gitlab CI & Dockerfile) and hashes for the ubuntu compiled version would match with the hash inside the container.

https://github.com/monero-project/monero/blob/a39b1d56c8835798e2f5e3cc43c33b5f2d8e13da/.github/workflows/build.yml#L69-L95

----

Additionally it would be awesome if the Container could be published within the GitHub releases via the [Github Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).



# Discussion History
## hyc | 2021-09-12T17:00:23+00:00
Fwiw, the Gitian builds use Ubuntu 18.04. IMO every other dockerized build should do the same.

## selsta | 2021-09-12T18:51:11+00:00
> I don't know how the release workflow works exactly but I would recommend to not compile monero again within the Dockerfile since its already built by the CI for ubuntu.

We don't use it for the release workflow and all our hashes are already reproducible.

# Action History
- Created by: Skaronator | 2021-09-12T16:47:57+00:00
- Closed at: 2021-09-24T03:21:35+00:00
