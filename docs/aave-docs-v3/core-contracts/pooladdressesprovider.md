# PoolAddressesProvider

## PoolAddressesProvider

Addresses register of the protocol for a particular market. This contract is immutable and the address will never change.

{% hint style="info" %}
Whenever the \`Pool\` contract is needed, we recommended you fetch the correct address from the \`PoolAddressesProvider\` smart contract.
{% endhint %}

The source code can be [found on Github](https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/configuration/PoolAddressesProvider.sol)

## View Methods

### getMarketId

`function getMarketId() external view override returns (string memory)`

Fetch the market id of the associated Aave market.

Return Values

| Type   | Description                           |
| ------ | ------------------------------------- |
| string | A string representation of the market |

### getAddress

`function getAddress(bytes32 id) public view override returns (address)`

Fetch the address of protocol contract stored at given id.

Call Params

| Name | Type    | Description                                         |
| ---- | ------- | --------------------------------------------------- |
| id   | bytes32 | id. Example, the Protocol Data Provider uses id 0x1 |

Return Values

| Type    | Description                                       |
| ------- | ------------------------------------------------- |
| address | The address associated with the bytes32 id passed |

```tsx
// Get address of incentive controller
import { utils } from '@ethers/lib/utils';

const id =  utils.keccak256(utils.toUtf8Bytes("INCENTIVES_CONTROLLER"));
const address = poolAddressProvider.getAddress(id);
```

### getPool

`function getPool() external view override returns (address)`

Fetch the contract of latest pool

Return Values

| Type    | Description                        |
| ------- | ---------------------------------- |
| address | The address of the associated Pool |

### getPoolConfigurator

`function getPoolConfigurator() external view override returns (address)`

Fetch the `PoolConfigurator` is used for configuration methods, like init reserves or update token implementation etc, of the market.

Return Value

| Type    | Description                                         |
| ------- | --------------------------------------------------- |
| address | The address of associated market’s PoolConfigurator |

### getPriceOracle

`function getPriceOracle() external view override returns (address)`

Fetch Price Oracle used by the market.

Return Value

| Type    | Description                                                |
| ------- | ---------------------------------------------------------- |
| address | The address of the price oracle used by associated market. |

### getACLManager

`function getACLManager() external view override returns (address)`

Fetch ACLManger that manages the system role of the market

Return Value

| Type    | Description                                                                              |
| ------- | ---------------------------------------------------------------------------------------- |
| address | The address of the ACLManger contract managing the system role of the associated market. |

### getACLAdmin

`function getACLAdmin() external view override returns (address)`

Fetch ACLAdmin of the market which holds the `DEFAULT_ADMIN_ROLE` in ACLManager.

Return Value

| Type    | Description                                                            |
| ------- | ---------------------------------------------------------------------- |
| address | The address of the access control list admin of the associated market. |

### getPriceOracleSentinel

`function getPriceOracleSentinel() external view override returns (address)`

Return Value

| Type    | Description                                                        |
| ------- | ------------------------------------------------------------------ |
| address | The address of the Price oracle sentinel of the associated market. |

### getPoolDataProvider

`function getPoolDataProvider() external view override returns (address)`
Fetch address of latest pool data provider.

Return Value

| Type    | Description                                                     |
| ------- | --------------------------------------------------------------- |
| address | The address of the pool data provider of the associated market. |

## Write Methods

### setMarketId

`function setMarketId(string memory newMarketId) external override onlyOwner`

Updates the identifier of the Aave market

Call Params
| Name        | Type    | Description               |
| ----------- | ------- | ------------------------- |
| newMarketId | `string` | The new id of the market |


### setAddress

`function setAddress(bytes32 id, address newAddress) external override onlyOwner`

Sets the address of protocol contract stored at given id.

Eg. `utils.keccak256(utils.toUtf8Bytes("INCENTIVES_CONTROLLER"))` is set to address of `INCENTIVES_CONTROLLER`

Call Params
| Name        | Type    | Description               |
| ----------- | ------- | ------------------------- |
| id | `bytes32` | keccak256 hash of UTF8Bytes string representing Contract |
| newAddress | `address` | The new address to be set corresponding to the `id` |


### setAddressAsProxy

`function setAddressAsProxy(bytes32 id, address newImplementationAddress) external override onlyOwner`

Sets/updates the implementation address of a specific proxied protocol contract.

{% hint style="info" %}
If there is no proxy registered with the given identifier, it creates the proxy setting `newAddress` as implementation and calls the initialize() function on the proxy
{% endhint %}

Call Params
| Name        | Type    | Description               |
| ----------- | ------- | ------------------------- |
| id | `bytes32` | id of Proxy contract |
| newImplementationAddress | `address` | The address of new implementation contract corresponding to the proxy |

### setPoolImpl

`function setPoolImpl(address newPoolImpl) external override onlyOwner `

Sets/update the implementation of the POOL proxy contract.

Call Params
| Name        | Type    | Description               |
| ----------- | ------- | ------------------------- |
| newPoolImpl | `address` | The address of new Pool implementation contract |

### setPoolConfiguratorImp

`function setPoolConfiguratorImpl(address newPoolConfiguratorImpl) external override onlyOwner`

Sets/updates the implementation of the POOL_CONFIGURATOR proxy contract.

Call Params
| Name        | Type    | Description               |
| ----------- | ------- | ------------------------- |
| newPoolConfiguratorImpl | `address` | The address of new PoolConfigurator implementation contract |

### setPriceOracle

`function setPriceOracle(address newPriceOracle) external override onlyOwner`

Sets/updates address of the PriceOracle contract.

Call Params
| Name        | Type    | Description               |
| ----------- | ------- | ------------------------- |
| newPriceOracle | `address` | The address of new PriceOracle contract |

### setACLAdmin

`function setACLAdmin(address newAclAdmin) external override onlyOwner `

Sets/updates address of the AclAdmin.

Call Params
| Name        | Type    | Description               |
| ----------- | ------- | ------------------------- |
| newAclAdmin | `address` | The address of new AclAdming |

### setPriceOracleSentinel

`function setPriceOracleSentinel(address newPriceOracleSentinel) external override onlyOwner`

Sets/updates address of the Price oracle sentinel.

Call Params
| Name        | Type    | Description               |
| ----------- | ------- | ------------------------- |
| newPriceOracleSentinel | `address` | The address of new PriceOracleSentinel |

### setPoolDataProvider

`function setPoolDataProvider(address newDataProvider) external override onlyOwner`

Sets/updates address of PoolDataProvider.

Call Params
| Name        | Type    | Description               |
| ----------- | ------- | ------------------------- |
| newDataProvider | `address` | The address of new PoolDataProvider |

## ABI

<details>
<summary>PoolAddressesProvider ABI</summary>

```
[
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "marketId",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "ACLAdminUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "ACLManagerUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
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
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "proxyAddress",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "oldImplementationAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newImplementationAddress",
                "type": "address"
            }
        ],
        "name": "AddressSetAsProxy",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "string",
                "name": "oldMarketId",
                "type": "string"
            },
            {
                "indexed": true,
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
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PoolConfiguratorUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PoolDataProviderUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PoolUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PriceOracleSentinelUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
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
                "indexed": true,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "proxyAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "implementationAddress",
                "type": "address"
            }
        ],
        "name": "ProxyCreated",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "getACLAdmin",
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
        "name": "getACLManager",
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
        "name": "getPool",
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
        "name": "getPoolConfigurator",
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
        "name": "getPoolDataProvider",
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
        "name": "getPriceOracleSentinel",
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
                "internalType": "address",
                "name": "newAclAdmin",
                "type": "address"
            }
        ],
        "name": "setACLAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newAclManager",
                "type": "address"
            }
        ],
        "name": "setACLManager",
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
                "name": "newImplementationAddress",
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
                "internalType": "string",
                "name": "newMarketId",
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
                "name": "newPoolConfiguratorImpl",
                "type": "address"
            }
        ],
        "name": "setPoolConfiguratorImpl",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newDataProvider",
                "type": "address"
            }
        ],
        "name": "setPoolDataProvider",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newPoolImpl",
                "type": "address"
            }
        ],
        "name": "setPoolImpl",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newPriceOracle",
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
                "name": "newPriceOracleSentinel",
                "type": "address"
            }
        ],
        "name": "setPriceOracleSentinel",
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