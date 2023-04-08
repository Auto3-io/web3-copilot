# LendingPool

The `LendingPool` contract is the main contract of the protocol. It exposes all the user-oriented actions that can be invoked using either Solidity or web3 libraries.&#x20;

The source code can be found on [Github here](https://github.com/aave/protocol-v2/blob/ice/mainnet-deployment-03-12-2020/contracts/protocol/lendingpool/LendingPool.sol)**.**

If you need development support,  join the #developers channel on the [Aave community Discord server](https://discord.gg/CJm5Jt3).

{% hint style="warning" %}
`LendingPool` methods**`deposit, borrow, withdraw and repay`**are only for ERC20, if you want to deposit, borrow, withdraw or repay using native ETH (or native MATIC incase of Polygon), use [`WETHGateway`](../weth-gateway.md) instead.
{% endhint %}

## Methods

### **deposit()**

**`function deposit(address asset, uint256 amount, address onBehalfOf, uint16 referralCode)`**

Deposits a certain `amount` of an `asset` into the protocol, minting the same `amount` of corresponding aTokens, and transferring them to the `onBehalfOf` address.

{% hint style="danger" %}
The referral program is currently in active and you can pass`0` as the`referralCode.`

In future for referral code to be active again, a governance proposal, with the list of unique referral codes for various integration must be passed via governance.&#x20;
{% endhint %}

{% hint style="warning" %}
When depositing, the `LendingPool` contract must have**`allowance()`**to spend funds on behalf of**`msg.sender`** for at-least**`amount`** for the **`asset`** being deposited. This can be done via the standard ERC20 `approve()` method.
{% endhint %}

| Parameter Name | Type    | Description                                                                                                                  |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `asset`        | address | address of the [underlying asset](../../deployed-contracts/deployed-contracts.md#supported-assets)                           |
| `amount`       | uint256 | amount deposited, expressed in wei units                                                                                     |
| `onBehalfOf`   | address | <p>address whom will receive the aTokens. <br>Use <code>msg.sender</code> when the aTokens should be sent to the caller.</p> |
| `referralCode` | uint16  | referral code for our [referral program](broken-reference). Use 0 for no referral.                                           |

### **withdraw()**

**`function withdraw(address asset, uint256 amount, address to)`**

Withdraws `amount` of the underlying `asset`, i.e. redeems the underlying token and burns the aTokens.

{% hint style="warning" %}
When withdrawing `to`another address,**`msg.sender`**should have`aToken`that will be burned by lendingPool .
{% endhint %}

| Parameter Name | Type    | Description                                                                                                          |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| `asset`        | address | address of the [underlying asset](../../deployed-contracts/deployed-contracts.md#supported-assets), not the aToken   |
| `amount`       | uint256 | <p>amount deposited, expressed in wei units. <br>Use <code>type(uint).max</code> to withdraw the entire balance.</p> |
| `to`           | address | address that will receive the `asset`                                                                                |

### **borrow()**

**`function borrow(address asset, uint256 amount, uint256 interestRateMode, uint16 referralCode, address onBehalfOf)`**

Borrows `amount` of `asset` with `interestRateMode`, sending the `amount` to `msg.sender`, with the debt being incurred by `onBehalfOf`.&#x20;

Note: `onBehalfOf` must have enough collateral via [`deposit()`](./#deposit) or have delegated credit to `msg.sender` via [`approveDelegation()`](../debt-tokens/#approvedelegation). See the [Credit Delegation guide](../../guides/credit-delegation.md) for more details.

| Parameter Name     | Type    | Description                                                                                                                       |
| ------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `asset`            | address | address of the [underlying asset](../../deployed-contracts/deployed-contracts.md#supported-assets)                                |
| `amount`           | uint256 | amount to be borrowed, expressed in wei units                                                                                     |
| `interestRateMode` | uint256 | <p>the type of borrow debt.</p><p>Stable: 1, Variable: 2</p>                                                                      |
| `referralCode`     | uint16  | referral code for our [referral program](broken-reference). Use 0 for no referral code.                                           |
| `onBehalfOf`       | address | <p>address of user who will incur the debt.</p><p>Use <code>msg.sender</code> when not calling on behalf of a different user.</p> |

### **repay()**

**`function repay(address asset, uint256 amount, uint256 rateMode, address onBehalfOf)`**

Repays `onBehalfOf`'s debt `amount` of `asset` which has a `rateMode`.

| Parameter Name | Type    | Description                                                                                                                                                                                                                                                                                                                                                    |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset`        | address | address of the [underlying asset](../../deployed-contracts/deployed-contracts.md#supported-assets)                                                                                                                                                                                                                                                             |
| `amount`       | uint256 | <p>amount to be borrowed, expressed in wei units.</p><p>Use <code>uint(-1)</code> to repay the entire debt,  <strong>ONLY</strong> when the repayment is not executed on behalf of a 3rd party. </p><p>In case of repayments on behalf of another user, it's recommended to send an <code>_amount</code> slightly higher than the current borrowed amount.</p> |
| `rateMode`     | uint256 | <p>the type of borrow debt.</p><p>Stable: 1, Variable: 2</p>                                                                                                                                                                                                                                                                                                   |
| `onBehalfOf`   | address | <p>address of user who will incur the debt.</p><p>Use <code>msg.sender</code> when not calling on behalf of a different user.</p>                                                                                                                                                                                                                              |

### **swapBorrowRateMode()**

**`function swapBorrowRateMode(address asset, uint256 rateMode)`**

Swaps the `msg.sender`'s borrow rate modes between stable and variable.

| Parameter Name | Type    | Description                                                                                        |
| -------------- | ------- | -------------------------------------------------------------------------------------------------- |
| `asset`        | address | address of the [underlying asset](../../deployed-contracts/deployed-contracts.md#supported-assets) |
| `rateMode`     | uint256 | <p>the rate mode the user is swapping <strong>to</strong>.</p><p>Stable: 1, Variable: 2</p>      |

### **setUserUseReserveAsCollateral()**

**`function setUserUseReserveAsCollateral(address asset, bool useAsCollateral)`**

Sets the `asset` of `msg.sender` to be used as collateral or not.

| Parameter Name    | Type    | Description                                                                                        |
| ----------------- | ------- | -------------------------------------------------------------------------------------------------- |
| `asset`           | address | address of the [underlying asset](../../deployed-contracts/deployed-contracts.md#supported-assets) |
| `useAsCollateral` | bool    | `true` if the `asset` should be used as collateral                                                 |

### **liquidationCall()**

**`function liquidationCall(address collateral, address debt, address user, uint256 debtToCover, bool receiveAToken)`**

Liquidate positions with a **health factor** below 1. Also see our [Liquidations guide](../../guides/liquidations.md).

When the health factor of a position is below 1, liquidators repay part or all of the outstanding borrowed amount on behalf of the borrower, while **receiving a discounted amount of collateral** in return (also known as a liquidation 'bonus"). Liquidators can decide if they want to receive an equivalent amount of collateral aTokens, or the underlying asset directly. When the liquidation is completed successfully, the health factor of the position is increased, bringing the health factor above 1.

{% hint style="info" %}
Liquidators can only close a certain amount of collateral defined by a close factor. Currently the **close factor is 0.5**. In other words, liquidators can only liquidate a maximum of 50% of the amount pending to be repaid in a position. The liquidation discount applies to this amount.
{% endhint %}

{% hint style="warning" %}
Liquidators must `approve()` the `LendingPool` contract to use `debtToCover` of the underlying ERC20 of the`asset` used for the liquidation.
{% endhint %}

**NOTES**

* _In most scenarios_, profitable liquidators will choose to liquidate as much as they can (50% of the `user` position).
* `debtToCover` parameter can be set to `uint(-1)` and the protocol will proceed with the highest possible liquidation allowed by the close factor.
* To check a user's health factor, use [`getUserAccountData()`](./#getuseracountdata).

| Parameter Name  | Type    | Description                                                                                                                                   |
| --------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `collateral`    | address | address of the collateral reserve                                                                                                             |
| `debt`          | address | address of the debt reserve                                                                                                                   |
| `user`          | address | address of the borrower                                                                                                                       |
| `debtToCover`   | uint256 | amount of `asset` debt that the liquidator will repay                                                                                         |
| `receiveAToken` | bool    | if `true`, the user receives the aTokens equivalent of the purchased collateral. If `false`, the user receives the underlying asset directly. |

### **flashLoan()**

**`function flashLoan(address receiverAddress, address[] calldata assets, uint256[] calldata amounts, uint256[] modes, address onBehalfOf, bytes calldata params, uint16 referralCode)`**

Sends the requested `amounts` of `assets` to the `receiverAddress` contract, passing the included `params`.&#x20;

If the flash loaned `amounts` + fee is not returned by the end of the transaction, then the transaction will either:

* revert if the associated `mode` is 0,
* `onBehalfOf` incurs a stable debt if `mode` is 1, or
* `onBehalfOf` incurs a variable debt if `mode` is 2.

{% hint style="warning" %}
Your contract which receives the flash loaned amounts **must** conform to the [`IFlashLoanReceiver`](broken-reference) interface. For more, see the [flash loan guides](../../guides/flash-loans/).
{% endhint %}

| Parameter Name    | Type        | Description                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `receiverAddress` | address     | <p>address of the contract receiving the funds.</p><p>Must implement the <code>IFlashLoanReceiver</code> interface.</p>                                                                                                                                                                                                                      |
| `assets`          | `address[]` | addresses of the reserves to flashloan                                                                                                                                                                                                                                                                                                       |
| `amounts`         | `uint256[]` | <p>amounts of <code>assets</code> to flashloan.</p><p>This needs to contain the same number of elements as <code>assets</code>.</p>                                                                                                                                                                                                          |
| `modes`           | `uint256[]` | <p>the types of debt to open if the flashloan is not returned.</p><p>0: Don't open any debt, just revert</p><p>1: stable mode debt</p><p>2: variable mode debt</p>                                                                                                                                                                           |
| `onBehalfOf`      | address     | <p>if the associated <code>mode</code> is not<code>0</code> then the incurred debt will be applied to the <code>onBehalfOf</code> address.</p><p>Note: <code>onBehalfOf</code> must already have <a href="../debt-tokens/#approvedelegation">approved</a> sufficient borrow allowance of the associated asset to <code>msg.sender</code></p> |
| `params`          | bytes       | bytes-encoded parameters to be used by the `receiverAddress` contract                                                                                                                                                                                                                                                                        |
| `referralCode`    | uint16      | referral code for our [referral program](broken-reference)                                                                                                                                                                                                                                                                                   |

## View Methods

### **getReserveData()**

**`function getReserveData(address asset)`**

Returns the state and configuration of the reserve

| Parameter Name | Type    | Description            |
| -------------- | ------- | ---------------------- |
| `asset`        | address | address of the reserve |

#### Return values

| Parameter Name                | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `configuration`               | uint256 | <p>See the <a href="https://github.com/aave/protocol-v2/blob/master/aave-v2-whitepaper.pdf">whitepaper</a> for details on why a bitmask was used.<br>To find out more about these values, see <a href="https://docs.aave.com/risk/asset-risk/risk-parameters#risk-parameters-analysis">the Risk docs</a>.</p><p>bit 0-15: LTV</p><p>bit 16-31: Liq. threshold</p><p>bit 32-47: Liq. bonus</p><p>bit 48-55: Decimals</p><p>bit 56: reserve is active</p><p>bit 57: reserve is frozen</p><p>bit 58: borrowing is enabled</p><p>bit 59: stable rate borrowing enabled</p><p>bit 60-63: reserved</p><p>bit 64-79: reserve factor</p><p></p><p>** <em>All % are 1e4 i.e. percentage plus two decimals</em></p><p>** <em>Decimals is 1e2</em> </p><p>** <em>Caveat on Liquidation bonus</em> <br><code>105% Liq Bonus = 100% principal + 5% bonus</code></p> |
| `liquidityIndex`              | uint128 | liquidity index in ray                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `variableBorrowIndex`         | uint128 | variable borrow index in ray                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `currentLiquidityRate`        | uint128 | current supply / liquidity / deposit rate in ray                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `currentVariableBorrowRate`   | uint128 | current variable borrow rate in ray                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `currentStableBorrowRate`     | uint128 | current stable borrow rate in ray                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `lastUpdateTimestamp`         | uint40  | timestamp of when reserve data was last updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `aTokenAddress`               | address | address of associated aToken (tokenised deposit)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `stableDebtTokenAddress`      | address | address of associated stable debt token                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `variableDebtTokenAddress`    | address | address of associated variable debt token                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `interestRateStrategyAddress` | address | <p>address of interest rate strategy. <br>See <a href="https://docs.aave.com/risk/liquidity-risk/borrow-interest-rate">Risk docs</a> for more info.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `id`                          | uint8   | the position in the list of active reserves                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### getUserAccountData**()**

**`function getUserAccountData(address user)`**

Returns the user account data across all the reserves

| Parameter Name | Type    | Description         |
| -------------- | ------- | ------------------- |
| `user`         | address | address of the user |

#### Return values

| Parameter Name                | Type    | Description                                                                                                                           |
| ----------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `totalCollateralETH`          | uint256 | total collateral in ETH of the use (wei decimal unit)                                                                                 |
| `totalDebtETH`                | uint256 | total debt in ETH of the user (wei decimal unit)                                                                                      |
| `availableBorrowsETH`         | uint256 | borrowing power left of the user (wei decimal unit)                                                                                   |
| `currentLiquidationThreshold` | uint256 | <p>liquidation threshold of the user<br>(1e4 format => percentage plus two decimals)</p>                                              |
| `ltv`                         | uint256 | <p>Loan To Value of the user<br>(1e4 format => percentage plus two decimals)</p>                                                      |
| `healthFactor`                | uint256 | <p>current health factor of the user.</p><p>Also see <a href="./#liquidationcall"><code>liquidationCall()</code></a><code></code></p> |

### getConfiguration**()**

**`function getConfiguration(address asset)`**

Returns the configuration of the reserve

| Parameter Name | Type    | Description            |
| -------------- | ------- | ---------------------- |
| `asset`        | address | address of the reserve |

#### Return values

| Return Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| uint256     | <p>See the <a href="https://github.com/aave/protocol-v2/blob/master/aave-v2-whitepaper.pdf">whitepaper</a> for details on why a bitmask was used.</p><p>bit 0-15: LTV</p><p>bit 16-31: Liq. threshold</p><p>bit 32-47: Liq. bonus</p><p>bit 48-55: Decimals</p><p>bit 56: reserve is active</p><p>bit 57: reserve is frozen</p><p>bit 58: borrowing is enabled</p><p>bit 59: stable rate borrowing enabled</p><p>bit 60-63: reserved</p><p>bit 64-79: reserve factor</p> |

### getUserConfiguration**()**

**`function getUserConfiguration(address user)`**

Returns the configuration of the user across all the reserves.

| Parameter Name | Type    | Description         |
| -------------- | ------- | ------------------- |
| `user`         | address | address of the user |

#### Return values

| Return Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| uint256     | <p>See the <a href="https://github.com/aave/protocol-v2/blob/master/aave-v2-whitepaper.pdf">whitepaper</a> for details on why a bitmask was used.</p><p>The bitmask is divided into pairs of bits, one pair for each asset. </p><p></p><p>The first bit of the pair indicates if it is being used as collateral by the user, the second bit indicates if it is being borrowed.<br><br>The corresponding assets are in the same position as <a href="./#getreserveslist"><code>getReservesList()</code></a><br><br>For example, if the hex value returned is <code>0x40020</code>,  which represents a decimal value of <code>262176</code>, then in binary it is <code>1000000000000100000</code>. If we format the binary value into pairs, starting from the right, we get <code>1 00 00 00 00 00 00 10 00 00</code>.</p><p>If we start from the right and move left in the above binary pairs, the third pair is <code>10</code>. The third reserve listed in <a href="./#getreserveslist"><code>getReserveList()</code></a> is WETH. Therefore the <code>1</code> indicates that WETH is used as collateral, and <code>0</code> indicates that WETH has not been borrowed by this user. </p><p>If we continue to go to the end of the binary pairs (furthest left), we have <code>1</code> which can also be represented as <code>01</code>. This is the 10th pair, which in <a href="./#getreserveslist"><code>getReserveList()</code></a> is DAI. Therefore the <code>0</code> indicates that DAI is not used as collateral, and the <code>1</code> indicates that it is being borrowed by this user.</p><p>In short, if a user is using WETH as collateral and has borrowed DAI, then the value returned would be <code>0x40020</code> (in hex) or <code>262176</code> (in decimal).</p> |

### getReserveNormalizedIncome**()**

**`function getReserveNormalizedIncome(address asset)`**

Returns the normalized income per unit of `asset`.&#x20;

A return value of $$1e27$$ indicates no income. As time passes, the income is accrued. A value of $$2 * 1e27$$ indicates that for each unit of asset, two units of income have been accrued.

| Parameter Name | Type    | Description            |
| -------------- | ------- | ---------------------- |
| `asset`        | address | address of the reserve |

### getReserveNormalizedVariableDebt**()**

**`function getReserveNormalizedVariableDebt(address asset)`**

Returns the normalized variable debt per unit of `asset`.

A return value of $$1e27$$ indicates no debt. As time passes, the debt is accrued. A value of $$2 * 1e27$$ indicates that for each unit of asset, two units of debt have been accrued.

| Parameter Name | Type    | Description            |
| -------------- | ------- | ---------------------- |
| `asset`        | address | address of the reserve |

### paused**()**

**`function paused()`**

Returns `true` if the LendingPool is paused.

### getReservesList**()**

**`function getReservesList()`**

Returns the list of initialized reserves.

### getAddressesProvider**()**

**function getAddressesProvider()**

Returns the addresses provider.

## Error Codes

In order to reduce gas usage and code size, aave contracts return numbered errors. If you are making calls to the protocol and receive numbered errors, you can use our [error code reference guide](../../guides/troubleshooting-errors.md#reference-guide) to know what the error number means. Alternatively, you can also find what the numbers represent by checking the [`Errors.sol`](https://github.com/aave/protocol-v2/blob/master/contracts/protocol/libraries/helpers/Errors.sol)

## ABI

<details>
  <summary>LendingPool ABI</summary>
  
  ```
  [
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reserve",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "onBehalfOf",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "borrowRateMode",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "borrowRate",
                "type": "uint256"
            },
            {
                "indexed": true,
                "internalType": "uint16",
                "name": "referral",
                "type": "uint16"
            }
        ],
        "name": "Borrow",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reserve",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "onBehalfOf",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "indexed": true,
                "internalType": "uint16",
                "name": "referral",
                "type": "uint16"
            }
        ],
        "name": "Deposit",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "target",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "initiator",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "premium",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint16",
                "name": "referralCode",
                "type": "uint16"
            }
        ],
        "name": "FlashLoan",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "collateralAsset",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "debtAsset",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "debtToCover",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "liquidatedCollateralAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "liquidator",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "receiveAToken",
                "type": "bool"
            }
        ],
        "name": "LiquidationCall",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [],
        "name": "Paused",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reserve",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "RebalanceStableBorrowRate",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reserve",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "repayer",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "Repay",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reserve",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "liquidityRate",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "stableBorrowRate",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "variableBorrowRate",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "liquidityIndex",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "variableBorrowIndex",
                "type": "uint256"
            }
        ],
        "name": "ReserveDataUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reserve",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "ReserveUsedAsCollateralDisabled",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reserve",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "ReserveUsedAsCollateralEnabled",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reserve",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "rateMode",
                "type": "uint256"
            }
        ],
        "name": "Swap",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [],
        "name": "Unpaused",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reserve",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "Withdraw",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "FLASHLOAN_PREMIUM_TOTAL",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "LENDINGPOOL_REVISION",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "MAX_NUMBER_RESERVES",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "MAX_STABLE_RATE_BORROW_SIZE_PERCENT",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "interestRateMode",
                "type": "uint256"
            },
            {
                "internalType": "uint16",
                "name": "referralCode",
                "type": "uint16"
            },
            {
                "internalType": "address",
                "name": "onBehalfOf",
                "type": "address"
            }
        ],
        "name": "borrow",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "onBehalfOf",
                "type": "address"
            },
            {
                "internalType": "uint16",
                "name": "referralCode",
                "type": "uint16"
            }
        ],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "balanceFromBefore",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "balanceToBefore",
                "type": "uint256"
            }
        ],
        "name": "finalizeTransfer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "receiverAddress",
                "type": "address"
            },
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "modes",
                "type": "uint256[]"
            },
            {
                "internalType": "address",
                "name": "onBehalfOf",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "params",
                "type": "bytes"
            },
            {
                "internalType": "uint16",
                "name": "referralCode",
                "type": "uint16"
            }
        ],
        "name": "flashLoan",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getAddressesProvider",
        "outputs": [
            {
                "internalType": "contract ILendingPoolAddressesProvider",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            }
        ],
        "name": "getConfiguration",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "data",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct DataTypes.ReserveConfigurationMap",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            }
        ],
        "name": "getReserveData",
        "outputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "data",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct DataTypes.ReserveConfigurationMap",
                        "name": "configuration",
                        "type": "tuple"
                    },
                    {
                        "internalType": "uint128",
                        "name": "liquidityIndex",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "variableBorrowIndex",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "currentLiquidityRate",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "currentVariableBorrowRate",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "currentStableBorrowRate",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint40",
                        "name": "lastUpdateTimestamp",
                        "type": "uint40"
                    },
                    {
                        "internalType": "address",
                        "name": "aTokenAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "stableDebtTokenAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "variableDebtTokenAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "interestRateStrategyAddress",
                        "type": "address"
                    },
                    {
                        "internalType": "uint8",
                        "name": "id",
                        "type": "uint8"
                    }
                ],
                "internalType": "struct DataTypes.ReserveData",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            }
        ],
        "name": "getReserveNormalizedIncome",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            }
        ],
        "name": "getReserveNormalizedVariableDebt",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getReservesList",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "getUserAccountData",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "totalCollateralETH",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "totalDebtETH",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "availableBorrowsETH",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "currentLiquidationThreshold",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "ltv",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "healthFactor",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "getUserConfiguration",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "data",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct DataTypes.UserConfigurationMap",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "aTokenAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "stableDebtAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "variableDebtAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "interestRateStrategyAddress",
                "type": "address"
            }
        ],
        "name": "initReserve",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract ILendingPoolAddressesProvider",
                "name": "provider",
                "type": "address"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "collateralAsset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "debtAsset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "debtToCover",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "receiveAToken",
                "type": "bool"
            }
        ],
        "name": "liquidationCall",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "rebalanceStableBorrowRate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "rateMode",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "onBehalfOf",
                "type": "address"
            }
        ],
        "name": "repay",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "configuration",
                "type": "uint256"
            }
        ],
        "name": "setConfiguration",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bool",
                "name": "val",
                "type": "bool"
            }
        ],
        "name": "setPause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "rateStrategyAddress",
                "type": "address"
            }
        ],
        "name": "setReserveInterestRateStrategyAddress",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "useAsCollateral",
                "type": "bool"
            }
        ],
        "name": "setUserUseReserveAsCollateral",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "rateMode",
                "type": "uint256"
            }
        ],
        "name": "swapBorrowRateMode",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            }
        ],
        "name": "withdraw",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
  ```
</details>
