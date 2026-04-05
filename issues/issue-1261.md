---
title: '[question] how to change hugepage value in windows 10??'
source_url: https://github.com/xmrig/xmrig/issues/1261
author: ari2asem
assignees: []
labels:
- question
created_at: '2019-11-05T00:30:58+00:00'
updated_at: '2019-12-22T19:36:01+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:36:01+00:00'
---

# Original Description
i would like to change this value in windows 10.

vm.nr_hugepages = *?*?*?

what command i can use for it? Large Pages is already enabled under Local Security Policy...

thanks in advance, erik

# Discussion History
## xmrig | 2019-11-05T15:40:28+00:00
There is no way to reserve certain amount of huge pages like Linux, if system has enough memory it will give huge pages to miner, otherwise not, closing heavy applications may help and last resort is reboot.
Thank you.

## ari2asem | 2019-11-05T19:09:58+00:00
so far i can remember when i was trying to run RandomX benchmark tool for very very first time, i had option to change the value of hugepages. but i have forgetten the command to change it again

## mechanator | 2019-11-06T12:47:03+00:00
source xmr-stak config.txt:
/*
 * LARGE PAGE SUPPORT
 * Large pages need a properly set up OS. It can be difficult if you are not used to systems administration,
 * but the performance results are worth the trouble - you will get around 20% boost. Slow memory mode is
 * meant as a backup, you won't get stellar results there. If you are running into trouble, especially
 * on Windows, please read the common issues in the README.
 *
 * By default we will try to allocate large pages. This means you need to "Run As Administrator" on Windows.
 * You need to edit your system's group policies to enable locking large pages. Here are the steps from MSDN
 *
 * 1. On the Start menu, click Run. In the Open box, type gpedit.msc.
 * 2. On the Local Group Policy Editor console, expand Computer Configuration, and then expand Windows Settings.
 * 3. Expand Security Settings, and then expand Local Policies.
 * 4. Select the User Rights Assignment folder.
 * 5. The policies will be displayed in the details pane.
 * 6. In the pane, double-click Lock pages in memory.
 * 7. In the Local Security Setting – Lock pages in memory dialog box, click Add User or Group.
 * 8. In the Select Users, Service Accounts, or Groups dialog box, add an account that you will run the miner on
 * 9. Reboot for change to take effect.
 *
 * Windows also tends to fragment memory a lot. If you are running on a system with 4-8GB of RAM you might need
 * to switch off all the auto-start applications and reboot to have a large enough chunk of contiguous memory.
 *
 * On Linux you will need to configure large page support "sudo sysctl -w vm.nr_hugepages=128" and increase your
 * ulimit -l. To do do this you need to add following lines to /etc/security/limits.conf - "* soft memlock 262144"
 * and "* hard memlock 262144". You can also do it Windows-style and simply run-as-root, but this is NOT
 * recommended for security reasons.
 *
 * Memory locking means that the kernel can't swap out the page to disk - something that is unlikely to happen on a
 * command line system that isn't starved of memory. I haven't observed any difference on a CLI Linux system between
 * locked and unlocked memory. If that is your setup see option "no_mlck".
 */


## ari2asem | 2019-11-06T20:56:46+00:00
@mechanator ..... thanks for your efforts. everything you mention, i knew that.  everything in your text ia nothing new to me,

my question is: how to change **`vm.nr_hugepages=128`** to **`vm.nr_hugepages=10240`** in windows 10?

my system has 80gb RAM memory (ecc-reg, ddr4-2666)

# Action History
- Created by: ari2asem | 2019-11-05T00:30:58+00:00
- Closed at: 2019-12-22T19:36:01+00:00
