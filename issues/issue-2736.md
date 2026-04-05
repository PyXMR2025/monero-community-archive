---
title: A lot of rejected share of "low difficulty share"
source_url: https://github.com/xmrig/xmrig/issues/2736
author: KohakuBlueleaf
assignees: []
labels: []
created_at: '2021-11-28T04:22:02+00:00'
updated_at: '2021-11-30T08:47:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Get a lot of rejected share "low-difficulty share" on different platform and different pool.
4800H with win11

in Rog Phone5, it get rejected share in very high frequency.
![image](https://user-images.githubusercontent.com/59680068/143729370-ea79e87c-0446-4500-bf42-e45c50ee6786.png)


**To Reproduce**
I don't actually know how to reproduce it.
I just run xmrig and this problem jump out.

**Expected behavior**
No rejected share of "low difficulty share" or in more low frequency.

**Required data**
tested platform: 
* Rog Phone5 with ubuntu on termux
* 5950x with win10
* 2673v3 with ubuntu20.04
* 2600E with win10
* 12700K with win11

tested version:
O meet this problem
△ in lower frequency, but also meet this problem
X doesn't meet this problem

* dev branch:
    * self complied with msvc (O)
    * self complied with gcc9.3.0 (△)
    * self complied with gcc10.3.0 (O)
* master brach:
    * self complied with gcc9.3.0 (△)
    * official binary for ubuntu 20.04 (O)
    * official binary for windows (△)

**Additional context**
My friends also meet this problem on different hardware or platform, so I think this is not a single case.



# Discussion History
## mynerzulu | 2021-11-28T18:22:48+00:00

More errors showing today.

```

[2021-11-28 12:07:27.640]  miner    speed 10s/60s/15m 6998.9 5131.0 5783.2 H/s max 22685.6 H/s
[2021-11-28 12:07:28.250]  cpu      accepted (688/1884) diff 16384 (71 ms)
[2021-11-28 12:07:30.778]  cpu      accepted (689/1884) diff 16384 (62 ms)
[2021-11-28 12:07:31.780]  cpu      accepted (690/1884) diff 16384 (65 ms)
[2021-11-28 12:07:39.458]  cpu      accepted (691/1884) diff 16384 (58 ms)
[2021-11-28 12:07:39.672]  cpu      accepted (692/1884) diff 16384 (59 ms)
[2021-11-28 12:07:42.185]  cpu      accepted (693/1884) diff 16384 (56 ms)
[2021-11-28 12:07:43.583]  cpu      accepted (694/1884) diff 16384 (57 ms)
[2021-11-28 12:07:46.230]  cpu      accepted (695/1884) diff 16384 (90 ms)
[2021-11-28 12:07:51.942]  cpu      accepted (696/1884) diff 16384 (57 ms)
[2021-11-28 12:07:53.954]  net      stratum+tcp://raptorna.011data.com:3032 invalid mining.set_difficulty notification: difficulty is not a number

[2021-11-28 12:07:53.956]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 194326
[2021-11-28 12:07:56.514]  cpu      rejected (696/1885) diff 16384 "low difficulty share of 0.632585578029744" (86 ms)
[2021-11-28 12:07:58.801]  cpu      rejected (696/1886) diff 16384 "low difficulty share of 0.26441416669604556" (68 ms)
[2021-11-28 12:07:59.626]  cpu      rejected (696/1887) diff 16384 "low difficulty share of 0.3558959827456327" (64 ms)
[2021-11-28 12:08:00.715]  cpu      rejected (696/1888) diff 16384 "low difficulty share of 0.2503947554569686" (65 ms)
[2021-11-28 12:08:01.942]  cpu      rejected (696/1889) diff 16384 "low difficulty share of 0.8874510498149618" (59 ms)
[2021-11-28 12:08:04.494]  cpu      rejected (696/1890) diff 16384 "low difficulty share of 0.35575210195069523" (124 ms)
[2021-11-28 12:08:06.144]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 194327
[2021-11-28 12:08:06.144]  cpu      GhostRider algo 1: cn/dark (512 KB)
[2021-11-28 12:08:06.144]  cpu      GhostRider algo 2: cn/turtle-lite (128 KB)
[2021-11-28 12:08:06.144]  cpu      GhostRider algo 3: cn/lite (1 MB)
[2021-11-28 12:08:06.886]  cpu      rejected (696/1891) diff 16384 "low difficulty share of 0.6175099906143441" (58 ms)
[2021-11-28 12:08:08.405]  cpu      rejected (696/1892) diff 16384 "low difficulty share of 0.3719574381261475" (62 ms)
[2021-11-28 12:08:10.486]  cpu      rejected (696/1893) diff 16384 "low difficulty share of 2.875936135917287" (56 ms)
[2021-11-28 12:08:15.112]  cpu      rejected (696/1894) diff 16384 "low difficulty share of 0.4635659856184347" (107 ms)
[2021-11-28 12:08:17.452]  cpu      accepted (697/1894) diff 16384 (57 ms)
[2021-11-28 12:08:19.068]  cpu      rejected (697/1895) diff 16384 "low difficulty share of 0.8799561964514382" (79 ms)
[2021-11-28 12:08:19.430]  cpu      rejected (697/1896) diff 16384 "low difficulty share of 0.28816016447898396" (119 ms)
[2021-11-28 12:08:19.716]  cpu      rejected (697/1897) diff 16384 "low difficulty share of 18.165523572845995" (74 ms)
[2021-11-28 12:08:20.880]  cpu      rejected (697/1898) diff 16384 "low difficulty share of 0.2723751226612982" (74 ms)
[2021-11-28 12:08:21.732]  cpu      rejected (697/1899) diff 16384 "low difficulty share of 0.4234740203538602" (68 ms)
[2021-11-28 12:08:24.627]  cpu      rejected (697/1900) diff 16384 "low difficulty share of 0.7262752029090173" (62 ms)
[2021-11-28 12:08:27.692]  miner    speed 10s/60s/15m 7136.9 7043.0 6014.0 H/s max 22685.6 H/s
[2021-11-28 12:08:27.889]  cpu      rejected (697/1901) diff 16384 "low difficulty share of 0.2904435066146254" (71 ms)
[2021-11-28 12:08:28.836]  cpu      rejected (697/1902) diff 16384 "low difficulty share of 0.34796658929966207" (57 ms)
[2021-11-28 12:08:29.690]  cpu      rejected (697/1903) diff 16384 "low difficulty share of 0.4269824493027187" (58 ms)
[2021-11-28 12:08:32.975]  cpu      rejected (697/1904) diff 16384 "low difficulty share of 0.7258169790259154" (61 ms)
[2021-11-28 12:08:34.835]  cpu      rejected (697/1905) diff 16384 "low difficulty share of 0.2682833729289973" (63 ms)
[2021-11-28 12:08:36.464]  cpu      rejected (697/1906) diff 16384 "low difficulty share of 0.2655373384742656" (59 ms)
[2021-11-28 12:08:39.653]  cpu      rejected (697/1907) diff 16384 "low difficulty share of 1.4046857378069457" (93 ms)
[2021-11-28 12:08:40.302]  cpu      rejected (697/1908) diff 16384 "low difficulty share of 0.4027275687380394" (76 ms)
[2021-11-28 12:08:40.331]  cpu      rejected (697/1909) diff 16384 "low difficulty share of 0.43659638315402854" (60 ms)
[2021-11-28 12:08:45.240]  cpu      rejected (697/1910) diff 16384 "low difficulty share of 0.3497293564295459" (60 ms)
[2021-11-28 12:08:48.865]  cpu      rejected (697/1911) diff 16384 "low difficulty share of 2.4070943833705214" (78 ms)
[2021-11-28 12:08:51.870]  cpu      rejected (697/1912) diff 16384 "low difficulty share of 0.26241349410161635" (72 ms)
[2021-11-28 12:08:55.017]  cpu      rejected (697/1913) diff 16384 "low difficulty share of 1.0725384714526858" (92 ms)
[2021-11-28 12:08:55.385]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 194328
[2021-11-28 12:08:55.386]  cpu      GhostRider algo 1: cn/fast (2 MB)
[2021-11-28 12:08:55.386]  cpu      GhostRider algo 2: cn/turtle (256 KB)
[2021-11-28 12:08:55.386]  cpu      GhostRider algo 3: cn/dark-lite (256 KB)
[2021-11-28 12:08:56.892]  cpu      rejected (697/1914) diff 16384 "low difficulty share of 0.3483353517144898" (79 ms)
[2021-11-28 12:08:59.831]  cpu      rejected (697/1915) diff 16384 "low difficulty share of 0.3398198648922949" (91 ms)
[2021-11-28 12:09:00.293]  cpu      rejected (697/1916) diff 16384 "low difficulty share of 15.613175668654423" (67 ms)
[2021-11-28 12:09:05.552]  cpu      rejected (697/1917) diff 16384 "low difficulty share of 1.115840536271956" (66 ms)
[2021-11-28 12:09:05.929]  cpu      rejected (697/1918) diff 16384 "low difficulty share of 2.3486250063065426" (66 ms)
[2021-11-28 12:09:06.947]  cpu      rejected (697/1919) diff 16384 "low difficulty share of 1.987580516743397" (83 ms)
[2021-11-28 12:09:11.619]  cpu      rejected (697/1920) diff 16384 "low difficulty share of 0.3808151548136726" (84 ms)
[2021-11-28 12:09:12.853]  cpu      rejected (697/1921) diff 16384 "low difficulty share of 0.3120604002790132" (88 ms)
[2021-11-28 12:09:14.412]  cpu      rejected (697/1922) diff 16384 "low difficulty share of 0.41294106893521126" (68 ms)
[2021-11-28 12:09:15.009]  cpu      rejected (697/1923) diff 16384 "low difficulty share of 2.03007978403861" (71 ms)
[2021-11-28 12:09:26.249]  cpu      rejected (697/1924) diff 16384 "low difficulty share of 0.3419614589397166" (111 ms)
[2021-11-28 12:09:27.746]  miner    speed 10s/60s/15m 6010.5 6534.7 6072.1 H/s max 22685.6 H/s
[2021-11-28 12:09:31.102]  cpu      rejected (697/1925) diff 16384 "low difficulty share of 0.2693278624838386" (66 ms)
[2021-11-28 12:09:32.269]  cpu      rejected (697/1926) diff 16384 "low difficulty share of 2.004950507064267" (65 ms)
[2021-11-28 12:09:33.310]  cpu      rejected (697/1927) diff 16384 "low difficulty share of 2.657446586146847" (185 ms)
[2021-11-28 12:09:40.940]  cpu      rejected (697/1928) diff 16384 "low difficulty share of 0.46816724592539233" (93 ms)
[2021-11-28 12:09:41.104]  cpu      rejected (697/1929) diff 16384 "low difficulty share of 13.380712052147915" (71 ms)
[2021-11-28 12:09:42.308]  cpu      rejected (697/1930) diff 16384 "low difficulty share of 0.7064239527935045" (66 ms)
[2021-11-28 12:09:42.461]  cpu      rejected (697/1931) diff 16384 "low difficulty share of 0.30237131297587627" (65 ms)
[2021-11-28 12:09:46.839]  cpu      rejected (697/1932) diff 16384 "low difficulty share of 0.3030229069598783" (93 ms)
[2021-11-28 12:09:47.175]  cpu      rejected (697/1933) diff 16384 "low difficulty share of 13.481107511116981" (171 ms)
[2021-11-28 12:09:47.242]  cpu      rejected (697/1934) diff 16384 "low difficulty share of 0.3229155703722466" (227 ms)
[2021-11-28 12:09:47.315]  cpu      rejected (697/1935) diff 16384 "low difficulty share of 0.7425440531197885" (162 ms)
[2021-11-28 12:09:48.219]  cpu      rejected (697/1936) diff 16384 "low difficulty share of 0.3967458568630892" (97 ms)
[2021-11-28 12:09:49.252]  cpu      rejected (697/1937) diff 16384 "low difficulty share of 1.616835586922164" (90 ms)
[2021-11-28 12:09:49.666]  cpu      rejected (697/1938) diff 16384 "low difficulty share of 0.6844020428658117" (160 ms)
[2021-11-28 12:09:49.703]  cpu      rejected (697/1939) diff 16384 "low difficulty share of 0.4642460460316916" (187 ms)
[2021-11-28 12:09:50.411]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 194328
[2021-11-28 12:09:51.079]  cpu      rejected (697/1940) diff 16384 "low difficulty share of 0.34997817641970624" (77 ms)
[2021-11-28 12:09:54.717]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 194329
[2021-11-28 12:09:54.721]  cpu      GhostRider algo 1: cn/turtle (256 KB)
[2021-11-28 12:09:54.721]  cpu      GhostRider algo 2: cn/lite (1 MB)
[2021-11-28 12:09:54.721]  cpu      GhostRider algo 3: cn/fast (2 MB)
[2021-11-28 12:09:54.759]  cpu      rejected (697/1941) diff 16384 "job not found" (29 ms)
[2021-11-28 12:10:00.008]  cpu      rejected (697/1942) diff 16384 "low difficulty share of 0.3884900125150025" (156 ms)
[2021-11-28 12:10:00.117]  cpu      rejected (697/1943) diff 16384 "low difficulty share of 0.30383643908728847" (89 ms)
[2021-11-28 12:10:03.475]  cpu      rejected (697/1944) diff 16384 "low difficulty share of 0.48427614709504235" (150 ms)
[2021-11-28 12:10:04.076]  cpu      rejected (697/1945) diff 16384 "low difficulty share of 0.40751273679659594" (81 ms)
[2021-11-28 12:10:05.245]  cpu      rejected (697/1946) diff 16384 "low difficulty share of 0.7721846850910113" (78 ms)
[2021-11-28 12:10:05.491]  cpu      rejected (697/1947) diff 16384 "low difficulty share of 0.6255639549634431" (78 ms)
[2021-11-28 12:10:08.128]  cpu      rejected (697/1948) diff 16384 "low difficulty share of 1.5367706345429317" (119 ms)
[2021-11-28 12:10:08.219]  cpu      rejected (697/1949) diff 16384 "low difficulty share of 0.276094956055717" (147 ms)
[2021-11-28 12:10:08.526]  cpu      rejected (697/1950) diff 16384 "low difficulty share of 0.9129855421629774" (80 ms)
[2021-11-28 12:10:15.373]  cpu      rejected (697/1951) diff 16384 "low difficulty share of 0.5191512785491611" (74 ms)
[2021-11-28 12:10:18.270]  cpu      rejected (697/1952) diff 16384 "low difficulty share of 0.30929031026215575" (76 ms)
[2021-11-28 12:10:27.800]  miner    speed 10s/60s/15m 3581.9 4669.8 6001.5 H/s max 22685.6 H/s
[2021-11-28 12:10:28.327]  cpu      rejected (697/1953) diff 16384 "low difficulty share of 0.6496036418384357" (102 ms)
[2021-11-28 12:10:30.469]  cpu      rejected (697/1954) diff 16384 "low difficulty share of 0.6004636763931329" (95 ms)
[2021-11-28 12:10:43.948]  cpu      rejected (697/1955) diff 16384 "low difficulty share of 0.3854672129289914" (78 ms)
[2021-11-28 12:10:44.157]  cpu      rejected (697/1956) diff 16384 "low difficulty share of 0.7028778861681166" (76 ms)
[2021-11-28 12:10:44.756]  cpu      rejected (697/1957) diff 16384 "low difficulty share of 0.27822433152697446" (74 ms)
[2021-11-28 12:10:49.039]  cpu      rejected (697/1958) diff 16384 "low difficulty share of 1.0089678214525313" (76 ms)
[2021-11-28 12:10:49.737]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 194329
[2021-11-28 12:10:51.191]  cpu      rejected (697/1959) diff 16384 "low difficulty share of 0.46573976018518" (74 ms)
[2021-11-28 12:10:59.064]  cpu      rejected (697/1960) diff 16384 "low difficulty share of 0.7395708068723427" (95 ms)
[2021-11-28 12:10:59.539]  cpu      rejected (697/1961) diff 16384 "low difficulty share of 3.711239906497919" (103 ms)
[2021-11-28 12:11:00.307]  cpu      rejected (697/1962) diff 16384 "low difficulty share of 0.4356527205215825" (106 ms)
[2021-11-28 12:11:05.484]  cpu      rejected (697/1963) diff 16384 "low difficulty share of 0.4937157863200191" (80 ms)
[2021-11-28 12:11:09.303]  cpu      rejected (697/1964) diff 16384 "low difficulty share of 5.748694660254694" (118 ms)
[2021-11-28 12:11:17.391]  cpu      rejected (697/1965) diff 16384 "low difficulty share of 0.7673127835484346" (79 ms)
[2021-11-28 12:11:17.666]  cpu      rejected (697/1966) diff 16384 "low difficulty share of 4.768853504803827" (82 ms)
[2021-11-28 12:11:18.507]  cpu      rejected (697/1967) diff 16384 "low difficulty share of 0.47590589557219803" (83 ms)
[2021-11-28 12:11:25.705]  cpu      rejected (697/1968) diff 16384 "low difficulty share of 0.29688815864321205" (77 ms)
[2021-11-28 12:11:27.859]  miner    speed 10s/60s/15m 3588.6 3584.9 5847.6 H/s max 22685.6 H/s
[2021-11-28 12:11:31.542]  cpu      rejected (697/1969) diff 16384 "low difficulty share of 1.4123020658029124" (78 ms)
[2021-11-28 12:11:37.185]  cpu      rejected (697/1970) diff 16384 "low difficulty share of 0.4290186888404489" (122 ms)
[2021-11-28 12:11:37.472]  cpu      rejected (697/1971) diff 16384 "low difficulty share of 1.2196772085011487" (78 ms)
[2021-11-28 12:11:41.172]  cpu      rejected (697/1972) diff 16384 "low difficulty share of 0.25977763016166056" (89 ms)
[2021-11-28 12:11:43.068]  cpu      rejected (697/1973) diff 16384 "low difficulty share of 1.7980105535225333" (82 ms)
[2021-11-28 12:11:44.614]  cpu      rejected (697/1974) diff 16384 "low difficulty share of 0.30419164232702023" (99 ms)
[2021-11-28 12:11:44.786]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 194329
[2021-11-28 12:11:46.666]  cpu      rejected (697/1975) diff 16384 "low difficulty share of 0.9566816760765579" (74 ms)
[2021-11-28 12:11:48.269]  cpu      rejected (697/1976) diff 16384 "low difficulty share of 0.4876507180693233" (106 ms)
[2021-11-28 12:11:51.081]  cpu      rejected (697/1977) diff 16384 "low difficulty share of 0.3742760552216292" (75 ms)
[2021-11-28 12:11:54.405]  cpu      rejected (697/1978) diff 16384 "low difficulty share of 2.1908472780977215" (79 ms)
[2021-11-28 12:11:55.090]  cpu      rejected (697/1979) diff 16384 "low difficulty share of 0.2699542068650119" (111 ms)
[2021-11-28 12:11:58.517]  cpu      rejected (697/1980) diff 16384 "low difficulty share of 5.87617632309716" (123 ms)
[2021-11-28 12:12:03.197]  cpu      rejected (697/1981) diff 16384 "low difficulty share of 0.2878282935043483" (84 ms)
[2021-11-28 12:12:19.517]  cpu      rejected (697/1982) diff 16384 "low difficulty share of 0.9841464580159434" (78 ms)
[2021-11-28 12:12:21.228]  cpu      rejected (697/1983) diff 16384 "low difficulty share of 3.424198649940916" (84 ms)
[2021-11-28 12:12:22.214]  cpu      rejected (697/1984) diff 16384 "low difficulty share of 0.382753646507558" (96 ms)
[2021-11-28 12:12:25.011]  cpu      rejected (697/1985) diff 16384 "low difficulty share of 2.9096876024493357" (88 ms)
[2021-11-28 12:12:27.914]  miner    speed 10s/60s/15m 3575.1 3583.4 5723.6 H/s max 22685.6 H/s
[2021-11-28 12:12:39.819]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 194329
[2021-11-28 12:12:43.697]  cpu      rejected (697/1986) diff 16384 "low difficulty share of 1.645864195263587" (74 ms)
[2021-11-28 12:12:48.931]  cpu      rejected (697/1987) diff 16384 "low difficulty share of 1.0454858321568787" (160 ms)
[2021-11-28 12:12:50.889]  cpu      rejected (697/1988) diff 16384 "low difficulty share of 0.752896117392906" (159 ms)
[2021-11-28 12:12:54.354]  cpu      rejected (697/1989) diff 16384 "low difficulty share of 0.3206919970064231" (179 ms)
[2021-11-28 12:13:03.610]  cpu      rejected (697/1990) diff 16384 "low difficulty share of 0.5018584216737311" (186 ms)
[2021-11-28 12:13:03.894]  cpu      rejected (697/1991) diff 16384 "low difficulty share of 0.39311153437561686" (82 ms)
[2021-11-28 12:13:06.020]  cpu      rejected (697/1992) diff 16384 "low difficulty share of 0.30857100644206736" (127 ms)
[2021-11-28 12:13:09.753]  cpu      rejected (697/1993) diff 16384 "low difficulty share of 0.6539578524368997" (124 ms)
[2021-11-28 12:13:11.196]  cpu      rejected (697/1994) diff 16384 "low difficulty share of 0.5926977336988551" (120 ms)
[2021-11-28 12:13:23.262]  cpu      rejected (697/1995) diff 16384 "low difficulty share of 0.36368219831353793" (83 ms)
[2021-11-28 12:13:24.993]  cpu      rejected (697/1996) diff 16384 "low difficulty share of 0.34971373713097165" (100 ms)
[2021-11-28 12:13:26.595]  signal   SIGHUP received, exiting
[2021-11-28 12:13:26.644]  cpu      stopped (49 ms)
```

`



## SChernykh | 2021-11-28T18:51:26+00:00
@mynerzulu you got the same problem as in https://github.com/xmrig/xmrig/issues/2737

## mynerzulu | 2021-11-29T18:15:13+00:00
This issue is now resolved in 6.16.1.
Thank you!!

## KohakuBlueleaf | 2021-11-30T08:44:39+00:00
@SChernykh My problem now is I cannot even run it in ubuntu on termux
(Get "fail to start thread" error)
(Use the same steps to compile it)
Is there any change of the compiling step?

## SChernykh | 2021-11-30T08:46:56+00:00
If you get this error it means GhostRider algorithm self-test failed, you would get rejected shares anyway. Is your compiler GCC 10.3.0 on ARM? I'll try to reproduce it.

## KohakuBlueleaf | 2021-11-30T08:47:37+00:00
@SChernykh  yes it is GCC 10.3.0 on ARM

# Action History
- Created by: KohakuBlueleaf | 2021-11-28T04:22:02+00:00
