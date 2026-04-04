---
title: check if opengl32sw.dll is definetely needed. IF yes, update readme's, windeploy_helper
  and build env accordingly
source_url: https://github.com/monero-project/monero-gui/issues/927
author: medusadigital
assignees: []
labels: []
created_at: '2017-10-24T13:26:36+00:00'
updated_at: '2023-08-13T23:57:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
check if opengl32sw.dll is definetely needed. Currently it is added by hand for each release. 

If it is needed, readme, windows deployment script and buildenv will need to be updated.

# Discussion History
## pazos | 2018-04-19T00:17:31+00:00
it was used in Helium Hydra, not in Lithium Luna yet.
This is a [library](https://www.mesa3d.org/llvmpipe.html) that supports opengl without needing a GPU.

This is really important for people trying to use the GUI via remote desktop or with VMware/Virtualbox

## selsta | 2023-08-13T23:57:59+00:00
Yes, opengl32sw.dll is required. I'll see if I can improve the DEPLOY instructions.

# Action History
- Created by: medusadigital | 2017-10-24T13:26:36+00:00
