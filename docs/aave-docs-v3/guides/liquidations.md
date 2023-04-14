# Liquidations

The health of the Aave Protocol is dependent on the 'health' of the collateralised positions within the protocol, also known as the 'health factor'. When the 'health factor' of an account's total loans is below 1, anyone can make a `liquidationCall()`  to the [`Pool`](../core-contracts/pool.md#liquidationcall) or [L2Pool](../getting-started/l2-optimization/l2pool.md#liquidationcall) (in case of Arbitrum/Optimism) contract, pay back part of the debt owed and receive discounted collateral in return (also known as the liquidation bonus).&#x20;

This incentivises third parties to participate in the health of the overall protocol, by acting in their own interest (to receive the discounted collateral) and as a result, ensure borrows are sufficiently collateralize.

There are multiple ways to participate in liquidations:

1. By calling the liquidationCall() directly in the [Pool](../core-contracts/pool.md#liquidationcall) or [L2Pool](../getting-started/l2-optimization/l2pool.md#liquidationcall) contract.
2. By creating your own automated bot or system to liquidate loans.

{% hint style="warning" %}
For liquidation calls to be profitable, you must take into account the gas cost involved in liquidating the loan. If a high gas price is used, then the liquidation may be unprofitable for you. See the [Calculating profitability](liquidations.md#calculating-profitability-vs-gas-cost) section for more details.
{% endhint %}

{% hint style="success" %}
V3 allows 100% of debt (i.e. `MAX_LIQUIDATION_CLOSE_FACTOR`) to be liquidated in single `liquidationCall()` if:\
`HF < CLOSE_FACTOR_HF_THRESHOLD`
{% endhint %}

## Prerequisites

When making a `liquidationCall()`, you must:

* Know the account (i.e. the ethreum address: `user`) whose health factor is below 1.
* Know the valid debt amount and asset (i.e. `debtToCover` & `debtAsset`)
  * If the HF is above `CLOSE_FACTOR_HF_THRESHOLD`, then only a maximum of 50% (i.e. `DEFAULT_LIQUIDATION_CLOSE_FACTOR`) of the debt can be liquidated per valid `liquidationCall()`
  * If the HF is below `CLOSE_FACTOR_HF_THRESHOLD`, then 100% (i.e. `MAX_LIQUIDATION_CLOSE_FACTOR`) of the debt can be liquidated in single valid `liquidationCall()`
  * &#x20;You can set the `debtToCover` to `uint(-1)` and the protocol will proceed with the highest possible liquidation allowed by the close factor.
  * You must already have sufficient balance of the debt asset, which will be used by the `liquidationCall` to pay back the debt. You can use `flashLoan` for liquidations 😉
* Know the collateral asset `collateralAsset` you closing, i.e. the asset that the user has `backing` their outstanding loan that you will receive as a `bonus`.
* Whether you want to receive _aTokens_ or the underlying asset after a successful `liquidationCall()` .

## Getting accounts to liquidate

{% hint style="warning" %}
"User Account" in the Aave Protocol refer to a single ethereum address that has interacted with the protocol. This can be an externally owned account or contract.
{% endhint %}

Only user accounts that have HF < 1 can be liquidated. There are multiple ways you can get the health factor:

### On Chain

1. To gather user account data from on-chain data, one way would be to monitor emitted events from the protocol and keep an up to date index of user data locally.
   1. Events are emitted each time a user interacts with the protocol (supply, borrow, repay, withdraw etc.)
2. When you have the user's address, you can simply call [`getUserAccountData()`](../core-contracts/pool.md#getuseraccountdata), to read the user's current healthFactor. If the HF < 1, then the account can be liquidated.

### GraphQL

1. Similarly to the sections above you will need to gather user account data and keep an index of the user data locally.
2. SInce GraphQL does not provide real time calculated user data such as `healthFactor,` you will need to compute this locally. The easiest way is to use the [Aave-utilities](https://github.com/aave/aave-utilities#formatusersummary) sdk, which has methods to compute user summary data.

## Executing the liquidation call

Once you have the account(s) to liquidate, you will need to calculate the amount of collateral that can be liquidated:

1. Use [`getUserReserveData()`](../periphery-contracts/uipooldataproviderv3.md#getuserreservesdata)
2. Max debt that be cleared by single liquidation call is given by the `DEFAULT_LIQUIDATION_CLOSE_FACTOR`(when `CLOSE_FACTOR_HF_THRESHOLD < HF < 1`) or `MAX_LIQUIDATION_CLOSE_FACTOR` (when `HF < CLOSE_FACTOR_HF_THRESHOLD`)
   1. `debtToCover = (userStableDebt + userVariableDebt) * LiquidationCloseFactor`
   2. &#x20;You can pass `uint(-1)`, i.e. `MAX_UINT`, as the `debtToCover` to liquidate the maximum amount allowed.
3. Max amount of collateral that can be liquidated to cover debt is given by the current _liquidationBonus_ for the reserves that have `usageAsCollateralEnabled` as true.
   1. `maxAmountOfCollateralToLiquidate = (debtAssetPrice * debtToCover * liquidationBonus)/ collateralPrice`

## Calculating profitability vs gas cost

One way to calculate the profitability is the following:

1. Store and retrieve each collateral's relevant details such as address, decimals used and liquidation bonus.
2. Get the user's collateral balance (aTokenBalance).
3. Get the asset's price according to the Aave's oracle contract using [`getAssetPrice()`](../core-contracts/aaveoracle.md#getassetprice).
4. The maximum collateral bonus received on liquidation is given by the `maxAmountOfCollateralToLiquidate * (1 - liquidationBonus) * collateralAssetPriceEth`
5. The maximum cost of your transaction will be you gas price multiplied by the amount of gas used. You should be able to get a good estimation of the gas amount used by calling `estimateGas` via your web3 provider.
6. Your approximate profit will be the value of the collateral bonus (4) minus the cost of your transaction (5).

## Appendix

### How is health factor calculated?

The health factor is calculated from the user's total collateral, i.e. all reserves for which `usageAsCollateral` is enabled, balance (in ETH) multiplied by the liquidation threshold percentage for all the user's outstanding assets, divided by the user's total borrow balance across all reserves (in ETH).

This can be calculated both off-chain and on-chain, see [Aave-utilities](https://github.com/aave/aave-utilities/blob/cdf8a8bf87c8848a2f0865c58defbd04e0871171/packages/math-utils/src/pool-math.ts#L169) and [GenericLogic Library](https://github.com/aave/aave-v3-core/blob/c8722965501b182f6ab380db23e52983eb87e406/contracts/protocol/libraries/logic/GenericLogic.sol#L183) respectively for reference.

### How is liquidation bonus determined?

Liquidation bonuses for all the assets are evaluated and determined based on each asset's liquidity risk and updated via Aave Governance process.
