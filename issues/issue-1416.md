---
title: '[DaemonManager]: use monerod in user path if available'
source_url: https://github.com/monero-project/monero-gui/issues/1416
author: pazos
assignees: []
labels: []
created_at: '2018-05-15T01:59:03+00:00'
updated_at: '2018-05-15T15:41:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
DaemonManager picks the daemon in the same folder as the wallet-gui, ignoring other possible paths.

```
diff --git a/src/daemon/DaemonManager.cpp b/src/daemon/DaemonManager.cpp
index 79db8cf..08fe2ae 100644
--- a/src/daemon/DaemonManager.cpp
+++ b/src/daemon/DaemonManager.cpp
@@ -298,15 +298,19 @@ DaemonManager::DaemonManager(QObject *parent)
     : QObject(parent)
 {
 
-    // Platform depetent path to monerod
-#ifdef Q_OS_WIN
-    m_monerod = QApplication::applicationDirPath() + "/monerod.exe";
-#elif defined(Q_OS_UNIX)
-    m_monerod = QApplication::applicationDirPath() + "/monerod";
-#endif
+    // Try to use monerod from system path if available
+    m_monerod = QStandardPaths::findExecutable("monerod");
+
+    // Fallback to monerod bundled with the application
+    if (m_monerod.length() == 0)
+        m_monerod = QStandardPaths::findExecutable("monerod",
+            (QStringList) QApplication::applicationDirPath());
 
     if (m_monerod.length() == 0) {
         qCritical() << "no daemon binary defined for current platform";
         m_has_daemon = false;
+    } else {
+        qWarning().noquote() << "Daemon: " + m_monerod;
     }
+
 }
``` 

This would allow the daemon to be in a different path than the wallet, but I'm worried about the implications of this change :/

# Discussion History
## stoffu | 2018-05-15T03:19:33+00:00
I tend to be neutral for now. In any case, I think this kind of proposal can also be submitted as a pull request.

## pazos | 2018-05-15T15:41:43+00:00
done in #1419 with other misc changes in DaemonManager

# Action History
- Created by: pazos | 2018-05-15T01:59:03+00:00
