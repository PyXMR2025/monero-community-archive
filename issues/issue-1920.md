---
title: Button of 404 page too close to bottom in some browsers
source_url: https://github.com/monero-project/monero-site/issues/1920
author: erciccione
assignees: []
labels:
- bug
created_at: '2022-01-18T09:46:52+00:00'
updated_at: '2023-08-17T15:39:47+00:00'
type: issue
status: closed
closed_at: '2023-08-17T15:39:47+00:00'
---

# Original Description
See screenshots in #1918

# Discussion History
## FedericoNembrini | 2023-01-03T13:16:16+00:00
It seems to me that the button is only too close if the browser window (or device screen) is too small.

We could add an `id` to the button and style it with `margin-bottom: 1rem;` (`1rem` so it keeps the margin constant as in the home content and footer).

# Action History
- Created by: erciccione | 2022-01-18T09:46:52+00:00
- Closed at: 2023-08-17T15:39:47+00:00
