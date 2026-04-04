---
title: 'Error in `monerod'': free(): corrupted unsorted chunks'
source_url: https://github.com/monero-project/monero/issues/8051
author: menaceone
assignees: []
labels: []
created_at: '2021-11-09T14:33:29+00:00'
updated_at: '2023-08-09T00:14:25+00:00'
type: issue
status: closed
closed_at: '2023-08-09T00:14:25+00:00'
---

# Original Description
Hello,

I'm running a Monero Container ('Oxygen Orion' (v0.17.2.3-release)) on my Ubuntu 20.04. Server, build with official Dockerfile.

Since a few days I'm getting `Error in 'monerod\': free(): corrupted unsorted chunks`  in irregular intervalls.
I'm not sure how to debug it further.
Could it be a memory problem in SW or in my Hardware?
Any suggestions?

Log:
```
2021-11-09 08:57:42.122 I SYNCHRONIZED OK
*** Error in `monerod': free(): corrupted unsorted chunks: 0x00007fabb002e9f0 ***
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x777f5)[0x7fcc0a6757f5]
/lib/x86_64-linux-gnu/libc.so.6(+0x8038a)[0x7fcc0a67e38a]
/lib/x86_64-linux-gnu/libc.so.6(cfree+0x4c)[0x7fcc0a68258c]
monerod(_ZN5boost4asio3ssl6detail11stream_coreD1Ev+0x32)[0x55c319450922]
monerod(_ZN4epee9net_utils16connection_basicD1Ev+0x305)[0x55c319ac9875]
monerod(_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEED1Ev+0x1e5)[0x55c3193fd475]
monerod(_ZN5boost6detail17sp_counted_impl_pIN4epee9net_utils10connectionINS3_4http19http_custom_handlerINS3_23connection_context_baseEEEEEE7disposeEv+0x22)[0x55c3193fd962]
monerod(_ZN5boost6detail15sp_counted_base7releaseEv+0x1a)[0x55c31935e85a]
monerod(_ZN5boost4asio6detail12wait_handlerIZN4epee9net_utils10connectionINS4_4http19http_custom_handlerINS4_23connection_context_baseEEEE11reset_timerENS_9date_time18subsecond_durationINS_10posix_time13time_durationELl1000EEEbEUlRKNS_6system10error_codeEE_NS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationESJ_m+0x191)[0x55c3193f7551]
monerod(_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0x542)[0x55c3193850b2]
monerod(_ZN4epee9net_utils18boosted_tcp_serverINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13worker_threadEv+0x2c8)[0x55c319394b78]
monerod(+0xefa905)[0x55c319df5905]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x76ba)[0x7fcc0a9cf6ba]
/lib/x86_64-linux-gnu/libc.so.6(clone+0x6d)[0x7fcc0a7054dd]
======= Memory map: ========
55c318efb000-55c31a2f1000 r-xp 00000000 00:eb 28                         /usr/local/bin/monerod
55c31a4f1000-55c31a552000 r--p 013f6000 00:eb 28                         /usr/local/bin/monerod
55c31a552000-55c31a561000 rw-p 01457000 00:eb 28                         /usr/local/bin/monerod
55c31a561000-55c31a562000 rw-p 00000000 00:00 0
55c31a562000-55c31a563000 rw-p 00000000 00:00 0
55c31a563000-55c31a5cf000 rw-p 00000000 00:00 0
55c31b187000-55c31b39f000 rw-p 00000000 00:00 0                          [heap]
7fab2ffff000-7fab40000000 rw-p 00000000 00:00 0
7fab40000000-7fab40106000 rw-p 00000000 00:00 0
7fab40106000-7fab44000000 ---p 00000000 00:00 0
7fab44000000-7fab475e1000 rw-p 00000000 00:00 0
7fab475e1000-7fab48000000 ---p 00000000 00:00 0
7fab48000000-7fab48106000 rw-p 00000000 00:00 0
7fab48106000-7fab4c000000 ---p 00000000 00:00 0
7fab4c000000-7fab4c106000 rw-p 00000000 00:00 0
7fab4c106000-7fab50000000 ---p 00000000 00:00 0
7fab50000000-7fab50106000 rw-p 00000000 00:00 0
7fab50106000-7fab54000000 ---p 00000000 00:00 0
7fab57fff000-7fab68000000 rw-p 00000000 00:00 0
7fab68000000-7fab68781000 rw-p 00000000 00:00 0
7fab68781000-7fab6c000000 ---p 00000000 00:00 0
7fab6c000000-7fab6c5ca000 rw-p 00000000 00:00 0
7fab6c5ca000-7fab70000000 ---p 00000000 00:00 0
7fab70000000-7fab7074b000 rw-p 00000000 00:00 0
7fab7074b000-7fab74000000 ---p 00000000 00:00 0
7fab75bdf000-7fab75be0000 ---p 00000000 00:00 0
7fab75be0000-7fab75ce0000 rw-p 00000000 00:00 0
7fab76501000-7fab76502000 ---p 00000000 00:00 0
7fab76502000-7fab76602000 rw-p 00000000 00:00 0
7fab76602000-7fab76603000 ---p 00000000 00:00 0
7fab76603000-7fab76703000 rw-p 00000000 00:00 0
7fab76c3a000-7fab76c50000 r-xp 00000000 00:eb 45                         /lib/x86_64-linux-gnu/libgcc_s.so.1
7fab76c50000-7fab76e4f000 ---p 00016000 00:eb 45                         /lib/x86_64-linux-gnu/libgcc_s.so.1
7fab76e4f000-7fab76e50000 rw-p 00015000 00:eb 45                         /lib/x86_64-linux-gnu/libgcc_s.so.1
7fab77743000-7fab77744000 ---p 00000000 00:00 0
7fab77744000-7fab77844000 rw-p 00000000 00:00 0
7fab77aff000-7fab77b00000 ---p 00000000 00:00 0
7fab77b00000-7fab78000000 rw-p 00000000 00:00 0
7fab78000000-7fab7ac00000 rw-p 00000000 00:00 0
7fab7ac00000-7fab7c000000 ---p 00000000 00:00 0
7fab7c000000-7fab7e761000 rw-p 00000000 00:00 0
7fab7e761000-7fab80000000 ---p 00000000 00:00 0
7fab80000000-7fab82adc000 rw-p 00000000 00:00 0
7fab82adc000-7fab84000000 ---p 00000000 00:00 0
7fab84000000-7fab86b7a000 rw-p 00000000 00:00 0
7fab86b7a000-7fab88000000 ---p 00000000 00:00 0
7fab88000000-7fab8abcb000 rw-p 00000000 00:00 0
7fab8abcb000-7fab8c000000 ---p 00000000 00:00 0
7fab8c000000-7fab8c95b000 rw-p 00000000 00:00 0
7fab8c95b000-7fab8c95c000 rw-p 00000000 00:00 0
7fab8c95c000-7fab90000000 rw-p 00000000 00:00 0
7fab90000000-7fab93020000 rw-p 00000000 00:00 0
7fab93020000-7fab94000000 ---p 00000000 00:00 0
7fab94000000-7fab96d75000 rw-p 00000000 00:00 0
7fab96d75000-7fab98000000 ---p 00000000 00:00 0
7fab98000000-7fab9bfe9000 rw-p 00000000 00:00 0
7fab9bfe9000-7fab9c000000 ---p 00000000 00:00 0
7fab9c000000-7fab9f4f2000 rw-p 00000000 00:00 0
7fab9f4f2000-7faba0000000 ---p 00000000 00:00 0
7faba0000000-7faba0021000 rw-p 00000000 00:00 0
7faba0021000-7faba4000000 ---p 00000000 00:00 0
7faba4000000-7faba4021000 rw-p 00000000 00:00 0
7faba4021000-7faba8000000 ---p 00000000 00:00 0
7faba80f4000-7faba80f5000 ---p 00000000 00:00 0
7faba80f5000-7faba85f5000 rw-p 00000000 00:00 0
7faba85f5000-7faba85f6000 ---p 00000000 00:00 0
7faba85f6000-7faba8af6000 rw-p 00000000 00:00 0
7faba8af6000-7faba8af7000 ---p 00000000 00:00 0
7faba8af7000-7faba8ff7000 rw-p 00000000 00:00 0
7faba8ff7000-7faba8ff8000 ---p 00000000 00:00 0
7faba8ff8000-7faba94f8000 rw-p 00000000 00:00 0
7faba94f8000-7faba94f9000 ---p 00000000 00:00 0
7faba94f9000-7faba99f9000 rw-p 00000000 00:00 0
7faba99f9000-7faba99fa000 ---p 00000000 00:00 0
7faba99fa000-7faba9efa000 rw-p 00000000 00:00 0
7faba9efa000-7faba9efb000 ---p 00000000 00:00 0
7faba9efb000-7fabaa3fb000 rw-p 00000000 00:00 0
7fabaa3fb000-7fabaa3fc000 ---p 00000000 00:00 0
7fabaa3fc000-7fabaa8fc000 rw-p 00000000 00:00 0
7fabaa8fc000-7fabaa8fd000 ---p 00000000 00:00 0
7fabaa8fd000-7fabaadfd000 rw-p 00000000 00:00 0
7fabaadfd000-7fabaadfe000 ---p 00000000 00:00 0
7fabaadfe000-7fabab2fe000 rw-p 00000000 00:00 0
7fabab2fe000-7fabab2ff000 ---p 00000000 00:00 0
7fabab2ff000-7fabab7ff000 rw-p 00000000 00:00 0
7fabab7ff000-7fabab800000 ---p 00000000 00:00 0
7fabab800000-7fabac000000 rw-p 00000000 00:00 0
7fabac000000-7fabafe99000 rw-p 00000000 00:00 0
7fabafe99000-7fabb0000000 ---p 00000000 00:00 0
7fabb0000000-7fabb37e9000 rw-p 00000000 00:00 0
7fabb37e9000-7fabb4000000 ---p 00000000 00:00 0
7fabb4000000-7fabb4021000 rw-p 00000000 00:00 0
7fabb4021000-7fabb8000000 ---p 00000000 00:00 0
7fabb801b000-7fabb801c000 ---p 00000000 00:00 0
7fabb801c000-7fabb851c000 rw-p 00000000 00:00 0
7fabb851c000-7fabb851d000 ---p 00000000 00:00 0
7fabb851d000-7fabb8d1d000 rw-p 00000000 00:00 0
7fabb8d1d000-7fabb8d1e000 ---p 00000000 00:00 0
7fabb8d1e000-7fabb951e000 rw-p 00000000 00:00 0
7fabb951e000-7fabb951f000 ---p 00000000 00:00 0
7fabb951f000-7fabb9d1f000 rw-p 00000000 00:00 0
7fabb9d1f000-7fabb9d20000 ---p 00000000 00:00 0
7fabb9d20000-7fabba520000 rw-p 00000000 00:00 0
7fabba520000-7fabba521000 ---p 00000000 00:00 0
7fabba521000-7fabbad21000 rw-p 00000000 00:00 0
7fabbad21000-7fabbad22000 ---p 00000000 00:00 0
7fabbad22000-7fabbb522000 rw-p 00000000 00:00 0
7fabbb522000-7fabbb523000 ---p 00000000 00:00 0
7fabbb523000-7fabbbd23000 rw-p 00000000 00:00 0
7fabbbd23000-7fcc0a2fc000 r--s 00000000 08:01 11403270                   /home/monero/.bitmonero/lmdb/data.mdb
7fcc0a2fc000-7fcc0a5fe000 rw-p 00000000 00:00 0
7fcc0a5fe000-7fcc0a7be000 r-xp 00000000 00:eb 42                         /lib/x86_64-linux-gnu/libc-2.23.so
7fcc0a7be000-7fcc0a9be000 ---p 001c0000 00:eb 42                         /lib/x86_64-linux-gnu/libc-2.23.so
7fcc0a9be000-7fcc0a9c2000 r--p 001c0000 00:eb 42                         /lib/x86_64-linux-gnu/libc-2.23.so
7fcc0a9c2000-7fcc0a9c4000 rw-p 001c4000 00:eb 42                         /lib/x86_64-linux-gnu/libc-2.23.so
7fcc0a9c4000-7fcc0a9c8000 rw-p 00000000 00:00 0
7fcc0a9c8000-7fcc0a9e0000 r-xp 00000000 00:eb 40                         /lib/x86_64-linux-gnu/libpthread-2.23.so
7fcc0a9e0000-7fcc0abdf000 ---p 00018000 00:eb 40                         /lib/x86_64-linux-gnu/libpthread-2.23.so
7fcc0abdf000-7fcc0abe0000 r--p 00017000 00:eb 40                         /lib/x86_64-linux-gnu/libpthread-2.23.so
7fcc0abe0000-7fcc0abe1000 rw-p 00018000 00:eb 40                         /lib/x86_64-linux-gnu/libpthread-2.23.so
7fcc0abe1000-7fcc0abe5000 rw-p 00000000 00:00 0
7fcc0abe5000-7fcc0aced000 r-xp 00000000 00:eb 38                         /lib/x86_64-linux-gnu/libm-2.23.so
7fcc0aced000-7fcc0aeec000 ---p 00108000 00:eb 38                         /lib/x86_64-linux-gnu/libm-2.23.so
7fcc0aeec000-7fcc0aeed000 r--p 00107000 00:eb 38                         /lib/x86_64-linux-gnu/libm-2.23.so
7fcc0aeed000-7fcc0aeee000 rw-p 00108000 00:eb 38                         /lib/x86_64-linux-gnu/libm-2.23.so
7fcc0aeee000-7fcc0aef1000 r-xp 00000000 00:eb 36                         /lib/x86_64-linux-gnu/libdl-2.23.so
7fcc0aef1000-7fcc0b0f0000 ---p 00003000 00:eb 36                         /lib/x86_64-linux-gnu/libdl-2.23.so
7fcc0b0f0000-7fcc0b0f1000 r--p 00002000 00:eb 36                         /lib/x86_64-linux-gnu/libdl-2.23.so
7fcc0b0f1000-7fcc0b0f2000 rw-p 00003000 00:eb 36                         /lib/x86_64-linux-gnu/libdl-2.23.so
7fcc0b0f2000-7fcc0b118000 r-xp 00000000 00:eb 33                         /lib/x86_64-linux-gnu/ld-2.23.so
7fcc0b133000-7fcc0b146000 r-xp 00000000 00:00 0
7fcc0b146000-7fcc0b159000 rw-p 00000000 00:00 0
7fcc0b159000-7fcc0b16c000 r-xp 00000000 00:00 0
7fcc0b16e000-7fcc0b181000 rw-p 00000000 00:00 0
7fcc0b186000-7fcc0b315000 rw-p 00000000 00:00 0
7fcc0b315000-7fcc0b317000 rw-s 00000000 08:01 11403269                   /home/monero/.bitmonero/lmdb/lock.mdb
7fcc0b317000-7fcc0b318000 r--p 00025000 00:eb 33                         /lib/x86_64-linux-gnu/ld-2.23.so
7fcc0b318000-7fcc0b319000 rw-p 00026000 00:eb 33                         /lib/x86_64-linux-gnu/ld-2.23.so
7fcc0b319000-7fcc0b31a000 rw-p 00000000 00:00 0
7ffef8cbe000-7ffef8ce1000 rw-p 00000000 00:00 0                          [stack]
7ffef8dd8000-7ffef8ddb000 r--p 00000000 00:00 0                          [vvar]
7ffef8ddb000-7ffef8ddc000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 --xp 00000000 00:00 0                  [vsyscall]
```

# Discussion History
## selsta | 2021-11-09T19:00:13+00:00
A couple things worth testing. Can you reproduce the issue with on of the following:

- `--rpc-ssl=disabled` flag added to your daemon
- latest `release-v0.17` branch
- https://github.com/monero-project/monero/pull/7759 applied

Also a debug build and full stack trace would help.

## menaceone | 2021-11-11T08:08:53+00:00
With `--rpc-ssl=disabled` the container is running fine for >24h. 

## selsta | 2021-11-11T17:12:13+00:00
I will keep this open as it's a valid issue.

## selsta | 2021-11-11T17:29:52+00:00
@menaceone It would still be really interesting if you could test #7759 + without `--rpc-ssl=disabled`, otherwise we don't know if the bug is fixed already in the rewrite or not.

Do you know how to compile it manually?

## menaceone | 2021-11-11T17:34:21+00:00
yep, I'm able to compile.
I'm checking out current `master` as #7759 is already merged, correct?

## selsta | 2021-11-11T17:35:52+00:00
it's not merged yet, you have to do:

```
git clone --recursive https://github.com/monero-project/monero
git checkout release-v0.17
git pull origin pull/7759/head
```

## selsta | 2021-11-11T17:44:00+00:00
(also `make debug` for a debug build)

## menaceone | 2021-11-11T19:29:00+00:00
Execeuted the git cmds and the last one created a merge conflict in `contrib/epee/include/net/abstract_tcp_server2.inl`.
I would say the second part is "theirs". Shall I take this?

From Line 629:
```
<<<<<<< HEAD
  //---------------------------------------------------------------------------------
    template<class t_protocol_handler>
  bool connection<t_protocol_handler>::do_send(byte_slice message) {
    TRY_ENTRY();

    // Use safe_shared_from_this, because of this is public method and it can be called on the object being deleted
    auto self = safe_shared_from_this();
    if (!self) return false;
    if (m_was_shutdown) return false;
                // TODO avoid copy

                std::uint8_t const* const message_data = message.data();
                const std::size_t message_size = message.size();

                const double factor = 32; // TODO config
                typedef long long signed int t_safe; // my t_size to avoid any overunderflow in arithmetic
                const t_safe chunksize_good = (t_safe)( 1024 * std::max(1.0,factor) );
        const t_safe chunksize_max = chunksize_good * 2 ;
                const bool allow_split = (m_connection_type == e_connection_type_RPC) ? false : true; // do not split RPC data

        CHECK_AND_ASSERT_MES(! (chunksize_max<0), false, "Negative chunksize_max" ); // make sure it is unsigned before removin sign with cast:
        long long unsigned int chunksize_max_unsigned = static_cast<long long unsigned int>( chunksize_max ) ;

        if (allow_split && (message_size > chunksize_max_unsigned)) {
                        { // LOCK: chunking
                epee::critical_region_t<decltype(m_chunking_lock)> send_guard(m_chunking_lock); // *** critical ***

                                MDEBUG("do_send() will SPLIT into small chunks, from packet="<<message_size<<" B for ptr="<<(const void*)message_data>                                // 01234567890
                                // ^^^^        (pos=0, len=4)     ;   pos:=pos+len, pos=4
                                //     ^^^^    (pos=4, len=4)     ;   pos:=pos+len, pos=8
                                //         ^^^ (pos=8, len=4)    ;

                                // const size_t bufsize = chunksize_good; // TODO safecast
                                // char* buf = new char[ bufsize ];

                                bool all_ok = true;
                                while (!message.empty()) {
                                        byte_slice chunk = message.take_slice(chunksize_good);

                                        MDEBUG("chunk_start="<<(void*)chunk.data()<<" ptr="<<(const void*)message_data<<" pos="<<(chunk.data() - mess>                                        MDEBUG("part of " << message.size() << ": pos="<<(chunk.data() - message_data) << " len="<<chunk.size());

                                        bool ok = do_send_chunk(std::move(chunk)); // <====== ***

                                        all_ok = all_ok && ok;
                                        if (!all_ok) {
                                                MDEBUG("do_send() DONE ***FAILED*** from packet="<<message_size<<" B for ptr="<<(const void*)message_>                                                MDEBUG("do_send() SEND was aborted in middle of big package - this is mostly harmless "
                                                        << " (e.g. peer closed connection) but if it causes trouble tell us at #monero-dev. " << mess>                                                return false; // partial failure in sending
                                        }
                                        // (in catch block, or uniq pointer) delete buf;
                                } // each chunk

                                MDEBUG("do_send() DONE SPLIT from packet="<<message_size<<" B for ptr="<<(const void*)message_data);
=======

  template<typename T>
  void connection<T>::cancel_handler()
  {
    if (state.protocol.released || state.protocol.wait_release)
      return;
    state.protocol.wait_release = true;
    state.lock.unlock();
    handler.release_protocol();
    state.lock.lock();
    state.protocol.wait_release = false;
    state.protocol.released = true;
    if (state.status == status_t::INTERRUPTED)
      on_interrupted();
    else if (state.status == status_t::TERMINATING)
      on_terminating();
  }

  template<typename T>
  void connection<T>::interrupt()
  {
    if (state.status != status_t::RUNNING)
      return;
    state.status = status_t::INTERRUPTED;
    cancel_timer();
    cancel_socket();
    on_interrupted();
    state.condition.notify_all();
    cancel_handler();
  }
>>>>>>> 5e49ac24b8343be333fa517136e4e319dacc72aa
```

## selsta | 2021-11-11T19:31:19+00:00
This is easier, the master version of the patch doesn't have any conflicts:

```
git clone --recursive https://github.com/monero-project/monero
git checkout master
git pull origin pull/7760/head
```

## menaceone | 2021-11-12T14:50:23+00:00
I changed the default Dockerfile from `make` to `make debug`

```
RUN set -ex && \
    git submodule init && git submodule update && \
    rm -rf build && \
[build.log](https://github.com/monero-project/monero/files/7528389/build.log)
    if [ -z "$NPROC" ] ; \
    then make debug -j$(nproc) depends target=x86_64-linux-gnu ; \
    else make debug -j$NPROC depends target=x86_64-linux-gnu ; \
    fi
```
And `make` returns an exit code greater zero. I paste the [build.log](https://github.com/monero-project/monero/files/7528395/build.log).

However I made an normal Build from master branch with pulled #7759 and ran it without the `rpc-ssl` flag.
It works absolutely fine without any Exceptions or crashes so far.
I will monitor this build and give feedback if a crash occurs.

## selsta | 2021-11-13T02:32:58+00:00
> I changed the default Dockerfile from make to make debug

Yes, the issue is that the Dockerfile uses `make depends`, which can't be simply changed to debug.

> I will monitor this build and give feedback if a crash occurs.

Thanks!

## rarealphacat | 2021-11-21T14:05:10+00:00
@menaceone  how is the build? I'm having the same error crash with v0.17.2.3

## menaceone | 2021-11-21T15:31:20+00:00
works fine for over a week now, no crash.

# Action History
- Created by: menaceone | 2021-11-09T14:33:29+00:00
- Closed at: 2023-08-09T00:14:25+00:00
