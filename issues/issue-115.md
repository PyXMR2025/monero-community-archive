---
title: I want to use miner with VirtualAlloct method
source_url: https://github.com/xmrig/xmrig/issues/115
author: mk148a
assignees: []
labels:
- av
created_at: '2017-09-18T20:14:58+00:00'
updated_at: '2018-02-23T21:12:29+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:53:05+00:00'
---

# Original Description
Hi, this miner is not working my pc because i have antivirus its protected with password so i cant change exclude list for antivirus :S and av is detect miner. I need to run this program to memory maybe its be undetectable. But i have error if i use Invoke Method or other call method

**# Method 1**

           byte[] body =File.ReadAllBytes("xmrig.exe");
            FileStream fs = new FileStream("xmr.exe", FileMode.Open);
            BinaryReader br = new BinaryReader(fs);
            byte[] bin = br.ReadBytes(Convert.ToInt32(fs.Length));
            fs.Close();
            br.Close();
            Assembly a = Assembly.Load(bin);
            MethodInfo method = a.EntryPoint;

            object o = a.CreateInstance(method.Name);
            // invoke the application starting point
            method.Invoke(o, null);

**# Method 2**

  ```
  byte[] x = File.ReadAllBytes("xmrig.exe");
                UInt32 funcAddr = VirtualAlloc(0, (UInt32)x.Length, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
                Marshal.Copy(x, 0, (IntPtr)(funcAddr), x.Length);
                IntPtr hThread = IntPtr.Zero;
                UInt32 threadId = 0;

                // Prepare data
                IntPtr pinfo = IntPtr.Zero;

                // Invoke the program
                hThread = CreateThread(0, 0, funcAddr, pinfo, 0, ref threadId);
                WaitForSingleObject(hThread, 0xFFFFFFFF);

```




**I have error in both. "BadImageFormatException".

My question is how to run this miner from memory?**


Another way
 i have c# app for controlling my miners, xmrig is embeded in resources my controll app. Xmrig language is c++ how can add this project to my c# app, or can i add like dll?
(for example xmrig=new xmrig(pool adress, pool username,pool pass); xmrig.start(); can i use it like this? )

# Discussion History
## esfomeado | 2017-09-19T13:20:46+00:00
What is the antivirus that you use?

## mk148a | 2017-09-23T16:35:37+00:00
Qihoo 360 Total Security  with password protect, i cant disable and change settings

# Action History
- Created by: mk148a | 2017-09-18T20:14:58+00:00
- Closed at: 2017-10-02T11:53:05+00:00
