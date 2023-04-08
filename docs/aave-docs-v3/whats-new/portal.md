# Portal

## Introduction

Portal feature can be used to allow supplied assets to seamlessly flow between Aave markets on different networks.

{% hint style="warning" %}
This feature can be used by _**bridging protocol**_. There are no core-protocol methods for end-user to take advantage of Portals directly.
{% endhint %}

Aave protocol V3 allows _**approved bridges**_ to burn _aTokens_ on the source network while instantly minting them on the destination network. The underlying assets can then be supplied to Aave on the destination network, in a deferred manner, by passing it to the pool after it has been moved through a bridge.

![](<../.gitbook/assets/image (1).png>)

## How it works?

Consider a scenario where a user wants to move funds from Ethereum to an L2 or another chain (eg., Arbitrum, Avalanche):

* The user submit _bridge tx_ to verified bridging protocol (say Connext) and have access to funds on the destination chain as soon as _tx_ is mined.
* Behind the scenes, bridging protocol:
  * mints _unbacked aTokens_, on the destination chain, to the intermediate contract and in-turn withdraw and transfer _underlying asset_ to the user immediately.
  * batch multiple bridge tx and actually move the underlying asset to L2
  * Later once the funds are available on L2, _bridge contract_ on L2 (i.e. with `BRIDGE` permissions on Aave V3) supply the _underlying asset_ and _fee_ to the Aave pool to back the previously minted _unbacked aTokens._

There are 3 parts involved in taking advantage of this feature:

*   Approve contracts for `BRIDGE` role

    `function addBridge (bridge)`

    Since, only the contracts (addresses) added to the list of `BRIDGE` role members can move the supplied liquidity across Aave V3 markets, the Aave Governance must have granted the required permissions/role to the verified _Bridge Contract_ via ACLManager.

{% hint style="danger" %}
The interest rate computation is part of the core protocol but the calculation of the deferred supplies to cover unbacked amount and protocol fee is not enforced by the core protocol. Hence, _caution must be taken by governance while approving the bridges._
{% endhint %}

*   Have access to liquidity on destination network instantly

    `function mintUnbacked (asset, amount, onBehalfOf, referralCode)`

    The contracts with `BRIDGE` role can access supplied assets in Aave V3 across network instantly by calling [`mintUnbacked` in Pool.sol](../core-contracts/pool.md#mintunbacked). The address specified by `onBehalfOf` will have access to the respective `amount` of _aToken_.

{% hint style="danger" %}
To prevent potential risks of excessive minting of unbacked aTokens, an `unbackedMintCap` is specified per asset.
{% endhint %}

*   Back the liquidity after moving funds through bridge

    `function backUnbacked (asset, amount, fee)`

    Once the underlying asset are moved to the destination network via _Cross Chain_ _Bridge_, it can be supplied to Aave V3 pool on the destination network along with the fee by calling [`backUnbacked` in Pool.sol](../core-contracts/pool.md#backunbacked).

{% hint style="info" %}
The amount to back and fee paid to the protocol is decided by the governance vote for `BRIDGE` role.
{% endhint %}
