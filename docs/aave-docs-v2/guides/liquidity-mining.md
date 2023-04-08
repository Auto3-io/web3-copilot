# Liquidity Mining

Liquidity mining/incentives was implemented in the [Main Aave market](../deployed-contracts/deployed-contracts.md) via [AIP-16](https://app.aave.com/governance/11-Qmf1JeXiw8BDUoKJ89VmUJ8wy22D2udqL4HxprCG7DZ5zG), enabling incentives for both depositing and borrowing. Incentives are also currently implemented on the [Polygon market](../deployed-contracts/matic-polygon-market.md) & [Avalanche market](../deployed-contracts/avalanche-market.md), using the same implementation details as described on this page.

| Market         | Code                                                                                                                                  | Address                                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Main Market    | [Github](https://github.com/aave/incentives-proposal/blob/master/contracts/incentives/StakedTokenIncentivesController.sol)            | [0xd784927Ff2f95ba542BfC824c8a8a98F3495f6b5](https://etherscan.io/address/0xd784927Ff2f95ba542BfC824c8a8a98F3495f6b5#readProxyContract)            |
| Polygon Market | [Github](https://github.com/aave/aave-stake-v2/blob/feat/incentives/mumbai-config/contracts/interfaces/IAaveIncentivesController.sol) | [0x357D51124f59836DeD84c8a1730D72B749d8BC23](https://explorer-mainnet.maticvigil.com/address/0x357D51124f59836DeD84c8a1730D72B749d8BC23/contracts) |
| Avalanche      | [Code](https://cchain.explorer.avax.network/address/0x198A4a8ECe13dfa29F5b37F5A5A3683a02185757/contracts)                             | [0x01D83Fe6A10D2f2B7AF17034343746188272cAc9](https://cchain.explorer.avax.network/address/0x01D83Fe6A10D2f2B7AF17034343746188272cAc9/contracts)    |

## Integration Guide

### 0. Prerequisites

Your user(s) should already have a position in the protocol. Depending on the market and incentives that are enabled, they should already have a [deposit](../the-core-protocol/lendingpool/#deposit), [borrow](../the-core-protocol/lendingpool/#borrow), or both, in one of the incentivised assets.&#x20;

To check if an asset is current incentivised, use the [`getAssetData()`](liquidity-mining.md#getassetdata) method, passing in the associated **aToken** or **debtToken** address of the incentivised asset. To get a list of associated tokens per asset, see also [`getReserveTokensAddresses()`](https://docs.aave.com/developers/the-core-protocol/protocol-data-provider#getreservetokensaddresses) in the Protocol Data Provider.

### 1. Check the user(s) reward balance

Call the [`getRewardsBalance()`](liquidity-mining.md#getrewardsbalance) method, passing in the relevant token addresses (aTokens and/or debtTokens) as an array.

### 2. Claim the accrued rewards

#### 2.1 Claim rewards from the user

Call the [`claimRewards()`](liquidity-mining.md#claimrewards) method, passing in the relevant token addresses (aTokens and/or debtTokens) as an array. The `msg.sender` must match the user's address that has accrued the rewards.

#### 2.2 Claim rewards on behalf of the user

{% hint style="warning" %}
A claimer must have been set via the [`setClaimer()`](liquidity-mining.md#setclaimer) method, enabling the caller to claim on the user's behalf.
{% endhint %}

Call the [`claimRewardsOnBehalf()`](liquidity-mining.md#claimrewardsonbehalf) method, passing in the relevant token addresses (aTokens and/or debtTokens) as an array. The `msg.sender` must have been previously set via [`setClaimer()`](liquidity-mining.md#setclaimer).

### 3. Consider the token that is rewarded

For the main market, stkAAVE is rewarded and automatically accrues interest based on the [Staking AAVE ](../protocol-governance/staking-aave.md)parameters _once claimed_. There is an associated 10 day cool down period to convert stkAAVE to AAVE, with a 2 day redeem period to do so. Ensure that this information is presented to the user and handled correctly.

For the Polygon market, WMATIC is rewarded with no 'lock up' period. Ensure that you account for the difference between WMATIC and the native MATIC, specifically that WMATIC needs to be unwrapped to MATIC. This can be done by calling [`withdraw()`](https://explorer-mainnet.maticvigil.com/address/0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270/write-contract) on the WMATIC contract.

### 4. Calculating Incentives APY

`APY = normalizedEmissionPerSecond * rewardTokenPriceInEth * SECONDS_PER_YEAR / normalizedTotalTokenSupply`&#x20;

**Note**:

* `normalizedEmissionPerSecond = emissionPerSecond/RWARD_TOKEN_DECIMALS`
* Reward Token is AAVE for mainnet and Matic for polygon.&#x20;
* `normalizedTotalTokenSupply = tokenTotalSupplyNormalized * tokenPriceInEth`,where token is the incentivized a/s/v token and token price is same as underlying asset's price.&#x20;
* &#x20;You can get price for reward token as well as reserve token from [`AavePriceOracle`](../the-core-protocol/price-oracle/#getassetsprices)&#x20;

## Methods

### **claimRewards()**

**`function claimRewards(address[] calldata assets, uint256 amount, address to)`**

Claims the accrued rewards for the `assets`, accumulating any pending rewards.

| Parameter Name | Type       | Description                                                                                                                                                                                                                                                                                                                               |
| -------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assets`       | address\[] | <p>addresses of the asset that accrue rewards, i.e. aTokens or debtTokens.</p><p><br>To get a list of associated tokens per asset, see also <a href="https://docs.aave.com/developers/the-core-protocol/protocol-data-provider#getreservetokensaddresses"><code>getReserveTokensAddresses()</code></a> in the Protocol Data Provider.</p> |
| `amount`       | uint256    | amount to claim, expressed in wei                                                                                                                                                                                                                                                                                                         |
| `to`           | address    | address where the claimed rewards will be sent                                                                                                                                                                                                                                                                                            |

### **claimRewardsOnBehalf()**

**`function claimRewardsOnBehalf(address[] calldata assets, uint256 amount, address user, address to)`**

Claims the accrued rewards for the `assets`, accumulating any pending rewards, on behalf of `user`.

{% hint style="warning" %}
The `user` must have previously called [`setClaimer()`](liquidity-mining.md#setclaimer), setting the `msg.sender` as the approved claimer.
{% endhint %}

| Parameter Name | Type       | Description                                                                                                                                                                                                                                                                                                                               |
| -------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assets`       | address\[] | <p>addresses of the asset that accrue rewards, i.e. aTokens or debtTokens.</p><p><br>To get a list of associated tokens per asset, see also <a href="https://docs.aave.com/developers/the-core-protocol/protocol-data-provider#getreservetokensaddresses"><code>getReserveTokensAddresses()</code></a> in the Protocol Data Provider.</p> |
| `amount`       | uint256    | amount to claim, expressed in wei                                                                                                                                                                                                                                                                                                         |
| `user`         | address    | address of the user who has pending rewards to claim                                                                                                                                                                                                                                                                                      |
| `to`           | address    | address where the claimed rewards will be sent                                                                                                                                                                                                                                                                                            |

### **setClaimer()**

**`function setClaimer(address user, address caller)`**

Sets an authorised `caller` to claim all rewards on behalf of the `user`.  This can only be set via Governance.

| Parameter Name | Type    | Description                                 |
| -------------- | ------- | ------------------------------------------- |
| `user`         | address | address of the user who has pending rewards |
| `caller`       | address | address of the new authorised claimer       |

## View Methods

### getAssetData**()**

{% hint style="warning" %}
`getAssetData()`is currently available only on ethereum markets. In case you are working on **Polygon** markets (main or mumbai), please read data from the public mapping `assets`directly 😅
{% endhint %}

**`function getAssetData(address asset)`**

Returns the asset index, the emissions per second (i.e. current rewards rate), and the last updated timestamp.

| Parameter Name | Type    | Description                                                                                                                                                                                                                                                                                                                              |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset`        | address | <p>address of the asset that accrue rewards, i.e. aTokens or debtTokens.</p><p><br>To get a list of associated tokens per asset, see also <a href="https://docs.aave.com/developers/the-core-protocol/protocol-data-provider#getreservetokensaddresses"><code>getReserveTokensAddresses()</code></a> in the Protocol Data Provider. </p> |

### getClaimer**()**

**`function getClaimer(address user)`**

Returns the authorised claimer of `user`'s accrued rewards. See also [setClaimer()](liquidity-mining.md#setclaimer).

| Parameter Name | Type    | Description                       |
| -------------- | ------- | --------------------------------- |
| `user`         | address | address of the authorised claimer |

### getRewardsBalance**()**

**`function getRewardsBalance(address[] assets, address user)`**

Returns the total rewards of `user` for `assets.`

| Parameter Name | Type       | Description                                                                                                                                                                                                                                                                                                                               |
| -------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assets`       | address\[] | <p>addresses of the asset that accrue rewards, i.e. aTokens or debtTokens.</p><p><br>To get a list of associated tokens per asset, see also <a href="https://docs.aave.com/developers/the-core-protocol/protocol-data-provider#getreservetokensaddresses"><code>getReserveTokensAddresses()</code></a> in the Protocol Data Provider.</p> |
| `user`         | address    | address of the user who has pending rewards to claim                                                                                                                                                                                                                                                                                      |

### getUserAssetData**()**

**`function getUserAssetData(address user, address asset)`**

Returns the data of `user` on a distribution from `asset`

| Parameter Name | Type    | Description                                                                                                                                                                                                                                                                                                                              |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user`         | address | address of the user                                                                                                                                                                                                                                                                                                                      |
| `asset`        | address | <p>address of the asset that accrue rewards, i.e. aTokens or debtTokens.</p><p><br>To get a list of associated tokens per asset, see also <a href="https://docs.aave.com/developers/the-core-protocol/protocol-data-provider#getreservetokensaddresses"><code>getReserveTokensAddresses()</code></a> in the Protocol Data Provider. </p> |

### getUserUnclaimedRewards**()**

**`function getUserUnclaimedRewards(address user)`**

Returns the unclaimed accumulated rewards of `user` for their last action in the protocol.

| Parameter Name | Type    | Description         |
| -------------- | ------- | ------------------- |
| `user`         | address | address of the user |

### getDistributionEnd**()**

**`function getDistributionEnd()`**

Returns the end of the distribution period
