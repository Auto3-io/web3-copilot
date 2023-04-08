# AMPL on Aave Caveats

The AMPL token supply automatically rebases in response to the demand. When price is high, wallet balances increase. When price is low, wallet balances decrease. These rebases effects the user's AMPL balance in the Aave markets.

{% hint style="info" %}
On every rebase the available liquidity of the pool changes but the borrowed liquidity remains same.
{% endhint %}

## Depositing AMPL

On depositing `AMPL` in Aave [LendingPool ](../the-core-protocol/lendingpool/)the user gets `aAMPL`. The available liquidity balance of the pool (ie. `suppliedLiquidity - borrowedLiquidity`) changes when the underlying asset gets rebased. Hence, the aToken balance of the depositors is affected on the AMPL rebase depending on the utilisation rate of the pool.

## Borrowing AMPL

AMPL borrow amount remains fixed ie. debt token balance does not change on underlying asset rebase. Hence, the debt denominated in AMPL remains fixed, while the value of that debt expressed in terms of purchasing power tends toward price-stability.
