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

## Example

| n | X(n) | C(n) | commit hash | balance (MAK) |
|---:|---:|---:|:---| ---:|
|12 | 2564  |  1.5  | commit be1f3408dc8edb7ed4d7e4f0a0bc3c89dc70ecd7 | 7895 |
|11 | 1709  |  1.5  | commit 372ca29fba3a52bafc5d651c87fdaa0edd09ee0b | 5331 |
|10 | 1139  |  1.5  | commit 432de77aa051ff0a5e0d9b54e08c57d9787b6729 | 3622 |
|9  |  759  |  1.5  | commit 4eaabc827342ddbc9bd095b53d5ba0b97e3c3a86 | 2483 |
|8  |  507  |  1.5  | commit dbf68749cb635e55a5f5b63b4e1a5477752ea886 | 1724 |
|7  |  362  |  1.4  | commit a7f59116975c02adbe6060a387e7656d4c147942 | 1217 |
|6  |  241  |  1.5  | commit 404d41872bf4122dca45d5d159d47c39d6a71490 |  855 |
|5  |  172  |  1.4  | commit 285e70a6348ffffef80b0ef6770e0310ed1db47e |  614 |
|4  |  132  |  1.3  | commit 403f88f1047f18dbc6dff6dc5e30f96d2e47a16d |  442 |
|3  |  110  |  1.2  | commit 8fb577b13d33379ae5210059e7237889b1030940 |  310 |
|2  |  100  |  1.1  | commit d2c47c28b6d58661615552db195e4e20f85c6f24 |  200 |
|1  |  100  |  1.0  | commit 56e292ed0dac7821b12c9e8ead1c32d189ab47aa |  100 |


## Negative Incentive plan

 * Annoyance: banned (1 month)
 * Cheating: banned (3 month)

# Q & A

If you have any question, please add below. It will be also counted as 1 commit. 

 * brah brah brah
 * brah brah brah

