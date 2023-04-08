# Changes from v1 to v2

Aave v2 improves many aspects over v1, opening up a vast new design space for developers to build products and services.

If you previously built on Aave v1, the following changes should be noted.

## Tokenization

### Keeping track of user positions

In Aave v2, all positions are tokenised. Therefore to calculate the debt that a user has, you just need to call `balanceOf()` for the associated debt token of that user.

See both [aTokens](the-core-protocol/atokens/) and [Debt Tokens](the-core-protocol/debt-tokens/) sections for more info.

### Approving ERC20/EIP20 tokens: LendingPool vs LendingPoolCore

In Aave v2, there is no more `LendingPoolCore` contract that holds all the protocol's assets. Asset's are held directly in the associated aToken contracts, with the [`LendingPool`](the-core-protocol/lendingpool/) being the 'core' contract of the protocol.

### WETH support

In Aave v2, to ensure consistency throughout the protocol we now use WETH (instead of ETH and a placeholder `reserve` value as was done in v1). Therefore to call a function using the ETH as an asset, use the [WETH address](deployed-contracts/deployed-contracts.md#supported-assets).

There is also a WETH helper contract that will help with wrapping/unwrapping ETH, when used within the protocol.

## Deposits

### Redeem and Withdraw via LendingPool, not the aToken

In Aave v2, nearly all actions should be performed via the `LendingPool` contract. This is different from v1, where a redeem/withdraw of an aTokens needed to be called on the aToken contract.&#x20;

In v2, you will need to call [withdraw](the-core-protocol/lendingpool/#withdraw) on the `LendingPool` contract only.

### Removal of interest redirection feature

In the initial release of Aave v2, interest redirection is not supported. However it is possible that the feature is added back later, via the governance process.

## Borrowing

### Native Credit Delegation

When a user has deposited collateral in the protocol, they can easily delegate credit to any address by calling [`approveDelegation()`](the-core-protocol/debt-tokens/#approvedelegation) on the relevant debt token.&#x20;

See the [Credit Delegation guide](guides/credit-delegation.md) for more details.

## Flash Loans

### Within the protocol

In Aave v2, flash loans are possible within the protocol itself. In fact, they are used extensively within the protocol for position swapping and other 'trading' like features.&#x20;

See the [Flash loans](guides/flash-loans/) section for more details.

### Batch flash loans

Flash loans can now be performed in batches, i.e. multiple flash loans with different parameters in the same call. This will allow powerful new use cases, such as paying back multiple assets and positions with [one flash loan transaction](https://kovan.etherscan.io/tx/0xf248bc23f93826b44e4ab18c6dc2a1e6b320e752637f3749288485b5058f7013).

### Flash loans modes

You can now perform a mix of 'traditional' flash loans, which are paid back immediately, along with flash loans where a debt is incurred (i.e. the flash loan isn't paid back immediately).&#x20;

See the [Flash loans](guides/flash-loans/) section for more details.

## Structural Changes

### Addresses Provider Registry

With multiple markets, there will be multiple `AddressesProviders`. The [`AddressesProviderRegistry`](the-core-protocol/addresses-provider-registry/) will maintain a registry of all the Aave market addresses providers.

### Replacing LendingPoolCore

`LendingPoolCore` is no longer used. Only `LendingPool` is used, which simplifies integrations and building on Aave v2.

