# DelegationAwareAToken

The special type of aToken that are minted and burned upon supply and withdraw of assets that has voting power associated _(which can be delegated)_ with them. These _aTokens_ are enabled to delegate voting power of the underlying asset to a different address.

_DelegationAwareAToken_ enables/implements all the methods available for aTokens with additional [`delegateUnderlyingTo`](delegationawareatoken.md#delegateunderlyingto) method.

Refer [_aToken_](atoken.md) docs for full list of contract api

### delegateUnderlyingTo

`function delegateUnderlyingTo(address delegatee)`

Delegates voting power of the underlying asset to a `delegatee` address.

{% hint style="danger" %}
This method can only be called by `POOL_ADMIN.`
{% endhint %}
