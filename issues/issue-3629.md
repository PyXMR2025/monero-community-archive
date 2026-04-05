---
title: '[Feature Request] Benchmark + stress any algo'
source_url: https://github.com/xmrig/xmrig/issues/3629
author: Motophan
assignees: []
labels:
- wontfix
created_at: '2025-02-04T06:49:26+00:00'
updated_at: '2025-06-16T15:18:38+00:00'
type: issue
status: closed
closed_at: '2025-06-16T15:18:38+00:00'
---

# Original Description
What I want to do

`sudo ./xmrig --algo cn-pico --benchmark=1M`

or

`sudo ./xmrig --algo cn-pico --stress`

the benchmark will eventually complete but will only warn me of errors at the end. Stress is useful since it will say rejected share or something to that effect if it makes a cpu mathematical error indicating my OC is unstable. 


Reason: some algos are memory hard, some algos are core hard. I want to be able to make sure my OC is stable by stressing various algos


it would be super useful for me to also run all algos, including gpu algos like `sudo ./xmrig --algo KawPow` and then mess with msi afterburner to find optimal powerlimit / core offsets / find a stable OC. 


I dont really care how this is accomplished. I understand --stress requires the dev to run a server that validates my blocks and the dev runs this for free since it generates them a small amount of money via blockchain. I understand asking for multiple servers validating some jobs that cost more to validate than they generate in money is not possible. If we could run xmrig-proxy on another pc to generate fake jobs for all algos OR have the benchmark periodically make sure the solution is valid with it doesnt matter to people who use this to validate OC. We are not trying to make money with this. 

fx:

--benchmark 9999G --validate 10M
where it would run for ~ 10 mins between validations and essentially run forever

would be effectively 

--stress

# Discussion History
## ahorek | 2025-02-10T22:03:08+00:00
cryptonight changes utilization over time, simulating it and comparing results with prepared correct results won't behave the same as real mining, so I don't think this mode will be realistic and usable for OC tuning.

there are more effective programs that can push your PC even harder for full stability testing. For example, [Prime95](https://www.mersenne.org/download/#stresstest) includes mathematical validation to ensure result correctness.

# Action History
- Created by: Motophan | 2025-02-04T06:49:26+00:00
- Closed at: 2025-06-16T15:18:38+00:00
