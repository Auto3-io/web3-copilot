# DebtToken

Debt tokens are interest-accruing tokens that are minted and burned on `borrow` and `repay`, representing the debt owed by the token holder. There are 2 types of debt tokens:

* _**Stable Debt Tokens**_**:** represent a debt to the protocol with stable interest rate.
* _**Variable Debt Tokens**_**:** represent a debt to the protocol with variable interest rate.

{% hint style="info" %}
Debt tokens are not transferable.
{% endhint %}

The _s/vToken_ value is pegged 1:1 to the value of underlying borrowed asset and represents the current total amount owed to the protocol i.e. principal debt + interest accrued.

## EIP20 Methods

Although debt tokens are modelled on the ERC20/EIP20 standard, they are non-transferrable. Therefore they do not implement any of the standard ERC20/EIP20 functions relating to `transfer()` and `allowance()`.

Following are the standard EIP20 methods that are implemented for the debt tokens:

### balanceOf

`function balanceOf(address account)`

Returns the most up to date accumulated debt (principal+interest) of the user.

### totalSupply

`function totalSupply()`

Returns the most up to date total debt accrued by all protocol users for that specific type _(stable or variable rate)_ of debt token.

### decimals

`function decimals()`

Returns decimals of the token contract.

### symbol

`function symbol()`

Returns the symbol of the token contract.

### name

`function name()`

Returns the name of the token contract.

## EIP712 Methods

### DOMAIN\_SEPARATOR

`function DOMAIN_SEPARATOR()`

Get the domain separator for the token at current chain.

### nonces

`function nonces(address owner)`

Returns the nonce value for address specified as parameter. This is the nonce used when calling `permit()`

```jsx
const token = new Contract(aTokenAddres, aToken.abi, provider);
await token.nonces(user);
```

## Aave Protocol Specific Methods

### Shared View Methods

Below are the view methods available for both type, stable and variable, of debt tokens.

#### POOL

`function POOL()`

Returns the address of the associated Pool for the debt token.

#### borrowAllowance

`function borrowAllowance(address fromUser, address toUser)`

#### UNDERLYING\_ASSET\_ADDRESS

`function UNDERLYING_ASSET_ADDRESS()`

Returns the underlying asset of the debt token.

#### getIncentivesController

`function getIncentivesController()`

Returns the address of the Incentives Controller contract

### Shared Write Methods

Below are the write methods available for both type, stable and variable, of debt tokens.

#### approveDelegation

`function approveDelegation(address delegatee, uint256 amount)`

Sets the `amount` of allowance for `delegatee` to borrow of a particular debt token.

#### delegationWithSig

`function delegationWithSig(address delegator, address delegatee, uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s)`

Sets the `value` of allowance for `delegatee` to borrow of a particular debt token via permit function.

#### setIncentivesController

`function setIncentivesController(IAaveIncentivesController controller)`

Sets a new Incentives Controller.

{% hint style="danger" %}
Only Pool Admin can call this methods. To update Incentives Controller on main Aave market, Governance Proposal must be submitted.
{% endhint %}

### Stable Debt Token Methods

#### getAverageStableRate

`function getAverageStableRate()`

Returns the average stable rate across all the stable rate debt in the protocol as `uint256`.

#### getUserLastUpdated

`function getUserLastUpdated(address user)`

Returns the timestamp of the last action taken by `user` as `uint40`.

#### getUserStableRate

`function getUserStableRate(address user)`

Returns the stable rate of `user` as `uint256`.

#### getSupplyData

`function getSupplyData()`

Returns the principal, the total supply, the average stable rate and the timestamp for the last update.

Return Values

| Type    | Description                                                                       |
| ------- | --------------------------------------------------------------------------------- |
| uint256 | The principal stable debt issued                                                  |
| uint256 | The total stable debt for the reserve across all users. Based on avg stable rate. |
| uint256 | The average stable debt rate across all users.                                    |
| uint40  | The timestamp of the last update on total supply of stable debt token.            |

#### getTotalSupplyAndAvgRate

`function getTotalSupplyAndAvgRate()`

Returns the total supply and average stable rate of the token.

Return Values

| Type    | Description                                                        |
| ------- | ------------------------------------------------------------------ |
| uint256 | total debt token supply. (includes principal + cumulated interest) |
| uint256 | average stable rate                                                |

#### getTotalSupplyLastUpdated

`function getTotalSupplyLastUpdated()`

Returns the timestamp of the last update of the total supply in `uint40`.

#### principalBalanceOf

`function principalBalanceOf(address user)`

Returns the principal debt balance of the user since the last burn/mint action.

### Variable Debt Token Methods

#### scaledBalanceOf

`function scaledBalanceOf(address user)`

Returns the scaled debt balance of `user`. The scaled balance is the sum of all the updated stored balance divided by the reserve's liquidity index at the moment of the update.

#### getScaledUserBalanceAndSupply

`function getScaledUserBalanceAndSupply(address user)`

Returns the scaled balance of the user and the scaled total supply.

#### scaledTotalSupply

`function scaledTotalSupply()`

Returns the scaled total supply of the debt token. Represents sum(debt/index)

#### getPreviousIndex

`function getPreviousIndex(address user)`

Returns last index interest that was accrued to the user's balance (expressed in ray).
