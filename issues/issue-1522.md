---
title: Some calls through the DaemonManager freezes the GUI
source_url: https://github.com/monero-project/monero-gui/issues/1522
author: sanderfoobar
assignees: []
labels: []
created_at: '2018-07-25T23:31:52+00:00'
updated_at: '2020-02-24T17:56:39+00:00'
type: issue
status: closed
closed_at: '2020-02-24T17:56:38+00:00'
---

# Original Description
https://github.com/monero-project/monero-gui/blob/1107daab98ccf39a259bf1979c751e18cb92ee8b/src/daemon/DaemonManager.cpp#L230-L251

Calling the above function from QML like this:

`daemonManager.sendCommand("status",currentWallet.nettype)` 

Will freeze the main GUI thread untill the daemon responds. 

In the event that monerod is slow or otherwise unresponsive, the result is a freezing UI. On avarage it returns within 1-2 second(s) (on my computer at least).

This is because even though `QProcess` and `waitForFinished` is used - it will still freeze [as per documentation](http://doc.qt.io/qt-5/qprocess.html#waitForFinished):

> Warning: Calling this function from the main (GUI) thread might cause your user interface to freeze. 

SO says "Use signals/slots instead". [This](http://doc.qt.io/qt-5/qtconcurrentrun.html) might also be helpful. 

I am unaware of other `daemonManager` methods that make the main thread freeze. 

I do think this issue is important for the overall feel and quality of the GUI. When I have time, ill look into it, if my C++-fu reaches far enough.

Pinging @pazos, what do you think?

+enhancement

# Discussion History
## pazos | 2018-07-29T23:41:20+00:00
The easy solution is to switch to a managed monerod process, starting the daemon as a child process of the gui, but it has some cons:

- if the gui crashes monerod will exit too (or maybe left in a zombie state, but I didn't found any)
- we can't repurpose monerod used for some other thing. We need to start and use our own process (once monerod is started other devices can connect -based on configuration-)
- there is no way to keep monerod running after exiting the gui. (This can be handled with a systemtray implementation)

the pros:
- interactive communication with monerod is waaaay faster than using rpc calls.
- no need to query the daemon each few seconds for keeping track of its state.
- we don't need to issue the waitForFinished on each new monerod invokation, since we have an interactive console open.

here is a snippet to start, stop and send input to a  binary.

```
... Constructor ...

    p = new QProcess();

    // signaling stdout & stderr
    connect(p, &QProcess::readyReadStandardOutput, [&]
    {
        auto feed = p->readAllStandardOutput();
        emit onOutput(feed.toStdString());
    });

    connect(p, &QProcess::readyReadStandardError, [&]{
        auto feed = p->readAllStandardError();
        emit onError(feed.toStdString());
    });

    // signaling process stateChanged
    connect(p, &QProcess::stateChanged, [&](QProcess::ProcessState state)
    {
        if (state == QProcess::Running)
            emit onState(true);
        else
            emit onState(false);
    });

    // signaling finish
    connect(p, QOverload<int, QProcess::ExitStatus>::of(&QProcess::finished),
        [=](int exitCode, QProcess::ExitStatus exitStatus)
    {
        Q_UNUSED(exitStatus)
        std::string msg = "process finished with status ";
        msg += std::to_string(exitCode);
        emit onOutput(msg);
    });
...........

// write to process from stdin (for interactive processes)
void ProcessManager::input(std::string cmd)
{

    cmd += "\n";
    p->write(QByteArray::fromStdString(cmd));
}

void ProcessManager::start(const QString binary, const QStringList args)
{
    p->start(binary, args);
}


void ProcessManager::stop()
{
    input("exit");
}
```


## On a second thought

If you're interested on:

> Will freeze the main GUI thread untill the daemon responds.
In the event that monerod is slow or otherwise unresponsive, the result is a freezing UI. On avarage it returns within 1-2 second(s) (on my computer at least).

We can use some kind of graphical information of the action taking place and some spinner and ignore new user events until we get out the block state.



## dEBRUYNE-1 | 2018-12-29T13:19:34+00:00
@pazos:

>The easy solution is to switch to a managed monerod process, starting the daemon as a child process of the gui

Any interest in implementing this? I think the advantages significantly outweigh the disadvantages, hence my question. 

EDIT: Perhaps prudent to first discuss this with other contributors before going ahead. 

## selsta | 2020-02-24T17:56:38+00:00
This (and other calls) are now async.

# Action History
- Created by: sanderfoobar | 2018-07-25T23:31:52+00:00
- Closed at: 2020-02-24T17:56:38+00:00
