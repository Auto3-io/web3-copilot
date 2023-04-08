# Addresses Provider Registry

## LendingPoolAddressesProviderRegistry

A register of the active [`LendingPoolAddressesProvider`](../addresses-provider/) contracts, covering all markets. This contract is immutable and the address will never change. Also see [Deployed Contracts](../../deployed-contracts/deployed-contracts.md) section.

For example, the LendingPool address for the main market is different from the LendingPool address for the Uniswap market.

The source code can be found [on Github here](https://github.com/aave/protocol-v2/blob/ice/mainnet-deployment-03-12-2020/contracts/protocol/configuration/LendingPoolAddressesProviderRegistry.sol).

## Methods

### getAddressesProvidersList**()**

**`function getAddressesProvidersList()`**

Returns the list of active [`LendingPoolAddressesProvider`](../addresses-provider/) contracts.

### getAddressesProviderIdByAddress**()**

**`function getAddressesProviderIdByAddress(address addressesProvider)`**

Returns the ID of an [`LendingPoolAddressesProvider`](../addresses-provider/)

| Parameter Name | Type    | Description                       |
| -------------- | ------- | --------------------------------- |
| `provider`     | address | address of the addresses provider |

## ABI

<details>
<summary>Addresses Provider Registry</summary>

```
[
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
        "name": "AddressesProviderRegistered",
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
        "name": "AddressesProviderUnregistered",
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
        "inputs": [
            {
                "internalType": "address",
                "name": "addressesProvider",
                "type": "address"
            }
        ],
        "name": "getAddressesProviderIdByAddress",
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
        "name": "getAddressesProvidersList",
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
        "inputs": [
            {
                "internalType": "address",
                "name": "provider",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "registerAddressesProvider",
        "outputs": [],
        "stateMutability": "nonpayable",
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
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "provider",
                "type": "address"
            }
        ],
        "name": "unregisterAddressesProvider",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
```
</details>