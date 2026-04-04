---
title: p2pool isInstalled check confirm latest hashes?
source_url: https://github.com/monero-project/monero-gui/issues/4191
author: plowsof
assignees: []
labels: []
created_at: '2023-07-02T00:01:00+00:00'
updated_at: '2023-07-03T15:04:46+00:00'
type: issue
status: closed
closed_at: '2023-07-03T15:04:46+00:00'
---

# Original Description
the Monero GUI will check if a binary called p2pool is in the same dir, if not, it will download the latest version. if the user has an old p2pool binary there, the GUI wont make them update.  I expect the [isInstalled](https://github.com/plowsof/monero-gui/blob/00ca9920dcdacb28e962b8cc1f7414659d3ba907/src/p2pool/P2PoolManager.cpp#L121) function to look something like this:

```C++
bool P2PoolManager::isInstalled()
{
    if (!QFileInfo(m_p2pool).isFile())
    {
        return false;
    }

    QString validHash;

    #ifdef Q_OS_WIN
        validHash = "";
    #elif defined(Q_OS_LINUX)
        validHash = "4aed4abc7a19833a19d599416933f203df49346c67562774a980e0022b1b203f";
    #elif defined(Q_OS_MACOS_AARCH64)
        validHash = "";
    #elif defined(Q_OS_MACOS)
        validHash = "";
    #endif

    QFile file(m_p2pool);
    if (!file.open(QIODevice::ReadOnly))
    {
        return false;
    }

    QCryptographicHash hash(QCryptographicHash::Sha256);
    if (hash.addData(&file))
    {
        QString fileHash = QString::fromUtf8(hash.result().toHex());
        file.close();

        if (fileHash == validHash)
        {
            return true;
        }
    }

    return false;
}
```
this way, anyone who downloads a new version of the Monero GUI and places it in the same dir as before (and does not manually delete the old p2pool binary) will update it. 

If this is valid / intended behaviour then sech would have to list the hashes of the binaries / update those too (each p2pool update) (along with the zip hashes) .. and the verify script would require a small change also.

# Discussion History
## SChernykh | 2023-07-03T13:57:05+00:00
New version of the Monero GUI, if you run the installer (at least on Windows), will delete the old p2pool folder, so the new GUI will download new p2pool.

Checking the hash of p2pool binary will lock users from manually updating their p2pool installation.

## plowsof | 2023-07-03T15:04:46+00:00
Thanks for the information, i hadn't considered this, closing the none issue now

# Action History
- Created by: plowsof | 2023-07-02T00:01:00+00:00
- Closed at: 2023-07-03T15:04:46+00:00
