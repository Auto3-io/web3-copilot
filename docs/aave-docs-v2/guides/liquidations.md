# Liquidations

The health of the Aave Protocol is dependant on the 'health' of the loans within the system, also known as the 'health factor'. When the 'health factor' of an account's total loans is below 1, anyone can make a [`liquidationCall()`](../the-core-protocol/lendingpool/#liquidationcall) to the `LendingPool` contract, paying back part of the debt owed and receiving discounted collateral in return (also known as the liquidation bonus as [listed here](https://docs.aave.com/risk/asset-risk/risk-parameters)).&#x20;

This incentivises third parties to participate in the health of the overall protocol, by acting in their own interest (to receive the discounted collateral) and as a result, ensure loans are sufficiently collateralised.

There are multiple ways to participate in liquidations:

1. By calling the [`liquidationCall()`](../the-core-protocol/lendingpool/#liquidationcall) directly in the LendingPool contract.
2. By creating your own automated bot or system to liquidate loans.

{% hint style="danger" %}
For liquidation calls to be profitable, you must take into account the gas cost involved in liquidating the loan. If a high gas price is used, then the liquidation may be unprofitable for you. See the '[Calculating profitability vs gas cost](liquidations.md#calculating-profitability-vs-gas-cost)' section for more details.
{% endhint %}

## 0. Prerequisites

When making a `liquidationCall()`, you must:

* Know the account (i.e. the ethereum address: `user`) whose health factor is below 1.
* Know the valid debt amount (`debtToCover`) and debt asset (`debt`) that can be paid.&#x20;
  * The close factor is 0.5, which means that only a maximum of 50% of the debt can be liquidated per valid `liquidationCall()`.
  * As mentioned [here](../the-core-protocol/lendingpool/#liquidationcall), you can set the `debtToCover` to `uint(-1)` and the protocol will proceed with the highest possible liquidation allowed by the close factor.
  * You must already have a sufficient balance of the debt asset, which will be used by the `liquidationCall()` to pay back the debts.
* Know the collateral asset (`collateral`)  you are closing. I.e. the collateral asset that the user has 'backing' their outstanding loan that you will partly receive as a 'bonus'.
* Whether you want to receive aTokens or the underlying asset (`receiveAToken`) after a successful `liquidationCall()`.

## 1. Getting accounts to liquidate

Only user accounts that have a health factor below 1 can be liquidated. There are multiple ways you can get the health factor, with most of them involving 'user account data'.

{% hint style="info" %}
"Users" in the Aave Protocol refer to a single ethereum address that has interacted with the protocol. This can be an externally owned account or contract.
{% endhint %}

### On-chain

1. To gather user account data from on-chain data, one way would be to monitor emitted events from the protocol and keep an up to date index of user data locally.
   1. Events are emitted each time a user interacts with the protocol (deposit, repay, borrow, etc). See the [contract source code](https://github.com/aave/protocol-v2/blob/master/contracts/protocol/lendingpool/LendingPool.sol) for relevant events.
2. When you have the user's address, you can simply call [`getUserAccountData()`](../the-core-protocol/lendingpool/#getuseraccountdata) to read the user's current `healthFactor`. If the `healthFactor` is below 1, then the account can be liquidated.

### GraphQL

1. Similarly to the sections above, you will need to gather user account data and keep an index of the user data locally.
2. Since GraphQL does not provide real time calculated user data such as the `healthFactor`, you will need to compute this yourself. The easiest way is to use the [Aave.js](https://github.com/aave/aave-js) package, which has methods to compute summary user data.
   1. The data you will need to pass into the Aave.js method's can be fetched from [our subgraph](../getting-started/using-graphql.md), namely the `UserReserve` objects.

## 2. Executing the liquidation call

Once you have the account(s) to liquidate, you will need to calculate the amount of collateral that _can_ be liquidated:

1. Use [`getUserReserveData()`](../the-core-protocol/protocol-data-provider/#getreservedata) on the [Protocol Data Provider ](../the-core-protocol/protocol-data-provider/)contract (for Solidity) or the `UserReserve` object (for GraphQL) with the relevant parameters.
2.  Max debt that can be cleared by single liquidation call is given by the current close factor (which is 0.5 currently).

    `debtToCover = (userStableDebt + userVariableDebt) * LiquidationCloseFactorPercent`

    1. You can also pass in `type(uint).max` as the `debtToCover` in [liquidationCall()](../the-core-protocol/lendingpool/#liquidationcall) to liquidate the maximum amount allowed.
3.  For reserves that have `usageAsCollateralEnabled` as `true`, the current [liquidation bonus](https://docs.aave.com/risk/asset-risk/risk-parameters) gives the max amount of collateral that need to be liquidated to cover debt 👇🏻

    `maxAmountOfCollateralToLiquidate = (debtAssetPrice * debtToCover * liquidationBonus)/ collateralPrice`

### Solidity

Below is an example contract. When making the `liquidationCall()` to the LendingPool contract, your contract **must** already have at least  `debtToCover` of `debt`.

{% tabs %}
{% tab title="Liquidator.sol" %}
```javascript
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "./ILendingPoolAddressesProvider.sol";
import "./ILendingPool.sol";


contract Liquidator {

    address constant lendingPoolAddressProvider = INSERT_LENDING_POOL_ADDRESS

    function myLiquidationFunction(
        address _collateral, 
        address _reserve,
        address _user,
        uint256 _purchaseAmount,
        bool _receiveaToken
    )
        external
    {
        ILendingPoolAddressesProvider addressProvider = ILendingPoolAddressesProvider(lendingPoolAddressProvider);
  
        ILendingPool lendingPool = ILendingPool(addressProvider.getLendingPool());
        
        require(IERC20(_reserve).approve(address(lendingPool), _purchaseAmount), "Approval error");

        // Assumes this contract already has `_purchaseAmount` of `_reserve`.
        lendingPool.liquidationCall(_collateral, _reserve, _user, _purchaseAmount, _receiveaToken);
    }
}
```
{% endtab %}

{% tab title="ILendingPoolAddressesProvider.sol" %}
```javascript
pragma solidity ^0.6.6;

interface ILendingPoolAddressesProvider {
    function getLendingPool() external view returns (address);
}
```
{% endtab %}

{% tab title="ILendingPool.sol" %}
```javascript
pragma solidity ^0.6.6;

interface ILendingPool {
  function liquidationCall ( address _collateral, address _reserve, address _user, uint256 _purchaseAmount, bool _receiveAToken ) external payable;
}
```
{% endtab %}
{% endtabs %}

### Javascript/Python

A similar call can be made with a package such as Web3.js/web.py. The account making the call must already have at least the `debtToCover` of `debt`.

{% tabs %}
{% tab title="JavaScript" %}
```javascript
// Import the ABIs, see: https://docs.aave.com/developers/developing-on-aave/deployed-contract-instances
import DaiTokenABI from "./DAItoken.json"
import LendingPoolAddressesProviderABI from "./LendingPoolAddressesProvider.json"
import LendingPoolABI from "./LendingPool.json"

// ... The rest of your code ...

// Input variables
const collateralAddress = 'THE_COLLATERAL_ASSET_ADDRESS'
const daiAmountInWei = web3.utils.toWei("1000", "ether").toString()
const daiAddress = '0x6B175474E89094C44Da98b954EedeAC495271d0F' // mainnet DAI
const user = 'USER_ACCOUNT'
const receiveATokens = true

const lpAddressProviderAddress = '0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5' // mainnet
const lpAddressProviderContract = new web3.eth.Contract(LendingPoolAddressesProviderABI, lpAddressProviderAddress)

// Get the latest LendingPool contract address
const lpAddress = await lpAddressProviderContract.methods
    .getLendingPool()
    .call()
    .catch((e) => {
        throw Error(`Error getting lendingPool address: ${e.message}`)
    })

// Approve the LendingPool address with the DAI contract
const daiContract = new web3.eth.Contract(DAITokenABI, daiAddress)
await daiContract.methods
    .approve(
        lpAddress,
        daiAmountInWei
    )
    .send()
    .catch((e) => {
        throw Error(`Error approving DAI allowance: ${e.message}`)
    })

// Make the deposit transaction via LendingPool contract
const lpContract = new web3.eth.Contract(LendingPoolABI, lpAddress)
await lpContract.methods
    .liquidationCall(
        collateralAddress,
        daiAddress,
        user,
        daiAmountInWei,
        receiveATokens,
    )
    .send()
    .catch((e) => {
        throw Error(`Error liquidating user with error: ${e.message}`)
    })
```
{% endtab %}

{% tab title="Python" %}
```python
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider(PROVIDER_URL))

def loadAbi(abi):
  return json.load(open("./abis/%s"%(abi)))
  
def getContractInstance(address, abiFile):
  return w3.eth.contract(address, abi=loadAbi(abiFile))
  
def liquidate(user, liquidator, amount):

  allowance = dai.functions.allowance(user, lendingPool.address).call()

  # Approve lendingPool to spend liquidator's funds
  if allowance <= 0:
    tx = dai.functions.approve(lendingPool.address, amount).transact({
      "from": liquidator,
    })

  # Liquidation Call, collateral: weth and debt: dai
  lendingPool.functions.liquidationCall(
    weth.address,
    dai.address,
    user,
    amount,
    True
  ).transact({"from": liquidator})
  
dai = getContractInstance("0x6B175474E89094C44Da98b954EedeAC495271d0F", "DAI.json")
weth = getContractInstance("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "WETH.json")
lendingPoolAddressProvider = getContractInstance("0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5", "LENDING_POOL_PROVIDER.json")
lendingPool = getContractInstance(
    # Get address of latest lendingPool from lendingPoolAddressProvider
    lendingPoolAddressProvider.functions.getLendingPool().call(),
    "LENDING_POOL.json"
  )

liquidate(alice, bob, amount)
```
{% endtab %}
{% endtabs %}

## 3. Setting up a bot

Depending on your environment, preferred programming tools and languages, your bot should:

* Ensure it has enough (or access to enough) funds when liquidating.
* Calculate the profitability of liquidating loans vs gas costs, taking into account the most lucrative collateral to liquidate.
* Ensure it has access to the latest protocol user data.
* Have the usual fail safes and security you'd expect for any production service.

### Calculating profitability vs gas cost

One way to calculate the profitability is the following:

1. Store and retrieve each collateral's relevant details such as address, decimals used, and [liquidation bonus as listed here](https://docs.aave.com/risk/asset-risk/risk-parameters).&#x20;
2. Get the user's collateral balance (`aTokenBalance`).
3. Get the asset's price according to the [Aave's oracle contract](../the-core-protocol/price-oracle/) (`getAssetPrice()`).
4. The maximum collateral bonus you can receive will be the collateral balance (2) multiplied by the liquidation bonus (1) multiplied by the collateral asset's price in ETH (3). Note that for assets such as USDC, the number of decimals are different from other assets.
5. The maximum cost of your transaction will be your gas price multiplied by the amount of gas used. You should be able to get a good estimation of the gas amount used by calling `estimateGas` via your web3 provider.
6. Your approximate profit will be the value of the collateral bonus (4) minus the cost of your transaction (5).

## Appendix

### How is health factor calculated?

The health factor is calculated from: the user's collateral balance (in ETH) multiplied by the current liquidation threshold for all the user's outstanding assets, divided by 100, divided by the user's borrow balance and fees (in ETH). [More info here](https://docs.aave.com/risk/asset-risk/risk-parameters#health-factor).

This can be both calculated off-chain and on-chain, see [Aave.js](https://github.com/aave/aave-js/blob/master/src/index.tsx#L90) and the [GenericLogic library](https://github.com/aave/protocol-v2/blob/750920303e33b66bc29862ea3b85206dda9ce786/contracts/protocol/libraries/logic/GenericLogic.sol#L244) contract, respectively.

### How is liquidation bonus determined?

At the moment, liquidation bonuses are evaluated and determined by the risk team based on liquidity risk and [updated here](https://docs.aave.com/risk/asset-risk/risk-parameters).

This will change in the future with [Aave Protocol Governance](https://docs.aave.com/aavenomics/governance).

### Price oracles

Aave Protocol uses Chainlink as a price oracle, with a backup oracle in case of a Chainlink malfunction. See our [Price Oracle](../the-core-protocol/price-oracle/) section for more details.

The health factor of accounts is determined by the user's account data and the price of relevant assets, as last updated by the Price Oracle.

