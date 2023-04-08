.. _factory-deployer:

=======================================
Metapool Factory: Deployer and Registry
=======================================

The ``Factory`` contract is used to deploy new Curve pools and to find existing ones. It is deployed to the mainnet at the following address:

    `0xB9fC157394Af804a3578134A6585C0dc9cc990d4 <https://etherscan.io/address/0xB9fC157394Af804a3578134A6585C0dc9cc990d4>`_

Source code for this contract is may be viewed on `Github <https://github.com/curvefi/curve-factory/blob/master/contracts/Factory.vy>`_.

.. _factory-deployer-deployment:

.. warning::

    Please carefully review the :ref:`limitations <factory-deployer-limitations>` of the factory prior to deploying a new pool. Deploying a pool using an incompatible token could result in permanent losses to liquidity providers and/or traders. Factory pools cannot be killed and tokens cannot be rescued from them!

Deploying a Pool
================

.. py:function:: Factory.deploy_metapool(_base_pool: address, _name: String[32], _symbol: String[10], _coin: address, _A: uint256, _fee: uint256) -> address: nonpayable

    Deploys a new metapool.

    * ``_base_pool``: Address of the :ref:`base pool <factory-deployer-base-pools>` to use within the new metapool.
    * ``_name``: Name of the new metapool.
    * ``_symbol``: Symbol for the new metapool's LP token. This value will be concatenated with the base pool symbol.
    * ``_coin``: Address of the coin being used in the metapool
    * ``_A``: :ref:`Amplification coefficient <factory-deployer-A>`
    * ``_fee``: :ref:`Trade fee <factory-deployer-fee>`, given as an integer with 1e10 precision.

    Returns the address of the newly deployed pool.

        .. code-block:: python

            >>> factory = Contract('0xB9fC157394Af804a3578134A6585C0dc9cc990d4')
            >>> esd = Contract('0x36F3FD68E7325a35EB768F1AedaAe9EA0689d723')
            >>> threepool = Contract('0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7')

            >>> tx = factory.deploy_metapool(threepool, "Empty Set Dollar", "ESD", esd, 10, 4000000, {'from': alice})
            Transaction sent: 0x2702cfc4b96be1877f853c246be567cbe8f80ef7a56348ace1d17c026bc31b68
              Gas price: 20 gwei   Gas limit: 1100000   Nonce: 9

            >>> tx.return_value
            "0xFD9f9784ac00432794c8D370d4910D2a3782324C"

    .. note::

        After deploying a pool, you must also :ref:`add initial liquidity <factory-pools-add-liquidity>` before the pool can be used.

.. _factory-deployer-limitations:

Limitations
-----------

* The token within the new pool must expose a ``decimals`` method and use a maximum of 18 decimal places.
* The token's ``transfer`` and ``transferFrom`` methods must revert upon failure.
* Successful token transfers must move exactly the specified number of tokens between the sender and receiver. Tokens that take a fee upon a successful transfer may cause the pool to break or act in unexpected ways.
* Token balances must not change without a transfer. Rebasing tokens are not supported!
* Pools deployed by the factory cannot be paused or killed.
* Pools deployed by the factory are not eligible for CRV rewards.

.. _factory-deployer-base-pools:

Base Pools
----------

A metapool pairs a coin against the LP token of another pool. This other pool is referred to as the "base pool". By using LP tokens, metapools allow swaps against any asset within their base pool, without diluting the base pool's liquidity.

The factory allows deployment of metapools that use the following base pools:

* `3pool <https://www.curve.fi/3pool>`_ (USD denominated assets): `0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7 <https://etherscan.io/address/0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7>`_
* `sBTC <https://www.curve.fi/sbtc>`_ (BTC denominated assets): `0x7fC77b5c7614E1533320Ea6DDc2Eb61fa00A9714 <https://etherscan.io/address/0x7fC77b5c7614E1533320Ea6DDc2Eb61fa00A9714>`_

It is possible to enable additional base pools through a DAO vote.

.. _factory-deployer-A:

Choosing an Amplification Coefficient
-------------------------------------

The amplification co-efficient ("A") determines a pool's tolerance for imbalance between the assets within it. A higher value means that trades will incure slippage sooner as the assets within the pool become imbalanced.

The appropriate value for A is dependent upon the type of coin being used within the pool. We recommend the following values:

* Uncollateralized algorithmic stablecoins: 5-10
* Non-redeemable, collateralized assets: 100
* Redeemable assets: 200-400

It is possible to modify the amplification coefficient for a pool after it has been deployed. However, it requires a vote within the Curve DAO and must reach a 15% quorum.

.. _factory-deployer-fee:

Trade fees
----------

Curve pools charge a fee for token exchanges and when adding or removing liquidity in an imbalanced manner. 50% of the fees are given to liquidity providers, 50% are distributed to veCRV holders.

For factory pools, the size of the fee is set at deployment. The minimum fee is 0.04% (represented as ``4000000``). The maximum fee is 1% (``100000000``). The fee cannot be changed after a pool has been deployed.

Finding Pools
=============

The following getter methods are available for finding pools that were deployed via the factory:

.. py:function:: Factory.pool_count() -> uint256: view

    Returns the total number of pools that have been deployed by the factory.

