# Subcon test 001

This is a traning example for the Rwanda Ether community to share subcon works.

# Roughly Design

## Incentive plan

 * 1st commit: +100 MAK
 * 2nd commit: + X(1) MAK, the X(1) depends on the first commit.
 * n-th commit: + X(n-1) MAK, the X(n-1) depends on the (n-1) th commit.
 * X(n) = X(n-1) * C(n-1), 0.5 < C(n-1) < 1.5
 * C(n) is a quality coefficient for n-th commit. If the commit was good quality, C is larger than 1.0. On the other hand, if it was not so good, C is less than 1.0.
 * each X(n) is rounded to the nearest even.

## Example of a simulating result

| n | X(n) | C(n) | commit hash | balance (MAK) |
|---:|---:|---:|:---| ---:|
| 1 | 100 | 1.490 | commit 56e292ed0dac7821b12c9e8ead1c32d189ab47aa | 100 |
| 2 | 149 | 0.918 | commit d2c47c28b6d58661615552db195e4e20f85c6f24 | 249 |
| 3 | 137 | 1.277 | commit 8fb577b13d33379ae5210059e7237889b1030940 | 386 |
| 4 | 175 | 1.471 | commit 403f88f1047f18dbc6dff6dc5e30f96d2e47a16d | 561 |
| 5 | 257 | 0.982 | commit 285e70a6348ffffef80b0ef6770e0310ed1db47e | 818 |
| 6 | 252 | 1.086 | commit 404d41872bf4122dca45d5d159d47c39d6a71490 | 1070 |
| 7 | 274 | 1.328 | commit a7f59116975c02adbe6060a387e7656d4c147942 | 1344 |
| 8 | 364 | 1.438 | commit dbf68749cb635e55a5f5b63b4e1a5477752ea886 | 1708 |
| 9 | 523 | 1.388 | commit 4eaabc827342ddbc9bd095b53d5ba0b97e3c3a86 | 2231 |
| 10 | 726 | 1.459 | commit 432de77aa051ff0a5e0d9b54e08c57d9787b6729 | 2957 |
| 11 | 1059 | 1.147 | commit 372ca29fba3a52bafc5d651c87fdaa0edd09ee0b | 4016 |
| 12 | 1215 | 1.482 | commit be1f3408dc8edb7ed4d7e4f0a0bc3c89dc70ecd7 | 5231 |
| 13 | 1801 | 1.033 | commit e62ee33aa63566c985e8a99c4444af4ff4555e43 | 7032 |
| 14 | 1861 | 1.294 | commit 0b71b9c08eb5a7c8401cab53f653f1d7d0a0d234 | 8893 |
| 15 | 2408 | 1.391 | commit 84c7c1a9b56b9e76f50ad4784c31de55bf95152c | 11301 |
| 16 | 3349 | 1.263 | commit 592a3183fb55e353d96cef12eb2361e51123c85d | 14650 |
| 17 | 4231 | 1.478 | commit 512bc0fe91f163eda034828c4b4f5b9d49a5fbd6 | 18881 |
| 18 | 6255 | 1.176 | commit 0348254dd0d711cdc41b4ba26b88ba85fe0a8940 | 25136 |
| 19 | 7357 | 1.302 | commit 1a63286ada731e13de13f931cfedf44088bfe997 | 32493 |
| 20 | 9576 | 1.457 | commit 66f442ca83276384f19fdc0373f673fe1e036983 | 42069 |
| 21 | 13955 | 0.970 | commit 221fcee60e0fc24e4a6c62e642fec67b2c6ed01c | 56024 |
| 22 | 13539 | 0.950 | commit 3f049a085bc2ec8d7f93fac7a9b16b22884e5a4c | 69563 |
| 23 | 12863 | 1.325 | commit 8915165083fd6b9cbe9cba46a722033d9d43f5ee | 82426 |
| 24 | 17044 | 1.403 | commit e031d662e79e7a542b4f06135227c7022ef23c05 | 99470 |
| 25 | 23915 | 1.078 | commit 541606655905a53de8dfa53ae734504b79a5e02e | 123385 |
| 26 | 25774 | 0.959 | commit a5859425031db0f23c022daf1f9f98cb15cb5a56 | 149159 |
| 27 | 24722 | 1.426 | commit 100cf714338bcfee09f480002b12001f09cd70cb | 173881 |
| 28 | 35262 | 1.180 | commit 622a28bc52f12a96f5e7a7c5ccd30b10070d18ce | 209143 |
| 29 | 41618 | 1.396 | commit fb68c947c170cafd8f2cb697505e90186c850c51 | 250761 |
| 30 | 58090 | 1.246 | commit 1e2e48c643a5fe52370c4f7a184c12af2014aa33 | 308851 |
| 31 | 72365 | 1.401 | commit c383fbf8b40aff48b0a3f33c1979715a6599257e | 381216 |
| 32 | 101355 | 0.967 | commit 07b4de8d32f9f67a75bb87c61fc62339e710f719 | 482571 |
| 33 | 98013 | 1.167 | commit 6c4315d1488644134e646259b6b7def435dccd4d | 580584 |
| 34 | 114371 | 1.166 | commit 562869eb9878ee3671f31e617526a9f7b4fb53ed | 694955 |
| 35 | 133408 | 1.093 | commit d47b080809ef72bec7f9d2d4d230c21d8ea4130d | 828363 |
| 36 | 145751 | 1.211 | commit 1e51feff404ac4f66bd0c000b9327dd5cbba23de | 974114 |
| 37 | 176434 | 1.417 | commit 5bd1930e1f9d337eca4b4b8fab08d4198fa92726 | 1150548 |
| 38 | 250016 | 1.483 | commit f730d3341f6c0ee77dbd08017b3d81e8f967c46e | 1400564 |
| 39 | 370753 | 1.195 | commit a8c377afc3cfc167b71d9db589edbb4ce8d2c56b | 1771317 |
| 40 | 443199 | 1.495 | commit 55b8d74115980bbec4937ec1cadfb225c7a0ffc7 | 2214516 |
| 41 | 662533 | 1.085 | commit 36a297976c4a9f7d8e0421878f96999b743b2238 | 2877049 |
| 42 | 719113 | 1.214 | commit 8b2813c919e00cce0bba6493e604c029d232ab2a | 3596162 |
| 43 | 872853 | 1.404 | commit 0b7144820449a4ad03bcdd61a6d62a074aef1a05 | 4469015 |


## Negative Incentive plan

 * Annoyance: banned (1 month)
 * Cheating: banned (3 month)

# Q & A

If you have any question, please add below. It will be also counted as 1 commit. 

 * brah brah brah
 * brah brah brah

