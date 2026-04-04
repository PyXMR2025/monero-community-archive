---
title: Reproducible Builds
source_url: https://github.com/monero-project/meta/issues/191
author: anonimal
assignees: []
labels: []
created_at: '2018-03-09T01:41:42+00:00'
updated_at: '2023-12-18T04:31:43+00:00'
type: issue
status: closed
closed_at: '2023-12-18T04:31:43+00:00'
---

# Original Description
This should apply to the entire build system. Ticketing for housekeeping.

Referencing https://github.com/monero-project/monero/issues/2641.

# Discussion History
## SamsungGalaxyPlayer | 2020-06-05T15:41:21+00:00
CLI: done
GUI: not yet done

## sedited | 2020-06-05T23:33:39+00:00
To keep this open and update on progress on the gui build:
Cmake support on the gui build was the primary goal. I initially authored a half-broken pull request to get the ball rolling last year: https://github.com/monero-project/monero-gui/pull/2404 . Its stability has improved greatly thanks to the work of xiphon to the point where its now nearing a usable state. In the meantime I've been working on the repro builds on this branch here: https://github.com/TheCharlatan/monero-gui/tree/dependsQtSub . I'm stuck at the moment with building qt with open gl support. Once that hurdle is overcome, I think it won't be too much work to get to a fully reproducible release.

## scottAnselmo | 2020-06-06T00:11:59+00:00
Thanks for the update @TheCharlatan! Perhaps a silly question, but have you asked on the reproducible-builds.org mailing list for advice (haven't seen anything in the last two months in subject concerning Qt/OpenGL/Monero/your handle)?

## sedited | 2020-06-06T09:16:49+00:00
I have not worked on the problem in the past few months, but I think this is rather something for the qt forums.

## carrington1859 | 2021-11-24T11:03:07+00:00
https://github.com/monero-project/monero-gui#compiling-the-monero-gui-from-source

Is it correct to say we now have reproducible builds for the GUI on everything other than Android?

## selsta | 2021-11-24T11:04:14+00:00
No. macOS isn't reproducible. Not sure about android.

## plowsof | 2023-12-17T16:46:04+00:00
what steps are required to solve the reproducible issues for the GUI? (we at least have a reproducible 'installer' .exe https://github.com/plowsof/monero-gui-exe 

## selsta | 2023-12-18T04:31:43+00:00
Let's keep track of the GUI reproducible build status in the GUI repo.

# Action History
- Created by: anonimal | 2018-03-09T01:41:42+00:00
- Closed at: 2023-12-18T04:31:43+00:00