.. py:function:: Factory.pool_list(i: uint256) -> address: view

    Returns the n'th entry in a zero-indexed array of deployed pools. Returns ``ZERO_ADDRESS`` when ``i`` is greater than the number of deployed pools.

    Note that because factory-deployed pools are not killable, they also cannot be removed from the registry. For this reason the ordering of pools within this array will never change.

.. py:function:: Factory.find_pool_for_coins(_from: address, _to: address, i: uint256 = 0) -> address: view

    Finds a pool that allows for swaps between ``_from`` and ``_to``. You can optionally include ``i`` to get the i-th pool, when multiple pools exist for the given pairing.

    The order of ``_from`` and ``_to`` does not affect the result.

    Returns ``ZERO_ADDRESS`` when swaps are not possible for the pair or ``i`` exceeds the number of available pools.

        .. code-block:: python

            >>> esd = Contract('0x36F3FD68E7325a35EB768F1AedaAe9EA0689d723')
            >>> usdc = Contract('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48')

            >>> factory.find_pool_for_coins(esd, usdc)
            '0xFD9f9784ac00432794c8D370d4910D2a3782324C'

Getting Pool Info
=================

The factory has a similar API to that of the main Registry, which can be used to query information about existing pools.

Coins and Coin Info
-------------------

.. py:function:: Factory.get_n_coins(pool: address) -> uint256[2]: view

    Get the number of coins and underlying coins within a pool.

        .. code-block:: python

            >>> factory.get_n_coins('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            (2, 4)

.. py:function:: Factory.get_coins(pool: address) -> address[2]: view

    Get a list of the swappable coins within a pool.

        .. code-block:: python

            >>> factory.get_coins('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            ("0x36F3FD68E7325a35EB768F1AedaAe9EA0689d723", "0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490")

.. py:function:: Factory.get_underlying_coins(pool: address) -> address[8]: view

    Get a list of the swappable underlying coins within a pool.

        .. code-block:: python

            >>> factory.get_underlying_coins('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            ("0x36F3FD68E7325a35EB768F1AedaAe9EA0689d723", "0x6B175474E89094C44Da98b954EedeAC495271d0F", "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "0xdAC17F958D2ee523a2206206994597C13D831ec7", "0x0000000000000000000000000000000000000000", "0x0000000000000000000000000000000000000000", "0x0000000000000000000000000000000000000000", "0x0000000000000000000000000000000000000000")

.. py:function:: Factory.get_decimals(pool: address) -> uint256[8]: view

    Get a list of decimal places for each coin within a pool.

        .. code-block:: python

            >>> factory.get_decimals('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            (18, 18, 0, 0, 0, 0, 0, 0)

.. py:function:: Factory.get_underlying_decimals(pool: address) -> uint256[8]: view

    Get a list of decimal places for each underlying coin within a pool.

    For pools that do not involve lending, the return value is identical to :func:`Registry.get_decimals <Registry.get_decimals>`.  Non-lending coins that still involve querying a rate (e.g. renBTC) are marked as having ``0`` decimals.

        .. code-block:: python

            >>> factory.get_underlying_decimals('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            (18, 18, 6, 6, 0, 0, 0, 0)

.. py:function:: Factory.get_coin_indices(pool: address, _from: address, _to: address) -> (int128, int128, bool): view

    Convert coin addresses into indices for use with pool methods.

    Returns the index of ``_from``, index of ``_to``, and a boolean indicating if the coins are considered underlying in the given pool.

        .. code-block:: python

            >>> factory.get_coin_indices('0xFD9f9784ac00432794c8D370d4910D2a3782324C', '0xdac17f958d2ee523a2206206994597c13d831ec7', '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48')
            (2, 1, True)

    Based on the above call, we know:

        * the index of the coin we are swapping out of is ``2``
        * the index of the coin we are swapping into is ``1``
        * the coins are considred underlying, so we must call ``exchange_underlying``

    From this information we can perform a token swap:

        .. code-block:: python

            >>> swap = Contract('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            >>> swap.exchange_underlying(2, 1, 1e18, 0, {'from': alice})


Balances and Rates
******************

.. py:function:: Factory.get_balances(pool: address) -> uint256[2]: view

    Get available balances for each coin within a pool.

    These values are not necessarily the same as calling ``Token.balanceOf(pool)`` as the total balance also includes unclaimed admin fees.

        .. code-block:: python

            >>> factory.get_balances('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            (11428161394428689823275227, 47831326741306)

.. py:function:: Factory.get_underlying_balances(pool: address) -> uint256[8]: view

    Get balances for each underlying coin within a pool.

        .. code-block:: python

            >>> factory.get_underlying_balances('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            (11876658145799734093379928, 48715210997790596223520238, 46553896776332824101242804, 49543896565857325657915396, 0, 0, 0, 0)

.. py:function:: Factory.get_admin_balances(pool: address) -> uint256[2]: view

    Get the current admin balances (uncollected fees) for a pool.

        .. code-block:: python

            >>> factory.get_admin_balances('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            (10800690926373756722358, 30891687335)

.. py:function:: Factory.get_rates(pool: address) -> uint256[2]: view

    Get the exchange rates between coins and underlying coins within a pool, normalized to a ``1e18`` precision.

        .. code-block:: python

            >>> factory.get_rates('0xFD9f9784ac00432794c8D370d4910D2a3782324C')
            (1000000000000000000, 1018479293504725874)
