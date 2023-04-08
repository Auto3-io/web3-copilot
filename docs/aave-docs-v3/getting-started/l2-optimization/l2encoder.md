---
description: >-
  Helper contract which has view methods to encode data that is passed to the
  L2Pool.
---

# L2Encoder

## Methods

### encodeSupplyParams

**`function encodeSupplyParams(address asset, uint256 amount, uint16 referralCode) external view returns (bytes32)`**

Returns `bytes32` result to be passed to `supply()` method of L2Pool.

| Param Name   | Type    | Description                                                                    |
| ------------ | ------- | ------------------------------------------------------------------------------ |
| asset        | address | address of the asset being supplied to the pool.                               |
| amount       | uint256 | amount of asset being supplied.                                                |
| referralCode | uint16  | unique code for 3rd party referral program integration. Use 0 for no referral. |

### encodeSupplyWithPermitParams&#x20;

`function encodeSupplyWithPermit(address asset, uint256 amount, uint16 referralCode, uint256 deadline, uint8 permitV, bytes32 permitR, bytes32 permitS)`` `**`external view returns (bytes32, bytes32, bytes32)`**

Returns (`bytes32, bytes32, bytes32`) result to be passed to `supplyWithPermit()` method of L2Pool.

Permit signature must be signed by `msg.sender` with spender as Pool address.&#x20;

Call Params

| Name         | Type    | Description                                                                                  |
| ------------ | ------- | -------------------------------------------------------------------------------------------- |
| asset        | address | Address of underlying asset being supplied. Same asset as used in permit s,v,r               |
| amount       | uint256 | Amount of asset to be supplied and signed for approval. Same amount as used in permit s,v,r  |
| referralCode | uint16  | <p>unique code for 3rd party referral program integration.<br><br>Use 0 for no referral.</p> |
| deadline     | uint256 | unix timestamp up-till which signature will be valid                                         |
| permitV      | uint8   | Signature parameter v                                                                        |
| permitR      | bytes32 | Signature parameter r                                                                        |
| permitS      | bytes32 | Signature parameter s                                                                        |

### encodeWithdrawParams

**`function encodeWithdrawParams(address asset, uint256 amount) external view returns (bytes32)`**

Returns `bytes32` result to be passed to `withdraw()` method of L2Pool.

Call Params

| Name   | Type    | Description                                                                                    |
| ------ | ------- | ---------------------------------------------------------------------------------------------- |
| asset  | address | address of the underlying asset, not the aToken                                                |
| amount | uint256 | amount deposited, expressed in wei units. Use `type(uint).max` to withdraw the entire balance. |

### encodeBorrowParams

**`function encodeBorrowParams(address asset, uint256 amount, uint256 interestRateMode, uint16 referralCode) external view returns (bytes32)`**

Returns `bytes32` result to be passed to `borrow()` method of L2Pool.

Call Params

| Name             | Type    | Description                                                         |
| ---------------- | ------- | ------------------------------------------------------------------- |
| asset            | address | address of the underlying asset                                     |
| amount           | uint256 | amount to be borrowed, expressed in wei units                       |
| interestRateMode | uint256 | <p>the type of borrow debt.<br><br>Stable: 1, Variable: 2</p>       |
| referralCode     | uint16  | referral code for our referral program. Use 0 for no referral code. |

### encodeRepayParams

**`function encodeRepayParams(address asset, uint256 amount, uint256 interestRateMode) external view returns (bytes32)`**

Returns `bytes32` result to be passed to `repay()` method of L2Pool.

Call Params

| Name             | Type    | Description                                                                                                                                                                                                                                                                                                   |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| asset            | address | address of the underlying asset                                                                                                                                                                                                                                                                               |
| amount           | uint256 | <p>amount to be borrowed, expressed in wei units.<br>Use uint(-1) to repay the entire debt,  ONLY when the repayment is not executed on behalf of a 3rd party. <br>In case of repayments on behalf of another user, it's recommended to send an _amount slightly higher than the current borrowed amount.</p> |
| interestRateMode | uint256 | <p>the type of debt being repaid.<br>Stable: 1, Variable: 2</p>                                                                                                                                                                                                                                               |

### encodeRepayWithPermitParams

`function encodeRepayWithPermitParams(address asset, uint256 amount, uint256 interestRateMode, uint256 deadline, uint8 permitV, bytes32 permitR, bytes32 permitS)`` `**`external view returns (bytes32, bytes32, bytes32)`**

Returns (`bytes32, bytes32, bytes32`) result to be passed to `repayWithPermit()` method of L2Pool.

Call Params

| Name             | Type    | Description                                                                                 |
| ---------------- | ------- | ------------------------------------------------------------------------------------------- |
| asset            | address | Address of underlying asset being supplied. Same asset as used in permit s,v,r              |
| amount           | uint256 | Amount of asset to be supplied and signed for approval. Same amount as used in permit s,v,r |
| interestRateMode | uint256 | <p>the type of debt being repaid.<br>Stable: 1, Variable: 2</p>                             |
| deadline         | uint256 | unix timestamp up-till which signature will be valid                                        |
| permitV          | uint8   | Signature parameter v                                                                       |
| permitR          | bytes32 | Signature parameter r                                                                       |
| permitS          | bytes32 | Signature parameter s                                                                       |

