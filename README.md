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

| n | X(n) | C(n) | commit hash | balance (MAK) |
|---:|---:|---:|:---| ---:|
| 1 | 100 | 1.914 | commit 56e292ed0dac7821b12c9e8ead1c32d189ab47aa | 100 |
| 2 | 141 | 1.781 | commit d2c47c28b6d58661615552db195e4e20f85c6f24 | 241 |
| 3 | 181 | 1.729 | commit 8fb577b13d33379ae5210059e7237889b1030940 | 422 |
| 4 | 222 | 1.571 | commit 403f88f1047f18dbc6dff6dc5e30f96d2e47a16d | 644 |
| 5 | 238 | 1.660 | commit 285e70a6348ffffef80b0ef6770e0310ed1db47e | 882 |
| 6 | 276 | 1.709 | commit 404d41872bf4122dca45d5d159d47c39d6a71490 | 1158 |
| 7 | 334 | 1.807 | commit a7f59116975c02adbe6060a387e7656d4c147942 | 1492 |
| 8 | 437 | 1.684 | commit dbf68749cb635e55a5f5b63b4e1a5477752ea886 | 1929 |
| 9 | 517 | 1.981 | commit 4eaabc827342ddbc9bd095b53d5ba0b97e3c3a86 | 2446 |
| 10 | 766 | 1.712 | commit 432de77aa051ff0a5e0d9b54e08c57d9787b6729 | 3212 |
| 11 | 928 | 1.557 | commit 372ca29fba3a52bafc5d651c87fdaa0edd09ee0b | 4140 |
| 12 | 980 | 1.592 | commit be1f3408dc8edb7ed4d7e4f0a0bc3c89dc70ecd7 | 5120 |
| 13 | 1070 | 1.752 | commit e62ee33aa63566c985e8a99c4444af4ff4555e43 | 6190 |
| 14 | 1339 | 1.884 | commit 0b71b9c08eb5a7c8401cab53f653f1d7d0a0d234 | 7529 |
| 15 | 1853 | 1.889 | commit 84c7c1a9b56b9e76f50ad4784c31de55bf95152c | 9382 |
| 16 | 2575 | 1.661 | commit 592a3183fb55e353d96cef12eb2361e51123c85d | 11957 |
| 17 | 2991 | 1.679 | commit 512bc0fe91f163eda034828c4b4f5b9d49a5fbd6 | 14948 |
| 18 | 3525 | 1.661 | commit 0348254dd0d711cdc41b4ba26b88ba85fe0a8940 | 18473 |
| 19 | 4093 | 1.981 | commit 1a63286ada731e13de13f931cfedf44088bfe997 | 22566 |
| 20 | 6063 | 1.714 | commit 66f442ca83276384f19fdc0373f673fe1e036983 | 28629 |
| 21 | 7363 | 1.666 | commit 221fcee60e0fc24e4a6c62e642fec67b2c6ed01c | 35992 |
| 22 | 8584 | 1.792 | commit 3f049a085bc2ec8d7f93fac7a9b16b22884e5a4c | 44576 |
| 23 | 11090 | 1.855 | commit 8915165083fd6b9cbe9cba46a722033d9d43f5ee | 55666 |
| 24 | 15025 | 1.956 | commit e031d662e79e7a542b4f06135227c7022ef23c05 | 70691 |
| 25 | 21870 | 1.693 | commit 541606655905a53de8dfa53ae734504b79a5e02e | 92561 |
| 26 | 26083 | 1.657 | commit a5859425031db0f23c022daf1f9f98cb15cb5a56 | 118644 |
| 27 | 30176 | 1.751 | commit 100cf714338bcfee09f480002b12001f09cd70cb | 148820 |
| 28 | 37757 | 1.912 | commit 622a28bc52f12a96f5e7a7c5ccd30b10070d18ce | 186577 |
| 29 | 53304 | 1.872 | commit fb68c947c170cafd8f2cb697505e90186c850c51 | 239881 |
| 30 | 73114 | 1.495 | commit 1e2e48c643a5fe52370c4f7a184c12af2014aa33 | 312995 |
| 31 | 72741 | 1.908 | commit c383fbf8b40aff48b0a3f33c1979715a6599257e | 385736 |
| 32 | 102398 | 1.582 | commit 07b4de8d32f9f67a75bb87c61fc62339e710f719 | 488134 |
| 33 | 110813 | 1.920 | commit 6c4315d1488644134e646259b6b7def435dccd4d | 598947 |
| 34 | 157363 | 1.864 | commit 562869eb9878ee3671f31e617526a9f7b4fb53ed | 756310 |
| 35 | 214670 | 1.705 | commit d47b080809ef72bec7f9d2d4d230c21d8ea4130d | 970980 |
| 36 | 258757 | 1.929 | commit 1e51feff404ac4f66bd0c000b9327dd5cbba23de | 1229737 |
| 37 | 369749 | 1.803 | commit 5bd1930e1f9d337eca4b4b8fab08d4198fa92726 | 1599486 |
| 38 | 481958 | 1.506 | commit f730d3341f6c0ee77dbd08017b3d81e8f967c46e | 2081444 |
| 39 | 485014 | 1.531 | commit a8c377afc3cfc167b71d9db589edbb4ce8d2c56b | 2566458 |
| 40 | 500190 | 1.880 | commit 55b8d74115980bbec4937ec1cadfb225c7a0ffc7 | 3066648 |
| 41 | 690035 | 1.499 | commit 36a297976c4a9f7d8e0421878f96999b743b2238 | 3756683 |
| 42 | 689491 | 1.637 | commit 8b2813c919e00cce0bba6493e604c029d232ab2a | 4446174 |
| 43 | 784104 | 1.662 | commit 0b7144820449a4ad03bcdd61a6d62a074aef1a05 | 5230278 |
| 44 | 911394 | 1.696 | commit d23e2e26dbdb2a98c0186d2897c72249fc26a260 | 6141672 |


## Negative Incentive model

 * Annoyance: banned (1 month)
 * Cheating: banned (3 month)

# Q & A

If you have any question, please add below. It will be also counted as 1 commit. 

 * Q1:
 * Q2:

