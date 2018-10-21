# Subcon test 001

This is a traning example for the Rwanda Ether community to share subcon works.

# Models

## Incentive model

 * 1st commit: you will get 100 MAK
 * 2nd commit: you will get X(2) MAK
 * n-th commit: you will get X(n) MAK
 * recurrence relation: X(n) = X(n-1) * (C(n-1) - 0.5)
 * quality coefficient: 1.0 < C < 2.0
 * C is a quality coefficient for n-th commit. If the commit was good quality, C becomes close to 2.0. On the other hand, if it was normal quality, C is close to 1.0.
 * X(n) is rounded to the nearest even for each commit.

## Example of a simulating result

# Initial Budget from a Client = 8000000 JPY (example case)
| n | X(n) | C(n) | commit hash | balance (MAK) | Client's Budget (JPY) |
|---:|---:|---:|:---| ---:|
| 1 | 100 | 1.974 | commit 404d41872bf4122dca45d5d159d47c39d6a71490 | 100 | 7999900|
| 2 | 147 | 1.939 | commit a7f59116975c02adbe6060a387e7656d4c147942 | 247 | 7999753|
| 3 | 212 | 1.631 | commit dbf68749cb635e55a5f5b63b4e1a5477752ea886 | 459 | 7999541|
| 4 | 240 | 1.559 | commit 4eaabc827342ddbc9bd095b53d5ba0b97e3c3a86 | 699 | 7999301|
| 5 | 254 | 1.918 | commit 432de77aa051ff0a5e0d9b54e08c57d9787b6729 | 953 | 7999047|
| 6 | 360 | 1.738 | commit 372ca29fba3a52bafc5d651c87fdaa0edd09ee0b | 1313 | 7998687|
| 7 | 446 | 1.588 | commit be1f3408dc8edb7ed4d7e4f0a0bc3c89dc70ecd7 | 1759 | 7998241|
| 8 | 485 | 1.983 | commit e62ee33aa63566c985e8a99c4444af4ff4555e43 | 2244 | 7997756|
| 9 | 719 | 1.988 | commit 0b71b9c08eb5a7c8401cab53f653f1d7d0a0d234 | 2963 | 7997037|
| 10 | 1070 | 1.762 | commit 84c7c1a9b56b9e76f50ad4784c31de55bf95152c | 4033 | 7995967|
| 11 | 1351 | 1.619 | commit 592a3183fb55e353d96cef12eb2361e51123c85d | 5384 | 7994616|
| 12 | 1512 | 1.541 | commit 512bc0fe91f163eda034828c4b4f5b9d49a5fbd6 | 6896 | 7993104|
| 13 | 1574 | 1.949 | commit 0348254dd0d711cdc41b4ba26b88ba85fe0a8940 | 8470 | 7991530|
| 14 | 2281 | 1.707 | commit 1a63286ada731e13de13f931cfedf44088bfe997 | 10751 | 7989249|
| 15 | 2753 | 1.854 | commit 66f442ca83276384f19fdc0373f673fe1e036983 | 13504 | 7986496|
| 16 | 3728 | 1.925 | commit 221fcee60e0fc24e4a6c62e642fec67b2c6ed01c | 17232 | 7982768|
| 17 | 5312 | 1.837 | commit 3f049a085bc2ec8d7f93fac7a9b16b22884e5a4c | 22544 | 7977456|
| 18 | 7103 | 1.812 | commit 8915165083fd6b9cbe9cba46a722033d9d43f5ee | 29647 | 7970353|
| 19 | 9319 | 1.741 | commit e031d662e79e7a542b4f06135227c7022ef23c05 | 38966 | 7961034|
| 20 | 11562 | 1.573 | commit 541606655905a53de8dfa53ae734504b79a5e02e | 50528 | 7949472|
| 21 | 12410 | 1.765 | commit a5859425031db0f23c022daf1f9f98cb15cb5a56 | 62938 | 7937062|
| 22 | 15694 | 1.659 | commit 100cf714338bcfee09f480002b12001f09cd70cb | 78632 | 7921368|
| 23 | 18194 | 1.914 | commit 622a28bc52f12a96f5e7a7c5ccd30b10070d18ce | 96826 | 7903174|
| 24 | 25730 | 1.911 | commit fb68c947c170cafd8f2cb697505e90186c850c51 | 122556 | 7877444|
| 25 | 36303 | 1.538 | commit 1e2e48c643a5fe52370c4f7a184c12af2014aa33 | 158859 | 7841141|
| 26 | 37685 | 1.739 | commit c383fbf8b40aff48b0a3f33c1979715a6599257e | 196544 | 7803456|
| 27 | 46675 | 1.501 | commit 07b4de8d32f9f67a75bb87c61fc62339e710f719 | 243219 | 7756781|
| 28 | 46717 | 1.709 | commit 6c4315d1488644134e646259b6b7def435dccd4d | 289936 | 7710064|
| 29 | 56484 | 1.585 | commit 562869eb9878ee3671f31e617526a9f7b4fb53ed | 346420 | 7653580|
| 30 | 61266 | 1.658 | commit d47b080809ef72bec7f9d2d4d230c21d8ea4130d | 407686 | 7592314|
| 31 | 70926 | 1.924 | commit 1e51feff404ac4f66bd0c000b9327dd5cbba23de | 478612 | 7521388|
| 32 | 101007 | 1.595 | commit 5bd1930e1f9d337eca4b4b8fab08d4198fa92726 | 579619 | 7420381|
| 33 | 110614 | 1.809 | commit f730d3341f6c0ee77dbd08017b3d81e8f967c46e | 690233 | 7309767|
| 34 | 144845 | 1.761 | commit a8c377afc3cfc167b71d9db589edbb4ce8d2c56b | 835078 | 7164922|
| 35 | 182675 | 1.987 | commit 55b8d74115980bbec4937ec1cadfb225c7a0ffc7 | 1017753 | 6982247|
| 36 | 271570 | 1.608 | commit 36a297976c4a9f7d8e0421878f96999b743b2238 | 1289323 | 6710677|
| 37 | 301017 | 1.879 | commit 8b2813c919e00cce0bba6493e604c029d232ab2a | 1590340 | 6409660|
| 38 | 415009 | 1.923 | commit 0b7144820449a4ad03bcdd61a6d62a074aef1a05 | 2005349 | 5994651|
| 39 | 590609 | 1.831 | commit d23e2e26dbdb2a98c0186d2897c72249fc26a260 | 2595958 | 5404042|
| 40 | 786189 | 1.598 | commit 85e800b80318251b67d2389a9f09c20b92149948 | 3382147 | 4617853|
| 41 | 863272 | 1.541 | commit 9a4dcbdd46b77201d27bc799af44a0ea13edfe54 | 4245419 | 3754581|
| 42 | 898944 | 1.729 | commit f53922715ca8a62a112005cac7f8c043aea06be1 | 5144363 | 2855637|
| 43 | 1105114 | 1.967 | commit 6a887d1f32c64ad8190f334d87c2813616a5ab6a | 6249477 | 1750523|
| 44 | 1620718 | 1.641 | commit c6d79a841d7ba70158afa6bc78ed96739de69fa0 | 7870195 | 129805|
| 45 | 129805 | 1.578 | commit 18ce50e9195b90028613d700d4dd3ef8d341fb55 | 7870195 | 0|



## Negative Incentive model

 * Annoyance: banned (1 month)
 * Cheating: banned (3 month)

# Q & A

If you have any question, please add below. It will be also counted as 1 commit. 

 * Q1:
 * Q2:

