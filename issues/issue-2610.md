---
title: '[beta] ci build optimization'
source_url: https://github.com/monero-project/monero-site/issues/2610
author: nahuhh
assignees: []
labels: []
created_at: '2026-03-19T12:10:04+00:00'
updated_at: '2026-03-19T14:30:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The ci builds the website in 7mins, includes all blog posts etc. This should be possible to reduce by 60+%.

Should we have it build using docker, and reduce the number of blog posts?

also, is there any reason its uploading build artifacts?

# Discussion History
## redsh4de | 2026-03-19T12:23:02+00:00
I think using Docker with the args to disable image optimization and cap the blog posts is a good idea, for previews

Only reason for the upload is to have seperate build and validate jobs - can collapse it into a single "Build & Validate" job to eliminate the upload step

## plowsof | 2026-03-19T12:36:28+00:00
just had a closer look at the 2 runs here, the "build site" section has completed twice in 3~mins , but the checkout action took 3 mins to run which i assume is bandwidth/lag on githubs end. 

moving the linter and html workflow to run concurrently would shave 2~minutes off also.

i've not checked on coolify previews since having webhooks enabled here, they _should_ be running 



## nahuhh | 2026-03-19T13:09:22+00:00
> I think using Docker with the args to disable image optimization and cap the blog posts is a good idea, for previews
> 

you don't think a good idea for the CI build as well? both docker and reducing blog posts



## redsh4de | 2026-03-19T13:56:22+00:00
> > I think using Docker with the args to disable image optimization and cap the blog posts is a good idea, for previews
> 
> you don't think a good idea for the CI build as well? both docker and reducing blog posts

We can definitely disable image optimization for CI

For the blog post limit... we'd probably want to make it so the limit includes any edited blog posts, thats the main blocker imo

## plowsof | 2026-03-19T14:28:07+00:00
it's expected that 2 blogs are pushed at once time + maybe a postmortem of something serious, the KISS currently limiting to 10 is fine 

*dynamically limiting to number of blog posts submitted , if the difference between 10 posts and 3~ is huge would be worth it 

## nahuhh | 2026-03-19T14:30:35+00:00
> it's expected that 2 blogs are pushed at once time + maybe a postmortem of something serious, the KISS currently limiting to 10 is fine 
> 

Yeah 
`bundle exec jekyll build --limit-posts 10` is current CI

# Action History
- Created by: nahuhh | 2026-03-19T12:10:04+00:00
