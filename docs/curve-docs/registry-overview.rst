.. _overview:


========
Registry
========

The Curve registry contracts are open source and may be `found on Github <https://github.com/curvefi/curve-pool-registry>`_.

The registry is comprised of the following contracts:

* ``AddressProvider``: Address provider for registry contracts. This contract is immutable and it's address will never change. On-chain integrators should always use this contract to fetch the current address of other registry components.
* ``Registry``: The main registry contract. Used to locate pools and query information about them as well as registered coins.
* ``PoolInfo``: Aggregate getter methods for querying large data sets about a single pool. Designed for off-chain use.
* ``Swaps``: The registry exchange contract. Used to find pools and query exchange rates for token swaps. Also provides a unified exchange API that can be useful for on-chain integrators.
