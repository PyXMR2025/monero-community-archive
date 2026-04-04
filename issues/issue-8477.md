---
title: 'monero-wallet-rpc fails to connect to daemon:'
source_url: https://github.com/monero-project/monero/issues/8477
author: sne4ker
assignees: []
labels: []
created_at: '2022-08-01T21:19:04+00:00'
updated_at: '2022-08-03T03:49:59+00:00'
type: issue
status: closed
closed_at: '2022-08-03T03:49:59+00:00'
---

# Original Description
I use the following command to start monerod:
`monerod --data-dir=/path/to/data --rpc-login <redacted>:<redacted> --rpc-bind-ip=127.0.0.1 --rpc-bind-port=8883`

I get the following output which looks absolutely fine with me:
```
2022-08-01 21:06:29.042 I Monero 'Fluorine Fermi' (v0.18.0.0-release)
2022-08-01 21:06:29.042 I Initializing cryptonote protocol...
2022-08-01 21:06:29.042 I Cryptonote protocol initialized OK
2022-08-01 21:06:29.042 I Initializing core...
2022-08-01 21:06:29.042 I Loading blockchain from folder /path/to/data/lmdb ...
2022-08-01 21:06:29.342 I Loading checkpoints
2022-08-01 21:06:29.343 I Core initialized OK
2022-08-01 21:06:29.343 I Initializing p2p server...
2022-08-01 21:06:29.346 I p2p server initialized OK
2022-08-01 21:06:29.346 I Initializing core RPC server...
2022-08-01 21:06:29.346 I Binding on 127.0.0.1 (IPv4):8883
2022-08-01 21:06:29.347 I core RPC server initialized OK on port: 8883
2022-08-01 21:06:29.347 I Starting core RPC server...
2022-08-01 21:06:29.347 I core RPC server started ok
2022-08-01 21:06:29.348 I Starting p2p net loop...
2022-08-01 21:06:30.348 I 
2022-08-01 21:06:30.348 I **********************************************************************
2022-08-01 21:06:30.348 I The daemon will start synchronizing with the network. This may take a long time to complete.
2022-08-01 21:06:30.348 I 
2022-08-01 21:06:30.348 I You can set the level of process detailization through "set_log <level|categories>" command,
2022-08-01 21:06:30.348 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2022-08-01 21:06:30.348 I 
2022-08-01 21:06:30.348 I Use the "help" command to see the list of available commands.
2022-08-01 21:06:30.348 I Use "help <command>" to see a command's documentation.
2022-08-01 21:06:30.348 I **********************************************************************
2022-08-01 21:06:30.390 I 
2022-08-01 21:06:30.390 I **********************************************************************
2022-08-01 21:06:30.390 I You are now synchronized with the network. You may now start monero-wallet-cli.
2022-08-01 21:06:30.390 I 
2022-08-01 21:06:30.390 I Use the "help" command to see the list of available commands.
2022-08-01 21:06:30.390 I **********************************************************************
```

When I then try to start monero-wallet-rpc with this command:
`monero-wallet-rpc --wallet-file=/path/to/wallet --rpc-bind-port=28084 --prompt-for-password --daemon-address=127.0.0.1:8883 --rpc-login <redacted>:<redacted>`

I get the following output with the error that it needs a connection to the daemon:
```
This is the RPC monero wallet. It needs to connect to a monero daemon to work correctly.

Monero 'Fluorine Fermi' (v0.18.0.0-release)
Logging to monero-wallet-rpc.log
2022-08-01 21:13:33.646 W Loading wallet...
Wallet password: 
2022-08-01 21:13:40.473 W Loaded wallet keys file, with public address: <redacted>
2022-08-01 21:13:40.733 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-08-01 21:13:40.733 E Initial refresh failed: no connection to daemon
2022-08-01 21:13:40.733 W Background mining not enabled. Run "set setup-background-mining 1" in monero-wallet-cli to change.
2022-08-01 21:13:40.734 I Binding on 127.0.0.1 (IPv4):28084
2022-08-01 21:13:41.999 W Starting wallet RPC server
2022-08-01 21:13:42.999 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-08-01 21:13:43.000 E Exception at while refreshing, what=no connection to daemon
2022-08-01 21:14:03.002 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-08-01 21:14:03.003 E Exception at while refreshing, what=no connection to daemon
```

# Discussion History
## selsta | 2022-08-01T21:22:56+00:00
Please post more information.

## sne4ker | 2022-08-01T21:23:54+00:00
> Please post more information.

Yes sorry I submitted accidentally before providing the description

