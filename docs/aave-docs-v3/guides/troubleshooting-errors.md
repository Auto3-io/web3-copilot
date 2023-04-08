# Troubleshooting Errors

## Error Codes

In order to reduce gas usage and code size, aave contracts return numbered errors. If you are making calls to the protocol and receive numbered errors, you can use the reference below to know what is the error. Alternatively, you can also find what the numbers represent by checking the [`Errors.sol`](https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/libraries/helpers/Errors.sol)

### Reference Guide

Error codes are returned as string.

| ERROR CODE (string) | ERROR NAME                                     | ERROR DESCRIPTION                                                                                         |
| ------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 1                   | CALLER_NOT_POOL_ADMIN                          | The caller of the function is not a pool admin                                                            |
| 2                   | CALLER_NOT_EMERGENCY_ADMIN                     | The caller of the function is not an emergency admin                                                      |
| 3                   | CALLER_NOT_POOL_OR_EMERGENCY_ADMIN             | The caller of the function is not a pool or emergency admin                                               |
| 4                   | CALLER_NOT_RISK_OR_POOL_ADMIN                  | The caller of the function is not a risk or pool admin                                                    |
| 5                   | CALLER_NOT_ASSET_LISTING_OR_POOL_ADMIN         | The caller of the function is not an asset listing or pool admin                                          |
| 6                   | CALLER_NOT_BRIDGE                              | The caller of the function is not a bridge                                                                |
| 7                   | ADDRESSES_PROVIDER_NOT_REGISTERED              | Pool addresses provider is not registered                                                                 |
| 8                   | INVALID_ADDRESSES_PROVIDER_ID                  | Invalid id for the pool addresses provider                                                                |
| 9                   | NOT_CONTRACT                                   | Address is not a contract                                                                                 |
| 10                  | CALLER_NOT_POOL_CONFIGURATOR                   | The caller of the function is not the pool configurator                                                   |
| 11                  | CALLER_NOT_ATOKEN                              | The caller of the function is not an AToken                                                               |
| 12                  | INVALID_ADDRESSES_PROVIDER                     | The address of the pool addresses provider is invalid                                                     |
| 13                  | INVALID_FLASHLOAN_EXECUTOR_RETURN              | Invalid return value of the flashloan executor function                                                   |
| 14                  | RESERVE_ALREADY_ADDED                          | Reserve has already been added to reserve list                                                            |
| 15                  | NO_MORE_RESERVES_ALLOWED                       | Maximum amount of reserves in the pool reached                                                            |
| 16                  | EMODE_CATEGORY_RESERVED                        | Zero eMode category is reserved for volatile heterogeneous assets                                         |
| 17                  | INVALID_EMODE_CATEGORY_ASSIGNMENT              | Invalid eMode category assignment to asset                                                                |
| 18                  | RESERVE_LIQUIDITY_NOT_ZERO                     | The liquidity of the reserve needs to be 0                                                                |
| 19                  | FLASHLOAN_PREMIUM_INVALID                      | Invalid flashloan premium                                                                                 |
| 20                  | INVALID_RESERVE_PARAMS                         | Invalid risk parameters for the reserve                                                                   |
| 21                  | INVALID_EMODE_CATEGORY_PARAMS                  | Invalid risk parameters for the eMode category                                                            |
| 22                  | BRIDGE_PROTOCOL_FEE_INVALID                    | Invalid bridge protocol fee                                                                               |
| 23                  | CALLER_MUST_BE_POOL                            | The caller of this function must be a pool                                                                |
| 24                  | INVALID_MINT_AMOUNT                            | Invalid amount to mint                                                                                    |
| 25                  | INVALID_BURN_AMOUNT                            | Invalid amount to burn                                                                                    |
| 26                  | INVALID_AMOUNT                                 | Amount must be greater than 0                                                                             |
| 27                  | RESERVE_INACTIVE                               | Action requires an active reserve                                                                         |
| 28                  | RESERVE_FROZEN                                 | Action cannot be performed because the reserve is frozen                                                  |
| 29                  | RESERVE_PAUSED                                 | Action cannot be performed because the reserve is paused                                                  |
| 30                  | BORROWING_NOT_ENABLED                          | Borrowing is not enabled                                                                                  |
| 31                  | STABLE_BORROWING_NOT_ENABLED                   | Stable borrowing is not enabled                                                                           |
| 32                  | NOT_ENOUGH_AVAILABLE_USER_BALANCE              | User cannot withdraw more than the available balance                                                      |
| 33                  | INVALID_INTEREST_RATE_MODE_SELECTED            | Invalid interest rate mode selected                                                                       |
| 34                  | COLLATERAL_BALANCE_IS_ZERO                     | The collateral balance is 0                                                                               |
| 35                  | HEALTH_FACTOR_LOWER_THAN_LIQUIDATION_THRESHOLD | Health factor is lesser than the liquidation threshold                                                    |
| 36                  | COLLATERAL_CANNOT_COVER_NEW_BORROW             | There is not enough collateral to cover a new borrow                                                      |
| 37                  | COLLATERAL_SAME_AS_BORROWING_CURRENCY          | Collateral is (mostly) the same currency that is being borrowed                                           |
| 38                  | AMOUNT_BIGGER_THAN_MAX_LOAN_SIZE_STABLE        | The requested amount is greater than the max loan size in stable rate mode                                |
| 39                  | NO_DEBT_OF_SELECTED_TYPE                       | For repayment of a specific type of debt, the user needs to have debt that type                           |
| 40                  | NO_EXPLICIT_AMOUNT_TO_REPAY_ON_BEHALF          | To repay on behalf of a user an explicit amount to repay is needed                                        |
| 41                  | NO_OUTSTANDING_STABLE_DEBT                     | User does not have outstanding stable rate debt on this reserve                                           |
| 42                  | NO_OUTSTANDING_VARIABLE_DEBT                   | User does not have outstanding variable rate debt on this reserve                                         |
| 43                  | UNDERLYING_BALANCE_ZERO                        | The underlying balance needs to be greater than 0                                                         |
| 44                  | INTEREST_RATE_REBALANCE_CONDITIONS_NOT_MET     | Interest rate rebalance conditions were not met                                                           |
| 45                  | HEALTH_FACTOR_NOT_BELOW_THRESHOLD              | Health factor is not below the threshold                                                                  |
| 46                  | COLLATERAL_CANNOT_BE_LIQUIDATED                | The collateral chosen cannot be liquidated                                                                |
| 47                  | SPECIFIED_CURRENCY_NOT_BORROWED_BY_USER        | User did not borrow the specified currency                                                                |
| 48                  | SAME_BLOCK_BORROW_REPAY                        | Borrow and repay in same block is not allowed                                                             |
| 49                  | INCONSISTENT_FLASHLOAN_PARAMS                  | Inconsistent flashloan parameters                                                                         |
| 50                  | BORROW_CAP_EXCEEDED                            | Borrow cap is exceeded                                                                                    |
| 51                  | SUPPLY_CAP_EXCEEDED                            | Supply cap is exceeded                                                                                    |
| 52                  | UNBACKED_MINT_CAP_EXCEEDED                     | Unbacked mint cap is exceeded                                                                             |
| 53                  | DEBT_CEILING_EXCEEDED                          | Debt ceiling is exceeded                                                                                  |
| 54                  | ATOKEN_SUPPLY_NOT_ZERO                         | AToken supply is not zero                                                                                 |
| 55                  | STABLE_DEBT_NOT_ZERO                           | Stable debt supply is not zero                                                                            |
| 56                  | VARIABLE_DEBT_SUPPLY_NOT_ZERO                  | Variable debt supply is not zero                                                                          |
| 57                  | LTV_VALIDATION_FAILED                          | Ltv validation failed                                                                                     |
| 58                  | INCONSISTENT_EMODE_CATEGORY                    | Inconsistent eMode category                                                                               |
| 59                  | PRICE_ORACLE_SENTINEL_CHECK_FAILED             | Price oracle sentinel validation failed                                                                   |
| 60                  | ASSET_NOT_BORROWABLE_IN_ISOLATION              | Asset is not borrowable in isolation mode                                                                 |
| 61                  | RESERVE_ALREADY_INITIALIZED                    | Reserve has already been initialized                                                                      |
| 62                  | USER_IN_ISOLATION_MODE                         | User is in isolation mode                                                                                 |
| 63                  | INVALID_LTV                                    | Invalid ltv parameter for the reserve                                                                     |
| 64                  | INVALID_LIQ_THRESHOLD                          | Invalid liquidity threshold parameter for the reserve                                                     |
| 65                  | INVALID_LIQ_BONUS                              | Invalid liquidity bonus parameter for the reserve                                                         |
| 66                  | INVALID_DECIMALS                               | Invalid decimals parameter of the underlying asset of the reserve                                         |
| 67                  | INVALID_RESERVE_FACTOR                         | Invalid reserve factor parameter for the reserve                                                          |
| 68                  | INVALID_BORROW_CAP                             | Invalid borrow cap for the reserve                                                                        |
| 69                  | INVALID_SUPPLY_CAP                             | Invalid supply cap for the reserve                                                                        |
| 70                  | INVALID_LIQUIDATION_PROTOCOL_FEE               | Invalid liquidation protocol fee for the reserve                                                          |
| 71                  | INVALID_EMODE_CATEGORY                         | Invalid eMode category for the reserve                                                                    |
| 72                  | INVALID_UNBACKED_MINT_CAP                      | Invalid unbacked mint cap for the reserve                                                                 |
| 73                  | INVALID_DEBT_CEILING                           | Invalid debt ceiling for the reserve                                                                      |
| 74                  | INVALID_RESERVE_INDEX                          | Invalid reserve index                                                                                     |
| 75                  | ACL_ADMIN_CANNOT_BE_ZERO                       | ACL admin cannot be set to the zero address                                                               |
| 76                  | INCONSISTENT_PARAMS_LENGTH                     | Array parameters that should be equal length are not                                                      |
| 77                  | ZERO_ADDRESS_NOT_VALID                         | Zero address not valid                                                                                    |
| 78                  | INVALID_EXPIRATION                             | Invalid expiration                                                                                        |
| 79                  | INVALID_SIGNATURE                              | Invalid signature                                                                                         |
| 80                  | OPERATION_NOT_SUPPORTED                        | Operation not supported                                                                                   |
| 81                  | DEBT_CEILING_NOT_ZERO                          | Debt ceiling is not zero                                                                                  |
| 82                  | ASSET_NOT_LISTED                               | Asset is not listed                                                                                       |
| 83                  | INVALID_OPTIMAL_USAGE_RATIO                    | Invalid optimal usage ratio                                                                               |
| 84                  | INVALID_OPTIMAL_STABLE_TO_TOTAL_DEBT_RATIO     | Invalid optimal stable to total debt ratio                                                                |
| 85                  | UNDERLYING_CANNOT_BE_RESCUED                   | The underlying asset cannot be rescued                                                                    |
| 86                  | ADDRESSES_PROVIDER_ALREADY_ADDED               | Reserve has already been added to reserve list                                                            |
| 87                  | POOL_ADDRESSES_DO_NOT_MATCH                    | The token implementation pool address and the pool address provided by the initializing pool do not match |
| 88                  | STABLE_BORROWING_ENABLED                       | Stable borrowing is enabled                                                                               |
| 89                  | SILOED_BORROWING_VIOLATION                     | User is trying to borrow multiple assets including a siloed one                                           |
| 90                  | RESERVE_DEBT_NOT_ZERO                          | // the total debt of the reserve needs to be 0                                                            |
