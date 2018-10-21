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
| 1 | 100 | 1.262 | commit 56e292ed0dac7821b12c9e8ead1c32d189ab47aa | 100 |
| 2 | 126 | 1.205 | commit d2c47c28b6d58661615552db195e4e20f85c6f24 | 226 |
| 3 | 152 | 1.331 | commit 8fb577b13d33379ae5210059e7237889b1030940 | 378 |
| 4 | 202 | 1.122 | commit 403f88f1047f18dbc6dff6dc5e30f96d2e47a16d | 580 |
| 5 | 227 | 0.911 | commit 285e70a6348ffffef80b0ef6770e0310ed1db47e | 807 |
| 6 | 207 | 0.986 | commit 404d41872bf4122dca45d5d159d47c39d6a71490 | 1014 |
| 7 | 204 | 1.480 | commit a7f59116975c02adbe6060a387e7656d4c147942 | 1218 |
| 8 | 302 | 1.346 | commit dbf68749cb635e55a5f5b63b4e1a5477752ea886 | 1520 |
| 9 | 406 | 1.204 | commit 4eaabc827342ddbc9bd095b53d5ba0b97e3c3a86 | 1926 |
| 10 | 489 | 1.289 | commit 432de77aa051ff0a5e0d9b54e08c57d9787b6729 | 2415 |
| 11 | 630 | 1.346 | commit 372ca29fba3a52bafc5d651c87fdaa0edd09ee0b | 3045 |
| 12 | 848 | 0.958 | commit be1f3408dc8edb7ed4d7e4f0a0bc3c89dc70ecd7 | 3893 |
| 13 | 813 | 1.158 | commit e62ee33aa63566c985e8a99c4444af4ff4555e43 | 4706 |
| 14 | 942 | 1.489 | commit 0b71b9c08eb5a7c8401cab53f653f1d7d0a0d234 | 5648 |
| 15 | 1403 | 1.360 | commit 84c7c1a9b56b9e76f50ad4784c31de55bf95152c | 7051 |
| 16 | 1909 | 1.245 | commit 592a3183fb55e353d96cef12eb2361e51123c85d | 8960 |
| 17 | 2378 | 0.972 | commit 512bc0fe91f163eda034828c4b4f5b9d49a5fbd6 | 11338 |
| 18 | 2310 | 1.000 | commit 0348254dd0d711cdc41b4ba26b88ba85fe0a8940 | 13648 |
| 19 | 2311 | 1.309 | commit 1a63286ada731e13de13f931cfedf44088bfe997 | 15959 |
| 20 | 3025 | 1.364 | commit 66f442ca83276384f19fdc0373f673fe1e036983 | 18984 |
| 21 | 4127 | 0.906 | commit 221fcee60e0fc24e4a6c62e642fec67b2c6ed01c | 23111 |
| 22 | 3737 | 1.094 | commit 3f049a085bc2ec8d7f93fac7a9b16b22884e5a4c | 26848 |
| 23 | 4089 | 1.478 | commit 8915165083fd6b9cbe9cba46a722033d9d43f5ee | 30937 |
| 24 | 6045 | 1.087 | commit e031d662e79e7a542b4f06135227c7022ef23c05 | 36982 |
| 25 | 6573 | 1.312 | commit 541606655905a53de8dfa53ae734504b79a5e02e | 43555 |
| 26 | 8624 | 1.046 | commit a5859425031db0f23c022daf1f9f98cb15cb5a56 | 52179 |
| 27 | 9017 | 1.470 | commit 100cf714338bcfee09f480002b12001f09cd70cb | 61196 |
| 28 | 13255 | 1.459 | commit 622a28bc52f12a96f5e7a7c5ccd30b10070d18ce | 74451 |
| 29 | 19333 | 1.194 | commit fb68c947c170cafd8f2cb697505e90186c850c51 | 93784 |
| 30 | 23088 | 1.387 | commit 1e2e48c643a5fe52370c4f7a184c12af2014aa33 | 116872 |
| 31 | 32025 | 1.079 | commit c383fbf8b40aff48b0a3f33c1979715a6599257e | 148897 |
| 32 | 34544 | 1.308 | commit 07b4de8d32f9f67a75bb87c61fc62339e710f719 | 183441 |
| 33 | 45172 | 0.970 | commit 6c4315d1488644134e646259b6b7def435dccd4d | 228613 |
| 34 | 43815 | 1.433 | commit 562869eb9878ee3671f31e617526a9f7b4fb53ed | 272428 |
| 35 | 62777 | 1.319 | commit d47b080809ef72bec7f9d2d4d230c21d8ea4130d | 335205 |
| 36 | 82780 | 1.413 | commit 1e51feff404ac4f66bd0c000b9327dd5cbba23de | 417985 |
| 37 | 117008 | 1.213 | commit 5bd1930e1f9d337eca4b4b8fab08d4198fa92726 | 534993 |
| 38 | 141877 | 1.498 | commit f730d3341f6c0ee77dbd08017b3d81e8f967c46e | 676870 |
| 39 | 212539 | 0.905 | commit a8c377afc3cfc167b71d9db589edbb4ce8d2c56b | 889409 |
| 40 | 192271 | 1.066 | commit 55b8d74115980bbec4937ec1cadfb225c7a0ffc7 | 1081680 |
| 41 | 205050 | 1.455 | commit 36a297976c4a9f7d8e0421878f96999b743b2238 | 1286730 |


## Negative Incentive plan

 * Annoyance: banned (1 month)
 * Cheating: banned (3 month)

# Q & A

If you have any question, please add below. It will be also counted as 1 commit. 

 * brah brah brah
 * brah brah brah