## selsta | 2022-08-01T21:52:16+00:00
It's still not clear what you are trying to do exactly in that second command?

Why do you connect to the daemon rpc at `127.0.0.1:8883` ? With what config did you start monerod?

## sne4ker | 2022-08-01T21:56:30+00:00
> It's still not clear what you are trying to do exactly in that second command?
> 
> Why do you connect to the daemon rpc at `127.0.0.1:8883` ? With what config did you start monerod?

In the top of my description you can see that I started monerod with this command:
`monerod --data-dir=/path/to/data --rpc-login <redacted>:<redacted> --rpc-bind-ip=127.0.0.1 --rpc-bind-port=8883`

## selsta | 2022-08-01T21:59:19+00:00
Ok, sorry I'm on mobile and read the first log wrong. As a first step can you check if you can correctly connect to the daemon with the CLI / GUI wallet?

## selsta | 2022-08-01T22:01:19+00:00
It seems that you are missing `--daemon-login`

## sne4ker | 2022-08-01T22:18:24+00:00
Maybe I'm missing somethin, but is this the same as the rpc-login? Because I tried that and it still gives me the same error:
```
monero-wallet-rpc --wallet-file=/path/to/wallet --rpc-bind-port=28084 --rpc-bind-ip=127.0.0.1 --prompt-for-password --daemon-address=127.0.0.1:8883 --daemon-login daemon-user:daemon-password --rpc-login daemon-user:daemon-password 
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Fluorine Fermi' (v0.18.0.0-release)
Logging to monero-wallet-rpc.log
2022-08-01 22:13:25.270 W Loading wallet...
Wallet password: 
2022-08-01 22:13:29.925 W Loaded wallet keys file, with public address: <redacted>
2022-08-01 22:13:30.186 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-08-01 22:13:30.186 E Initial refresh failed: no connection to daemon
2022-08-01 22:13:30.186 W Background mining not enabled. Run "set setup-background-mining 1" in monero-wallet-cli to change.
2022-08-01 22:13:30.186 I Binding on 127.0.0.1 (IPv4):28084
2022-08-01 22:13:30.482 W Starting wallet RPC server
2022-08-01 22:13:31.482 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-08-01 22:13:31.482 E Exception at while refreshing, what=no connection to daemon
```

## selsta | 2022-08-01T22:19:40+00:00
It's the same you set here: `monerod --data-dir=/path/to/data --rpc-login <redacted>:<redacted> --rpc-bind-ip=127.0.0.1 --rpc-bind-port=8883`

Please try this as a first step: https://github.com/monero-project/monero/issues/8477#issuecomment-1201765646

## sne4ker | 2022-08-01T22:38:01+00:00
> It's the same you set here: `monerod --data-dir=/path/to/data --rpc-login <redacted>:<redacted> --rpc-bind-ip=127.0.0.1 --rpc-bind-port=8883`
> 
> Please try this as a first step: [#8477 (comment)](https://github.com/monero-project/monero/issues/8477#issuecomment-1201765646)

I was actually not able to correctly connect to the daemon with the cli wallet. But when I removed the passwords and rpc port specifications it somehow works now:

```
monero-wallet-rpc --wallet-file=/path/to/wallet --rpc-bind-port=28084 --rpc-bind-ip=127.0.0.1 --prompt-for-password --daemon-address=127.0.0.1:18081
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Fluorine Fermi' (v0.18.0.0-release)
Logging to monero-wallet-rpc.log
2022-08-01 22:28:10.739 W Loading wallet...
Wallet password: 
2022-08-01 22:28:13.563 W Loaded wallet keys file, with public address: <redacted>
2022-08-01 22:28:13.984 W RPC username/password is stored in file monero-wallet-rpc.28084.login
2022-08-01 22:28:13.984 W Background mining not enabled. Run "set setup-background-mining 1" in monero-wallet-cli to change.
2022-08-01 22:28:13.984 I Binding on 127.0.0.1 (IPv4):28084
2022-08-01 22:28:14.987 W Starting wallet RPC server
```

## sne4ker | 2022-08-02T05:43:01+00:00
I just checked again and now it just took about half an hour and the error appears again:
```
monero-wallet-rpc --wallet-file=/path/to/walllet --rpc-bind-port=28084 --rpc-bind-ip=127.0.0.1 --prompt-for-password --daemon-address=127.0.0.1:18081                       
This is the RPC monero wallet. It needs to connect to a monero                                                                                                                                
daemon to work correctly.                                                                                                                                                                     
                                                                                                                                                                                              
Monero 'Fluorine Fermi' (v0.18.0.0-release)                                                                                                                                                   
Logging to monero-wallet-rpc.log                                                                                                                                                              
2022-08-01 22:28:10.739 W Loading wallet...                                                                                                                                                   
Wallet password:                                                                                                                                                                              
2022-08-01 22:28:13.563 W Loaded wallet keys file, with public address: <redacted>                       
2022-08-01 22:28:13.984 W RPC username/password is stored in file monero-wallet-rpc.28084.login                                                                                               
2022-08-01 22:28:13.984 W Background mining not enabled. Run "set setup-background-mining 1" in monero-wallet-cli to change.                                                                  
2022-08-01 22:28:13.984 I Binding on 127.0.0.1 (IPv4):28084                                                                                                                                   
2022-08-01 22:28:14.987 W Starting wallet RPC server                                                                                                                                          
                                                                                                                                                                                              
2022-08-01 22:56:01.108 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon                                                                                                          
2022-08-01 22:56:01.108 E Exception at while refreshing, what=no connection to daemon 
````

But when I connect to the wallet via monero-wallet-cli everything works now:

```
monero-wallet-cli
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Fluorine Fermi' (v0.18.0.0-release)
Logging to monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): 
Error: Wallet name not valid. Please try again or use Ctrl-C to quit.
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): WalletFile
Wallet and key files found, loading...
Wallet password: 
Opened wallet: <redacted>
**********************************************************************
Use the "help" command to see a simplified list of available commands.
Use "help all" to see the list of all available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Background mining not enabled. Run "set setup-background-mining 1" to change.
Starting refresh...
Refresh done, blocks received: 0                                
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 <redacted>        <redacted>            <redacted>       Primary account
------------------------------------------------------------------------------------
          Total              <redacted>             <redacted>
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: <redacted>, unlocked balance: <redacted>
Background refresh thread started
[wallet <redacted>]:
```

## moneromooo-monero | 2022-08-02T16:25:16+00:00
What is the full monero-wallet-cli command line ?


## moneromooo-monero | 2022-08-02T16:27:14+00:00
Or is the first line the actual command line (ie, just filename without path) ?

## moneromooo-monero | 2022-08-02T16:29:40+00:00
I will assume that. So, after you start monero-wallet-rpc, run netstat to check which ports are listening, and on which a request is being made:

sudo netstat -napt

Do this will you see monero-wallet-cli sending something on a socket. If the connection succeeds, you'll see ESTABLISHED, if it gets lost you'll probably get SYN_SENT.

The problem might be the connection never gets made, or it could be the wallet doens't like what it's seeing right after connection.


## sne4ker | 2022-08-02T17:36:06+00:00
This is the command used to run monero-wallet-rpc:
`monero-wallet-rpc --wallet-file=/path/to/wallet --rpc-bind-port=28084 --rpc-bind-ip=127.0.0.1 --prompt-for-password --daemon-address=127.0.0.1:18081`

I get the following output:
```
This is the RPC monero wallet. It needs to connect to a monero daemon to work correctly.

Monero 'Fluorine Fermi' (v0.18.0.0-release)
Logging to monero-wallet-rpc.log
2022-08-02 17:13:16.646 W Loading wallet...
Wallet password: 
2022-08-02 17:13:25.970 W Loaded wallet keys file, with public address: <redacted>
2022-08-02 17:13:26.272 W RPC username/password is stored in file monero-wallet-rpc.28084.login
2022-08-02 17:13:26.272 W Background mining not enabled. Run "set setup-background-mining 1" in monero-wallet-cli to change.
2022-08-02 17:13:26.272 I Binding on 127.0.0.1 (IPv4):28084
2022-08-02 17:13:26.477 W Starting wallet RPC server
2022-08-02 17:14:47.629 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-08-02 17:14:47.630 E Exception at while refreshing, what=no connection to daemon
2022-08-02 17:15:27.898 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-08-02 17:15:27.899 E Exception at while refreshing, what=no connection to daemon
2022-08-02 17:21:49.264 W Transaction extra has unsupported format: <6f6522bac014ce5ae0f07ac5b1e0104d2956b4e36d6f09fbfee4c4e88522fb5a>
2022-08-02 17:24:49.883 W Transaction extra has unsupported format: <6f6522bac014ce5ae0f07ac5b1e0104d2956b4e36d6f09fbfee4c4e88522fb5a>
2022-08-02 17:25:09.895 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-08-02 17:25:09.895 E Exception at while refreshing, what=no connection to daemon
```
When running `netstat -napt` the connection shows as established:
```
Active Internet connections (servers and established)                                                                                                                                         
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name                                                                                              
tcp        0      0 0.0.0.0:18080           0.0.0.0:*               LISTEN      43081/monerod                                                                                                 
tcp        0      0 127.0.0.1:18081         0.0.0.0:*               LISTEN      43081/monerod                                                                                                 
tcp        0      0 127.0.0.1:18082         0.0.0.0:*               LISTEN      43081/monerod                                                                                                 
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      39499/haproxy                                                                                                 
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      29300/nginx: master                                                                                           
tcp        0      0 0.0.0.0:8081            0.0.0.0:*               LISTEN      39499/haproxy                                                                                                 
tcp        0      0 127.0.0.1:4242          0.0.0.0:*               LISTEN      39580/./monero-pool                                                                                           
tcp        0      0 127.0.0.1:4243          0.0.0.0:*               LISTEN      39580/./monero-pool                                                                                           
tcp        0      0 127.0.0.1:28084         0.0.0.0:*               LISTEN      43152/monero-wallet                                                                                           
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      804/sshd: /usr/sbin                                                                                           
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      29300/nginx: master                                                                                           
tcp        0      0 <PUBLIC_IP>:18080     	93.224.209.17:5791      ESTABLISHED 43081/monerod                                                                                                 
tcp        0   8654 <PUBLIC_IP>:18080     	92.124.136.131:48564    ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 127.0.0.1:18081         127.0.0.1:35770         ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 <PUBLIC_IP>:48318    	142.132.194.142:18080   ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 <PUBLIC_IP>:443       	162.158.129.167:47008   ESTABLISHED 29808/nginx: worker                                                                                           
tcp        0      0 <PUBLIC_IP>:18080     	76.138.189.129:46268    ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 <PUBLIC_IP>:18080     	68.12.169.74:43212      ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 <PUBLIC_IP>:49836     	65.108.60.175:18080     TIME_WAIT   -                                                                                                             
tcp        0      0 <PUBLIC_IP>:18080     	47.154.30.4:44030       ESTABLISHED 43081/monerod                                                                                                 
tcp        0      1 <PUBLIC_IP>:50034     	162.218.65.147:18080    FIN_WAIT1   -                                                                                                             
tcp        0      0 <PUBLIC_IP>:18080     	24.66.104.136:32952     ESTABLISHED 43081/monerod                                                                                                 
tcp        0    240 <PUBLIC_IP>:22        	<redacted>:35972      	ESTABLISHED 42949/sshd: <redacted>@<redacted>                                                                                           
tcp        0      0 <PUBLIC_IP>:18080     	186.22.54.132:15202     ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 <PUBLIC_IP>:39770     	165.232.177.22:18080    TIME_WAIT   -                                                                                                             
tcp        0      0 <PUBLIC_IP>:18080     	162.218.65.219:46225    ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 <PUBLIC_IP>:58800     	162.250.189.42:18080    ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 127.0.0.1:4243          127.0.0.1:41924         TIME_WAIT   -                                                                                                             
tcp        0      0 <PUBLIC_IP>:18080     	49.12.228.128:53130     ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 <PUBLIC_IP>:41358     	95.216.189.35:18080     TIME_WAIT   -                                                                                                             
tcp        0      0 <PUBLIC_IP>:18080     	159.100.254.56:48446    ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 <PUBLIC_IP>:54038     	138.201.244.138:18080   TIME_WAIT   -                                                                                                             
tcp        0      0 <PUBLIC_IP>:37076     	138.201.244.104:18080   ESTABLISHED 43081/monerod                                                                                                 
tcp        0      0 <PUBLIC_IP>:18080     	37.11.243.68:50076      ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:39696     	134.19.179.179:29942    ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:44712     	95.216.189.98:18080     TIME_WAIT   -                    
tcp        0      0 <PUBLIC_IP>:18080     	82.202.161.222:46276    ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	50.207.31.98:50643      ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:44184     	178.172.193.207:18080   ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:33712     	165.22.12.133:18080     TIME_WAIT   -                    
tcp        0      0 <PUBLIC_IP>:42430     	141.94.96.195:18080     ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	24.134.174.177:63026    ESTABLISHED 43081/monerod
tcp        0      0 <PUBLIC_IP>:18080     	221.139.1.42:34686      ESTABLISHED 43081/monerod        
tcp        0      0 127.0.0.1:35770         127.0.0.1:18081         ESTABLISHED 43152/monero-wallet 
tcp        0   3886 <PUBLIC_IP>:18080     	84.17.53.146:49150      ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	190.89.104.134:47588    TIME_WAIT   -                    
tcp        0      0 <PUBLIC_IP>:18080     	202.137.24.114:40726    ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:443       	162.158.129.121:49046   TIME_WAIT   -                    
tcp        0      0 127.0.0.1:4243          127.0.0.1:41922         TIME_WAIT   -                    
tcp        0      0 <PUBLIC_IP>:18080     	93.209.238.222:65388    ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	156.34.60.244:64296     ESTABLISHED 43081/monerod        
tcp        0  97920 <PUBLIC_IP>:18080     	221.231.171.167:18798   ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	24.205.24.204:38568     ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:49794     	217.115.120.70:18080    ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	185.204.1.226:56314     ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:22        	61.177.173.37:45434     ESTABLISHED 43178/sshd: [accept
tcp        0      0 <PUBLIC_IP>:57286     	62.166.156.32:18080     ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	178.34.150.32:22681     ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:54734     	98.61.7.251:18080       ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	103.173.178.109:36582   ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:58498     	174.128.244.217:18080   ESTABLISHED 43081/monerod        
tcp        0      1 <PUBLIC_IP>:34774     	162.218.65.169:18080    SYN_SENT    43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	72.198.16.239:1289      ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	209.222.252.155:25339   ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:18080     	103.231.88.10:34812     ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:60282     	103.231.88.10:57380     TIME_WAIT   -                    
tcp        0      0 <PUBLIC_IP>:18080     	185.220.101.183:11678   ESTABLISHED 43081/monerod        
tcp        0      0 <PUBLIC_IP>:35510     	23.88.126.25:18080      TIME_WAIT   -                    
tcp        0      0 <PUBLIC_IP>:60374     	138.201.191.51:18080    TIME_WAIT   -                    
tcp        0      1 <PUBLIC_IP>:38108     	162.218.65.165:18080    FIN_WAIT1   -                    
tcp        0      0 <PUBLIC_IP>:8080      	185.7.214.104:43382     TIME_WAIT   -                    
tcp        0      0 <PUBLIC_IP>:38940     	49.12.227.227:18080     TIME_WAIT   -                    
tcp        0      0 <PUBLIC_IP>:40644     	188.137.47.9:18080      ESTABLISHED 43081/monerod        
tcp        0      0 127.0.0.1:4242          127.0.0.1:58302         TIME_WAIT   -                    
tcp        0      0 <PUBLIC_IP>:35730     	73.162.45.57:18080      ESTABLISHED 43081/monerod        
tcp6       0      0 :::22                   :::*                    LISTEN      804/sshd: /usr/sbin
```

## sne4ker | 2022-08-02T17:38:25+00:00
> What is the full monero-wallet-cli command line ?



> Or is the first line the actual command line (ie, just filename without path) ?

Yes it's actually just `monero-wallet-cli` and then I provide the walletfile after.

## moneromooo-monero | 2022-08-02T17:44:15+00:00
> tcp        0      0 127.0.0.1:18081         127.0.0.1:35770         ESTABLISHED 43081/monerod                                                                                                 

This shows that at least one connection is made to the daemon RPC. Unless you had another wallet running, it means the wallet connected. So the issue seems to be the wallet doesn't like what the daemon says. Which boils down to a get_version call, so it's hard to see how that would fail...

Do you know how to use wireshark ? You could run this to log loopback traffic on 18081 when doing so. It'll show what data is exchanged, if any.

## sne4ker | 2022-08-02T19:18:46+00:00
There is no GUI on the machine, so I can't use wireshark, but I was able to capture the traffic using tshark. It looks like the error occurs when an rpc request is made to the monero-rpc-wallet.

First I start tshark to monitor the traffic:
`tshark -i lo -f "tcp port 18081"`

Then I start the monero-wallet-rpc:

`monero-wallet-rpc --wallet-file=/path/to/wallet --rpc-bind-port=28084 --rpc-bind-ip=127.0.0.1 --prompt-for-password --daemon-address=127.0.0.1:18081`
While the output of monero-wallet-rpc is the following:
```
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Fluorine Fermi' (v0.18.0.0-release)
Logging to monero-wallet-rpc.log
2022-08-02 19:10:15.000 W Loading wallet...
Wallet password: 
2022-08-02 19:10:19.024 W Loaded wallet keys file, with public address: <redacted>
2022-08-02 19:10:19.555 W RPC username/password is stored in file monero-wallet-rpc.28084.login
2022-08-02 19:10:19.555 W Background mining not enabled. Run "set setup-background-mining 1" in monero-wallet-cli to change.
2022-08-02 19:10:19.555 I Binding on 127.0.0.1 (IPv4):28084
2022-08-02 19:10:20.065 W Starting wallet RPC server
2022-08-02 19:10:41.199 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
```
The output of tshark is:
```
    1 0.000000000    127.0.0.1 → 127.0.0.1    TCP 74 47268 → 18081 [SYN] Seq=0 Win=65495 Len=0 MSS=65495 SACK_PERM=1 TSval=1069066954 TSecr=0 WS=128
    2 0.000007580    127.0.0.1 → 127.0.0.1    TCP 74 18081 → 47268 [SYN, ACK] Seq=0 Ack=1 Win=65483 Len=0 MSS=65495 SACK_PERM=1 TSval=1069066954 TSecr=1069066954 WS=128
    3 0.000013599    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=1 Ack=1 Win=65536 Len=0 TSval=1069066954 TSecr=1069066954
    4 0.060239888    127.0.0.1 → 127.0.0.1    TLSv1 321 Client Hello
    5 0.060244987    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=1 Ack=256 Win=65280 Len=0 TSval=1069067015 TSecr=1069067015
    6 0.067498479    127.0.0.1 → 127.0.0.1    TLSv1.3 2022 Server Hello, Change Cipher Spec, Application Data, Application Data, Application Data, Application Data
    7 0.067506788    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=256 Ack=1957 Win=64000 Len=0 TSval=1069067022 TSecr=1069067022
    8 0.150863286    127.0.0.1 → 127.0.0.1    TLSv1.3 146 Change Cipher Spec, Application Data
    9 0.150872516    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=1957 Ack=336 Win=65536 Len=0 TSval=1069067105 TSecr=1069067105
   10 0.151006162    127.0.0.1 → 127.0.0.1    TLSv1.3 224 Application Data, Application Data
   11 0.151012832    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=336 Ack=2115 Win=65408 Len=0 TSval=1069067105 TSecr=1069067105
   12 0.241071484    127.0.0.1 → 127.0.0.1    TLSv1.3 223 Application Data
   13 0.241075694    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=2115 Ack=493 Win=65408 Len=0 TSval=1069067195 TSecr=1069067195
   14 0.241091843    127.0.0.1 → 127.0.0.1    TLSv1.3 316 Application Data
   15 0.241095183    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=2115 Ack=743 Win=65280 Len=0 TSval=1069067195 TSecr=1069067195
   16 0.241492753    127.0.0.1 → 127.0.0.1    TLSv1.3 7753 Application Data
   17 0.241502363    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=743 Ack=9802 Win=61056 Len=0 TSval=1069067196 TSecr=1069067196
   18 0.241839724    127.0.0.1 → 127.0.0.1    TLSv1.3 208 Application Data
   19 0.241869143    127.0.0.1 → 127.0.0.1    TLSv1.3 7082 Application Data
   20 0.241918972    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=9802 Ack=7901 Win=65536 Len=0 TSval=1069067196 TSecr=1069067196
   21 0.388167721    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   22 0.388173571    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=7901 Ack=26208 Win=56704 Len=0 TSval=1069067342 TSecr=1069067342
   23 0.388191220    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   24 0.388195030    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=7901 Ack=42614 Win=48512 Len=0 TSval=1069067342 TSecr=1069067342
   25 0.388206990    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   26 0.388210000    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=7901 Ack=59020 Win=40320 Len=0 TSval=1069067342 TSecr=1069067342
   27 0.388221589    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   28 0.388224699    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=7901 Ack=75426 Win=32000 Len=0 TSval=1069067343 TSecr=1069067342
   29 0.388234199    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   30 0.388314447    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=7901 Ack=91832 Win=65536 Len=0 TSval=1069067343 TSecr=1069067343
   31 0.388324637    127.0.0.1 → 127.0.0.1    TLSv1.3 32834 Application Data
   32 0.388328907    127.0.0.1 → 127.0.0.1    TLSv1.3 20197 Application Data, Application Data, Application Data
   33 0.388363246    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=7901 Ack=144731 Win=65536 Len=0 TSval=1069067343 TSecr=1069067343
   34 0.390616807    127.0.0.1 → 127.0.0.1    TLSv1.3 208 Application Data
   35 0.390638387    127.0.0.1 → 127.0.0.1    TLSv1.3 4067 Application Data
   36 0.390659776    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=144731 Ack=12044 Win=65536 Len=0 TSval=1069067345 TSecr=1069067345
   37 0.481953318    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   38 0.481959607    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=12044 Ack=161137 Win=196480 Len=0 TSval=1069067436 TSecr=1069067436
   39 0.481975617    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   40 0.481979067    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=12044 Ack=177543 Win=327552 Len=0 TSval=1069067436 TSecr=1069067436
   41 0.481990767    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   42 0.481993657    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=12044 Ack=193949 Win=458496 Len=0 TSval=1069067436 TSecr=1069067436
   43 0.482004886    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   44 0.482007476    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=12044 Ack=210355 Win=589440 Len=0 TSval=1069067436 TSecr=1069067436
   45 0.482011976    127.0.0.1 → 127.0.0.1    TLSv1.3 1332 Application Data
   46 0.482013446    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=12044 Ack=211621 Win=622208 Len=0 TSval=1069067436 TSecr=1069067436
   47 0.483486758    127.0.0.1 → 127.0.0.1    TLSv1.3 159 Application Data
   48 0.483507177    127.0.0.1 → 127.0.0.1    TLSv1.3 1095 Application Data
   49 0.483529407    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=211621 Ack=13166 Win=65536 Len=0 TSval=1069067438 TSecr=1069067438
   50 0.483824349    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   51 0.483827749    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=13166 Ack=228027 Win=753152 Len=0 TSval=1069067438 TSecr=1069067438
   52 0.483842619    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   53 0.483846559    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=13166 Ack=244433 Win=884224 Len=0 TSval=1069067438 TSecr=1069067438
   54 0.483867898    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   55 0.483870588    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=13166 Ack=260839 Win=1015168 Len=0 TSval=1069067438 TSecr=1069067438
   56 0.483882668    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   57 0.483885128    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=13166 Ack=277245 Win=1146112 Len=0 TSval=1069067438 TSecr=1069067438
   58 0.483895217    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   59 0.483898057    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=13166 Ack=293651 Win=1277056 Len=0 TSval=1069067438 TSecr=1069067438
   60 0.483903657    127.0.0.1 → 127.0.0.1    TLSv1.3 5102 Application Data
   61 0.483905457    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=13166 Ack=298687 Win=1408000 Len=0 TSval=1069067438 TSecr=1069067438
   62 2.023504161    127.0.0.1 → 127.0.0.1    TLSv1.3 223 Application Data
   63 2.023531140    127.0.0.1 → 127.0.0.1    TLSv1.3 316 Application Data
   64 2.023554789    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=298687 Ack=13573 Win=65536 Len=0 TSval=1069068978 TSecr=1069068978
   65 2.024037257    127.0.0.1 → 127.0.0.1    TLSv1.3 7753 Application Data
   66 2.024047966    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=13573 Ack=306374 Win=1538944 Len=0 TSval=1069068978 TSecr=1069068978
   67 2.024331879    127.0.0.1 → 127.0.0.1    TLSv1.3 159 Application Data
   68 2.024353499    127.0.0.1 → 127.0.0.1    TLSv1.3 1095 Application Data
   69 2.024377728    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=306374 Ack=14695 Win=65536 Len=0 TSval=1069068979 TSecr=1069068979
   70 2.024490055    127.0.0.1 → 127.0.0.1    TLSv1.3 364 Application Data
   71 2.024495025    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=14695 Ack=306672 Win=1538944 Len=0 TSval=1069068979 TSecr=1069068979
   72 10.385885446    127.0.0.1 → 127.0.0.1    TCP 74 47286 → 18081 [SYN] Seq=0 Win=65495 Len=0 MSS=65495 SACK_PERM=1 TSval=1069077340 TSecr=0 WS=128
   73 10.385895376    127.0.0.1 → 127.0.0.1    TCP 74 18081 → 47286 [SYN, ACK] Seq=0 Ack=1 Win=65483 Len=0 MSS=65495 SACK_PERM=1 TSval=1069077340 TSecr=1069077340 WS=128
   74 10.385903286    127.0.0.1 → 127.0.0.1    TCP 66 47286 → 18081 [ACK] Seq=1 Ack=1 Win=65536 Len=0 TSval=1069077340 TSecr=1069077340
   75 10.385939945    127.0.0.1 → 127.0.0.1    HTTP/JSON 223 POST /json_rpc HTTP/1.1 , JavaScript Object Notation (application/json)
   76 10.385946094    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47286 [ACK] Seq=1 Ack=158 Win=65408 Len=0 TSval=1069077340 TSecr=1069077340
   77 10.386152829    127.0.0.1 → 127.0.0.1    HTTP/JSON 1302 HTTP/1.1 200 Ok , JavaScript Object Notation (application/json)
   78 10.386162279    127.0.0.1 → 127.0.0.1    TCP 66 47286 → 18081 [ACK] Seq=158 Ack=1237 Win=64384 Len=0 TSval=1069077340 TSecr=1069077340
   79 10.386180188    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47286 [FIN, ACK] Seq=1237 Ack=158 Win=65536 Len=0 TSval=1069077340 TSecr=1069077340
   80 10.386234577    127.0.0.1 → 127.0.0.1    TCP 66 47286 → 18081 [FIN, ACK] Seq=158 Ack=1238 Win=65536 Len=0 TSval=1069077341 TSecr=1069077340
   81 10.386243167    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47286 [ACK] Seq=1238 Ack=159 Win=65536 Len=0 TSval=1069077341 TSecr=1069077341
   82 22.026396008    127.0.0.1 → 127.0.0.1    TLSv1.3 223 Application Data
   83 22.026422377    127.0.0.1 → 127.0.0.1    TLSv1.3 316 Application Data
   84 22.026452856    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=306672 Ack=15102 Win=65536 Len=0 TSval=1069088981 TSecr=1069088981
   85 22.027064581    127.0.0.1 → 127.0.0.1    TLSv1.3 8348 Application Data
   86 22.027074840    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=15102 Ack=314954 Win=1670016 Len=0 TSval=1069088981 TSecr=1069088981
   87 22.027389772    127.0.0.1 → 127.0.0.1    TLSv1.3 208 Application Data
   88 22.027412422    127.0.0.1 → 127.0.0.1    TLSv1.3 1588 Application Data
   89 22.027437261    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [ACK] Seq=314954 Ack=16766 Win=65536 Len=0 TSval=1069088982 TSecr=1069088982
   90 22.156053296    127.0.0.1 → 127.0.0.1    TLSv1.3 16472 Application Data
   91 22.156059586    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=16766 Ack=331360 Win=1760000 Len=0 TSval=1069089110 TSecr=1069089110
   92 22.156074265    127.0.0.1 → 127.0.0.1    TLSv1.3 10634 Application Data
   93 22.156077815    127.0.0.1 → 127.0.0.1    TCP 66 47268 → 18081 [ACK] Seq=16766 Ack=341928 Win=1754752 Len=0 TSval=1069089110 TSecr=1069089110
   94 22.156091625    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47268 [FIN, ACK] Seq=341928 Ack=16766 Win=65536 Len=0 TSval=1069089110 TSecr=1069089110
   95 22.156768087    127.0.0.1 → 127.0.0.1    TLSv1.3 159 Application Data
   96 22.156782307    127.0.0.1 → 127.0.0.1    TCP 54 18081 → 47268 [RST] Seq=341929 Win=0 Len=0
   97 22.157668504    127.0.0.1 → 127.0.0.1    TCP 74 47306 → 18081 [SYN] Seq=0 Win=65495 Len=0 MSS=65495 SACK_PERM=1 TSval=1069089112 TSecr=0 WS=128
   98 22.157678254    127.0.0.1 → 127.0.0.1    TCP 74 18081 → 47306 [SYN, ACK] Seq=0 Ack=1 Win=65483 Len=0 MSS=65495 SACK_PERM=1 TSval=1069089112 TSecr=1069089112 WS=128
   99 22.157686444    127.0.0.1 → 127.0.0.1    TCP 66 47306 → 18081 [ACK] Seq=1 Ack=1 Win=65536 Len=0 TSval=1069089112 TSecr=1069089112
  100 22.218049057    127.0.0.1 → 127.0.0.1    TLSv1 321 Client Hello
  101 22.218057987    127.0.0.1 → 127.0.0.1    TCP 66 18081 → 47306 [ACK] Seq=1 Ack=256 Win=65280 Len=0 TSval=1069089172 TSecr=1069089172
  102 22.223174555    127.0.0.1 → 127.0.0.1    TLSv1.3 2022 Server Hello, Change Cipher Spec, Application Data, Application Data, Application Data, Application Data
  103 22.223179414    127.0.0.1 → 127.0.0.1    TCP 66 47306 → 18081 [ACK] Seq=256 Ack=1957 Win=64000 Len=0 TSval=1069089177 TSecr=1069089177
  104 22.308780805    127.0.0.1 → 127.0.0.1    TLSv1.3 146 Change Cipher Spec, Application Data
```

## sne4ker | 2022-08-03T03:49:41+00:00
I think this isn't an issue with the actual monero-wallet rpc but rather with the way the underlying pool software makes its rpc requests, as when I do an rpc request with curl i.e. get_height it returns the correct current block height and does not throw an error.

I will close this issue for you, thanks for your help.

# Action History
- Created by: sne4ker | 2022-08-01T21:19:04+00:00
- Closed at: 2022-08-03T03:49:59+00:00
