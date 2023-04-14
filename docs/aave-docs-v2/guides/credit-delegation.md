# Credit Delegation

Native Credit Delegation (**CD**) is a new feature in Aave v2. It allows a depositor to deposit funds in the protocol to earn interest, and delegate borrowing power (i.e. their credit) to other users. The enforcement of the loan and its terms are agreed upon between the depositor and borrowers, which can be either off-chain via legal agreements or on-chain via smart contracts.&#x20;

This enables:

* The depositor (delegator) to earn extra yield on top of the yield they already earn from the protocol,
* The borrowers (delegatees) to access an uncollateralized loan.

Follow the below steps to create your first Credit Delegation.

{% hint style="info" %}
TL;DR: A **starter** example contract can be found on [Kovan etherscan](https://kovan.etherscan.io/address/0x0006e96F380C62C2fdCff37C26aBA16293DBaEcD#code) and [Github code examples repo](https://github.com/aave/code-examples-protocol/tree/main/V2/Credit%20Delegation), with a [twitter discussion here](https://twitter.com/daveytea/status/1333807980509278211).
{% endhint %}

{% hint style="warning" %}
In the following guide, we refer to `borrower` and `delegatee`. However credit delegation allows the delegation to **multiple users,** so it can also be read as `borrowers` and `delegatees`.
{% endhint %}

## Approving the delegation

The [`approveDelegation()`](../the-core-protocol/debt-tokens/#approvedelegation) method must be called by the depositor (delegator), approving the borrower (delegatee) a certain amount.&#x20;

This is done for each debt token that needs to be delegated.

{% hint style="warning" %}
The depositor (delegator) does not need to already have deposited funds in the protocol to `approveDelegation()`. However, **before** the borrower (delegatee) executes `borrow()`, there must be sufficient collateral assigned to the depositor (delegator) in the protocol.
{% endhint %}

{% tabs %}
{% tab title="Solidity" %}
```javascript
// Import relevant interfaces
import './IAaveProtocolDataProvider.sol';
import './IDebtToken.sol';

// ... beginning of your contract. Constructors etc...

// Within a relevant function in your contract:

    // Get the Protocol Data Provider
    IAaveProtocolDataProvider provider = IAaveProtocolDataProvider(address(INSERT_DATA_PROVIDER_ADDRESS));
  
    // Get the relevant debt token address
    (, address stableDebtTokenAddress, address variableDebtTokenAddress) = provider.getReserveTokensAddresses(INSERT_ASSET_ADDRESS);

    // Relevant details for credit delegation
    address borrower = address(INSERT_BORROWER_ADDRESS);
    uint256 amountInWei = INSERT_DELEGATED_AMOUNT;
    
    // For stable debt tokens
    IDebtToken(stableDebtTokenAddress).approveDelegation(borrower, amountInWei);
    
    // For variable debt tokens
    IDebtToken(variableDebtTokenAddress).approveDelegation(borrower, amountInWei);

```
{% endtab %}

{% tab title="Web3.js" %}
```javascript
// Import relevant ABIs
import IAaveProtocolDataProviderABI from './IAaveProtocolDataProviderAbi.json'
import IDebtTokenABI from './IDebtToken.json'

// ... beginning of your code

// Within a relevant function in your code:

    // Get the Aave Protocol Data Provider
    const provider = new web3.eth.Contract(IAaveProtocolDataProviderABI, INSERT_DATA_PROVIDER_ADDRESS)

    // Get the relevant debt token address
    const tokenDetails = await provider.methods
        .getReserveTokensAddresses(INSERT_ASSET_ADDRESS)
        .call()
        .catch((e) => {
            throw Error(`Error getting token details: ${e.message}`)
        })
    
    // Relevant details for credit delegation
    const borrower = INSERT_BORROWER_ADDRESS
    const amountInWei = INSERT_DELEGATED_AMOUNT
    
    // For stable debt tokens
    const stableDebtContract = new web3.eth.Contract(IDebtTokenABI, tokenDetails.stableDebtTokenAddress)
    await stableDebtContract.methods
        .approveDelegation(borrower, amountInWei)
        .send()
        .catch((e) => {
            throw Error(`Error approving delegation: ${e.message}`)
        })
    
    // For variable debt tokens
    const variableDebtContract = new web3.eth.Contract(IDebtTokenABI, tokenDetails.variableDebtTokenAddress)
    await variableDebtContract.methods
        .approveDelegation(borrower, amountInWei)
        .send()
        .catch((e) => {
            throw Error(`Error approving delegation: ${e.message}`)
        })

```
{% endtab %}
{% endtabs %}

## Borrowing the credit

The borrower (delegatee) calls the [`borrow()`](../the-core-protocol/lendingpool/#borrow) method on the `LendingPool`, using the depositor's (delegator's) address in final parameter `onBehalfOf`.

The borrower's available credit is reduced by the borrowed amount.

{% tabs %}
{% tab title="Solidity" %}
```javascript
// Import relevant interfaces
import './IAddressesProvider.sol';
import './ILendingPool.sol';

// ... beginning of your contract. Constructors etc...

// Within a relevant function in your contract:

    // Get the latest LendingPool contract for the relevant market
    IAddressesProvider provider = IAddressesProvider(address(INSERT_ADDRESSES_PROVIDER_ADDRESS));
    ILendingPool lendingPool = ILendingPool(provider.getLendingPool());
    
    // Borrow the relevant amount
    address assetToBorrow = address(INSERT_ASSET_ADDRESS); // E.g. the address for Dai
    uint256 amountToBorrowInWei = INSERT_AMOUNT; // must be equal to or less than the amount delegated to the borrower
    uint256 interestRateMode = INSERT_INTEREST_RATE_MODE; // must be of the same type as the debt token that is delegated. I.e. stable = 1, variable = 2.
    uint16 referralCode = INSERT_REFERRAL_CODE;
    address delegatorAddress = INSERT_DELEGATOR_ADDRESS;
    
    lendingPool.borrow(assetToBorrow, amountToBorrowInWei, interestRateMode, referralCode, delegatorAddress);
    
```
{% endtab %}

{% tab title="Web3.js" %}
```javascript
// Import relevant ABIs
import IAddressProviderABI from './IAddressesProviderAbi.json'
import ILendingPoolABI from './ILendingPool.json'

// ... beginning of your code

// Within a relevant function in your code:

    // Get the latest LendingPool contract for the relevant market
    const provider = new web3.eth.Contract(IAddressProviderABI, INSERT_ADDRESSES_PROVIDER_ADDRESS)
    const lendingPoolAddress = await provider.methods
        .getLendingPool()
        .call()
        .catch((e) => {
            throw Error(`Error getting lendingPool address: ${e.message}`)
        })
    const lendingPoolContract = new web3.eth.Contract(ILendingPoolABI, lendingPoolAddress)
    
    // Borrow the relevant amount
    const assetToBorrow = INSERT_ASSET_ADDRESS; // E.g. the address for Dai
    const amountToBorrowInWei = INSERT_AMOUNT; // must be equal to or less than the amount delegated to the borrower
    const interestRateMode = INSERT_INTERST_RATE_MODE; // must be of the same type as the debt token that is delegated. I.e. stable = 1, variable = 2.
    const referralCode = INSERT_REFERRAL_CODE;
    const delegatorAddress = INSERT_DELEGATOR_ADDRESS;
    
    await lendingPoolContract.methods
        .borrow(
            assetToBorrow,
            amountToBorrowInWei,
            interestRateMode,
            referralCode,
            delegatorAddress
        )
        .send()
        .catch((e) => {
            throw Error(`Error borrowing: ${e.message}`)
        })

```
{% endtab %}
{% endtabs %}

## Repaying the credit

The borrower (delegatee) can also call [`repay()`](../the-core-protocol/lendingpool/#repay) at anytime to repay their uncollateralized loan, passing in the depositor's (delegator's) address as the final parameter `onBehalfOf`.

There is no change to the borrower's available credit after repayment.

{% tabs %}
{% tab title="Solidity" %}
```javascript
// Import relevant interfaces
import './IAddressesProvider.sol';
import './ILendingPool.sol';
import './IERC20.sol';

// ... beginning of your contract. Constructors etc...

// Within a relevant function in your contract:

// Get the latest LendingPool contract for the relevant market
IAddressesProvider provider = IAddressesProvider(address(INSERT_ADDRESSES_PROVIDER_ADDRESS));
ILendingPool lendingPool = ILendingPool(provider.getLendingPool());

// Approve the asset to be repaid  
address assetToRepay = address(INSERT_ASSET_ADDRESS); // E.g. the address for Dai
uint256 amountToRepayInWei = INSERT_AMOUNT; // must be equal to or less than the amount delegated to the borrower

IERC20(assetToRepay).approve(address(lendingPool), amounToRepayInWei);

// Repay the relevant amount
uint256 interestRateMode = INSERT_INTEREST_RATE_MODE; // must be of the same type as the debt token that is delegated. I.e. stable = 1, variable = 2.
address delegatorAddress = INSERT_DELEGATOR_ADDRESS;

lendingPool.repay(assetToRepay, amountToRepayInWei, interestRateMode, delegatorAddress);
    
```
{% endtab %}

{% tab title="Web3.js" %}
```javascript
// Import relevant ABIs
import IAddressProviderABI from './IaddressesProviderAbi.json'
import ILendingPoolABI from './ILendingPool.json'
import IERC20ABI from './IERC20.json'

// ... beginning of your code

// Within a relevant function in your code:

// Get the latest LendingPool contract for the relevant market
const provider = new web3.eth.Contract(IAddressProviderABI, INSERT_ADDRESSES_PROVIDER_ADDRESS)
const lendingPoolAddress = await provider.methods
    .getLendingPool()
    .call()
    .catch((e) => {
        throw Error(`Error getting lendingPool address: ${e.message}`)
    })
const lendingPoolContract = new web3.eth.Contract(ILendingPoolABI, lendingPoolAddress)

const assetToRepay = INSERT_ASSET_ADDRESS; // E.g. the address for Dai
const amountToRepayInWei = INSERT_AMOUNT; // must be equal to or less than the amount delegated to the borrower
const delegatorAddress = INSERT_DELEGATOR_ADDRESS;

// Approve the asset to be repaid
const assetContract = new web3.eth.Contract(IERC20ABI, assetToRepay)
await assetContract.methods
  .approve(provider, amountToRepayInWei)
  .send()
  .catch((e) => {
    throw Error(`Error approving asset allowance: ${e.message}`)
  })

const lendingPoolContract = new web3.eth.Contract(ILendingPoolABI, lendingPoolAddress)
await lendingPoolContract.methods
  .repay(
			assetToRepay, 
			amountToRepayInWei, 
			delegatorAddress
	)
  .send()
  .catch((e) => {
    throw Error(`Error repaying: ${e.message}`)
  })

```
{% endtab %}
{% endtabs %}

## Increasing the credit delegation

To increase or decrease a borrower's available credit, the [`approveDelegation()`](../the-core-protocol/debt-tokens/#approvedelegation) method should be called again. This sets that new amount available to borrow **on top of** (not including) outstanding borrows.&#x20;

This is done for each debt token that requires a modification.

{% tabs %}
{% tab title="Solidity" %}
```javascript
// Import relevant interfaces
import './IAaveProtocolDataProvider.sol';
import './IDebtToken.sol';

// ... beginning of your contract. Constructors etc...

// Within a relevant function in your contract:

    // Get the Protocol Data Provider
    IAaveProtocolDataProvider provider = IAaveProtocolDataProvider(address(INSERT_DATA_PROVIDER_ADDRESS));
  
    // Get the relevant debt token address
    (, address stableDebtTokenAddress, address variableDebtTokenAddress) = provider.getReserveTokensAddresses(INSERT_ASSET_ADDRESS);

    // Relevant details for credit delegation
    address borrower = address(INSERT_BORROWER_ADDRESS);
    uint256 amountInWei = INSERT_DELEGATED_AMOUNT; // This is the total amount to be delegated (not just the increase)
    
    // For stable debt tokens
    IDebtToken(stableDebtTokenAddress).approveDelegation(borrower, amountInWei);
    
    // For variable debt tokens
    IDebtToken(variableDebtTokenAddress).approveDelegation(borrower, amountInWei);

```
{% endtab %}

{% tab title="Web3.js" %}
```javascript
// Import relevant ABIs
import IAaveProtocolDataProviderABI from './IAaveProtocolDataProviderAbi.json'
import IDebtTokenABI from './IDebtToken.json'

// ... beginning of your code

// Within a relevant function in your code:

    // Get the Aave Protocol Data Provider
    const provider = new web3.eth.Contract(IAaveProtocolDataProviderABI, INSERT_DATA_PROVIDER_ADDRESS)

    // Get the relevant debt token address
    const tokenDetails = await provider.methods
        .getReserveTokensAddresses(INSERT_ASSET_ADDRESS)
        .call()
        .catch((e) => {
            throw Error(`Error getting token details: ${e.message}`)
        })
    
    // Relevant details for credit delegation
    const borrower = INSERT_BORROWER_ADDRESS
    const amountInWei = INSERT_DELEGATED_AMOUNT // This is the total amount to be delegated (not just the increase)
    
    // For stable debt tokens
    const stableDebtContract = new web3.eth.Contract(IDebtTokenABI, tokenDetails.stableDebtTokenAddress)
    await stableDebtContract.methods
        .approveDelegation(borrower, amountInWei)
        .send()
        .catch((e) => {
            throw Error(`Error approving delegation: ${e.message}`)
        })
    
    // For variable debt tokens
    const variableDebtContract = new web3.eth.Contract(IDebtTokenABI, tokenDetails.variableDebtTokenAddress)
    await variableDebtContract.methods
        .approveDelegation(borrower, amountInWei)
        .send()
        .catch((e) => {
            throw Error(`Error approving delegation: ${e.message}`)
        })

```
{% endtab %}
{% endtabs %}

## Checking the amount delegated

To check the current allowance of a user, simply call [`borrowAllowance()`](../the-core-protocol/debt-tokens/#borrowallowance) passing in the depositor (delegator) and borrower (delegatee) addresses.

This is done for each debt token that is delegated.

{% tabs %}
{% tab title="Solidity" %}
```javascript
// Import relevant interfaces
import './IAaveProtocolDataProvider.sol';
import './IDebtToken.sol';

// ... beginning of your contract. Constructors etc...

// Within a relevant function in your contract:

    // Get the Protocol Data Provider
    IAaveProtocolDataProvider provider = IAaveProtocolDataProvider(address(INSERT_DATA_PROVIDER_ADDRESS));
  
    // Get the relevant debt token address
    (, address stableDebtTokenAddress, address variableDebtTokenAddress) = provider.getReserveTokensAddresses(INSERT_ASSET_ADDRESS);

    // Relevant details for credit delegation
    address delegator = address(INSERT_DEPOSITOR_ADDRESS)
    address delegatee = address(INSERT_BORROWER_ADDRESS);
    
    // For stable debt tokens
    uint256 stableAllowance = IDebtToken(stableDebtTokenAddress).borrowAllowance(delegator, delegatee);
    
    // For variable debt tokens
    uint256 variableAllowance = IDebtToken(variableDebtTokenAddress).borrowAllowance(delegator, delegatee);

```
{% endtab %}

{% tab title="Web3.js" %}
```javascript
// Import relevant ABIs
import IAaveProtocolDataProviderABI from './IAaveProtocolDataProviderAbi.json'
import IDebtTokenABI from './IDebtToken.json'

// ... beginning of your code

// Within a relevant function in your code:

    // Get the Aave Protocol Data Provider
    const provider = new web3.eth.Contract(IAaveProtocolDataProviderABI, INSERT_DATA_PROVIDER_ADDRESS)

    // Get the relevant debt token address
    const tokenDetails = await provider.methods
        .getReserveTokensAddresses(INSERT_ASSET_ADDRESS)
        .call()
        .catch((e) => {
            throw Error(`Error getting token details: ${e.message}`)
        })
    
    // Relevant details for credit delegation
    const delegator = INSERT_DEPOSITOR_ADDRESS
    const delegatee = INSERT_BORROWER_ADDRESS
    
    // For stable debt tokens
    const stableDebtContract = new web3.eth.Contract(IDebtTokenABI, tokenDetails.stableDebtTokenAddress)
    const stableAllowance = await stableDebtContract.methods
        .borrowAllowance(delegator, delegatee)
        .call()
        .catch((e) => {
            throw Error(`Error approving delegation: ${e.message}`)
        })
    
    // For variable debt tokens
    const variableDebtContract = new web3.eth.Contract(IDebtTokenABI, tokenDetails.variableDebtTokenAddress)
    const variableAllowance = await variableDebtContract.methods
        .borrowAllowance(delegator, delegatee)
        .call()
        .catch((e) => {
            throw Error(`Error approving delegation: ${e.message}`)
        })

```
{% endtab %}
{% endtabs %}

