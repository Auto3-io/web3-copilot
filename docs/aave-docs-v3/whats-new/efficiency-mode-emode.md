# Efficiency Mode (eMode)

## Efficiency Mode (eMode)

The High Efficiency mode feature (or "eMode") is designed to maximise capital efficiency when collateral and borrowed assets are correlated in price.

The `RISK_ADMINS` and `POOL_ADMIN`, set by Aave Governance, can configure a maximum of 255 eMode categories, with each `EModeCategory` having following _risk management parameters_:

* LTV (Loan to value)
* Liquidation threshold
* Liquidation bonus
* A custom price oracle (optional)

{% hint style="info" %}
💡 Category 0 is reserved as the default non-eMode category. All the assets listed on Aave V3, by default have category 0 (which indicates the standard operational mode).
{% endhint %}

All Assets listed on Aave V3 can be set to any of the pre-configured `eModeCategory` by the `RISK_ADMINS` or `POOL_ADMIN`.

{% hint style="info" %}
The correct categorisation is not enforced on-chain and needs to be maintained by the `RISK_ADMINS` and `POOL_ADMINS` selected via the Aave Governance vote.
{% endhint %}

eMode also offers the possibility of introducing a specific price oracle for a certain category.

## How it works?

If the user has supplied liquidity to the protocol, the user `eMode` category is set to 0 by default.

The protocol allows user to set the user eMode category to any of the `eModeCategories` configured by the `PoolConfigurator` given the following conditions holds true:

* all the borrowed assets of the user are in the chosen category.
* changing eMode doesn’t leave user position under-collateralised
