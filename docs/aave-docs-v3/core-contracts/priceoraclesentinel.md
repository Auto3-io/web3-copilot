# PriceOracleSentinel

## [PriceOracleSentinel](https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/configuration/PriceOracleSentinel.sol)

This contract validates if the operations are allowed depending on the PriceOracle health.

The `PriceOracle` is considered healthy once its completely up and the grace period has passed.

## View Methods

### [isBorrowAllowed](https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/configuration/PriceOracleSentinel.sol#L62)

`function isBorrowAllowed()`

Return Value

| Type | Description                                                   |
| ---- | ------------------------------------------------------------- |
| bool | Returns true if PriceOracle is up and grace period has passed |

### [isLiquidationAllowed](https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/configuration/PriceOracleSentinel.sol#L67)

`function isLiquidationAllowed()`

Return Value

| Type | Description                                                   |
| ---- | ------------------------------------------------------------- |
| bool | Returns true if PriceOracle is up and grace period has passed |

### [getSequencerOracle](https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/configuration/PriceOracleSentinel.sol#L93)

`function getSequencerOracle()`

Return Value

| Type    | Description                     |
| ------- | ------------------------------- |
| address | Address of the SequencerOracle. |

### [getGracePeriod](https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/configuration/PriceOracleSentinel.sol#L98)

`function getGracePeriod()`

Return Value

| Type    | Description                                  |
| ------- | -------------------------------------------- |
| uint256 | The duration of the grace period in seconds. |

## Write Methods

### [setSequencerOracle](https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/configuration/PriceOracleSentinel.sol#L81)

`function setSequencerOracle(address newSequencerOracle)`

{% hint style="warning" %}
Can be called only by PoolAdmin.
{% endhint %}

Call Params

| Name               | Type    | Description                                  |
| ------------------ | ------- | -------------------------------------------- |
| newSequencerOracle | address | address of the new SequecerOracle to be set. |

### [setGracePeriod](https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/configuration/PriceOracleSentinel.sol#L87)

`function setGracePeriod(uint256 newGracePeriod`

{% hint style="warning" %}
Can be called only by PoolAdmin or RiskAdmin.
{% endhint %}

Call Params

| Name           | Type    | Description                              |
| -------------- | ------- | ---------------------------------------- |
| newGracePeriod | uint256 | duration of new grace period in seconds. |

## ABI
<details>
<summary>PriceOracleSentinel ABI</summary>

```
[
    {
        "inputs": [
            {
                "internalType": "contract IPoolAddressesProvider",
                "name": "provider",
                "type": "address"
            },
            {
                "internalType": "contract ISequencerOracle",
                "name": "oracle",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "gracePeriod",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "newGracePeriod",
                "type": "uint256"
            }
        ],
        "name": "GracePeriodUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "newSequencerOracle",
                "type": "address"
            }
        ],
        "name": "SequencerOracleUpdated",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "ADDRESSES_PROVIDER",
        "outputs": [
            {
                "internalType": "contract IPoolAddressesProvider",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getGracePeriod",
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
        "name": "getSequencerOracle",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "isBorrowAllowed",
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
        "inputs": [],
        "name": "isLiquidationAllowed",
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
                "internalType": "uint256",
                "name": "newGracePeriod",
                "type": "uint256"
            }
        ],
        "name": "setGracePeriod",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newSequencerOracle",
                "type": "address"
            }
        ],
        "name": "setSequencerOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
```
</details>
