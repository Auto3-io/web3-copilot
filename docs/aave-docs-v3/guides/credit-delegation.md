# Credit Delegation

Credit delegation allows a depositor to deposit funds in the protocol to earn interest, and delegate borrowing power (i.e. their credit) to other users. The enforcement of the loan and its terms are agreed upon between the depositor and borrowers, which can be either off-chain via legal agreements or on-chain via smart contracts.

This enables:

* The supplier (aka delegator) to earn extra yield on top of the yield they already earn from the protocol,
* The borrowers (aka delegatees) to access an uncollateralized loan.

{% hint style="warning" %}
Borrow by _delegatee_ must be consistent with _delegator_ [eMode](../whats-new/efficiency-mode-emode.md) category. \
For eg. if a delegator eMode category is `STABLECOINS`, then&#x20;

* delegator can only borrow `STABLECOINS` eMode category asset.&#x20;
* in case _delegator_ approve credit to _delegatee_ for non `STABLECOINS`category (for eg. weth), then borrow would revert.
{% endhint %}

{% hint style="danger" %}
The _delegatee_ cannot abuse credit approval to liquidate _delegator_ i.e. if the borrow puts _delegator's_ position in HF < `HEALTH_FACTOR_LIQUIDATION_THRESHOLD`, then borrow will fail.
{% endhint %}

## Approving the delegation

The [`approveDelegation()`](../tokens/debttoken.md#approvedelegation) or [`delegationWithSig()`](../tokens/debttoken.md#delegationwithsig) must be called by the supplier (delegator), approving the borrower (delegatee) a certain amount.

This is done for each debt token that needs to be delegated.

{% hint style="info" %}
The delegator does not need to already have supplied funds in the protocol to `approveDelegation()`. However, **before** the delegatee executes `borrow()`, there must be sufficient collateral supplied by delegator in the protocol.
{% endhint %}

## Borrowing the credit

The borrower (delegatee) calls the [`borrow()`](broken-reference) method on the `Pool`, using the supplier's (delegator's) address in final parameter `onBehalfOf`.

The borrower's available credit is reduced by the borrowed amount.

## Repaying the credit

Anyone can repay the debt _OnBehalf_ of the user, by calling one of the methods - [repay()](../core-contracts/pool.md#repay) or [repayWithPermit()](../core-contracts/pool.md#repaywithpermit). The supplier (aka creditor) can also use [repayWithATokens()](../core-contracts/pool.md#repaywithatokens) method to repay  debt with their _aTokens_ of the underlying debt asset in the same pool.
