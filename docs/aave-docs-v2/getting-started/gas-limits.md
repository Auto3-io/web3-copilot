# Gas Limits

The following table shows the recommended gas limit to set when calling the functions. Note that this is the _safe_ gas limit to set to ensure that the transaction completes, however the transaction may use significantly less than these gas limits.&#x20;

| Function                                                                                         | Recommended Gas Limit |
| ------------------------------------------------------------------------------------------------ | --------------------- |
| [setUserUseReserveAsCollateral](../the-core-protocol/lendingpool/#setuserusereserveascollateral) | 90000                 |
| [swapBorrowRateMode](../the-core-protocol/lendingpool/#swapborrowratemode)                       | 600000                |
| [deposit](../the-core-protocol/lendingpool/#deposit)                                             | 400000                |
| [withdraw](../the-core-protocol/lendingpool/#withdraw)                                           | 500000                |
| [borrow](../the-core-protocol/lendingpool/#borrow)                                               | 550000                |
| [repay](../the-core-protocol/lendingpool/#repay)                                                 | 400000                |
| [stake](../protocol-governance/staking-aave.md#stake)                                            | 600000                |
| [claimRewards](../protocol-governance/staking-aave.md#claimrewards)                              | 450000                |
| [redeem](../protocol-governance/staking-aave.md#redeem)                                          | 300000                |
| [cooldown](../protocol-governance/staking-aave.md#cooldown)                                      | 100000                |
