---
title: 🐞 Bug - Arch/Manjaro Linux - P2Pool permissions
source_url: https://github.com/monero-project/monero-gui/issues/4108
author: Rikj000
assignees: []
labels: []
created_at: '2023-01-25T06:46:51+00:00'
updated_at: '2025-08-21T19:36:38+00:00'
type: issue
status: closed
closed_at: '2025-08-21T16:34:09+00:00'
---

# Original Description
### Issue Description
When installing `monero-gui` and `p2pool` from the official repositories on Arch/Manjaro Linux,   
then `p2pool` will run into permission issues.

This happens because:
- The `monero-gui` and `p2pool` packages are installed in the `/usr/bin/` folder,   
    to which only the `root` user has write access, not the currently logged in user!
- The `P2PoolManager` of `monero-gui` launches `p2pool` with the same working directory as what the `monero-gui` is using.   
    So `/usr/bin/` is being used as the working directory for `p2pool`, see:
    - https://github.com/monero-project/monero-gui/blob/b7ba9437d8cca6df4ecff7f5ae38a53cac5e26b2/src/p2pool/P2PoolManager.cpp#L235
    - https://github.com/monero-project/monero-gui/blob/b7ba9437d8cca6df4ecff7f5ae38a53cac5e26b2/src/p2pool/P2PoolManager.cpp#L192

### Fix Proposal
Alter the `P2PoolManager` to launch `p2pool` under a different working directory when running on Linux.

### Reproduction steps
1. Install the `monero`, `monero-gui` and `p2pool` packages on Arch/Manjaro from the Official Repositories (community)
2. Run the `monero-gui` as the logged in user from CLI with:
    ```bash
    QT_QPA_PLATFORMTHEME=qt5ct monero-wallet-gui %u
    ```
3. Start mining with `p2pool` through the `monero-gui` *(Configured in the dropdown)*
4. Monitor the permission issues in the CLI output
    - At the start:
        ![monero-gui-p2pool-permission-issue](https://user-images.githubusercontent.com/24852597/214495611-78e95976-fc56-4a22-bfe8-966dc699ac92.png)
    - After a while of running:
        ![monero-gui-p2pool-peer-list-issue](https://user-images.githubusercontent.com/24852597/214498019-39e0d983-8cf2-4e38-afa5-804fa2b512f4.png)
5. The `monero-gui` stays stuck with Network Status `Connected + Mining` and Mining Status `Starting P2Pool`
    ![monero-gui-stuck-starting-p2pool](https://user-images.githubusercontent.com/24852597/214498152-17e9b2a2-94b8-447c-8360-b7f645d023b2.png)

### Note
When starting `p2pool` manually from CLI as following,   
then none of these permission issues occur
```bash
# Move to a directory where the currently logged in user has write-permissions
cd ~
# Run p2pool
p2pool
# Stop p2pool with CTRL+C and check if the p2pool.log file got created
ls -alh ~ | grep p2pool.log
```

### Environment
| Software | Version | Source |
| --- | --- | --- | 
| OS | Manjaro Linux x86_64 | Official Repositories (core) |
| Kernel | 5.15.89-1-MANJARO | Official Repositories (core) |
| QT5 | 5.15.8+kde+r174-1 | [Official Repositories (extra)](https://archlinux.org/packages/extra/x86_64/qt5-base/) |
| Monero | 0.18.1.2-3 | [Official Repositories (extra)](https://archlinux.org/packages/extra/x86_64/monero/) |
| Monero GUI | 0.18.1.2-2 | [Official Repositories (extra)](https://archlinux.org/packages/extra/x86_64/monero-gui/) |
| P2Pool | 2.7-1 | [Official Repositories (extra)](https://archlinux.org/packages/extra/x86_64/p2pool/) |

### Linked issues
- https://github.com/monero-project/monero-gui/issues/4246
- https://github.com/monero-project/monero-gui/issues/4022
- https://github.com/monero-project/monero-gui/issues/4001
- https://github.com/monero-project/monero-gui/issues/3938

# Discussion History
## selsta | 2023-02-02T20:16:14+00:00
p2pool integration was built with the portable binaries from getmonero.org in mind.

I thought about adding this for package managers: https://github.com/monero-project/monero-gui/pull/3926

> Alter the P2PoolManager to launch p2pool under a different working directory when running on Linux.

What would you suggest here?

## Rikj000 | 2023-02-04T09:56:06+00:00
> > Alter the P2PoolManager to launch p2pool under a different working directory when running on Linux.
> 
> What would you suggest here?

To modify the `m_p2poolPath` variable after the `m_p2pool` variable has been set in the `P2PoolManager`'s constructor.

Something like:
```cpp
#elif defined(Q_OS_UNIX)
    m_p2poolPath = QApplication::applicationDirPath();
    m_p2pool = m_p2poolPath + "/p2pool";
    m_p2poolPath = QString::fromStdString(tools::get_default_data_dir()) + "/p2pool/"; // A.k.a. m_p2poolWorkingDir
```

With above change,   
the `m_p2poold->setWorkingDirectory(m_p2poolPath);` line of the `P2PoolManager::start()` function,
should initialize the `p2pool` process under a write-able `p2pool` directory,   
inside the already existing `~/.bitmonero` folder.

However I didn't check the other occurrences/usages of `m_p2poolPath` in the rest of the `P2PoolManager` thoroughly.   
To prevent breaking anything, it might be good to introduce a new variable for this, e.g. `m_p2poolWorkingDir`,

## TBX3D | 2025-08-16T20:45:10+00:00
can we get this fixed seriously

## q7nm | 2025-08-17T07:26:36+00:00
https://github.com/SChernykh/p2pool/issues/198#issuecomment-3113160309 @TBX3D 

# Action History
- Created by: Rikj000 | 2023-01-25T06:46:51+00:00
- Closed at: 2025-08-21T16:34:09+00:00
