---
title: Intel(R) Xeon(R) CPU E3-1240 wrong Hashrate
source_url: https://github.com/xmrig/xmrig/issues/307
author: Zelecktor
assignees: []
labels: []
created_at: '2018-01-01T08:43:25+00:00'
updated_at: '2019-08-02T12:46:10+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:46:10+00:00'
---

# Original Description
As the title. Im running this procesor on linux debian 8.
I tried to run it with many confugurations to have the best hashrate (when i know that this processor working full full, makes abour 300-350h/s but im getting about 10-15h/s.)

This is the running messaje:

root@mininguser:~/xmrig/build# sudo ./xmrig -a cryptonight -o stratum+tcp://pool.supportxmr.com:3333 -u 4956NVBAzkGA8imVZzLYe7f65xG8HXiERGbbMEHqiqfqdyDFdjwqXVv8U1MHbiki6jjMzMUykNmYQLNUvEbkTJDU9miq5qb -p opk01 -t 8 --av=1 -r 5 --cpu-affinity 0xFF --cpu-priority 5 --max-cpu-usage=80

 * VERSIONS:     XMRig/2.4.3 libuv/1.9.1 gcc/4.9.2
 * HUGE PAGES:   available, disabled
 * CPU:          Intel(R) Xeon(R) CPU E3-1240 V2 @ 3.40GHz (1) x64 AES-NI
 * CPU L2/L3:    1.0 MB/8.0 MB
 * THREADS:      8, cryptonight, av=1, donate=5%, affinity=0xFF
 * POOL #1:      pool.supportxmr.com:3333
 * COMMANDS:     hashrate, pause, resume
[2018-01-01 03:32:35] use pool pool.supportxmr.com:3333 107.178.104.10
[2018-01-01 03:32:35] new job from pool.supportxmr.com:3333 diff 1000
[2018-01-01 03:32:39] speed 2.5s/60s/15m n/a 13.5 n/a H/s max: n/a H/s

Also tried with 2 threats and cpu affinity with 0x5
4 threats and cpu affinity with 0x55
but same results, no more than 10-15H/s

Please help me with the config please!


# Discussion History
## bs3vcenk | 2018-01-01T20:36:19+00:00
Reduce the threads to 4 (for best performance cryptonight needs 2MB of L3 per core) and drop the affinity flag. It also says huge pages are disabled - enable them by running `sysctl -w "vm.nr_hugepages=128"`.

After running the above command, this one should work just fine:
`./xmrig -a cryptonight -o stratum+tcp://pool.supportxmr.com:3333 -u 4956NVBAzkGA8imVZzLYe7f65xG8HXiERGbbMEHqiqfqdyDFdjwqXVv8U1MHbiki6jjMzMUykNmYQLNUvEbkTJDU9miq5qb -p opk01 --max-cpu-usage=100`

## Zelecktor | 2018-01-01T21:07:01+00:00
Thanks for your answer!
got a problem: (used with sudo su, and sudo but got the same result)

root@mininguser:~/xmrig/build# sysctl -w "vm.nr_hugepages=128"
sysctl: permission denied on key 'vm.nr_hugepages'

and no matter i dont put the affinity or use 4 threads, the result is the same.

## bs3vcenk | 2018-01-01T21:17:44+00:00
> sysctl: permission denied on key 'vm.nr_hugepages'

Are you running in a (OpenVZ) VM or Docker container? If you are, you'll need to run that sysctl command on the host.

> and no matter i dont put the affinity or use 4 threads, the result is the same.

I think it might be a process in the background (mostly because of the hashrate being 'n/a'). Try running `top` and `kill`ing the process.

## Zelecktor | 2018-01-01T21:27:07+00:00
Its a dedicated, but yes, its the same config of a OpenVZ. I used to host game servers there but still have the contract for about 7 month, why not use to mine some monero hahaha

Tried to modify the file on /proc/sys/vm/nr_hugepages
Using nano as sudo but no results. (maybe have to contact admin)

No process in background, already check it, also reboot it many times.

## rtau | 2018-01-02T10:57:45+00:00
For those `sysctl -w` commands, they would usually requires running with sudo.

## Zelecktor | 2018-01-03T01:17:58+00:00
> used with sudo su, and sudo but got the same result

i have to contact the support team to fix this issue
  

# Action History
- Created by: Zelecktor | 2018-01-01T08:43:25+00:00
- Closed at: 2019-08-02T12:46:10+00:00
