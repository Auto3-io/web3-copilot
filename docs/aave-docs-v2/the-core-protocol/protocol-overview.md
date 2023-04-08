# Protocol Overview

The Aave Protocol repository can be found [on Github here](https://github.com/aave/protocol-v2/tree/ice/mainnet-deployment-03-12-2020), with an [NPM package available here](https://www.npmjs.com/package/@aave/protocol-v2).

![](<../.gitbook/assets/image (1).png>)

## Main contracts

{% hint style="info" %}
Both `LendingPoolAddressesProvider` and `LendingPoolAddressesProviderRegistry` control the upgradeability of the protocol, including asset listings and changes to protocol parameters. AAVE holders will be in control of both, via Aave Protocol Governance.
{% endhint %}

The main contracts in Aave v2 and their purposes are:

### LendingPool

The main entry point into the Aave Protocol. Most interactions with Aave will happen via the LendingPool, including:

* [deposit()](lendingpool/#deposit)&#x20;
* [borrow()](lendingpool/#borrow)
* [repay()](lendingpool/#repay)
* [swapBorrowRateMode()](lendingpool/#swapborrowratemode)
* [setUserUseReserveAsCollateral()](lendingpool/#setuserusereserveascollateral)
* [withdraw()](lendingpool/#withdraw)
* [flashloan()](lendingpool/#flashloan)
* [liquidationCall()](lendingpool/#liquidationcall)

### LendingPoolAddressesProvider

The main addresses register of the protocol, for particular markets. The latest contract addresses should be retrieved from this contract by making the appropriate calls.

### LendingPoolAddressesProviderRegistry

Contains a list of active `LendingPoolAddressesProvider` addresses, for different markets.

### aTokens

The yield-generating, tokenised deposits used throughout the Aave protocol. They implement most of the standard EIP-20/ERC20 token methods with slight modifications, as well as Aave specific methods including:

* [scaledBalanceOf()](atokens/#scaledbalanceof)
* [getScaledUserBalanceAndSupply()](atokens/#getscaleduserbalanceandsupply)
* [scaledTotalSupply()](atokens/#scaledtotalsupply)

All aTokens also implement [EIP-2612](https://github.com/ethereum/EIPs/blob/8a34d644aacf0f9f8f00815307fd7dd5da07655f/EIPS/eip-2612.md), which via the [`permit()`](atokens/#permit) function enables gas-less transfers and single transaction approve + actions.&#x20;

### Stable and Variable Debt Tokens

The tokenised borrow positions used throughout the Aave protocol. Most of the standard EIP-20/ERC20 methods are disabled, since debt tokens are non-transferrable.

For more information, see the [Debt Tokens](debt-tokens/) section.

## Supporting contracts

The following contracts should generally not be interacted with directly, but are used throughout the Aave Protocol via contract calls.

### LendingPoolCollateralManager

Using `delegatecall` via the LendingPool contract, the LendingPoolCollateralManager implements actions involving management of collateral in the protocol, including:

* `liquidationCall()`

The above function should only be called via the main `LendingPool` contract.

### Lending Pool Configurator

Provides configuration functions for the `LendingPool` contracts. It also has a number of important functions:

* Activates / Deactivates reserves,
* Enables / Disables borrowing for a reserve,
* Enables / Disables using a reserve as collateral,
* Enables / Disables stable rate borrowing for a reserve,
* Freezes / Unfreezes reserves,
* Updates a reserve's Loan to Value,
* Updates a reserve's liquidation threshold,
* Updates a reserve's liquidation bonus,
* Updates a reserve's decimals,
* Updates a reserve's interest rate strategy address,
* Activates / Deactivates all functions of a LendingPool in emergencies.

For all of the above functions, relevant events are emitted to the blockchain. Anyone can monitor these changes to know when values have been modified or added/removed.

### Interest Rate Strategy

Holds the information needed to calculate and update the interest rates of specific reserves.

Each contract stores the optimised base curves using the corresponding parameters of each currency. This means that there is a mathematical function which determines the interest rate of each asset pool, with the interest rate changing based on the amount of borrowed funds and the total liquidity (i.e. utilisation) of the asset pool.

The parameters for the optimised base curves are:

* `baseVariableBorrowRate`
* `variableRateSlope1`
* `variableRateSlope2`
* `stableRateSlope1`
* `stableRateSlope2`

The interest rates are calculated depending on the available liquidity and the total borrowed amount.

### Price Oracle Provider

Provides asset price data required throughout the Aave protocol, using Chainlink and a fallback when necessary. More details on the [Price Oracle](price-oracle/) page.

### Library contracts

Various libraries are also used throughout the Aave Protocol, which can be found on our [Github here](https://github.com/aave/protocol-v2/tree/master/contracts/protocol/libraries).
