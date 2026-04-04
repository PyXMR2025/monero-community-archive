---
title: Pick a more common open source license to dual-license the project under and
  ease adoption
source_url: https://github.com/monero-project/monero-gui/issues/4115
author: chris00001
assignees: []
labels: []
created_at: '2023-02-04T23:20:32+00:00'
updated_at: '2023-02-05T01:02:01+00:00'
type: issue
status: closed
closed_at: '2023-02-05T00:54:34+00:00'
---

# Original Description
The current license complicates getting it into Debian and hundreds of downstream distributions. While I'm not seeing anything particularly problematic with the license itself (I don't think anyway)  the fragmentation of licenses (each project having a different unique license) makes inclusion into distributions difficult. Debian is generally the ideal distribution to get software into as most mainstream distributions and desktop-oriented distributions geared toward users that need greater privacy or security are derived from it. Tails for instance is a small however very popular distribution focused on privacy and Tor (it's very much connected to the Tor project). It is derived from Debian. While Tails developers and users want to include Monero GUI they can't easily do so right now. The first thing they need is it packaged for Debian, but it can't be packaged for Debian (or not for the core repo anyway) until after there is an acceptable license. An acceptable license is basically something that has been reviewed and thus with Monero GUI being a unique license even if open source it's not made its way into Debian or Tails. Selecting one of the other licenses to dual-license the software under would really help achieve the aim of easing adoption and increasing the adoption of Monero.

There are a list of licenses in Debian's main repository that would be ideal to pick from:

https://www.debian.org/legal/licenses/

# Discussion History
## selsta | 2023-02-04T23:23:17+00:00
Monero uses https://opensource.org/licenses/BSD-3-Clause which is linked on the debian page.

## chris00001 | 2023-02-05T00:27:09+00:00
Yes, but it's this program, monero-gui that I'm referring to that uses some custom license, not the BSD 3-Clause license: https://github.com/monero-project/monero-gui/blob/master/LICENSE 

If monero-gui also utilized the BSD 3-Clause license that would be wonderful.

## selsta | 2023-02-05T00:32:12+00:00
Can you be more precise? monero-gui does not use a custom license. It uses the exact license I linked, BSD 3-Clause.

The only difference is that we have "All rights reserved." which is used in some places and not in others, see for example: https://joinup.ec.europa.eu/licence/bsd-3-clause-new-or-revised-license

## chris00001 | 2023-02-05T00:49:30+00:00
How did you come to that conclusion? The license file doesn't say anything about the BSD 3-Clause license. I just linked to the license for the monero-gui source which includes a license file that says: Copyright (c) 2014-2018, The Monero Project

err ... never mind. I must be blind.

## selsta | 2023-02-05T00:54:34+00:00
I'm not sure if you are trolling at this point, in case you are not here is a different example project that uses 3-Clause BSD: https://github.com/openthread/openthread/blob/main/LICENSE

# Action History
- Created by: chris00001 | 2023-02-04T23:20:32+00:00
- Closed at: 2023-02-05T00:54:34+00:00
