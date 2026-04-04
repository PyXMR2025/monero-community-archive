---
title: Automated Docker Hub build
source_url: https://github.com/monero-project/monero/issues/3076
author: noonien
assignees: []
labels:
- proposal
created_at: '2018-01-07T14:15:27+00:00'
updated_at: '2025-10-03T15:22:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The project currently has a Dockerfile that can be used to build the project, it would be great if the project was automatically built by the Docker Hub, so users have access to the docker image more easily. This would allow users to deploy monerod by just running `docker run monero-project/monero`.

The only requirement for automated builds is that the GitHub repo have a Dockerfile, this requirement is already met.

Here's a guide on how to add the repository to the Docker Hub: https://docs.docker.com/docker-hub/github/#linking-docker-hub-to-a-github-account



# Discussion History
## moneromooo-monero | 2018-01-08T08:40:12+00:00
For clarity to people who may not realize, this means you'd be running a binary built by some third party.

## dEBRUYNE-1 | 2018-01-08T12:40:11+00:00
+proposal

## modernNeo | 2022-09-11T03:52:27+00:00
is there a reason this hasn't happened yet? It's not that hard to have an image uploaded to https://hub.docker.com/

## SamsungGalaxyPlayer | 2025-10-03T15:22:35+00:00
Personally, I think hosting Docker images [here on GitHub Packages](https://github.com/orgs/monero-project/packages) is a good idea. That way the existing organization account and its controls can be used. No Docker Hub account needed.

# Action History
- Created by: noonien | 2018-01-07T14:15:27+00:00
