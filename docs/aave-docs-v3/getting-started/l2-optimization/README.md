# L2 Optimization

The main transaction cost on L2 comes from calldata. To minimize this cost, Aave V3 uses slightly different L2 Contracts, on Arbitrum and Optimism, that compress the info passed to Pool methods.

Below are the contracts introduced for L2 optimization:

* ****[**L2Pool**](l2pool.md): Contract for L2 optimized user facing methods that takes byte encoded input arguments.
* **CalldataLogic**: Library contract used to decode the byte32 arguments passed to the L2Pool.
* ****[**L2Encoder**](l2encoder.md): Helper contract which has view methods to encode data to be passed to L2Pool.

{% hint style="info" %}
Pool methods not exposed in L2Pool.sol (such as flashLoan, setUserEMode etc.) are same on L2 as on other versions of protocol. Refer [Pool](../../core-contracts/pool.md) docs for rest of the methods.&#x20;
{% endhint %}
