# Addresses Provider

## LendingPoolAddressesProvider

Addresses register of the protocol for a particular market. This contract is immutable and the address will never change. Also see [Deployed Contracts](../../deployed-contracts/deployed-contracts.md) section.

{% hint style="info" %}
Whenever the `LendingPool` contract is needed, we recommended you fetch the correct address from the `LendingPoolAddressesProvider` smart contract.
{% endhint %}

The source code can be [found on Github here](https://github.com/aave/protocol-v2/blob/ice/mainnet-deployment-03-12-2020/contracts/protocol/configuration/LendingPoolAddressesProvider.sol).

## Methods

### getMarketId**()**

**`function getMarketId()`**

#### Return values

| Type   | Description                           |
| ------ | ------------------------------------- |
| string | A string representation of the market |

### getLendingPool**()**

**`function getLendingPool()`**

#### Return values

| Type    | Description                                                  |
| ------- | ------------------------------------------------------------ |
| address | The address of the associated [LendingPool](../lendingpool/) |

### getLendingPoolConfigurator**()**

**`function getLendingPoolConfigurator()`**

The `LendingPoolConfigurator` is used for configuration methods for each market, e.g.initialising a reserve or updating aTokens.

#### Return values

| Type    | Description                                            |
| ------- | ------------------------------------------------------ |
| address | The address of the associated `LendingPoolConfiguator` |

### getLendingPoolCollateralManager**()**

**`function getLendingPoolCollateralManager()`**

The `LendingPoolCollateralManager` is used for management of collateral in the protocol, the main one being for liquidations. The contract should never be called directly, only via the `LendingPool`.

#### Return values

| Type    | Description                                                  |
| ------- | ------------------------------------------------------------ |
| address | The address of the associated `LendingPoolCollateralManager` |

### getPoolAdmin**()**

**`function getPoolAdmin()`**

#### Return values

| Type    | Description                              |
| ------- | ---------------------------------------- |
| address | The address of the market / pool's admin |

### getPoolEmergencyAdmin**()**

**`function getPoolEmergencyAdmin()`**

#### Return values

| Type    | Description                                        |
| ------- | -------------------------------------------------- |
| address | The address of the market / pool's emergency admin |

### getPriceOracle**()**

**`function getPriceOracle()`**

#### Return values

| Type    | Description                     |
| ------- | ------------------------------- |
| address | The address of the price oracle |

### getLendingRateOracle**()**

**`function getLendingRateOracle()`**

#### Return values

| Type    | Description                            |
| ------- | -------------------------------------- |
| address | The address of the `LendingRateOracle` |

### getAddress**()**

**`function getAddress(bytes32 id)`**

For example, the [Protocol Data Provider](../protocol-data-provider/) uses the id: `0x1`

#### Return values

| Type    | Description                                       |
| ------- | ------------------------------------------------- |
| address | The address associated with the `bytes32` id used |

## ABI

<details>
<summary>Addresses Provider ABI</summary>

```
[
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "marketId",
                "type": "string"
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
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "hasProxy",
                "type": "bool"
            }
        ],
        "name": "AddressSet",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "ConfigurationAdminUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "EmergencyAdminUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "LendingPoolCollateralManagerUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "LendingPoolConfiguratorUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "LendingPoolUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "LendingRateOracleUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "string",
                "name": "newMarketId",
                "type": "string"
            }
        ],
        "name": "MarketIdSet",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PriceOracleUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "ProxyCreated",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            }
        ],
        "name": "getAddress",
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
        "name": "getEmergencyAdmin",
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
        "name": "getLendingPool",
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
        "name": "getLendingPoolCollateralManager",
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
        "name": "getLendingPoolConfigurator",
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
        "name": "getLendingRateOracle",
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
        "name": "getMarketId",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getPoolAdmin",
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
        "name": "getPriceOracle",
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
        "name": "owner",
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
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "setAddress",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "implementationAddress",
                "type": "address"
            }
        ],
        "name": "setAddressAsProxy",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "emergencyAdmin",
                "type": "address"
            }
        ],
        "name": "setEmergencyAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "manager",
                "type": "address"
            }
        ],
        "name": "setLendingPoolCollateralManager",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "configurator",
                "type": "address"
            }
        ],
        "name": "setLendingPoolConfiguratorImpl",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            }
        ],
        "name": "setLendingPoolImpl",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "lendingRateOracle",
                "type": "address"
            }
        ],
        "name": "setLendingRateOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "marketId",
                "type": "string"
            }
        ],
        "name": "setMarketId",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "admin",
                "type": "address"
            }
        ],
        "name": "setPoolAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "priceOracle",
                "type": "address"
            }
        ],
        "name": "setPriceOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
```
</details>
