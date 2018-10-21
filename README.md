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

Initial Budget from a Client = 8000000 JPY (example case)

| n | X(n) | C(n) | commit hash | balance (MAK) | Client's Budget (JPY) |
|---:|---:|---:|:---| ---:|---:|
| 1 | 100 | 1.754 | commit 404d41872bf4122dca45d5d159d47c39d6a71490 | 100 | 7999900|
| 2 | 125 | 1.835 | commit a7f59116975c02adbe6060a387e7656d4c147942 | 225 | 7999775|
| 3 | 167 | 1.752 | commit dbf68749cb635e55a5f5b63b4e1a5477752ea886 | 392 | 7999608|
| 4 | 209 | 1.992 | commit 4eaabc827342ddbc9bd095b53d5ba0b97e3c3a86 | 601 | 7999399|
| 5 | 312 | 1.805 | commit 432de77aa051ff0a5e0d9b54e08c57d9787b6729 | 913 | 7999087|
| 6 | 407 | 1.949 | commit 372ca29fba3a52bafc5d651c87fdaa0edd09ee0b | 1320 | 7998680|
| 7 | 590 | 1.994 | commit be1f3408dc8edb7ed4d7e4f0a0bc3c89dc70ecd7 | 1910 | 7998090|
| 8 | 881 | 1.638 | commit e62ee33aa63566c985e8a99c4444af4ff4555e43 | 2791 | 7997209|
| 9 | 1002 | 1.858 | commit 0b71b9c08eb5a7c8401cab53f653f1d7d0a0d234 | 3793 | 7996207|
| 10 | 1361 | 1.591 | commit 84c7c1a9b56b9e76f50ad4784c31de55bf95152c | 5154 | 7994846|
| 11 | 1485 | 1.526 | commit 592a3183fb55e353d96cef12eb2361e51123c85d | 6639 | 7993361|
| 12 | 1524 | 1.971 | commit 512bc0fe91f163eda034828c4b4f5b9d49a5fbd6 | 8163 | 7991837|
| 13 | 2241 | 1.883 | commit 0348254dd0d711cdc41b4ba26b88ba85fe0a8940 | 10404 | 7989596|
| 14 | 3098 | 1.819 | commit 1a63286ada731e13de13f931cfedf44088bfe997 | 13502 | 7986498|
| 15 | 4087 | 1.552 | commit 66f442ca83276384f19fdc0373f673fe1e036983 | 17589 | 7982411|
| 16 | 4300 | 1.838 | commit 221fcee60e0fc24e4a6c62e642fec67b2c6ed01c | 21889 | 7978111|
| 17 | 5752 | 1.872 | commit 3f049a085bc2ec8d7f93fac7a9b16b22884e5a4c | 27641 | 7972359|
| 18 | 7894 | 1.758 | commit 8915165083fd6b9cbe9cba46a722033d9d43f5ee | 35535 | 7964465|
| 19 | 9929 | 1.849 | commit e031d662e79e7a542b4f06135227c7022ef23c05 | 45464 | 7954536|
| 20 | 13396 | 1.753 | commit 541606655905a53de8dfa53ae734504b79a5e02e | 58860 | 7941140|
| 21 | 16789 | 1.607 | commit a5859425031db0f23c022daf1f9f98cb15cb5a56 | 75649 | 7924351|
| 22 | 18585 | 1.722 | commit 100cf714338bcfee09f480002b12001f09cd70cb | 94234 | 7905766|
| 23 | 22715 | 1.562 | commit 622a28bc52f12a96f5e7a7c5ccd30b10070d18ce | 116949 | 7883051|
| 24 | 24121 | 1.897 | commit fb68c947c170cafd8f2cb697505e90186c850c51 | 141070 | 7858930|
| 25 | 33696 | 1.847 | commit 1e2e48c643a5fe52370c4f7a184c12af2014aa33 | 174766 | 7825234|
| 26 | 45393 | 1.810 | commit c383fbf8b40aff48b0a3f33c1979715a6599257e | 220159 | 7779841|
| 27 | 59442 | 1.853 | commit 07b4de8d32f9f67a75bb87c61fc62339e710f719 | 279601 | 7720399|
| 28 | 80454 | 1.668 | commit 6c4315d1488644134e646259b6b7def435dccd4d | 360055 | 7639945|
| 29 | 93963 | 1.764 | commit 562869eb9878ee3671f31e617526a9f7b4fb53ed | 454018 | 7545982|
| 30 | 118813 | 1.684 | commit d47b080809ef72bec7f9d2d4d230c21d8ea4130d | 572831 | 7427169|
| 31 | 140616 | 1.828 | commit 1e51feff404ac4f66bd0c000b9327dd5cbba23de | 713447 | 7286553|
| 32 | 186717 | 1.899 | commit 5bd1930e1f9d337eca4b4b8fab08d4198fa92726 | 900164 | 7099836|
| 33 | 261165 | 1.800 | commit f730d3341f6c0ee77dbd08017b3d81e8f967c46e | 1161329 | 6838671|
| 34 | 339556 | 1.685 | commit a8c377afc3cfc167b71d9db589edbb4ce8d2c56b | 1500885 | 6499115|
| 35 | 402374 | 1.970 | commit 55b8d74115980bbec4937ec1cadfb225c7a0ffc7 | 1903259 | 6096741|
| 36 | 591552 | 2.000 | commit 36a297976c4a9f7d8e0421878f96999b743b2238 | 2494811 | 5505189|
| 37 | 887162 | 1.626 | commit 8b2813c919e00cce0bba6493e604c029d232ab2a | 3381973 | 4618027|
| 38 | 999272 | 1.998 | commit 0b7144820449a4ad03bcdd61a6d62a074aef1a05 | 4381245 | 3618755|
| 39 | 1497137 | 1.596 | commit d23e2e26dbdb2a98c0186d2897c72249fc26a260 | 5878382 | 2121618|
| 40 | 1641425 | 1.616 | commit 85e800b80318251b67d2389a9f09c20b92149948 | 7519807 | 480193|
| 41 | 480193 | 1.672 | commit 9a4dcbdd46b77201d27bc799af44a0ea13edfe54 | 8000000 | 0|



## Negative Incentive model

 * Annoyance: banned (1 month)
 * Cheating: banned (3 month)

# Q & A

If you have any question, please add below. It will be also counted as 1 commit. 

 * Q1:
 * Q2:

