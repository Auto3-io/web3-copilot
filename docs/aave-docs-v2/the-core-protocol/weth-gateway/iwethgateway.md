# IWETHGateway

Also available on [Github](https://github.com/aave/protocol-v2/blob/master/contracts/misc/interfaces/IWETHGateway.sol).

{% tabs %}
{% tab title="IWETHGateway.sol" %}
```javascript

// SPDX-License-Identifier: agpl-3.0
pragma solidity 0.6.12;

interface IWETHGateway {
  function depositETH(
    address lendingPool,
    address onBehalfOf,
    uint16 referralCode
  ) external payable;

  function withdrawETH(
    address lendingPool,
    uint256 amount,
    address onBehalfOf
  ) external;

  function repayETH(
    address lendingPool,
    uint256 amount,
    uint256 rateMode,
    address onBehalfOf
  ) external payable;

  function borrowETH(
    address lendingPool,
    uint256 amount,
    uint256 interesRateMode,
    uint16 referralCode
  ) external;

}

```
{% endtab %}
{% endtabs %}
