---
title: Checkbox description text broken
source_url: https://github.com/monero-project/monero-gui/issues/2450
author: sebseb7
assignees: []
labels: []
created_at: '2019-11-21T14:15:23+00:00'
updated_at: '2020-01-22T22:27:01+00:00'
type: issue
status: closed
closed_at: '2020-01-22T22:27:01+00:00'
---

# Original Description
same for all checkboxes

![image](https://user-images.githubusercontent.com/57943861/69345540-90e53680-0c71-11ea-8891-f4e2131f972c.png)


# Discussion History
## selsta | 2019-11-21T14:17:02+00:00
What OS, Qt, GUI version are you using? Self compiled?

## sebseb7 | 2019-11-21T14:30:09+00:00
windows, self compiled, used fully updated msys (qr 5.13.2)

## sebseb7 | 2019-11-21T14:31:08+00:00
this fixes this for me
```
diff --git a/components/CheckBox.qml b/components/CheckBox.qml
index 99ea641..a248bfa 100644
--- a/components/CheckBox.qml
+++ b/components/CheckBox.qml
@@ -105,7 +105,7 @@ Item {
             font.pixelSize: checkBox.fontSize
             color: MoneroComponents.Style.defaultFontColor
             textFormat: Text.RichText
-            wrapMode: Text.Wrap
+            wrapMode: Text.NoWrap
         }
     }
```

## selsta | 2019-11-21T14:32:05+00:00
It does not happen on macOS with Qt 5.13 so I’ll look into it.

Thank you for the potential fix.

## selsta | 2019-11-21T16:04:45+00:00
@sebseb7 Using Qt 5.13.2 I can’t reproduce this on macOS. Seems to be a Windows/Linux (?) thing. Can you check the following diff?

```
diff --git a/wizard/WizardModeRemoteNodeWarning.qml b/wizard/WizardModeRemoteNodeWarning.qml
index be53b16..6c80546 100644
--- a/wizard/WizardModeRemoteNodeWarning.qml
+++ b/wizard/WizardModeRemoteNodeWarning.qml
@@ -103,6 +103,7 @@ Rectangle {
                 MoneroComponents.CheckBox {
                     id: understoodCheckbox
                     Layout.topMargin: 20
+                    Layout.fillWidth: true
                     fontSize: 16
                     text: qsTr("I understand the privacy implications of using a third-party server.") + translationManager.emptyString
                     onClicked: {
```

# Action History
- Created by: sebseb7 | 2019-11-21T14:15:23+00:00
- Closed at: 2020-01-22T22:27:01+00:00
