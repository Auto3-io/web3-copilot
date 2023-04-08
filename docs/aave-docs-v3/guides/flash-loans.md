# Flash Loans

Flash Loans are special transactions that allow the borrowing of an asset, as long as the borrowed amount (and a fee) is returned before the end of the transaction (also called One Block Borrows). These transactions do not require a user to supply collateral prior to engaging in the transaction. There is no real world analogy to Flash Loans, so it requires some basic understanding of how state is managed within blocks in blockchains.

{% hint style="info" %}
Flash Loans are an advanced concept aimed at developers. You **must** have a good understanding of EVM, programming, and smart contracts to be able to use this feature.
{% endhint %}

## Overview

Flash-loan allows users to access liquidity of the pool (only for reserves for which borrow is enabled) for one transaction as long as the amount taken plus fee is returned or (if allowed) debt position is opened by the end of the transaction.

Aave V3 offers two options for flash loans:

* [`flashLoan`](../core-contracts/pool.md#flashloan): Allows borrower to access liquidity of _**multiple reserves**_ in single _flashLoan_ transaction. The borrower also has an option to open stable or variabled rate debt position backed by supplied collateral or credit delegation in this case.\
  NOTE: _flash loan fee_ is waived for approved `flashBorrowers` (managed by [ACLManager](../core-contracts/aclmanager.md))
* [`flashLoanSimple`](../core-contracts/pool.md#flashloansimple):  Allows borrower to access liquidity of _single reserve_ for the transaction. In this case flash loan fee is not waived nor can borrower open any debt position at the end of the transaction. This method is gas efficient for those trying take advantage of simple flash loan with single reserve asset.

### Execution Flow

For developers, a helpful mental model to consider when developing your solution:

1. Your contract calls the `Pool` contract, requesting a Flash Loan of a certain `amount(s)` of `reserve(s)` using [`flashLoanSimple()`](../core-contracts/pool.md#flashloansimple) or [`flashLoan()`](../core-contracts/pool.md#flashloan).
2. After some sanity checks, the `Pool` transfers the requested `amounts` of the `reserves` to your contract, then calls `executeOperation()` on `receiver` contract .
3. Your contract, now holding the flash loaned `amount(s)`, executes any arbitrary operation in its code.&#x20;
   * If you are performing a **flashLoanSimple**, then when your code has finished, you approve Pool for flash loaned amount + fee.
   * If you are performing **flashLoan,** then for all the reserves either depending on  `interestRateMode` passed for the asset, either the Pool must be approved for flash loaned amount + fee or must or sufficient collateral or credit delegation should be available to open debt position.
   * If the amount owing is not available (due to a lack of balance or approval or insufficient collateral for debt), then the transaction is reverted.
4. All of the above happens in 1 transaction (hence in a single ethereum block).



### Applications of Flash Loans

Aave Flash Loans are already used with Aave V3 for liquidity swap feature. Other examples in the wild include:

* Arbitrage between assets, without needing to have the principal amount to execute the arbitrage.
* Liquidating borrow positions, without having to repay the debt of the positions and using discounted collateral claimed to payoff flashLoan amount + fee.

### Flash loan fee

The flash loan fee is initialized at deployment to 0.09% and can be updated via Governance Vote. Use [`FLASHLOAN_PREMIUM_TOTAL`](../core-contracts/pool.md#flashloan\_premium\_total) to get current value.

Flashloan fee can be shared by the LPs (liquidity providers) and the protocol treasury. The `FLASHLOAN_PREMIUM_TOTAL` represents the total fee paid by the borrowers of which:

* Fee to LP: `FLASHLOAN_PREMIUM_TOTAL - FLASHLOAN_PREMIUM_TO_PROTOCOL`
* Fee to Protocol: `FLASHLOAN_PREMIUM_TO_PROTOCOL`

{% hint style="info" %}
At initialization, `FLASHLOAN_PREMIUM_TO_PROTOCOL` is set to 0.
{% endhint %}

## Step by step

### 1. Setting Up

Your contract that receives the flash loaned amounts **must** conform to the [IFlashLoanSimpleReceiver.sol](https://github.com/aave/aave-v3-core/blob/master/contracts/flashloan/interfaces/IFlashLoanSimpleReceiver.sol) or [IFlashLoanReceiver.sol](https://github.com/aave/aave-v3-core/blob/master/contracts/flashloan/interfaces/IFlashLoanReceiver.sol) interface by implementing the relevant `executeOperation()` function.

Also note that since the owed amounts will be _pulled_ from your contract, your contract must give allowance to the `Pool` to pull those funds to pay back the flash loan amount + premiums.

### 2. Calling flashLoan() or flashLoanSimple()

To call either of the two flash loan methods on the Pool, we need to pass in the relevant parameters. There are 3 ways you can do this.

1.  #### From an EOA ('normal' ethereum account)

    To use an EOA, send a transaction to the relevant `Pool` calling the `flashLoan()` or `flashLoanSimple()` function. See [Pool api docs](../core-contracts/pool.md) for parameter details, ensuring you use your contract address from [step 1](flash-loans.md#1.-setting-up) for the `receiverAddress`.\

2.  #### From a different contract

    Similar to sending a transaction from an EOA as above, ensure the `receiverAddress` is your contract address from [step 1](flash-loans.md#1.-setting-up).\

3.  #### From the _same_ contract

    If you want to use the same contract as in step 1, use `address(this)` for the `receiverAddress` parameter in the flash loan method.

{% hint style="danger" %}
Never keep funds permanently on your `FlashLoanReceiverBase` contract as they could be exposed to a ['griefing' attack](https://ethereum.stackexchange.com/a/92457/19365), where the stored funds are used by an attacker.
{% endhint %}

### Completing the flash loan

Once you have performed your logic with the flash loaned assets (in your `executeOperation()` function), you will need to pay back the flash loaned amounts if you used `flashLoanSimple() or` `interestRateMode=0` in `flashLoan()`for any of the assets in `modes` parameter.

*   #### Paying back a flash loaned asset

    Ensure your contract has the relevant amount + premium to payback the borrowed asset. You can calculate this by taking the sum of the relevant entry in the `amounts` and `premiums` array passed into the `executeOperation()` function.\


    You **do not** need to transfer the owed amount back to the `Pool`. The funds will be automatically _pulled_ at the conclusion of your operation.
*   #### Incurring a debt (i.e. not immediately paying back)

    If you initially used a `mode=1` or `mode=2` for any of the assets in the `modes` parameter, then the address passed in for `onBehalfOf` will incur the debt **if** the `onBehalfOf` address has previously approved the `msg.sender` to incur debts on their behalf.

    This means that you can have some assets that are paid back immediately, while other assets incur a debt.
