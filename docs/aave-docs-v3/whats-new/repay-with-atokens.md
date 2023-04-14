# Repay With aTokens

Allows user to repay with _aTokens_ in case the underlying borrowed asset is locked in the Aave liquidity pool.

_Example:_ **User have stable DAI debt and also holds aDAI token**

The user in this case can use aDAI to repay DAI debt in single transaction without any approvals or having to withdraw their supplied liquidity to the pool using `repayWithATokens` feature.

```tsx
import { Contract, utils } from "ethers";
const poolAbi = require("./abis/pool.json");
const pool = new Contract(POOL_ADDRESS, poolAbi, signer);

// repay amount of DAI debt using aDAI tokens
pool.repayWithATokens(DAI.address, amount, 2);

// User must hold aDAI >= amount being repaid
```
