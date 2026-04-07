---
title: self-test possibility of referencing the null pointer.
source_url: https://github.com/xmrig/xmrig/issues/1309
author: yesilcimenahmet
assignees: []
labels:
- bug
created_at: '2019-11-23T14:02:43+00:00'
updated_at: '2019-11-23T17:55:08+00:00'
type: issue
status: closed
closed_at: '2019-11-23T17:55:08+00:00'
---

# Original Description
Please check the following lines in the **Workers.cpp**

When the **worker** variable is null, the following code will try to call the **id()** method of the **worker** variable.

```
void xmrig::Workers<T>::onReady(void *arg)
{
    auto handle = static_cast<Thread<T>* >(arg);

    IWorker *worker = create(handle);
    assert(worker != nullptr);

    if (!worker || !worker->selfTest()) {
        LOG_ERR("%s " "thread " "#%zu" " self-test failed", T::tag(), worker->id());

        handle->backend()->start(worker, false);
        delete worker;

        return;
    }
```

# Discussion History
## xmrig | 2019-11-23T17:55:08+00:00
Fixed. Thank you.

# Action History
- Created by: yesilcimenahmet | 2019-11-23T14:02:43+00:00
- Closed at: 2019-11-23T17:55:08+00:00
