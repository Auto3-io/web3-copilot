# RewardsController

## RewardsController

All rewards type enabled in Aave V3 are managed by [RewardsDistributor.sol](https://github.com/aave/aave-v3-periphery/blob/master/contracts/rewards/RewardsDistributor.sol). This is the contract used to check rewards data, user’s rewards balance and for claiming the rewards.

## Structs

### AssetData

| Name             | Type                          |
| ---------------- | ----------------------------- |
| rewards          | mapping(address ⇒ RewardData) |
| availableRewards | address\[]                    |
| decimals         | uint8                         |

### RewardsData

| Name                | Type                        |
| ------------------- | --------------------------- |
| emissionPerSecond   | uint88                      |
| index               | uint104                     |
| lastUpdateTimestamp | uint32                      |
| distributionEnd     | uint32                      |
| usersIndex          | mapping(address => uint256) |

## View Methods

### getRewardsData

`getRewardsData (asset, reward)`

Get the data of the reward emitted for the asset.

**Call Params**

| Name   | Type    | Description                                                              |
| ------ | ------- | ------------------------------------------------------------------------ |
| asset  | address | address of the a/s/v Tokens for which incentive information is requested |
| reward | address | address of the reward token                                              |

**Return Value**

| Type    | Description                                                     |
| ------- | --------------------------------------------------------------- |
| uint104 | index of the reward token                                       |
| uint88  | total reward tokens awarded per second for the given asset pool |
| uint32  | unix timestamp of last time the emissions were updated          |
| uint32  | unix timestamp of when the emissions will end                   |

### getRewardsByAsset

`getRewardsByAsset (asset)`

Get list of rewards activated for the asset

Call Params

| Name  | Type    | Description                                                              |
| ----- | ------- | ------------------------------------------------------------------------ |
| asset | address | address of the a/s/vTokens for which incentive rewards list is requested |

Return Value

| Type       | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| address\[] | list of reward token addresses activated for the given asset |

## Write Methods

### claimRewards

`claimRewards (assets, amount, to, reward)`

Claims single reward type specified by `reward` for the list of assets. Rewards are received by `to` address.

Call Params

| Name   | Type       | Description                                                                                |
| ------ | ---------- | ------------------------------------------------------------------------------------------ |
| assets | address\[] | address list of assets for which rewards are being claimed. Pass a/s/vToken addresses      |
| amount | uint256    | amount to claim, expressed in wei. Pass MAX\_UINT to claim entire unclaimed reward balance |
| to     | address    | address which will receive the reward tokens                                               |
| reward | address    | address of the reward token being claimed. eg. stkAaave                                    |

### claimRewardsOnBehalf

`claimRewardsOnBehalfOf (assets, amount, user, to, reward)`

Claims single reward type specified by `reward` for the given list of assets on behalf of the `user`. Rewards are received by `to` address.

{% hint style="info" %}
The `msg.sender` must be an authorised claimer set using `setClaimer()` method, via Governance Vote.
{% endhint %}

Call Params

| Name   | Type       | Description                                                                                |
| ------ | ---------- | ------------------------------------------------------------------------------------------ |
| assets | address\[] | address list of assets for which rewards are being claimed. Pass a/s/vToken addresses      |
| amount | uint256    | amount to claim, expressed in wei. Pass MAX\_UINT to claim entire unclaimed reward balance |
| user   | address    | address of user who’s rewards are being claimed                                            |
| to     | address    | address which will receive the reward tokens                                               |
| reward | address    | address of the reward token being claimed. eg. stkAaave                                    |

### claimRewardsToSelf

`claimRewardsToSelf (assets, amount, reward)`

Claims single reward type accrued by the `msg.sender` specified by `reward` for the given list of assets. Rewards are received by `msg.sender` .

Call Params

| Name   | Type       | Description                                                                                |
| ------ | ---------- | ------------------------------------------------------------------------------------------ |
| assets | address\[] | address list of assets for which rewards are being claimed. Pass a/s/vToken addresses      |
| amount | uint256    | amount to claim, expressed in wei. Pass MAX\_UINT to claim entire unclaimed reward balance |
| reward | address    | address of the reward token being claimed. eg. stkAaave                                    |

### claimAllRewards

`claimAllRewards (assets, to)`

Claims all rewards for the list of assets. Rewards are received by `to` address.

Call Params

| Name   | Type       | Description                                                                           |
| ------ | ---------- | ------------------------------------------------------------------------------------- |
| assets | address\[] | address list of assets for which rewards are being claimed. Pass a/s/vToken addresses |
| to     | address    | address which will receive the reward tokens                                          |

### claimAllRewardsOnBehalf

`claimAllRewardsOnBehalfOf (assets, user, to)`

Claims all rewards for the given list of assets on behalf of the `user`. Rewards are received by `to` address.

{% hint style="info" %}
The `msg.sender` must be an authorised claimer set using `setClaimer()` method, via Governance Vote.
{% endhint %}

Call Params

| Name   | Type       | Description                                                                           |
| ------ | ---------- | ------------------------------------------------------------------------------------- |
| assets | address\[] | address list of assets for which rewards are being claimed. Pass a/s/vToken addresses |
| user   | address    | address of user who’s rewards are being claimed                                       |
| reward | address    | address of the reward token being claimed. eg. stkAaave                               |

### claimAllRewardsToSelf

`claimAllRewardsToSelf (assets)`

Claims all rewards accrued by `msg.sender` for the given list of assets. Rewards are received by `msg.sender` .

Call Params

| Name   | Type       | Description                                                                           |
| ------ | ---------- | ------------------------------------------------------------------------------------- |
| assets | address\[] | address list of assets for which rewards are being claimed. Pass a/s/vToken addresses |

## ABI
<details>
<summary>RewardsController ABI</summary>

```
[
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "emissionManager",
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
                "name": "asset",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "reward",
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
                "name": "assetIndex",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "userIndex",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "rewardsAccrued",
                "type": "uint256"
            }
        ],
        "name": "Accrued",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "reward",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "oldEmission",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "newEmission",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "oldDistributionEnd",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "newDistributionEnd",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetIndex",
                "type": "uint256"
            }
        ],
        "name": "AssetConfigUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "claimer",
                "type": "address"
            }
        ],
        "name": "ClaimerSet",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "oldEmissionManager",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newEmissionManager",
                "type": "address"
            }
        ],
        "name": "EmissionManagerUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reward",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "rewardOracle",
                "type": "address"
            }
        ],
        "name": "RewardOracleUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "reward",
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
                "internalType": "address",
                "name": "claimer",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "RewardsClaimed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "reward",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "transferStrategy",
                "type": "address"
            }
        ],
        "name": "TransferStrategyInstalled",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "REVISION",
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
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            }
        ],
        "name": "claimAllRewards",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "rewardsList",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "claimedAmounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            }
        ],
        "name": "claimAllRewardsOnBehalf",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "rewardsList",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "claimedAmounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            }
        ],
        "name": "claimAllRewardsToSelf",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "rewardsList",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "claimedAmounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
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
            },
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "claimRewards",
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
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "claimRewardsOnBehalf",
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
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "claimRewardsToSelf",
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
                "components": [
                    {
                        "internalType": "uint88",
                        "name": "emissionPerSecond",
                        "type": "uint88"
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalSupply",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint32",
                        "name": "distributionEnd",
                        "type": "uint32"
                    },
                    {
                        "internalType": "address",
                        "name": "asset",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "reward",
                        "type": "address"
                    },
                    {
                        "internalType": "contract ITransferStrategyBase",
                        "name": "transferStrategy",
                        "type": "address"
                    },
                    {
                        "internalType": "contract IEACAggregatorProxy",
                        "name": "rewardOracle",
                        "type": "address"
                    }
                ],
                "internalType": "struct RewardsDataTypes.RewardsConfigInput[]",
                "name": "config",
                "type": "tuple[]"
            }
        ],
        "name": "configureAssets",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "getAllUserRewards",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "rewardsList",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "unclaimedAmounts",
                "type": "uint256[]"
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
        "name": "getAssetDecimals",
        "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
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
        "name": "getClaimer",
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
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "getDistributionEnd",
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
        "name": "getEmissionManager",
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
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "getRewardOracle",
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
                "name": "asset",
                "type": "address"
            }
        ],
        "name": "getRewardsByAsset",
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
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "getRewardsData",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
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
        "name": "getRewardsList",
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
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "getTransferStrategy",
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
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "getUserAccruedRewards",
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
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "getUserAssetIndex",
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
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            }
        ],
        "name": "getUserRewards",
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
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "totalSupply",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "userBalance",
                "type": "uint256"
            }
        ],
        "name": "handleAction",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "emissionManager",
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
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "caller",
                "type": "address"
            }
        ],
        "name": "setClaimer",
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
                "name": "reward",
                "type": "address"
            },
            {
                "internalType": "uint32",
                "name": "newDistributionEnd",
                "type": "uint32"
            }
        ],
        "name": "setDistributionEnd",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "emissionManager",
                "type": "address"
            }
        ],
        "name": "setEmissionManager",
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
                "internalType": "address[]",
                "name": "rewards",
                "type": "address[]"
            },
            {
                "internalType": "uint88[]",
                "name": "newEmissionsPerSecond",
                "type": "uint88[]"
            }
        ],
        "name": "setEmissionPerSecond",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            },
            {
                "internalType": "contract IEACAggregatorProxy",
                "name": "rewardOracle",
                "type": "address"
            }
        ],
        "name": "setRewardOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "reward",
                "type": "address"
            },
            {
                "internalType": "contract ITransferStrategyBase",
                "name": "transferStrategy",
                "type": "address"
            }
        ],
        "name": "setTransferStrategy",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
```
</details>