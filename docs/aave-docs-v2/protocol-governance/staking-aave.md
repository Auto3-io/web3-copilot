# Staking AAVE

The AAVE token can also be staked in the Safety Module, a core part of [Aavenomics](https://docs.aave.com/aavenomics/). By staking AAVE in the Safety Module, users help protect the protocol from a [short fall event](https://docs.aave.com/aavenomics/safety-module) and earn an incentive as a result.

{% hint style="info" %}
This section will cover the technical aspects of staking and the Safety Module. For governance, security, and incentive details, see the [Aavenomics](https://docs.aave.com/aavenomics/) documentation.
{% endhint %}

The source code for the Safety Module, which includes the Staked AAVE token, can be found on [Github here](https://github.com/aave/safety-module).

## Deployed Contracts

{% tabs %}
{% tab title="Mainnet" %}
| Proxy Contracts                                                                                                     | Interface                                                                                          | Address and ABIs                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Staked AAVE](https://github.com/aave/aave-stake-v2/blob/master/contracts/stake/StakedAaveV2.sol) (stkAAVE)         | [Solidity](https://github.com/aave/safety-module/blob/master/contracts/interfaces/IStakedAave.sol) | [0x4da27a545c0c5B758a6BA100e3a049001de870f5](https://etherscan.io/address/0x4da27a545c0c5b758a6ba100e3a049001de870f5#code) |
| [Staked Balancer LP ](https://github.com/aave/aave-stake-v2/blob/master/contracts/stake/StakedTokenV2.sol)(stkABPT) | [Solidity](https://github.com/aave/aave-stake-v2/blob/master/contracts/interfaces/IStakedAave.sol) | [0xa1116930326D21fB917d5A27F1E9943A9595fb47](https://etherscan.io/address/0xa1116930326d21fb917d5a27f1e9943a9595fb47)      |

| Underlying token | Address                                                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| AAVE token       | [0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9](https://etherscan.io/address/0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9#readProxyContract) |
| ABPT token       | [0x41A08648C3766F9F9d85598fF102a08f4ef84F84](https://etherscan.io/address/0x41a08648c3766f9f9d85598ff102a08f4ef84f84#readProxyContract) |

Note that the interface for AAVE/WETH Balancer pool can be found [here](https://pools.balancer.exchange/#/pool/0xc697051d1c6296c24ae3bcef39aca743861d9a81/about).
{% endtab %}

{% tab title="Kovan" %}
| Proxy Contracts                                                                                                                    | Interface                                                                                          | Address and ABIs                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [Staked AAVE](https://github.com/aave/safety-module/blob/master/contracts/lib/InitializableAdminUpgradeabilityProxy.sol) (stkAAVE) | [Solidity](https://github.com/aave/safety-module/blob/master/contracts/interfaces/IStakedAave.sol) | [0xf2fbf9A6710AfDa1c4AaB2E922DE9D69E0C97fd2](https://kovan.etherscan.io/address/0xf2fbf9a6710afda1c4aab2e922de9d69e0c97fd2#code) |
{% endtab %}
{% endtabs %}

## Audits

| Auditor                                                                                                                           | Audit Type     |
| --------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [Consensys Diligence](https://diligence.consensys.net/audits/2020/09/aave-safety-module/) (Safety Module / Staked AAVE)           | Smart Contract |
| [CertiK](https://github.com/aave/safety-module/blob/master/audits/CertiK\_Aave\_Staking\_audit.pdf) (Safety Module / Staked AAVE) | Smart Contract |

## Integrating Staking

To perform AAVE staking in your integration, the following steps should be followed:

### 1. Ensure your users have AAVE

If they still have LEND, then the LEND tokens need to be migrated. See the [LEND to AAVE migration](https://docs.aave.com/developers/v/1.0/developing-on-aave/the-protocol/aave-token#lend-to-aave-migration) guide of the V1 docs.

### 2. Stake the user's AAVE

1. The user must first `approve()` the amount for the [`Staked AAVE contract`](staking-aave.md#deployed-contracts) to stake.
2. The user should call [`stake()`](staking-aave.md#stake), passing in their address and the amount to stake.

### 3. Claim staking rewards

After a period of time, the user will accrue rewards. To check the rewards accrued for a certain user, call [`getTotalRewardsBalance()`](staking-aave.md#gettotalrewardsbalance) to fetch the pending rewards. To claim the rewards, call [`claimRewards()`](staking-aave.md#claimrewards).

### 4. Un-staking

To un-stake, a user must first activate the cool down timer, wait for the cool down time to elapse, then redeem their staked tokens.

1. To activate the cool down timer, call [`cooldown()`](staking-aave.md#cooldown).
2. To check if the cool down timer has finished, the current unix timestamp must be greater than the value returned from [`stakersColldowns()`](staking-aave.md#stakerscooldowns) + [`COOLDOWN_SECONDS()`](staking-aave.md#cooldown\_seconds).
3. When the cool down has finished, the user will have a maximum [`UNSTAKE_WINDOW()`](staking-aave.md#unstake\_window) of time to redeem their tokens. If they do not redeem before this time period has elapsed, then the cool down timer is reset and they will need to activate the cool down again.
4. The final step to un-stake it to call [`redeem()`](staking-aave.md#redeem).

## Staked AAVE (stkAAVE)

When a user stakes AAVE in the Safety Module, the user receives an equivalent amount of stkAAVE in return, and starts accruing rewards in AAVE. The user is then able to claim the rewards at anytime. To withdraw their staked AAVE, the user needs to activate a `coolDown()` period, as detailed below.

### stake()

**`function stake(address onBehalfOf, uint256 amount)`** - [code](https://github.com/aave/safety-module/blob/3c8d5c30302c35239b6ea8c23ad3df36b485d7b6/contracts/stake/StakedToken.sol#L74)

Stakes a certain amount of AAVE tokens, with the option of sending the staked AAVE tokens (stkAAVE) to another address (i.e. the `onBehalfOf` address).

Note: the `msg.sender` must already have a balance of AAVE token.

{% hint style="danger" %}
The user must `approve()` the `amount` for the [`Staked AAVE`](staking-aave.md#deployed-contracts) contract to stake, before execution.
{% endhint %}

| Parameter    | Type    | Description                                                                                                                    |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `onBehalfOf` | address | The address which will receive the stkAAVE tokens. Use `msg.sender` if the stkAAVE should be sent to the same calling address. |
| `amount`     | uint256 | The amount of AAVE to be staked                                                                                                |

### claimRewards()

**`function claimRewards(address to, uint256 amount)`** - [code](https://github.com/aave/safety-module/blob/3c8d5c30302c35239b6ea8c23ad3df36b485d7b6/contracts/stake/StakedToken.sol#L148)

Claims an `amount` of AAVE rewards that the `msg.sender` has accrued, with the option of sending the rewards to a different account.

| Parameter | Type    | Description                                                                                                                              |
| --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `to`      | address | The address which will receive the AAVE tokens rewards. Use `msg.sender` if the AAVE rewards should be sent to the same calling address. |
| `amount`  | uint256 | The amount of AAVE to be claimed. Use `type(uint).max` to claim all outstanding rewards for the user.                                    |

### redeem()

**`function redeem(address to, uint256 amount)`** - [code](https://github.com/aave/safety-module/blob/3c8d5c30302c35239b6ea8c23ad3df36b485d7b6/contracts/stake/StakedToken.sol#L102)

Redeems the staked tokens - receiving AAVE tokens and burning stkAAVE tokens.

{% hint style="warning" %}
A user can only redeem the underlying AAVE tokens if the following has been satisfied:

1. Activated their [`cooldown()`](staking-aave.md#cooldown) period, and
2. The sum of [`stakersCooldowns()`](staking-aave.md#stakerscooldowns) + [`COOLDOWN_SECONDS()`](staking-aave.md#cooldown\_seconds) for their address must be less than the current unix block timestamp, and
3. They must call `redeem()` before the sum of [`stakersCooldowns()`](staking-aave.md#stakerscooldowns) + [`COOLDOWN_SECONDS()`](staking-aave.md#cooldown\_seconds) +[`UNSTAKE_WINDOW()`](staking-aave.md#unstake\_window) has passed.
{% endhint %}



| Parameter | Type    | Description                                                                                                                       |
| --------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `to`      | address | The address which will receive the redeemed AAVE tokens. Use `msg.sender` if the AAVE should be sent to the same calling address. |
| `amount`  | uint256 | The amount of AAVE to be redeemed. Use `uint(-1)` to redeem the entire balance of the user.                                       |

### cooldown()

**`function cooldown()`** - [code](https://github.com/aave/safety-module/blob/3c8d5c30302c35239b6ea8c23ad3df36b485d7b6/contracts/stake/StakedToken.sol#L135)

Activates the cool down timer to be able to unstake.

See [`getNextCooldownTimestamp()` ](staking-aave.md#getnextcooldowntimestamp)for example cool down periods and scenarios.

### stakersCooldowns()

**`function stakersCooldowns(address staker) view returns uint`** - [code](https://github.com/aave/safety-module/blob/3c8d5c30302c35239b6ea8c23ad3df36b485d7b6/contracts/stake/StakedToken.sol#L35)

Returns the unix timestamp in seconds for when the `staker` activated the cool down by calling [`cooldown()`](staking-aave.md#cooldown).

A staker is able to successfully unstake when this value + [`COOLDOWN_SECONDS`](staking-aave.md#cooldown\_seconds) in unix time has passed.

### COOLDOWN\_SECONDS()

**`function COOLDOWN_SECONDS() view returns uint`** - [code](https://github.com/aave/safety-module/blob/3c8d5c30302c35239b6ea8c23ad3df36b485d7b6/contracts/stake/StakedToken.sol#L26)

Returns the current minimum cool down time needed to elapse before a staker is able to unstake their tokens.

As of October 2020, the current `COOLDOWN_SECONDS` value is 864000 seconds (i.e. 10 days). This value should always be checked directly from the contracts.

### UNSTAKE\_WINDOW()

**`function UNSTAKE_WINDOW() view returns uint`** - [code](https://github.com/aave/safety-module/blob/3c8d5c30302c35239b6ea8c23ad3df36b485d7b6/contracts/stake/StakedToken.sol#L29)

Returns the maximum window of time in seconds that a staker can [`redeem()`](staking-aave.md#redeem) their stake once a [`cooldown()`](staking-aave.md#cooldown) period has been completed.

As of October 2020, the current `UNSTAKE_WINDOW` value is 172800 seconds (i.e. 2 days). This value should always be checked directly from the contracts.

### getNextCooldownTimestamp()

**`function getNextCooldownTimestamp(uint256 fromCooldownTimestamp, uint256 amountToReceive, address toAddress, uint256 toBalance) public returns (uint256)`** - [code](https://github.com/aave/safety-module/blob/3c8d5c30302c35239b6ea8c23ad3df36b485d7b6/contracts/stake/StakedToken.sol#L238)

Calculates the cool down timestamp based on the sender / receiver timestamps.

#### Cool down examples:

* A user stakes AAVE for the first time. Their cool down time is set to the current block timestamp.
* A user already has stkAAVE and decides to stake more AAVE (i.e. call `stake()`), while they already have a cool down period active:
  * If the cool down is expired (e.g. beyond the `UNSTAKE_WINDOW`), then the cool down period will remain expired.
  * If the cool down period is still valid, using the amount staked and and the current block timestamp, a weighted average is calculated with the current cool down timestamp of the user.
* A user calls `redeem()`. This will reset the cool down timestamp.
* A user calls `claimRewards()`. The cool down timestamp is not affected.
* A user transfers (i.e. sends) stkAAVE to another address:
  * The cool down timestamp of the `msg.sender` remains the same.
  * For the receiver of the stkAAVE:
    * If they have a valid cool down period finishing before the cool down period of the `msg.sender`, a weighted average is calculated with the current cool down timestamp of the user.
    * If the receiver has an expired cool down timestamp, the cool down timestamp is reset.
    * If both the receiver and `msg.sender` have valid cool down periods, and the `msg.sender` cool down period ends before the receiver, then the receiver's cool down period remains the same.

| Parameter               | Type    | Description                                 |
| ----------------------- | ------- | ------------------------------------------- |
| `fromCooldownTimestamp` | uint256 | The cool down timestamp of the sender       |
| `amountToReceive`       | uint256 | The amount of stkAAVE tokens to be sent     |
| `toAddress`             | address | The receiver's address                      |
| `toBalance`             | uint256 | The current stkAAVE balance of the receiver |

### getTotalRewardsBalance()

**`function getTotalRewardsBalance(address staker) external view returns (uint256)`** - [code](https://github.com/aave/safety-module/blob/3c8d5c30302c35239b6ea8c23ad3df36b485d7b6/contracts/stake/StakedToken.sol#L279)

Returns the total rewards that are pending to be claimed by a staker.

| Parameter | Type    | Description          |
| --------- | ------- | -------------------- |
| `staker`  | address | The staker's address |

## Calculating APR for stkAAVE

To calculate the APR (as shown in the client UI), simply use:\
`emissionsPerSecond` x `seconds in a year` / `current stakes`

To get the `emissionsPerSecond`, go to the[ stkAAVE contract](staking-aave.md#deployed-contracts) and under `assets()` input the stkAave address.

To get `current stakes`, fetch the `balanceOf()` the stkAAVE contract for the AAVE token.