### encodeRepayWithATokensParams <a href="#encoderepayparams" id="encoderepayparams"></a>

**`function encodeRepayWithATokensParams(address asset, uint256 amount, uint256 interestRateMode) external view returns (bytes32)`**

Returns `bytes32` result to be passed to `repay()` method of L2Pool.

Call Params​

| Name             | Type    | Description                                                                                                                                                                                                                                                                                                   |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| asset            | address | address of the underlying asset                                                                                                                                                                                                                                                                               |
| amount           | uint256 | <p>amount to be borrowed, expressed in wei units.<br>Use uint(-1) to repay the entire debt,  ONLY when the repayment is not executed on behalf of a 3rd party. <br>In case of repayments on behalf of another user, it's recommended to send an _amount slightly higher than the current borrowed amount.</p> |
| interestRateMode | uint256 | <p>the type of debt being repaid.<br>Stable: 1, Variable: 2</p>                                                                                                                                                                                                                                               |

### encodeSwapBorrowRateMode

**`function encodeSwapBorrowRateMode(address asset, uint256 rateMode) external view returns (bytes32)`**

Returns `bytes32` result to be passed to `swapBorrowRateMode()` method of L2Pool.

Call Params

| Name     | Type    | Description                                                               |
| -------- | ------- | ------------------------------------------------------------------------- |
| asset    | address | address of the underlying asset                                           |
| rateMode | uint256 | <p>the rate mode the user is swapping from.<br>Stable: 1, Variable: 2</p> |

### encodeRebalanceStableBorrowRate

`function encodeRebalanceStableBorrowRate(address asset, address user)`` `**`external view returns (bytes32)`**

Returns `bytes32` result to be passed to `rebalanceStableBorrowRate()` method of L2Pool.

Call Params

| Name  | Type    | Description                                                                                        |
| ----- | ------- | -------------------------------------------------------------------------------------------------- |
| asset | address | Address of the underlying token that has been borrowed for which the position is being rebalanced. |
| user  | address | Address of the user being rebalanced.                                                              |

### encodeSetUserUseReserveAsCollateral

**`function encodeSetUserUseReserveAsCollateral(address asset, bool useAsCollateral) external view returns (bytes32)`**

Returns `bytes32` result to be passed to `setUserUseReserveAsCollateral()` method of L2Pool.

Call Params

| Name            | Type    | Description                                              |
| --------------- | ------- | -------------------------------------------------------- |
| asset           | address | address of the underlying asset to be used as collateral |
| useAsCollateral | bool    | true if the asset should be used as collateral           |

### encodeLiquidationCall&#x20;

**`function encodeLiquidationCall(address collateral, address debt, address user, uint256 debtToCover, bool receiveAToken) external view returns (bytes32, bytes32)`**

Returns (`bytes32, bytes32`) result to be passed to `liquidationCall()` method of L2Pool.

Call Params

| Name          | Type    | Description                                                                                                                               |
| ------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| collateral    | address | address of the collateral reserve                                                                                                         |
| debt          | address | address of the debt reserve                                                                                                               |
| user          | address | address of the borrower                                                                                                                   |
| debtToCover   | uint256 | amount of asset debt that the liquidator will repay                                                                                       |
| receiveAToken | bool    | if true, the user receives the aTokens equivalent of the purchased collateral. If false, the user receives the underlying asset directly. |

## ABI
<details>
<summary>L2Encoder ABI</summary>

```
[
    {
        "inputs": [
            {
                "internalType": "contract IPool",
                "name": "pool",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "POOL",
        "outputs": [
            {
                "internalType": "contract IPool",
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
            }
        ],
        "name": "encodeBorrowParams",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
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
        "name": "encodeLiquidationCall",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
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
        "name": "encodeRebalanceStableBorrowRate",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
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
            }
        ],
        "name": "encodeRepayParams",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
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
            }
        ],
        "name": "encodeRepayWithATokensParams",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
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
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            },
            {
                "internalType": "uint8",
                "name": "permitV",
                "type": "uint8"
            },
            {
                "internalType": "bytes32",
                "name": "permitR",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "permitS",
                "type": "bytes32"
            }
        ],
        "name": "encodeRepayWithPermitParams",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
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
                "internalType": "bool",
                "name": "useAsCollateral",
                "type": "bool"
            }
        ],
        "name": "encodeSetUserUseReserveAsCollateral",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
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
                "internalType": "uint16",
                "name": "referralCode",
                "type": "uint16"
            }
        ],
        "name": "encodeSupplyParams",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
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
                "internalType": "uint16",
                "name": "referralCode",
                "type": "uint16"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            },
            {
                "internalType": "uint8",
                "name": "permitV",
                "type": "uint8"
            },
            {
                "internalType": "bytes32",
                "name": "permitR",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "permitS",
                "type": "bytes32"
            }
        ],
        "name": "encodeSupplyWithPermitParams",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
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
                "name": "interestRateMode",
                "type": "uint256"
            }
        ],
        "name": "encodeSwapBorrowRateMode",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
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
            }
        ],
        "name": "encodeWithdrawParams",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
```
</details>