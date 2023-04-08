# Troubleshooting Errors

## Error Codes

In order to reduce gas usage and code size, aave contracts return numbered errors. If you are making calls to the protocol and receive numbered errors, you can use the reference below to know what is the error. Alternatively, you can also find what the numbers represent by checking the [`Errors.sol`](https://github.com/aave/protocol-v2/blob/master/contracts/protocol/libraries/helpers/Errors.sol)

### Reference Guide

`ValidationLogic` and `LendingPoolCollateralManager` return some collateral related errors. Return type `uint`

| ERROR CODE (uint) | ERROR DESCRIPTION                              |
| ----------------- | ---------------------------------------------- |
| 0                 | No Error                                       |
| 1                 | No Collateral available                        |
| 2                 | Collateral cannot be liquidated                |
| 3                 | Currency not borrowed                          |
| 4                 | Health factor above threshold                  |
| 5                 | Not enough liquidity                           |
| 6                 | Health factor lower than liquidation threshold |
| 7                 | Invalid equal assets to swap                   |
| 8                 | Frozen reserve                                 |

Other error codes returned as `string`:

| ERROR CODE (string) | ORIGINATOR                           | ERROR DESCRIPTION                                                          |
| ------------------- | ------------------------------------ | -------------------------------------------------------------------------- |
| 1                   | ValidationLogic                      | Amount must be greater than 0                                              |
| 2                   | ValidationLogic                      | Action requires an active reserve                                          |
| 3                   | ValidationLogic                      | Action cannot be performed because the reserve is frozen                   |
| 4                   | ValidationLogic                      | The current liquidity is not enough                                        |
| 5                   | ValidationLogic                      | User cannot withdraw more than the available balance                       |
| 6                   | ValidationLogic                      | Transfer cannot be allowed                                                 |
| 7                   | ValidationLogic                      | Borrowing is not enabled                                                   |
| 8                   | ValidationLogic                      | Invalid interest rate mode selected                                        |
| 9                   | ValidationLogic                      | Collateral balance is 0                                                    |
| 10                  | ValidationLogic                      | Health factor is lesser than the liquidation threshold                     |
| 11                  | ValidationLogic                      | There is not enough collateral to cover a new borrow                       |
| 12                  | ValidationLogic                      | Stable borrowing not enabled                                               |
| 13                  | ValidationLogic                      | Collateral is same currency that is being borrowed                         |
| 14                  | ValidationLogic                      | The requested amount is greater than the max loan size in stable rate mode |
| 15                  | ValidationLogic                      | No debt of selected type                                                   |
| 16                  | ValidationLogic                      | To repay on behalf of a user an explicit amount to repay is needed         |
| 17                  | ValidationLogic                      | User does not have a stable rate loan in this reserve                      |
| 18                  | ValidationLogic                      | User does not have a variable rate loan in this reserve                    |
| 19                  | ValidationLogic                      | Underlying balance needs to be greater than 0                              |
| 20                  | ValidationLogic                      | User deposit is already being used as collatoral                           |
| 21                  | LendingPool                          | Not enough stable rate borrow balance                                      |
| 22                  | LendingPool                          | Interest rate rebalance conditions not met                                 |
| 23                  | LendingPool                          | Liquidation call failed                                                    |
| 24                  | LendingPool                          | Not enough liquidity to borrow                                             |
| 25                  | LendingPool                          | Requested amount too small for flashloan                                   |
| 26                  | LendingPool                          | The actual balance of protocol is inconsistent                             |
| 27                  | LendingPool                          | The caller of the function is not lending pool configurator                |
| 28                  | LendingPool                          | Inconsistent flashloan params                                              |
| 29                  | a/Debt Token                         | Caller must be lending pool                                                |
| 30                  | a/Debt Token                         | User cannot give allowance to oneself                                      |
| 31                  | a/Debt Token                         | Transfer amount needs to be > 0                                            |
| 32                  | ReserveLogic                         | Reserve has already been initialised                                       |
| 33                  |                                      | Caller not pool admin                                                      |
| 34                  | LendingPoolConfigurator              | Liquidity of reserve needs to be 0                                         |
| 35                  | LendingPoolConfigurator              | Invalid aToken pool address                                                |
| 36                  | LendingPoolConfigurator              | Invalid stable debt token pool address                                     |
| 37                  | LendingPoolConfigurator              | Invalid variable debt token pool address                                   |
| 38                  | LendingPoolConfigurator              | Invalid address of underlying asset for stabled debt token                 |
| 39                  | LendingPoolConfigurator              | Invalid address of underlying asset for variable debt token                |
| 40                  | LendingPoolConfigurator              | Invalid address provider id                                                |
| 41                  | LendingPoolAddressesProviderRegistry | Provider is not registered                                                 |
| 42                  | LendingPoolCollateralManager         | Health factor not below threshold                                          |
| 43                  | LendingPoolCollateralManager         | Collateral cannot be liquidated                                            |
| 44                  | LendingPoolCollateralManager         | User did not borrow the specified currency                                 |
| 45                  | LendingPoolCollateralManager         | Not enough liquidity to liquidate                                          |
| 46                  | LendingPoolCollateralManager         | No errors                                                                  |
| 47                  | LiquidityProvider                    | Invalid flashloan mode                                                     |
| 48                  | Math                                 | Multiplication overflow                                                    |
| 49                  | Math                                 | Addition overflow                                                          |
| 50                  | Math                                 | Division by zero                                                           |
| 51                  | ReserveLogic                         | Liquidity index overflows                                                  |
| 52                  | ReserveLogic                         | Variable borrow index overflow                                             |
| 53                  | ReserveLogic                         | Liquidity rate overflow                                                    |
| 54                  | ReserveLogic                         | Variable borrow rate overflow                                              |
| 55                  | ReserveLogic                         | Stable borrow rate overflow                                                |
| 56                  | a/Debt Token                         | Invalid mint amount                                                        |
| 57                  | LendingPool                          | Failed to repay with collateral                                            |
| 58                  | a/Debt Token                         | Invalid burn amount                                                        |
| 59                  |                                      | Borrow allowance not enough                                                |
| 60                  | LendingPool                          | Failded collateral swap                                                    |
| 61                  | LendingPool                          | Invalid equal assets to swap                                               |
| 62                  | LendingPool                          | Reentrancy not allowed                                                     |
| 63                  | LendingPool                          | Caller must be an aToken                                                   |
| 64                  | LendingPool                          | Pool is paused                                                             |
| 65                  | LendingPool                          | No more reserves allowed                                                   |
| 66                  | LendingPool                          | Invalid amount returned from flash loan executor                           |
| 67                  | ReserveConfiguration                 | Invalid locked total value                                                 |
| 68                  | ReserveConfiguration                 | Invalid liquidity threshold                                                |
| 69                  | ReserveConfiguration                 | Invalid liquidity bonus                                                    |
| 70                  | ReserveConfiguration                 | Invalid decimals                                                           |
| 71                  | ReserveConfiguration                 | Invalid reserve factor                                                     |
| 72                  | LendingPoolAddressesProviderRegistry | Invalid address provider id                                                |
| 73                  | ValidationLogic                      | Inconsistent flashloan params                                              |
| 74                  | LendingPool                          | Inconsistent params length                                                 |
| 75                  | LendingPoolConfigurator              | Invalid configuration                                                      |
| 76                  | LendingPoolConfigurator              | Caller is not an emergency admin                                           |
| 77                  | UserConfiguration                    | Invalid index                                                              |
| 78                  | LendingPool                          | Not a contract                                                             |
| 79                  | stableDebtToken                      | Stable debt overflow                                                       |
| 80                  | stableDebtToken                      | Burn exceeds balance                                                       |

## Debugging transactions on mainnet / Kovan

If your contracts are successfully deployed on a public network, then you can use the very useful service [Tenderly](https://tenderly.co).

Tenderly allows you to debug transactions, just like you would on a local instance, using their powerful tools. If your transaction has reverted, try using their debugger to find the line of code where your transaction failed.

## Debugging transactions in Truffle

If you have an instance of Truffle running (e.g. `console` or `develop`), then you can debug specific transactions using `debug YOUR_TX_HASH` into your Truffle instance. For more information, see the [ez-flashloan starter template README.MD](https://github.com/mrdavey/ez-flashloan#truffle-debugger).

## EVM revert SafeERC20: low-level call failed

This error indicates that a call to the SafeERC20 implementation of a function has failed. In production, you want to keep using these SafeERC20 implementations.&#x20;

However in testing, you may want more precise EVM error messages by removing the SafeERC20 implementations. You can do this by replacing the SafeERC20 calls with standard ERC20 calls. For example, in the[ ez-flashloan starter template](https://github.com/mrdavey/ez-flashloan/blob/4247dbe9b4dfce5b270ce9b836095162403dba1e/contracts/aave/FlashLoanReceiverBase.sol#L35), replace the following:

```
IERC20(_reserve).safeTransfer(_destination, _amount);
```

with:

```
IERC20(_reserve).transfer(_destination, _amount);
```

You will then receive standard EVM error messages if it reverts on this line, which can sometimes be more helpful for debugging purposes.

## Web3 error: nonce too low

This error is usually due to the nonce that is being used by your web3 wallet, when creating a transaction to send. It means that the nonce being used is not correct, as the Ethereum node your wallet is communicating with indicates that there is a more recent transaction (with a higher nonce). [Here is a good overview](https://kb.myetherwallet.com/en/transactions/what-is-nonce/) of nonces in Ethereum transactions.

Some potential solutions:

* If using a web3 wallet such as MetaMask: Go to your MetaMask settings --> Advanced --> Reset Account. This will reset the transaction history stored in your local browser cache, including the nonce count. The next transaction you send will use the most recent nonce from the Ethereum node your wallet is connected to.
* If the error is not coming from your web3 wallet, then it may be due to the Ethereum node it is connected to. For services such as Infura, their network consist of many servers, where a previously submitted transaction may not be present on the server you are currently connected to. In these cases, wait a few minutes, then try again.

