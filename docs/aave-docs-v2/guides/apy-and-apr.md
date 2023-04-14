---
description: You can query latest APY and APR on chain and subgraph
---

# APY and APR

{% hint style="info" %}
All rates queried on chain or subgraph, are expressed in RAY units i.e. 10^27.\
All emissions are expressed in WAD units i.e. 10^18.
{% endhint %}

{% hint style="info" %}
APY: Compounding interest accrued by deposit or borrow on [`LendingPool`](../the-core-protocol/lendingpool/)``

APR: Non Compounding rewards earned as part of [LiquidityMining](liquidity-mining.md)
{% endhint %}

The deposit and borrow APY displayed on the Aave front-end is **compounded per second**.&#x20;

## Fetch Data

### Subgraph

Use [subgraph](../getting-started/using-graphql.md#aaves-subgraphs) to query reserve data.

```javascript
{
  reserves {
    name
    underlyingAsset
    
    liquidityRate 
    stableBorrowRate
    variableBorrowRate
    
    aEmissionPerSecond
    vEmissionPerSecond
    sEmissionPerSecond
    
    totalATokenSupply
    totalCurrentVariableDebt
  }
}
```

### On-Chain

APR: [`getAssetData`](liquidity-mining.md#getassetdata) to fetch liquidity mining incentives for a/s/vToken.

APY: [`getReserveData`](../the-core-protocol/lendingpool/#getreservedata)to fetch deposit and borrow rates of asset.

```javascript
[, liquidityIndex, variableBorrowIndex, 
currentLiquidityRate, currentVariableBorrowRate,
currentStableBorrowRate, ,
aTokenAddress, stableDebtTokenAddress,
variableDebtTokenAddress, , ] = LendingPool.getReserveData(asset.address) 
// asset is the ERC20 deposited or borrowed, eg. DAI, WETH

[,aEmissionPerSecond,] = IcentivesController.getAssetData(aTokenAddress)
[,vEmissionPerSecond,] = IcentivesController.getAssetData(variableDebtTokenAddress)
[,sEmissionPerSecond,] = IcentivesController.getAssetData(stableDebtTokenAddress)
```

## Compute Data

Calculate rates as👇🏻with `js`, `python` or whatever you like 😉

```javascript
RAY = 10**27 // 10 to the power 27
SECONDS_PER_YEAR = 31536000

// Deposit and Borrow calculations
// APY and APR are returned here as decimals, multiply by 100 to get the percents

depositAPR = liquidityRate/RAY
variableBorrowAPR = variableBorrowRate/RAY
stableBorrowAPR = variableBorrowRate/RAY

depositAPY = ((1 + (depositAPR / SECONDS_PER_YEAR)) ^ SECONDS_PER_YEAR) - 1
variableBorrowAPY = ((1 + (variableBorrowAPR / SECONDS_PER_YEAR)) ^ SECONDS_PER_YEAR) - 1
stableBorrowAPY = ((1 + (stableBorrowAPR / SECONDS_PER_YEAR)) ^ SECONDS_PER_YEAR) - 1

// Incentives calculation

aEmissionPerYear = aEmissionPerSecond * SECONDS_PER_YEAR
vEmissionPerYear = vEmissionPerSecond * SECONDS_PER_YEAR

WEI_DECIMALS = 10**18 // All emissions are in wei units, 18 decimal places

// UNDERLYING_TOKEN_DECIMALS will be the decimals of token underlying the aToken or debtToken
// For Example, UNDERLYING_TOKEN_DECIMALS for aUSDC will be 10**6 because USDC has 6 decimals

incentiveDepositAPRPercent = 100 * (aEmissionPerYear * REWARD_PRICE_ETH * WEI_DECIMALS)/
                          (totalATokenSupply * TOKEN_PRICE_ETH * UNDERLYING_TOKEN_DECIMALS)
                          
incentiveBorrowAPRPercent = 100 * (vEmissionPerYear * REWARD_PRICE_ETH * WEI_DECIMALS)/
                          (totalCurrentVariableDebt * TOKEN_PRICE_ETH * UNDERLYING_TOKEN_DECIMALS)
```



## Conversions

Both of these conversions take the input and ouput in decimal form. Multiply the output by 100 to get the percentage.&#x20;

### APR -> APY

To convert the APR to APY compounded per second the formula is:

$$
APY = (1 + (APR / secondsPerYear))^{secondsPerYear} - 1
$$

### APY -> APR

To convert APY compounded per second to APR the formula is:

$$
APR = ((1 + APY)^{(1/secondsPerYear)}  - 1) * secondsPerYear
$$
