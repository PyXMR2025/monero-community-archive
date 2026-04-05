---
title: Trouble enabling Hugepages in VPS
source_url: https://github.com/xmrig/xmrig/issues/176
author: StealthBadger747
assignees: []
labels: []
created_at: '2017-10-25T21:31:02+00:00'
updated_at: '2019-12-30T04:20:19+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:36:15+00:00'
---

# Original Description
My VPS is running Ubuntu 16.04 and I complied the miner myself.
Whether I run xmrig as root or not, I still get hugepages disabled.
I tried following this guide [HERE](http://docs.netapp.com/oci-73/index.jsp?topic=%2Fcom.netapp.doc.oci-ig-lin%2FGUID-8BD86753-27AC-407C-BEE6-85A1D2363E7D.html) to enable hugepages, but when I run `sudo sysctl -p` as root, I get `sysctl: permission denied on key 'vm.nr_hugepages'` and I can't find a way around this.

# Discussion History
## ghost | 2017-11-04T18:09:50+00:00
There is no way around this, and by the sound of it: it's useless to run it on your VPS instance.
The kernel you are using is OpenVZ, meaning you're running a confined environment on a single machine that other people alongside you share. You are all sharing the same processor and have no reservation on a strict amount that only you can use.

Your hosting company in theory, can enable hugepages on their kernel, and make the changes to you and your neighbors on the same hardware, but it's seldom. 

If you really insist on running the miner on something in the criteria of a VPS, you would want to make sure that it is KVM and not OpenVZ.

Have a look at this google search: https://www.google.com/search?ei=WAL-WfuBOITUjwPb1pPQDw&q=openvz+sysctl+permission+denied&oq=sysctl+openvz+permi&gs_l=psy-ab.3.0.0i22i30k1.4360.6890.0.7934.19.19.0.0.0.0.133.1747.13j6.19.0....0...1.1.64.psy-ab..0.19.1738...0j0i131k1j0i67k1j0i131i46k1j46i131k1j0i22i10i30k1.0.Pc_E2fuVQ_g

## vuongcongquan | 2018-03-16T17:21:41+00:00
i am having ubuntu vps 16. so i want to install xmrig running on vps i have to do how! please help me


# Action History
- Created by: StealthBadger747 | 2017-10-25T21:31:02+00:00
- Closed at: 2017-11-27T00:36:15+00:00
