---
title: 'Builder kovri-all-win32 Build #852 '
source_url: https://github.com/monero-project/meta/issues/195
author: anonimal
assignees: []
labels: []
created_at: '2018-03-16T21:47:01+00:00'
updated_at: '2018-03-16T23:00:49+00:00'
type: issue
status: closed
closed_at: '2018-03-16T23:00:49+00:00'
---

# Original Description
https://build.getmonero.org/builders/kovri-all-win32/builds/852

```
warning: failed to remove build/CMakeFiles/CMakeOutput.log: Device or resource busy
warning: failed to remove build/src/client: Device or resource busy
```

```
program finished with exit code 1
elapsedTime=18.328000
exception from rmdirRecursive
Traceback (most recent call last):
  File "C:\python27\lib\threading.py", line 801, in __bootstrap_inner
    self.run()
  File "C:\python27\lib\threading.py", line 754, in run
    self.__target(*self.__args, **self.__kwargs)
  File "C:\python27\lib\site-packages\twisted\_threads\_threadworker.py", line 46, in work
    task()
  File "C:\python27\lib\site-packages\twisted\_threads\_team.py", line 190, in doWork
    task()
--- <exception caught here> ---
  File "C:\python27\lib\site-packages\twisted\python\threadpool.py", line 246, in inContext
    result = inContext.theWork()
  File "C:\python27\lib\site-packages\twisted\python\threadpool.py", line 262, in <lambda>
    inContext.theWork = lambda: context.call(ctx, func, *args, **kw)
  File "C:\python27\lib\site-packages\twisted\python\context.py", line 118, in callWithContext
    return self.currentContext().callWithContext(ctx, func, *args, **kw)
  File "C:\python27\lib\site-packages\twisted\python\context.py", line 81, in callWithContext
    return func(*args,**kw)
  File "C:\python27\lib\site-packages\buildslave\commands\utils.py", line 92, in rmdirRecursive
    rmdirRecursive(full_name)
  File "C:\python27\lib\site-packages\buildslave\commands\utils.py", line 92, in rmdirRecursive
    rmdirRecursive(full_name)
  File "C:\python27\lib\site-packages\buildslave\commands\utils.py", line 96, in rmdirRecursive
    os.remove(full_name)
exceptions.WindowsError: [Error 32] The process cannot access the file because it is being used by another process: u'C:\\msys32\\home\\buildbot\\slave\\kovri-all-win32\\build\\build\\CMakeFiles\\CMakeOutput.log'
program finished with exit code -1
```

# Discussion History
## danrmiller | 2018-03-16T22:59:08+00:00
I was changing configuration on buildbot and the windows builders don't recover well from those restarts. Here is that job run successfully: https://build.getmonero.org/builders/kovri-all-win32/builds/854

## anonimal | 2018-03-16T23:00:49+00:00
Thanks Dan.

# Action History
- Created by: anonimal | 2018-03-16T21:47:01+00:00
- Closed at: 2018-03-16T23:00:49+00:00
