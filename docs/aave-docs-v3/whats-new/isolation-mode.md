# Isolation Mode

Isolation mode allows to list new assets as _**Isolated**_ which has a specific debt ceiling and can be only used to borrow stablecoins that have been permitted, by Aave Governance, to be borrowable in isolation mode.

{% hint style="info" %}
Debt Ceiling for an \*Isolated Asset\* is represented as the maximum amount in USD that can be borrowed against the collateral with two decimals of precision.
{% endhint %}

## Supply Isolated Asset

A user can supply an _Isolated Asset_ just like any other asset using `supply()` method in pool.sol, though, the default behaviour while supplying an _Isolated Asset_ may vary based on below conditions

| Use as Collateral | Condition                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Enabled           | <p>- if Isolated Asset is the first asset supplied by the user<br>OR<br>- no other supplied asset is enabled as collateral by the user</p> |
| Disabled          | if any other asset is currently enabled as collateral                                                                                      |

{% hint style="info" %}
In case the user has other assets enabled as collateral, they can still supply _Isolated Asset_ to capture the yield but won’t be able to use it as collateral
{% endhint %}

## Borrow in Isolated Mode

Borrowers using an _Isolated Asset_ as collateral can only use that particular asset as collateral and can only borrow assets that are _borrowable in isolation mode,_ i.e. have `BORROWABLE_IN_ISOLATION_MASK` bit set in reserve configuration.

{% hint style="info" %}
Borrower in Isolation Mode cannot enable any other assets including the other isolated assets as collateral.
{% endhint %}

## Exit Isolation Mode

Users can turn off isolation mode by disabling the isolated asset as collateral. This can be done only if the user has no outstanding debt. A user must use `repay()` method in Pool.sol to pay off all of their debt before exiting Isolation Mode
