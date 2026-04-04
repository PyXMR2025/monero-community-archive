---
title: PID failure at service restart - possible p2p socks5 issues, or external /mnt/
source_url: https://github.com/monero-project/monero-gui/issues/4523
author: hal9000node
assignees: []
labels: []
created_at: '2025-11-13T11:48:24+00:00'
updated_at: '2025-11-13T19:22:32+00:00'
type: issue
status: closed
closed_at: '2025-11-13T19:22:32+00:00'
---

# Original Description
Trying to follow the instructions here.   [Running a Monero Node via Systemd](https://docs.getmonero.org/running-node/monerod-systemd/)


- This appears to be an 'official user guide' for deploying a full node and Tor hidden service by cli and enabling the p2p connectivity over Tor.

- I have mounted a 2TB ssd at sdc1 and it is persistent at /mnt/MONERO_NODE/

- Tor service is enabled and working, ufw is enabled and working.


The gist of the user guide is as follows.

- create directories (blockchain dir at /mnt/MONERO_NODE/monero)
- download GUI tar
- extract
- move binaries to /bin/
- write to .conf and .service systemd files
- enable monerod service
- SKIP opening ports (Tor)
- switch to root and configure torrc and hidden service
- Get onion address, and,
- update .config file with onion address and tor proxy


DESCRIPTION OF ISSUE.

1. You can basically speedrun this install guide, and it works at first instance. ✔
2. A system reboot seems to break the p2p connection / handshake.  I did not wait for IBD to sync.
3. I can not seem to restore the working state.
4. GPT assist thinks its write permissions to /mnt/ and we attempted PreExec settings such as mkdir /run/monero, chown /mnt (all Failed)
5. GPT is unable to correctly troubleshoot the p2p connectivity; we just seem to be collaborating to break things at this point.

# Discussion History
## nahuhh | 2025-11-13T13:03:54+00:00
Logs

## hal9000node | 2025-11-13T18:27:35+00:00
● monerod.service - Monero Daemon
     Loaded: loaded (/etc/systemd/system/monerod.service; enabled; preset: enabled)
     Active: activating (auto-restart) (Result: exit-code) since Thu 2025-11-13 13:23:52 EST; 5s ago
    Process: 42888 ExecStartPre=/bin/mkdir -p /run/monero (code=exited, status=0/SUCCESS)
    Process: 42890 ExecStartPre=/bin/chown monero:monero /run/monero (code=exited, status=0/SUCCESS)
    Process: 42892 ExecStart=/usr/local/bin/monerod --detach --config-file /etc/monero/monerod.conf --pidfile /run/monero/monerod.pid (code=exited, status=0/SUCCESS)
    Process: 42895 ExecStartPost=/bin/sleep 0.1 (code=exited, status=0/SUCCESS)
   Main PID: 42894 (code=exited, status=1/FAILURE)
        CPU: 196ms



A start job for unit monerod.service has finished successfully.
░░ 
░░ The job identifier is 242815.
Nov 13 13:23:48 LivingRoom systemd[1]: monerod.service: Main process exited, code=exited, status=1/FAILURE
░░ Subject: Unit process exited
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ An ExecStart= process belonging to unit monerod.service has exited.
░░ 
░░ The process' exit code is 'exited' and its exit status is 1.
Nov 13 13:23:48 LivingRoom systemd[1]: monerod.service: Failed with result 'exit-code'.
░░ Subject: Unit failed
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ The unit monerod.service has entered the 'failed' state with result 'exit-code'.
Nov 13 13:23:51 LivingRoom systemd[1]: Stopped monerod.service - Monero Daemon.
░░ Subject: A stop job for unit monerod.service has finished
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ A stop job for unit monerod.service has finished.
░░ 
░░ The job identifier is 242926 and the job result is done.
Nov 13 13:23:51 LivingRoom systemd[1]: Starting monerod.service - Monero Daemon...
░░ Subject: A start job for unit monerod.service has begun execution
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ A start job for unit monerod.service has begun execution.
░░ 
░░ The job identifier is 242926.
Nov 13 13:23:51 LivingRoom monerod[42892]: 2025-11-13 18:23:51.949        I Monero 'Fluorine Fermi' (v0.18.4.3-release)
Nov 13 13:23:51 LivingRoom monerod[42892]: Forking to background...
Nov 13 13:23:52 LivingRoom systemd[1]: monerod.service: Main process exited, code=exited, status=1/FAILURE
░░ Subject: Unit process exited
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ An ExecStart= process belonging to unit monerod.service has exited.
░░ 
░░ The process' exit code is 'exited' and its exit status is 1.
Nov 13 13:23:52 LivingRoom systemd[1]: monerod.service: Failed to parse PID from file /run/monero/monerod.pid: No such process
Nov 13 13:23:52 LivingRoom systemd[1]: monerod.service: Failed with result 'exit-code'.
░░ Subject: Unit failed
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ The unit monerod.service has entered the 'failed' state with result 'exit-code'.
Nov 13 13:23:52 LivingRoom systemd[1]: Failed to start monerod.service - Monero Daemon.
░░ Subject: A start job for unit monerod.service has failed
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ A start job for unit monerod.service has finished with a failure.
░░ 
░░ The job identifier is 242926 and the job result is failed.
lines 4951-5008/5008 (END)



## nahuhh | 2025-11-13T18:48:44+00:00
Sorry, the monerod logs.

might also be helpful to set --log-level 2 on monerod

## hal9000node | 2025-11-13T19:04:09+00:00
2025-11-13 18:58:39.138	I Moving from main() into the daemonize now.
2025-11-13 18:58:39.138	I Initializing cryptonote protocol...
2025-11-13 18:58:39.138	I Cryptonote protocol initialized OK
2025-11-13 18:58:39.138	I Initializing core...
2025-11-13 18:58:39.138	I Loading blockchain from folder /mnt/MONERO_NODE/monero/bitmonero/lmdb ...
2025-11-13 18:58:39.138	D option: fast
2025-11-13 18:58:39.139	D option: async
2025-11-13 18:58:39.139	D option: 250000000bytes
2025-11-13 18:58:39.142	D DB map size:     6078439936
2025-11-13 18:58:39.143	D Space used:      4851503104
2025-11-13 18:58:39.143	D Space remaining: 1226936832
2025-11-13 18:58:39.143	D Size threshold:  0
2025-11-13 18:58:39.143	D Percent used: 79.8149  Percent threshold: 90.0000
2025-11-13 18:58:39.143	D Setting m_height to: 488172
2025-11-13 18:58:39.494	D init done
2025-11-13 18:58:39.494	I batch transaction mode already enabled, but asked to enable batch mode
2025-11-13 18:58:39.494	I batch transactions enabled
2025-11-13 18:58:39.494	D DB map size:     6078439936
2025-11-13 18:58:39.494	D Space used:      4851503104
2025-11-13 18:58:39.494	D Space remaining: 1226936832
2025-11-13 18:58:39.494	D Size threshold:  0
2025-11-13 18:58:39.494	D Percent used: 79.8149  Percent threshold: 90.0000
2025-11-13 18:58:39.625	I Loading precomputed blocks (439492 bytes)
2025-11-13 18:58:39.627	I precomputed blocks hash: <4725ea463d1520b56ce7cd54dd478d44f976e65d73ad6fe01c427eff854ecf79>, expected 4725ea463d1520b56ce7cd54dd478d44f976e65d73ad6fe01c427eff854ecf79
2025-11-13 18:58:39.695	I 6867 block hashes loaded
2025-11-13 18:58:39.705	I Blockchain initialized. last block: 488171, d3888.h18.m16.s7 time ago, current difficulty: 911446496
2025-11-13 18:58:39.707	I Validating txpool contents for v1
2025-11-13 18:58:39.707	D DB map size:     6078439936
2025-11-13 18:58:39.707	D Space used:      4851503104
2025-11-13 18:58:39.707	D Space remaining: 1226936832
2025-11-13 18:58:39.707	D Size threshold:  0
2025-11-13 18:58:39.707	D Percent used: 79.8149  Percent threshold: 90.0000
2025-11-13 18:58:39.707	I Loading checkpoints
2025-11-13 18:58:39.708	I Blockchain checkpoints file not found
2025-11-13 18:58:39.708	D DB map size:     6078439936
2025-11-13 18:58:39.708	D Space used:      4851503104
2025-11-13 18:58:39.708	D Space remaining: 1226936832
2025-11-13 18:58:39.708	D Size threshold:  0
2025-11-13 18:58:39.708	D Percent used: 79.8149  Percent threshold: 90.0000

_**[redacted - checkpoint data]**_

2025-11-13 18:58:39.708	I Core initialized OK
2025-11-13 18:58:39.708	I Initializing p2p server...
2025-11-13 18:58:39.710	D Found 0 out connections having height >= 488172
2025-11-13 18:58:39.711	I Setting LIMIT: 1.04858e+06 kbps
2025-11-13 18:58:39.711	I Set limit-up to 1048576 kB/s
2025-11-13 18:58:39.711	I Setting LIMIT: 1.04858e+06 kbps
2025-11-13 18:58:39.711	I Setting LIMIT: 1.04858e+06 kbps
2025-11-13 18:58:39.711	I Set limit-down to 1048576 kB/s
2025-11-13 18:58:39.712	E Invalid inbound address (http://ogqmtkpff6frzzcogni2s7qvsvbh2fo6gpawmf3z2pvxspnoc5mjzgid.onion:18084) for --anonymous-inbound: Network address not supported
2025-11-13 18:58:39.712	E Failed to handle command line
2025-11-13 18:58:39.712	I Deinitializing core...
2025-11-13 18:58:39.725	I Stopping cryptonote protocol...
2025-11-13 18:58:39.725	I Cryptonote protocol stopped successfully
2025-11-13 18:58:39.725	E Exception in main! Failed to initialize p2p server.


## nahuhh | 2025-11-13T19:08:01+00:00
Remove the "http://" portion from the onion

## hal9000node | 2025-11-13T19:14:33+00:00
ok I gotta tell you I tried that yesterday and it didn't work  !?
now I tried it today, and it worked.  But I would not close the issue until it survives a crash reboot....brb

and, thank-you

## hal9000node | 2025-11-13T19:22:32+00:00
I can't believe that was the problem ✔✔✔
I was about to refine this machine for precious metals yesterday.

Thanks again.

# Action History
- Created by: hal9000node | 2025-11-13T11:48:24+00:00
- Closed at: 2025-11-13T19:22:32+00:00
