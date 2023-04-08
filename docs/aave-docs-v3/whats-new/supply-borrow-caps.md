# Supply Borrow Caps

## Supply/Borrow Caps

Aave Governance can appoint `RISK_ADMIN` and `POOL_ADMIN` who have the ability to configure Borrow and Supply Caps of the individual reserves.

## **Borrow Caps**

Allow modulation of how much of each asset can be borrowed, which reduces insolvency risk.

By default borrow cap of an asset is 0, which signifies no cap. Anyone who has been granted `RISK_ADMIN` or `POOL_ADMIN` role via the ACLManager can call [`setBorrowCap` method in PoolConfigurator](../core-contracts/poolconfigurator.md#write-methods) to update the max total borrow (stable + variable) for the given reserve.

{% hint style="info" %}
In case \*Borrow Cap\* of the reserve is set lower than the current \*totalDebt\* the existing borrowers are not effected but no more borrows (stable or variable) can be initiated for that reserve.
{% endhint %}

## **Supply Caps**

Allow limiting how much of a certain asset is supplied to the Aave protocol. This helps reducing exposure to a certain asset and mitigate attacks like infinite minting or price oracle manipulation.

By default supply cap of an asset is 0, which signifies no cap. Anyone who has been granted `RISK_ADMIN` or `POOL_ADMIN` role via the ACLManager can call [`setSupplyCap` method in PoolConfigurator](../core-contracts/poolconfigurator.md#write-methods) to update the liquidity supply for the given reserve.

{% hint style="info" %}
In case _Supply Cap_ of the reserve is set lower than the current liquidity of the reserve, the existing suppliers are not effected but no more liquidity can be supplied to that reserve.
{% endhint %}
